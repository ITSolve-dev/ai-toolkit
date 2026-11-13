"""Board arithmetic over a task-master snapshot, so no agent has to count.

    board_metrics.py snapshot.json [--settings workflow.toml] [--out metrics.json]
                     [--compare earlier-snapshot.json] [--window-start D --window-end D]
                     [--sprint NAME] [--age-at D]

Reads a snapshot written by snapshot.py (schema 1). --settings is the project's workflow settings
(TOML); from it the script uses [process.wip] (limits: a key is a status name or a kind name),
[process].sle ("<n> days at <p>%"), [process].timezone, [process].acceptance_headings and
[board.size] (the estimate scale, label = number). Each absent from settings that were given
means: no limits, the heading "Acceptance criteria", no SLE, UTC days, no estimates. Settings
given must hold a [process] with a valid setup ("this does not look like the project's workflow
settings" otherwise) and pass snapshot.py's validation (closed key sets). Without --settings
nothing is known about what the team
declared: the output says `settings.given: false` and every figure that needs the settings says
"no settings given (--settings)", never "none declared".

Every figure carries `basis`, saying what it was computed from:
  exact            - from history the tool reported (status_since, started_at, finished_at,
                     transitions)
  since_created    - age counted from created_at, because the tool reports no time in state;
                     a task stuck in a state looks the same as one long open
  created_at       - arrivals, from creation time (which is what created_at is)
  by_sprint_field  - velocity, from the sprint each finished item names now
  unknown          - no timestamp; the value is null
  not_computed     - the data does not support the figure; `reason` says what is missing
`updated_at` is never read as a start, finish or state change.

Scope: counts, wip, limits, throughput, arrivals, cycle_time, estimates, velocity and comparison
carry `scope_complete` (the snapshot's scope.complete: true, false or null) and `scope_reason`
(null only when the read was complete). A snapshot without a scope record is labelled unknown.
When the scope excludes finished work (scope.includes_finished false), throughput, cycle time (and
so sle, scatterplot, histogram), velocity and burndown refuse. comparison refuses when the two
snapshots were read with different queries or finished-work inclusion.

Abandoned: "delivered" is finished and not marked abandoned. A finished issue whose abandoned
marker cannot be read (null, or no markers) counts as delivered and is listed in
`abandoned_unknown` beside every figure that uses delivered work.

History-dependent figures need native history on the issues (see snapshot.py):
  cycle_time, sle, series.scatterplot, series.histogram - finished_at and a start on every
      finished item in scope. The start is the first transition into a started status; without
      transitions, started_at is the field a tool with native history must supply.
      status_since of a finished item is when it finished, not when it started.
  throughput, series.burndown - finished_at.
  series.cfd - transitions on every issue.
Transitions are trusted only when whole: the last one must be into the issue's current status,
and the first within 5 minutes after created_at (HISTORY_TOLERANCE); otherwise the history is cut
and the figures using it refuse. A transition into a status not in the mapping before the start
refuses cycle time too: a renamed or retired status may be where the work started.
Any item in scope lacking them makes the figure null with the reason; it is not computed from
the items that happen to have them.
Started statuses, decided per status: every active and handed_off status; a queued status only
when [process.wip] names it, or names the kind queued (then every queued status). They decide
what counts as WIP, which open items age marks `started`, where cycle time starts, and Work
Item Age; wip, age and cycle_time report them as started_statuses with started_reason.
Percentiles are nearest rank; one whose rank n cannot resolve (n < 100/(100-p): p50 needs 2,
p70 4, p85 7, p95 20) is null, with `percentile_reasons`. sle.small_sample is true below the
same bound for the SLE's probability.
Estimates: an issue's estimate is its label that is a key of [board.size], read as that key's
number, matched exactly; no such label is missing, two or more are unreadable (listed, never
guessed). estimates.case_mismatch lists [{id, label}] for issues without an estimate that carry
a label equal to a size key but for case.
Point sums (estimates.total, velocity points, burndown remaining) never count a missing estimate
as zero: velocity points are null when any finished item of the sprint lacks a readable one;
estimates and burndown carry `complete: false` beside the sum and list the items.

Window (--window-start/--window-end, ISO dates or times; a date-only end includes that day):
scopes throughput.window, arrivals.window and cycle time (items finished in the window).
--age-at: the reference time for age (a date-only value means the end of that day; at most
taken_at); the open items are still those open at taken_at.
--compare: net differences against an earlier snapshot (added, removed, status, kind, estimate,
sprint, mapping, and the forces in estimate units), the plan record where there is no history.
--sprint names the burndown's sprint; without it the one sprint whose state is "active".

Days: date-only bounds and per-day series use [process].timezone (a UTC offset such as "+03:00",
or an IANA name this Python knows), default UTC; the zone is named in each method. A timestamp
without a zone is read as UTC and counted in snapshot.naive_timestamps. Timestamps out of order
(after taken_at, a finish or start before creation) are listed in timestamp_problems.
Reference time for ages is the snapshot's taken_at (or --age-at), not the moment this runs.
Malformed input: exit 2, message on stderr, nothing on stdout.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
import tomllib
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

sys.path.insert(0, str(Path(__file__).resolve().parent))
from snapshot import (CATEGORY_KINDS, KINDS, SCHEMA, InputError, check_unique_ids, count_naive,  # noqa: E402
                      label_names, load_json, parse_time, validate_issue, validate_settings)

WIP_KINDS = ("active", "handed_off")
DEFAULT_HEADINGS = ["Acceptance criteria"]
UNMAPPED = "(unmapped)"
NO_STATUS = "(no status)"
NO_SETTINGS = "no settings given (--settings)"
HISTORY_TOLERANCE = timedelta(minutes=5)
CLOSED_STATES = {"closed", "complete", "completed"}
EXCLUDED = ("the read excluded finished work (scope.includes_finished is false): finished counts "
            "would read as zero")

ATX = re.compile(r"^\s{0,3}#{1,6}\s*(.*?)\s*#*\s*$")
WIKI = re.compile(r"^\s*h[1-6]\.\s*(.*?)\s*$")
BOLD = re.compile(r"^\s*(\*\*|__)(.+?)\1\s*:?\s*$")
SETEXT_RULE = re.compile(r"^\s*(=+|-+)\s*$")
OFFSET = re.compile(r"^([+-])(\d{2}):?(\d{2})$")


def load_settings(path):
    """None when no settings were given, which is not the same as empty ones."""
    if path is None:
        return None
    try:
        cfg = tomllib.loads(Path(path).read_text(encoding="utf-8"))
    except OSError as e:
        raise InputError(f"{path}: cannot read: {e}") from None
    except tomllib.TOMLDecodeError as e:
        raise InputError(f"{path}: malformed TOML: {e}") from None
    try:
        validate_settings(cfg, require_process=True)
    except InputError as e:
        raise InputError(f"{path}: {e}") from None
    return cfg


def process(cfg):
    return cfg.get("process") or {}


def validate_snapshot(snap):
    if not isinstance(snap, dict):
        raise InputError("snapshot: expected a JSON object")
    if snap.get("schema") != SCHEMA:
        raise InputError(f"snapshot: schema must be {SCHEMA}, got {snap.get('schema')!r}")
    for key in ("taken_at", "source", "issues", "mapping"):
        if key not in snap:
            raise InputError(f"snapshot: missing required field: {key}")
    if snap["source"] not in ("composed", "native"):
        raise InputError(f"snapshot: source must be composed or native, got {snap['source']!r}")
    if parse_time(snap["taken_at"], "snapshot: taken_at") is None:
        raise InputError("snapshot: taken_at may not be null")
    mapping = snap["mapping"]
    if not isinstance(mapping, dict) or not all(k in KINDS for k in mapping.values()):
        raise InputError(f"snapshot: mapping must map status names to {', '.join(KINDS)}")
    if snap.get("scope") is not None and not isinstance(snap["scope"], dict):
        raise InputError("snapshot: scope must be an object or null")
    if not isinstance(snap["issues"], list):
        raise InputError("snapshot: issues must be an array")
    for i, obj in enumerate(snap["issues"]):
        validate_issue(obj, f"issues[{i}]")
        if "kind" not in obj or (obj["kind"] is not None and obj["kind"] not in KINDS):
            raise InputError(f"issues[{i}]: kind must be one of {', '.join(KINDS)} or null; "
                             "was the snapshot made by snapshot.py?")
    check_unique_ids(snap["issues"], "snapshot: issues")
    sprints = snap.get("sprints")
    if sprints is not None and not isinstance(sprints, list):
        raise InputError("snapshot: sprints must be an array or null")
    if sprints and not all(isinstance(sp, dict) for sp in sprints):
        raise InputError("snapshot: each sprint must be an object")


# --- scope, days, settings -------------------------------------------------------------------

def scope_of(snap):
    sc = snap.get("scope")
    if sc is None:
        return {"recorded": False, "query": None, "complete": None, "includes_finished": None,
                "fetched": None, "reported_total": None}
    return {"recorded": True, "query": sc.get("query"), "complete": sc.get("complete"),
            "includes_finished": sc.get("includes_finished"), "fetched": sc.get("fetched"),
            "reported_total": sc.get("reported_total")}


def scope_reason(sc):
    if not sc["recorded"]:
        return ("the snapshot records no scope: whether the read was the whole board cannot be told; "
                "figures count only what was fetched")
    if sc["complete"] is True:
        return None
    if sc["complete"] is False:
        of = f" of {sc['reported_total']} reported" if sc["reported_total"] is not None else ""
        return (f"the read was not complete ({sc['fetched']} fetched{of}); figures count only what "
                "was fetched")
    return "the tool did not say whether the read was complete; figures count only what was fetched"


def label(fig, sc):
    fig["scope_complete"] = sc["complete"]
    fig["scope_reason"] = scope_reason(sc)
    return fig


def excluded(sc):
    return sc["includes_finished"] is False


def day_zone(cfg):
    """[process].timezone -> (tzinfo, label). Default UTC."""
    raw = process(cfg).get("timezone")
    if raw is None:
        return timezone.utc, "UTC"
    if not isinstance(raw, str):
        raise InputError(f"[process].timezone = {raw!r}: expected a string")
    if raw.upper() in ("UTC", "Z"):
        return timezone.utc, "UTC"
    m = OFFSET.match(raw)
    if m:
        delta = timedelta(hours=int(m.group(2)), minutes=int(m.group(3)))
        return timezone(-delta if m.group(1) == "-" else delta), f"UTC{raw}"
    try:
        return ZoneInfo(raw), raw
    except (ZoneInfoNotFoundError, ValueError):
        raise InputError(f"[process].timezone = {raw!r}: not a UTC offset (\"+03:00\") or a time zone "
                         "this Python knows (IANA names on Windows need the tzdata package; give an "
                         "offset)") from None


def parse_bound(raw, where, tz):
    """-> (aware datetime, date_only). A date-only value is midnight in the day zone."""
    if isinstance(raw, str):
        try:
            d = date.fromisoformat(raw)
        except ValueError:
            d = None
        if d is not None:
            return datetime.combine(d, time(), tzinfo=tz), True
    return parse_time(raw, where), False


def _next_midnight(t, tz):
    return datetime.combine(t.astimezone(tz).date() + timedelta(days=1), time(), tzinfo=tz)


def status_name(obj):
    return obj["status"]["name"] if obj["status"]["name"] is not None else NO_STATUS


def tally(items, key):
    out = {}
    for obj in items:
        k = key(obj)
        out[k] = out.get(k, 0) + 1
    return out


def idlist(ids):
    return {"count": len(ids), "ids": ids}


def shown(ids):
    return ", ".join(map(str, ids[:20])) + (" ..." if len(ids) > 20 else "")


# --- counts ----------------------------------------------------------------------------------

def counts(issues):
    mapped = [o for o in issues if o["kind"] is not None]
    return {
        "total": len(issues),
        "by_kind": tally(mapped, lambda o: o["kind"]),
        "unmapped": len(issues) - len(mapped),
        "by_status": tally(issues, status_name),
        "basis": "count of issues in the snapshot (see scope_complete)",
    }


def wip_table(cfg):
    table = process(cfg).get("wip")
    if table is not None and not isinstance(table, dict):
        raise InputError("[process.wip] must be a table")
    return table


class Started:
    """Which statuses count as started. Per status, not per kind: active and handed_off always;
    a queued status only when [process.wip] names it, or names the kind queued (then every queued
    status)."""

    def __init__(self, cfg, mapping, issues):
        table = wip_table(cfg) or {}
        self.keys = set(table)
        self.all_queued = "queued" in table
        pairs = dict(mapping)
        for o in issues:
            if o["status"]["name"] is not None and o["kind"] is not None:
                pairs.setdefault(o["status"]["name"], o["kind"])
        self.statuses = sorted(n for n, k in pairs.items() if self.of(n, k))
        queued = sorted(n for n, k in pairs.items() if k == "queued" and self.of(n, k))
        if self.all_queued:
            self.reason = "active and handed_off statuses, and every queued status: [process.wip] limits the kind queued"
        elif queued:
            self.reason = (f"active and handed_off statuses, and the queued status(es) [process.wip] "
                           f"limits ({', '.join(queued)})")
        else:
            self.reason = "active and handed_off statuses; no queued status is limited in [process.wip]"

    def of(self, status, kind):
        if kind in WIP_KINDS:
            return True
        return kind == "queued" and (self.all_queued or status in self.keys)

    def issue(self, o):
        return self.of(o["status"]["name"], o["kind"])

    def out(self):
        return {"started_statuses": self.statuses, "started_reason": self.reason}


def wip(issues, st):
    started = [o for o in issues if st.issue(o)]
    by_assignee, unassigned, not_read = {}, [], []
    for o in started:
        if "assignees" not in o:
            not_read.append(o["id"])
            continue
        people = o["assignees"] or []
        if not people:
            unassigned.append(o["id"])
        for p in people:
            key = (p.get("name") or p.get("id")) if isinstance(p, dict) else p
            key = str(key) if key is not None else "(unnamed)"
            by_assignee[key] = by_assignee.get(key, 0) + 1
    return {
        "total": len(started),
        "by_kind": tally(started, lambda o: o["kind"]),
        "by_status": tally(started, status_name),
        "by_assignee": by_assignee,
        "unassigned": idlist(unassigned),
        "assignees_not_read": idlist(not_read),
        **st.out(),
        "basis": "issues in a started status (started_statuses, why in started_reason); unmapped issues are "
                 "not counted. by_assignee: an item with several assignees counts once for each, so it "
                 "may sum above total; unassigned: assignees [] or null (null is the board holding no "
                 "value, per the normalized issue); assignees_not_read: the read carried no assignees "
                 "key, so who holds it is unknown",
    }


def limits(issues, snap, cfg, given):
    if not given:
        return {"declared": None, "breaches": None, "unknown_keys": None,
                "basis": f"{NO_SETTINGS}: whether the team keeps limits cannot be told"}
    table = wip_table(cfg)
    if table is None:
        return {"declared": False, "breaches": [], "unknown_keys": [],
                "basis": "no [process.wip] in settings"}
    statuses = set(snap.get("mapping") or {}) | set(snap.get("unmapped_statuses") or [])
    statuses |= {o["status"]["name"] for o in issues if o["status"]["name"] is not None}
    by_kind = tally(issues, lambda o: o["kind"])
    by_status = tally(issues, lambda o: o["status"]["name"])
    breaches, unknown = [], []
    for key, n in table.items():
        if not isinstance(n, int) or isinstance(n, bool) or n < 1:
            raise InputError(f"[process.wip] {key!r} = {n!r}: a limit must be a positive integer")
        if key in KINDS:
            scope, count = "kind", by_kind.get(key, 0)
        elif key in statuses:
            scope, count = "status", by_status.get(key, 0)
        else:
            unknown.append(key)
            continue
        if count > n:
            breaches.append({"key": key, "scope": scope, "limit": n, "count": count})
    return {"declared": True, "breaches": breaches, "unknown_keys": unknown,
            "basis": "count of issues in the status, or of the kind, against [process.wip]; "
                     "a key that is a kind name is read as a kind"}


# --- history ---------------------------------------------------------------------------------

NAMELESS = "(no name, category "


def _state(name, category):
    """A status as a trail entry: its name, or for a status the board gives no name, its category."""
    return name if name is not None else f"{NAMELESS}{category})"


def kind_of(mapping, st):
    if st.startswith(NAMELESS):
        return CATEGORY_KINDS.get(st[len(NAMELESS):-1])
    return mapping.get(st)


def _trail(o):
    return sorted(((parse_time(t["at"], f"issue {o['id']}: transitions"), t["at"],
                    _state(t["status"], t.get("category"))) for t in o["transitions"]),
                  key=lambda x: x[0])


def history_gap(o):
    """Why the issue's transitions are not a whole history, or None."""
    if not o.get("transitions"):
        return None
    tr = _trail(o)
    if tr[-1][2] != _state(o["status"]["name"], o["status"].get("category")):
        return (f"transitions end in {tr[-1][2]!r} but the issue is in {o['status']['name']!r}: the "
                "history is cut at the end")
    created = parse_time(o["created_at"], f"issue {o['id']}: created_at")
    if created is None:
        return "created_at is null: whether the transitions start at creation cannot be told"
    if tr[0][0] > created + HISTORY_TOLERANCE:
        return (f"the first transition ({tr[0][1]}) is more than 5 minutes after created_at "
                f"({o['created_at']}): the history is cut at the front")
    return None


