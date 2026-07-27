---
name: read-book
description: >-
  Adapter: convert a PDF or EPUB book into a normalized raw/ source file for an llm-wiki.
  Faithful, structure-preserving extraction only — it does NOT judge relevance (that is
  wiki-ingest's job). Uses Docling (accurate: tables/code) or pymupdf4llm (fast, text-layer
  PDFs). Trigger when a book/PDF/EPUB is a source to add to the wiki.
allowed-tools: Bash(uv run *)
---

# read-book

An adapter. Turns one PDF/EPUB into `raw/<slug>.md` per the
[adapter contract](../../references/adapter-contract.md) — nothing filtered, structure
preserved, provenance recorded.

## Backends

- **Docling** (default) — best fidelity: tables and code blocks preserved; handles EPUB.
  Heavy: pulls PyTorch and downloads models (~GB) on first run.
- **pymupdf4llm** (`--fast`) — no models, very fast; best for plain text-layer PDFs.

## Run

Dependencies install on demand via `uv` (keeps the base plugin light):

```bash
# accurate (Docling)
uv run --no-project --with docling \
  "${CLAUDE_PLUGIN_ROOT}/skills/read-book/scripts/extract.py" \
  <source.pdf|epub> --raw-dir <wiki-root>/raw

# fast (pymupdf4llm)
uv run --no-project --with pymupdf4llm \
  "${CLAUDE_PLUGIN_ROOT}/skills/read-book/scripts/extract.py" \
  <source.pdf> --raw-dir <wiki-root>/raw --fast
```

Optional: `--slug <name>` (defaults to a slug derived from the filename).

## Contract reminder

Output is `raw/<slug>.md`: frontmatter (`type: source`, `source_kind: book`, `origin`,
`sha256`, `structure` map from headings) + the normalized markdown body. Extract faithfully;
do not summarize or drop content.
