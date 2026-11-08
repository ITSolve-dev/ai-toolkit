#!/usr/bin/env python3
"""Run the pilot from the plugin's design doc: same agent, same brief, with and without the base.

    run_pilot.py run <tasks-dir> <out-dir> --model <model> [--only <task>]
    run_pilot.py answer <out-dir> <task> <variant> <answer-file>
    run_pilot.py blind <out-dir> [--force]
    run_pilot.py score <out-dir> <ranks.json> [--false-applications <cited> <false>]

A task is a folder outside this repository, because the tasks are held out from the wiki:

    task.json   {"mode": "improve", "repo": "<path>", "commit": "<before the edit>",
                 "checks": ["<cmd>"], "setup": ["<cmd>"], "expected_failing": ["<cmd>"]}
    brief.md    the brief, given unchanged to every variant
    journal.md  the real journal, cut before the first code edit; only `overloaded` receives it

`setup` is optional and prepares a fresh export of the commit, for example by installing
dependencies. `checks` must pass before the edit, except those named in `expected_failing`, such as
the reproducer of a debug task. Otherwise a check could never report a new failure, so `run` stops.

`run` executes the agent unattended. Each variant gets its own export with no history, because the
source repository holds the real solution in later commits. Its shell may run the commands in
`checks` and whatever Claude Code treats as read-only. Those commands run the repository's code:
use only repositories you trust.

`ranks.json` maps every task to all its solutions, lower is better, ties allowed:
{"task-1": {"solution-1": 1, "solution-2": 2, "solution-3": 2, "solution-4": 3}}. The grader works
from `<out-dir>/blind` alone and never sees `key.json`.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import random
import re
import secrets
import shutil
import signal
import stat
import subprocess
import sys
import tarfile
from pathlib import Path

PLUGIN = Path(__file__).resolve().parent.parent
AGENT = "craftsman"
VARIANTS = {  # name: (has the base, receives the journal)
    "overloaded": (False, True),
    "clean-1": (False, False),
    "clean-2": (False, False),
    "base": (True, False),
}
PILOT_TASKS = 8
WINS_NEEDED = 6
MAX_FALSE_SHARE = 0.10
CHECK_TIMEOUT_SECONDS = 1800
AGENT_TIMEOUT_SECONDS = 3600


def strip_base(agent_text: str) -> str:
    """Remove the agent's only section about the base."""
    stripped, count = re.subn(r"^## The base\n.*?(?=^## )", "", agent_text, flags=re.M | re.S)
    if count != 1:
        raise ValueError("expected exactly one '## The base' section")
    return stripped


def agent_definition(root: Path | None) -> dict:
    """Turn the real agent file into an inline definition, for a session with no plugins.

    With `root` the agent reads the base there. Without it the section about the base goes.
    """
    text = (PLUGIN / "agents" / "craftsman.md").read_text(encoding="utf-8")
    _, front, body = text.split("---\n", 2)
    tools = re.search(r"^tools: (.+)$", front, re.M).group(1)
    description = re.search(r"^description: >-\n((?:  .+\n)+)", front, re.M).group(1)
    return {
        AGENT: {
            "description": " ".join(description.split()),
            "tools": [tool.strip() for tool in tools.split(",")],
            "prompt": body.replace("${CLAUDE_PLUGIN_ROOT}", root.as_posix()) if root else strip_base(body),
        }
    }


def remove_tree(path: Path) -> None:
    """Delete a folder, including the read-only objects of a git repository on Windows."""

    def clear_and_retry(function, target, _error) -> None:
        os.chmod(target, stat.S_IWRITE)
        function(target)

    if path.exists():
        shutil.rmtree(path, onexc=clear_and_retry)


def copy_base(dest: Path) -> Path:
    """Copy what an install ships, for one run: no hook guards it here, and `raw/` never ships."""
    remove_tree(dest)
    (dest / "knowledge").mkdir(parents=True)
    shutil.copytree(PLUGIN / "knowledge" / "wiki", dest / "knowledge" / "wiki")
    return dest


