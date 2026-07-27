# Adapter contract

Every `read-*` adapter turns one source of its format into **one normalized markdown file in
`raw/`** (flat). This single contract is
what lets [`wiki-ingest`](../skills/wiki-ingest) stay format-agnostic: it always reads the same
shape, no matter where the content came from.

The **slug is informative** — `<source_kind>-<title-slug>` (e.g. `book-implementing-ddd`,
`web-page-ddd-guide-2026`) — so you can tell what a source is straight from the filename.
`source_kind` is an open, general human category (e.g. `book`, `paper`, `web-page`, `talk`,
`document`, `meeting`), not a file extension or a fixed enum. The full readable title always
lives in the file's `title` frontmatter.

Template: [`assets/source.md.template`](../assets/source.md.template).
Layout: [directory-layout.md](directory-layout.md).

## The division of labor

- **Adapters extract faithfully. They do NOT judge relevance.** An adapter's job is a clean,
  complete, structure-preserving conversion of the source to markdown — nothing is filtered
  or summarized. Deciding what matters *for this wiki* is [`wiki-ingest`](../skills/wiki-ingest)'s
  job, done against the wiki's `SCHEMA.md` charter.
- **One source → one `raw/<slug>.md`** (flat). The slug is stable, informative
  (`<source_kind>-<title-slug>`), and mirrors the eventual source-summary page under `wiki/`.

## Required output

A `raw/<slug>.md` file with this frontmatter (see the template for the full field list):

```yaml
---
type: source
title: Designing Data-Intensive Applications
source_kind: book          # open human category — book | paper | web-page | talk | document | ...
origin: /books/ddia.pdf     # original path or URL
authors: [Martin Kleppmann]
published: 2017
retrieved: 2026-07-15       # when the adapter ran
sha256: <hash of the original source>   # provenance hash, recorded in .manifest.json
structure:                  # the structural map — chapters / sections / timestamps
  - "ch1: Reliable, Scalable, Maintainable Applications"
  - "ch5: Replication"
---
```

Then the **normalized markdown body**:

- Preserve document structure — headings, lists, **tables**, and **code blocks**.
- Keep the structural anchors (chapter/section headings, or timestamps for audio/video) so
  citations can pin a claim to a location (see the citation rules in
  [page-conventions.md](page-conventions.md)).
- **Images**: where the format and backend allow it, download them next to the raw file and
  reference them locally (LLMs read the text first, then view images separately). Where an
  adapter can't (e.g. a boilerplate-stripping web extractor), keep the image references intact
  so the ingesting agent can fetch one if a page turns on it. Don't rely on inline base64.

An adapter script extracts the source's own content — text and images — and stops there. A
source *may* also carry reader discussion (comments, forum replies) whose knowledge is worth
keeping, but the script neither knows whether it exists nor reliably reaches it (it is often
loaded dynamically, after the boilerplate stripper has run). Judging that a source has such
discussion, reading it, and holding it to a stricter bar than the author's text is the
ingesting agent's job, not this contract's — see [`wiki-ingest`](../skills/wiki-ingest).

## Provenance

The `sha256` + `origin` recorded here are the single source of truth for provenance:
`.manifest.json` is **generated** from them by `build_manifest.py` (nothing hand-maintained), so
any wiki page can be traced back to its source, and re-running the adapter later yields a fresh
hash to compare against the recorded one when checking whether a source changed. Record them once
here, correctly, and the manifest follows.

## Adding a new adapter

A new format is a new adapter that satisfies this contract — nothing in `wiki-ingest`
changes. See an existing adapter skill under [`skills/`](../skills) as a model.
