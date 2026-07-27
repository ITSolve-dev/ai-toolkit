#!/usr/bin/env python3
"""Regenerate <wiki-root>/.manifest.json from raw/ source frontmatter.

The manifest is a DERIVED index — like wiki/index.md — so it cannot drift from the sources it
describes. Each `raw/<slug>.md` already carries its own provenance in frontmatter (title,
source_kind, origin, sha256, retrieved), written by the read-* adapter per the adapter
contract. This script denormalizes that into one JSON object keyed by raw slug, which:

  - lets `wiki-lint` detect a changed source (compare a fresh adapter run's sha256 to the
    stored one) and trace any page back to its origin, and
  - lets `wiki-scout` dedup candidate sources against what the wiki already holds.

Because it is regenerated (the Stop hook runs it each turn, and it is gitignored), there is
nothing to hand-edit and nothing to keep in sync.

Usage:
    build_manifest.py <wiki-root>
    build_manifest.py --auto        # resolve from cwd; exit 0 silently if not in a wiki

Dependencies: standard library only.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from _frontmatter import atomic_write, find_wiki_root_auto, parse_frontmatter, read_text, validate_wiki_root

# The provenance fields the adapter contract guarantees on every raw/ source file.
FIELDS = ("title", "source_kind", "origin", "sha256", "retrieved")


def build_manifest(wiki_root: Path) -> dict[str, dict[str, str]]:
    """Map each raw/<slug>.md to its provenance fields, keyed by slug."""
    raw_dir = wiki_root / "raw"
    entries: dict[str, dict[str, str]] = {}
    if raw_dir.exists():
        for src in sorted(raw_dir.glob("*.md")):
            fm = parse_frontmatter(read_text(src))
            entries[src.stem] = {k: fm.get(k, "") for k in FIELDS}
    return entries


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Regenerate .manifest.json from raw/ frontmatter.")
    parser.add_argument("wiki_root", nargs="?", help="wiki root (dir containing SCHEMA.md)")
    parser.add_argument("--auto", action="store_true", help="resolve wiki root from cwd; no-op if none")
    args = parser.parse_args(argv)

    if args.auto:
        root = find_wiki_root_auto(Path.cwd())
        if root is None:
            return 0  # not in a wiki — silent no-op (used by the Stop hook)
    elif args.wiki_root:
        root = Path(args.wiki_root).resolve()
        problem = validate_wiki_root(root)
        if problem:
            print(problem, file=sys.stderr)
            return 2
    else:
        parser.error("provide a wiki root or --auto")

    manifest = build_manifest(root)
    atomic_write(root / ".manifest.json", json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    if not args.auto:  # the Stop hook runs every turn and stays quiet; a manual run reports
        print(f"wrote .manifest.json - {len(manifest)} source(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
