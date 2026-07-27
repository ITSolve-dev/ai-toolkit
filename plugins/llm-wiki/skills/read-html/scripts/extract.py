#!/usr/bin/env python3
"""read-html adapter: web page (or multi-page web work) or local HTML -> normalized raw/<slug>.md.

Faithful extraction only — no relevance filtering (that is wiki-ingest's job). Uses Trafilatura,
which outputs markdown directly. Satisfies references/adapter-contract.md.

With --follow, a multi-page work (a web book / doc site with a table of contents) is gathered into
ONE raw file: the adapter follows same-domain links under the start URL's path, concatenates each
page as its own `#` section, and builds a structure map — so a large web source looks identical to
a book to the ingest step (one raw file + chapter map).

Dependency installed on demand by the caller via `uv run --no-project --with trafilatura` (see SKILL.md).

Usage:
    extract.py <url-or-file.html> --raw-dir <wiki-root>/raw [--slug NAME] [--force]
    extract.py <toc-or-start-url> --raw-dir <wiki-root>/raw --follow [--cap 40] [--title "Work Title"]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urldefrag, urlparse


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


def heading_map(markdown: str, limit: int = 400) -> list[str]:
    """The document's real ATX headings, for the structure map.

    Two independent gates, because relying on the running ``` fence state alone is fragile: a
    single unbalanced fence (one stray ``` among many concatenated pages) inverts that state and
    lets every code comment downstream masquerade as a heading. So a line counts only if it sits
    OUTSIDE a fence AND starts its own block — the previous line was blank or was itself a heading
    (start-of-file counts). A `#` comment inside code follows code, not a block boundary, so it
    fails the second gate even when the fence state is wrong. Extracted markdown always block-
    separates real headings with a blank line, so the boundary gate does not drop real ones.
    """
    out: list[str] = []
    in_fence = False
    at_boundary = True  # start-of-file is a block boundary
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


def fetch(url: str) -> str:
    import trafilatura  # lazy

    html = trafilatura.fetch_url(url)
    if not html:
        raise RuntimeError(f"failed to fetch {url}")
    return html


def load_html(source: str) -> tuple[str, str]:
    """Return (html, origin). Fetches a URL or reads a local file."""
    if source.startswith(("http://", "https://")):
        return fetch(source), source
    path = Path(source)
    return path.read_text(encoding="utf-8", errors="replace"), str(path.resolve())


def extract_markdown(html: str) -> tuple[str, str]:
    """Return (markdown, title)."""
    import trafilatura  # lazy

    md = trafilatura.extract(html, output_format="markdown", include_tables=True, include_links=True)
    if md is None:
        raise RuntimeError("trafilatura extracted no content")
    meta = trafilatura.extract_metadata(html)
    title = getattr(meta, "title", None) or ""
    return md, title


class _LinkGrabber(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "a":
            for k, v in attrs:
                if k == "href" and v:
                    self.hrefs.append(v)


def discover_pages(start_url: str, html: str, cap: int) -> list[str]:
    """Same-domain page URLs under the start URL's directory, in document order, deduped.

    Targets a self-contained web work (a book/doc under one path prefix, e.g. /book/*). Not a
    general crawler: it never leaves the start path prefix or the domain.
    """
    parsed = urlparse(start_url)
    start_dir = parsed.path.rsplit("/", 1)[0] + "/"
    grabber = _LinkGrabber()
    grabber.feed(html)
    seen: set[str] = set()
    ordered: list[str] = []
    # the start page itself first, so a chapter passed directly is still included
    start_clean = urldefrag(f"{parsed.scheme}://{parsed.netloc}{parsed.path}")[0]
    seen.add(start_clean)
    ordered.append(start_clean)
    for href in grabber.hrefs:
        absu = urldefrag(urljoin(start_url, href))[0]
        p = urlparse(absu)
        if p.netloc != parsed.netloc or not p.path.startswith(start_dir):
            continue
        if absu in seen:
            continue
        seen.add(absu)
        ordered.append(absu)
        if len(ordered) >= cap:
            break
    return ordered


def gather_follow(start_url: str, cap: int) -> tuple[str, str, str]:
    """Follow the TOC/pages of a web work. Return (combined_body, work_title, combined_text)."""
    start_html = fetch(start_url)
    _, start_title = extract_markdown(start_html)
    urls = discover_pages(start_url, start_html, cap)
    sections: list[str] = []
    for i, url in enumerate(urls):
        try:
            page_html = start_html if url == urls[0] else fetch(url)
            md, title = extract_markdown(page_html)
        except Exception as exc:  # one bad page must not abort the whole work
            print(f"  skipped {url}: {exc}", file=sys.stderr)
            continue
        if not md or not md.strip():
            continue
        head = title.strip() or url.rsplit("/", 1)[-1]
        sections.append(f"# {head}\n\n<!-- source: {url} -->\n\n{md.strip()}")
    if not sections:
        raise RuntimeError("follow gathered no usable pages")
    body = "\n\n".join(sections)
    print(f"  gathered {len(sections)} page(s) of {len(urls)} discovered", file=sys.stderr)
    return body, (start_title or start_url), body


def build_source_file(origin: str, title: str, hash_text: str, body: str) -> str:
    # Hash the EXTRACTED text, not the raw HTML: raw HTML churns on ads / CSRF tokens / timestamps
    # every fetch, which would make any change-check cry wolf. The distilled text is what we ingest.
    sha = hashlib.sha256(hash_text.encode("utf-8", "replace")).hexdigest()
    fm = [
        "---",
        "type: source",
        f"title: {json.dumps(title or origin)}",
        "source_kind: web-page",
        f"origin: {json.dumps(origin)}",
        "authors: []",
        'published: ""',
        f"retrieved: {date.today().isoformat()}",
        f"sha256: {sha}",
        f"structure:{yaml_list(heading_map(body))}",
        "---",
        "",
    ]
    return "\n".join(fm) + body.rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="read-html adapter: URL/HTML -> raw/<slug>.md")
    parser.add_argument("source", help="URL or local .html file (with --follow, the start/TOC URL)")
    parser.add_argument("--raw-dir", type=Path, required=True, help="the wiki's raw/ directory")
    parser.add_argument("--slug", help="output slug (default: from title/URL)")
    parser.add_argument("--force", action="store_true", help="overwrite an existing raw/ file (re-ingest)")
    parser.add_argument("--follow", action="store_true", help="gather a multi-page web work (TOC) into one raw file")
    parser.add_argument("--cap", type=int, default=40, help="max pages to gather with --follow (default 40)")
    parser.add_argument("--title", help="override the work title (useful with --follow)")
    args = parser.parse_args(argv)

    try:
        if args.follow:
            if not args.source.startswith(("http://", "https://")):
                print("--follow needs a URL", file=sys.stderr)
                return 2
            body, title, hash_text = gather_follow(args.source, args.cap)
            origin = args.source
        else:
            html, origin = load_html(args.source)
            body, title = extract_markdown(html)
            hash_text = body
    except Exception as exc:  # faithful failure, no silent empty output
        print(f"extraction failed: {exc}", file=sys.stderr)
        return 1

    if args.title:
        title = args.title
    slug = args.slug or f"web-page-{slugify(title or Path(args.source).stem)}"
    if not slug or slug in (".", "..") or any(c in slug for c in "/\\:"):
        print(f"invalid --slug '{slug}': must be a bare filename (no path separators)", file=sys.stderr)
        return 2
    args.raw_dir.mkdir(parents=True, exist_ok=True)
    out = args.raw_dir / f"{slug}.md"
    if out.exists() and not args.force:
        print(f"{out.name} already exists — re-ingest with --force, or pass a distinct --slug", file=sys.stderr)
        return 3
    out.write_text(build_source_file(origin, title, hash_text, body), encoding="utf-8")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
