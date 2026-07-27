#!/usr/bin/env python3
"""read-book adapter: PDF/EPUB -> normalized raw/<slug>.md.

Faithful, structure-preserving extraction only — this does NOT filter for relevance (that is
wiki-ingest's job). Backends: Docling (default, accurate) or pymupdf4llm (--fast). Produces a
file that satisfies references/adapter-contract.md.

Dependencies are installed on demand by the caller via `uv run --no-project --with docling|pymupdf4llm`
(see SKILL.md); this script imports them lazily so the light path stays light.

Usage:
    extract.py <source.pdf|epub> --raw-dir <wiki-root>/raw [--slug NAME] [--fast]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
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
    """A filesystem-safe, informative slug that never collapses distinct titles together.

    Latin (incl. accents via NFKD) and Cyrillic transliterate to ASCII kebab-case. A title in a
    script with no transliteration here (CJK, Arabic, …) reduces to empty and would overwrite a
    shared file, so fall back to a short stable hash of the title.
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


def to_markdown(src: Path, fast: bool) -> str:
    if fast:
        import pymupdf4llm  # lazy

        return pymupdf4llm.to_markdown(str(src))
    from docling.document_converter import DocumentConverter  # lazy

    return DocumentConverter().convert(str(src)).document.export_to_markdown()


def yaml_list(items: list[str]) -> str:
    if not items:
        return "[]"
    return "\n" + "\n".join(f"  - {json.dumps(i)}" for i in items)


def source_title(src: Path) -> str:
    """Best-effort document title from PDF/EPUB metadata (falls back to '')."""
    try:
        import pymupdf as _fitz  # lazy; pymupdf4llm pulls this in
    except Exception:
        try:
            import fitz as _fitz
        except Exception:
            return ""
    try:
        with _fitz.open(str(src)) as doc:
            return ((doc.metadata or {}).get("title") or "").strip()
    except Exception:
        return ""


def build_source_file(src: Path, body: str, title: str) -> str:
    fm = [
        "---",
        "type: source",
        f"title: {json.dumps(title)}",
        "source_kind: book",
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
    parser = argparse.ArgumentParser(description="read-book adapter: PDF/EPUB -> raw/<slug>.md")
    parser.add_argument("source", type=Path, help="PDF or EPUB file")
    parser.add_argument("--raw-dir", type=Path, required=True, help="the wiki's raw/ directory")
    parser.add_argument("--slug", help="output slug (default: from filename)")
    parser.add_argument("--fast", action="store_true", help="use pymupdf4llm instead of Docling")
    parser.add_argument("--force", action="store_true", help="overwrite an existing raw/ file (re-ingest)")
    args = parser.parse_args(argv)

    if not args.source.exists():
        print(f"source not found: {args.source}", file=sys.stderr)
        return 1

    title = source_title(args.source) or args.source.stem
    slug = args.slug or f"book-{slugify(title)}"
    if not slug or slug in (".", "..") or any(c in slug for c in "/\\:"):
        print(f"invalid --slug '{slug}': must be a bare filename (no path separators)", file=sys.stderr)
        return 2
    args.raw_dir.mkdir(parents=True, exist_ok=True)
    out = args.raw_dir / f"{slug}.md"
    if out.exists() and not args.force:
        print(f"{out.name} already exists — re-ingest with --force, or pass a distinct --slug", file=sys.stderr)
        return 3
    body = to_markdown(args.source, args.fast)
    out.write_text(build_source_file(args.source, body, title), encoding="utf-8")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
