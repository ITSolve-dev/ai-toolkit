"""Tests for run_pilot.py: the parts that decide what the pilot concludes."""

from __future__ import annotations

import argparse
import json
import random
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import run_pilot


class StripBase(unittest.TestCase):
    def test_real_agent_keeps_no_mention_of_the_base(self):
        text = (run_pilot.PLUGIN / "agents" / "craftsman.md").read_text(encoding="utf-8")
        stripped = run_pilot.strip_base(text)
        for word in ("base", "wiki", "knowledge", "page", "model opinion"):
            self.assertNotIn(word, stripped.lower(), word)
        self.assertIn("## Limits", stripped)
        self.assertIn("rules of good code", stripped)

    def test_missing_section_is_an_error(self):
        with self.assertRaises(ValueError):
            run_pilot.strip_base("# agent\n\n## Limits\n")


class AgentDefinition(unittest.TestCase):
    def test_base_variant_points_at_the_copy(self):
        agent = run_pilot.agent_definition(Path("/tmp/copy"))["craftsman"]
        self.assertIn("/tmp/copy/knowledge", agent["prompt"])
        self.assertNotIn("CLAUDE_PLUGIN_ROOT", agent["prompt"])

    def test_control_variant_has_no_base(self):
        agent = run_pilot.agent_definition(None)["craftsman"]
        self.assertNotIn("## The base", agent["prompt"])
        self.assertNotIn("CLAUDE_PLUGIN_ROOT", agent["prompt"])

    def test_variants_differ_only_by_that_section(self):
        with_base = run_pilot.agent_definition(Path("/x"))["craftsman"]
        without = run_pilot.agent_definition(None)["craftsman"]
        self.assertEqual(with_base["tools"], without["tools"])
        self.assertEqual(with_base["description"], without["description"])
        self.assertEqual(run_pilot.strip_base(with_base["prompt"]), without["prompt"])
        self.assertIn("Edit", without["tools"])


class CopyBase(unittest.TestCase):
    def test_copy_holds_the_wiki_and_never_the_raw_source(self):
        with tempfile.TemporaryDirectory() as folder:
            dest = run_pilot.copy_base(Path(folder) / "copy")
            self.assertTrue((dest / "knowledge" / "wiki" / "index.md").exists())
            self.assertFalse((dest / "knowledge" / "raw").exists())


class ClaudeArgs(unittest.TestCase):
    def test_task_checks_are_granted(self):
        args = run_pilot.claude_args(Path("a"), "m", ["run tests", "run linter"])
        granted = args[args.index("--allowedTools") + 1 :]
        self.assertEqual(granted, ["Bash(run tests)", "Bash(run linter)"])

    def test_no_checks_grants_no_commands(self):
        self.assertNotIn("--allowedTools", run_pilot.claude_args(Path("a"), "m", []))

    def test_user_settings_and_connectors_stay_out(self):
        args = run_pilot.claude_args(Path("a"), "m", ["t"])
        self.assertEqual(args[args.index("--setting-sources") + 1], "project")
        self.assertIn("--strict-mcp-config", args)

    def test_only_the_base_variant_reaches_the_base(self):
        self.assertNotIn("--add-dir", run_pilot.claude_args(Path("a"), "m", ["t"]))
        args = run_pilot.claude_args(Path("a"), "m", ["t"], Path("b"))
        self.assertEqual(args[args.index("--add-dir") + 1], "b")


def event(**body) -> str:
    return json.dumps(body)


