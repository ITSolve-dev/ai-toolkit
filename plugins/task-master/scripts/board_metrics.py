"""Board arithmetic over a task-master snapshot, so no agent has to count.

    board_metrics.py snapshot.json [--config .claude/task-master.toml] [--out metrics.json]
                     [--compare earlier-snapshot.json] [--window-start D --window-end D]
                     [--sprint NAME]

Reads a snapshot written by snapshot.py (schema 1). From the config it uses [limits],
[checks].acceptance_headings, [project].sle ("<n> days at <p>%") and [fields].estimate
("field:<name>" or "label:<prefix>{value}"); each absent means: no limits, the heading
"Acceptance criteria", no SLE, no estimates.

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

History-dependent figures need native history on the issues (see snapshot.py):
  cycle_time, sle, series.scatterplot, series.histogram - finished_at and a start on every
      finished item in scope. The start is the first transition into a started kind; without
      transitions, started_at is the field a tool with native history must supply.
      status_since of a finished item is when it finished, not when it started.
Started kinds: [project].started_kinds (default active, handed_off) decide what counts as WIP,
which open items age marks `started`, and where cycle time starts.
  throughput, series.burndown - finished_at.
  series.cfd - transitions on every issue.
Any item in scope lacking them makes the figure null with the reason; it is not computed from
the items that happen to have them.

Window (--window-start/--window-end, ISO dates or times; a date-only end includes that day):
scopes throughput.window, arrivals.window and cycle time (items finished in the window).
--compare: net differences against an earlier snapshot (added, removed, status, kind, estimate,
sprint), the plan record where there is no history. --sprint names the burndown's sprint;
without it the one sprint whose state is "active".

Reference time for ages is the snapshot's taken_at, not the moment this runs. Days are UTC.
Malformed input: exit 2, message on stderr, nothing on stdout.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
import tomllib
from datetime import datetime, time, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from snapshot import (KINDS, SCHEMA, InputError, label_names, load_json, parse_time,  # noqa: E402
                      validate_issue)

WIP_KINDS = ("active", "handed_off")
DEFAULT_HEADINGS = ["Acceptance criteria"]
UNMAPPED = "(unmapped)"
NO_STATUS = "(no status)"

ATX = re.compile(r"^\s{0,3}#{1,6}\s*(.*?)\s*#*\s*$")
WIKI = re.compile(r"^\s*h[1-6]\.\s*(.*?)\s*$")
BOLD = re.compile(r"^\s*(\*\*|__)(.+?)\1\s*:?\s*$")
SETEXT_RULE = re.compile(r"^\s*(=+|-+)\s*$")


def load_metrics_config(path):
    if path is None:
        return {}
    try:
        return tomllib.loads(Path(path).read_text(encoding="utf-8"))
    except OSError as e:
        raise InputError(f"{path}: cannot read: {e}") from None
    except tomllib.TOMLDecodeError as e:
        raise InputError(f"{path}: malformed TOML: {e}") from None


def validate_snapshot(snap):
    if not isinstance(snap, dict):
        raise InputError("snapshot: expected a JSON object")
    if snap.get("schema") != SCHEMA:
        raise InputError(f"snapshot: schema must be {SCHEMA}, got {snap.get('schema')!r}")
    for key in ("taken_at", "source", "issues"):
        if key not in snap:
            raise InputError(f"snapshot: missing required field: {key}")
    if snap["source"] not in ("composed", "native"):
        raise InputError(f"snapshot: source must be composed or native, got {snap['source']!r}")
    if parse_time(snap["taken_at"], "snapshot: taken_at") is None:
        raise InputError("snapshot: taken_at may not be null")
    if not isinstance(snap["issues"], list):
        raise InputError("snapshot: issues must be an array")
    for i, obj in enumerate(snap["issues"]):
        validate_issue(obj, f"issues[{i}]")
        if "kind" not in obj or (obj["kind"] is not None and obj["kind"] not in KINDS):
            raise InputError(f"issues[{i}]: kind must be one of {', '.join(KINDS)} or null; "
                             "was the snapshot made by snapshot.py?")
    sprints = snap.get("sprints")
    if sprints is not None and not isinstance(sprints, list):
        raise InputError("snapshot: sprints must be an array or null")
    if sprints and not all(isinstance(sp, dict) for sp in sprints):
        raise InputError("snapshot: each sprint must be an object")


def status_name(obj):
    return obj["status"]["name"] if obj["status"]["name"] is not None else NO_STATUS


def tally(items, key):
    out = {}
    for obj in items:
        k = key(obj)
        out[k] = out.get(k, 0) + 1
    return out


def counts(issues):
    mapped = [o for o in issues if o["kind"] is not None]
    return {
        "total": len(issues),
        "by_kind": tally(mapped, lambda o: o["kind"]),
        "unmapped": len(issues) - len(mapped),
        "by_status": tally(issues, status_name),
        "basis": "count of issues in the snapshot",
    }


def idlist(ids):
    return {"count": len(ids), "ids": ids}


def shown(ids):
    return ", ".join(map(str, ids[:20])) + (" ..." if len(ids) > 20 else "")


def started_kinds(cfg):
    """[project].started_kinds: the kinds that count as started work. Default WIP_KINDS."""
    raw = (cfg.get("project") or {}).get("started_kinds")
    if raw is None:
        return list(WIP_KINDS)
    ok = [k for k in KINDS if k != "finished"]
    if not isinstance(raw, list) or not raw or not all(isinstance(k, str) and k in ok for k in raw):
        raise InputError(f"[project].started_kinds = {raw!r}: expected a non-empty list of {', '.join(ok)}")
    return list(dict.fromkeys(raw))


def wip(issues, kinds):
    started = [o for o in issues if o["kind"] in kinds]
    by_assignee, unassigned, not_read = {}, [], []
    for o in started:
        if "assignees" not in o:
            not_read.append(o["id"])
            continue
        people = o["assignees"] or []
        if not isinstance(people, list):
            raise InputError(f"issue {o['id']}: assignees must be a list or null")
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
        "started_kinds": kinds,
        "basis": f"issues of a started kind ({', '.join(kinds)}, from [project].started_kinds or the "
                 "default); unmapped issues are not counted. by_assignee: "
                 "an item with several assignees counts once for each, so it may sum above total; "
                 "assignees_not_read: the read carried no assignees key, so who holds it is unknown",
    }


def limits(issues, snap, cfg):
    table = cfg.get("limits")
    if table is None:
        return {"declared": False, "breaches": [], "unknown_keys": [],
                "basis": "no [limits] in config"}
    if not isinstance(table, dict):
        raise InputError("[limits] must be a table")
    statuses = set(snap.get("mapping") or {}) | set(snap.get("unmapped_statuses") or [])
    statuses |= {o["status"]["name"] for o in issues if o["status"]["name"] is not None}
    by_kind = tally(issues, lambda o: o["kind"])
    by_status = tally(issues, lambda o: o["status"]["name"])
    breaches, unknown = [], []
    for key, n in table.items():
        if not isinstance(n, int) or isinstance(n, bool) or n < 1:
            raise InputError(f"[limits] {key!r} = {n!r}: a limit must be a positive integer")
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
            "basis": "count of issues in the status, or of the kind, against [limits]; "
                     "a key that is a kind name is read as a kind"}


def age(issues, taken, kinds):
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
        days = round((taken - start).total_seconds() / 86400, 2) if start else None
        items.append({"id": o["id"], "status": o["status"]["name"], "kind": o["kind"],
                      "started": o["kind"] in kinds, "days": days, "basis": basis})
    return {"reference_time": None, "items": items, "skipped_unmapped": skipped, "started_kinds": kinds,
            "basis": "every open mapped item; `started` marks those of a started kind (started_kinds). "
                     "per item: exact = time in current state from the tool's history; "
                     "since_created = days since created_at, not time in state; "
                     "unknown = no timestamp. Unmapped issues are skipped: open or not cannot be told"}


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
    checks = cfg.get("checks", {})
    headings = checks.get("acceptance_headings", DEFAULT_HEADINGS)
    if not isinstance(headings, list) or not headings or not all(isinstance(h, str) for h in headings):
        raise InputError("[checks].acceptance_headings must be a non-empty list of strings")
    items = []
    for o in issues:
        if o["kind"] == "finished":
            continue
        if not o["description"]:
            items.append({"id": o["id"], "status": o["status"]["name"], "reason": "no_description"})
        elif not has_heading(o["description"], headings):
            items.append({"id": o["id"], "status": o["status"]["name"], "reason": "no_heading"})
    return {"headings": headings, "items": items,
            "basis": "unfinished issues whose description has no heading (Markdown #, underlined, "
                     "hN., or a bold line) named as one of `headings`; content under it is not judged"}


def _period_bounds(sprint, taken):
    start_raw, end_raw = sprint.get("start_date"), sprint.get("end_date")
    start = parse_time(start_raw, f"sprint {sprint.get('name')!r}: start_date")
    end = parse_time(end_raw, f"sprint {sprint.get('name')!r}: end_date")
    if end is not None and isinstance(end_raw, str) and len(end_raw) == 10:
        end += timedelta(days=1)  # a date-only end includes that whole day
    return start, end if end is not None else taken, end is None


def delivered(issues):
    """Finished and not marked abandoned: abandoned work finished but was not delivered."""
    return [o for o in issues if o["kind"] == "finished"
            and (o.get("markers") or {}).get("abandoned") is not True]


def finish_gap(finished):
    lacking = [o["id"] for o in finished if o.get("finished_at") is None]
    if lacking:
        return (f"{len(lacking)} finished issue(s) have no finish time from the tool "
                f"({shown(lacking)}); updated_at is not a finish time")
    return None


def finished_time(o):
    return parse_time(o["finished_at"], f"issue {o['id']}: finished_at")


def throughput(issues, sprints, taken):
    refuse = lambda reason: {"periods": None, "reason": reason, "basis": "not_computed"}
    finished = delivered(issues)
    gap = finish_gap(finished)
    if gap:
        return refuse(gap)
    if not sprints:
        return refuse("no sprint dates in the snapshot")
    periods, skipped = [], []
    placed = set()
    for sp in sprints:
        if not isinstance(sp, dict):
            raise InputError("sprints: each sprint must be an object")
        start, end, open_period = _period_bounds(sp, taken)
        if start is None:
            skipped.append(sp.get("name"))
            continue
        ids = [o["id"] for o in finished if start <= parse_time(o["finished_at"], "finished_at") < end]
        placed.update(ids)
        periods.append({"sprint": sp.get("name"), "start": sp.get("start_date"),
                        "end": sp.get("end_date"), "finished": len(ids), "open_period": open_period})
    if not periods:
        return refuse("no sprint in the snapshot has a start date")
    return {"periods": periods, "skipped_sprints": skipped,
            "finished_outside_periods": len([o for o in finished if o["id"] not in placed]),
            "reason": None,
            "basis": "exact",
            "method": "finished issues not marked abandoned, counted by the tool's finished_at within each sprint's dates "
                      "(a date-only end includes that day); an open period runs to taken_at"}


PERCENTILES = (50, 70, 85, 95)
NO_WINDOW = "no window given (--window-start/--window-end)"


def parse_window(window):
    """(start, end) strings -> {start, end, from, to}; a date-only end includes that day."""
    if window is None:
        return None
    s_raw, e_raw = window
    start, end = parse_time(s_raw, "window start"), parse_time(e_raw, "window end")
    if start is None or end is None:
        raise InputError("a window needs both --window-start and --window-end")
    if len(e_raw) == 10:
        end += timedelta(days=1)
    if end <= start:
        raise InputError(f"window: end {e_raw!r} is not after start {s_raw!r}")
    return {"start": s_raw, "end": e_raw, "from": start, "to": end}


def in_window(t, win):
    return win["from"] <= t < win["to"]


def window_info(win):
    return {"start": win["start"], "end": win["end"]} if win else None


def window_throughput(issues, win):
    if win is None:
        return {"finished": None, "ids": None, "reason": NO_WINDOW, "basis": "not_computed"}
    finished = delivered(issues)
    gap = finish_gap(finished)
    if gap:
        return {**window_info(win), "finished": None, "ids": None, "reason": gap, "basis": "not_computed"}
    ids = [o["id"] for o in finished if in_window(finished_time(o), win)]
    return {**window_info(win), "finished": len(ids), "ids": ids, "reason": None, "basis": "exact",
            "method": "finished issues not marked abandoned whose finished_at falls in the window"}


def num(text):
    x = float(text)
    return int(x) if x == int(x) else x


def start_of(o, kinds, mapping):
    """-> (raw ISO start, source) or (None, None). From transitions when the tool gave them: the
    first entry into a status whose kind is started; otherwise the tool's own started_at."""
    trans = o.get("transitions")
    if trans:
        entries = sorted(((parse_time(t["at"], f"issue {o['id']}: transitions"), t["at"]) for t in trans
                          if mapping.get(t["status"]) in kinds), key=lambda x: x[0])
        return (entries[0][1], "transitions") if entries else (None, None)
    if o.get("started_at") is not None:
        return o["started_at"], "started_at"
    return None, None


