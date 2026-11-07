import json
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
import snapshot  # noqa: E402

SCRIPT = Path(__file__).parent / "snapshot.py"

CONFIG = """
version = 1
[board]
tool = "sometool"
tool_version = "0.1.0"
[states]
"Backlog" = "before_start"
"In Progress" = "active"
"Done" = "finished"
[markers]
blocked = "label:blocked"
waiting = "field:flagged"
"""


def issue(id="1", status="In Progress", labels=None, **over):
    base = {
        "id": id, "kind": "issue", "url": None, "title": "t", "description": "d",
        "type": None, "status": {"name": status, "category": None},
        "assignees": [], "labels": labels if labels is not None else [],
        "priority": None, "parent": None, "subtasks": [], "links": [],
        "sprint": None, "milestone": None, "due_date": None, "author": None,
        "created_at": "2026-01-01T00:00:00Z", "updated_at": "2026-01-05T00:00:00Z",
    }
    base.update(over)
    return base


STATUSES = [{"id": "s1", "name": "Backlog", "category": "todo"},
            {"id": "s2", "name": "In Progress", "category": "in_progress"},
            {"id": "s3", "name": "Done", "category": "done"},
            {"id": "s4", "name": "QA", "category": None}]


@pytest.fixture
def cfg(tmp_path):
    p = tmp_path / "task-master.toml"
    p.write_text(CONFIG, encoding="utf-8")
    return snapshot.load_config(p)


def compose(cfg, issues, statuses=STATUSES, sprints=None):
    return snapshot.compose(issues, statuses, sprints, cfg, "2026-02-01T00:00:00Z")


def test_composed_header(cfg):
    s = compose(cfg, [issue()])
    assert s["schema"] == 1
    assert s["source"] == "composed"
    assert s["taken_at"] == "2026-02-01T00:00:00Z"
    assert s["tool"] == "sometool" and s["tool_version"] == "0.1.0"
    assert s["mapping"]["Done"] == "finished"


def test_kind_from_states(cfg):
    s = compose(cfg, [issue(status="Backlog")])
    assert s["issues"][0]["kind"] == "before_start"


def test_tool_kind_is_kept_aside(cfg):
    s = compose(cfg, [issue()])
    assert s["issues"][0]["tool_kind"] == "issue"


def test_unmapped_status_kept_and_listed(cfg):
    s = compose(cfg, [issue(id="9", status="Triage")])
    assert s["issues"][0]["id"] == "9"
    assert s["issues"][0]["kind"] is None
    assert "Triage" in s["unmapped_statuses"]
    # a board status with no mapping is listed too, even if no issue sits in it
    assert "QA" in s["unmapped_statuses"]
    assert "Done" not in s["unmapped_statuses"]


def test_null_status_name_is_not_guessed(cfg):
    s = compose(cfg, [issue(id="7", status=None)])
    assert s["issues"][0]["kind"] is None
    assert s["issues_without_status"] == ["7"]


def test_mapping_naming_absent_status_is_reported(tmp_path):
    p = tmp_path / "c.toml"
    p.write_text(CONFIG.replace('"Done" = "finished"', '"Done" = "finished"\n"Gone" = "queued"'),
                 encoding="utf-8")
    s = compose(snapshot.load_config(p), [issue()])
    assert s["mapping_unknown_statuses"] == ["Gone"]


def test_label_marker_recognised_other_left_null(cfg):
    s = compose(cfg, [issue(labels=["blocked"]), issue(id="2", labels=[{"name": "x"}])])
    a, b = s["issues"]
    assert a["markers"]["blocked"] is True
    assert b["markers"]["blocked"] is False
    assert a["markers"]["waiting"] is None  # not label-based: unrecognisable
    assert a["markers"]["untriaged"] is None  # not declared: board cannot show it


def test_label_objects_are_read(cfg):
    s = compose(cfg, [issue(labels=[{"name": "blocked", "color": "red"}])])
    assert s["issues"][0]["markers"]["blocked"] is True


def test_null_field_stays_null(cfg):
    s = compose(cfg, [issue(description=None, created_at=None)])
    assert s["issues"][0]["description"] is None
    assert s["issues"][0]["created_at"] is None


