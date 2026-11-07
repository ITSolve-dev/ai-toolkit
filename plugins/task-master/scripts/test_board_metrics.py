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


# --- wip per assignee -------------------------------------------------------------------------

def test_wip_by_assignee_counts_started_items_and_unassigned():
    issues = [issue("1", "active", "In Progress", assignees=[{"id": "u1", "name": "Ann"}]),
              issue("2", "handed_off", "In Review", assignees=[{"id": "u1", "name": "Ann"},
                                                                {"id": "u2", "name": "Bob"}]),
              issue("3", "active", "In Progress", assignees=[]),
              issue("4", "active", "In Progress", assignees=None),
              issue("5", "queued", "Ready", assignees=[{"id": "u2", "name": "Bob"}]),
              issue("6", "active", "In Progress")]  # no assignees key: the read did not carry it
    w = board_metrics.compute(snap(issues), cfg())["wip"]
    assert w["by_assignee"] == {"Ann": 2, "Bob": 1}
    assert w["unassigned"] == {"count": 2, "ids": ["3", "4"]}
    assert w["assignees_not_read"] == {"count": 1, "ids": ["6"]}


# --- cycle time, percentiles, SLE -------------------------------------------------------------

def done(id, started, finished, **over):
    return issue(id, "finished", "Done", started_at=started, finished_at=finished, **over)


TEN = [done(str(i), "2026-01-01T00:00:00Z", f"2026-01-{1 + i:02d}T00:00:00Z") for i in range(1, 11)]


def test_cycle_time_percentiles_nearest_rank():
    c = board_metrics.compute(snap(TEN, source="native"), cfg())["cycle_time"]
    assert c["basis"] == "exact"
    assert c["n"] == 10
    assert c["percentiles"] == {"50": 5.0, "70": 7.0, "85": 9.0, "95": 10.0}
    assert {x["id"]: x["days"] for x in c["items"]}["3"] == 3.0


def test_cycle_time_refuses_without_started_at():
    # status_since of a finished item is when it became finished, not when it started
    i = issue("1", "finished", "Done", status_since="2026-01-02T00:00:00Z", finished_at="2026-01-05T00:00:00Z")
    c = board_metrics.compute(snap([i]), cfg())["cycle_time"]
    assert c["percentiles"] is None and c["n"] is None
    assert "started_at" in c["reason"] and "1" in c["reason"]
    assert c["basis"] == "not_computed"


def test_cycle_time_refuses_without_finished_at():
    i = issue("1", "finished", "Done", started_at="2026-01-02T00:00:00Z")
    c = board_metrics.compute(snap([i]), cfg())["cycle_time"]
    assert c["percentiles"] is None and "finish time" in c["reason"]


def test_cycle_time_skips_abandoned_and_open():
    issues = TEN[:2] + [issue("x", "finished", "Canceled", markers={"abandoned": True}),
                        issue("y", "active", "In Progress")]
    c = board_metrics.compute(snap(issues), cfg())["cycle_time"]
    assert c["n"] == 2


def test_cycle_time_no_finished_items():
    c = board_metrics.compute(snap([issue("y", "active", "In Progress")]), cfg())["cycle_time"]
    assert c["percentiles"] is None and "no finished" in c["reason"]


def test_cycle_time_finish_before_start_fails():
    with pytest.raises(board_metrics.InputError):
        board_metrics.compute(snap([done("1", "2026-01-05T00:00:00Z", "2026-01-01T00:00:00Z")]), cfg())


def test_cycle_time_within_window_only():
    w = board_metrics.compute(snap(TEN), cfg(), window=("2026-01-07", "2026-01-10"))["cycle_time"]
    assert sorted(x["id"] for x in w["items"]) == ["6", "7", "8", "9"]
    assert w["window"] == {"start": "2026-01-07", "end": "2026-01-10"}


def sle_cfg(sle):
    return {"project": {"sle": sle}}


def test_sle_share_from_cycle_times():
    s = board_metrics.compute(snap(TEN), sle_cfg("7 days at 85%"))["sle"]
    assert s["days"] == 7 and s["probability"] == 85
    assert s["within"] == 7 and s["n"] == 10 and s["share"] == 0.7
    assert s["misses"] == ["8", "9", "10"]
    assert s["basis"] == "exact"


def test_sle_refuses_without_cycle_times():
    i = issue("1", "finished", "Done", finished_at="2026-01-05T00:00:00Z")
    s = board_metrics.compute(snap([i]), sle_cfg("7 days at 85%"))["sle"]
    assert s["share"] is None and "cycle time" in s["reason"]


