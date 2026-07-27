# llm-wiki

An LLM-maintained knowledge wiki for Claude Code, implementing
[Andrej Karpathy's llm-wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
(the source of truth — mirrored in [`references/karpathy-llm-wiki.md`](references/karpathy-llm-wiki.md)).

Instead of re-searching raw documents on every question (RAG), an LLM **incrementally
builds and maintains** a persistent, cross-linked markdown wiki. Ingestion is
**context-aware distillation**: extract only what matters *for this wiki's charter*, and
structure it well.

## Three layers (Karpathy)

| Layer | Here | Mutable? |
|-------|------|----------|
| **Raw sources** | `raw/` — normalized markdown produced by adapters | immutable |
| **The wiki** | `wiki/` — grouped pages plus the generated catalog | LLM-maintained |
| **The schema** | `SCHEMA.md` at the wiki root — charter + the lens for ingestion | co-evolved |

The operation log lives at the wiki root beside `SCHEMA.md`. Full shape:
[`references/directory-layout.md`](references/directory-layout.md).

## Components

```text
llm-wiki/
├── agents/wiki-keeper.md      # the expert agent that owns & maintains the wiki
├── skills/
│   ├── wiki-init/             # quick-start: scaffold a wiki and fill its charter
│   ├── wiki-ingest/           # context-aware distillation of a normalized source
│   ├── wiki-query/            # retrieval + synthesis, answered with citations
│   ├── wiki-scout/            # charter-driven source candidates from the web, for approval
│   ├── wiki-lint/             # health checks + the deterministic maintenance scripts
│   ├── wiki-serve/            # local browser preview of the wiki
│   └── read-*/                # format adapters: one per source format -> normalized raw/
├── references/                # shared rulebook (read on demand)
├── assets/                    # templates stamped into a new wiki
└── hooks/                     # write approval for wiki files; index regen + lint each turn
```

## Hooks

- **Writes to a wiki's own files are approved automatically.** One ingest touches many files,
  so a `PreToolUse` hook approves writes that land on `wiki/`, `raw/`, `SCHEMA.md`, `log.md`,
  the manifest and the configs — and stays silent for every other path, including elsewhere in
  a project whose root is also the wiki root. Your `deny` rules still take precedence, and the
  hook is listed in `/hooks`.
- **The index is regenerated and mechanically linted at the end of each turn**, so the catalog
  never drifts. Both no-op outside a wiki.
- **Requires [`uv`](https://docs.astral.sh/uv/) on `PATH`.** The hook scripts and adapters run
  via `uv run`; without it the per-turn index/lint hooks error and the write-approval hook goes
  silent (ingest falls back to prompting per file). Nothing is destroyed — the plugin just
  degrades — but install `uv` for it to work as intended.

## Operations

Karpathy's three operations — Ingest, Query, Lint — plus Scout, this plugin's own addition:

- **Ingest** — a source → distilled, cross-linked pages, index + log updated.
- **Query** — search the wiki, synthesize a cited answer; valuable answers can be filed back as pages.
- **Lint** — find contradictions, stale claims, orphans, broken links; and, generatively,
  propose new questions and sources. Two triggers: automatic (Stop hook, deterministic/mechanical)
  and manual (`wiki-lint` skill, deep/semantic).
- **Scout** *(this plugin's addition)* — read the charter, find coverage gaps, fan out parallel
  web searchers, and propose ranked source candidates for approval (never ingests).

## Deviations from Karpathy's gist

This plugin follows the [gist](references/karpathy-llm-wiki.md) but makes a few deliberate
choices it does not spell out:

- **`raw/` holds adapter-normalized markdown, not the human's original files.** The gist's raw
  layer is the source material as collected (PDFs, pages, notes), kept immutable. Here each
  source is normalized to one markdown file so ingest stays format-agnostic; the untouched
  original stays wherever the human keeps it, and each raw file's `origin` points back to it.
- **Page frontmatter is mandatory.** The gist keeps page structure loose; here every page carries
  required frontmatter (category, tags, sources, dates) because the mechanical lint and the
  generated index depend on it.
- **Outputs are markdown-centric.** The gist lists richer query outputs (tables, slide decks,
  charts); here answers are markdown pages (which can hold tables). Richer output formats are
  out of scope.
- **The schema lives in `SCHEMA.md`, not the host agent's instruction file.** The gist names the
  schema as e.g. `CLAUDE.md`/`AGENTS.md`; here the charter is a dedicated `SCHEMA.md` at the wiki
  root, so a wiki can nest inside a project that already has its own agent instructions, and so
  the same file doubles as the wiki-root marker.
- **Scout is an added operation.** The gist's operations are ingest, query, and lint; this plugin
  adds a charter-driven source-scouting step that proposes candidates and never ingests, to assist
  the sourcing the gist leaves to the human.

## Usage

### Standalone

Dispatch the **`wiki-keeper`** agent to build and maintain a wiki in the current project:

- *"Ingest this PDF into the wiki"* → keeper runs the matching adapter (`read-book`) then `wiki-ingest`.
- *"Lint the wiki" / "reorganize these pages"* → keeper runs `wiki-lint`, regenerates the index.

Ask domain questions **inline** with the `wiki-query` skill (cited answers) — no need to dispatch the agent.

### From a domain-expert agent

This plugin is the shared machinery; **domain experts live in their own plugins and depend on it.**
Each expert points at its own wiki (its own `SCHEMA.md` root). An expert works through three verbs:

| Verb | How | Where it runs |
|------|-----|---------------|
| **orient / answer** | read its wiki, answer with citations, via `wiki-query` | inline, in the expert's context |
| **grow** | add a source / extend the base, by **delegating to `wiki-keeper`** | isolated context (keeps heavy ingest out of the expert) |
| **maintain** | lint / reorganize, by delegating to `wiki-keeper` | isolated context |

An expert grows its base **on request** ("add this source") today; **automatically** (watch an
inbox, capture on session end) is planned via hooks / a background ingester.

