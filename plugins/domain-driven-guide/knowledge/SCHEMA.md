# Domain-Driven Design — SCHEMA

<!--
This file is the CHARTER and the ROOT MARKER: its presence marks this directory as a wiki
root, and its contents are the lens ingest uses to decide what to keep.

Per Karpathy, the schema is "what makes the LLM a disciplined wiki maintainer rather than a
generic chatbot" — and it is a LIVING document you and the LLM co-evolve as you learn what
works for this domain. The generic structure/conventions/workflows live in the llm-wiki
plugin; this file holds the DOMAIN-SPECIFIC charter and any local overrides. Fill every
section, then keep refining it.
-->

## Purpose

A team reference for Domain-Driven Design's tactical and strategic patterns — entities, value
objects, aggregates, repositories, domain services, and domain events on the tactical side;
bounded contexts, context mapping, ubiquitous language, and subdomains on the strategic side.
Serves the team when designing or reviewing system/domain models, so pattern usage stays
consistent and decisions are traceable to the reasoning behind them, not just habit.

## Scope — the ingestion lens

Ingest judges every candidate fact from a source against this. Be specific — this is what
separates signal from noise for THIS wiki.

**In scope (keep):**
- Tactical building blocks: entities, value objects, aggregates (and aggregate boundary rules),
  repositories, domain services, domain events, factories.
- Strategic design: bounded contexts, context mapping patterns (shared kernel, customer-supplier,
  conformist, anticorruption layer, etc.), ubiquitous language, subdomain classification (core,
  supporting, generic).
- Decision rules and heuristics for when/why to apply a given pattern.
- Trade-offs and pros/cons of each pattern choice.
- Common failure modes / misapplications (e.g. anemic domain models, oversized aggregates,
  leaky bounded contexts).
- Concrete code-level examples showing a pattern correctly applied.

**Out of scope (drop):**
- Generic OOP or architectural patterns not specifically tied to DDD (e.g. plain CRUD design,
  GoF patterns discussed outside a DDD context).
- Framework/tooling-specific tutorials that aren't about the DDD concept itself.
- Organizational/Team Topologies content, unless directly used to justify a bounded context split.

## Domain extraction schema

From each source, extract these kinds of knowledge (tailor to the domain — this overrides
the generic default):

- Pattern definitions (what it is, precisely).
- Decision rules / heuristics (when to use it, when not to).
- Trade-offs (what you gain, what you give up).
- Failure modes (how this pattern is commonly misapplied, and the symptom that reveals it).
- Code-level examples / artifacts illustrating correct application.

## Grouping principle

Pages live in subdirectories of `wiki/`, named by this domain's own topics, so the folder tree
is self-documenting (e.g. `strategic-design/`, not `concepts/`). Rather than enumerate every
group, state the **principle** by which this wiki splits pages into groups; new groups are
created as topics appear, and the emerging tree shows what exists. A page's `category`
frontmatter equals its folder name.

Group by pattern category/family, finer-grained than a flat strategic-vs-tactical split — e.g.
`building-blocks/` (entities, value objects, aggregates, repositories, domain services),
`context-mapping/` (bounded contexts, the ubiquitous language they scope, and the context-mapping
patterns between them), `aggregate-design/` (aggregate boundary rules and invariant enforcement
specifically, if it grows large enough to warrant its own folder), `event-design/` (domain events,
event storming outputs), `anti-patterns/` (DDD failure modes and misapplications — anemic domain
model, oversized aggregates, leaky bounded contexts). A page goes where a reader hunting for that
specific pattern family would look.


## Languages

- **Wiki language:** English — pages, summaries, and synthesis are written in English.
- **Communication language:** Russian — the LLM converses in Russian (questions, surfaced
  takeaways, reports).

## Conventions

- Pages, frontmatter, and `[[wikilinks]]` follow the `llm-wiki` plugin's page conventions.
- Link style: `[[slug]]` (Obsidian-style).

## Workflow customizations

Per-wiki overrides to the plugin's default ingest / query / lint behavior. Leave empty to
use the defaults; add rules here as you and the LLM discover what this domain needs. E.g.:

- Ingest: always write a standalone source summary page for every ingested source, in addition
  to distilling its claims into the relevant topic pages — don't fold a source in silently.

## Notes

Key sources not yet decided — the canonical starting points for this domain are typically Eric
Evans' "Domain-Driven Design" (the original text) and Vaughn Vernon's "Implementing
Domain-Driven Design", but nothing is committed yet. Update this section once sources are
chosen (via `wiki-scout` or direct ingest).

<!-- Co-evolution log: record decisions about how THIS wiki is run as they emerge. -->