def test_sle_not_declared():
    s = board_metrics.compute(snap(TEN), cfg())["sle"]
    assert s["declared"] is False and s["share"] is None


def test_sle_malformed_fails():
    with pytest.raises(board_metrics.InputError):
        board_metrics.compute(snap(TEN), sle_cfg("about a week"))


# --- arrivals and throughput over a window ----------------------------------------------------

def test_arrivals_per_sprint_and_window():
    issues = [issue("a", "queued", "Ready", created="2026-01-03T00:00:00Z"),
              issue("b", "queued", "Ready", created="2026-01-14T12:00:00Z"),
              issue("c", "queued", "Ready", created="2026-01-20T00:00:00Z")]
    a = board_metrics.compute(snap(issues, sprints=SPRINTS), cfg(), window=("2026-01-10", "2026-01-20"))["arrivals"]
    p = {x["sprint"]: x["arrived"] for x in a["periods"]}
    assert p == {"S1": 2, "S2": 1}
    assert a["window"]["arrived"] == 2 and sorted(a["window"]["ids"]) == ["b", "c"]
    assert "created_at" in a["basis"]


def test_arrivals_refuse_when_created_at_missing():
    issues = [issue("a", "queued", "Ready", created=None)]
    a = board_metrics.compute(snap(issues, sprints=SPRINTS), cfg(), window=("2026-01-10", "2026-01-20"))["arrivals"]
    assert a["periods"] is None and "a" in a["reason"]
    assert a["window"]["arrived"] is None


def test_arrivals_without_window_or_sprints():
    a = board_metrics.compute(snap(BOARD), cfg())["arrivals"]
    assert a["periods"] is None and a["window"]["arrived"] is None
    assert "window" in a["window"]["reason"]


def test_throughput_over_window():
    issues = [issue("a", "finished", "Done", finished_at="2026-01-10T00:00:00Z"),
              issue("b", "finished", "Done", finished_at="2026-01-20T23:00:00Z"),
              issue("c", "finished", "Done", finished_at="2026-01-21T00:00:00Z")]
    t = board_metrics.compute(snap(issues), cfg(), window=("2026-01-10", "2026-01-20"))["throughput"]
    assert t["window"]["finished"] == 2 and t["window"]["basis"] == "exact"
    assert sorted(t["window"]["ids"]) == ["a", "b"]
    assert t["periods"] is None  # no sprints: the per-sprint figure still refuses


def test_throughput_window_refuses_without_finish_times():
    t = board_metrics.compute(snap(BOARD), cfg(), window=("2026-01-10", "2026-01-20"))["throughput"]
    assert t["window"]["finished"] is None and "finish time" in t["window"]["reason"]


def test_window_end_before_start_fails():
    with pytest.raises(board_metrics.InputError):
        board_metrics.compute(snap(BOARD), cfg(), window=("2026-01-20", "2026-01-10"))


# --- estimates and velocity -------------------------------------------------------------------

def est_cfg(spec):
    return {"fields": {"estimate": spec}}


def test_estimate_from_labels_totals_and_missing_counted_apart():
    issues = [issue("1", "queued", "Ready", labels=["size-3"]),
              issue("2", "active", "In Progress", labels=[{"name": "size-5"}]),
              issue("3", "active", "In Progress", labels=[]),
              issue("4", "queued", "Ready", labels=["size-XL"]),
              issue("5", "queued", "Ready", labels=["size-1", "size-2"])]
    e = board_metrics.compute(snap(issues), est_cfg("label:size-{value}"))["estimates"]
    assert e["declared"] is True and e["total"] == 8
    assert e["by_kind"] == {"queued": 3, "active": 5}
    assert e["with_estimate"] == 2
    assert e["without_estimate"] == {"count": 1, "ids": ["3"]}
    assert e["unreadable"] == {"count": 2, "ids": ["4", "5"]}


def test_estimate_from_field():
    issues = [issue("1", "queued", "Ready", points=2), issue("2", "queued", "Ready", points=None),
              issue("3", "queued", "Ready", fields={"points": "1.5"})]
    e = board_metrics.compute(snap(issues), est_cfg("field:points"))["estimates"]
    assert e["total"] == 3.5 and e["without_estimate"]["ids"] == ["2"]


def test_estimates_not_declared():
    e = board_metrics.compute(snap(BOARD), cfg())["estimates"]
    assert e["declared"] is False and e["total"] is None


