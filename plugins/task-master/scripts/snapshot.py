"""Compose or enrich the task-master snapshot of a board scope.

The skill runs the board reads with the board tool and hands this script the results as files,
with --settings naming the project's workflow settings (TOML; the file the project's agent
instructions name, else workflow.toml, or a draft holding only [board] tables while init sets the
project up). The script reads no board and runs no tool.

Composed (the tool has no snapshot of its own):
    snapshot.py --issues issues.json --statuses statuses.json [--sprints sprints.json]
                --settings workflow.toml [--taken-at ISO] [--out snapshot.json]
                [--tool NAME] [--tool-version V] [scope flags] [--history DIR]
Native (the tool wrote a snapshot):
    snapshot.py --native tool-snapshot.json --settings workflow.toml [--out snapshot.json]
                [--tool NAME] [--tool-version V] [scope flags] [--history DIR]
--tool/--tool-version: recorded as the snapshot's tool and tool_version (null when not given; a
  native snapshot's own claim is used, and a flag that contradicts it is an error). [board]
  belongs to the board tool and is not read for them.
Settings: [process] and its tables have closed key sets (an unknown key, e.g. a misspelt one or
  a [process.limits] table, is an error, as is a marker other than blocked, waiting, untriaged,
  abandoned). A file with no [process] is accepted (a draft); a [process] that is present needs
  setup = "iterations"|"flow"; commitment, executor and ceiling (a key of [board.size]) are
  checked when given; a [board.size] key may not be a marker's label.
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
  A file may instead hold a history read with since and moves, as written:
  {id?, status?{name}, since, moves[{from, to{name}, at, by?}]}. `since` becomes status_since
  (null: unknown), each move's to.name and at a transition, opened by the first move's `from`
  at created_at (no moves: the issue's status, unless since is later); started_at and finished_at are left
  to be derived from the transitions. A `status` other than the issue's is an error (the issue
  moved between the reads). One file holds one shape, never keys of both.

Normalized issue: the shape the plugin expects from any tool, whichever tool produced it.
    {id, kind, url, title, description, type, status{name, category}, assignees[{id, name}],
     labels[], priority, parent, subtasks[], links[{type, id}], sprint, milestone, due_date,
     author{id, name}, created_at, updated_at}
  Required keys: REQUIRED_ISSUE_KEYS. status.category is todo, in_progress, done, canceled or
  null (absent is null). A key the board has no value for is present and null; null
  stays null here. `labels` items are strings or objects with a string `name`; anything else is
  an error. `assignees` is a list or null. `sprint` is null, a string or number, or an object
  with `id` and/or `name`; a list (every sprint the item was in) is an error: the adapter
  passes the one sprint the item counts in. Ids must be unique (a repeat is an error). Timestamps
  are ISO 8601; one without a zone is read as UTC and counted in naive_timestamps.
  Optional native history, used only when the tool reports it (a tool with native history
  supplies these; without them the history-dependent figures are null with the reason):
    status_since  - when the issue entered its current status
    started_at    - when it first entered a started state; cycle time runs from it when the
                    issue has no transitions (then from the first transition into a started
                    status, see board_metrics.py). status_since of a finished issue is when it
                    finished, so it cannot stand in
    finished_at   - when it reached a finished status
    transitions   - [{status, at}], every status the issue entered and when, its first status
                    included; a cumulative flow chart needs it on every issue. A status the board
                    has no name for is {status: null, category, at}
  `updated_at` is never a substitute for any of them.
  The tool's own `kind` (if any) is kept as `tool_kind`; `kind` becomes the plugin's kind.

Statuses: array of {name, category?, ...}, category as on an issue.
Sprints: array of {id, name, state, start_date, end_date}.

Snapshot written:
    {schema: 1, taken_at, taken_at_basis: "given"|"script_run_time"|"tool",
     source: "composed"|"native", atomic, tool, tool_version,
     scope{query, fetched, reported_total, complete, includes_finished, empty_ok},
     mapping{status: kind}, mapping_sources{status: "process.kinds"|"review_statuses"|"category"},
     unmapped_statuses[], mapping_unknown_statuses[]|null, mapping_unknown_statuses_reason,
     category_conflicts[{status, categories[]}], issues_without_status[],
     marker_specs{marker: {spec, source: "settings"|"default"|"category"}},
     markers_unknown_statuses[]|null, markers_undeclared[{marker, label}],
     markers_undeclared_reason, naive_timestamps,
     history{merged, missing} (with --history only), sprints, issues[]}
  atomic: false for a composed snapshot; for a native one the tool's own `atomic` claim, else
  null.
  Category of a status: one per status, from the statuses read, else the first issue that gives
  one; every category seen for a status that disagrees is listed in category_conflicts. Issue
  kinds and mapping both use this one category, so they never differ.
  Kind of a status, first match wins: its entry in [process.kinds]; handed_off if in
  [process].review_statuses; else by category (todo -> before_start, in_progress -> active,
  done and canceled -> finished); else null, never guessed. An entry that would make a done or
  canceled status unfinished is an error. mapping holds every status seen
  (statuses read and issues) or declared in [process.kinds]/review_statuses that has a kind;
  unmapped_statuses those seen without one. mapping_unknown_statuses: names in [process.kinds]
  or review_statuses the board does not have; null when the board's statuses were not read.
  Each issue gains `kind` and `markers`. blocked, waiting and untriaged come from
  [process.markers] (defaults "blocked", "needs-info", "needs-triage"): a plain value is a label
  name (true when the issue carries it), "status:<name>" a column (true when the issue is in it).
  abandoned is true for category canceled (or a declared abandoned marker that holds), false for
  any other category or when a declared marker does not hold, null when the category is null and
  none is declared. A value written "label:..." or with Status:/STATUS:, or a name with
  surrounding spaces, is a settings error. marker_specs says how each marker was read and where
  the spec came from (abandoned: category canceled, plus a declared spec if any).
  markers_unknown_statuses: "status:<name>" markers naming a status not seen (statuses read and
  issues); null when the board's statuses were not read.
  markers_undeclared: label markers whose label is not in [board.labels], so the board cannot show
  them yet; with no [board.labels] every label marker is listed and markers_undeclared_reason
  says so (else null).

With --out, a one-line JSON summary goes to stderr: issue counts by kind, unmapped issues,
unmapped statuses, issues without a status, mapping entries the board lacks, undeclared markers,
marker columns the board lacks, statuses with conflicting categories, whether the scope is
complete, taken_at_basis and naive_timestamps.

Malformed input or a missing required key: exit 2, message on stderr, nothing on stdout.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
import tomllib
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = 1
KINDS = ("before_start", "queued", "active", "handed_off", "finished")
CATEGORIES = ("todo", "in_progress", "done", "canceled")
CATEGORY_KINDS = {"todo": "before_start", "in_progress": "active", "done": "finished", "canceled": "finished"}
DEFAULT_MARKERS = {"blocked": "blocked", "waiting": "needs-info", "untriaged": "needs-triage"}
MARKER_KEYS = ("blocked", "waiting", "untriaged", "abandoned")
PROCESS_KEYS = ("setup", "period_days", "sle", "review_statuses", "ceiling", "doc", "commitment",
                "executor", "timezone", "acceptance_headings", "wip", "markers", "kinds")
SETUPS = ("iterations", "flow")
COMMITMENTS = ("goal", "selection")
EXECUTORS = ("agent", "people", "mixed")
NOT_SETTINGS = "this does not look like the project's workflow settings: no [process] with setup"
UNFINISHED_CATEGORIES = ("done", "canceled")
REQUIRED_ISSUE_KEYS = ("id", "title", "description", "status", "labels", "created_at", "updated_at")
HISTORY_KEYS = ("status_since", "started_at", "finished_at")
HISTORY_FILE_KEYS = HISTORY_KEYS + ("transitions",)
MOVES_FILE_KEYS = ("status", "since", "moves")
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


def load_settings(path):
    """The project's workflow settings (TOML), validated by validate_settings."""
    try:
        cfg = tomllib.loads(Path(path).read_text(encoding="utf-8"))
    except OSError as e:
        raise InputError(f"{path}: cannot read: {e}") from None
    except tomllib.TOMLDecodeError as e:
        raise InputError(f"{path}: malformed TOML: {e}") from None
    try:
        validate_settings(cfg)
    except InputError as e:
        raise InputError(f"{path}: {e}") from None
    return cfg


