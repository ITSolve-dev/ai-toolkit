#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
"""Scaffold a new llm-wiki from the plugin's asset templates.

Creates the layout described in references/directory-layout.md:

    <target>/
    ├── SCHEMA.md          (from assets/SCHEMA.md.template)
    ├── log.md             (from assets/log.md.template) — operational record, at the root
    ├── .gitignore         (from assets/gitignore.template)
    ├── raw/
    └── wiki/
        ├── index.md       (from assets/index.md.template)
        ├── overview.md    entry point: what this wiki covers and how it is organized
        └── synthesis.md   the evolving thesis — what it all means

Page groups are not scaffolded — they emerge from the domain as the keeper ingests sources.

Idempotent-ish: never overwrites an existing file; refuses if SCHEMA.md already exists
(the directory is already a wiki root). Refuses a home or drive root as target.

Usage:
    uv run --no-project init_wiki.py <target-dir>

Dependencies: standard library only.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path


def plugin_root() -> Path:
    """Locate the plugin root (…/llm-wiki), preferring $CLAUDE_PLUGIN_ROOT."""
    env = os.environ.get("CLAUDE_PLUGIN_ROOT")
    if env:
        return Path(env)
    # …/skills/wiki-init/scripts/init_wiki.py -> parents[3] == plugin root
    return Path(__file__).resolve().parents[3]


def assets_dir() -> Path:
    return plugin_root() / "assets"


def is_forbidden_root(target: Path) -> bool:
    """True if target is a home directory or a filesystem/drive root.

    Mirrors the mandatory-stop rule in references/wiki-resolution.md — never scaffold a
    wiki at a home or drive root.
    """
    target = target.resolve()
    if target.parent == target:  # filesystem / drive root (e.g. C:\ or /)
        return True
    return target == Path.home().resolve()


def write_if_absent(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.write_text(content, encoding="utf-8")
    return True


def stamp(template_name: str, dest: Path) -> bool:
    """Copy assets/<template_name> to dest if dest does not exist."""
    src = assets_dir() / template_name
    if not src.exists():
        raise FileNotFoundError(f"template not found: {src}")
    return write_if_absent(dest, src.read_text(encoding="utf-8"))


def init_wiki(target: Path) -> int:
    resolved = target.resolve()

    if is_forbidden_root(resolved):
        print(f"refusing to initialize a wiki at a home/drive root: {resolved}", file=sys.stderr)
        return 2
    if resolved.exists() and not resolved.is_dir():
        print(f"target exists and is not a directory: {resolved}", file=sys.stderr)
        return 2
    if (resolved / "SCHEMA.md").exists():
        print(f"already a wiki root (SCHEMA.md exists): {resolved}", file=sys.stderr)
        return 3
    target = resolved

    target.mkdir(parents=True, exist_ok=True)
    (target / "raw").mkdir(exist_ok=True)
    # No page-group subdirectories are pre-created: groups are not predefined, they emerge
    # from the domain as the keeper ingests sources (each group is a subdirectory of wiki/).
    (target / "wiki").mkdir(exist_ok=True)

    # Everything EXCEPT the SCHEMA.md marker is written first. SCHEMA.md is what "already a
    # wiki" keys on, so writing it last means a failure partway through leaves no marker and the
    # scaffold can simply be re-run to completion rather than being locked out forever.
    created = []
    if stamp("gitignore.template", target / ".gitignore"):
        created.append(".gitignore")
    if stamp("index.md.template", target / "wiki" / "index.md"):
        created.append("wiki/index.md")
    if stamp("log.md.template", target / "log.md"):
        created.append("log.md")
    if write_if_absent(
        target / "wiki" / "overview.md",
        "# Overview\n\n<Entry point: what this wiki covers and how it is organized. A map.>\n",
    ):
        created.append("wiki/overview.md")
    if write_if_absent(
        target / "wiki" / "synthesis.md",
        "# Synthesis\n\n"
        "<The evolving thesis: what it all means taken together. Each new source strengthens\n"
        "or challenges this. Delete this file if the wiki is pure reference with no thesis.>\n",
    ):
        created.append("wiki/synthesis.md")
    if stamp("SCHEMA.md.template", target / "SCHEMA.md"):  # marker LAST — see note above
        created.append("SCHEMA.md")

    print(f"initialized wiki at {target}")
    for name in created:
        print(f"  + {name}")
    print(
        "\nNext: interview the human, then fill SCHEMA.md from their answers — domain and"
        "\npurpose, who it serves, what is in scope and what to deliberately drop, what each"
        "\nsource should yield, the key sources, and how they would split this domain into"
        "\ntopics. Do not leave placeholders, and do not guess what you can simply ask."
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Scaffold a new llm-wiki.")
    parser.add_argument("target", help="directory to initialize as a wiki root")
    args = parser.parse_args(argv)
    # A bare drive letter ("C:") is drive-RELATIVE on Windows — Path resolves it to the current
    # directory, not the drive root, so a user meaning "the drive" would scaffold a wiki wherever
    # they happen to be. Refuse it; require an explicit path.
    if re.fullmatch(r"[A-Za-z]:", args.target.strip()):
        print(f"ambiguous drive-relative target {args.target!r}; pass an explicit directory path", file=sys.stderr)
        return 2
    return init_wiki(Path(args.target))


if __name__ == "__main__":
    raise SystemExit(main())
