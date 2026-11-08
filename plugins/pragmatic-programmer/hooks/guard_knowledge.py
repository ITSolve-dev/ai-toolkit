#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
"""PreToolUse hook: let agents read the bundled base, and keep them from changing it.

The base sits in the plugin's install directory, outside the project. A prompt there stops a
background agent, and plugin agents cannot set a permission mode, so reads are approved here.
`llm-wiki` approves writes to any wiki's own files, and the expert holds `Write`, so writes are
denied here.

    Read, Grep, Glob inside <plugin-root>/knowledge    allow
    Write, Edit, NotebookEdit under <plugin-root>      deny
    Bash, PowerShell naming <plugin-root>              deny
    Bash, PowerShell run from under <plugin-root>      deny

The `if` filters in hooks.json keep Write and Edit outside a `knowledge` folder from reaching this
script, so the guarantee covers the base rather than the whole plugin root.

Any other call gets no decision, so the normal permission flow applies. The user's deny rules still
take precedence over an approval.

The shell check matches text. It stops an agent working normally from running a command on the
plugin, and it does not stop a command that builds the path at run time: only the tool list and the
operating system can promise that. A command that merely mentions the installed path is denied too,
which costs little because nothing outside this hook needs that path in a shell.

Reads the hook payload on stdin, writes a decision on stdout. Fails open: on unexpected input it
stays silent rather than blocking the user.

Dependencies: standard library only.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

READ_TOOLS = {"Read", "Grep", "Glob"}
WRITE_TOOLS = {"Write", "Edit", "NotebookEdit"}
SHELL_TOOLS = {"Bash", "PowerShell"}
PATH_KEYS = ("file_path", "notebook_path", "path")
GLOB_CHARS = re.compile(r"[*?\[{]")
DRIVE_RE = re.compile(r"^[A-Za-z]:[\\/]")


def resolve(value: str, cwd: str) -> Path:
    path = Path(value)
    if not path.is_absolute() and cwd:
        path = Path(cwd) / path
    return path.resolve()


def target_path(tool_input: dict, cwd: str) -> Path | None:
    """The path a file tool acts on, resolved against the session's working directory."""
    for key in PATH_KEYS:
        value = tool_input.get(key)
        if value and isinstance(value, str):
            return resolve(value, cwd)
    return None


def is_absolute_pattern(pattern: str) -> bool:
    # Path("/x").is_absolute() is False on Windows, so test the spelling, not the platform's view.
    return pattern.startswith(("/", "\\", "~")) or bool(DRIVE_RE.match(pattern))


def glob_target(tool_input: dict, cwd: str) -> Path | None:
    """Where a Glob can look, or None if that cannot be told from the call."""
    pattern = tool_input.get("pattern")
    if not isinstance(pattern, str) or ".." in re.split(r"[\\/]", pattern):
        return None
    if is_absolute_pattern(pattern):
        if tool_input.get("path"):
            return None
        fixed = GLOB_CHARS.split(pattern, maxsplit=1)[0]
        return resolve(fixed, cwd) if fixed.strip("/\\") else None
    return target_path(tool_input, cwd)


def is_inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def normalize(text: str) -> str:
    """One spelling of a path for comparison: forward slashes, no quotes, no `.` or `..` steps."""
    text = text.replace("\\ ", " ").replace('"', "").replace("'", "").replace("\\", "/")
    text = re.sub(r"/+", "/", text)
    text = re.sub(r"(?:/\.)+(?=/|\s|$)", "", text)
    previous = None
    while previous != text:
        previous = text
        text = re.sub(r"/[^/\s]+/\.\.(?=/|\s|$)", "", text)
    return text.lower()


def root_spellings(plugin_root: Path, raw_root: str) -> set[str]:
    """Every spelling of the plugin root a shell command is likely to use."""
    spellings = set()
    for path in {plugin_root, Path(raw_root)}:
        posix = path.as_posix()
        spellings.add(posix)
        if path.drive:
            # Git Bash spells C:/x as /c/x.
            spellings.add(f"/{path.drive[0]}{posix[len(path.drive):]}")
        try:
            relative = path.relative_to(Path.home()).as_posix()
        except ValueError:
            continue
        spellings.update({f"~/{relative}", f"$HOME/{relative}", f"${{HOME}}/{relative}"})
    return {normalize(spelling) for spelling in spellings}


def names_plugin(command: str, spellings: set[str]) -> bool:
    normalized = normalize(command)
    # The boundary keeps a sibling such as `pragmatic-programmer/0.1.0-old` out of the match.
    return any(
        re.search(re.escape(spelling) + r"(?![\w.-])", normalized) for spelling in spellings
    )


def decide(payload: dict, plugin_root: Path, raw_root: str) -> tuple[str, str] | None:
    """Return (decision, reason) for a tool call, or None to leave it to the normal flow."""
    tool = payload.get("tool_name")
    tool_input = payload.get("tool_input") or {}
    cwd = payload.get("cwd") or ""

    if tool in SHELL_TOOLS:
        command = tool_input.get("command")
        if not isinstance(command, str):
            return None
        inside = bool(cwd) and is_inside(Path(cwd).resolve(), plugin_root)
        if inside or names_plugin(command, root_spellings(plugin_root, raw_root)):
            return "deny", "The installed plugin is read through Read, Grep and Glob, not a shell."
        return None

    if tool in WRITE_TOOLS:
        path = target_path(tool_input, cwd)
        if path is not None and is_inside(path, plugin_root):
            return "deny", "The installed plugin is read-only: a change here reaches every project."
        return None

    if tool in READ_TOOLS:
        path = glob_target(tool_input, cwd) if tool == "Glob" else target_path(tool_input, cwd)
        if path is not None and is_inside(path, plugin_root / "knowledge"):
            return "allow", "pragmatic-programmer reads its bundled knowledge base."
    return None


def main() -> int:
    # One guard around the whole read and decision: the payload shape is not ours to trust, and a
    # PreToolUse hook that raises surfaces an error on every tool call. Read bytes, because stdin
    # text uses the system code page on Windows and silently garbles a Cyrillic user name.
    try:
        root = os.environ.get("CLAUDE_PLUGIN_ROOT")
        if not root:
            return 0
        verdict = decide(json.load(sys.stdin.buffer), Path(root).resolve(), root)
    except Exception:
        return 0

    if verdict is None:
        return 0

    decision, reason = verdict
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": decision,
                "permissionDecisionReason": reason,
            }
        },
        sys.stdout,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
