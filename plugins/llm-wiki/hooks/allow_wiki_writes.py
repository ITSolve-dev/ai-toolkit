#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
"""PreToolUse hook: approve writes that land on a wiki's own files.

Maintaining a wiki means writing many files in one operation — a single ingest touches the
pages, the index, the log and the manifest. This hook approves exactly those writes so the
work runs uninterrupted, and stays silent about everything else.

Scope is deliberately narrow. A wiki root is often the project root (`wiki-init` defaults
there), so "inside the wiki root" would cover the whole project. Only the paths the keeper
actually owns are approved:

    <wiki-root>/wiki/**      curated pages, the generated index, overview, synthesis
    <wiki-root>/raw/**       normalized sources
    <wiki-root>/SCHEMA.md    the charter
    <wiki-root>/log.md       the operation log
    <wiki-root>/.manifest.json, mkdocs.yml, .gitignore

Anything else — including any path outside a wiki — gets no decision, so the normal
permission flow applies. A user's deny rules still take precedence over an approval, and the
hook is visible in `/hooks` and disabled along with the plugin.

Reads the hook payload on stdin, writes a decision on stdout. Fails open: on any unexpected
input or error it stays silent rather than blocking the user.

Dependencies: standard library only.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

OWNED_DIRS = ("wiki", "raw")
OWNED_FILES = ("SCHEMA.md", "log.md", ".manifest.json", "mkdocs.yml", ".gitignore")


def is_forbidden_root(path: Path) -> bool:
    """True if `path` is the user's home directory or a filesystem/drive root."""
    path = path.resolve()
    if path.parent == path:  # filesystem / drive root
        return True
    return path == Path.home().resolve()


def find_wiki_root(start: Path) -> Path | None:
    """Walk up to the first dir holding SCHEMA.md; never past — or onto — home / drive root.

    Mirrors references/wiki-resolution.md, including the mandatory stop. The boundary is tested
    BEFORE the marker, so a stray SCHEMA.md in a home or drive root cannot turn it into a wiki
    (which would otherwise auto-approve writes across the user's whole home directory).
    """
    cur = start.resolve()
    while True:
        if is_forbidden_root(cur):
            return None
        if (cur / "SCHEMA.md").exists():
            return cur
        cur = cur.parent


def owned_by_wiki(path: Path) -> Path | None:
    """Return the wiki root that owns `path`, or None."""
    path = path.resolve()
    # The file may not exist yet (Write creates it), so resolve from its directory.
    root = find_wiki_root(path.parent)
    if root is None:
        return None

    try:
        rel = path.relative_to(root)
    except ValueError:
        return None

    if rel.parts and rel.parts[0] in OWNED_DIRS:
        return root
    if rel.as_posix() in OWNED_FILES:
        return root
    return None


def main() -> int:
    # One guard around the whole read+resolve: the payload shape is not ours to trust, so any
    # unexpected type (a list, a string, a null tool_input) must leave the hook silent rather
    # than raise — a PreToolUse hook that exits non-zero surfaces an error on every tool call.
    try:
        payload = json.load(sys.stdin)
        raw_path = (payload.get("tool_input") or {}).get("file_path")
        if not raw_path or not isinstance(raw_path, str):
            return 0
        root = owned_by_wiki(Path(raw_path))
    except Exception:
        return 0

    if root is None:
        return 0

    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "allow",
                "permissionDecisionReason": f"llm-wiki maintains this file (wiki root: {root}).",
            }
        },
        sys.stdout,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
