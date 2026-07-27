---
name: read-html
description: >-
  Adapter: convert a web page or local HTML file into a normalized raw/ source file for an
  llm-wiki. Strips boilerplate to clean markdown with Trafilatura. Faithful extraction only —
  no relevance filtering (that is wiki-ingest's job). Trigger when a URL or HTML file is a
  source to add to the wiki.
allowed-tools: Bash(uv run *)
---

# read-html

An adapter. Turns one URL or `.html` file into `raw/<slug>.md` per the
[adapter contract](../../references/adapter-contract.md), using Trafilatura to extract the
main article as markdown (it outputs markdown directly — no markdownify needed).

## Run

```bash
uv run --no-project --with trafilatura \
  "${CLAUDE_PLUGIN_ROOT}/skills/read-html/scripts/extract.py" \
  <url-or-file.html> --raw-dir <wiki-root>/raw [--slug NAME]
```

### Multi-page works (a web book / doc with a table of contents)

When the source is a whole work whose chapters live at separate URLs (a web book, a docs site),
add `--follow` to gather it into **one** raw file — then the ingest step treats it like a book.
The adapter follows same-domain links under the start URL's path (never leaving that prefix or the
domain), concatenates each page as its own section, and builds a chapter structure map:

```bash
uv run --no-project --with trafilatura \
  "${CLAUDE_PLUGIN_ROOT}/skills/read-html/scripts/extract.py" \
  <toc-or-start-url> --raw-dir <wiki-root>/raw --follow [--cap 40] [--title "Work Title"] [--slug NAME]
```

A large gathered work then routes to the large-source ingest workflow, same as any book.

## Notes

- Handles both remote URLs and local HTML files.
- Trafilatura removes boilerplate aggressively; if it strips wanted content, the extraction
  can be tuned (`favor_recall`) — adjust the script if a source needs it.
- Faithful extraction only: the adapter does not decide what matters for the wiki.
- This script extracts the article body and stops there; it does not fetch reader comments
  (a boilerplate stripper misses threads loaded dynamically anyway). Whether a page has
  discussion worth reading is your call as the ingesting agent — see the discussion step in
  [`wiki-ingest`](../wiki-ingest).