def _table(value, name):
    if not isinstance(value, dict):
        raise InputError(f"{name} must be a table")
    return value


def _one_of(table, key, allowed, section="[process]"):
    v = table.get(key)
    if v is not None and v not in allowed:
        raise InputError(f"{section}.{key} = {v!r}: expected one of {', '.join(allowed)}")


def validate_settings(cfg, *, require_process=False):
    """Check what task-master reads from the settings. [process] and its tables have closed key
    sets; [board] belongs to the board tool, so only [board.labels] and [board.size] are checked.
    Without require_process, a file with no [process] at all is accepted (init has not written it
    yet); a [process] that is present needs a valid setup either way."""
    _table(cfg, "settings")
    board = _table(cfg.get("board", {}), "[board]")
    if "process" not in cfg:
        if require_process:
            raise InputError(NOT_SETTINGS)
        process = {}
    else:
        process = _table(cfg["process"], "[process]")
        unknown = [k for k in process if k not in PROCESS_KEYS]
        if unknown:
            raise InputError(f"unknown key {unknown[0]} in [process]; expected {', '.join(PROCESS_KEYS)}")
        if "setup" not in process:
            raise InputError(NOT_SETTINGS if require_process else "[process] has no setup; expected "
                             f"setup = {' or '.join(map(repr, SETUPS))}")
        _one_of(process, "setup", SETUPS)
        _one_of(process, "commitment", COMMITMENTS)
        _one_of(process, "executor", EXECUTORS)
    kinds = _table(process.get("kinds", {}), "[process.kinds]")
    for name, kind in kinds.items():
        if kind not in KINDS:
            raise InputError(f"[process.kinds] {name!r} = {kind!r}: kind must be one of {', '.join(KINDS)}")
    review = process.get("review_statuses", [])
    if not isinstance(review, list) or not all(isinstance(s, str) for s in review):
        raise InputError("[process].review_statuses must be a list of status names")
    _table(process.get("wip", {}), "[process.wip]")
    markers = _table(process.get("markers", {}), "[process.markers]")
    unknown = [k for k in markers if k not in MARKER_KEYS]
    if unknown:
        raise InputError(f"unknown key {unknown[0]} in [process.markers]; expected {', '.join(MARKER_KEYS)}")
    for marker, spec in markers.items():
        if not isinstance(spec, str):
            raise InputError(f"[process.markers] {marker} must be a string")
        prefix, sep, name = spec.partition(":")
        if not spec.strip():
            raise InputError(f"[process.markers] {marker} is empty")
        if sep and prefix.lower() == "status" and (prefix != "status" or not name or name != name.strip()):
            raise InputError(f"[process.markers] {marker} = {spec!r}: a column is written "
                             "\"status:<name>\", the name exactly as the board shows it")
        if sep and prefix.lower() == "label":
            raise InputError(f"[process.markers] {marker} = {spec!r}: a label is written as its "
                             "plain name, without label:")
        if not sep and spec != spec.strip():
            raise InputError(f"[process.markers] {marker} = {spec!r}: a label name has no surrounding spaces")
    labels = board.get("labels")
    if labels is not None and not isinstance(labels, (dict, list)):
        raise InputError("[board.labels] must be a table of label names")
    size = board.get("size")
    if size is not None:
        if not isinstance(size, dict) or not size:
            raise InputError("[board.size] must be a non-empty table of label = number")
        for key, v in size.items():
            if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) or v < 0:
                raise InputError(f"[board.size] {key!r} = {v!r}: a size must be a non-negative number")
        clash = [f"{m} = {n!r}" for m, (via, n) in marker_specs(cfg).items() if via == "label" and n in size]
        if clash:
            raise InputError(f"[board.size] has a key that is also a marker label ({', '.join(clash)}): "
                             "one label cannot be both an estimate and a marker")
        if "ceiling" in process and process["ceiling"] not in size:
            raise InputError(f"[process].ceiling = {process['ceiling']!r} is not a key of [board.size]")
    return cfg


