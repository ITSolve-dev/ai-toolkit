#!/usr/bin/env python3
"""Check that compressing a wiki page kept what the base is worth: its evidence and its claims' force.

caveman-compress validates headings, code, URLs and paths. It does not see quotations, wikilinks,
line citations, numbers or negations, and its rules allow merging bullets and dropping examples.
On this base a quotation that drifts is a false source, and a dropped "not" reverses a rule, so
each of those must survive compression unchanged.

Usage:
    verify_compressed.py --pair READABLE.md COMPRESSED.md
    verify_compressed.py --root KNOWLEDGE_DIR --ref GIT_REF [PAGE ...]

With --ref, every page under wiki/ (or each PAGE given) is compared with its text at GIT_REF,
normally the tag of the readable base. log.md and wiki/index.md are never compressed and are
skipped. Exit status is 1 if any page fails, 2 on a usage or git error.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

FRONTMATTER = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n", re.DOTALL)
FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
WIKILINK = re.compile(r"\[\[[^\]\n]+\]\]")
LINE_CITE = re.compile(r"\bL\d+(?:\s*[-–]\s*L?\d+)?\b")
INLINE_CODE = re.compile(r"`[^`\n]+`")
NUMBER = re.compile(r"(?<![\w.])\d+(?:[.,]\d+)*%?")
# Straight or curly double quotes, at least two words inside, so a scare-quoted term
# is still checked but a stray inch mark is not.
QUOTATION = re.compile(r'"([^"\n]*\s[^"\n]*)"|“([^”\n]*\s[^”\n]*)”')
NEGATION = re.compile(
    r"\b(?:not|no|never|none|nothing|nor|neither|without|cannot)\b|n't\b", re.IGNORECASE
)
SKIPPED = {"log.md", "index.md"}


def _split(text: str) -> tuple[str, str]:
    m = FRONTMATTER.match(text)
    return (m.group(0), text[m.end():]) if m else ("", text)


def _code_blocks(body: str) -> tuple[list[str], str]:
    """Return fenced blocks verbatim and the body with them blanked out."""
    blocks, kept, current, fence = [], [], None, None
    for line in body.splitlines():
        m = FENCE.match(line)
        if current is None and m:
            current, fence = [line], m.group(1)[0]
        elif current is not None:
            current.append(line)
            if m and m.group(1)[0] == fence:
                blocks.append("\n".join(current))
                current = None
        else:
            kept.append(line)
    if current is not None:
        blocks.append("\n".join(current))
    return blocks, "\n".join(kept)


def _blockquotes(body: str) -> tuple[list[str], list[str]]:
    """Return each blockquote verbatim, and the first sentence of prose after each one."""
    quotes, followers = [], []
    lines = body.splitlines()
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith(">"):
            start = i
            while i < len(lines) and lines[i].lstrip().startswith(">"):
                i += 1
            quotes.append("\n".join(l.rstrip() for l in lines[start:i]))
            j = i
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and not lines[j].lstrip().startswith(("#", ">", "|", "-", "*")):
                para = []
                while j < len(lines) and lines[j].strip():
                    para.append(lines[j].strip())
                    j += 1
                sentence = re.split(r"(?<=[.!?])\s", " ".join(para), maxsplit=1)[0]
                followers.append(sentence)
        else:
            i += 1
    return quotes, followers


def features(text: str) -> dict:
    """Everything that must survive compression, extracted from one page."""
    frontmatter, body = _split(text.replace("\r\n", "\n"))
    code, prose = _code_blocks(body)
    quotes, followers = _blockquotes(prose)
    unquoted = "\n".join(l for l in prose.splitlines() if not l.lstrip().startswith(">"))
    # A quotation may wrap across lines, and compression reflows text: compare it with each
    # paragraph joined into one line, so a reflow is no change and a wrapped quotation is seen.
    unquoted = re.sub(r"(?<=\S)[ \t]*\n(?=[ \t]*[^\s#>|*-])", " ", unquoted)
    return {
        "frontmatter": frontmatter,
        "headings": [l.rstrip() for l in prose.splitlines() if re.match(r"^#{1,6}\s", l)],
        "code blocks": code,
        "blockquotes": quotes,
        "sentence after a blockquote": followers,
        "quotations": Counter(a or b for a, b in QUOTATION.findall(unquoted)),
        "wikilinks": Counter(WIKILINK.findall(prose)),
        "line citations": Counter(re.sub(r"\s+", "", c).replace("–", "-") for c in LINE_CITE.findall(prose)),
        "inline code": Counter(INLINE_CODE.findall(prose)),
        "numbers": Counter(NUMBER.findall(prose)),
        "negations": Counter(_negation(m) for m in NEGATION.findall(prose)),
    }


def _negation(word: str) -> str:
    """Count "doesn't" and "does not" as the same negation, so the contraction alone is no change."""
    w = word.lower()
    return "not" if w in ("n't", "cannot") else w


def compare(readable: str, compressed: str) -> list[str]:
    """Return one line per difference; an empty list means the compressed page is acceptable."""
    a, b = features(readable), features(compressed)
    problems = []
    for name in a:
        if a[name] == b[name]:
            continue
        if isinstance(a[name], Counter):
            lost = a[name] - b[name]
            added = b[name] - a[name]
            if lost:
                problems.append(f"{name} lost: {_show(lost)}")
            if added:
                problems.append(f"{name} added: {_show(added)}")
        elif isinstance(a[name], list):
            lost = [x for x in a[name] if x not in b[name]]
            added = [x for x in b[name] if x not in a[name]]
            if lost:
                problems.append(f"{name} lost or changed: {_show(lost)}")
            if added:
                problems.append(f"{name} added or changed: {_show(added)}")
            if not lost and not added:
                problems.append(f"{name} reordered or duplicated")
        else:
            problems.append(f"{name} changed")
    return problems


def _show(items) -> str:
    items = list(items.elements()) if isinstance(items, Counter) else list(items)
    shown = [repr(x if len(x) <= 70 else x[:67] + "...") for x in items[:5]]
    more = f" (+{len(items) - 5} more)" if len(items) > 5 else ""
    return ", ".join(shown) + more


def _git_show(root: Path, ref: str, path: Path) -> str:
    top = Path(subprocess.run(["git", "-C", str(root), "rev-parse", "--show-toplevel"],
                              capture_output=True, text=True, check=True).stdout.strip())
    rel = path.resolve().relative_to(top.resolve()).as_posix()
    out = subprocess.run(["git", "-C", str(top), "show", f"{ref}:{rel}"],
                         capture_output=True, check=True)
    return out.stdout.decode("utf-8")


def main(argv: list[str] | None = None) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--pair", nargs=2, metavar=("READABLE", "COMPRESSED"), type=Path)
    ap.add_argument("--root", type=Path, help="the wiki root, holding SCHEMA.md and wiki/")
    ap.add_argument("--ref", help="git ref of the readable base, e.g. its tag")
    ap.add_argument("pages", nargs="*", type=Path)
    args = ap.parse_args(argv)

    if args.pair:
        pairs = [(args.pair[1], args.pair[0].read_text(encoding="utf-8"))]
    elif args.root and args.ref:
        pages = args.pages or sorted((args.root / "wiki").rglob("*.md")) + [args.root / "SCHEMA.md"]
        pairs = []
        for page in pages:
            if page.name in SKIPPED:
                continue
            try:
                pairs.append((page, _git_show(args.root, args.ref, page)))
            except subprocess.CalledProcessError as e:
                print(f"{page}: cannot read it at {args.ref}: {e.stderr.decode().strip()}", file=sys.stderr)
                return 2
    else:
        ap.error("give --pair, or --root with --ref")

    failed = 0
    for page, readable in pairs:
        problems = compare(readable, page.read_text(encoding="utf-8"))
        if problems:
            failed += 1
            print(f"FAIL {page}")
            for p in problems:
                print(f"  {p}")
    print(f"{len(pairs) - failed} of {len(pairs)} pages pass")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