def test_sprints_carried(cfg):
    sp = [{"id": "1", "name": "S1", "state": "closed",
           "start_date": "2026-01-01", "end_date": "2026-01-14"}]
    assert compose(cfg, [issue()], sprints=sp)["sprints"] == sp
    assert compose(cfg, [issue()])["sprints"] is None


def test_native_snapshot_enriched_and_validated(cfg):
    native = {"taken_at": "2026-02-01T00:00:00Z", "tool": "native-tool", "tool_version": "2.0",
              "issues": [issue(status="Done", labels=["blocked"], finished_at="2026-01-10T00:00:00Z")]}
    s = snapshot.enrich_native(native, cfg)
    assert s["source"] == "native"
    assert s["tool"] == "native-tool" and s["tool_version"] == "2.0"
    assert s["issues"][0]["kind"] == "finished"
    assert s["issues"][0]["markers"]["blocked"] is True
    assert s["issues"][0]["finished_at"] == "2026-01-10T00:00:00Z"


def test_native_without_taken_at_fails(cfg):
    with pytest.raises(snapshot.InputError):
        snapshot.enrich_native({"issues": [issue()]}, cfg)


@pytest.mark.parametrize("bad", [
    {k: v for k, v in issue().items() if k != "status"},          # missing required field
    {k: v for k, v in issue().items() if k != "created_at"},      # missing, not null
    issue(status="x") | {"status": "In Progress"},                 # status not an object
    issue(labels="blocked"),                                       # labels not a list
    issue(created_at="yesterday"),                                 # not a timestamp
    issue(id=None),                                                # id may not be null
])
def test_malformed_issue_fails(cfg, bad):
    with pytest.raises(snapshot.InputError):
        compose(cfg, [bad])


def test_issues_not_array_fails(cfg):
    with pytest.raises(snapshot.InputError):
        compose(cfg, {"issues": []})


def test_bad_kind_in_config_fails(tmp_path):
    p = tmp_path / "c.toml"
    p.write_text(CONFIG.replace('"finished"', '"closed"'), encoding="utf-8")
    with pytest.raises(snapshot.InputError):
        snapshot.load_config(p)


def test_config_without_states_fails(tmp_path):
    p = tmp_path / "c.toml"
    p.write_text("version = 1\n", encoding="utf-8")
    with pytest.raises(snapshot.InputError):
        snapshot.load_config(p)


def run(*args):
    return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)],
                          capture_output=True, text=True, encoding="utf-8")


def test_cli_composed_to_file(tmp_path):
    (tmp_path / "c.toml").write_text(CONFIG, encoding="utf-8")
    (tmp_path / "i.json").write_text(json.dumps([issue()]), encoding="utf-8")
    (tmp_path / "s.json").write_text(json.dumps(STATUSES), encoding="utf-8")
    out = tmp_path / "snap.json"
    r = run("--issues", tmp_path / "i.json", "--statuses", tmp_path / "s.json",
            "--config", tmp_path / "c.toml", "--out", out)
    assert r.returncode == 0, r.stderr
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data["source"] == "composed" and data["issues"][0]["kind"] == "active"


def test_cli_native_stdout(tmp_path):
    (tmp_path / "c.toml").write_text(CONFIG, encoding="utf-8")
    (tmp_path / "n.json").write_text(json.dumps(
        {"taken_at": "2026-02-01T00:00:00Z", "issues": [issue()]}), encoding="utf-8")
    r = run("--native", tmp_path / "n.json", "--config", tmp_path / "c.toml")
    assert r.returncode == 0, r.stderr
    assert json.loads(r.stdout)["source"] == "native"


def test_cli_malformed_json_fails_loudly(tmp_path):
    (tmp_path / "c.toml").write_text(CONFIG, encoding="utf-8")
    (tmp_path / "i.json").write_text("[{not json", encoding="utf-8")
    (tmp_path / "s.json").write_text(json.dumps(STATUSES), encoding="utf-8")
    r = run("--issues", tmp_path / "i.json", "--statuses", tmp_path / "s.json",
            "--config", tmp_path / "c.toml")
    assert r.returncode != 0
    assert "i.json" in r.stderr
    assert r.stdout == ""


def test_cli_composed_needs_statuses(tmp_path):
    (tmp_path / "c.toml").write_text(CONFIG, encoding="utf-8")
    (tmp_path / "i.json").write_text(json.dumps([issue()]), encoding="utf-8")
    r = run("--issues", tmp_path / "i.json", "--config", tmp_path / "c.toml")
    assert r.returncode != 0


