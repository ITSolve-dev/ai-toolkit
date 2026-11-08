import json
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
import snapshot  # noqa: E402

SCRIPT = Path(__file__).parent / "snapshot.py"

SETTINGS = """
[board]
kind = "sometool"
[board.labels]
blocked = "work cannot proceed"
"needs-info" = "waiting on someone outside the team"
"needs-triage" = "not yet looked at"
[process]
setup = "flow"
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
            {"id": "s4", "name": "QA", "category": None},
            {"id": "s5", "name": "Canceled", "category": "canceled"}]


def settings(tmp_path, text=SETTINGS):
    p = tmp_path / "workflow.toml"
    p.write_text(text, encoding="utf-8")
    return snapshot.load_settings(p)


@pytest.fixture
def cfg(tmp_path):
    return settings(tmp_path)


def compose(cfg, issues, statuses=STATUSES, sprints=None):
    return snapshot.compose(issues, statuses, sprints, cfg, "2026-02-01T00:00:00Z")


def test_composed_header(cfg):
    s = compose(cfg, [issue()])
    assert s["schema"] == 1
    assert s["source"] == "composed"
    assert s["taken_at"] == "2026-02-01T00:00:00Z"
    assert s["tool"] is None and s["tool_version"] is None  # [board] is the tool's; not read for this
    assert s["mapping"]["Done"] == "finished"
    t = snapshot.compose([issue()], STATUSES, None, cfg, "2026-02-01T00:00:00Z", tool="sometool",
                         tool_version="0.1.0")
    assert t["tool"] == "sometool" and t["tool_version"] == "0.1.0"


def test_native_tool_claim_conflicting_with_flag_fails(cfg):
    n = {"taken_at": "2026-02-01T00:00:00Z", "tool": "a", "issues": [issue()]}
    assert snapshot.enrich_native(n, cfg, tool="a")["tool"] == "a"
    assert snapshot.enrich_native({**n, "tool": None}, cfg, tool_version="9")["tool_version"] == "9"
    with pytest.raises(snapshot.InputError, match="tool"):
        snapshot.enrich_native(n, cfg, tool="b")


def test_kind_from_category_of_the_statuses_read(cfg):
    s = compose(cfg, [issue(status="Backlog")])
    assert s["issues"][0]["kind"] == "before_start"
    assert s["mapping_sources"]["Backlog"] == "category"


def test_kind_from_the_issues_own_category(cfg):
    s = compose(cfg, [dict(issue(), status={"name": "Triage", "category": "in_progress"}),
                      dict(issue(id="2"), status={"name": "Done", "category": "canceled"})])
    assert s["issues"][0]["kind"] == "active"
    assert s["mapping"]["Triage"] == "active" and "Triage" not in s["unmapped_statuses"]
    assert s["issues"][1]["kind"] == "finished"


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
    c = settings(tmp_path, SETTINGS + 'review_statuses = ["Ghost"]\n[process.kinds]\n"Gone" = "queued"\n')
    s = compose(c, [issue()])
    assert s["mapping_unknown_statuses"] == ["Ghost", "Gone"]


ORDER = SETTINGS + '''review_statuses = ["In Review", "Ready"]
[process.kinds]
"Ready" = "queued"
"QA" = "handed_off"
'''


def test_kind_derivation_order(tmp_path):
    statuses = STATUSES + [{"name": "In Review", "category": "in_progress"},
                           {"name": "Ready", "category": "todo"}]
    issues = [issue(id="r", status="Ready"), issue(id="v", status="In Review"),
              issue(id="q", status="QA"), issue(id="b", status="Backlog"), issue(id="t", status="Triage")]
    s = compose(settings(tmp_path, ORDER), issues, statuses=statuses)
    kinds = {o["id"]: o["kind"] for o in s["issues"]}
    # [process.kinds] beats review_statuses and the category
    assert kinds["r"] == "queued" and s["mapping_sources"]["Ready"] == "process.kinds"
    # review_statuses beats the category
    assert kinds["v"] == "handed_off" and s["mapping_sources"]["In Review"] == "review_statuses"
    # [process.kinds] gives a kind where the tool gives no category
    assert kinds["q"] == "handed_off" and "QA" not in s["unmapped_statuses"]
    assert kinds["b"] == "before_start" and s["mapping_sources"]["Backlog"] == "category"
    # no category and no entry: unmapped, never guessed
    assert kinds["t"] is None and s["unmapped_statuses"] == ["Triage"]


def test_settings_without_process_decide_by_category(tmp_path):
    c = settings(tmp_path, '[board]\nkind = "sometool"\n')
    s = compose(c, [issue(), issue(id="2", status="QA")])
    assert s["issues"][0]["kind"] == "active" and s["issues"][1]["kind"] is None
    assert s["mapping_unknown_statuses"] == []


@pytest.mark.parametrize("category", ["Done", "closed", 3])
def test_unknown_category_fails(cfg, category):
    with pytest.raises(snapshot.InputError, match="category"):
        compose(cfg, [dict(issue(), status={"name": "X", "category": category})])
    with pytest.raises(snapshot.InputError, match="category"):
        compose(cfg, [issue()], statuses=[{"name": "X", "category": category}])


def test_marker_defaults_are_labels(cfg):
    s = compose(cfg, [issue(labels=["blocked", "needs-info"]), issue(id="2", labels=[{"name": "needs-triage"}])])
    a, b = s["issues"]
    assert a["markers"]["blocked"] is True and b["markers"]["blocked"] is False
    assert a["markers"]["waiting"] is True and b["markers"]["waiting"] is False
    assert a["markers"]["untriaged"] is False and b["markers"]["untriaged"] is True
    assert s["marker_specs"] == {"blocked": {"spec": "label:blocked", "source": "default"},
                                 "waiting": {"spec": "label:needs-info", "source": "default"},
                                 "untriaged": {"spec": "label:needs-triage", "source": "default"},
                                 "abandoned": {"spec": "category:canceled", "source": "category"}}


def test_marker_overrides_and_status_form(tmp_path):
    c = settings(tmp_path, SETTINGS + '[process.markers]\nblocked = "impeded"\nwaiting = "status:Waiting"\n')
    s = compose(c, [issue(labels=["impeded", "blocked"]), issue(id="2", status="Waiting")])
    a, b = s["issues"]
    assert a["markers"]["blocked"] is True and b["markers"]["blocked"] is False
    assert a["markers"]["waiting"] is False and b["markers"]["waiting"] is True
    assert a["markers"]["untriaged"] is False  # the default still applies
    assert s["marker_specs"]["waiting"] == {"spec": "status:Waiting", "source": "settings"}
    assert s["marker_specs"]["blocked"] == {"spec": "label:impeded", "source": "settings"}


def test_canceled_is_finished_and_abandoned(cfg):
    s = compose(cfg, [issue(status="Canceled"), issue(id="2", status="Done"), issue(id="3", status="QA")])
    c, d, q = s["issues"]
    assert c["kind"] == "finished" and c["markers"]["abandoned"] is True
    assert d["kind"] == "finished" and d["markers"]["abandoned"] is False
    assert q["markers"]["abandoned"] is None  # no category: cannot be told


def test_declared_abandoned_column_reads_without_category(tmp_path):
    c = settings(tmp_path, SETTINGS + '[process.kinds]\n"Dropped" = "finished"\n'
                                      '[process.markers]\nabandoned = "status:Dropped"\n')
    s = compose(c, [issue(status="Dropped"), issue(id="2", status="QA"), issue(id="3", status="Canceled")])
    assert [o["markers"]["abandoned"] for o in s["issues"]] == [True, False, True]


def test_markers_undeclared_lists_label_markers_missing_from_board_labels(tmp_path):
    text = SETTINGS.replace('"needs-info" = "waiting on someone outside the team"\n', "")
    s = compose(settings(tmp_path, text + '[process.markers]\nuntriaged = "status:Triage"\n'), [issue()])
    assert s["markers_undeclared"] == [{"marker": "waiting", "label": "needs-info"}]
    assert s["markers_undeclared_reason"] is None


def test_markers_undeclared_without_board_labels_lists_all(tmp_path):
    s = compose(settings(tmp_path, '[board]\nkind = "t"\n[process]\nsetup = "flow"\n'), [issue()])
    assert [m["marker"] for m in s["markers_undeclared"]] == ["blocked", "waiting", "untriaged"]
    assert "[board.labels]" in s["markers_undeclared_reason"]


def test_all_markers_declared(cfg):
    s = compose(cfg, [issue()])
    assert s["markers_undeclared"] == [] and s["markers_undeclared_reason"] is None


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
              "issues": [dict(issue(labels=["blocked"], finished_at="2026-01-10T00:00:00Z"),
                              status={"name": "Done", "category": "done"})]}
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


def test_bad_kind_in_process_kinds_fails(tmp_path):
    with pytest.raises(snapshot.InputError, match="process.kinds"):
        settings(tmp_path, SETTINGS + '[process.kinds]\n"Ready" = "closed"\n')


@pytest.mark.parametrize("extra", ['review_statuses = "Review"\n', 'review_statuses = [1]\n'])
def test_bad_review_statuses_fail(tmp_path, extra):
    with pytest.raises(snapshot.InputError, match="review_statuses"):
        settings(tmp_path, SETTINGS + extra)


def test_malformed_settings_toml_fails(tmp_path):
    with pytest.raises(snapshot.InputError, match="TOML"):
        settings(tmp_path, "[process\n")


def run(*args):
    return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)],
                          capture_output=True, text=True, encoding="utf-8")


def test_cli_composed_to_file(tmp_path):
    (tmp_path / "c.toml").write_text(SETTINGS, encoding="utf-8")
    (tmp_path / "i.json").write_text(json.dumps([issue()]), encoding="utf-8")
    (tmp_path / "s.json").write_text(json.dumps(STATUSES), encoding="utf-8")
    out = tmp_path / "snap.json"
    r = run("--issues", tmp_path / "i.json", "--statuses", tmp_path / "s.json",
            "--settings", tmp_path / "c.toml", "--out", out)
    assert r.returncode == 0, r.stderr
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data["source"] == "composed" and data["issues"][0]["kind"] == "active"


def test_cli_native_stdout(tmp_path):
    (tmp_path / "c.toml").write_text(SETTINGS, encoding="utf-8")
    (tmp_path / "n.json").write_text(json.dumps(
        {"taken_at": "2026-02-01T00:00:00Z", "issues": [issue()]}), encoding="utf-8")
    r = run("--native", tmp_path / "n.json", "--settings", tmp_path / "c.toml")
    assert r.returncode == 0, r.stderr
    assert json.loads(r.stdout)["source"] == "native"


def test_cli_malformed_json_fails_loudly(tmp_path):
    (tmp_path / "c.toml").write_text(SETTINGS, encoding="utf-8")
    (tmp_path / "i.json").write_text("[{not json", encoding="utf-8")
    (tmp_path / "s.json").write_text(json.dumps(STATUSES), encoding="utf-8")
    r = run("--issues", tmp_path / "i.json", "--statuses", tmp_path / "s.json",
            "--settings", tmp_path / "c.toml")
    assert r.returncode != 0
    assert "i.json" in r.stderr
    assert r.stdout == ""


def test_cli_composed_needs_statuses(tmp_path):
    (tmp_path / "c.toml").write_text(SETTINGS, encoding="utf-8")
    (tmp_path / "i.json").write_text(json.dumps([issue()]), encoding="utf-8")
    r = run("--issues", tmp_path / "i.json", "--settings", tmp_path / "c.toml")
    assert r.returncode != 0


def test_cli_out_prints_summary_to_stderr(tmp_path):
    (tmp_path / "c.toml").write_text(SETTINGS.replace('"needs-triage" = "not yet looked at"\n', "")
                                     + '[process.kinds]\n"Gone" = "queued"\n', encoding="utf-8")
    (tmp_path / "i.json").write_text(json.dumps([issue(), issue(id="2", status="Triage"),
                                                 issue(id="3", status=None)]), encoding="utf-8")
    (tmp_path / "s.json").write_text(json.dumps(STATUSES), encoding="utf-8")
    out = tmp_path / "snap.json"
    r = run("--issues", tmp_path / "i.json", "--statuses", tmp_path / "s.json",
            "--settings", tmp_path / "c.toml", "--out", out)
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
    assert summary["markers_undeclared"] == ["untriaged"]
    assert r.stdout == ""


def test_cli_stdout_prints_no_summary(tmp_path):
    (tmp_path / "c.toml").write_text(SETTINGS, encoding="utf-8")
    (tmp_path / "n.json").write_text(json.dumps(
        {"taken_at": "2026-02-01T00:00:00Z", "issues": [issue()]}), encoding="utf-8")
    r = run("--native", tmp_path / "n.json", "--settings", tmp_path / "c.toml")
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


@pytest.mark.parametrize("spec", ["label:blocked", "Label:blocked", "Status:Waiting", "STATUS:Waiting",
                                  "status:", " "])
def test_marker_spec_typo_fails(tmp_path, spec):
    with pytest.raises(snapshot.InputError, match="markers"):
        settings(tmp_path, SETTINGS + f'[process.markers]\nwaiting = "{spec}"\n')


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
    (tmp_path / "c.toml").write_text(SETTINGS, encoding="utf-8")
    (tmp_path / "i.json").write_text(json.dumps(issues), encoding="utf-8")
    (tmp_path / "s.json").write_text(json.dumps(STATUSES), encoding="utf-8")
    return ["--issues", tmp_path / "i.json", "--statuses", tmp_path / "s.json", "--settings", tmp_path / "c.toml"]


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


# --- a history read with since and moves ------------------------------------------------------

def moves_file(**over):
    data = {"id": "1", "status": {"name": "In Progress", "category": "in_progress"},
            "since": "2026-01-05T00:00:00Z",
            "moves": [{"from": None, "to": {"name": "Todo", "category": "todo"},
                       "at": "2026-01-01T00:00:00Z", "by": "ann"},
                      {"from": {"name": "Todo", "category": "todo"},
                       "to": {"name": "In Progress", "category": "in_progress"},
                       "at": "2026-01-05T00:00:00Z", "by": "bob"}]}
    data.update(over)
    return data


def test_moves_shape_becomes_status_since_and_transitions(cfg, tmp_path):
    (tmp_path / "1.json").write_text(json.dumps(moves_file()), encoding="utf-8")
    s = snapshot.compose([issue()], STATUSES, None, cfg, "2026-02-01T00:00:00Z",
                         history=snapshot.load_history(tmp_path, [issue()]))
    one = s["issues"][0]
    assert one["status_since"] == "2026-01-05T00:00:00Z"
    assert one["transitions"] == [{"status": "Todo", "at": "2026-01-01T00:00:00Z"},
                                  {"status": "In Progress", "at": "2026-01-05T00:00:00Z"}]
    assert "started_at" not in one and "finished_at" not in one
    assert s["history"]["merged"] == 1


def test_moves_shape_null_since_leaves_status_since_unset(cfg, tmp_path):
    (tmp_path / "1.json").write_text(json.dumps(moves_file(since=None)), encoding="utf-8")
    h = snapshot.load_history(tmp_path, [issue()])
    assert h["1"].get("status_since") is None
    assert len(h["1"]["transitions"]) == 2


def test_moves_without_a_creation_move_start_in_the_first_from(cfg, tmp_path):
    # Created 01-01 in Todo, one move Todo -> In Progress 01-03, no creation move.
    data = moves_file(since="2026-01-03T00:00:00Z",
                      moves=[{"from": {"name": "Todo"}, "to": {"name": "In Progress"},
                              "at": "2026-01-03T00:00:00Z"}])
    (tmp_path / "1.json").write_text(json.dumps(data), encoding="utf-8")
    s = snapshot.compose([issue()], STATUSES, None, cfg, "2026-02-01T00:00:00Z",
                         history=snapshot.load_history(tmp_path, [issue()]))
    one = s["issues"][0]
    assert one["transitions"] == [{"status": "Todo", "at": "2026-01-01T00:00:00Z"},
                                  {"status": "In Progress", "at": "2026-01-03T00:00:00Z"}]
    import board_metrics
    assert board_metrics.history_gap(one) is None


@pytest.mark.parametrize("since, expected", [
    (None, [{"status": "In Progress", "at": "2026-01-01T00:00:00Z"}]),
    ("2026-01-01T00:00:00Z", [{"status": "In Progress", "at": "2026-01-01T00:00:00Z"}]),
    ("2026-01-04T00:00:00Z", []),
])
def test_no_moves_start_in_the_current_status_unless_since_says_otherwise(tmp_path, since, expected):
    (tmp_path / "1.json").write_text(json.dumps(moves_file(since=since, moves=[])), encoding="utf-8")
    assert snapshot.load_history(tmp_path, [issue()])["1"]["transitions"] == expected


def test_moves_shape_status_other_than_the_issue_read_fails(tmp_path):
    (tmp_path / "1.json").write_text(json.dumps(moves_file(status={"name": "Done", "category": "done"})),
                                     encoding="utf-8")
    with pytest.raises(snapshot.InputError, match="moved between the reads"):
        snapshot.load_history(tmp_path, [issue()])


@pytest.mark.parametrize("moves", [
    "nope",
    [{"to": "In Progress", "at": "2026-01-05T00:00:00Z"}],
    [{"to": {"name": "In Progress"}}],
    [{"to": {"name": "In Progress"}, "at": "later"}],
])
def test_malformed_moves_fail(tmp_path, moves):
    (tmp_path / "1.json").write_text(json.dumps(moves_file(moves=moves)), encoding="utf-8")
    with pytest.raises(snapshot.InputError, match="moves"):
        snapshot.load_history(tmp_path, [issue()])


def test_mixing_the_two_shapes_fails(tmp_path):
    (tmp_path / "1.json").write_text(json.dumps(moves_file(started_at="2026-01-05T00:00:00Z")),
                                     encoding="utf-8")
    with pytest.raises(snapshot.InputError, match="one shape"):
        snapshot.load_history(tmp_path, [issue()])


def test_cli_history_dir_moves_shape(tmp_path):
    hist = tmp_path / "hist"
    hist.mkdir()
    data = moves_file(id="PROJ-1", status={"name": "Done", "category": "done"}, since="2026-01-09T00:00:00Z")
    (hist / "PROJ-1.json").write_text(json.dumps(data), encoding="utf-8")
    r = run(*write_cli_inputs(tmp_path, [issue(id="PROJ-1", status="Done")]), "--history", hist)
    assert r.returncode == 0, r.stderr
    got = json.loads(r.stdout)["issues"][0]
    assert got["status_since"] == "2026-01-09T00:00:00Z" and len(got["transitions"]) == 2


# --- settings validation and consistency --------------------------------------------------------

@pytest.mark.parametrize("extra, match", [
    ('review_status = "Review"\n', "unknown key review_status in \\[process\\]"),
    ('time_zone = "+03:00"\n', "unknown key time_zone"),
    ('[process.limits]\n"In Progress" = 1\n', "unknown key limits"),
    ('[process.markers]\nblokced = "impeded"\n', "unknown key blokced in \\[process.markers\\]"),
    ('commitment = "promise"\n', "commitment"),
    ('executor = "robots"\n', "executor"),
    ('ceiling = "XL"\n[board.size]\nS = 1\nL = 3\n', "ceiling"),
    ('[process.markers]\nwaiting = "L"\n[board.size]\nS = 1\nL = 3\n', "marker label"),
    ('[process.markers]\nblocked = "status: Blocked"\n', "markers"),
    ('[process.markers]\nblocked = " impeded"\n', "markers"),
])
def test_settings_mistakes_fail(tmp_path, extra, match):
    with pytest.raises(snapshot.InputError, match=match):
        settings(tmp_path, SETTINGS + extra)


def test_ceiling_in_board_size_passes(tmp_path):
    settings(tmp_path, SETTINGS + 'ceiling = "L"\n[board.size]\nS = 1\nL = 3\n')


@pytest.mark.parametrize("text", ['[process]\nsle = "5 days at 85%"\n', '[process]\nsetup = "kanban"\n'])
def test_process_present_needs_a_valid_setup(tmp_path, text):
    with pytest.raises(snapshot.InputError, match="setup"):
        settings(tmp_path, text)


def test_validated_also_when_given_as_a_table(cfg):
    with pytest.raises(snapshot.InputError, match="unknown key"):
        compose({"process": {"setup": "flow", "wip_limits": {}}}, [issue()])


DRAFT = """
[board]
kind = "sometool"
url = "https://example.invalid/board"
[board.statuses]
"In Progress" = "doing"
[board.labels]
blocked = "work cannot proceed"
"""


def test_draft_settings_with_only_board_tables(tmp_path):
    (tmp_path / ".task-master").mkdir()
    p = tmp_path / ".task-master" / "settings-draft.toml"
    p.write_text(DRAFT, encoding="utf-8")
    c = snapshot.load_settings(p)
    s = compose(c, [issue(), issue(id="2", status="QA")])
    assert s["issues"][0]["kind"] == "active" and s["issues"][1]["kind"] is None
    assert s["unmapped_statuses"] == ["QA"]
    assert [m["marker"] for m in s["markers_undeclared"]] == ["waiting", "untriaged"]


def test_cli_draft_settings_and_tool_flags(tmp_path):
    (tmp_path / "d.toml").write_text(DRAFT, encoding="utf-8")
    (tmp_path / "i.json").write_text(json.dumps([issue()]), encoding="utf-8")
    (tmp_path / "s.json").write_text(json.dumps(STATUSES), encoding="utf-8")
    r = run("--issues", tmp_path / "i.json", "--statuses", tmp_path / "s.json", "--settings", tmp_path / "d.toml",
            "--tool", "sometool", "--tool-version", "1.2")
    assert r.returncode == 0, r.stderr
    out = json.loads(r.stdout)
    assert out["tool"] == "sometool" and out["tool_version"] == "1.2"
    assert out["issues"][0]["kind"] == "active"


def test_status_marker_naming_a_status_the_board_lacks_is_listed(tmp_path):
    c = settings(tmp_path, SETTINGS + '[process.markers]\nblocked = "status:Blocked"\nwaiting = "status:QA"\n')
    s = compose(c, [issue()])
    assert s["markers_unknown_statuses"] == ["Blocked"]
    n = snapshot.enrich_native({"taken_at": "2026-02-01T00:00:00Z", "issues": [issue()]}, c)
    assert n["markers_unknown_statuses"] is None


def test_category_conflict_statuses_read_win_and_kinds_agree(cfg):
    s = compose(cfg, [dict(issue(), status={"name": "X", "category": "in_progress"})],
                statuses=[{"name": "X", "category": "todo"}])
    assert s["issues"][0]["kind"] == "before_start" and s["mapping"]["X"] == "before_start"
    assert s["category_conflicts"] == [{"status": "X", "categories": ["todo", "in_progress"]}]


def test_category_conflict_between_issues_first_wins(cfg):
    s = compose(cfg, [dict(issue(), status={"name": "Y", "category": "in_progress"}),
                      dict(issue(id="2"), status={"name": "Y", "category": "done"})],
                statuses=[{"name": "Y", "category": None}])
    assert [o["kind"] for o in s["issues"]] == ["active", "active"] and s["mapping"]["Y"] == "active"
    assert s["category_conflicts"] == [{"status": "Y", "categories": ["in_progress", "done"]}]
    assert compose(cfg, [issue()])["category_conflicts"] == []


@pytest.mark.parametrize("extra, status", [('review_statuses = ["Done"]\n', "Done"),
                                           ('[process.kinds]\n"Canceled" = "queued"\n', "Canceled")])
def test_unfinishing_a_finished_category_fails(tmp_path, extra, status):
    with pytest.raises(snapshot.InputError, match=status):
        compose(settings(tmp_path, SETTINGS + extra), [issue()])


def test_finished_kind_for_a_done_status_is_allowed(tmp_path):
    s = compose(settings(tmp_path, SETTINGS + '[process.kinds]\n"Done" = "finished"\n'), [issue()])
    assert s["mapping_sources"]["Done"] == "process.kinds"