def marker_specs(cfg):
    """{marker: ("label"|"status", name)} with the defaults filled in; abandoned only if declared."""
    return {m: (("status", spec[len("status:"):]) if spec.startswith("status:") else ("label", spec))
            for m, (spec, _) in marker_sources(cfg).items()}


def marker_sources(cfg):
    """{marker: (spec as written, "settings"|"default")}; abandoned only if declared."""
    declared = ((cfg.get("process") or {}).get("markers") or {})
    out = {}
    for marker in dict.fromkeys(tuple(DEFAULT_MARKERS) + tuple(declared)):
        if marker in declared:
            out[marker] = (declared[marker], "settings")
        else:
            out[marker] = (DEFAULT_MARKERS[marker], "default")
    return out


def marker_specs_out(cfg):
    """The marker_specs snapshot key: {marker: {spec, source}}."""
    specs = marker_specs(cfg)
    srcs = marker_sources(cfg)
    out = {m: {"spec": f"{via}:{what}", "source": srcs[m][1]} for m, (via, what) in specs.items()}
    if "abandoned" in out:
        out["abandoned"]["spec"] += " or category:canceled"
    else:
        out["abandoned"] = {"spec": "category:canceled", "source": "category"}
    return out


def board_label_names(cfg):
    """Label names in [board.labels], or None when the table is absent."""
    labels = (cfg.get("board") or {}).get("labels")
    if labels is None:
        return None
    if isinstance(labels, dict):
        return set(labels)
    return {lab if isinstance(lab, str) else lab.get("name") for lab in labels
            if isinstance(lab, str) or isinstance(lab, dict)}


