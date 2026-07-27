---
name: wiki-ingest
description: >-
  Use when adding a source to an llm-wiki — a book, article, web page, doc, transcript, or
  anything already normalized into raw/. Distills the source against the wiki's SCHEMA.md
  charter into durable, cross-linked pages. Format-agnostic: any adapter that satisfies the
  adapter contract can feed it. One ingest may touch 10-15 pages. Trigger on "add this to the
  wiki", "ingest this", "process this source", "learn from this".
allowed-tools: Bash(uv run *), WebFetch
---

# wiki-ingest

The core operation. Ingestion is **context-aware distillation** — not copying a source in,
but extracting the maximum useful signal **for this wiki's charter** and structuring it well.

## Preconditions

- The wiki is resolved and `SCHEMA.md` has been read — it is your lens.
- Write pages in the wiki's language and converse in its communication language
  (`SCHEMA.md` → Languages).

## What you're given

Route by what you're handed, then follow the flow below:

- **A source already normalized into `raw/`** (per the
  [adapter contract](../../references/adapter-contract.md)) — this skill is format-agnostic; any
  adapter that satisfies the contract works. Proceed with the flow.
- **A source not yet in `raw/`** — a URL or a file path: run the matching `read-*` adapter to
  normalize it into `raw/` first, then proceed. Delegate a heavy source (a book, a long article)
  to the `wiki-keeper` agent — it is heavy bookkeeping.
- **Free-text knowledge the human states directly** — a fact, correction, or clarification: the
  human is the source, so there is no `raw/` file and no adapter. Fold it straight into the pages
  it concerns via the page-writing steps below and log the operation. If it contradicts a page,
  reconcile with attribution rather than overwriting.

## Large sources — hand off to the map-reduce workflow

A book, or a multi-page work already gathered into one large `raw/` file, is **too big to read in
a single context** — distilling it inline truncates it and under-covers it. When a raw source is
large — its `structure` map lists many chapters, or it runs to tens of thousands of words — hand it
to the bundled **`ingest-large-source`** workflow instead of the inline flow below.

**The main agent launches it — a delegated subagent cannot.** Starting a workflow is not one of a
keeper subagent's tools, so a large source is orchestrated one level up: the main agent starts the
workflow, and the workflow itself fans out the parallel distillers and the single merge-writer.
(This is why a book is never fully handled by delegating to the keeper alone.)

Pass the wiki root and raw slug so it goes straight to work; the workflow **re-discovers both on its
own if the runtime drops the arguments**, so it is robust however it is invoked:

```text
Workflow({ name: "llm-wiki:ingest-large-source", args: { wikiRoot: "<abs wiki root>", rawSlug: "<raw slug>" } })
```

It splits the source by chapter, distills the chapters **in parallel** (each agent reads only its
own line-range against the charter), and a **single writer** merges the results — so coverage
scales with the source and the parallel distillers never collide on the wiki's shared files. Small
sources (an article, a single page) use the inline flow below.

## The flow

Full procedure: [`ingest-workflow.md`](ingest-workflow.md). The gist gives this as an *example*
flow; it is this plugin's default, and a wiki can override it in `SCHEMA.md`:

1. **Read** the normalized source in `raw/`, and read `index.md` to see what already exists.
   If the page has reader discussion (adapters don't fetch it), read that too — it counts,
   under a stricter bar applied when you distill (see the discussion note in
   [`ingest-workflow.md`](ingest-workflow.md)).
2. **Gate the source against the charter.** Judge its subject against Purpose/Scope: ingest it,
   ingest only its in-scope part, or reject it outright — log the rejection and create no pages.
   The per-claim keep/drop still runs on whatever passes.
3. **Surface key takeaways for direction**, then distill. How direction reaches you depends on
   how ingest runs — see [`## Human involvement`](#human-involvement) below.
4. **Write the summary page** for this source (placed in the group that fits it).
5. **Update/create the pages the source touches across the wiki** — each placed in the group
   that fits it. Cross-link with `[[slug]]`; cite claims back to the source. A surfaced
   connection worth keeping becomes its own page too.
6. **Revisit `overview.md` and `synthesis.md`** where this source changes the map or the thesis.
7. **Provenance is automatic** — `.manifest.json` (source hash + origin) is derived from the
   `raw/` frontmatter the adapter wrote and regenerated each turn; nothing to do by hand.
8. **Regenerate the index** — it is derived, so it comes after the pages exist.
9. **Append an entry to `log.md`**.

A rich source can cascade into many pages (Karpathy cites 10-15), and that cascade of
cross-reference edits is exactly the bookkeeping to do thoroughly. Let the material set the
count.

## Selective in scope, deep in what it keeps

Two halves of one rule:

- **Selective** — extract what the `SCHEMA.md` charter cares about, and prefer updating or
  merging an existing page over creating a near-duplicate.
- **Deep** — keep what you take properly: its reasoning, its concrete specifics, and the
  verbatim quotes worth preserving. Distillation makes the material shorter and denser, not
  vaguer.

## Human involvement

Karpathy's role split: the human **curates sources, directs the analysis, asks good
questions, and thinks about what it all means; the LLM does everything else.** The human
directs — it does not co-do the mechanical page work.

That direction enters at different points depending on how ingest runs:

- **Inline / foreground** — live: ingest one source at a time, stay involved, guide emphasis
  as it goes. Karpathy's default preference.
- **In the dispatching task** — explicit steering in the prompt that launched you is first-class
  direction; weigh it alongside `SCHEMA.md`.
- **Delegated (keeper subagent), charter alone** — front-loaded: with no task-specific steering,
  follow the emphasis written into `SCHEMA.md` and report takeaways in the returned summary for
  review afterward.

Batch, low-supervision ingest is equally valid; set it as this wiki's preference in
`SCHEMA.md` workflow customizations.

## Guardrails

Full list in [`ingest-workflow.md`](ingest-workflow.md#guardrails). The load-bearing ones:
`raw/` is immutable (re-run the adapter, don't edit it); keep pages atomic
([page conventions](../../references/page-conventions.md)); handle images by reading the
extracted text first, then viewing the downloaded images separately.
