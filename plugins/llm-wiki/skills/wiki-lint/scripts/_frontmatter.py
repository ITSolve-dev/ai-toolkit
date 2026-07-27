#!/usr/bin/env python3
"""Shared frontmatter helpers for the wiki-lint scripts.

One home for the wiki-root walk and the minimal `key: value` frontmatter parser, so
build_index.py, lint_mechanical.py and build_manifest.py don't each carry their own copy.
No third-party YAML dependency — the frontmatter this plugin writes is deliberately flat.

Dependencies: standard library only.
"""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path


def is_forbidden_root(path: Path) -> bool:
    """True if `path` is the user's home directory or a filesystem/drive root.

    Per references/wiki-resolution.md such a directory is never a wiki root — not even when it
    happens to contain a SCHEMA.md.
    """
    path = path.resolve()
    if path.parent == path:  # filesystem / drive root
        return True
    return path == Path.home().resolve()


def find_wiki_root(start: Path) -> Path | None:
    """Walk up from `start` to the first directory containing SCHEMA.md.

    The boundary is tested BEFORE the marker, so a home or drive root is never returned even if
    a SCHEMA.md sits there (references/wiki-resolution.md: never treat it as a candidate).
    """
    cur = start.resolve()
    while True:
        if is_forbidden_root(cur):
            return None
        if (cur / "SCHEMA.md").exists():
            return cur
        cur = cur.parent


def find_wiki_root_auto(start: Path) -> Path | None:
    """Resolve the wiki root for hook / `--auto` mode, tolerating a wiki nested below `start`.

    First walk up (the common case: `start` is the wiki root or inside it). If that finds nothing,
    look one level down: when `start` has exactly one immediate subdirectory that is a wiki root,
    use it — this covers a wiki that lives in a subfolder of the working directory. Zero or several
    candidates below → return None, so the hook stays a silent no-op instead of guessing. A wiki
    deeper than one level below, or a sibling outside `start`, is still out of reach from cwd alone.
    """
    up = find_wiki_root(start)
    if up is not None:
        return up
    start = start.resolve()
    if is_forbidden_root(start):
        return None
    try:
        children = sorted(d for d in start.iterdir() if d.is_dir())
    except OSError:
        return None
    candidates = [d for d in children if (d / "SCHEMA.md").exists() and not is_forbidden_root(d)]
    return candidates[0] if len(candidates) == 1 else None


def read_text(path: Path) -> str:
    """Read a file for parsing, tolerating undecodable bytes and unreadable paths.

    These scripts run on every turn, so one mis-encoded or unreadable file must not abort the
    pass — that would silently freeze the generated artifacts from then on.
    """
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            return path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            return ""
    except OSError:
        return ""


def atomic_write(path: Path, text: str) -> None:
    """Write `text` to `path` atomically, replacing a symlink at `path` instead of writing through it.

    A derived artifact (index.md, .manifest.json) regenerated automatically by the Stop hook must not
    follow a symlink a crafted wiki repo could have planted there — that would let it clobber an
    arbitrary writable file. Writing a temp file in the same directory and os.replace-ing it over the
    name swaps the directory entry (the symlink) itself rather than its target.
    """
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=path.name + ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def validate_wiki_root(root: Path) -> str | None:
    """Return an error message if `root` is not a usable wiki root, else None.

    Used by the scripts' explicit-path mode, which would otherwise happily create wiki
    artifacts inside any directory it is pointed at.
    """
    root = root.resolve()
    if is_forbidden_root(root):
        return f"refusing a home or drive root as a wiki root: {root}"
    if not (root / "SCHEMA.md").exists():
        return f"not a wiki root (no SCHEMA.md): {root}"
    return None


def strip_inline_comment(value: str) -> str:
    """Drop an unquoted trailing `# ...` comment from a frontmatter value.

    Only cuts at a `#` that follows whitespace and sits outside quotes, so values like
    "C# basics" or a quoted 'a # b' survive intact.
    """
    value = value.strip()
    if value[:1] in {'"', "'"}:
        closing = value.find(value[0], 1)
        return value[: closing + 1] if closing != -1 else value
    cut = value.find(" #")
    return value[:cut].strip() if cut != -1 else value


def decode_scalar(value: str) -> str:
    """Decode one frontmatter value.

    Adapters write strings with `json.dumps`, so a double-quoted value is a JSON string and must
    be JSON-decoded — otherwise escapes survive into the parsed value: `\\uXXXX` stays literal,
    a Windows path doubles its separators, and a `\\"` inside the text truncates it. `raw_decode`
    reads just the leading JSON string and ignores any trailing inline comment.
    """
    v = value.strip()
    if v.startswith('"'):
        try:
            obj, _ = json.JSONDecoder().raw_decode(v)
            if isinstance(obj, str):
                return obj
        except ValueError:
            pass  # not valid JSON — fall through to the plain reading
    return strip_inline_comment(v).strip('"').strip("'")


def parse_frontmatter(text: str, dequote: bool = True) -> dict[str, str]:
    """Parse the leading `---` frontmatter block into a flat {key: value} dict.

    Reads only top-level `key: value` scalars; list items and nested lines contribute
    harmless extra keys that callers simply don't read. With `dequote` (default), surrounding
    quotes are stripped from each value.
    """
    text = text.lstrip("﻿")  # a byte-order mark would otherwise hide the whole block
    lines = text.splitlines()
    # Opening and closing markers must each be a line that is exactly `---` (surrounding whitespace
    # ignored). A line like `---invalid` is NOT a delimiter, so it can neither open the block nor
    # terminate it early and smuggle malformed frontmatter past the parser.
    if not lines or lines[0].strip() != "---":
        return {}
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return {}
    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        # Only top-level keys count. An indented line belongs to a nested block, and letting it
        # through would let a nested `title:`/`category:` shadow the page's real one.
        if line[:1].isspace():
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = decode_scalar(value) if dequote else strip_inline_comment(value)
    return fields
