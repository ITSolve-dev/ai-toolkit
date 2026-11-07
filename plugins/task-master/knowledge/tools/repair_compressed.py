#!/usr/bin/env python3
"""Repair a compressed page that verify_compressed rejected, or put the readable page back.

caveman-compress rewrites prose freely, so on this base it routinely drops a "not" or rewrites the
sentence that attributes a quotation. Each failure is narrow and named by verify_compressed, so a
second model pass is given the readable page, the compressed page and the list of differences, and
asked to restore exactly those. A page still failing after the retries is restored from the
readable tag: an uncompressed page costs some context, a wrong one costs a false rule.

A page is restored only when nothing but compression can have changed it since the ref: its text
at HEAD equals its text at the ref (the compression is uncommitted), or caveman-compress's backup
PAGE.original.md beside it equals the ref text. Otherwise it may hold edits newer than the ref,
and it is left as is and reported "not restored".

A model reply that is not a page (no frontmatter where the readable page has one, or a known
error text such as "API Error"), a non-zero exit, or no answer within TIMEOUT seconds is an
error: nothing is written and the run stops.

Usage:
    repair_compressed.py --root KNOWLEDGE_DIR --ref GIT_REF PAGE [PAGE ...]

Requires the `claude` CLI on PATH. Prints one line per page: passed, repaired, restored, or not
restored. Exit status: 0 every page passed or was repaired; 3 a page was restored from the ref
(and none is left failing); 1 a page is left failing (not restored); 2 an error (git, the model
call, a missing `claude`), with the pages before it already handled.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from verify_compressed import _git_show, compare  # noqa: E402

TIMEOUT = 600
ERROR_PREFIXES = ("api error", "error:", "credit balance", "rate limit", "usage limit", "overloaded",
                  "request timed out", "invalid api key")

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


class ModelError(Exception):
    pass


def _claude(prompt: str, timeout: int = TIMEOUT) -> str:
    exe = shutil.which("claude")
    if exe is None:
        raise ModelError("the claude CLI is not on PATH")
    try:
        out = subprocess.run([exe, "--print", "--model", "sonnet"], input=prompt, capture_output=True,
                             text=True, encoding="utf-8", check=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        raise ModelError(f"claude did not answer in {timeout} s") from None
    except subprocess.CalledProcessError as e:
        raise ModelError(f"claude exited {e.returncode}: {(e.stderr or e.stdout or '').strip()[:200]}") from None
    text = out.stdout.strip() + "\n"
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0]
    return text


def check_reply(text: str, readable: str) -> None:
    """Raise ModelError when the reply is not a page: an error text the CLI printed with exit 0."""
    head = text.lstrip()[:200]
    if head.lower().startswith(ERROR_PREFIXES):
        raise ModelError(f"the model replied with an error, not a page: {head[:120]!r}")
    if readable.startswith("---") and not text.startswith("---"):
        raise ModelError(f"the reply is not a page (no frontmatter): {head[:120]!r}")


def _decode(err) -> str:
    return err.decode("utf-8", "replace") if isinstance(err, bytes) else (err or "")


def only_compression_changed(root: Path, ref: str, page: Path, readable: str) -> bool:
    backup = page.with_name(page.stem + ".original.md")
    if backup.is_file() and backup.read_text(encoding="utf-8") == readable:
        return True
    try:
        return _git_show(root, "HEAD", page) == readable
    except subprocess.CalledProcessError:
        return False


def repair(page: Path, readable: str, tries: int = 2, root: Path | None = None, ref: str | None = None) -> str:
    compressed = page.read_text(encoding="utf-8")
    problems = compare(readable, compressed)
    if not problems:
        return "passed"
    for _ in range(tries):
        fixed = _claude(PROMPT.format(problems="\n".join(f"- {p}" for p in problems),
                                      readable=readable, compressed=compressed))
        check_reply(fixed, readable)
        problems = compare(readable, fixed)
        if not problems:
            page.write_text(fixed, encoding="utf-8", newline="\n")
            return "repaired"
        compressed = fixed
    why = f"the model's repair still fails the checks: {'; '.join(problems)}"[:240]
    if root is not None and not only_compression_changed(root, ref, page, readable):
        return (f"not restored: the page changed after {ref} by more than an uncommitted compression "
                f"(no matching .original.md backup), so it may hold newer edits; left as is. {why}")
    page.write_text(readable, encoding="utf-8", newline="\n")
    return f"restored from {ref}: {why}"


def main(argv: list[str] | None = None) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--root", type=Path, required=True)
    ap.add_argument("--ref", required=True)
    ap.add_argument("pages", nargs="+", type=Path)
    args = ap.parse_args(argv)
    restored = failing = False
    for page in args.pages:
        try:
            result = repair(page, _git_show(args.root, args.ref, page), root=args.root, ref=args.ref)
        except subprocess.CalledProcessError as e:
            print(f"{page}: error: git: {_decode(e.stderr).strip()[:200]}", file=sys.stderr)
            return 2
        except ModelError as e:
            print(f"{page}: error: {e}; the page is unchanged", file=sys.stderr)
            return 2
        except (OSError, UnicodeDecodeError, ValueError) as e:
            print(f"{page}: error: {e}", file=sys.stderr)
            return 2
        restored |= result.startswith("restored")
        failing |= result.startswith("not restored")
        print(f"{page}: {result}", flush=True)
    return 1 if failing else 3 if restored else 0


if __name__ == "__main__":
    sys.exit(main())