class ParseStream(unittest.TestCase):
    def stream(self, report="Status: DONE\nmore") -> str:
        lines = [event(type="system", subtype="init", model="sonnet-x")]
        for path in (
            "C:\\x\\knowledge\\wiki\\complexity\\dry.md",
            "/p/knowledge/wiki/complexity/dry.md",
            "/p/knowledge/SCHEMA.md",
            "/project/wiki/notes.md",
        ):
            block = {"type": "tool_use", "name": "Read", "input": {"file_path": path}}
            lines.append(event(type="assistant", message={"content": [block]}))
        lines.append("not json")
        lines.append(
            event(
                type="result", session_id="s", result=report, total_cost_usd=0.5,
                usage={"input_tokens": 10, "output_tokens": 5, "service_tier": "x"},
            )
        )
        return "\n".join(lines)

    def test_pages_are_unique_and_only_from_the_base(self):
        self.assertEqual(run_pilot.parse_stream(self.stream())["pages"], ["wiki/complexity/dry.md"])

    def test_the_resolved_model_is_kept(self):
        self.assertEqual(run_pilot.parse_stream(self.stream())["model"], "sonnet-x")

    def test_tokens_and_status(self):
        parsed = run_pilot.parse_stream(self.stream())
        self.assertEqual(parsed["tokens"], 15)
        self.assertEqual(parsed["status"], "DONE")

    def test_needs_info_wins_over_a_later_word(self):
        parsed = run_pilot.parse_stream(self.stream("NEEDS_INFO\n1. Not DONE because..."))
        self.assertEqual(parsed["status"], "NEEDS_INFO")

    def test_the_first_status_word_decides(self):
        parsed = run_pilot.parse_stream(self.stream("Status: DONE\nNothing was BLOCKED."))
        self.assertEqual(parsed["status"], "DONE")

    def test_a_status_past_the_opening_still_counts(self):
        parsed = run_pilot.parse_stream(self.stream("x" * 500 + "\nNEEDS_INFO"))
        self.assertEqual(parsed["status"], "NEEDS_INFO")

    def test_a_separator_inside_the_report_keeps_the_result(self):
        parsed = run_pilot.parse_stream(self.stream("Status: DONE\u2028more"))
        self.assertEqual(parsed["status"], "DONE")

    def test_a_report_with_no_status_is_not_done(self):
        self.assertEqual(run_pilot.parse_stream(self.stream("hello"))["status"], "UNKNOWN")


class Blind(unittest.TestCase):
    def test_every_variant_appears_once_per_task(self):
        key = run_pilot.assign_blind(["a", "b"], random.Random(1))
        for solutions in key.values():
            self.assertEqual(sorted(solutions.values()), sorted(run_pilot.VARIANTS))

    def test_unblind_maps_ranks_back(self):
        key = {"t": {"solution-1": "base", "solution-2": "clean-1"}}
        ranks_given = {"t": {"solution-1": 1, "solution-2": 2}}
        self.assertEqual(run_pilot.unblind(ranks_given, key), {"t": {"base": 1, "clean-1": 2}})

    def test_a_second_draw_is_refused(self):
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder)
            (out / "key.json").write_text("{}", encoding="utf-8")
            with self.assertRaises(SystemExit):
                run_pilot.command_blind(argparse.Namespace(out=out, force=False))


def ranks(base: int, first: int, second: int) -> dict[str, int]:
    return {"overloaded": 4, "clean-1": first, "clean-2": second, "base": base}


class Verdict(unittest.TestCase):
    COMPLETE, GAIN, NOISE, FAILURES, FALSE = range(5)

    def tasks(self, won: int, tied: int = 0, noise: int = 0, count: int = 8) -> dict:
        table = {}
        for i in range(count):
            base = 1 if i < won else (2 if i < won + tied else 3)
            second = 1 if i < noise else 3
            table[f"t{i}"] = ranks(base, 2, second)
        return table

    def passed(self, table, failures=(), cited=10, false=1) -> list:
        return [p for _, p in run_pilot.verdict(table, list(failures), cited, false)]

    def test_six_of_eight_passes(self):
        self.assertEqual(self.passed(self.tasks(6)), [True] * 5)

    def test_five_fails(self):
        self.assertFalse(self.passed(self.tasks(5))[self.GAIN])

    def test_a_tie_counts_for_neither(self):
        self.assertFalse(self.passed(self.tasks(5, tied=3))[self.GAIN])

    def test_noise_as_large_as_gain_fails(self):
        self.assertFalse(self.passed(self.tasks(6, noise=6))[self.NOISE])

    def test_new_failure_fails(self):
        self.assertFalse(self.passed(self.tasks(6), failures=["t0: test"])[self.FAILURES])

    def test_false_share_is_bounded_at_ten_percent(self):
        self.assertTrue(self.passed(self.tasks(6), cited=10, false=1)[self.FALSE])
        self.assertFalse(self.passed(self.tasks(6), cited=10, false=2)[self.FALSE])

    def test_uncounted_false_applications_are_not_a_pass(self):
        self.assertIsNone(self.passed(self.tasks(6), cited=None, false=None)[self.FALSE])

    def test_no_citation_is_not_a_pass(self):
        self.assertIsNone(self.passed(self.tasks(6), cited=0, false=0)[self.FALSE])

    def test_fewer_tasks_never_pass(self):
        result = self.passed(self.tasks(4, count=4))
        self.assertIsNone(result[self.COMPLETE])
        self.assertIsNone(result[self.GAIN])
        self.assertIsNone(result[self.NOISE])