def test_bad_estimate_spec_fails():
    with pytest.raises(board_metrics.InputError):
        board_metrics.compute(snap(BOARD), est_cfg("size"))


def test_velocity_by_sprint_field():
    issues = [issue("a", "finished", "Done", labels=["size-3"], sprint="S1"),
              issue("b", "finished", "Done", labels=["size-5"], sprint={"id": "1", "name": "S1"}),
              issue("c", "finished", "Done", labels=[], sprint="S1"),
              issue("d", "active", "In Progress", labels=["size-8"], sprint="S1"),
              issue("e", "finished", "Done", labels=["size-2"], sprint="S2"),
              issue("f", "finished", "Canceled", labels=["size-2"], sprint="S2", markers={"abandoned": True}),
              issue("g", "finished", "Done", labels=["size-1"], sprint=None)]
    v = board_metrics.compute(snap(issues, sprints=SPRINTS), est_cfg("label:size-{value}"))["velocity"]
    assert v["basis"] == "by_sprint_field"
    assert "carried" in v["method"]
    p = {x["sprint"]: x for x in v["periods"]}
    assert p["S1"]["points"] == 8 and p["S1"]["finished"] == 3
    assert p["S1"]["finished_without_estimate"] == {"count": 1, "ids": ["c"]}
    assert p["S2"]["points"] == 2 and p["S2"]["finished"] == 1
    assert v["finished_outside_sprints"] == {"count": 1, "ids": ["g"]}


def test_velocity_without_estimates_is_by_count():
    issues = [issue("a", "finished", "Done", sprint="S1")]
    v = board_metrics.compute(snap(issues, sprints=SPRINTS), cfg())["velocity"]
    p = v["periods"][0]
    assert p["finished"] == 1 and p["points"] is None
    assert "estimate" in v["points_reason"]


def test_velocity_refuses_without_sprints():
    v = board_metrics.compute(snap(BOARD), cfg())["velocity"]
    assert v["periods"] is None and "sprint" in v["reason"]


# --- snapshot comparison ----------------------------------------------------------------------

def test_compare_two_snapshots():
    earlier = snap([issue("1", "queued", "Ready", labels=["size-3"], sprint="S1"),
                    issue("2", "queued", "Ready"),
                    issue("3", "active", "In Progress", sprint="S1")])
    earlier["taken_at"] = "2026-01-15T00:00:00Z"
    later = snap([issue("1", "active", "In Progress", labels=["size-5"], sprint="S1"),
                  issue("3", "active", "In Progress", sprint="S2"),
                  issue("4", "queued", "Ready")])
    c = board_metrics.compute(later, est_cfg("label:size-{value}"), earlier=earlier)["comparison"]
    assert c["made"] is True and c["earlier_taken_at"] == "2026-01-15T00:00:00Z"
    assert c["added"] == ["4"] and c["removed"] == ["2"]
    assert c["status_changed"] == [{"id": "1", "from": "Ready", "to": "In Progress"}]
    assert c["kind_changed"] == [{"id": "1", "from": "queued", "to": "active"}]
    assert c["estimate_changed"] == [{"id": "1", "from": 3, "to": 5}]
    assert c["sprint_changed"] == [{"id": "3", "from": "S1", "to": "S2"}]
    assert "net" in c["basis"]


def test_compare_not_given():
    c = board_metrics.compute(snap(BOARD), cfg())["comparison"]
    assert c["made"] is False and c["reason"]


def test_compare_estimate_not_declared():
    c = board_metrics.compute(snap(BOARD), cfg(), earlier=snap(BOARD))["comparison"]
    assert c["estimate_changed"] is None and c["estimate_reason"]


def test_compare_earlier_after_later_fails():
    earlier = snap(BOARD)
    earlier["taken_at"] = "2026-03-01T00:00:00Z"
    with pytest.raises(board_metrics.InputError):
        board_metrics.compute(snap(BOARD), cfg(), earlier=earlier)


# --- series -----------------------------------------------------------------------------------

def test_series_refuse_without_history():
    s = board_metrics.compute(snap(BOARD, sprints=SPRINTS), est_cfg("label:size-{value}"))["series"]
    for name in ("cfd", "burndown", "scatterplot", "histogram"):
        assert s[name]["points"] is None, name
        assert s[name]["reason"], name
        assert s[name]["basis"] == "not_computed", name
    assert "transitions" in s["cfd"]["reason"]


