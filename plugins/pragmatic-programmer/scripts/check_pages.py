#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
"""Check this wiki's own page format, and that a compression pass kept what it must not change.

`wiki-lint` checks links and generic frontmatter. It knows nothing of this wiki's charter, and it
always exits 0. This script enforces the charter's mechanical rules and fails the build.

Usage:
    check_pages.py <wiki-root>                      check every page against the charter
    check_pages.py <wiki-root> --baseline <copy>    also compare pages with a copy from before
                                                    a compression pass

Exit code: 0 clean, 1 violations found, 2 bad usage.

Dependencies: standard library only.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

KINDS = {"summary", "concept", "rule", "decision-rule", "method"}
PARADIGMS = {"any", "oop", "fp"}
RULE_KINDS = {"rule", "decision-rule"}
RULE_SECTIONS = ["Rule", "Sign in code", "When not to apply", "Repair", "Before and after", "Source"]
SUBSTANTIVE_SECTIONS = ["Rule", "Sign in code", "When not to apply", "Repair"]
MIN_SECTION_CHARS = 30
PROTECTED_SECTIONS = {"source", "sources", "when not to apply"}
ROOT_PAGES = {"index.md", "overview.md", "synthesis.md"}
PSEUDOCODE_FENCE_TAGS = {"", "text", "pseudo", "pseudocode"}

FRONTMATTER_RE = re.compile(r"\A﻿?---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)
LIST_MARKER = r"(?:(?:[-*+]|\d+[.)])[ \t]+)"
FENCE_OPEN_RE = re.compile(rf"^[ \t]*{LIST_MARKER}*(`{{3,}}|~{{3,}})(.*)$")
QUOTE_LINE_RE = re.compile(rf"^[ \t]*{LIST_MARKER}*>")
LIST_ITEM_RE = re.compile(rf"^[ \t]*{LIST_MARKER}")
INDENTED_RE = re.compile(r"^(?: {4}|\t)[ \t]*\S")
HEADING_RE = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.+?)[ \t]*$")
INLINE_CODE_RE = re.compile(r"`[^`]+`")
WIKILINK_RE = re.compile(r"\[\[[^\[\]]+\]\]")
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
QUOTATION_RE = re.compile(
    r"[“„][^”“]*[”“]"
    r"|«[^»]*»"
    r"|‘[^’]*’"
    r"|(?<!\w)\"[^\"]+\"(?!\w)"
    r"|(?<![\w'])'[^']+'(?!\w)"
)
SENTENCE_END_RE = re.compile(r"(?<=[.!?…])\s+")
# A sentence holding one of these keeps its meaning only word for word, so a pass leaves it alone.
# Comparing the words alone would let a negation move to the next sentence and invert both.
GUARDED_RE = re.compile(
    r"\d"
    r"|\b(?:not|never|no|none|nor|neither|nothing|nobody|nowhere|only|except|without|unless|cannot"
    r"|rarely|seldom|hardly|barely|non-\w+|\w+n['’]t"
    r"|zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|half|twice"
    r"|[IVX]{2,}"
    r"|не|нет|ни|нельзя|никогда|без|только|лишь|кроме"
    r"|ноль|один|одна|два|две|три|четыре|пять|шесть|семь|восемь|девять|десять)\b",
    re.IGNORECASE,
)


@dataclass
class Blocks:
    """A page body sorted into the block kinds a compression pass must treat differently."""

    fences: list[tuple[str, str]] = field(default_factory=list)  # (info string, content)
    indented: list[str] = field(default_factory=list)
    quotes: list[str] = field(default_factory=list)
    headings: list[tuple[int, str]] = field(default_factory=list)
    prose: list[str] = field(default_factory=list)
    lines: list[tuple[str, str]] = field(default_factory=list)  # (kind, line), in order


def parse_blocks(body: str) -> Blocks:
    """Sort a body line by line, following CommonMark's fence rules.

    A closing fence uses the opener's character, is at least as long, and carries nothing else. An
    unclosed fence runs to the end of the page.
    """
    blocks = Blocks()
    opener: tuple[str, int] | None = None
    info = ""
    content: list[str] = []
    in_quote = False

    for line in body.splitlines():
        if opener:
            stripped = line.strip()
            char, length = opener
            if len(stripped) >= length and not stripped.strip(char):
                blocks.fences.append((info, "\n".join(content)))
                opener = None
            else:
                content.append(line)
            blocks.lines.append(("fence", line))
            continue

        fence = FENCE_OPEN_RE.match(line)
        heading = HEADING_RE.match(line)
        if fence and not (fence.group(1)[0] == "`" and "`" in fence.group(2)):
            opener = (fence.group(1)[0], len(fence.group(1)))
            info, content, in_quote = fence.group(2).strip(), [], False
            blocks.lines.append(("fence", line))
        elif not line.strip():
            in_quote = False
            blocks.lines.append(("blank", line))
        elif heading:
            in_quote = False
            blocks.headings.append((len(heading.group(1)), heading.group(2)))
            blocks.lines.append(("heading", line))
        elif QUOTE_LINE_RE.match(line) or in_quote:
            in_quote = True
            blocks.quotes.append(line.strip())
            blocks.lines.append(("quote", line))
        elif INDENTED_RE.match(line):
            blocks.indented.append(line)
            blocks.lines.append(("indented", line))
        else:
            blocks.prose.append(line)
            blocks.lines.append(("prose", line))

    if opener:
        blocks.fences.append((info, "\n".join(content)))
    return blocks


def split_page(text: str) -> tuple[dict[str, str], str, str]:
    """Return a page's flat frontmatter fields, the raw frontmatter block, and its body."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, "", text
    fields = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep and key and not key.startswith((" ", "\t")):
            fields[key.strip()] = value.strip()
    return fields, match.group(1), text[match.end() :]