def cycle_time(issues, win, kinds, mapping):
    def refuse(reason):
        return {"n": None, "percentiles": None, "items": None, "window": window_info(win),
                "reason": reason, "basis": "not_computed"}
    finished = delivered(issues)
    gap = finish_gap(finished)
    if gap:
        return refuse(gap)
    if win:
        finished = [o for o in finished if in_window(finished_time(o), win)]
    if not finished:
        return refuse("no finished issues" + (" in the window" if win else ""))
    starts = {id(o): start_of(o, kinds, mapping) for o in finished}
    lacking = [o["id"] for o in finished if starts[id(o)][0] is None]
    if lacking:
        return refuse(f"{len(lacking)} finished issue(s) have no start time: neither transitions into a "
                      f"started kind ({', '.join(kinds)}) nor started_at from the tool ({shown(lacking)}); "
                      "status_since of a finished issue is when it finished, and updated_at is not a start")
    items = []
    for o in finished:
        raw, source = starts[id(o)]
        s, f = parse_time(raw, f"issue {o['id']}: start"), finished_time(o)
        if f < s:
            raise InputError(f"issue {o['id']}: finished_at is before its start")
        items.append({"id": o["id"], "started_at": raw, "start_source": source,
                      "finished_at": o["finished_at"],
                      "days": round((f - s).total_seconds() / 86400, 2), "_f": f})
    items.sort(key=lambda x: x["_f"])
    for x in items:
        del x["_f"]
    vals = sorted(x["days"] for x in items)
    n = len(vals)
    pct = {str(p): vals[-(-p * n // 100) - 1] for p in PERCENTILES}
    return {"n": n, "percentiles": pct, "items": items, "window": window_info(win), "reason": None,
            "basis": "exact",
            "started_kinds": kinds,
            "method": "finished_at minus the start, in days, for finished issues not marked abandoned "
                      "(in the window, when one is given); percentiles by nearest rank over n items. "
                      "start_source transitions = first entry into a started kind (started_kinds); "
                      "started_at = the tool's own start, used only without transitions, which may "
                      "not follow started_kinds"}


SLE_RX = re.compile(r"^\s*(\d+(?:\.\d+)?)\s*days?\s+at\s+(\d+(?:\.\d+)?)\s*%\s*$", re.IGNORECASE)


def sle(cfg, ct):
    raw = (cfg.get("project") or {}).get("sle")
    base = {"declared": raw is not None, "sle": raw, "days": None, "probability": None,
            "n": None, "within": None, "share": None, "misses": None}
    if raw is None:
        return {**base, "reason": "no [project].sle in config", "basis": "not_computed"}
    m = SLE_RX.match(raw) if isinstance(raw, str) else None
    if not m or not 0 < float(m.group(2)) <= 100:
        raise InputError(f"[project].sle = {raw!r}: expected \"<n> days at <p>%\"")
    days, prob = num(m.group(1)), num(m.group(2))
    base.update(days=days, probability=prob)
    if ct["n"] is None:
        return {**base, "reason": f"no cycle times: {ct['reason']}", "basis": "not_computed"}
    misses = [x["id"] for x in ct["items"] if x["days"] > days]
    within = ct["n"] - len(misses)
    return {**base, "n": ct["n"], "within": within, "share": round(within / ct["n"], 4),
            "misses": misses, "reason": None, "basis": "exact",
            "method": "share of the cycle_time items whose cycle time is at most the SLE's days; "
                      "compare it with the SLE's probability"}


def arrivals(issues, sprints, taken, win):
    lacking = [o["id"] for o in issues if o["created_at"] is None]
    if lacking:
        reason = (f"{len(lacking)} issue(s) have no created_at ({shown(lacking)}); "
                  "when they arrived cannot be told")
        return {"periods": None, "reason": reason,
                "window": {"arrived": None, "ids": None, "reason": reason}, "basis": "not_computed"}
    created = {o["id"]: parse_time(o["created_at"], f"issue {o['id']}: created_at") for o in issues}
    periods, reason = None, "no sprint dates in the snapshot"
    for sp in sprints or []:
        start, end, open_period = _period_bounds(sp, taken)
        if start is None:
            continue
        ids = [i for i, t in created.items() if start <= t < end]
        periods = (periods or []) + [{"sprint": sp.get("name"), "start": sp.get("start_date"),
                                      "end": sp.get("end_date"), "arrived": len(ids), "ids": ids,
                                      "open_period": open_period}]
    if periods is not None:
        reason = None
    elif sprints:
        reason = "no sprint in the snapshot has a start date"
    if win is None:
        wd = {"arrived": None, "ids": None, "reason": NO_WINDOW}
    else:
        ids = [i for i, t in created.items() if in_window(t, win)]
        wd = {**window_info(win), "arrived": len(ids), "ids": ids, "reason": None}
    return {"periods": periods, "reason": reason, "window": wd, "basis": "created_at",
            "method": "issues whose created_at falls in each sprint's dates or the window; an issue "
                      "that left the scope before this snapshot is not seen"}


# --- estimates -------------------------------------------------------------------------------

def estimate_reader(cfg):
    spec = (cfg.get("fields") or {}).get("estimate")
    if spec is None:
        return None
    if isinstance(spec, str) and spec.startswith("field:") and len(spec) > 6:
        return {"spec": spec, "field": spec[6:]}
    if isinstance(spec, str) and spec.startswith("label:") and spec.count("{value}") == 1:
        pre, post = spec[6:].split("{value}")
        return {"spec": spec, "label": re.compile("^" + re.escape(pre) + "(.+?)" + re.escape(post) + "$")}
    raise InputError(f"[fields].estimate = {spec!r}: expected \"field:<name>\" or \"label:<prefix>{{value}}\"")


def _number(v):
    if isinstance(v, bool) or not isinstance(v, (int, float, str)):
        return None
    try:
        x = float(v)
    except ValueError:
        return None
    if not math.isfinite(x) or x < 0:
        return None
    return int(x) if x == int(x) else x


def read_estimate(o, reader):
    """-> (value, state), state one of ok, missing, unreadable. A missing estimate is not zero."""
    if "field" in reader:
        name = reader["field"]
        fields = o.get("fields") if isinstance(o.get("fields"), dict) else {}
        raw = o[name] if name in o else fields.get(name)
        if raw is None:
            return None, "missing"
        v = _number(raw)
        return (v, "ok") if v is not None else (None, "unreadable")
    found = {m.group(1) for n in label_names(o["labels"]) if (m := reader["label"].match(n))}
    if not found:
        return None, "missing"
    v = _number(found.pop()) if len(found) == 1 else None
    return (v, "ok") if v is not None else (None, "unreadable")


def estimates(issues, reader):
    if reader is None:
        return {"declared": False, "field": None, "total": None, "by_kind": None, "with_estimate": None,
                "without_estimate": None, "unreadable": None,
                "reason": "no [fields].estimate in config", "basis": "not_computed"}
    total, by_kind, ok, missing, bad = 0, {}, 0, [], []
    for o in issues:
        v, state = read_estimate(o, reader)
        if state == "missing":
            missing.append(o["id"])
        elif state == "unreadable":
            bad.append(o["id"])
        else:
            ok += 1
            total += v
            if o["kind"] is not None:
                by_kind[o["kind"]] = by_kind.get(o["kind"], 0) + v
    return {"declared": True, "field": reader["spec"], "total": total, "by_kind": by_kind,
            "with_estimate": ok, "without_estimate": idlist(missing), "unreadable": idlist(bad),
            "reason": None, "basis": "estimate as the board holds it now",
            "method": "sum of estimates read through [fields].estimate; total includes unmapped issues, "
                      "by_kind does not. Issues without one, or with one that is not a single "
                      "non-negative number, are counted apart, never as zero"}


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


def velocity(issues, sprints, reader):
    if not sprints:
        return {"periods": None, "reason": "no sprints in the snapshot", "basis": "not_computed"}
    finished = delivered(issues)
    periods, placed = [], set()
    for sp in sprints:
        if not isinstance(sp, dict):
            raise InputError("sprints: each sprint must be an object")
        mine = [o for o in finished if in_sprint(o, sp)]
        placed.update(id(o) for o in mine)
        points, missing, bad = (0 if reader else None), [], []
        for o in mine if reader else []:
            v, state = read_estimate(o, reader)
            if state == "ok":
                points += v
            else:
                (missing if state == "missing" else bad).append(o["id"])
        periods.append({"sprint": sp.get("name"), "state": sp.get("state"), "start": sp.get("start_date"),
                        "end": sp.get("end_date"), "finished": len(mine), "points": points,
                        "finished_without_estimate": idlist(missing) if reader else None,
                        "finished_estimate_unreadable": idlist(bad) if reader else None})
    return {"periods": periods,
            "points_reason": None if reader else "no [fields].estimate in config: velocity by count only",
            "finished_outside_sprints": idlist([o["id"] for o in finished if id(o) not in placed]),
            "reason": None, "basis": "by_sprint_field",
            "method": "per sprint, finished issues not marked abandoned whose sprint field names it, and "
                      "the sum of their whole estimates (all or nothing). It reads the sprint each item "
                      "names now, not finish times: an item finished after its sprint closed and "
                      "carried to the next is counted in the sprint it now names"}


# --- comparison ------------------------------------------------------------------------------

def comparison(snap, earlier, reader):
    if earlier is None:
        return {"made": False, "reason": "no earlier snapshot given (--compare)", "basis": "not_computed"}
    try:
        validate_snapshot(earlier)
    except InputError as e:
        raise InputError(f"earlier {e}") from None
    if parse_time(earlier["taken_at"], "earlier taken_at") > parse_time(snap["taken_at"], "taken_at"):
        raise InputError("--compare: the earlier snapshot was taken after this one")
    before = {str(o["id"]): o for o in earlier["issues"]}
    now = {str(o["id"]): o for o in snap["issues"]}
    changed = {"status_changed": [], "kind_changed": [], "estimate_changed": [] if reader else None,
               "sprint_changed": []}
    for key, o in now.items():
        e = before.get(key)
        if e is None:
            continue
        pairs = [("status_changed", e["status"]["name"], o["status"]["name"]),
                 ("kind_changed", e["kind"], o["kind"]),
                 ("sprint_changed", sprint_label(e.get("sprint")), sprint_label(o.get("sprint")))]
        if reader:
            pairs.append(("estimate_changed", read_estimate(e, reader)[0], read_estimate(o, reader)[0]))
        for name, old, new in pairs:
            if old != new:
                changed[name].append({"id": o["id"], "from": old, "to": new})
    return {"made": True, "earlier_taken_at": earlier["taken_at"], "later_taken_at": snap["taken_at"],
            "added": [o["id"] for k, o in now.items() if k not in before],
            "removed": [o["id"] for k, o in before.items() if k not in now],
            **changed,
            "estimate_reason": None if reader else "no [fields].estimate in config",
            "basis": "net difference between two snapshots: what changed, not when or how often; "
                     "an item added and removed between them does not show"}


# --- series ----------------------------------------------------------------------------------

def _refuse_series(reason, **extra):
    return {**extra, "points": None, "reason": reason, "basis": "not_computed"}


def _days(first, last):
    d = first
    while d <= last:
        yield d
        d += timedelta(days=1)


def _day_end(d):
    return datetime.combine(d + timedelta(days=1), time(), tzinfo=timezone.utc)


def _utc_date(t):
    return t.astimezone(timezone.utc).date()


def cfd(issues, mapping, taken, win):
    if not issues:
        return _refuse_series("no issues in the snapshot")
    lacking = [o["id"] for o in issues if not o.get("transitions")]
    if lacking:
        return _refuse_series(f"{len(lacking)} issue(s) have no transitions from the tool ({shown(lacking)}); "
                              "a cumulative flow chart needs each issue's entry into each state, and counts "
                              "of what sits in each column now are not that")
    trails = [sorted(((parse_time(t["at"], f"issue {o['id']}: transitions"), t["status"])
                      for t in o["transitions"]), key=lambda x: x[0]) for o in issues]
    first = _utc_date(win["from"]) if win else min(_utc_date(tr[0][0]) for tr in trails)
    last = _utc_date(taken)
    if win:
        last = min(last, _utc_date(win["to"] - timedelta(microseconds=1)))
    points = []
    for d in _days(first, last):
        cut, row = _day_end(d), {}
        for tr in trails:
            entered = [st for at, st in tr if at < cut]
            if entered:
                kind = mapping.get(entered[-1]) or UNMAPPED
                row[kind] = row.get(kind, 0) + 1
        points.append({"date": d.isoformat(), "counts": row})
    return {"points": points, "reason": None, "basis": "exact",
            "method": "per UTC day, issues by the kind of the last status entered by that day's end, from "
                      "the tool's transitions and the snapshot's mapping; an issue that left the scope "
                      "before this snapshot is not seen"}


def burndown(issues, sprints, taken, reader, name):
    if reader is None:
        return _refuse_series("no [fields].estimate in config: a burndown needs estimates", sprint=name)
    if not sprints:
        return _refuse_series("no sprints in the snapshot", sprint=name)
    if name is not None:
        chosen = [sp for sp in sprints if name in (sp.get("name"), str(sp.get("id")))]
        if not chosen:
            return _refuse_series(f"sprint {name!r} is not in the snapshot", sprint=name)
    else:
        chosen = [sp for sp in sprints if sp.get("state") == "active"]
        if len(chosen) != 1:
            return _refuse_series("no sprint named (--sprint) and not exactly one active sprint", sprint=None)
    sp = chosen[0]
    label = sp.get("name")
    start, end, _ = _period_bounds(sp, taken)
    if start is None:
        return _refuse_series(f"sprint {label!r} has no start date", sprint=label)
    abandoned = [o for o in issues if (o.get("markers") or {}).get("abandoned") is True and in_sprint(o, sp)]
    gone = {id(o) for o in abandoned}
    mine = [o for o in issues if in_sprint(o, sp) and id(o) not in gone]
    if not mine:
        return _refuse_series(f"no issue names sprint {label!r}", sprint=label)
    gap = finish_gap([o for o in mine if o["kind"] == "finished"])
    if gap:
        return _refuse_series(gap, sprint=label)
    sized, missing, bad = [], [], []
    for o in mine:
        v, state = read_estimate(o, reader)
        if state == "ok":
            done = finished_time(o) if o["kind"] == "finished" else None
            sized.append((v, done))
        else:
            (missing if state == "missing" else bad).append(o["id"])
    last = min(_utc_date(end - timedelta(microseconds=1)), _utc_date(taken))
    points = []
    for d in _days(_utc_date(start), last):
        cut = _day_end(d)
        points.append({"date": d.isoformat(),
                       "remaining": sum(v for v, done in sized if done is None or done >= cut)})
    return {"sprint": label, "points": points, "without_estimate": idlist(missing),
            "estimate_unreadable": idlist(bad), "abandoned_excluded": [o["id"] for o in abandoned],
            "reason": None, "basis": "exact finish times, current scope",
            "method": "per UTC day of the sprint up to taken_at, the sum of estimates of the issues naming "
                      "the sprint now that were not finished by that day's end (the tool's finished_at). "
                      "Sprint membership and estimates are as of this snapshot: scope added or removed "
                      "and re-estimates during the sprint are not seen; issues without an estimate are "
                      "listed, not counted as zero"}


def scatterplot(ct):
    if ct["n"] is None:
        return _refuse_series(f"no cycle times: {ct['reason']}")
    pts = [{"id": x["id"], "finished": _utc_date(parse_time(x["finished_at"], "finished_at")).isoformat(),
            "days": x["days"]} for x in ct["items"]]
    return {"points": pts, "percentiles": ct["percentiles"], "reason": None, "basis": "exact",
            "method": "one point per cycle_time item: its finish date (UTC) and cycle time in days"}


def histogram(ct):
    if ct["n"] is None:
        return _refuse_series(f"no cycle times: {ct['reason']}")
    bands = [math.floor(x["days"]) for x in ct["items"]]
    pts = [{"from_days": b, "to_days": b + 1, "count": bands.count(b)} for b in range(min(bands), max(bands) + 1)]
    return {"points": pts, "percentiles": ct["percentiles"], "reason": None, "basis": "exact",
            "method": "cycle_time items per whole-day band [from_days, to_days); empty bands included"}


def compute(snap, cfg, earlier=None, window=None, sprint=None):
    validate_snapshot(snap)
    taken = parse_time(snap["taken_at"], "taken_at")
    issues = snap["issues"]
    win = parse_window(window)
    reader = estimate_reader(cfg)
    kinds = started_kinds(cfg)
    a = age(issues, taken, kinds)
    a["reference_time"] = snap["taken_at"]
    t = throughput(issues, snap.get("sprints"), taken)
    t["window"] = window_throughput(issues, win)
    ct = cycle_time(issues, win, kinds, snap.get("mapping") or {})
    return {
        "schema": SCHEMA,
        "snapshot": {"taken_at": snap["taken_at"], "source": snap["source"],
                     "atomic": snap["source"] == "native",
                     "unmapped_statuses": snap.get("unmapped_statuses", [])},
        "counts": counts(issues),
        "wip": wip(issues, kinds),
        "limits": limits(issues, snap, cfg),
        "age": a,
        "missing_acceptance_criteria": acceptance(issues, cfg),
        "throughput": t,
        "arrivals": arrivals(issues, snap.get("sprints"), taken, win),
        "cycle_time": ct,
        "sle": sle(cfg, ct),
        "estimates": estimates(issues, reader),
        "velocity": velocity(issues, snap.get("sprints"), reader),
        "comparison": comparison(snap, earlier, reader),
        "series": {
            "cfd": cfd(issues, snap.get("mapping") or {}, taken, win),
            "burndown": burndown(issues, snap.get("sprints"), taken, reader, sprint),
            "scatterplot": scatterplot(ct),
            "histogram": histogram(ct),
        },
    }


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("snapshot")
    p.add_argument("--config")
    p.add_argument("--out")
    p.add_argument("--compare", help="an earlier snapshot to diff against")
    p.add_argument("--window-start")
    p.add_argument("--window-end")
    p.add_argument("--sprint", help="the sprint for the burndown; default the one active sprint")
    a = p.parse_args(argv)
    try:
        if (a.window_start is None) != (a.window_end is None):
            raise InputError("a window needs both --window-start and --window-end")
        window = (a.window_start, a.window_end) if a.window_start else None
        earlier = load_json(a.compare) if a.compare else None
        result = compute(load_json(a.snapshot), load_metrics_config(a.config),
                         earlier=earlier, window=window, sprint=a.sprint)
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
