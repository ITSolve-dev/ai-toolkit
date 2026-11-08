import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HOOK = Path(__file__).resolve().parents[1] / "hooks" / "guard_knowledge.py"


class Guard(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        base = Path(self.tmp.name).resolve()
        self.root = base / "plugin"
        self.knowledge = self.root / "knowledge"
        self.project = base / "project"
        self.knowledge.mkdir(parents=True)
        self.project.mkdir()

    def run_hook(self, tool, tool_input, env_root=True, raw=None):
        env = {k: v for k, v in os.environ.items() if k != "CLAUDE_PLUGIN_ROOT"}
        env.pop("PYTHONUTF8", None)
        env.pop("PYTHONIOENCODING", None)
        env.update(getattr(self, "env_extra", {}))
        if env_root:
            env["CLAUDE_PLUGIN_ROOT"] = str(self.root)
        payload = raw if raw is not None else json.dumps(
            {"tool_name": tool, "tool_input": tool_input, "cwd": str(self.project)},
            ensure_ascii=False,
        )
        # Claude Code sends UTF-8 whatever the code page, so the test sends bytes too.
        result = subprocess.run(
            [sys.executable, str(HOOK)], input=payload.encode("utf-8"), capture_output=True, env=env
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        if not result.stdout:
            return None
        return json.loads(result.stdout)["hookSpecificOutput"]["permissionDecision"]

    def test_read_of_base_is_allowed(self):
        self.assertEqual(self.run_hook("Read", {"file_path": str(self.knowledge / "wiki/a.md")}), "allow")

    def test_grep_of_base_reads_path_not_file_path(self):
        self.assertEqual(self.run_hook("Grep", {"pattern": "x", "path": str(self.knowledge)}), "allow")

    def test_glob_of_base_is_allowed(self):
        self.assertEqual(self.run_hook("Glob", {"pattern": "**/*.md", "path": str(self.knowledge)}), "allow")

    def test_glob_escaping_the_base_gets_no_decision(self):
        tool_input = {"pattern": "../../**", "path": str(self.knowledge)}
        self.assertIsNone(self.run_hook("Glob", tool_input))

    def test_read_outside_base_gets_no_decision(self):
        self.assertIsNone(self.run_hook("Read", {"file_path": str(self.root / "plugin.json")}))
        self.assertIsNone(self.run_hook("Read", {"file_path": str(self.project / "a.py")}))

    def test_sibling_with_shared_prefix_is_outside(self):
        sibling = self.root / "knowledge-extra" / "a.md"
        self.assertIsNone(self.run_hook("Read", {"file_path": str(sibling)}))

    def test_traversal_out_of_base_gets_no_decision(self):
        path = str(self.knowledge) + "/../../project/secret.md"
        self.assertIsNone(self.run_hook("Read", {"file_path": path}))

    def test_relative_path_resolves_against_cwd(self):
        self.assertIsNone(self.run_hook("Write", {"file_path": "src/a.py"}))
        self.assertEqual(self.run_hook("Write", {"file_path": "../plugin/knowledge/a.md"}), "deny")

    def test_write_under_plugin_root_is_denied(self):
        for tool in ("Write", "Edit"):
            self.assertEqual(self.run_hook(tool, {"file_path": str(self.knowledge / "wiki/a.md")}), "deny")
            self.assertEqual(self.run_hook(tool, {"file_path": str(self.root / "hooks/x.py")}), "deny")

    def test_notebook_edit_under_plugin_root_is_denied(self):
        self.assertEqual(self.run_hook("NotebookEdit", {"notebook_path": str(self.knowledge / "a.ipynb")}), "deny")

    def test_write_in_project_gets_no_decision(self):
        self.assertIsNone(self.run_hook("Write", {"file_path": str(self.project / "a.py")}))

    def test_shell_naming_the_plugin_is_denied(self):
        posix = self.knowledge.as_posix()
        root = self.root.as_posix()
        for command in (
            f"echo x >> {posix}/wiki/a.md",
            f'rm -rf "{self.knowledge}"',
            f"cd {root} && rm -rf knowledge",
            f"rm -rf {root}",
            f"mv {root} {root}.bak",
            f"find {root} -name '*.md' -delete",
            f"sed -i s/a/b/ {root}/know*/wiki/a.md",
            f"rm {root}/./knowledge/a.md",
            f"rm {root}/hooks/../knowledge/a.md",
            f'rm "{root}"/knowledge/a.md',
        ):
            self.assertEqual(self.run_hook("Bash", {"command": command}), "deny", command)
            self.assertEqual(self.run_hook("PowerShell", {"command": command}), "deny", command)

    def test_shell_with_home_spelling_is_denied(self):
        home = Path(self.tmp.name).resolve()
        self.env_extra = {"HOME": str(home), "USERPROFILE": str(home)}
        relative = self.root.relative_to(home).as_posix()
        for prefix in ("~", "$HOME", "${HOME}"):
            command = f"rm {prefix}/{relative}/knowledge/a.md"
            self.assertEqual(self.run_hook("Bash", {"command": command}), "deny", command)

    def test_shell_with_escaped_space_is_denied(self):
        self.root = self.root.parent / "Jo Smith" / "plugin"
        (self.root / "knowledge").mkdir(parents=True)
        escaped = self.root.as_posix().replace(" ", "\\ ")
        self.assertEqual(self.run_hook("Bash", {"command": f"rm {escaped}/knowledge/a.md"}), "deny")

    def test_shell_run_from_inside_the_plugin_is_denied(self):
        payload = json.dumps(
            {"tool_name": "Bash", "tool_input": {"command": "rm a.md"}, "cwd": str(self.knowledge)}
        )
        self.assertEqual(self.run_hook("", {}, raw=payload), "deny")

    def test_shell_naming_a_sibling_gets_no_decision(self):
        self.assertIsNone(self.run_hook("Bash", {"command": f"cat {self.root.as_posix()}-old/a.md"}))

    def test_variable_in_a_commit_message_gets_no_decision(self):
        command = "git commit -m 'fix: read from $CLAUDE_PLUGIN_ROOT/knowledge in agents'"
        self.assertIsNone(self.run_hook("Bash", {"command": command}))

    def test_cyrillic_plugin_root_is_understood(self):
        self.root = self.root.parent / "Роман" / "plugin"
        self.knowledge = self.root / "knowledge"
        self.knowledge.mkdir(parents=True)
        tool_input = {"file_path": str(self.knowledge / "a.md")}
        self.assertEqual(self.run_hook("Read", tool_input), "allow")
        self.assertEqual(self.run_hook("Write", tool_input), "deny")

    def test_glob_with_absolute_pattern_and_a_path_gets_no_decision(self):
        tool_input = {"pattern": "/Users/x/**", "path": str(self.knowledge)}
        self.assertIsNone(self.run_hook("Glob", tool_input))

    def test_glob_with_a_pattern_inside_the_base_is_allowed(self):
        pattern = self.knowledge.as_posix() + "/wiki/*.md"
        self.assertEqual(self.run_hook("Glob", {"pattern": pattern}), "allow")

    def test_glob_with_a_pattern_outside_the_base_gets_no_decision(self):
        pattern = self.project.as_posix() + "/*.md"
        self.assertIsNone(self.run_hook("Glob", {"pattern": pattern}))
        self.assertIsNone(self.run_hook("Glob", {"pattern": "**/*.md"}))

    @unittest.skipUnless(os.name == "nt", "Git Bash spelling exists only on Windows")
    def test_bash_git_bash_spelling_is_denied(self):
        posix = self.knowledge.as_posix()
        spelled = "/" + posix[0].lower() + posix[2:]
        self.assertEqual(self.run_hook("Bash", {"command": f"rm {spelled}/a.md"}), "deny")

    def test_bash_elsewhere_gets_no_decision(self):
        self.assertIsNone(self.run_hook("Bash", {"command": "pytest -q"}))

    def test_other_tools_get_no_decision(self):
        self.assertIsNone(self.run_hook("WebFetch", {"url": "https://example.com"}))

    def test_missing_plugin_root_stays_silent(self):
        self.assertIsNone(self.run_hook("Read", {"file_path": "x"}, env_root=False))

    def test_malformed_payload_stays_silent(self):
        for raw in ("not json", "[]", "null", '{"tool_name": "Read", "tool_input": "x"}'):
            self.assertIsNone(self.run_hook("", {}, raw=raw))


if __name__ == "__main__":
    unittest.main()