def claude_args(agents: Path, model: str, checks: list[str], base: Path | None = None) -> list[str]:
    """Build the same session for every variant.

    User settings and MCP servers stay out, because they inject context and a clean variant has to
    be clean. Those settings are also what loads `--plugin-dir`, so the agent is passed inline.
    """
    args = [
        "--agents", str(agents),
        "--agent", AGENT,
        "--model", model,
        "--setting-sources", "project",
        "--strict-mcp-config",
        "--permission-mode", "acceptEdits",
    ]
    if base:
        args += ["--add-dir", str(base)]
    if checks:
        args += ["--allowedTools", *[f"Bash({command})" for command in checks]]
    return args


def kill_tree(process: subprocess.Popen) -> None:
    """Stop a process and its children: a timeout on the shell alone leaves the check running."""
    if os.name == "nt":
        subprocess.run(
            ["taskkill", "/T", "/F", "/PID", str(process.pid)],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
    else:
        os.killpg(process.pid, signal.SIGKILL)


def run_bounded(
    command: list[str],
    cwd: Path,
    timeout: int,
    stdin: str | None = None,
    env: dict[str, str] | None = None,
) -> tuple[int, str, str]:
    """Run a command to completion or to its timeout. A timeout returns the exit code -1."""
    process = subprocess.Popen(
        command, cwd=cwd, env=env, text=True, encoding="utf-8", errors="replace",
        stdin=subprocess.PIPE if stdin is not None else subprocess.DEVNULL,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=os.name != "nt",
    )
    try:
        out, err = process.communicate(stdin, timeout=timeout)
    except subprocess.TimeoutExpired:
        kill_tree(process)
        out, err = process.communicate()
        return -1, out, err
    return process.returncode, out, err


def find_result(stream: str) -> dict:
    # Split on newlines only: splitlines() also breaks on separators allowed inside JSON strings.
    result: dict = {}
    for line in stream.split("\n"):
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(event, dict) and event.get("type") == "result":
            result = event
    return result


def claude(args: list[str], prompt: str, cwd: Path) -> str:
    """Run one session. A failed run raises, so it is never recorded as a solution."""
    exe = shutil.which("claude")
    if exe is None:
        sys.exit("claude is not on PATH")
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
    env["CLAUDE_CODE_DISABLE_AUTO_MEMORY"] = "1"  # Project memory would differ from a clean context.
    code, out, err = run_bounded(
        [exe, "-p", "--output-format", "stream-json", "--verbose", *args],
        cwd, AGENT_TIMEOUT_SECONDS, stdin=prompt, env=env,
    )
    result = find_result(out)
    if code != 0 or not result or result.get("is_error"):
        raise RuntimeError(f"run failed, exit {code}: {result.get('result') or err[-500:]}")
    return out


def parse_stream(stream: str) -> dict:
    """Pull the report, the cost and the opened pages out of a stream-json transcript."""
    pages: list[str] = []
    model = None
    for line in stream.split("\n"):
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "system" and event.get("subtype") == "init":
            model = event.get("model")
        if event.get("type") != "assistant":
            continue
        for block in event["message"].get("content", []):
            if block.get("type") == "tool_use" and block.get("name") == "Read":
                path = str(block["input"].get("file_path", "")).replace("\\", "/")
                page = re.search(r"/knowledge/(wiki/.+\.md)$", path)
                if page and page.group(1) not in pages:
                    pages.append(page.group(1))
    result = find_result(stream)
    usage = result.get("usage", {})
    tokens = sum(v for k, v in usage.items() if k.endswith("_tokens") and isinstance(v, int))
    report = result.get("result", "")
    found = re.search(r"NEEDS_INFO|BLOCKED|DONE", report)
    return {
        "session": result.get("session_id"),
        "model": model,
        "report": report,
        "status": found.group() if found else "UNKNOWN",
        "tokens": tokens,
        "cost_usd": result.get("total_cost_usd", 0),
        "pages": pages,
    }


def bash() -> str:
    """Find the shell the agent uses. On Windows `bash` on PATH is often the WSL launcher."""
    git_exe = shutil.which("git")
    if git_exe:
        bundled = Path(git_exe).resolve().parents[1] / "bin" / "bash.exe"
        if bundled.exists():
            return str(bundled)
    return shutil.which("bash") or "bash"


def run_checks(commands: list[str], cwd: Path) -> tuple[dict[str, int], str]:
    codes = {}
    log = []
    for command in commands:
        code, out, err = run_bounded([bash(), "-c", command], cwd, CHECK_TIMEOUT_SECONDS)
        codes[command] = code
        log.append(f"$ {command}\n[exit {code}]\n{out}\n{err}\n")
    return codes, "\n".join(log)


def checks_on_copy(commands: list[str], work: Path) -> tuple[dict[str, int], str]:
    """Check a copy, so that what the checks write never reaches a patch or a resumed agent."""
    copy = work.with_name(f"{work.name}-checks")
    remove_tree(copy)
    shutil.copytree(work, copy, symlinks=True)
    try:
        return run_checks(commands, copy)
    finally:
        remove_tree(copy)


def git(repo: Path | str, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), *args], check=True, capture_output=True, text=True,
        encoding="utf-8", errors="replace",
    ).stdout