def test_status_marker_recognised(tmp_path):
    p = tmp_path / "c.toml"
    p.write_text(CONFIG.replace('[markers]', '[markers]\nabandoned = "status:Canceled"')
                 .replace('"Done" = "finished"', '"Done" = "finished"\n"Canceled" = "finished"'),
                 encoding="utf-8")
    s = compose(snapshot.load_config(p), [issue(status="Canceled"), issue(id="2", status="Done")])
    assert s["issues"][0]["markers"]["abandoned"] is True
    assert s["issues"][1]["markers"]["abandoned"] is False


def test_cli_out_prints_summary_to_stderr(tmp_path):
    (tmp_path / "c.toml").write_text(CONFIG.replace('"Done" = "finished"', '"Done" = "finished"\n"Gone" = "queued"'),
                                     encoding="utf-8")
    (tmp_path / "i.json").write_text(json.dumps([issue(), issue(id="2", status="Triage"),
                                                 issue(id="3", status=None)]), encoding="utf-8")
    (tmp_path / "s.json").write_text(json.dumps(STATUSES), encoding="utf-8")
    out = tmp_path / "snap.json"
    r = run("--issues", tmp_path / "i.json", "--statuses", tmp_path / "s.json",
            "--config", tmp_path / "c.toml", "--out", out)
    assert r.returncode == 0, r.stderr
    lines = r.stderr.strip().splitlines()
    assert len(lines) == 1
    summary = json.loads(lines[0])
    assert summary["out"] == str(out)
    assert summary["issues"] == 3
    assert summary["by_kind"] == {"active": 1}
    assert summary["unmapped"] == 2
    assert summary["unmapped_statuses"] == ["QA", "Triage"]
    assert summary["issues_without_status"] == ["3"]
    assert summary["mapping_unknown_statuses"] == ["Gone"]
    assert r.stdout == ""


def test_cli_stdout_prints_no_summary(tmp_path):
    (tmp_path / "c.toml").write_text(CONFIG, encoding="utf-8")
    (tmp_path / "n.json").write_text(json.dumps(
        {"taken_at": "2026-02-01T00:00:00Z", "issues": [issue()]}), encoding="utf-8")
    r = run("--native", tmp_path / "n.json", "--config", tmp_path / "c.toml")
    assert r.returncode == 0 and r.stderr == ""


def test_history_fields_validated_and_kept(cfg):
    s = compose(cfg, [issue(started_at="2026-01-02T00:00:00Z",
                            transitions=[{"status": "In Progress", "at": "2026-01-02T00:00:00Z"}])])
    assert s["issues"][0]["started_at"] == "2026-01-02T00:00:00Z"
    assert s["issues"][0]["transitions"][0]["status"] == "In Progress"


@pytest.mark.parametrize("bad", [
    issue(started_at="soon"),
    issue(transitions="In Progress"),
    issue(transitions=[{"status": "In Progress"}]),
    issue(transitions=[{"status": 3, "at": "2026-01-02T00:00:00Z"}]),
])
def test_malformed_history_fails(cfg, bad):
    with pytest.raises(snapshot.InputError):
        compose(cfg, [bad])


# --- silent-failure fixes ---------------------------------------------------------------------

def test_scope_record_is_stored(cfg):
    s = snapshot.compose([issue(), issue(id="2")], STATUSES, None, cfg, "2026-02-01T00:00:00Z",
                         scope={"query": "project = X", "complete": True, "reported_total": 2})
    assert s["scope"] == {"query": "project = X", "fetched": 2, "reported_total": 2, "complete": True,
                          "includes_finished": None, "empty_ok": False}


def test_scope_complete_derived_from_reported_total(cfg):
    s = snapshot.compose([issue()], STATUSES, None, cfg, "2026-02-01T00:00:00Z",
                         scope={"reported_total": 250})
    assert s["scope"]["complete"] is False and s["scope"]["fetched"] == 1


def test_scope_without_flags_is_unknown(cfg):
    assert compose(cfg, [issue()])["scope"]["complete"] is None