def start_of(o, started, mapping):
    """-> (raw ISO start, source, problem). From transitions when the tool gave them: the first
    entry into a started status; otherwise the tool's own started_at. `problem` says
    why transitions present cannot give a start that can be trusted."""
    if o.get("transitions"):
        gap = history_gap(o)
        if gap:
            return None, None, gap
        unmapped = []
        for _, raw, st in _trail(o):
            kind = kind_of(mapping, st)
            if kind is None:
                unmapped.append(st)
            elif started.of(st, kind):
                if unmapped:
                    return None, None, (f"transition(s) into {', '.join(map(repr, dict.fromkeys(unmapped)))} "
                                        "before its start are not in the mapping; a renamed or retired "
                                        "status may be where the work started")
                return raw, "transitions", None
        if unmapped:
            return None, None, (f"no transition into a started status, and {', '.join(map(repr, dict.fromkeys(unmapped)))} "
                                "is not in the mapping")
        return None, None, None
    if o.get("started_at") is not None:
        return o["started_at"], "started_at", None
    return None, None, None


def timestamp_problems(issues, taken):
    items = []
    for o in issues:
        oid = o["id"]
        created = parse_time(o["created_at"], f"issue {oid}: created_at")
        for key in ("created_at", "status_since", "started_at", "finished_at"):
            t = parse_time(o.get(key), f"issue {oid}: {key}")
            if t is not None and t > taken:
                items.append({"id": oid, "field": key, "problem": "after taken_at"})
        trans = o.get("transitions") or []
        if any(parse_time(t["at"], f"issue {oid}: transitions") > taken for t in trans):
            items.append({"id": oid, "field": "transitions", "problem": "after taken_at"})
        if created is None:
            continue
        for key in ("started_at", "finished_at"):
            t = parse_time(o.get(key), f"issue {oid}: {key}")
            if t is not None and t < created - HISTORY_TOLERANCE:
                items.append({"id": oid, "field": key, "problem": "before created_at"})
        if trans and _trail(o)[0][0] < created - HISTORY_TOLERANCE:
            items.append({"id": oid, "field": "transitions", "problem": "before created_at"})
    return {"count": len(items), "items": items,
            "basis": "timestamps out of order, used as given; an age or period involving them may be "
                     "wrong. After taken_at often means --taken-at was earlier than the reads"}


