"""Compose or enrich the task-master snapshot of a board scope.

The skill runs the board reads with the commands recorded in `.claude/task-master.toml` and hands
this script the results as files. The script reads no board and runs no tool.

Composed (the tool has no snapshot of its own):
    snapshot.py --issues issues.json --statuses statuses.json [--sprints sprints.json]
                --config .claude/task-master.toml [--taken-at ISO] [--out snapshot.json]
                [scope flags] [--history DIR]
Native (the tool wrote a snapshot):
    snapshot.py --native tool-snapshot.json --config .claude/task-master.toml [--out snapshot.json]
                [scope flags] [--history DIR]
Scope flags, recording what the issue read was:
    --scope QUERY                    the query or filter that produced the issue read
    --complete true|false            whether the tool reported the read complete (not cut at a
                                     page limit)
    --reported-total N               the total the tool said the query matches; without
                                     --complete, complete = (N equals the issues fetched)
    --includes-finished true|false   whether the query returns finished work
    --empty-ok                       an empty issue list is genuine; without it an empty list is
                                     refused, since it most often means the read was not made
  A native snapshot may carry the same record as `scope` {query, complete, reported_total,
  includes_finished}; a flag that contradicts it is an error.
--history DIR: one JSON object per issue, DIR/<id>.json (characters of the id outside
  [A-Za-z0-9._-] replaced by "_"), holding any of status_since, started_at, finished_at,
  transitions (and optionally its id). Merged into that issue and validated as the issue's own
  history fields; a key the issue already holds with a different value is an error. Issues
  without a file are listed in history.missing.

Normalized issue: the shape the plugin expects from any tool, whichever tool produced it.
    {id, kind, url, title, description, type, status{name, category}, assignees[{id, name}],
     labels[], priority, parent, subtasks[], links[{type, id}], sprint, milestone, due_date,
     author{id, name}, created_at, updated_at}
  Required keys: REQUIRED_ISSUE_KEYS. A key the board has no value for is present and null; null
  stays null here. `labels` items are strings or objects with a string `name`; anything else is
  an error. `assignees` is a list or null. `sprint` is null, a string or number, or an object
  with `id` and/or `name`; a list (Jira's every-sprint-it-was-in field) is an error: the adapter
  passes the one sprint the item counts in. Ids must be unique (a repeat is an error). Timestamps
  are ISO 8601; one without a zone is read as UTC and counted in naive_timestamps.
  Optional native history, used only when the tool reports it (a tool with native history
  supplies these; without them the history-dependent figures are null with the reason):
    status_since  - when the issue entered its current status
    started_at    - when it first entered a started state; cycle time runs from it when the
                    issue has no transitions (then from the first transition into a kind listed
                    in [project].started_kinds). status_since of a finished issue is when it
                    finished, so it cannot stand in
    finished_at   - when it reached a finished status
    transitions   - [{status, at}], every status the issue entered and when, its first status
                    included; a cumulative flow chart needs it on every issue
  `updated_at` is never a substitute for any of them.
  The tool's own `kind` (if any) is kept as `tool_kind`; `kind` becomes the plugin's kind.

Statuses: array of {name, ...}. Sprints: array of {id, name, state, start_date, end_date}.

Snapshot written:
    {schema: 1, taken_at, taken_at_basis: "given"|"script_run_time"|"tool",
     source: "composed"|"native", atomic, tool, tool_version,
     scope{query, fetched, reported_total, complete, includes_finished, empty_ok}, mapping,
     unmapped_statuses[], mapping_unknown_statuses[]|null, mapping_unknown_statuses_reason,
     issues_without_status[], markers_unreadable{marker: spec}, naive_timestamps,
     history{merged, missing} (with --history only), sprints, issues[]}
  atomic: false for a composed snapshot; for a native one the tool's own `atomic` claim, else
  null. mapping_unknown_statuses is null when the board's statuses were not read.
  Each issue gains `kind` (from [states]; null when unmapped, never guessed) and `markers`
  (true/false for a marker declared as `label:<name>` or `status:<name>`; null when the board
  cannot show it or shows it some other way, which these files do not carry; a marker declared
  some other way is listed in markers_unreadable). A marker spec not of the form
  `<prefix>:<name>`, or with Label:/STATUS: in another case, is a config error.

With --out, a one-line JSON summary goes to stderr: issue counts by kind, unmapped issues,
unmapped statuses, issues without a status, mapping entries the board lacks, whether the scope is
complete, taken_at_basis and naive_timestamps.

Malformed input or a missing required key: exit 2, message on stderr, nothing on stdout.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import tomllib
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = 1
KINDS = ("before_start", "queued", "active", "handed_off", "finished")
KNOWN_MARKERS = ("blocked", "waiting", "untriaged", "abandoned")
REQUIRED_ISSUE_KEYS = ("id", "title", "description", "status", "labels", "created_at", "updated_at")
HISTORY_KEYS = ("status_since", "started_at", "finished_at")
HISTORY_FILE_KEYS = HISTORY_KEYS + ("transitions",)
SCOPE_KEYS = ("query", "complete", "reported_total", "includes_finished")


class InputError(Exception):
    pass


def parse_time(value, where):
    """ISO 8601 string -> aware datetime (UTC when no zone). None stays None."""
    if value is None:
        return None
    if not isinstance(value, str):
        raise InputError(f"{where}: expected an ISO 8601 string or null, got {value!r}")
    try:
        dt = datetime.fromisoformat(value)
    except ValueError:
        raise InputError(f"{where}: not an ISO 8601 timestamp: {value!r}") from None
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def load_json(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except OSError as e:
        raise InputError(f"{path}: cannot read: {e}") from None
    except json.JSONDecodeError as e:
        raise InputError(f"{path}: malformed JSON: {e}") from None


def load_config(path):
    try:
        cfg = tomllib.loads(Path(path).read_text(encoding="utf-8"))
    except OSError as e:
        raise InputError(f"{path}: cannot read: {e}") from None
    except tomllib.TOMLDecodeError as e:
        raise InputError(f"{path}: malformed TOML: {e}") from None
    states = cfg.get("states")
    if not isinstance(states, dict) or not states:
        raise InputError(f"{path}: [states] is missing or empty; run init to map the board's statuses")
    for name, kind in states.items():
        if kind not in KINDS:
            raise InputError(f"{path}: [states] {name!r} = {kind!r}: kind must be one of {', '.join(KINDS)}")
    markers = cfg.get("markers", {})
    if not isinstance(markers, dict) or not all(isinstance(v, str) for v in markers.values()):
        raise InputError(f"{path}: [markers] must map a marker to a string")
    for marker, spec in markers.items():
        prefix, sep, name = spec.partition(":")
        if not sep or not prefix or not name:
            raise InputError(f"{path}: [markers] {marker} = {spec!r}: expected \"label:<name>\" or "
                             "\"status:<name>\"")
        if prefix.lower() in ("label", "status") and prefix != prefix.lower():
            raise InputError(f"{path}: [markers] {marker} = {spec!r}: write the prefix as {prefix.lower()}:")
    return cfg


def label_names(labels):
    names = set()
    for lab in labels:
        if isinstance(lab, str):
            names.add(lab)
        elif isinstance(lab, dict) and isinstance(lab.get("name"), str):
            names.add(lab["name"])
        else:
            raise InputError(f"label {lab!r}: expected a string or an object with a string name")
    return names


def _scalar(v):
    return isinstance(v, (str, int)) and not isinstance(v, bool)


def validate_sprint_field(ref, where):
    """null, a string or number, or {id, name} with at least one of them a string or number."""
    if ref is None or _scalar(ref):
        return
    if isinstance(ref, dict):
        vals = [ref.get(k) for k in ("id", "name")]
        if all(v is None or _scalar(v) for v in vals) and any(v is not None for v in vals):
            return
    kind = "a list" if isinstance(ref, list) else repr(ref)
    raise InputError(f"{where}: sprint must be null, a string or number, or {{id, name}}; got {kind}. "
                     "A list of every sprint the item was in is not accepted: pass the one it counts in")


def check_unique_ids(issues, where="issues"):
    seen, dup = set(), []
    for o in issues:
        key = str(o["id"])
        if key in seen and key not in dup:
            dup.append(key)
        seen.add(key)
    if dup:
        raise InputError(f"{where}: repeated issue id(s) {', '.join(dup)}; a paged read over a board "
                         "that changed between pages repeats items. Read again")


def is_naive(value):
    if not isinstance(value, str):
        return False
    try:
        return datetime.fromisoformat(value).tzinfo is None
    except ValueError:
        return False


def count_naive(issues):
    """Timestamps on the issues that carry no zone (read as UTC)."""
    n = 0
    for o in issues:
        for key in ("created_at", "updated_at") + HISTORY_KEYS:
            n += is_naive(o.get(key))
        for t in o.get("transitions") or []:
            n += is_naive(t.get("at")) if isinstance(t, dict) else 0
    return n


def validate_issue(obj, where):
    if not isinstance(obj, dict):
        raise InputError(f"{where}: an issue must be an object")
    missing = [k for k in REQUIRED_ISSUE_KEYS if k not in obj]
    if missing:
        raise InputError(f"{where}: missing required field(s): {', '.join(missing)}")
    if not isinstance(obj["id"], (str, int)) or isinstance(obj["id"], bool):
        raise InputError(f"{where}: id must be a string or number, got {obj['id']!r}")
    where = f"{where} (id {obj['id']})"
    status = obj["status"]
    if not isinstance(status, dict) or "name" not in status:
        raise InputError(f"{where}: status must be an object with a name")
    if status["name"] is not None and not isinstance(status["name"], str):
        raise InputError(f"{where}: status.name must be a string or null")
    if not isinstance(obj["labels"], list):
        raise InputError(f"{where}: labels must be a list")
    try:
        label_names(obj["labels"])
    except InputError as e:
        raise InputError(f"{where}: {e}") from None
    if obj.get("assignees") is not None and not isinstance(obj["assignees"], list):
        raise InputError(f"{where}: assignees must be a list or null")
    if "sprint" in obj:
        validate_sprint_field(obj["sprint"], where)
    if obj["description"] is not None and not isinstance(obj["description"], str):
        raise InputError(f"{where}: description must be a string or null")
    for key in ("created_at", "updated_at") + HISTORY_KEYS:
        if key in obj:
            parse_time(obj[key], f"{where}: {key}")
    trans = obj.get("transitions")
    if trans is not None:
        if not isinstance(trans, list):
            raise InputError(f"{where}: transitions must be a list or null")
        for j, t in enumerate(trans):
            if (not isinstance(t, dict) or not isinstance(t.get("status"), str)
                    or parse_time(t.get("at"), f"{where}: transitions[{j}].at") is None):
                raise InputError(f"{where}: transitions[{j}] must be {{status: string, at: ISO 8601}}")


def enrich_issue(obj, states, markers_cfg):
    out = dict(obj)
    if "kind" in obj:
        out["tool_kind"] = obj["kind"]
    out["kind"] = states.get(obj["status"]["name"])
    names = label_names(obj["labels"])
    markers = {}
    for marker in dict.fromkeys(KNOWN_MARKERS + tuple(markers_cfg)):
        how = markers_cfg.get(marker) or ""
        if how.startswith("label:"):
            markers[marker] = how[len("label:"):] in names
        elif how.startswith("status:"):
            markers[marker] = obj["status"]["name"] == how[len("status:"):]
        else:
            markers[marker] = None
    out["markers"] = markers
    return out


def _tri(value, where):
    if value is None or isinstance(value, bool):
        return value
    raise InputError(f"{where}: expected true, false or null, got {value!r}")


def scope_record(given, native, fetched, empty_ok):
    """The record of what the issue read was: `given` from the flags, `native` from the tool."""
    merged = {}
    for k in SCOPE_KEYS:
        a, b = (native or {}).get(k), (given or {}).get(k)
        if a is not None and b is not None and a != b:
            raise InputError(f"scope.{k}: the flag says {b!r}, the tool's snapshot says {a!r}")
        merged[k] = b if b is not None else a
    if merged["query"] is not None and not isinstance(merged["query"], str):
        raise InputError("scope.query must be a string")
    total = merged["reported_total"]
    if total is not None and (not isinstance(total, int) or isinstance(total, bool) or total < 0):
        raise InputError(f"scope.reported_total must be a non-negative integer, got {total!r}")
    complete = _tri(merged["complete"], "scope.complete")
    if total is not None:
        if complete is True and total != fetched:
            raise InputError(f"scope: complete, but the tool reported {total} issues and {fetched} were fetched")
        if complete is None:
            complete = total == fetched
    if fetched == 0 and not empty_ok:
        raise InputError("issues: the list is empty, which most often means the read failed or was not "
                         "made; pass --empty-ok if the scope is genuinely empty")
    return {"query": merged["query"], "fetched": fetched, "reported_total": total, "complete": complete,
            "includes_finished": _tri(merged["includes_finished"], "scope.includes_finished"),
            "empty_ok": bool(empty_ok)}


def history_file_name(issue_id):
    return re.sub(r"[^A-Za-z0-9._-]", "_", str(issue_id)) + ".json"


def load_history(directory, issues):
    """{str(id): history} from DIR/<id>.json; an issue without a file is absent from the result."""
    directory = Path(directory)
    if not directory.is_dir():
        raise InputError(f"--history {directory}: not a directory")
    names, out = {}, {}
    for o in issues if isinstance(issues, list) else []:
        if not isinstance(o, dict) or "id" not in o:
            continue
        name = history_file_name(o["id"])
        if names.get(name, str(o["id"])) != str(o["id"]):
            raise InputError(f"--history: ids {names[name]!r} and {o['id']!r} map to the same file {name}")
        names[name] = str(o["id"])
        path = directory / name
        if not path.is_file():
            continue
        data = load_json(path)
        if not isinstance(data, dict):
            raise InputError(f"{path}: expected a JSON object")
        unknown = [k for k in data if k not in HISTORY_FILE_KEYS + ("id",)]
        if unknown:
            raise InputError(f"{path}: unknown key(s) {', '.join(unknown)}; expected "
                             f"{', '.join(HISTORY_FILE_KEYS)}")
        if "id" in data and str(data["id"]) != str(o["id"]):
            raise InputError(f"{path}: id {data['id']!r} is not {o['id']!r}")
        out[str(o["id"])] = {k: v for k, v in data.items() if k != "id"}
    return out


def merge_history(issues, history):
    merged, missing = [], []
    for o in issues:
        h = history.get(str(o["id"]))
        if h is None:
            missing.append(o["id"])
            merged.append(o)
            continue
        o = dict(o)
        for k, v in h.items():
            if o.get(k) is not None and v is not None and o[k] != v:
                raise InputError(f"issue {o['id']}: {k} from --history ({v!r}) differs from the issue's "
                                 f"own ({o[k]!r})")
            if v is not None or k not in o:
                o[k] = v
        merged.append(o)
    return merged, {"merged": len(issues) - len(missing), "missing": {"count": len(missing), "ids": missing}}


def _build(issues, statuses, sprints, cfg, taken_at, source, tool, tool_version, *, scope=None,
           native_scope=None, empty_ok=False, taken_at_basis="given", atomic=False, history=None):
    if not isinstance(issues, list):
        raise InputError("issues: expected a JSON array")
    hist_info = None
    if history is not None:
        for i, obj in enumerate(issues):
            if not isinstance(obj, dict) or "id" not in obj:
                raise InputError(f"issues[{i}]: an issue must be an object with an id")
        issues, hist_info = merge_history(issues, history)
    for i, obj in enumerate(issues):
        validate_issue(obj, f"issues[{i}]")
    check_unique_ids(issues)
    record = scope_record(scope, native_scope, len(issues), empty_ok)
    states = cfg["states"]
    markers_cfg = cfg.get("markers", {})
    parse_time(taken_at, "taken_at")
    if taken_at is None:
        raise InputError("taken_at: required")

    seen = []
    if statuses is not None:
        if not isinstance(statuses, list):
            raise InputError("statuses: expected a JSON array")
        for i, s in enumerate(statuses):
            if not isinstance(s, dict) or not isinstance(s.get("name"), str):
                raise InputError(f"statuses[{i}]: expected an object with a string name")
            seen.append(s["name"])
    seen += [o["status"]["name"] for o in issues if o["status"]["name"] is not None]
    if sprints is not None and not isinstance(sprints, list):
        raise InputError("sprints: expected a JSON array")

    board = cfg.get("board", {})
    out = {
        "schema": SCHEMA,
        "taken_at": taken_at,
        "taken_at_basis": taken_at_basis,
        "source": source,
        "atomic": atomic,
        "tool": tool if tool is not None else board.get("tool"),
        "tool_version": tool_version if tool_version is not None else board.get("tool_version"),
        "scope": record,
        "mapping": dict(states),
        "unmapped_statuses": sorted({n for n in seen if n not in states}),
        "mapping_unknown_statuses": (sorted(n for n in states if n not in set(seen))
                                     if statuses is not None else None),
        "mapping_unknown_statuses_reason": None if statuses is not None else "statuses not read",
        "issues_without_status": [o["id"] for o in issues if o["status"]["name"] is None],
        "markers_unreadable": {m: v for m, v in markers_cfg.items()
                               if not v.startswith(("label:", "status:"))},
        "naive_timestamps": count_naive(issues),
        "sprints": sprints,
        "issues": [enrich_issue(o, states, markers_cfg) for o in issues],
    }
    if hist_info is not None:
        out["history"] = hist_info
    return out


def compose(issues, statuses, sprints, cfg, taken_at, *, scope=None, empty_ok=False,
            taken_at_basis="given", history=None):
    """Snapshot from separate reads. Not atomic: an edit between reads lands in it partly."""
    if statuses is None:
        raise InputError("statuses: required for a composed snapshot")
    return _build(issues, statuses, sprints, cfg, taken_at, "composed", None, None, scope=scope,
                  empty_ok=empty_ok, taken_at_basis=taken_at_basis, atomic=False, history=history)


def enrich_native(native, cfg, *, scope=None, empty_ok=False, history=None):
    """The tool's own snapshot: validate it and add kind and markers."""
    if not isinstance(native, dict):
        raise InputError("native snapshot: expected a JSON object")
    for key in ("taken_at", "issues"):
        if key not in native:
            raise InputError(f"native snapshot: missing required field: {key}")
    nscope = native.get("scope")
    if nscope is not None and not isinstance(nscope, dict):
        raise InputError("native snapshot: scope must be an object")
    atomic = native.get("atomic") if isinstance(native.get("atomic"), bool) else None
    return _build(native["issues"], native.get("statuses"), native.get("sprints"), cfg,
                  native["taken_at"], "native", native.get("tool"), native.get("tool_version"),
                  scope=scope, native_scope=nscope, empty_ok=empty_ok, taken_at_basis="tool",
                  atomic=atomic, history=history)