def snapshot(task: dict, dest: Path) -> None:
    """Export the commit with no history, because later commits hold the real solution."""
    remove_tree(dest)
    dest.mkdir(parents=True)
    archive = subprocess.run(
        ["git", "-C", str(task["repo"]), "archive", task["commit"]],
        check=True, capture_output=True,
    ).stdout
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        tar.extractall(dest, filter="data")
    for command in task.get("setup", []):
        code, out, err = run_bounded([bash(), "-c", command], dest, CHECK_TIMEOUT_SECONDS)
        if code:
            raise RuntimeError(f"setup failed, exit {code}: {command}\n{out[-500:]}\n{err[-500:]}")
    git(dest, "init", "-q")
    git(dest, "config", "core.autocrlf", "false")
    git(dest, "add", "-A")
    git(
        dest, "-c", "user.name=pilot", "-c", "user.email=pilot@example.invalid",
        "-c", "commit.gpgsign=false", "commit", "-q", "--allow-empty", "-m", "snapshot",
    )


def write_text(path: Path, text: str) -> None:
    # Keep line feeds: on Windows the default newline makes a patch unappliable.
    path.write_text(text, encoding="utf-8", newline="\n")


def collect(run_dir: Path, work: Path, task: dict, stream: str, previous: dict | None = None) -> dict:
    """Write a finished run's artefacts. A resumed run adds its tokens to the first part's."""
    parsed = parse_stream(stream)
    git(work, "add", "-AN")
    # Against HEAD: against the index, `add -AN` hides deleted files and half of every rename.
    diff = git(work, "diff", "HEAD", "--ignore-space-at-eol")
    checks, log = checks_on_copy(task["checks"], work)
    write_text(run_dir / "diff.patch", diff)
    write_text(run_dir / "checks.log", log)
    write_text(run_dir / "report.md", parsed["report"])
    with (run_dir / "stream.jsonl").open("a", encoding="utf-8") as transcript:
        transcript.write(stream)
    run = {k: v for k, v in parsed.items() if k != "report"}
    if previous:  # total_cost_usd is already cumulative across a resume; usage is not.
        run["tokens"] += previous["tokens"]
        run["pages"] = previous["pages"] + [p for p in run["pages"] if p not in previous["pages"]]
        run["args"] = previous["args"]
        run["worktree"] = previous["worktree"]
    run["checks"] = checks
    return run


