"""Compose or enrich the task-master snapshot of a board scope.

The skill runs the board reads with the commands recorded in `.claude/task-master.toml` and hands
this script the results as files. The script reads no board and runs no tool.

Composed (the tool has no snapshot of its own):
    snapshot.py --issues issues.json --statuses statuses.json [--sprints sprints.json]
                --config .claude/task-master.toml [--taken-at ISO] [--out snapshot.json]
Native (the tool wrote a snapshot):
    snapshot.py --native tool-snapshot.json --config .claude/task-master.toml [--out snapshot.json]

Normalized issue: the shape the plugin expects from any tool, whichever tool produced it.
    {id, kind, url, title, description, type, status{name, category}, assignees[{id, name}],
     labels[], priority, parent, subtasks[], links[{type, id}], sprint, milestone, due_date,
     author{id, name}, created_at, updated_at}
  Required keys: REQUIRED_ISSUE_KEYS. A key the board has no value for is present and null; null
  stays null here. `labels` items are strings or objects with `name`. Timestamps are ISO 8601;
  one without a zone is read as UTC.
  Optional native history, used only when the tool reports it:
    status_since  - when the issue entered its current status
    finished_at   - when it reached a finished status
  `updated_at` is never a substitute for either.
  The tool's own `kind` (if any) is kept as `tool_kind`; `kind` becomes the plugin's kind.

Statuses: array of {name, ...}. Sprints: array of {id, name, state, start_date, end_date}.

Snapshot written:
    {schema: 1, taken_at, source: "composed"|"native", tool, tool_version, mapping,
     unmapped_statuses[], mapping_unknown_statuses[], issues_without_status[], sprints, issues[]}
  Each issue gains `kind` (from [states]; null when unmapped, never guessed) and `markers`
  (true/false for a marker declared as `label:<name>` or `status:<name>`; null when the board
  cannot show it or shows it some other way, which these files do not carry).

Malformed input or a missing required key: exit 2, message on stderr, nothing on stdout.
"""

from __future__ import annotations

import argparse
import json
import sys
import tomllib
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = 1
KINDS = ("before_start", "queued", "active", "handed_off", "finished")
KNOWN_MARKERS = ("blocked", "waiting", "untriaged", "abandoned")
REQUIRED_ISSUE_KEYS = ("id", "title", "description", "status", "labels", "created_at", "updated_at")
HISTORY_KEYS = ("status_since", "finished_at")


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
    return cfg


def label_names(labels):
    names = set()
    for lab in labels:
        if isinstance(lab, str):
            names.add(lab)
        elif isinstance(lab, dict) and isinstance(lab.get("name"), str):
            names.add(lab["name"])
    return names


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
    if obj["description"] is not None and not isinstance(obj["description"], str):
        raise InputError(f"{where}: description must be a string or null")
    for key in ("created_at", "updated_at") + HISTORY_KEYS:
        if key in obj:
            parse_time(obj[key], f"{where}: {key}")


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


def _build(issues, statuses, sprints, cfg, taken_at, source, tool, tool_version):
    if not isinstance(issues, list):
        raise InputError("issues: expected a JSON array")
    for i, obj in enumerate(issues):
        validate_issue(obj, f"issues[{i}]")
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
    return {
        "schema": SCHEMA,
        "taken_at": taken_at,
        "source": source,
        "tool": tool if tool is not None else board.get("tool"),
        "tool_version": tool_version if tool_version is not None else board.get("tool_version"),
        "mapping": dict(states),
        "unmapped_statuses": sorted({n for n in seen if n not in states}),
        "mapping_unknown_statuses": sorted(n for n in states if n not in set(seen)) if statuses is not None else [],
        "issues_without_status": [o["id"] for o in issues if o["status"]["name"] is None],
        "sprints": sprints,
        "issues": [enrich_issue(o, states, markers_cfg) for o in issues],
    }


def compose(issues, statuses, sprints, cfg, taken_at):
    """Snapshot from separate reads. Not atomic: an edit between reads lands in it partly."""
    if statuses is None:
        raise InputError("statuses: required for a composed snapshot")
    return _build(issues, statuses, sprints, cfg, taken_at, "composed", None, None)


def enrich_native(native, cfg):
    """The tool's own snapshot: validate it and add kind and markers."""
    if not isinstance(native, dict):
        raise InputError("native snapshot: expected a JSON object")
    for key in ("taken_at", "issues"):
        if key not in native:
            raise InputError(f"native snapshot: missing required field: {key}")
    return _build(native["issues"], native.get("statuses"), native.get("sprints"), cfg,
                  native["taken_at"], "native", native.get("tool"), native.get("tool_version"))


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument("--config", required=True)
    p.add_argument("--issues")
    p.add_argument("--statuses")
    p.add_argument("--sprints")
    p.add_argument("--native")
    p.add_argument("--taken-at", help="when the reads were made (ISO 8601); default now, UTC")
    p.add_argument("--out")
    a = p.parse_args(argv)
    try:
        cfg = load_config(a.config)
        if a.native:
            if a.issues or a.statuses or a.sprints:
                raise InputError("--native takes no --issues/--statuses/--sprints")
            snap = enrich_native(load_json(a.native), cfg)
        else:
            if not a.issues or not a.statuses:
                raise InputError("a composed snapshot needs --issues and --statuses (or pass --native)")
            taken = a.taken_at or datetime.now(timezone.utc).isoformat(timespec="seconds")
            snap = compose(load_json(a.issues), load_json(a.statuses),
                           load_json(a.sprints) if a.sprints else None, cfg, taken)
    except InputError as e:
        print(f"snapshot.py: error: {e}", file=sys.stderr)
        return 2
    text = json.dumps(snap, ensure_ascii=False, indent=2)
    if a.out:
        Path(a.out).write_text(text + "\n", encoding="utf-8")
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