def tr(*pairs):
    return [{"status": st, "at": at} for st, at in pairs]


def test_cfd_per_day_counts_per_kind():
    m = {"Ready": "queued", "In Progress": "active", "Done": "finished"}
    issues = [issue("1", "finished", "Done", transitions=tr(("Ready", "2026-01-01T09:00:00Z"),
                                                            ("In Progress", "2026-01-02T09:00:00Z"),
                                                            ("Done", "2026-01-03T09:00:00Z"))),
              issue("2", "active", "In Progress", transitions=tr(("Ready", "2026-01-02T10:00:00Z"),
                                                                 ("In Progress", "2026-01-03T10:00:00Z")))]
    s = snap(issues, source="native")
    s["mapping"] = m
    s["taken_at"] = "2026-01-03T23:00:00Z"
    cfd = board_metrics.compute(s, cfg())["series"]["cfd"]
    assert cfd["basis"] == "exact"
    assert cfd["points"] == [
        {"date": "2026-01-01", "counts": {"queued": 1}},
        {"date": "2026-01-02", "counts": {"queued": 1, "active": 1}},
        {"date": "2026-01-03", "counts": {"active": 1, "finished": 1}},
    ]


def test_cfd_refuses_if_any_issue_lacks_transitions():
    issues = [issue("1", "active", "In Progress", transitions=tr(("In Progress", "2026-01-02T00:00:00Z"))),
              issue("2", "active", "In Progress")]
    cfd = board_metrics.compute(snap(issues), cfg())["series"]["cfd"]
    assert cfd["points"] is None and "2" in cfd["reason"]


def test_scatterplot_and_histogram_from_cycle_times():
    s = board_metrics.compute(snap(TEN[:3]), cfg())["series"]
    assert s["scatterplot"]["points"] == [{"id": "1", "finished": "2026-01-02", "days": 1.0},
                                          {"id": "2", "finished": "2026-01-03", "days": 2.0},
                                          {"id": "3", "finished": "2026-01-04", "days": 3.0}]
    assert s["histogram"]["points"] == [{"from_days": 1, "to_days": 2, "count": 1},
                                        {"from_days": 2, "to_days": 3, "count": 1},
                                        {"from_days": 3, "to_days": 4, "count": 1}]


def test_burndown_remaining_estimate_per_day():
    sprints = [{"id": "1", "name": "S1", "state": "active", "start_date": "2026-01-01", "end_date": "2026-01-04"}]
    issues = [issue("a", "finished", "Done", labels=["size-3"], sprint="S1", finished_at="2026-01-02T10:00:00Z"),
              issue("b", "active", "In Progress", labels=["size-5"], sprint="S1"),
              issue("c", "active", "In Progress", labels=[], sprint="S1"),
              issue("d", "queued", "Ready", labels=["size-8"], sprint="S2")]
    s = snap(issues, sprints=sprints)
    s["taken_at"] = "2026-01-03T12:00:00Z"
    b = board_metrics.compute(s, est_cfg("label:size-{value}"))["series"]["burndown"]
    assert b["sprint"] == "S1"
    assert b["points"] == [{"date": "2026-01-01", "remaining": 8},
                           {"date": "2026-01-02", "remaining": 5},
                           {"date": "2026-01-03", "remaining": 5}]
    assert b["without_estimate"] == {"count": 1, "ids": ["c"]}
    assert "scope" in b["method"]


def test_burndown_refuses_without_finish_times():
    sprints = [{"id": "1", "name": "S1", "state": "active", "start_date": "2026-01-01", "end_date": "2026-01-04"}]
    issues = [issue("a", "finished", "Done", labels=["size-3"], sprint="S1")]
    b = board_metrics.compute(snap(issues, sprints=sprints), est_cfg("label:size-{value}"))["series"]["burndown"]
    assert b["points"] is None and "finish time" in b["reason"]


def test_burndown_named_sprint():
    issues = [issue("a", "active", "In Progress", labels=["size-3"], sprint="S1")]
    b = board_metrics.compute(snap(issues, sprints=SPRINTS), est_cfg("label:size-{value}"),
                              sprint="S1")["series"]["burndown"]
    assert b["sprint"] == "S1" and len(b["points"]) == 14


def test_new_figures_have_a_basis():
    m = board_metrics.compute(snap(BOARD, sprints=SPRINTS), cfg())
    for key in ("cycle_time", "sle", "arrivals", "estimates", "velocity", "comparison"):
        assert m[key].get("basis"), key