def inputs_manifest(tasks: dict[str, dict], model: str) -> dict:
    """Pin what every run of the pilot must share, so a continued run cannot drift."""
    digest = hashlib.sha256()
    for path in [PLUGIN / "agents" / "craftsman.md", *sorted((PLUGIN / "knowledge" / "wiki").rglob("*.md"))]:
        digest.update(path.read_bytes())
    commits = {name: git(t["repo"], "rev-parse", t["commit"]).strip() for name, t in tasks.items()}
    return {"model": model, "agent_and_wiki": digest.hexdigest(), "commits": commits}


def check_before_edit(task: dict, codes: dict[str, int]) -> list[str]:
    """Name the checks that cannot report a new failure, because they start in the wrong state."""
    expected = task.get("expected_failing", [])
    problems = []
    for command, code in codes.items():
        if code and command not in expected:
            problems.append(f"fails before the edit: {command}")
        if not code and command in expected:
            problems.append(f"passes before the edit, but is expected to fail: {command}")
    return problems


def command_run(args: argparse.Namespace) -> None:
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    folders = sorted(p for p in args.tasks.resolve().iterdir() if (p / "task.json").exists())
    tasks = {p.name: json.loads((p / "task.json").read_text(encoding="utf-8")) for p in folders}

    manifest = inputs_manifest(tasks, args.model)
    manifest_path = out / "manifest.json"
    if manifest_path.exists():
        if json.loads(manifest_path.read_text(encoding="utf-8")) != manifest:
            sys.exit("the model, the agent, the wiki or a commit changed since this pilot started")
    manifest_path.write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    (out / "tasks.json").write_text(json.dumps(tasks, indent=1), encoding="utf-8")

    base_copy = out / "base-copy"
    base_agent = out / "agent-base.json"
    control_agent = out / "agent-control.json"
    base_agent.write_text(json.dumps(agent_definition(base_copy)), encoding="utf-8")
    control_agent.write_text(json.dumps(agent_definition(None)), encoding="utf-8")

    for folder in folders:
        task = tasks[folder.name]
        if args.only and folder.name != args.only:
            continue
        before = out / "runs" / folder.name / "before-checks.json"
        before.parent.mkdir(parents=True, exist_ok=True)
        if not before.exists():
            work = out / "work" / folder.name / "before"
            snapshot(task, work)
            codes, log = run_checks(task["checks"], work)
            write_text(before.with_suffix(".log"), log)
            problems = check_before_edit(task, codes)
            if problems:
                sys.exit(f"{folder.name}: " + "; ".join(problems))
            before.write_text(json.dumps(codes), encoding="utf-8")
        brief = (folder / "brief.md").read_text(encoding="utf-8")
        for variant, (has_base, has_journal) in VARIANTS.items():
            run_dir = out / "runs" / folder.name / variant
            if (run_dir / "run.json").exists():
                continue
            run_dir.mkdir(parents=True, exist_ok=True)
            # An opaque name: the working directory reaches the session.
            work = out / "work" / folder.name / secrets.token_hex(4)
            snapshot(task, work)
            prompt = brief
            if has_journal:
                journal = (folder / "journal.md").read_text(encoding="utf-8")
                prompt = f"{journal}\n\n---\n\n{brief}"
            print(f"{folder.name} / {variant}", flush=True)
            if has_base:
                copy_base(base_copy)
                agent_args = claude_args(base_agent, args.model, task["checks"], base_copy)
            else:
                agent_args = claude_args(control_agent, args.model, task["checks"])
            stream = claude(agent_args, prompt, work)
            run = collect(run_dir, work, task, stream)
            run["args"] = agent_args
            run["worktree"] = str(work)
            (run_dir / "run.json").write_text(json.dumps(run, indent=1), encoding="utf-8")
            print(f"  {run['status']}, {run['tokens']} tokens", flush=True)


def command_answer(args: argparse.Namespace) -> None:
    out = args.out.resolve()
    task = json.loads((out / "tasks.json").read_text(encoding="utf-8"))[args.task]
    run_dir = out / "runs" / args.task / args.variant
    run = json.loads((run_dir / "run.json").read_text(encoding="utf-8"))
    answer = args.answer_file.read_text(encoding="utf-8")
    work = Path(run["worktree"])
    stream = claude([*run["args"], "--resume", run["session"]], answer, work)
    updated = collect(run_dir, work, task, stream, previous=run)
    (run_dir / "run.json").write_text(json.dumps(updated, indent=1), encoding="utf-8")
    print(updated["status"])