def test_scope_claimed_complete_but_short_fails(cfg):
    with pytest.raises(snapshot.InputError):
        snapshot.compose([issue()], STATUSES, None, cfg, "2026-02-01T00:00:00Z",
                         scope={"complete": True, "reported_total": 5})


def test_empty_issue_list_needs_empty_ok(cfg):
    with pytest.raises(snapshot.InputError, match="empty"):
        compose(cfg, [])
    s = snapshot.compose([], STATUSES, None, cfg, "2026-02-01T00:00:00Z", empty_ok=True)
    assert s["issues"] == [] and s["scope"]["empty_ok"] is True


def test_duplicate_ids_fail(cfg):
    with pytest.raises(snapshot.InputError, match="1"):
        compose(cfg, [issue(id="1"), issue(id=1)])


@pytest.mark.parametrize("sprint", [["S1", "S2"], {"state": "active"}, True, {"id": ["1"]}])
def test_bad_sprint_field_fails(cfg, sprint):
    with pytest.raises(snapshot.InputError, match="sprint"):
        compose(cfg, [issue(sprint=sprint)])


@pytest.mark.parametrize("sprint", [None, "S1", 7, {"id": "1", "name": "S1"}, {"name": "S1"}])
def test_good_sprint_field_passes(cfg, sprint):
    compose(cfg, [issue(sprint=sprint)])


@pytest.mark.parametrize("labels", [[3], [{"color": "red"}], [None]])
def test_malformed_label_fails(cfg, labels):
    with pytest.raises(snapshot.InputError, match="label"):
        compose(cfg, [issue(labels=labels)])


def test_assignees_must_be_list_or_null(cfg):
    with pytest.raises(snapshot.InputError, match="assignees"):
        compose(cfg, [issue(assignees="ann")])


@pytest.mark.parametrize("spec", ["Label:Abandoned", "STATUS:Canceled", "abandoned", "label:"])
def test_marker_spec_typo_fails(tmp_path, spec):
    p = tmp_path / "c.toml"
    p.write_text(CONFIG.replace('[markers]', f'[markers]\nabandoned = "{spec}"'), encoding="utf-8")
    with pytest.raises(snapshot.InputError, match="markers"):
        snapshot.load_config(p)


def test_marker_shown_another_way_is_listed(cfg):
    assert compose(cfg, [issue()])["markers_unreadable"] == {"waiting": "field:flagged"}


def test_mapping_unknown_is_null_when_statuses_not_read(cfg):
    s = snapshot.enrich_native({"taken_at": "2026-02-01T00:00:00Z", "issues": [issue()]}, cfg)
    assert s["mapping_unknown_statuses"] is None
    assert "not read" in s["mapping_unknown_statuses_reason"]
    assert compose(cfg, [issue()])["mapping_unknown_statuses_reason"] is None


def test_taken_at_basis_recorded(cfg):
    assert compose(cfg, [issue()])["taken_at_basis"] == "given"
    s = snapshot.compose([issue()], STATUSES, None, cfg, "2026-02-01T00:00:00Z",
                         taken_at_basis="script_run_time")
    assert s["taken_at_basis"] == "script_run_time"
    n = snapshot.enrich_native({"taken_at": "2026-02-01T00:00:00Z", "issues": [issue()]}, cfg)
    assert n["taken_at_basis"] == "tool"


def test_atomic_is_the_tools_claim(cfg):
    assert compose(cfg, [issue()])["atomic"] is False
    n = {"taken_at": "2026-02-01T00:00:00Z", "issues": [issue()]}
    assert snapshot.enrich_native(n, cfg)["atomic"] is None
    assert snapshot.enrich_native({**n, "atomic": True}, cfg)["atomic"] is True


def test_naive_timestamps_counted(cfg):
    s = compose(cfg, [issue(created_at="2026-01-01T00:00:00", finished_at="2026-01-02T00:00:00")])
    assert s["naive_timestamps"] == 2


def test_native_scope_merged_and_conflict_fails(cfg):
    n = {"taken_at": "2026-02-01T00:00:00Z", "issues": [issue()], "scope": {"query": "all", "complete": True}}
    assert snapshot.enrich_native(n, cfg)["scope"]["complete"] is True
    with pytest.raises(snapshot.InputError):
        snapshot.enrich_native(n, cfg, scope={"query": "open only"})