# --- age -------------------------------------------------------------------------------------

def age(issues, ref, started, mapping):
    items, skipped = [], []
    for o in issues:
        if o["kind"] is None:
            skipped.append(o["id"])
            continue
        if o["kind"] == "finished":
            continue
        since = parse_time(o.get("status_since"), "status_since")
        created = parse_time(o["created_at"], "created_at")
        if since is not None:
            start, basis = since, "exact"
        elif created is not None:
            start, basis = created, "since_created"
        else:
            start, basis = None, "unknown"
        item = {"id": o["id"], "status": o["status"]["name"], "kind": o["kind"],
                "started": started.issue(o), "days": None, "basis": basis}
        if start is not None and start > ref:
            item.update(basis="unknown", reason=f"its {'status_since' if since else 'created_at'} is after "
                                                "the reference time")
        elif start is not None:
            item["days"] = round((ref - start).total_seconds() / 86400, 2)
        wia, wbasis, why = None, None, None
        if not item["started"]:
            why = "not started: its status is not in started_statuses"
        else:
            raw, src, problem = start_of(o, started, mapping)
            if raw is None:
                why = problem or ("no start time: neither transitions into a started status nor started_at "
                                  "from the tool")
            else:
                s = parse_time(raw, f"issue {o['id']}: start")
                if s > ref:
                    why = "started after the reference time"
                else:
                    wia, wbasis = round((ref - s).total_seconds() / 86400, 2), src
        item.update(work_item_age_days=wia, work_item_age_basis=wbasis, work_item_age_reason=why)
        items.append(item)
    return {"reference_time": None, "items": items, "skipped_unmapped": skipped, **started.out(),
            "basis": "every open mapped item; `started` marks those in a started status (started_statuses). "
                     "days: exact = time in current state from the tool's history; "
                     "since_created = days since created_at, not time in state; "
                     "unknown = no timestamp. work_item_age_days: days since the started point "
                     "(first transition into a started status, else the tool's started_at), null with "
                     "work_item_age_reason otherwise. Unmapped issues are skipped: open or not cannot "
                     "be told. With --age-at the open items are still those open at taken_at"}