def markers_undeclared(cfg, specs):
    names = board_label_names(cfg)
    items = [{"marker": m, "label": n} for m, (via, n) in specs.items()
             if via == "label" and (names is None or n not in names)]
    reason = ("no [board.labels] in settings: whether the board has these labels cannot be told"
              if names is None else None)
    return items, reason


class KindRules:
    """How a status's kind is decided: [process.kinds], then review_statuses, then category."""

    def __init__(self, cfg):
        process = cfg.get("process") or {}
        self.kinds = dict(process.get("kinds") or {})
        self.review = list(process.get("review_statuses") or [])

    def kind(self, name, category):
        """-> (kind or None, source)."""
        if name in self.kinds:
            return self.kinds[name], "process.kinds"
        if name in self.review:
            return "handed_off", "review_statuses"
        if category is not None:
            return CATEGORY_KINDS[category], "category"
        return None, None

    def declared(self):
        return list(dict.fromkeys(list(self.kinds) + self.review))


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


def check_category(value, where):
    if value is not None and value not in CATEGORIES:
        raise InputError(f"{where}: expected one of {', '.join(CATEGORIES)} or null, got {value!r}")


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
    check_category(status.get("category"), f"{where}: status.category")
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
            named = isinstance(t, dict) and (isinstance(t.get("status"), str) or (
                t.get("status") is None and t.get("category") in CATEGORY_KINDS))
            if not named or parse_time(t.get("at"), f"{where}: transitions[{j}].at") is None:
                raise InputError(f"{where}: transitions[{j}] must be {{status: string, or null with a "
                                 "category, at: ISO 8601}}")


def enrich_issue(obj, rules, specs, categories):
    out = dict(obj)
    if "kind" in obj:
        out["tool_kind"] = obj["kind"]
    name = obj["status"]["name"]
    category = categories.get(name) if name is not None else obj["status"].get("category")
    # A status with no name still has the board's category (GitLab: closed, its label gone).
    out["kind"] = rules.kind(name, category)[0] if name is not None else CATEGORY_KINDS.get(category)
    names = label_names(obj["labels"])
    markers = {}
    for marker, (via, what) in specs.items():
        markers[marker] = what in names if via == "label" else name == what
    if category == "canceled" or markers.get("abandoned") is True:
        markers["abandoned"] = True
    elif category is not None or "abandoned" in specs:
        markers["abandoned"] = False
    else:
        markers["abandoned"] = None
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


