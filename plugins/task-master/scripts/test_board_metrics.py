import json
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
import board_metrics  # noqa: E402

SCRIPT = Path(__file__).parent / "board_metrics.py"
TAKEN = "2026-02-01T00:00:00Z"


def issue(id, kind, status, created="2026-01-22T00:00:00Z", description="## Acceptance criteria\n- x", **over):
    base = {"id": id, "title": "t", "description": description,
            "status": {"name": status, "category": None}, "labels": [],
            "created_at": created, "updated_at": "2026-01-31T00:00:00Z",
            "kind": kind, "markers": {}}
    base.update(over)
    return base


def snap(issues, source="composed", sprints=None):
    return {"schema": 1, "taken_at": TAKEN, "source": source, "tool": "t", "tool_version": "1",
            "mapping": {}, "unmapped_statuses": [], "issues": issues, "sprints": sprints}


def cfg(limits=None, headings=None):
    c = {}
    if limits is not None:
        c["limits"] = limits
    if headings is not None:
        c["checks"] = {"acceptance_headings": headings}
    return c


BOARD = [
    issue("1", "active", "In Progress"),
    issue("2", "active", "In Progress"),
    issue("3", "handed_off", "In Review"),
    issue("4", "queued", "Ready"),
    issue("5", "finished", "Done"),
    issue("6", None, "Triage"),
]


def test_counts_per_kind_and_status():
    m = board_metrics.compute(snap(BOARD), cfg())
    assert m["counts"]["by_kind"] == {"active": 2, "handed_off": 1, "queued": 1, "finished": 1}
    assert m["counts"]["unmapped"] == 1
    assert m["counts"]["by_status"]["In Progress"] == 2
    assert m["counts"]["by_status"]["Triage"] == 1
    assert m["counts"]["total"] == 6
    assert m["counts"]["basis"]


def test_wip_counts_started_unfinished_only():
    m = board_metrics.compute(snap(BOARD), cfg())
    assert m["wip"]["total"] == 3
    assert m["wip"]["by_kind"] == {"active": 2, "handed_off": 1}
    assert m["wip"]["by_status"] == {"In Progress": 2, "In Review": 1}
    assert "unmapped" in m["wip"]["basis"]


def test_limit_breach_by_status_and_kind():
    m = board_metrics.compute(snap(BOARD), cfg(limits={"In Progress": 1, "handed_off": 1, "active": 5}))
    br = m["limits"]["breaches"]
    assert {"key": "In Progress", "scope": "status", "limit": 1, "count": 2} in br
    assert all(b["key"] != "handed_off" for b in br)  # at the limit is not over it
    assert all(b["key"] != "active" for b in br)


def test_no_limits_declared():
    m = board_metrics.compute(snap(BOARD), cfg())
    assert m["limits"]["declared"] is False
    assert m["limits"]["breaches"] == []


def test_limit_key_matching_nothing_is_reported():
    m = board_metrics.compute(snap(BOARD), cfg(limits={"In Prgress": 2}))
    assert m["limits"]["unknown_keys"] == ["In Prgress"]


@pytest.mark.parametrize("bad", [{"In Progress": 0}, {"In Progress": "3"}, {"In Progress": True}])
def test_bad_limit_fails(bad):
    with pytest.raises(board_metrics.InputError):
        board_metrics.compute(snap(BOARD), cfg(limits=bad))


def test_age_since_created_when_no_history():
    m = board_metrics.compute(snap(BOARD), cfg())
    a = {x["id"]: x for x in m["age"]["items"]}
    assert a["1"]["days"] == 10.0
    assert a["1"]["basis"] == "since_created"
    assert "5" not in a  # finished is not open
    assert m["age"]["skipped_unmapped"] == ["6"]
    assert m["age"]["reference_time"] == TAKEN


def test_age_never_from_updated_at():
    m = board_metrics.compute(snap([issue("1", "active", "In Progress", created=None)]), cfg())
    item = m["age"]["items"][0]
    assert item["days"] is None and item["basis"] == "unknown"


def test_age_exact_from_native_history():
    i = issue("1", "active", "In Progress", status_since="2026-01-29T00:00:00Z")
    m = board_metrics.compute(snap([i], source="native"), cfg())
    item = m["age"]["items"][0]
    assert item["days"] == 3.0 and item["basis"] == "exact"


def test_missing_acceptance_criteria():
    issues = [issue("1", "queued", "Ready", description="no heading here\nAcceptance criteria are vague"),
              issue("2", "queued", "Ready", description=None),
              issue("3", "queued", "Ready", description="Intro\n\n### acceptance criteria:\n- a"),
              issue("4", "queued", "Ready", description="Acceptance Criteria\n---\n- a"),
              issue("5", "queued", "Ready", description="h2. Acceptance criteria\n* a"),
              issue("6", "finished", "Done", description="none")]
    m = board_metrics.compute(snap(issues), cfg())
    got = {x["id"]: x["reason"] for x in m["missing_acceptance_criteria"]["items"]}
    assert got == {"1": "no_heading", "2": "no_description"}