# --- acceptance ------------------------------------------------------------------------------

def _norm(text):
    return text.strip().rstrip(":").strip().casefold()


def has_heading(description, headings):
    wanted = {_norm(h) for h in headings}
    lines = description.splitlines()
    for i, line in enumerate(lines):
        cands = []
        for rx, grp in ((ATX, 1), (WIKI, 1), (BOLD, 2)):
            m = rx.match(line)
            if m:
                cands.append(m.group(grp))
        if line.strip() and i + 1 < len(lines) and SETEXT_RULE.match(lines[i + 1]):
            cands.append(line)
        if any(_norm(c) in wanted for c in cands):
            return True
    return False


def acceptance(issues, cfg):
    proc = process(cfg)
    source = "settings" if "acceptance_headings" in proc else "default"
    headings = proc.get("acceptance_headings", DEFAULT_HEADINGS)
    if not isinstance(headings, list) or not headings or not all(isinstance(h, str) for h in headings):
        raise InputError("[process].acceptance_headings must be a non-empty list of strings")
    judged = [o for o in issues if o["kind"] not in (None, "finished")]
    skipped = [o["id"] for o in issues if o["kind"] is None]
    base = {"headings": headings, "headings_source": source, "skipped_unmapped": skipped}
    if judged and all(o["description"] is None for o in judged):
        return {**base, "items": None, "basis": "not_computed",
                "reason": "descriptions not read: every unfinished issue has a null description, which "
                          "a list read often leaves out; read the issues themselves"}
    items = []
    for o in judged:
        if not o["description"]:
            items.append({"id": o["id"], "status": o["status"]["name"], "reason": "no_description"})
        elif not has_heading(o["description"], headings):
            items.append({"id": o["id"], "status": o["status"]["name"], "reason": "no_heading"})
    return {**base, "items": items, "reason": None,
            "basis": "unfinished mapped issues whose description has no heading (Markdown #, underlined, "
                     "hN., or a bold line) named as one of `headings`; content under it is not judged. "
                     "Unmapped issues are skipped: finished or not cannot be told"}


# --- periods ---------------------------------------------------------------------------------

def period_bounds(sprint, taken, tz):
    """-> (start, end, open_period, skip_reason)."""
    name = sprint.get("name")
    start, _ = parse_bound(sprint.get("start_date"), f"sprint {name!r}: start_date", tz)
    end, end_date_only = parse_bound(sprint.get("end_date"), f"sprint {name!r}: end_date", tz)
    if end is not None and end_date_only:
        end += timedelta(days=1)  # a date-only end includes that whole day
        end = datetime.combine(end.date(), time(), tzinfo=tz)
    closed = str(sprint.get("state") or "").lower() in CLOSED_STATES
    if start is None:
        return None, None, None, "no start date"
    if end is None and closed:
        return None, None, None, "closed, but no end date: where it ended cannot be told"
    if start > taken:
        return start, None, None, "starts after taken_at: not started"
    open_period = end is None or end > taken
    return start, end if end is not None else taken, open_period, None


def no_sprints_reason(sprints):
    return "sprints not read: the snapshot has no sprints" if sprints is None else "the board has no sprints"


def delivered(issues):
    """-> (finished and not marked abandoned, ids among them whose abandoned marker is unreadable)."""
    out = [o for o in issues if o["kind"] == "finished"
           and (o.get("markers") or {}).get("abandoned") is not True]
    unknown = [o["id"] for o in out if (o.get("markers") or {}).get("abandoned") is None]
    return out, unknown


DELIVERED = ("finished issues not marked abandoned (a finished issue whose abandoned marker cannot be "
             "read counts as delivered and is listed in abandoned_unknown)")


def finish_gap(finished):
    lacking = [o["id"] for o in finished if o.get("finished_at") is None]
    if lacking:
        return (f"{len(lacking)} finished issue(s) have no finish time from the tool "
                f"({shown(lacking)}); updated_at is not a finish time")
    return None


def finished_time(o):
    return parse_time(o["finished_at"], f"issue {o['id']}: finished_at")


def throughput(issues, sprints, taken, tz, zone, sc):
    refuse = lambda reason: {"periods": None, "reason": reason, "basis": "not_computed"}
    if excluded(sc):
        return refuse(EXCLUDED)
    finished, unknown = delivered(issues)
    gap = finish_gap(finished)
    if gap:
        return refuse(gap)
    if not sprints:
        return refuse(no_sprints_reason(sprints))
    periods, skipped = [], []
    placed = set()
    for sp in sprints:
        start, end, open_period, skip = period_bounds(sp, taken, tz)
        if skip:
            skipped.append({"sprint": sp.get("name"), "reason": skip})
            continue
        ids = [o["id"] for o in finished if start <= finished_time(o) < end]
        placed.update(ids)
        periods.append({"sprint": sp.get("name"), "start": sp.get("start_date"),
                        "end": sp.get("end_date"), "finished": len(ids), "open_period": open_period})
    if not periods:
        return refuse("no sprint in the snapshot can be placed in time: "
                      + "; ".join(f"{s['sprint']}: {s['reason']}" for s in skipped))
    return {"periods": periods, "skipped_sprints": skipped,
            "finished_outside_periods": len([o for o in finished if o["id"] not in placed]),
            "abandoned_unknown": idlist(unknown),
            "reason": None,
            "basis": "exact",
            "method": f"{DELIVERED}, counted by the tool's finished_at within each sprint's dates "
                      f"(days in {zone}; a date-only end includes that day); an open period runs to "
                      "taken_at; a closed sprint without an end date, or one not yet started, is skipped"}


PERCENTILES = (50, 70, 85, 95)
NO_WINDOW = "no window given (--window-start/--window-end)"


def parse_window(window, tz):
    """(start, end) strings -> {start, end, from, to}; a date-only end includes that day."""
    if window is None:
        return None
    s_raw, e_raw = window
    start, _ = parse_bound(s_raw, "window start", tz)
    end, end_date_only = parse_bound(e_raw, "window end", tz)
    if start is None or end is None:
        raise InputError("a window needs both --window-start and --window-end")
    if end_date_only:
        end = datetime.combine(end.date() + timedelta(days=1), time(), tzinfo=tz)
    if end <= start:
        raise InputError(f"window: end {e_raw!r} is not after start {s_raw!r}")
    return {"start": s_raw, "end": e_raw, "from": start, "to": end}