def assign_blind(tasks: list[str], rng: random.Random) -> dict[str, dict[str, str]]:
    key = {}
    for task in tasks:
        variants = list(VARIANTS)
        rng.shuffle(variants)
        key[task] = {f"solution-{i}": v for i, v in enumerate(variants, 1)}
    return key


def reveals_base(diff: str, slugs: set[str]) -> bool:
    """Look for the base in what a solution added. Single-word slugs are ordinary code words."""
    added = "\n".join(line for line in diff.splitlines() if line.startswith("+"))
    if re.search(r"wiki[/\\]|knowledge[/\\]|model opinion", added):
        return True
    return any(slug in added for slug in slugs if "-" in slug)


def unfinished_runs(statuses: dict[str, str]) -> list[str]:
    """Runs that have no solution to grade. BLOCKED is a result of the run; the rest are not."""
    return [run for run, status in statuses.items() if status not in ("DONE", "BLOCKED")]


def command_blind(args: argparse.Namespace) -> None:
    out = args.out.resolve()
    key_path = out / "key.json"
    if key_path.exists() and not args.force:
        sys.exit("key.json exists. A new draw invalidates ranks made from the old one: use --force")
    tasks = sorted(json.loads((out / "tasks.json").read_text(encoding="utf-8")))
    statuses = {}
    for task in tasks:
        for variant in VARIANTS:
            path = out / "runs" / task / variant / "run.json"
            run = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
            statuses[f"{task}/{variant}"] = run.get("status", "MISSING")
    unfinished = unfinished_runs(statuses)
    if unfinished:
        sys.exit("waiting for: " + ", ".join(f"{r} ({statuses[r]})" for r in unfinished))
    for run, status in statuses.items():
        if status != "DONE":
            print(f"{run}: {status}")
    slugs = {p.stem for p in (PLUGIN / "knowledge" / "wiki").rglob("*.md")}
    key = assign_blind(tasks, random.SystemRandom())
    for task, solutions in key.items():
        folder = out / "blind" / task
        remove_tree(folder)
        folder.mkdir(parents=True)
        for solution, variant in solutions.items():
            diff = (out / "runs" / task / variant / "diff.patch").read_text(encoding="utf-8")
            if reveals_base(diff, slugs):
                print(f"WARNING: a solution of {task} names the base in code. Check it before grading.")
            write_text(folder / f"{solution}.patch", diff)
    key_path.write_text(json.dumps(key, indent=1), encoding="utf-8")


def rank_problems(ranks: dict, key: dict) -> list[str]:
    """A partial ranking would lower the bar: it must cover every solution of every task."""
    problems = []
    for task in sorted(set(key) | set(ranks)):
        if set(ranks.get(task, {})) != set(key.get(task, {})):
            problems.append(task)
    return problems


def unblind(ranks: dict, key: dict) -> dict[str, dict[str, int]]:
    return {t: {key[t][s]: rank for s, rank in sol.items()} for t, sol in ranks.items()}


def wins(by_variant: dict[str, dict[str, int]], winner: str, loser: str) -> list[str]:
    """Tasks where `winner` ranks strictly better. A tie counts for neither."""
    return [t for t, ranks in by_variant.items() if ranks[winner] < ranks[loser]]