def test_acceptance_heading_configurable():
    issues = [issue("1", "queued", "Ready", description="## Definition of done\n- a")]
    assert board_metrics.compute(snap(issues), cfg())["missing_acceptance_criteria"]["items"]
    m = board_metrics.compute(snap(issues), cfg(headings=["Definition of done"]))
    assert m["missing_acceptance_criteria"]["items"] == []
    assert m["missing_acceptance_criteria"]["headings"] == ["Definition of done"]


SPRINTS = [{"id": "1", "name": "S1", "state": "closed", "start_date": "2026-01-01", "end_date": "2026-01-14"},
           {"id": "2", "name": "S2", "state": "active", "start_date": "2026-01-15", "end_date": None}]


def test_throughput_refuses_without_finish_times():
    m = board_metrics.compute(snap(BOARD, sprints=SPRINTS), cfg())
    assert m["throughput"]["periods"] is None
    assert "finish time" in m["throughput"]["reason"]


def test_throughput_refuses_without_sprints():
    i = issue("5", "finished", "Done", finished_at="2026-01-10T00:00:00Z")
    m = board_metrics.compute(snap([i]), cfg())
    assert m["throughput"]["periods"] is None
    assert "sprint" in m["throughput"]["reason"]


def test_throughput_refuses_if_any_finished_lacks_finish_time():
    a = issue("5", "finished", "Done", finished_at="2026-01-10T00:00:00Z")
    b = issue("7", "finished", "Done")
    m = board_metrics.compute(snap([a, b], sprints=SPRINTS), cfg())
    assert m["throughput"]["periods"] is None
    assert "7" in m["throughput"]["reason"]


def test_throughput_exact_per_sprint():
    issues = [issue("a", "finished", "Done", finished_at="2026-01-10T00:00:00Z"),
              issue("b", "finished", "Done", finished_at="2026-01-14T23:00:00Z"),
              issue("c", "finished", "Done", finished_at="2026-01-20T00:00:00Z"),
              issue("d", "active", "In Progress")]
    m = board_metrics.compute(snap(issues, source="native", sprints=SPRINTS), cfg())
    t = m["throughput"]
    assert t["basis"] == "exact"
    p = {x["sprint"]: x for x in t["periods"]}
    assert p["S1"]["finished"] == 2
    assert p["S2"]["finished"] == 1 and p["S2"]["open_period"] is True


def test_updated_at_is_not_a_finish_time():
    i = issue("5", "finished", "Done")  # updated_at present, finished_at absent
    m = board_metrics.compute(snap([i], sprints=SPRINTS), cfg())
    assert m["throughput"]["periods"] is None


def test_every_figure_has_a_basis():
    m = board_metrics.compute(snap(BOARD, sprints=SPRINTS), cfg(limits={"In Progress": 1}))
    for key in ("counts", "wip", "limits", "age", "missing_acceptance_criteria", "throughput"):
        assert m[key].get("basis"), key
    assert m["snapshot"]["source"] == "composed"


@pytest.mark.parametrize("bad", [
    {"schema": 2, "taken_at": TAKEN, "issues": []},
    {"schema": 1, "issues": []},
    {"schema": 1, "taken_at": TAKEN, "issues": [{"id": "1"}]},
    {"schema": 1, "taken_at": TAKEN, "issues": [issue("1", "running", "X")]},
    [],
])
def test_malformed_snapshot_fails(bad):
    with pytest.raises(board_metrics.InputError):
        board_metrics.compute(bad, cfg())


def run(*args):
    return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)],
                          capture_output=True, text=True, encoding="utf-8")


def test_cli_reads_snapshot_and_config(tmp_path):
    (tmp_path / "s.json").write_text(json.dumps(snap(BOARD)), encoding="utf-8")
    (tmp_path / "c.toml").write_text('[limits]\n"In Progress" = 1\n', encoding="utf-8")
    r = run(tmp_path / "s.json", "--config", tmp_path / "c.toml")
    assert r.returncode == 0, r.stderr
    assert json.loads(r.stdout)["limits"]["breaches"][0]["key"] == "In Progress"


def test_cli_malformed_fails_loudly(tmp_path):
    (tmp_path / "s.json").write_text("{", encoding="utf-8")
    r = run(tmp_path / "s.json")
    assert r.returncode != 0 and r.stderr and r.stdout == ""


def test_abandoned_is_not_throughput():
    done = issue("a", "finished", "Done", finished_at="2026-01-10T00:00:00Z")
    gone = issue("b", "finished", "Canceled", markers={"abandoned": True})  # no finish time needed
    m = board_metrics.compute(snap([done, gone], source="native", sprints=SPRINTS), cfg())
    assert m["throughput"]["periods"][0]["finished"] == 1