def write_cli_inputs(tmp_path, issues):
    (tmp_path / "c.toml").write_text(CONFIG, encoding="utf-8")
    (tmp_path / "i.json").write_text(json.dumps(issues), encoding="utf-8")
    (tmp_path / "s.json").write_text(json.dumps(STATUSES), encoding="utf-8")
    return ["--issues", tmp_path / "i.json", "--statuses", tmp_path / "s.json", "--config", tmp_path / "c.toml"]


def test_cli_scope_flags(tmp_path):
    r = run(*write_cli_inputs(tmp_path, [issue()]), "--scope", "project = X", "--complete", "false",
            "--reported-total", "40", "--includes-finished", "true", "--taken-at", "2026-02-01T00:00:00Z")
    assert r.returncode == 0, r.stderr
    sc = json.loads(r.stdout)["scope"]
    assert sc == {"query": "project = X", "fetched": 1, "reported_total": 40, "complete": False,
                  "includes_finished": True, "empty_ok": False}


def test_cli_default_taken_at_is_labelled(tmp_path):
    r = run(*write_cli_inputs(tmp_path, [issue()]))
    assert json.loads(r.stdout)["taken_at_basis"] == "script_run_time"


def test_cli_empty_list_refused_unless_empty_ok(tmp_path):
    args = write_cli_inputs(tmp_path, [])
    r = run(*args)
    assert r.returncode == 2 and "--empty-ok" in r.stderr and r.stdout == ""
    assert run(*args, "--empty-ok").returncode == 0


def test_cli_bad_complete_value_fails(tmp_path):
    assert run(*write_cli_inputs(tmp_path, [issue()]), "--complete", "yes").returncode == 2


# --- per-task history files -------------------------------------------------------------------

def test_history_dir_merged(cfg, tmp_path):
    (tmp_path / "1.json").write_text(json.dumps(
        {"started_at": "2026-01-02T00:00:00Z",
         "transitions": [{"status": "In Progress", "at": "2026-01-02T00:00:00Z"}]}), encoding="utf-8")
    issues = [issue(), issue(id="2")]
    s = snapshot.compose(issues, STATUSES, None, cfg, "2026-02-01T00:00:00Z",
                         history=snapshot.load_history(tmp_path, issues))
    one, two = s["issues"]
    assert one["started_at"] == "2026-01-02T00:00:00Z" and one["transitions"][0]["status"] == "In Progress"
    assert "started_at" not in two
    assert s["history"] == {"merged": 1, "missing": {"count": 1, "ids": ["2"]}}


def test_history_file_validated(cfg, tmp_path):
    (tmp_path / "1.json").write_text(json.dumps({"finished_at": "soon"}), encoding="utf-8")
    with pytest.raises(snapshot.InputError, match="finished_at"):
        snapshot.compose([issue()], STATUSES, None, cfg, "2026-02-01T00:00:00Z",
                         history=snapshot.load_history(tmp_path, [issue()]))


def test_history_file_unknown_key_fails(tmp_path):
    (tmp_path / "1.json").write_text(json.dumps({"finished": "2026-01-02T00:00:00Z"}), encoding="utf-8")
    with pytest.raises(snapshot.InputError, match="finished"):
        snapshot.load_history(tmp_path, [issue()])


def test_history_conflicting_with_issue_fails(cfg, tmp_path):
    (tmp_path / "1.json").write_text(json.dumps({"finished_at": "2026-01-03T00:00:00Z"}), encoding="utf-8")
    i = issue(finished_at="2026-01-02T00:00:00Z")
    with pytest.raises(snapshot.InputError, match="finished_at"):
        snapshot.compose([i], STATUSES, None, cfg, "2026-02-01T00:00:00Z",
                         history=snapshot.load_history(tmp_path, [i]))


def test_cli_history_dir(tmp_path):
    hist = tmp_path / "hist"
    hist.mkdir()
    (hist / "PROJ-1.json").write_text(json.dumps({"finished_at": "2026-01-03T00:00:00Z"}), encoding="utf-8")
    r = run(*write_cli_inputs(tmp_path, [issue(id="PROJ-1", status="Done")]), "--history", hist)
    assert r.returncode == 0, r.stderr
    assert json.loads(r.stdout)["issues"][0]["finished_at"] == "2026-01-03T00:00:00Z"
