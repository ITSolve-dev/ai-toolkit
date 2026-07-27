#!/usr/bin/env python3
"""read-docx adapter: Word .docx -> normalized raw/<slug>.md.

Faithful, structure-preserving extraction only — no relevance filtering (that is
wiki-ingest's job). Backends: Pandoc (default, external binary) or Mammoth (--mammoth,
pure-Python). Satisfies references/adapter-contract.md.

Usage:
    extract.py <source.docx> --raw-dir <wiki-root>/raw [--slug NAME] [--mammoth]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from datetime import date
from pathlib import Path


# Cyrillic → Latin so Russian/Ukrainian titles yield a readable slug, not a hash fallback.
_CYRILLIC = {
    "а": "a", "б": "b", "в": "v", "г": "g", "ґ": "g", "д": "d", "е": "e", "ё": "e",
    "є": "ye", "ж": "zh", "з": "z", "и": "i", "і": "i", "ї": "yi", "й": "y", "к": "k",
    "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t",
    "у": "u", "ф": "f", "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "shch",
    "ъ": "", "ы": "y", "ь": "", "э": "e", "ю": "yu", "я": "ya",
}


def slugify(text: str) -> str:
    """Filesystem-safe, informative slug that never collapses distinct titles together.

    Latin (incl. accents via NFKD) and Cyrillic transliterate to ASCII kebab-case; a title in a
    script with no transliteration here (CJK, Arabic, …) reduces to empty and would overwrite a
    shared file, so fall back to a short stable hash.
    """
    translit = "".join(_CYRILLIC.get(ch, ch) for ch in text.lower())
    ascii_text = unicodedata.normalize("NFKD", translit).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_text).strip("-")
    if slug:
        return slug
    if text.strip():
        return "x" + hashlib.sha1(text.strip().encode("utf-8")).hexdigest()[:8]
    return "source"


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def heading_map(markdown: str, limit: int = 300) -> list[str]:
    """The document's real ATX headings, for the structure map / citation anchors.

    Two gates so a `#` inside a fenced code block or a code comment is not indexed as a heading
    (the large-source workflow slices the source at these lines): a line counts only if it is
    OUTSIDE a ``` fence AND starts its own block (previous line blank or itself a heading).
    """
    out: list[str] = []
    in_fence = False
    at_boundary = True
    for ln in markdown.splitlines():
        stripped = ln.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            at_boundary = False
            continue
        is_heading = not in_fence and at_boundary and ln.startswith("#")
        if is_heading:
            out.append(ln.strip())
        at_boundary = is_heading or not ln.strip()
    return out[:limit]


def yaml_list(items: list[str]) -> str:
    return "[]" if not items else "\n" + "\n".join(f"  - {json.dumps(i)}" for i in items)


def to_markdown_pandoc(src: Path, media_dir: Path) -> str:
    result = subprocess.run(
        ["pandoc", str(src), "-t", "gfm", "--wrap=none", f"--extract-media={media_dir}"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "pandoc failed")
    return result.stdout


def to_markdown_mammoth(src: Path) -> str:
    import mammoth  # lazy

    with src.open("rb") as f:
        return mammoth.convert_to_markdown(f).value


def build_source_file(src: Path, body: str) -> str:
    fm = [
        "---",
        "type: source",
        f"title: {json.dumps(src.stem)}",
        "source_kind: document",
        f"origin: {json.dumps(str(src.resolve()))}",
        "authors: []",
        'published: ""',
        f"retrieved: {date.today().isoformat()}",
        f"sha256: {sha256_of(src)}",
        f"structure:{yaml_list(heading_map(body))}",
        "---",
        "",
    ]
    return "\n".join(fm) + body.rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="read-docx adapter: .docx -> raw/<slug>.md")
    parser.add_argument("source", type=Path, help="Word .docx file")
    parser.add_argument("--raw-dir", type=Path, required=True, help="the wiki's raw/ directory")
    parser.add_argument("--slug", help="output slug (default: from filename)")
    parser.add_argument("--mammoth", action="store_true", help="use Mammoth instead of Pandoc")
    parser.add_argument("--force", action="store_true", help="overwrite an existing raw/ file (re-ingest)")
    args = parser.parse_args(argv)

    if not args.source.exists():
        print(f"source not found: {args.source}", file=sys.stderr)
        return 1

    slug = args.slug or f"document-{slugify(args.source.stem)}"
    if not slug or slug in (".", "..") or any(c in slug for c in "/\\:"):
        print(f"invalid --slug '{slug}': must be a bare filename (no path separators)", file=sys.stderr)
        return 2
    out = args.raw_dir / f"{slug}.md"
    if out.exists() and not args.force:
        print(f"{out.name} already exists — re-ingest with --force, or pass a distinct --slug", file=sys.stderr)
        return 3
    args.raw_dir.mkdir(parents=True, exist_ok=True)
    try:
        if args.mammoth:
            body = to_markdown_mammoth(args.source)
        else:
            body = to_markdown_pandoc(args.source, args.raw_dir / f"{slug}-media")
    except FileNotFoundError:
        print("pandoc not found on PATH — install it or pass --mammoth", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"extraction failed: {exc}", file=sys.stderr)
        return 1

    out = args.raw_dir / f"{slug}.md"
    out.write_text(build_source_file(args.source, body), encoding="utf-8")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