class RankProblems(unittest.TestCase):
    KEY = {"a": {"solution-1": "base", "solution-2": "clean-1"}, "b": {"solution-1": "base"}}

    def test_complete_ranks_pass(self):
        given = {"a": {"solution-1": 1, "solution-2": 2}, "b": {"solution-1": 1}}
        self.assertEqual(run_pilot.rank_problems(given, self.KEY), [])

    def test_a_missing_task_is_named(self):
        given = {"a": {"solution-1": 1, "solution-2": 2}}
        self.assertEqual(run_pilot.rank_problems(given, self.KEY), ["b"])

    def test_a_missing_solution_is_named(self):
        given = {"a": {"solution-1": 1}, "b": {"solution-1": 1}}
        self.assertEqual(run_pilot.rank_problems(given, self.KEY), ["a"])


class Gates(unittest.TestCase):
    def test_only_finished_runs_reach_the_grader(self):
        statuses = {"a": "DONE", "b": "BLOCKED", "c": "NEEDS_INFO", "d": "UNKNOWN", "e": "MISSING"}
        self.assertEqual(run_pilot.unfinished_runs(statuses), ["c", "d", "e"])

    def test_a_check_failing_before_the_edit_stops_the_run(self):
        self.assertTrue(run_pilot.check_before_edit({}, {"test": 1}))
        self.assertFalse(run_pilot.check_before_edit({"expected_failing": ["test"]}, {"test": 1}))

    def test_an_expected_failure_that_passes_stops_the_run(self):
        self.assertTrue(run_pilot.check_before_edit({"expected_failing": ["test"]}, {"test": 0}))

    def test_a_reproducer_still_failing_is_not_a_new_failure(self):
        task = {"expected_failing": ["repro"]}
        self.assertEqual(run_pilot.new_failures(task, {"repro": 1, "test": 2}), ["test"])


class RevealsBase(unittest.TestCase):
    def test_added_line_with_a_wiki_path(self):
        self.assertTrue(run_pilot.reveals_base("+# see wiki\\complexity\\dry.md\n", set()))

    def test_added_line_with_a_slug(self):
        self.assertTrue(run_pilot.reveals_base("+# per tell-dont-ask\n", {"tell-dont-ask"}))

    def test_context_lines_and_plain_words_do_not_count(self):
        self.assertFalse(run_pilot.reveals_base(" knowledge/x\n+dry = True\n", {"dry"}))


class Claude(unittest.TestCase):
    def call(self, code: int, stream: str) -> str:
        with mock.patch.object(run_pilot.shutil, "which", return_value="claude"):
            with mock.patch.object(run_pilot, "run_bounded", return_value=(code, stream, "boom")) as run:
                result = run_pilot.claude([], "brief", Path("."))
        self.env = run.call_args.kwargs["env"]
        return result

    def test_a_good_run_returns_its_stream(self):
        stream = event(type="result", result="DONE", is_error=False)
        self.assertEqual(self.call(0, stream), stream)

    def test_project_memory_is_off(self):
        self.call(0, event(type="result", result="DONE"))
        self.assertEqual(self.env["CLAUDE_CODE_DISABLE_AUTO_MEMORY"], "1")

    def test_error_result_raises_though_its_subtype_says_success(self):
        with self.assertRaises(RuntimeError):
            self.call(0, event(type="result", subtype="success", is_error=True, result="limit"))

    def test_non_zero_exit_raises(self):
        with self.assertRaises(RuntimeError):
            self.call(1, event(type="result", result="DONE"))

    def test_no_result_event_raises(self):
        with self.assertRaises(RuntimeError):
            self.call(0, event(type="system", subtype="init"))