def verdict(
    by_variant: dict[str, dict[str, int]],
    new_failures: list[str],
    cited: int | None,
    false: int | None,
) -> list[tuple[str, bool | None]]:
    """The success condition, fixed in the design doc before any run."""
    complete = len(by_variant) == PILOT_TASKS
    gain = wins(by_variant, "base", "clean-1")
    noise = wins(by_variant, "clean-2", "clean-1")
    false_ok = None if not cited else (false or 0) / cited <= MAX_FALSE_SHARE
    return [
        (f"tasks ranked: {len(by_variant)} of {PILOT_TASKS}", complete or None),
        (
            f"base beats clean-1 in {len(gain)} tasks, needs {WINS_NEEDED}",
            len(gain) >= WINS_NEEDED if complete else None,
        ),
        (
            f"clean-2 beats clean-1 in {len(noise)}, must be fewer than {len(gain)}",
            len(noise) < len(gain) if complete else None,
        ),
        (f"new check failures with the base: {new_failures or 'none'}", not new_failures),
        (f"false applications: {false} of {cited}", false_ok),
    ]


def new_failures(task: dict, checks: dict[str, int]) -> list[str]:
    """Checks that passed before the edit and fail after it."""
    expected = task.get("expected_failing", [])
    return [command for command, code in checks.items() if code and command not in expected]


def command_score(args: argparse.Namespace) -> None:
    out = args.out.resolve()
    key = json.loads((out / "key.json").read_text(encoding="utf-8"))
    tasks = json.loads((out / "tasks.json").read_text(encoding="utf-8"))
    ranks = json.loads(args.ranks.read_text(encoding="utf-8"))
    incomplete = rank_problems(ranks, key)
    if incomplete:
        sys.exit("ranks do not cover every solution of: " + ", ".join(incomplete))
    by_variant = unblind(ranks, key)

    failures = []
    for task in by_variant:
        run = json.loads((out / "runs" / task / "base" / "run.json").read_text(encoding="utf-8"))
        failures += [f"{task}: {command}" for command in new_failures(tasks[task], run["checks"])]

    cited, false = args.false_applications or (None, None)
    for line, passed in verdict(by_variant, failures, cited, false):
        mark = {True: "PASS", False: "FAIL", None: "NOT_RUN"}[passed]
        print(f"{mark}  {line}")

    for winner in ("clean-1", "base"):
        count = len(wins(by_variant, winner, "overloaded"))
        print(f"{winner} beats overloaded in {count}, threshold {WINS_NEEDED}")

    print("\nby mode, base against clean-1:")
    for mode in sorted({tasks[t]["mode"] for t in by_variant}):
        group = {t: r for t, r in by_variant.items() if tasks[t]["mode"] == mode}
        print(f"  {mode}: {len(wins(group, 'base', 'clean-1'))} of {len(group)}")

    print("\ntokens and pages:")
    for variant in VARIANTS:
        runs = [
            json.loads((out / "runs" / t / variant / "run.json").read_text(encoding="utf-8"))
            for t in by_variant
        ]
        tokens = sum(r["tokens"] for r in runs)
        cost = sum(r["cost_usd"] for r in runs)
        pages = sum(len(r["pages"]) for r in runs)
        print(f"  {variant}: {tokens} tokens, ${cost:.2f}, {pages} pages opened")


def main() -> None:
    parser = argparse.ArgumentParser(description=(__doc__ or "").splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run")
    run.add_argument("tasks", type=Path)
    run.add_argument("out", type=Path)
    run.add_argument("--model", required=True)
    run.add_argument("--only")
    run.set_defaults(handler=command_run)
    answer = sub.add_parser("answer")
    answer.add_argument("out", type=Path)
    answer.add_argument("task")
    answer.add_argument("variant", choices=list(VARIANTS))
    answer.add_argument("answer_file", type=Path)
    answer.set_defaults(handler=command_answer)
    blind = sub.add_parser("blind")
    blind.add_argument("out", type=Path)
    blind.add_argument("--force", action="store_true")
    blind.set_defaults(handler=command_blind)
    score = sub.add_parser("score")
    score.add_argument("out", type=Path)
    score.add_argument("ranks", type=Path)
    score.add_argument("--false-applications", nargs=2, type=int, metavar=("CITED", "FALSE"))
    score.set_defaults(handler=command_score)
    args = parser.parse_args()
    args.handler(args)


if __name__ == "__main__":
    main()
