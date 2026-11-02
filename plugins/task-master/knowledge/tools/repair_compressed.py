#!/usr/bin/env python3
"""Repair a compressed page that verify_compressed rejected, or put the readable page back.

caveman-compress rewrites prose freely, so on this base it routinely drops a "not" or rewrites the
sentence that attributes a quotation. Each failure is narrow and named by verify_compressed, so a
second model pass is given the readable page, the compressed page and the list of differences, and
asked to restore exactly those. A page still failing after the retries is restored from the
readable tag: an uncompressed page costs some context, a wrong one costs a false rule.

Usage:
    repair_compressed.py --root KNOWLEDGE_DIR --ref GIT_REF PAGE [PAGE ...]

Requires the `claude` CLI on PATH. Prints one line per page: passed, repaired, or restored.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from verify_compressed import _git_show, compare  # noqa: E402

PROMPT = """You are fixing a compressed copy of a wiki page. Compression was allowed to shorten prose,
but a checker found that it changed things that must stay exactly as in the readable page:

{problems}

Edit the COMPRESSED page so that every item above matches the READABLE page exactly:
- a lost or changed blockquote, quotation, heading, code block, wikilink, line citation (L123) or
  number: copy it back character for character from the readable page;
- a sentence after a blockquote: use the readable sentence verbatim;
- a lost negation (not, no, never, none, nothing, nor, neither, without, cannot): put the same word
  back in the sentence it came from, rewording that sentence only as far as it needs;
- a lost hedge, scope or attribution word (would, may, if, when, only, under, here, says, this wiki,
  the author, ...): put it back in its sentence, so the claim is again as sure, as scoped and as
  attributed as in the readable page;
- an added item: remove what compression introduced, or reword without it.
Leave everything else compressed. Keep the frontmatter byte for byte.

Return ONLY the full corrected page, starting with its frontmatter. No fence around it, no comment.

READABLE:
{readable}

COMPRESSED:
{compressed}
"""


def _claude(prompt: str) -> str:
    exe = shutil.which("claude") or "claude"
    out = subprocess.run([exe, "--print", "--model", "sonnet"], input=prompt, capture_output=True,
                         text=True, encoding="utf-8", check=True)
    text = out.stdout.strip() + "\n"
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0]
    return text


def repair(page: Path, readable: str, tries: int = 2) -> str:
    compressed = page.read_text(encoding="utf-8")
    problems = compare(readable, compressed)
    if not problems:
        return "passed"
    for _ in range(tries):
        fixed = _claude(PROMPT.format(problems="\n".join(f"- {p}" for p in problems),
                                      readable=readable, compressed=compressed))
        problems = compare(readable, fixed)
        if not problems:
            page.write_text(fixed, encoding="utf-8", newline="\n")
            return "repaired"
        compressed = fixed
    page.write_text(readable, encoding="utf-8", newline="\n")
    return "restored: " + "; ".join(problems)[:200]


def main(argv: list[str] | None = None) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--ref", required=True)
    ap.add_argument("pages", nargs="+", type=Path)
    args = ap.parse_args(argv)
    for page in args.pages:
        try:
            result = repair(page, _git_show(args.root, args.ref, page))
        except subprocess.CalledProcessError as e:
            print(f"{page}: error: {(e.stderr or '')[:200]}", file=sys.stderr)
            return 2
        print(f"{page}: {result}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
