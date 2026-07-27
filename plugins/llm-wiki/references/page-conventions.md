# Page conventions

How a single wiki page is written. Layout context: [directory-layout.md](directory-layout.md).
Where raw sources come from: [adapter-contract.md](adapter-contract.md).

## Page kinds

Page kinds fall into two classes.

**Many-of, atomic, in domain groups** — summaries, entity pages, concept pages, comparisons:

| Kind | What it holds |
|---|---|
| **summary** | One per ingested source: what it is, its thesis, what it covers, how to read it. |
| **entity** | One specific named thing — a person, system, org, product, event. |
| **concept** | One idea or mechanism, defined and situated. |
| **comparison** | How two or more things differ and when to reach for each. Often a filed-back query answer. |

These are **shapes, not locations**: each is an ordinary page living in the domain group it is
*about*, with `category` equal to that folder and its kind in `tags`. A concept page and a
comparison on the same topic sit side by side. The list is open — when the domain calls for a
shape that isn't here (a case study, a decision record), invent it and record it in `SCHEMA.md`
so it stays consistent.

**One-of, non-atomic, at `wiki/` root** — an overview and a synthesis:

- **`overview.md`** — the entry point: what this wiki covers and how it is organized. A map.
- **`synthesis.md`** — the evolving thesis: what it all *means* taken together. Each new source
  strengthens or challenges it, and it already reflects everything you've read. A position,
  not a map.

Both are single living documents. Whether a wiki needs both is a domain call — a reference wiki
may want only the overview; a research wiki lives on its synthesis.

They are ordinary link targets, so `[[overview]]` and `[[synthesis]]` resolve like any page.
Being entry points, nothing is required to link *to* them and lint never counts them as orphans.

## Atomicity

**One page = one thing.** A page covers a single, self-contained unit of knowledge. When a
page starts covering several distinct things, split it; when two pages describe the same thing
under different names, merge them. The gist prizes "the connections between documents as valuable
as the documents themselves" — atomic pages make those connections explicit.

When splitting and merging pull opposite ways — a pattern and the procedure for applying it,
say — split if each part would be cited on its own and carry its own inbound links; keep them
together if one is only ever read in the context of the other.

## Location & slug

- File: `wiki/<group>/<slug>.md` — the page lives in its group's subdirectory.
- The **slug is the page's identity**: lowercase kebab-case, stable, meaningful
  (`raft-consensus`, not `page-2`), and **unique across all groups**. Renaming a slug means
  updating every `[[link]]` to it.
- **Disambiguate homonyms** with qualified slugs: `mercury-planet` vs `mercury-element`,
  `spring-framework` vs `spring-season`.

## Groups

Pages are grouped into subdirectories of `wiki/`, one directory per group. **Groups are not
predefined — the keeper designs them to fit the domain and evolves them as the wiki grows.**

**Name groups by the domain's own topics**, so the page tree is self-explanatory and
navigable — not by generic page-type words like `concepts/` or `pages/`. (A security wiki
might grow `authentication/`, `threat-models/`, `crypto/`; a DDD wiki `strategic-design/`,
`tactical-patterns/`, `anti-patterns/`.) This wiki's grouping *principle* lives in its
`SCHEMA.md`; the live set of groups is the folder tree itself, surfaced in `index.md`.

**Placement principle:** put each atomic page in the group where a reader would look for it.
When a page belongs to a distinct topic no existing group covers, **create a new group** (a new
subdirectory), keeping `SCHEMA.md`'s grouping principle current — never force a page into a
group it doesn't fit.

**Folders follow topics; the catalog follows folders.** A page's folder is decided by what it
is *about*, and `index.md` derives its sections from the folders that exist. A page's *kind*
is recorded in `tags`, so it stays queryable without shaping the tree.

## Frontmatter (required on every atomic page)

```yaml
---
title: Raft Consensus
category: <group>        # MUST equal this page's folder name (its group)
summary: One-sentence description used in the generated index.
tags: [distributed-systems, consensus]
sources: [book-designing-data-intensive-applications]   # bare slugs of source pages / raw
created: 2026-07-15
updated: 2026-07-15
---
```

- `category` **must equal the folder name** the page lives in (lint enforces this).
- `updated` drives staleness checks in lint.
- `sources` lists **bare slugs** (not wikilinks); the body uses `[[wikilinks]]`.
- The non-atomic root pages (`overview`, `synthesis`) are exempt: they belong to no group, so
  `category` and the required-field check don't apply to them.

## Body & cross-references

- Open with a clear, self-contained lead paragraph (encyclopedic definition).
- **Carry the source's substance.** Distilling makes the material shorter and denser, not
  vaguer: keep the reasoning behind a claim and its concrete specifics — numbers, mechanisms,
  worked examples, trade-offs, limits. The page should stand on its own for the reader.
- **Quote the source directly** where a definition or a load-bearing claim carries the weight:
  a short blockquote with its citation.
- **Cross-link liberally** with `[[slug]]` in the body. A page with no inbound links is an
  orphan (lint flags it).
- Link out for tangential concepts, and explain this page's own subject here in full.

## Citations

Claims that come from a source must be traceable to it. Cite the source page/`raw/` file,
and where practical pin the location (e.g. a line range `L120-L138` in the raw file, or a
chapter/section). This lets lint and the reader verify a claim against its origin, and lets
`wiki-query` answer *with citations* rather than from general knowledge.

Where the extraction itself is corrupted — OCR noise, lost line breaks — a literal quote would
be unreadable. Transcribe it into legible form, say that you transcribed it, and point at the
source page's extraction caveat.

## Filing query answers back

A valuable query answer — a comparison, an analysis, a discovered connection — becomes an
ordinary page of whatever kind fits it, in the group it belongs to.
