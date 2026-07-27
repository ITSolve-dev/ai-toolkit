#!/usr/bin/env python3
"""Deterministic (mechanical) lint for an llm-wiki.

Tier 1 of the two-tier lint (see lint-workflow.md): catches only the things a machine can
decide for certain — missing frontmatter, category/folder mismatch, duplicate slugs, broken
[[wikilinks]], misfiled pages, and orphan pages. The semantic tier (contradictions, stale
claims, gaps) is the LLM's job in the wiki-lint skill.

Pages live one subdirectory per group under wiki/ (the set of groups is not fixed — any
subdirectory is a group). A page's `category` frontmatter must equal its folder name, and its
slug (filename stem) is unique across every group. Non-blocking: always exits 0 and reports.

Usage:
    lint_mechanical.py <wiki-root>
    lint_mechanical.py --auto            # resolve from cwd; no-op if not in a wiki
    lint_mechanical.py --auto --quiet    # print nothing when clean (hook mode)

Dependencies: standard library only.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from _frontmatter import find_wiki_root_auto, parse_frontmatter, read_text, validate_wiki_root

REQUIRED_FIELDS = ["title", "category", "summary", "tags", "sources", "created", "updated"]

# A wikilink is [[target]], [[target|alias]] or [[target#anchor]]. Capture the inner text
# broadly (anything but brackets/newline) and resolve the bare target afterwards, so aliased,
# anchored, or wrongly-cased links are still checked instead of silently skipped.
WIKILINK_RE = re.compile(r"\[\[([^\[\]\n]+?)\]\]")
FENCE_RE = re.compile(r"```.*?```|~~~.*?~~~", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def link_targets(text: str) -> list[str]:
    """Bare link targets in a page body, ignoring anything inside code spans/blocks.

    Code is stripped first so a page that *documents* `[[slug]]` syntax (or shows it in a code
    example) doesn't register phantom links. Each target drops its `|alias` and `#anchor`.
    """
    text = INLINE_CODE_RE.sub(" ", FENCE_RE.sub(" ", text))
    targets = []
    for inner in WIKILINK_RE.findall(text):
        bare = inner.split("|", 1)[0].split("#", 1)[0].strip()
        if bare:
            targets.append(bare)
    return targets


def parse_list(raw: str) -> list[str]:
    """Parse an inline frontmatter list `[a, b]` into its bare items."""
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        raw = raw[1:-1]
    return [item.strip().strip('"').strip("'") for item in raw.split(",") if item.strip()]


def lint(wiki_root: Path) -> list[str]:
    wiki_dir = wiki_root / "wiki"
    findings: list[str] = []

    # Classify every page by its depth under wiki/. index.md is generated and log.md lives above
    # wiki/, so neither is part of the link graph.
    group_pages: list[Path] = []
    root_pages: list[Path] = []
    deep_pages: list[Path] = []
    for p in sorted(wiki_dir.rglob("*.md")) if wiki_dir.exists() else []:
        parts = p.relative_to(wiki_dir).parts
        if len(parts) == 1:
            if p.name != "index.md":
                root_pages.append(p)  # overview, synthesis, ... (non-atomic entry points)
        elif len(parts) == 2:
            group_pages.append(p)
        else:
            deep_pages.append(p)

    def rel(p: Path) -> str:
        return "/".join(p.relative_to(wiki_dir).parts)

    # A slug (filename stem) must be unique across all groups, so [[links]] resolve unambiguously.
    stem_to_paths: dict[str, list[str]] = {}
    for p in group_pages + root_pages + deep_pages:
        stem_to_paths.setdefault(p.stem.casefold(), []).append(rel(p))
    for stem, paths in sorted(stem_to_paths.items()):
        if len(paths) > 1:
            findings.append(f"duplicate slug '{stem}' across: {', '.join(sorted(paths))} (slugs must be unique, case-insensitive)")

    # Resolve links case-insensitively against a lowercased slug set; slugs are lowercase by
    # convention, so a mis-cased link still resolves rather than reading as broken.
    lower_to_stem = {p.stem.lower(): p.stem for p in group_pages + root_pages + deep_pages}
    lower_to_stem.setdefault("index", "index")  # the generated catalog is a valid [[index]] target, never an orphan
    inbound: dict[str, int] = {p.stem: 0 for p in group_pages}  # only atomic group pages get orphan-checked

    def credit(target: str, source_stem: str) -> None:
        stem = lower_to_stem.get(target.lower())
        if stem and stem != source_stem and stem in inbound:
            inbound[stem] += 1

    # A page misfiled below its group is invisible to the index; surface it instead of ignoring it.
    for p in deep_pages:
        findings.append(f"{rel(p)}: page nested below its group (expected wiki/<group>/<slug>.md)")

    for page in group_pages:
        fm = parse_frontmatter(read_text(page))
        for field in REQUIRED_FIELDS:
            if field not in fm:
                findings.append(f"{rel(page)}: missing frontmatter field '{field}'")
        category = fm.get("category", "").strip()
        if category and category != page.parent.name:
            findings.append(f"{rel(page)}: category '{category}' does not match its folder '{page.parent.name}'")
        # A page listed in another page's `sources:` is referenced, so it is not an orphan.
        for src in parse_list(fm.get("sources", "")):
            credit(src, page.stem)

    for page in group_pages + root_pages:
        text = read_text(page)
        for target in link_targets(text):
            if target.lower() == page.stem.lower():
                continue
            if target.lower() not in lower_to_stem:
                findings.append(f"{rel(page)}: broken link [[{target}]] (no such page)")
            else:
                credit(target, page.stem)

    for stem, count in sorted(inbound.items()):
        if count == 0:
            findings.append(f"{stem}: orphan page (no inbound [[links]] or sources reference)")

    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Deterministic mechanical lint for an llm-wiki.")
    parser.add_argument("wiki_root", nargs="?", help="wiki root (dir containing SCHEMA.md)")
    parser.add_argument("--auto", action="store_true", help="resolve wiki root from cwd; no-op if none")
    parser.add_argument("--quiet", action="store_true", help="print nothing when there are no findings")
    args = parser.parse_args(argv)

    if args.auto:
        root = find_wiki_root_auto(Path.cwd())
        if root is None:
            return 0
    elif args.wiki_root:
        root = Path(args.wiki_root).resolve()
        problem = validate_wiki_root(root)
        if problem:
            print(problem, file=sys.stderr)
            return 2
    else:
        parser.error("provide a wiki root or --auto")

    findings = lint(root)
    if findings:
        print(f"wiki-lint (mechanical): {len(findings)} finding(s)")
        for f in findings:
            print(f"  - {f}")
    elif not args.quiet:
        print("wiki-lint (mechanical): clean")
    return 0  # non-blocking


if __name__ == "__main__":
    raise SystemExit(main())