def in_window(t, win):
    return win["from"] <= t < win["to"]


def window_info(win):
    return {"start": win["start"], "end": win["end"]} if win else None


def window_throughput(issues, win, sc):
    if win is None:
        return {"finished": None, "ids": None, "reason": NO_WINDOW, "basis": "not_computed"}
    if excluded(sc):
        return {**window_info(win), "finished": None, "ids": None, "reason": EXCLUDED, "basis": "not_computed"}
    finished, unknown = delivered(issues)
    gap = finish_gap(finished)
    if gap:
        return {**window_info(win), "finished": None, "ids": None, "reason": gap, "basis": "not_computed"}
    ids = [o["id"] for o in finished if in_window(finished_time(o), win)]
    return {**window_info(win), "finished": len(ids), "ids": ids, "reason": None, "basis": "exact",
            "abandoned_unknown": idlist([i for i in unknown if i in ids]),
            "method": f"{DELIVERED} whose finished_at falls in the window"}


def num(text):
    x = float(text)
    return int(x) if x == int(x) else x


def rank_needed(p):
    return math.ceil(100 / (100 - p) - 1e-9) if p < 100 else math.inf


def percentiles(vals):
    n, pct, why = len(vals), {}, {}
    for p in PERCENTILES:
        need = rank_needed(p)
        if n < need:
            pct[str(p)] = None
            why[str(p)] = f"n={n} too small for p{p} (needs {need})"
        else:
            pct[str(p)] = vals[-(-p * n // 100) - 1]
    return pct, why


def cycle_time(issues, win, started, mapping, sc):
    def refuse(reason):
        return {"n": None, "percentiles": None, "items": None, "window": window_info(win),
                "reason": reason, "basis": "not_computed"}
    if excluded(sc):
        return refuse(EXCLUDED)
    finished, unknown = delivered(issues)
    gap = finish_gap(finished)
    if gap:
        return refuse(gap)
    if win:
        finished = [o for o in finished if in_window(finished_time(o), win)]
    if not finished:
        return refuse("no finished issues" + (" in the window" if win else ""))
    starts = {id(o): start_of(o, started, mapping) for o in finished}
    problems = [(o["id"], starts[id(o)][2]) for o in finished if starts[id(o)][2]]
    if problems:
        return refuse(f"{len(problems)} finished issue(s) have a history that cannot give a start: "
                      + "; ".join(f"{i}: {p}" for i, p in problems[:5]) + (" ..." if len(problems) > 5 else ""))
    lacking = [o["id"] for o in finished if starts[id(o)][0] is None]
    if lacking:
        return refuse(f"{len(lacking)} finished issue(s) have no start time: neither transitions into a "
                      f"started status ({', '.join(started.statuses)}) nor started_at from the tool ({shown(lacking)}); "
                      "status_since of a finished issue is when it finished, and updated_at is not a start")
    items = []
    for o in finished:
        raw, src, _ = starts[id(o)]
        s, f = parse_time(raw, f"issue {o['id']}: start"), finished_time(o)
        if f < s:
            raise InputError(f"issue {o['id']}: finished_at is before its start")
        items.append({"id": o["id"], "started_at": raw, "start_source": src,
                      "finished_at": o["finished_at"],
                      "days": round((f - s).total_seconds() / 86400, 2), "_f": f})
    items.sort(key=lambda x: x["_f"])
    for x in items:
        del x["_f"]
    vals = sorted(x["days"] for x in items)
    pct, why = percentiles(vals)
    ids = {x["id"] for x in items}
    return {"n": len(vals), "percentiles": pct, "percentile_reasons": why, "items": items,
            "window": window_info(win), "reason": None, "basis": "exact",
            **started.out(),
            "abandoned_unknown": idlist([i for i in unknown if i in ids]),
            "method": f"finished_at minus the start, in days, for {DELIVERED} (in the window, when one "
                      "is given); percentiles by nearest rank over n items, null where n cannot resolve "
                      "the rank. start_source transitions = first entry into a started status "
                      "(started_statuses); started_at = the tool's own start, used only without "
                      "transitions, which may not follow started_statuses"}


SLE_RX = re.compile(r"^\s*(\d+(?:\.\d+)?)\s*days?\s+at\s+(\d+(?:\.\d+)?)\s*%\s*$", re.IGNORECASE)


def sle(cfg, ct, given):
    raw = process(cfg).get("sle")
    base = {"declared": (raw is not None) if given else None, "sle": raw, "days": None,
            "probability": None, "n": None, "within": None, "share": None, "misses": None,
            "small_sample": None, "small_sample_reason": None}
    if raw is None:
        return {**base, "reason": NO_SETTINGS if not given else "no [process].sle in settings",
                "basis": "not_computed"}
    m = SLE_RX.match(raw) if isinstance(raw, str) else None
    if not m or not 0 < float(m.group(2)) <= 100:
        raise InputError(f"[process].sle = {raw!r}: expected \"<n> days at <p>%\"")
    days, prob = num(m.group(1)), num(m.group(2))
    base.update(days=days, probability=prob)
    if ct["n"] is None:
        return {**base, "reason": f"no cycle times: {ct['reason']}", "basis": "not_computed"}
    misses = [x["id"] for x in ct["items"] if x["days"] > days]
    within = ct["n"] - len(misses)
    need = rank_needed(prob)
    small = ct["n"] < need
    return {**base, "n": ct["n"], "within": within, "share": round(within / ct["n"], 4),
            "misses": misses, "small_sample": small,
            "small_sample_reason": f"n={ct['n']} is below {need} items, too few to test a {prob}% SLE"
                                   if small else None,
            "reason": None, "basis": "exact",
            "method": "share of the cycle_time items whose cycle time is at most the SLE's days; "
                      "compare it with the SLE's probability"}


def arrivals(issues, sprints, taken, win, tz, zone):
    lacking = [o["id"] for o in issues if o["created_at"] is None]
    if lacking:
        reason = (f"{len(lacking)} issue(s) have no created_at ({shown(lacking)}); "
                  "when they arrived cannot be told")
        return {"periods": None, "reason": reason,
                "window": {"arrived": None, "ids": None, "reason": reason}, "basis": "not_computed"}
    created = {o["id"]: parse_time(o["created_at"], f"issue {o['id']}: created_at") for o in issues}
    periods, skipped = [], []
    for sp in sprints or []:
        start, end, open_period, skip = period_bounds(sp, taken, tz)
        if skip:
            skipped.append({"sprint": sp.get("name"), "reason": skip})
            continue
        ids = [i for i, t in created.items() if start <= t < end]
        periods.append({"sprint": sp.get("name"), "start": sp.get("start_date"),
                        "end": sp.get("end_date"), "arrived": len(ids), "ids": ids,
                        "open_period": open_period})
    if periods:
        reason = None
    elif not sprints:
        reason = no_sprints_reason(sprints)
    else:
        reason = "no sprint in the snapshot can be placed in time: " + "; ".join(
            f"{s['sprint']}: {s['reason']}" for s in skipped)
    if win is None:
        wd = {"arrived": None, "ids": None, "reason": NO_WINDOW}
    else:
        ids = [i for i, t in created.items() if in_window(t, win)]
        wd = {**window_info(win), "arrived": len(ids), "ids": ids, "reason": None}
    return {"periods": periods or None, "skipped_sprints": skipped, "reason": reason, "window": wd,
            "basis": "created_at",
            "method": f"issues whose created_at falls in each sprint's dates or the window (days in "
                      f"{zone}); an issue that left the scope before this snapshot is not seen"}


# --- estimates ------------------------------------------------------------------------------

def size_scale(cfg):
    """[board.size] -> {label: number}, or None when the project keeps no estimates."""
    table = (cfg.get("board") or {}).get("size")
    return None if table is None else dict(table)


def read_estimate(o, scale):
    """-> (value, state), state one of ok, missing (no size label), unreadable (several). Missing is
    not zero."""
    found = [n for n in label_names(o["labels"]) if n in scale]
    if not found:
        return None, "missing"
    return (scale[found[0]], "ok") if len(found) == 1 else (None, "unreadable")


def no_size_reason(given):
    return NO_SETTINGS if not given else "no [board.size] in settings"


def estimates(issues, scale, given):
    if scale is None:
        return {"declared": False if given else None, "scale": None, "total": None, "by_kind": None,
                "with_estimate": None, "without_estimate": None, "unreadable": None, "complete": None,
                "case_mismatch": None,
                "reason": no_size_reason(given), "basis": "not_computed"}
    total, by_kind, ok, missing, bad, mismatch = 0, {}, 0, [], [], []
    folded = {k.casefold() for k in scale}
    for o in issues:
        v, state = read_estimate(o, scale)
        if state == "ok":
            ok += 1
            total += v
            if o["kind"] is not None:
                by_kind[o["kind"]] = by_kind.get(o["kind"], 0) + v
        else:
            (missing if state == "missing" else bad).append(o["id"])
            if state == "missing":
                mismatch += [{"id": o["id"], "label": n} for n in sorted(label_names(o["labels"]))
                             if n.casefold() in folded]
    none = ok == 0
    return {"declared": True, "scale": scale, "total": None if none else total,
            "by_kind": None if none else by_kind,
            "total_reason": "no issue has a readable estimate" if none else None,
            "with_estimate": ok, "without_estimate": idlist(missing), "unreadable": idlist(bad),
            "complete": not (missing or bad), "case_mismatch": mismatch,
            "reason": None, "basis": "estimate as the board holds it now",
            "method": "sum of estimates, each the number [board.size] gives the issue's size label; "
                      "total includes unmapped issues, by_kind does not. Issues without a size label, "
                      "or with more than one (unreadable), are counted apart, never as zero; complete is "
                      "false when any exists. Size labels match exactly; case_mismatch lists issues without "
                      "an estimate that carry a label equal to a size key but for case"}


def in_sprint(o, sp):
    ref = o.get("sprint")
    keys = {str(k) for k in (sp.get("name"), sp.get("id")) if k is not None}
    if isinstance(ref, dict):
        return any(str(ref[k]) in keys for k in ("name", "id") if ref.get(k) is not None)
    return ref is not None and str(ref) in keys


def sprint_label(ref):
    if isinstance(ref, dict):
        return ref.get("name") if ref.get("name") is not None else ref.get("id")
    return ref


def velocity(issues, sprints, reader, given, sc):
    if excluded(sc):
        return {"periods": None, "reason": EXCLUDED, "basis": "not_computed"}
    if not sprints:
        return {"periods": None, "reason": no_sprints_reason(sprints), "basis": "not_computed"}
    finished, unknown = delivered(issues)
    periods, placed = [], set()
    for sp in sprints:
        mine = [o for o in finished if in_sprint(o, sp)]
        placed.update(id(o) for o in mine)
        points, missing, bad = (0 if reader else None), [], []
        for o in mine if reader else []:
            v, state = read_estimate(o, reader)
            if state == "ok":
                points += v
            else:
                (missing if state == "missing" else bad).append(o["id"])
        lacking = missing + bad
        why = None
        if reader and lacking:
            points, why = None, (f"{len(lacking)} finished item(s) lack a readable estimate "
                                 f"({shown(lacking)}): a sum without them would be too low")
        periods.append({"sprint": sp.get("name"), "state": sp.get("state"), "start": sp.get("start_date"),
                        "end": sp.get("end_date"), "finished": len(mine), "points": points,
                        "points_reason": why,
                        "finished_without_estimate": idlist(missing) if reader else None,
                        "finished_estimate_unreadable": idlist(bad) if reader else None})
    return {"periods": periods,
            "points_reason": None if reader else f"{no_size_reason(given)}: velocity by count only",
            "finished_outside_sprints": idlist([o["id"] for o in finished if id(o) not in placed]),
            "abandoned_unknown": idlist(unknown),
            "reason": None, "basis": "by_sprint_field",
            "method": f"per sprint, {DELIVERED} whose sprint field names it, and the sum of their "
                      "estimates, null when any of them lacks a readable one. It reads the sprint each "
                      "item names now, not finish times: an item finished after its sprint closed and "
                      "carried to the next is counted in the sprint it now names"}


# --- comparison ------------------------------------------------------------------------------

def mapping_diff(old, new):
    if old == new:
        return None
    return {"added": {k: v for k, v in new.items() if k not in old},
            "removed": {k: v for k, v in old.items() if k not in new},
            "changed": [{"status": k, "from": old[k], "to": new[k]} for k in new
                        if k in old and old[k] != new[k]]}


def _force(objs, reader):
    ids, lacking, total = [], [], 0
    for o in objs:
        ids.append(o["id"])
        v, state = read_estimate(o, reader)
        if state == "ok":
            total += v
        else:
            lacking.append(o["id"])
    return {"points": None if lacking else total, "ids": ids, "without_estimate": lacking}


def forces(before, now, reader, given):
    names = ("completed", "abandoned", "added", "removed", "re_estimated", "residual")
    if reader is None:
        return {**dict.fromkeys(names), "kind_unknown": None,
                "reason": f"{no_size_reason(given)}: forces are in estimate units"}
    later = list(now.values())

    def was_finished(o):
        e = before.get(str(o["id"]))
        return e is not None and e["kind"] == "finished"
    abandoned = lambda o: (o.get("markers") or {}).get("abandoned") is True
    re_items, re_unknown, delta = [], [], 0
    for key, o in now.items():
        e = before.get(key)
        if e is None:
            continue
        (old, s1), (new, s2) = read_estimate(e, reader), read_estimate(o, reader)
        if s1 == "ok" and s2 == "ok":
            if old != new:
                re_items.append({"id": o["id"], "from": old, "to": new})
                delta += new - old
        elif s1 == "ok" or s2 == "ok":
            re_unknown.append(o["id"])
    return {
        "completed": _force([o for o in later if o["kind"] == "finished" and not abandoned(o)
                             and not was_finished(o)], reader),
        "abandoned": _force([o for o in later if o["kind"] == "finished" and abandoned(o)
                             and not was_finished(o)], reader),
        "added": _force([o for k, o in now.items() if k not in before], reader),
        "removed": _force([o for k, o in before.items() if k not in now], reader),
        "re_estimated": {"delta": delta, "ids": [x["id"] for x in re_items], "items": re_items,
                         "estimate_appeared_or_lost": re_unknown},
        "residual": _force([o for o in later if o["kind"] not in (None, "finished")], reader),
        "kind_unknown": [o["id"] for o in later if o["kind"] is None],
        "reason": None,
        "method": "estimate units between the two snapshots: completed = finished now (not abandoned) "
                  "and not finished before, valued now; abandoned likewise; added = in the later only, "
                  "valued now; removed = in the earlier only, valued then; re_estimated.delta = later "
                  "minus earlier over items with both readable; residual = unfinished now. An item may be "
                  "both added and completed. points is null when any item of the set lacks a readable "
                  "estimate (without_estimate); unmapped items are in kind_unknown only"}


def comparison(snap, earlier, reader, given, sc):
    if earlier is None:
        return {"made": False, "reason": "no earlier snapshot given (--compare)", "basis": "not_computed"}
    try:
        validate_snapshot(earlier)
    except InputError as e:
        raise InputError(f"earlier {e}") from None
    if parse_time(earlier["taken_at"], "earlier taken_at") > parse_time(snap["taken_at"], "taken_at"):
        raise InputError("--compare: the earlier snapshot was taken after this one")
    esc = scope_of(earlier)
    for k in ("query", "includes_finished"):
        if esc[k] != sc[k]:
            return {"made": False, "basis": "not_computed",
                    "reason": f"the two snapshots were read with different scopes ({k}: {esc[k]!r} then "
                              f"{sc[k]!r}); their difference would mix scope with change"}
    before = {str(o["id"]): o for o in earlier["issues"]}
    now = {str(o["id"]): o for o in snap["issues"]}
    changed = {"status_changed": [], "kind_changed": [], "kind_changed_by_mapping": [],
               "estimate_changed": [] if reader else None, "sprint_changed": []}
    for key, o in now.items():
        e = before.get(key)
        if e is None:
            continue
        same_status = e["status"]["name"] == o["status"]["name"]
        pairs = [("status_changed", e["status"]["name"], o["status"]["name"]),
                 ("kind_changed_by_mapping" if same_status else "kind_changed", e["kind"], o["kind"]),
                 ("sprint_changed", sprint_label(e.get("sprint")), sprint_label(o.get("sprint")))]
        if reader:
            pairs.append(("estimate_changed", read_estimate(e, reader)[0], read_estimate(o, reader)[0]))
        for name, old, new in pairs:
            if old != new:
                changed[name].append({"id": o["id"], "from": old, "to": new})
    reasons = [r for r in (scope_reason(esc), scope_reason(sc)) if r]
    return {"made": True, "earlier_taken_at": earlier["taken_at"], "later_taken_at": snap["taken_at"],
            "added": [o["id"] for k, o in now.items() if k not in before],
            "removed": [o["id"] for k, o in before.items() if k not in now],
            **changed,
            "mapping_changed": mapping_diff(earlier["mapping"], snap["mapping"]),
            "forces": forces(before, now, reader, given),
            "estimate_reason": None if reader else no_size_reason(given),
            "scope_complete": (True if esc["complete"] is True and sc["complete"] is True
                               else False if False in (esc["complete"], sc["complete"]) else None),
            "scope_reason": "; ".join(reasons) or None,
            "basis": "net difference between two snapshots: what changed, not when or how often; "
                     "an item added and removed between them does not show; an issue missing from an "
                     "incomplete read shows as removed. kind_changed_by_mapping: the status is the same "
                     "and the mapping changed"}


# --- series ----------------------------------------------------------------------------------

def _refuse_series(reason, **extra):
    return {**extra, "points": None, "reason": reason, "basis": "not_computed"}


def _days(first, last):
    d = first
    while d <= last:
        yield d
        d += timedelta(days=1)


def _day_end(d, tz):
    return datetime.combine(d + timedelta(days=1), time(), tzinfo=tz)


def _local_date(t, tz):
    return t.astimezone(tz).date()


def cfd(issues, mapping, taken, win, tz, zone):
    if not issues:
        return _refuse_series("no issues in the snapshot")
    lacking = [o["id"] for o in issues if not o.get("transitions")]
    if lacking:
        return _refuse_series(f"{len(lacking)} issue(s) have no transitions from the tool ({shown(lacking)}); "
                              "a cumulative flow chart needs each issue's entry into each state, and counts "
                              "of what sits in each column now are not that")
    gaps = [(o["id"], g) for o in issues if (g := history_gap(o))]
    if gaps:
        return _refuse_series(f"{len(gaps)} issue(s) have a history that is not whole: "
                              + "; ".join(f"{i}: {g}" for i, g in gaps[:5]) + (" ..." if len(gaps) > 5 else ""))
    trails = [[(at, st) for at, _, st in _trail(o)] for o in issues]
    first = _local_date(win["from"], tz) if win else min(_local_date(tr[0][0], tz) for tr in trails)
    last = _local_date(taken, tz)
    if win:
        last = min(last, _local_date(win["to"] - timedelta(microseconds=1), tz))
    points = []
    for d in _days(first, last):
        cut, row = _day_end(d, tz), {}
        for tr in trails:
            entered = [st for at, st in tr if at < cut]
            if entered:
                kind = kind_of(mapping, entered[-1]) or UNMAPPED
                row[kind] = row.get(kind, 0) + 1
        points.append({"date": d.isoformat(), "counts": row})
    return {"points": points, "reason": None, "basis": "exact",
            "method": f"per day ({zone}), issues by the kind of the last status entered by that day's end, "
                      "from the tool's transitions and the snapshot's mapping; an issue that left the "
                      "scope before this snapshot is not seen"}


def burndown(issues, sprints, taken, reader, name, tz, zone, given, sc):
    if excluded(sc):
        return _refuse_series(EXCLUDED, sprint=name)
    if reader is None:
        return _refuse_series(f"{no_size_reason(given)}: a burndown needs estimates", sprint=name)
    if not sprints:
        return _refuse_series(no_sprints_reason(sprints), sprint=name)
    if name is not None:
        chosen = [sp for sp in sprints if name in (sp.get("name"), str(sp.get("id")))]
        if not chosen:
            return _refuse_series(f"sprint {name!r} is not in the snapshot", sprint=name)
        if len(chosen) > 1:
            return _refuse_series(f"{len(chosen)} sprints match {name!r}; name one by id", sprint=name)
    else:
        chosen = [sp for sp in sprints if sp.get("state") == "active"]
        if len(chosen) != 1:
            return _refuse_series("no sprint named (--sprint) and not exactly one active sprint", sprint=None)
    sp = chosen[0]
    label_ = sp.get("name")
    start, end, _, skip = period_bounds(sp, taken, tz)
    if skip:
        return _refuse_series(f"sprint {label_!r}: " + ("has not started" if start is not None else skip),
                              sprint=label_)
    abandoned = [o for o in issues if (o.get("markers") or {}).get("abandoned") is True and in_sprint(o, sp)]
    gone = {id(o) for o in abandoned}
    mine = [o for o in issues if in_sprint(o, sp) and id(o) not in gone]
    if not mine:
        return _refuse_series(f"no issue names sprint {label_!r}", sprint=label_)
    gap = finish_gap([o for o in mine if o["kind"] == "finished"])
    if gap:
        return _refuse_series(gap, sprint=label_)
    sized, missing, bad = [], [], []
    for o in mine:
        v, state = read_estimate(o, reader)
        if state == "ok":
            done = finished_time(o) if o["kind"] == "finished" else None
            sized.append((v, done))
        else:
            (missing if state == "missing" else bad).append(o["id"])
    lacking = missing + bad
    last = min(_local_date(end - timedelta(microseconds=1), tz), _local_date(taken, tz))
    points = []
    for d in _days(_local_date(start, tz), last):
        cut = _day_end(d, tz)
        points.append({"date": d.isoformat(),
                       "remaining": sum(v for v, done in sized if done is None or done >= cut)})
    return {"sprint": label_, "points": points, "without_estimate": idlist(missing),
            "estimate_unreadable": idlist(bad),
            "complete": not lacking,
            "complete_reason": (f"remaining leaves out {len(lacking)} issue(s) without a readable estimate "
                                f"({shown(lacking)}), so it is too low") if lacking else None,
            "abandoned_excluded": [o["id"] for o in abandoned],
            "reason": None, "basis": "exact finish times, current scope",
            "method": f"per day ({zone}) of the sprint up to taken_at, the sum of estimates of the issues "
                      "naming the sprint now that were not finished by that day's end (the tool's "
                      "finished_at). Sprint membership and estimates are as of this snapshot: scope added "
                      "or removed and re-estimates during the sprint are not seen; issues without an "
                      "estimate are listed, not counted as zero"}


def scatterplot(ct, tz, zone):
    if ct["n"] is None:
        return _refuse_series(f"no cycle times: {ct['reason']}")
    pts = [{"id": x["id"], "finished": _local_date(parse_time(x["finished_at"], "finished_at"), tz).isoformat(),
            "days": x["days"]} for x in ct["items"]]
    return {"points": pts, "percentiles": ct["percentiles"], "reason": None, "basis": "exact",
            "method": f"one point per cycle_time item: its finish date ({zone}) and cycle time in days"}


def histogram(ct):
    if ct["n"] is None:
        return _refuse_series(f"no cycle times: {ct['reason']}")
    bands = [math.floor(x["days"]) for x in ct["items"]]
    pts = [{"from_days": b, "to_days": b + 1, "count": bands.count(b)} for b in range(min(bands), max(bands) + 1)]
    return {"points": pts, "percentiles": ct["percentiles"], "reason": None, "basis": "exact",
            "method": "cycle_time items per whole-day band [from_days, to_days); empty bands included"}


def compute(snap, cfg, earlier=None, window=None, sprint=None, age_at=None):
    given = cfg is not None
    if given:
        validate_settings(cfg, require_process=True)
    cfg = cfg or {}
    validate_snapshot(snap)
    taken = parse_time(snap["taken_at"], "taken_at")
    issues = snap["issues"]
    mapping = snap["mapping"]
    tz, zone = day_zone(cfg)
    sc = scope_of(snap)
    win = parse_window(window, tz)
    reader = size_scale(cfg)
    started = Started(cfg, mapping, issues)
    ref = taken
    if age_at is not None:
        ref, date_only = parse_bound(age_at, "--age-at", tz)
        if date_only:
            ref = _next_midnight(ref, tz)
        if ref > taken:
            raise InputError(f"--age-at {age_at!r} is after the snapshot's taken_at {snap['taken_at']!r}")
    a = age(issues, ref, started, mapping)
    a["reference_time"] = age_at if age_at is not None else snap["taken_at"]
    t = throughput(issues, snap.get("sprints"), taken, tz, zone, sc)
    t["window"] = label(window_throughput(issues, win, sc), sc)
    ct = cycle_time(issues, win, started, mapping, sc)
    atomic = snap["atomic"] if "atomic" in snap else (False if snap["source"] == "composed" else None)
    return {
        "schema": SCHEMA,
        "settings": {"given": given, "reason": None if given else NO_SETTINGS},
        "snapshot": {"taken_at": snap["taken_at"], "taken_at_basis": snap.get("taken_at_basis"),
                     "source": snap["source"], "atomic": atomic,
                     "scope": snap.get("scope"), "scope_complete": sc["complete"],
                     "scope_reason": scope_reason(sc),
                     "unmapped_statuses": snap.get("unmapped_statuses", []),
                     "naive_timestamps": count_naive(issues), "day_boundaries": zone},
        "timestamp_problems": timestamp_problems(issues, taken),
        "counts": label(counts(issues), sc),
        "wip": label(wip(issues, started), sc),
        "limits": label(limits(issues, snap, cfg, given), sc),
        "age": a,
        "missing_acceptance_criteria": acceptance(issues, cfg),
        "throughput": label(t, sc),
        "arrivals": label(arrivals(issues, snap.get("sprints"), taken, win, tz, zone), sc),
        "cycle_time": label(ct, sc),
        "sle": sle(cfg, ct, given),
        "estimates": label(estimates(issues, reader, given), sc),
        "velocity": label(velocity(issues, snap.get("sprints"), reader, given, sc), sc),
        "comparison": comparison(snap, earlier, reader, given, sc),
        "series": {
            "cfd": cfd(issues, mapping, taken, win, tz, zone),
            "burndown": burndown(issues, snap.get("sprints"), taken, reader, sprint, tz, zone, given, sc),
            "scatterplot": scatterplot(ct, tz, zone),
            "histogram": histogram(ct),
        },
    }


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("snapshot")
    p.add_argument("--settings", help="the project's workflow settings (TOML)")
    p.add_argument("--out")
    p.add_argument("--compare", help="an earlier snapshot to diff against")
    p.add_argument("--window-start")
    p.add_argument("--window-end")
    p.add_argument("--sprint", help="the sprint for the burndown; default the one active sprint")
    p.add_argument("--age-at", help="reference time for age (ISO date or time, at most taken_at); "
                                    "a date means the end of that day")
    a = p.parse_args(argv)
    try:
        if (a.window_start is None) != (a.window_end is None):
            raise InputError("a window needs both --window-start and --window-end")
        window = (a.window_start, a.window_end) if a.window_start else None
        earlier = load_json(a.compare) if a.compare else None
        result = compute(load_json(a.snapshot), load_settings(a.settings),
                         earlier=earlier, window=window, sprint=a.sprint, age_at=a.age_at)
    except InputError as e:
        print(f"board_metrics.py: error: {e}", file=sys.stderr)
        return 2
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if a.out:
        Path(a.out).write_text(text + "\n", encoding="utf-8")
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