def summary(snap, out):
    by_kind = {}
    for o in snap["issues"]:
        if o["kind"] is not None:
            by_kind[o["kind"]] = by_kind.get(o["kind"], 0) + 1
    return {"out": out, "issues": len(snap["issues"]), "by_kind": by_kind,
            "unmapped": sum(1 for o in snap["issues"] if o["kind"] is None),
            "unmapped_statuses": snap["unmapped_statuses"],
            "issues_without_status": snap["issues_without_status"],
            "mapping_unknown_statuses": snap["mapping_unknown_statuses"],
            "scope_complete": snap["scope"]["complete"], "taken_at_basis": snap["taken_at_basis"],
            "naive_timestamps": snap["naive_timestamps"]}


def _bool_flag(text):
    if text not in ("true", "false"):
        raise argparse.ArgumentTypeError("expected true or false")
    return text == "true"


def _count_flag(text):
    if not text.isdigit():
        raise argparse.ArgumentTypeError("expected a non-negative integer")
    return int(text)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--config", required=True)
    p.add_argument("--issues")
    p.add_argument("--statuses")
    p.add_argument("--sprints")
    p.add_argument("--native")
    p.add_argument("--taken-at", help="when the reads were made (ISO 8601); default now, UTC, "
                                      "recorded as taken_at_basis script_run_time")
    p.add_argument("--scope", help="the query or filter that produced the issue read")
    p.add_argument("--complete", type=_bool_flag, help="true|false: the tool reported the read complete")
    p.add_argument("--reported-total", type=_count_flag, help="the total the tool reported for the query")
    p.add_argument("--includes-finished", type=_bool_flag, help="true|false: the query returns finished work")
    p.add_argument("--empty-ok", action="store_true", help="an empty issue list is genuine")
    p.add_argument("--history", help="directory of per-issue history files, <id>.json")
    p.add_argument("--out")
    a = p.parse_args(argv)
    scope = {"query": a.scope, "complete": a.complete, "reported_total": a.reported_total,
             "includes_finished": a.includes_finished}
    try:
        cfg = load_config(a.config)
        if a.native:
            if a.issues or a.statuses or a.sprints or a.taken_at:
                raise InputError("--native takes no --issues/--statuses/--sprints/--taken-at")
            native = load_json(a.native)
            hist = (load_history(a.history, native.get("issues") if isinstance(native, dict) else None)
                    if a.history else None)
            snap = enrich_native(native, cfg, scope=scope, empty_ok=a.empty_ok, history=hist)
        else:
            if not a.issues or not a.statuses:
                raise InputError("a composed snapshot needs --issues and --statuses (or pass --native)")
            basis = "given" if a.taken_at else "script_run_time"
            taken = a.taken_at or datetime.now(timezone.utc).isoformat(timespec="seconds")
            issues = load_json(a.issues)
            hist = load_history(a.history, issues) if a.history else None
            snap = compose(issues, load_json(a.statuses),
                           load_json(a.sprints) if a.sprints else None, cfg, taken, scope=scope,
                           empty_ok=a.empty_ok, taken_at_basis=basis, history=hist)
    except InputError as e:
        print(f"snapshot.py: error: {e}", file=sys.stderr)
        return 2
    text = json.dumps(snap, ensure_ascii=False, indent=2)
    if a.out:
        Path(a.out).write_text(text + "\n", encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
        print(json.dumps(summary(snap, a.out), ensure_ascii=False), file=sys.stderr)
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