def test_cli_window_compare_and_sprint(tmp_path):
    (tmp_path / "s.json").write_text(json.dumps(snap(TEN)), encoding="utf-8")
    e = snap(TEN[:5])
    e["taken_at"] = "2026-01-05T00:00:00Z"
    (tmp_path / "e.json").write_text(json.dumps(e), encoding="utf-8")
    r = run(tmp_path / "s.json", "--compare", tmp_path / "e.json",
            "--window-start", "2026-01-01", "--window-end", "2026-01-31", "--sprint", "S1")
    assert r.returncode == 0, r.stderr
    out = json.loads(r.stdout)
    assert out["throughput"]["window"]["finished"] == 10
    assert len(out["comparison"]["added"]) == 5


def test_cli_window_needs_both_ends(tmp_path):
    (tmp_path / "s.json").write_text(json.dumps(snap(TEN)), encoding="utf-8")
    r = run(tmp_path / "s.json", "--window-start", "2026-01-01")
    assert r.returncode == 2 and r.stdout == ""


# --- started kinds from config ----------------------------------------------------------------

def sk_cfg(kinds, **extra):
    return {"project": {"started_kinds": kinds, **extra}}


def test_started_kinds_default_is_active_and_handed_off():
    m = board_metrics.compute(snap(BOARD), cfg())
    assert m["wip"]["started_kinds"] == ["active", "handed_off"]
    assert m["age"]["started_kinds"] == ["active", "handed_off"]


def test_started_kinds_with_queued_counts_queued_as_wip():
    issues = BOARD[:5] + [issue("7", "queued", "Ready", assignees=[{"id": "u1", "name": "Ann"}])]
    m = board_metrics.compute(snap(issues), sk_cfg(["queued", "active", "handed_off"]))
    w = m["wip"]
    assert w["total"] == 5
    assert w["by_kind"] == {"active": 2, "handed_off": 1, "queued": 2}
    assert w["by_assignee"] == {"Ann": 1}
    assert w["started_kinds"] == ["queued", "active", "handed_off"]
    assert "queued" in w["basis"]
    a = {x["id"]: x for x in m["age"]["items"]}
    assert a["4"]["started"] is True and a["1"]["started"] is True


def test_age_marks_unstarted_items():
    a = {x["id"]: x for x in board_metrics.compute(snap(BOARD), cfg())["age"]["items"]}
    assert a["4"]["started"] is False  # queued is not started by default
    assert a["1"]["started"] is True


def test_cycle_time_starts_at_first_started_kind_in_transitions():
    s = snap([issue("1", "finished", "Done", finished_at="2026-01-05T00:00:00Z",
                    transitions=tr(("Backlog", "2026-01-01T00:00:00Z"), ("Ready", "2026-01-02T00:00:00Z"),
                                   ("In Progress", "2026-01-03T00:00:00Z"), ("Done", "2026-01-05T00:00:00Z")))])
    s["mapping"] = {"Backlog": "before_start", "Ready": "queued", "In Progress": "active", "Done": "finished"}
    default = board_metrics.compute(s, cfg())["cycle_time"]["items"][0]
    assert default["days"] == 2.0 and default["start_source"] == "transitions"
    wide = board_metrics.compute(s, sk_cfg(["queued", "active"]))["cycle_time"]["items"][0]
    assert wide["days"] == 3.0 and wide["started_at"] == "2026-01-02T00:00:00Z"


def test_cycle_time_refuses_when_transitions_never_reach_a_started_kind():
    s = snap([issue("1", "finished", "Done", finished_at="2026-01-05T00:00:00Z",
                    transitions=tr(("Ready", "2026-01-02T00:00:00Z"), ("Done", "2026-01-05T00:00:00Z")))])
    s["mapping"] = {"Ready": "queued", "Done": "finished"}
    c = board_metrics.compute(s, cfg())["cycle_time"]
    assert c["n"] is None and "1" in c["reason"]


def test_cycle_time_from_tool_started_at_is_labelled():
    c = board_metrics.compute(snap(TEN[:1]), cfg())["cycle_time"]
    assert c["items"][0]["start_source"] == "started_at"


@pytest.mark.parametrize("bad", [[], ["running"], ["finished"], "active", [1]])
def test_bad_started_kinds_fail(bad):
    with pytest.raises(board_metrics.InputError):
        board_metrics.compute(snap(BOARD), sk_cfg(bad))