def inline_list(raw: str) -> list[str]:
    return [item.strip() for item in raw.strip().strip("[]").split(",") if item.strip()]


def sections(body: str) -> list[tuple[str, str]]:
    """The `## ` sections of a body, in order. A heading inside a code block starts nothing."""
    found: list[tuple[str, list[str]]] = []
    for kind, line in parse_blocks(body).lines:
        heading = HEADING_RE.match(line) if kind == "heading" else None
        if heading and len(heading.group(1)) == 2:
            found.append((heading.group(2), []))
        elif found:
            found[-1][1].append(line)
    return [(name, "\n".join(lines).strip()) for name, lines in found]


def protected_section_text(body: str) -> list[str]:
    """Every line under a protected heading of any level, until a heading of the same or higher level."""
    kept: list[str] = []
    level = 0
    for kind, line in parse_blocks(body).lines:
        heading = HEADING_RE.match(line) if kind == "heading" else None
        if heading:
            depth = len(heading.group(1))
            if level and depth <= level:
                level = 0
            if not level and heading.group(2).strip().casefold() in PROTECTED_SECTIONS:
                level = depth
                continue
        if level and line.strip():
            kept.append(line.strip())
    return kept


def has_substance(text: str) -> bool:
    """False for an empty section, a placeholder such as TODO, or one holding only subheadings."""
    text = COMMENT_RE.sub("", text)
    lines = [line for line in text.splitlines() if not HEADING_RE.match(line)]
    return len(" ".join(lines).strip()) >= MIN_SECTION_CHARS


def check_rule_page(body: str, sources: list[str]) -> list[str]:
    problems = []
    found = sections(body)
    names = [name for name, _ in found]
    present = [name for name in names if name in RULE_SECTIONS]
    missing = [name for name in RULE_SECTIONS if name not in names]
    if missing:
        problems.append(f"missing sections: {', '.join(missing)}")
    elif present != RULE_SECTIONS:
        problems.append(f"sections out of order: {', '.join(present)}")

    contents = dict(found)
    for name in SUBSTANTIVE_SECTIONS:
        if name in contents and not has_substance(contents[name]):
            problems.append(f"empty or token section: {name}")

    if "Before and after" in contents:
        fences = parse_blocks(contents["Before and after"]).fences
        if not any(text.strip() for _, text in fences):
            problems.append("Before and after has no fenced pseudocode")

    if "Source" in contents:
        source = INLINE_CODE_RE.sub(" ", contents["Source"])
        if not source.strip():
            problems.append("empty section: Source")
        elif sources and not WIKILINK_RE.search(source):
            problems.append("Source section links to no source page")
    return problems


def check_page(path: Path, group: str) -> list[str]:
    fields, _, body = split_page(path.read_text(encoding="utf-8"))
    if not fields:
        return ["no frontmatter"]

    tags = inline_list(fields.get("tags", ""))
    kind = tags[0] if tags else ""
    problems = []
    if fields.get("category") != group:
        problems.append(f"category must equal the folder name: {group}")
    if kind not in KINDS:
        problems.append(f"first tag is not a page kind: {kind or '(none)'}")
    if kind != "summary" and fields.get("paradigm") not in PARADIGMS:
        problems.append(f"paradigm must be one of {sorted(PARADIGMS)}")
    if not fields.get("sources", "").startswith("["):
        problems.append("sources must be an inline list")
    if kind in RULE_KINDS:
        problems.extend(check_rule_page(body, inline_list(fields.get("sources", ""))))
    for info, _ in parse_blocks(body).fences:
        if info.lower() not in PSEUDOCODE_FENCE_TAGS:
            problems.append(f"code fence names a language: {info}")
    return problems