def from_moves(data, issue, path):
    """A history read with since and moves, as status_since and transitions.

    {id?, status?{name}, since, moves[{from, to{name}, at, by?}]}: `since` is when the issue
    entered its current status (null when the moves do not end in it); each move's `to.name` and
    `at` is a transition. The status the issue was created in opens the transitions at
    created_at: the first move's `from` when it has one; with no moves, the current status
    unless `since` says the issue entered it after creation."""
    mixed = [k for k in data if k not in MOVES_FILE_KEYS + ("id",)]
    if mixed:
        raise InputError(f"{path}: {', '.join(mixed)} beside since/moves; a history file holds one shape")
    status = data.get("status")
    if status is not None:
        name = status.get("name") if isinstance(status, dict) else status
        if name != issue["status"]["name"]:
            raise InputError(f"{path}: the history read shows status {name!r}, the issue read "
                             f"{issue['status']['name']!r}: the issue moved between the reads; read both again")
    moves = data.get("moves")
    if moves is not None and not isinstance(moves, list):
        raise InputError(f"{path}: moves must be a list or null")
    transitions = []
    for j, m in enumerate(moves or []):
        to = m.get("to") if isinstance(m, dict) else None
        # A status the board has no name for (GitLab: a closed issue whose status label is gone)
        # comes as name null with its category; it is kept as such, not given a name.
        nameless = (isinstance(to, dict) and to.get("name") is None
                    and to.get("category") in CATEGORY_KINDS)
        if not isinstance(to, dict) or not (isinstance(to.get("name"), str) or nameless):
            raise InputError(f"{path}: moves[{j}] must be {{to: {{name: string, or null with a "
                             "category}}, at: ISO 8601}}")
        if parse_time(m.get("at"), f"{path}: moves[{j}].at") is None:
            raise InputError(f"{path}: moves[{j}].at is missing")
        t = {"status": to["name"], "at": m["at"]}
        if nameless:
            t["category"] = to["category"]
        transitions.append(t)
    created = issue.get("created_at")
    if moves is not None and created is not None:
        first = moves[0].get("from") if moves else None
        start = first.get("name") if isinstance(first, dict) else first
        since = data.get("since")
        if not moves and (since is None or parse_time(since, f"{path}: since")
                          == parse_time(created, f"{path}: created_at")):
            start = issue["status"]["name"]
        if isinstance(start, str):
            transitions.insert(0, {"status": start, "at": created})
    out ={"transitions": transitions if moves is not None else None, "status_since": data.get("since")}
    if "id" in data:
        out["id"] = data["id"]
    return out


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
        if any(k in data for k in MOVES_FILE_KEYS):
            data = from_moves(data, o, path)
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
    validate_settings(cfg)
    rules = KindRules(cfg)
    specs = marker_specs(cfg)
    parse_time(taken_at, "taken_at")
    if taken_at is None:
        raise InputError("taken_at: required")

    seen_cats = {}  # every status seen (statuses read, then issues) -> categories in the order seen
    if statuses is not None:
        if not isinstance(statuses, list):
            raise InputError("statuses: expected a JSON array")
        for i, s in enumerate(statuses):
            if not isinstance(s, dict) or not isinstance(s.get("name"), str):
                raise InputError(f"statuses[{i}]: expected an object with a string name")
            check_category(s.get("category"), f"statuses[{i}] ({s['name']}): category")
            seen_cats.setdefault(s["name"], []).append(s.get("category"))
    for o in issues:
        name = o["status"]["name"]
        if name is not None:
            seen_cats.setdefault(name, []).append(o["status"].get("category"))
    # one category per status: the statuses read win, else the first issue's; issue kinds and the
    # mapping both come from it, so they never disagree
    categories, conflicts = {}, []
    for name, cats in seen_cats.items():
        distinct = list(dict.fromkeys(c for c in cats if c is not None))
        if distinct:
            categories[name] = distinct[0]
        if len(distinct) > 1:
            conflicts.append({"status": name, "categories": distinct})
    for name in rules.declared():
        kind, src = rules.kind(name, categories.get(name))
        if categories.get(name) in UNFINISHED_CATEGORIES and kind != "finished":
            where = "[process.kinds]" if src == "process.kinds" else "[process].review_statuses"
            raise InputError(f"{where} makes {name!r} {kind}, but its category is {categories[name]}: "
                             "work there is finished")
    known = seen_cats
    seen = list(known)
    mapping, mapping_sources, unmapped = {}, {}, []
    for name in seen + [n for n in rules.declared() if n not in known]:
        kind, src = rules.kind(name, categories.get(name))
        if kind is None:
            unmapped.append(name)
        else:
            mapping[name], mapping_sources[name] = kind, src
    if sprints is not None and not isinstance(sprints, list):
        raise InputError("sprints: expected a JSON array")
    undeclared, undeclared_reason = markers_undeclared(cfg, specs)
    marker_columns = [n for via, n in specs.values() if via == "status"]

    out = {
        "schema": SCHEMA,
        "taken_at": taken_at,
        "taken_at_basis": taken_at_basis,
        "source": source,
        "atomic": atomic,
        "tool": tool,
        "tool_version": tool_version,
        "scope": record,
        "mapping": mapping,
        "mapping_sources": mapping_sources,
        "unmapped_statuses": sorted(unmapped),
        "mapping_unknown_statuses": (sorted(n for n in rules.declared() if n not in known)
                                     if statuses is not None else None),
        "mapping_unknown_statuses_reason": None if statuses is not None else "statuses not read",
        "category_conflicts": conflicts,
        "issues_without_status": [o["id"] for o in issues if o["status"]["name"] is None],
        "marker_specs": marker_specs_out(cfg),
        "markers_unknown_statuses": (sorted({n for n in marker_columns if n not in known})
                                     if statuses is not None else None),
        "markers_undeclared": undeclared,
        "markers_undeclared_reason": undeclared_reason,
        "naive_timestamps": count_naive(issues),
        "sprints": sprints,
        "issues": [enrich_issue(o, rules, specs, categories) for o in issues],
    }
    if hist_info is not None:
        out["history"] = hist_info
    return out


