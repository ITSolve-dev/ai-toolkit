"""Board arithmetic over a task-master snapshot, so no agent has to count.

    board_metrics.py snapshot.json [--config .claude/task-master.toml] [--out metrics.json]

Reads a snapshot written by snapshot.py (schema 1). From the config it uses only [limits] and
[checks].acceptance_headings; without a config there are no limits and the heading is
"Acceptance criteria".

Every figure carries `basis`, saying what it was computed from:
  exact          - from history the tool reported (status_since, finished_at)
  since_created  - age counted from created_at, because the tool reports no time in state;
                   a task stuck in a state looks the same as one long open
  unknown        - neither is available; the value is null
`updated_at` is never read as a finish time or a state change.

Reference time for ages is the snapshot's taken_at, not the moment this runs.
Malformed input: exit 2, message on stderr, nothing on stdout.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import tomllib
from datetime import timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from snapshot import KINDS, SCHEMA, InputError, load_json, parse_time, validate_issue  # noqa: E402

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


def wip(issues):
    started = [o for o in issues if o["kind"] in WIP_KINDS]
    return {
        "total": len(started),
        "by_kind": tally(started, lambda o: o["kind"]),
        "by_status": tally(started, status_name),
        "basis": "issues of kind active or handed_off; unmapped issues are not counted",
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


def age(issues, taken):
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
                      "days": days, "basis": basis})
    return {"reference_time": None, "items": items, "skipped_unmapped": skipped,
            "basis": "per item: exact = time in current state from the tool's history; "
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


def throughput(issues, sprints, taken):
    refuse = lambda reason: {"periods": None, "reason": reason, "basis": "not_computed"}
    # abandoned work (marker true) is finished but was not delivered: not throughput
    finished = [o for o in issues if o["kind"] == "finished"
                and (o.get("markers") or {}).get("abandoned") is not True]
    lacking = [o["id"] for o in finished if o.get("finished_at") is None]
    if lacking:
        shown = ", ".join(map(str, lacking[:20])) + (" ..." if len(lacking) > 20 else "")
        return refuse(f"{len(lacking)} finished issue(s) have no finish time from the tool "
                      f"({shown}); updated_at is not a finish time")
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


def compute(snap, cfg):
    validate_snapshot(snap)
    taken = parse_time(snap["taken_at"], "taken_at")
    issues = snap["issues"]
    a = age(issues, taken)
    a["reference_time"] = snap["taken_at"]
    return {
        "schema": SCHEMA,
        "snapshot": {"taken_at": snap["taken_at"], "source": snap["source"],
                     "atomic": snap["source"] == "native",
                     "unmapped_statuses": snap.get("unmapped_statuses", [])},
        "counts": counts(issues),
        "wip": wip(issues),
        "limits": limits(issues, snap, cfg),
        "age": a,
        "missing_acceptance_criteria": acceptance(issues, cfg),
        "throughput": throughput(issues, snap.get("sprints"), taken),
    }


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("snapshot")
    p.add_argument("--config")
    p.add_argument("--out")
    a = p.parse_args(argv)
    try:
        result = compute(load_json(a.snapshot), load_metrics_config(a.config))
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