class RunBounded(unittest.TestCase):
    def test_timeout_stops_the_child_as_well(self):
        child = (
            "import subprocess, sys, time;"
            "subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(9)']);"
            "time.sleep(9)"
        )
        started = time.monotonic()
        code, _, _ = run_pilot.run_bounded([sys.executable, "-c", child], Path("."), 1)
        self.assertEqual(code, -1)
        self.assertLess(time.monotonic() - started, 7)


def commit(repo: Path, message: str) -> str:
    run_pilot.git(repo, "add", "-A")
    run_pilot.git(
        repo, "-c", "user.name=t", "-c", "user.email=t@example.invalid",
        "-c", "commit.gpgsign=false", "commit", "-qm", message,
    )
    return run_pilot.git(repo, "rev-parse", "HEAD").strip()


class Export(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(folder.cleanup)
        self.root = Path(folder.name)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        run_pilot.git(self.repo, "init", "-q")
        (self.repo / "old.txt").write_text("line one\nline two\nline three\n", encoding="utf-8")
        (self.repo / "dead.txt").write_text("unused\n", encoding="utf-8")
        self.first = commit(self.repo, "before")
        (self.repo / "solution.txt").write_text("the real fix\n", encoding="utf-8")
        commit(self.repo, "the fix")
        self.task = {"repo": str(self.repo), "commit": self.first, "checks": []}
        self.work = self.root / "work"
        run_pilot.snapshot(self.task, self.work)
        self.run_dir = self.root / "run"
        self.run_dir.mkdir()

    def test_export_has_no_later_commits(self):
        self.assertFalse((self.work / "solution.txt").exists())
        history = run_pilot.git(self.work, "log", "--all", "--oneline")
        self.assertEqual(len(history.strip().splitlines()), 1)

    def test_patch_shows_deletion_rename_and_new_file(self):
        (self.work / "dead.txt").unlink()
        (self.work / "old.txt").rename(self.work / "new.txt")
        (self.work / "added.txt").write_text("hello\n", encoding="utf-8")
        run_pilot.collect(self.run_dir, self.work, self.task, event(type="result", result="DONE"))
        patch = (self.run_dir / "diff.patch").read_text(encoding="utf-8")
        self.assertIn("deleted file", patch)
        self.assertIn("rename from old.txt", patch)
        self.assertIn("new file", patch)

    def test_what_a_check_writes_stays_out_of_the_tree(self):
        command = "echo noise > generated.txt"
        task = {**self.task, "checks": [command]}
        run = run_pilot.collect(self.run_dir, self.work, task, event(type="result", result="DONE"))
        self.assertEqual(run["checks"], {command: 0})
        self.assertFalse((self.work / "generated.txt").exists())
        self.assertIn(command, (self.run_dir / "checks.log").read_text(encoding="utf-8"))

    def test_setup_is_part_of_the_starting_point(self):
        task = {**self.task, "setup": ["echo built > built.txt"]}
        work = self.root / "work-setup"
        run_pilot.snapshot(task, work)
        self.assertEqual(run_pilot.git(work, "status", "--short"), "")
        self.assertTrue((work / "built.txt").exists())

    def test_a_resumed_run_adds_tokens_and_keeps_the_cumulative_cost(self):
        previous = {"tokens": 10, "pages": ["wiki/a.md"], "args": ["x"], "worktree": "w", "cost_usd": 1.0}
        stream = event(type="result", result="DONE", total_cost_usd=1.5, usage={"input_tokens": 5})
        run = run_pilot.collect(self.run_dir, self.work, self.task, stream, previous=previous)
        self.assertEqual(run["tokens"], 15)
        self.assertEqual(run["cost_usd"], 1.5)
        self.assertEqual(run["args"], ["x"])

    def test_patch_keeps_line_feeds(self):
        path = self.root / "x.patch"
        run_pilot.write_text(path, "a\nb\n")
        self.assertEqual(path.read_bytes(), b"a\nb\n")


if __name__ == "__main__":
    unittest.main()