def compose(issues, statuses, sprints, cfg, taken_at, *, scope=None, empty_ok=False,
            taken_at_basis="given", history=None, tool=None, tool_version=None):
    """Snapshot from separate reads. Not atomic: an edit between reads lands in it partly."""
    if statuses is None:
        raise InputError("statuses: required for a composed snapshot")
    return _build(issues, statuses, sprints, cfg, taken_at, "composed", tool, tool_version, scope=scope,
                  empty_ok=empty_ok, taken_at_basis=taken_at_basis, atomic=False, history=history)


def _claim(name, native, flag):
    if native is not None and flag is not None and native != flag:
        raise InputError(f"{name}: the flag says {flag!r}, the tool's snapshot says {native!r}")
    return native if native is not None else flag


def enrich_native(native, cfg, *, scope=None, empty_ok=False, history=None, tool=None, tool_version=None):
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
                  native["taken_at"], "native", _claim("tool", native.get("tool"), tool),
                  _claim("tool_version", native.get("tool_version"), tool_version),
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
            "markers_undeclared": [m["marker"] for m in snap["markers_undeclared"]],
            "markers_unknown_statuses": snap["markers_unknown_statuses"],
            "category_conflicts": [c["status"] for c in snap["category_conflicts"]],
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
    p.add_argument("--settings", required=True, help="the project's workflow settings (TOML)")
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
    p.add_argument("--history", help="directory of per-issue history files, <id>.json (id characters "
                                     "outside A-Za-z0-9._- become _), each holding either "
                                     "status_since/started_at/finished_at/transitions[{status, at}] or "
                                     "a history read as written: since, moves[{from, to{name}, at}]")
    p.add_argument("--tool", help="the board tool's name, recorded in the snapshot")
    p.add_argument("--tool-version", help="the board tool's version, recorded in the snapshot")
    p.add_argument("--out")
    a = p.parse_args(argv)
    scope = {"query": a.scope, "complete": a.complete, "reported_total": a.reported_total,
             "includes_finished": a.includes_finished}
    try:
        cfg = load_settings(a.settings)
        if a.native:
            if a.issues or a.statuses or a.sprints or a.taken_at:
                raise InputError("--native takes no --issues/--statuses/--sprints/--taken-at")
            native = load_json(a.native)
            hist = (load_history(a.history, native.get("issues") if isinstance(native, dict) else None)
                    if a.history else None)
            snap = enrich_native(native, cfg, scope=scope, empty_ok=a.empty_ok, history=hist,
                                 tool=a.tool, tool_version=a.tool_version)
        else:
            if not a.issues or not a.statuses:
                raise InputError("a composed snapshot needs --issues and --statuses (or pass --native)")
            basis = "given" if a.taken_at else "script_run_time"
            taken = a.taken_at or datetime.now(timezone.utc).isoformat(timespec="seconds")
            issues = load_json(a.issues)
            hist = load_history(a.history, issues) if a.history else None
            snap = compose(issues, load_json(a.statuses),
                           load_json(a.sprints) if a.sprints else None, cfg, taken, scope=scope,
                           empty_ok=a.empty_ok, taken_at_basis=basis, history=hist,
                           tool=a.tool, tool_version=a.tool_version)
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
