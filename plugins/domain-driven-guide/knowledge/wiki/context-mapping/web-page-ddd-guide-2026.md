---
title: "Source Summary — DDD: полный гайд по моделированию домена в 2026 году"
category: context-mapping
summary: A broad practitioner intro to DDD (Habr / OTUS, 2026) covering ubiquitous language, bounded contexts, and the tactical building blocks with Java code; accepted in full for its DDD content, marketing dropped.
tags: [summary, ddd, strategic-design, building-blocks, bounded-context]
sources: [web-page-ddd-guide-2026]
created: 2026-07-25
updated: 2026-07-25
---

**Source:** Сергей Прощаев, *"Domain-Driven Design: полный гайд по моделированию домена в 2026
году"* — a Russian-language Habr article published under the OTUS company blog. Origin:
<https://habr.com/ru/companies/otus/articles/994158/>. Raw extraction:
`raw/web-page-ddd-guide-2026.md`.

## What it is

An opinionated, example-driven introduction to DDD aimed at practitioners: it deliberately skips
the Evans/Vernon theory and instead argues, through two real-world war stories and Java code
snippets, how DDD keeps a growing codebase from collapsing. It spans both strategic design
(ubiquitous language, bounded contexts) and the core tactical building blocks (value object,
entity, aggregate), plus a short note that modelling is a continuous dialogue, not a one-off
drawing.

## Relevance verdict — accepted in full (in-scope content)

The article is squarely on-charter — tactical *and* strategic DDD patterns — and its DDD substance
was distilled across the wiki:

- [[ubiquitous-language]] — language as living, code-bound communication (not a glossary); the
  "Order = invoice / boxes / DB row" mismatch; the "is it named the same in code?" test.
- [[bounded-context]] — slice by context not technology; the FinTech shared-`Client` failure; and
  the standout case that context boundaries pay off **inside a monolith** (the acquiring-system
  firefighting story).
- [[value-object]] — self-validating, identity-free objects; the `Email` value object worked
  example.
- [[entity]] — identity that persists across attribute change; cohesion around identity/lifecycle.
- [[aggregate]] — *extended* an existing page with the aggregate-root framing, the `Order` /
  `OrderItem` example, and the rule that other aggregates are referenced by ID only.
- [[anemic-domain-model]] — the guide independently restates Fowler's warning, recorded there as
  corroboration.

## What was set aside, and why

- **Marketing / teaser content** — the OTUS course promotion, free-lesson schedule, and the "next
  article will cover repositories and domain events" teaser: advertising, not knowledge.
- **The Saga / compensating-transaction mechanism** and the ports-and-adapters refactor in the
  monolith story — general architectural patterns, kept only as the *mechanism* that realised the
  context boundary (noted on [[bounded-context]]), not given their own pages per the charter.
- The "modelling is a dialogue, not drawing" point (raw L156–L160) was folded as context into
  [[bounded-context]] and [[ubiquitous-language]] rather than made a standalone page — it is a
  stance, not a distinct pattern with its own decision rules.

## How to read it

A solid, correct *introduction*: the definitions and the boundary reasoning align with mainstream
DDD, and the two case studies are its real value. Treat it as a starting map, not a deep reference
— it explicitly covers only "the tip of the iceberg" (language, contexts, aggregates) and leaves
repositories, domain services, and domain events to later instalments. Slug note: extracted with an
explicit `--slug` because the adapter does not transliterate Cyrillic, so the auto-slug from the
Russian title would have been a meaningless hash.

## Reader discussion

The article has a comment thread (JavaScript-loaded; not captured by the HTML adapter — fetched
separately from the comments endpoint). Held to a stricter bar than the author's own text, one
point cleared it:

- **Espleth** — argues the monolith performance story needs no DDD (plain async decomposition would
  do), and that a field hardcoded in 50 places is basic code quality, not a modelling failure → a
  reasoned critique of the case studies, recorded as a counterpoint on [[bounded-context]].

Dropped as not clearing the bar: **dproshchaeva** and **ivvi** (both merely restate the article's
own points about the ubiquitous language failing to reach the code), and tangential remarks from
andreygn and LeoKudrik.