def check_wiki(root: Path) -> list[str]:
    problems = []
    wiki = root / "wiki"
    for loose in sorted(wiki.glob("*.md")):
        if loose.name not in ROOT_PAGES:
            problems.append(f"{loose.relative_to(root)}: a page lives in a group folder")
    for group in sorted(p for p in wiki.iterdir() if p.is_dir()):
        for nested in sorted(p for p in group.iterdir() if p.is_dir()):
            problems.append(f"{nested.relative_to(root)}: groups are flat, the index skips this")
        for page in sorted(group.glob("*.md")):
            for problem in check_page(page, group.name):
                problems.append(f"{page.relative_to(root)}: {problem}")
    return problems


def paragraphs(prose: list[str]) -> list[str]:
    """Prose as blocks with line wraps undone, since rewrapping a line is not a change."""
    blocks: list[list[str]] = [[]]
    for line in prose:
        if LIST_ITEM_RE.match(line):
            blocks.append([])
        blocks[-1].append(line.strip(" \t"))
    return [" ".join(block) for block in blocks if block]


def body_paragraphs(blocks: Blocks) -> list[str]:
    """Paragraphs of prose, split at every blank line or non-prose block."""
    runs: list[list[str]] = [[]]
    for kind, line in blocks.lines:
        if kind == "prose":
            runs[-1].append(line)
        elif runs[-1]:
            runs.append([])
    found: list[str] = []
    for run in runs:
        found.extend(paragraphs(run))
    return found


def protected_parts(text: str) -> dict[str, list[str]]:
    """Everything a compression pass must leave unchanged, in order of appearance."""
    _, frontmatter, body = split_page(text)
    blocks = parse_blocks(body)
    parts: dict[str, list[str]] = {
        "frontmatter": [
            "updated:" if line.startswith("updated:") else line for line in frontmatter.splitlines()
        ],
        "code blocks": [f"{info}\n{content}" for info, content in blocks.fences],
        "indented code": blocks.indented,
        "headings": [f"{level} {title}" for level, title in blocks.headings],
        "protected sections": protected_section_text(body),
        "block quotes": blocks.quotes,
    }

    inline_code, wikilinks, quotations, sentences = [], [], [], []
    for paragraph in body_paragraphs(blocks):
        inline_code.extend(INLINE_CODE_RE.findall(paragraph))
        text_only = INLINE_CODE_RE.sub(" ", paragraph)
        wikilinks.extend(WIKILINK_RE.findall(text_only))
        quotations.extend(QUOTATION_RE.findall(text_only))
        sentences.extend(s for s in SENTENCE_END_RE.split(paragraph) if GUARDED_RE.search(s))
    parts["inline code"] = inline_code
    parts["wikilinks"] = wikilinks
    parts["quotations"] = quotations
    parts["guarded sentences"] = sentences
    return parts


def compare_page(before: str, after: str) -> list[str]:
    old, new = protected_parts(before), protected_parts(after)
    return [f"{name} changed" for name in old if old[name] != new[name]]


def compare_wiki(root: Path, baseline: Path) -> list[str]:
    problems = []
    wiki, old_wiki = root / "wiki", baseline / "wiki"
    pages = {p.relative_to(wiki) for p in wiki.rglob("*.md")}
    old_pages = {p.relative_to(old_wiki) for p in old_wiki.rglob("*.md")}
    for missing in sorted(old_pages - pages):
        problems.append(f"wiki/{missing.as_posix()}: removed by the pass")
    for extra in sorted(pages - old_pages):
        problems.append(f"wiki/{extra.as_posix()}: added by the pass")
    for relative in sorted(pages & old_pages):
        before = (old_wiki / relative).read_text(encoding="utf-8")
        after = (wiki / relative).read_text(encoding="utf-8")
        if relative == Path("index.md"):
            continue
        for problem in compare_page(before, after):
            problems.append(f"wiki/{relative.as_posix()}: {problem}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("root", type=Path, help="wiki root holding SCHEMA.md")
    parser.add_argument("--baseline", type=Path, help="copy of the wiki root from before the pass")
    args = parser.parse_args()

    for root in filter(None, (args.root, args.baseline)):
        if not (root / "SCHEMA.md").is_file() or not (root / "wiki").is_dir():
            print(f"not a wiki root: {root}", file=sys.stderr)
            return 2

    problems = check_wiki(args.root)
    if args.baseline:
        problems.extend(compare_wiki(args.root, args.baseline))

    for problem in problems:
        print(problem)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
