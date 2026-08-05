---
title: "Source Summary — Architecture Patterns with Python (Cosmic Python), Preface"
category: building-blocks
summary: The preface of Percival & Gregory's "Cosmic Python"; largely meta, its only in-scope nugget is the book's DDD thesis. No concept pages distilled — flagged as a high-value candidate for full ingestion.
tags: [summary, ddd, candidate-source, cosmic-python]
sources: [web-page-cosmic-python-preface]
created: 2026-07-25
updated: 2026-07-26
---

> **Update (2026-07-26):** the full ingestion recommended below is now underway. The book's Introduction
> through Chapter 5 have been distilled — see [[web-page-cosmic-python-book]] for the full source summary
> and the concept pages it produced ([[domain-model]], [[repository]], [[dependency-inversion-principle]],
> [[big-ball-of-mud]], the [[application-service|service layer]], and more).

**Source:** Harry Percival & Bob Gregory, *Architecture Patterns with Python* ("Cosmic Python",
O'Reilly), **Preface**. Origin: <https://www.cosmicpython.com/book/preface>. Raw extraction:
`raw/web-page-cosmic-python-preface.md`.

## What it is

The front matter of a well-regarded book that implements DDD and event-driven architecture in
Python. The preface introduces the authors, the running example domain (MADE.com, a furniture
e-commerce company optimising a global supply chain), the book's motivation, a chapter map, and
the usual O'Reilly conventions/acknowledgements.

## Relevance verdict — accepted partly (thin)

A preface is mostly meta, and this one is no exception; held against the charter, almost nothing is
distillable **pattern** knowledge. Honestly, the in-scope signal is two things, neither of which
justifies a concept page:

1. **The book's DDD thesis** — *"Domain-driven design (DDD) asks us to focus our efforts on
   building a good model of the business domain, but how do we make sure that our models aren't
   encumbered with infrastructure concerns and don't become hard to change?"* (raw L82). This is
   the same keep-the-model-clean concern that underlies the [[anemic-domain-model]] layering
   discussion and this wiki's [[synthesis]]. Recorded here; not worth a standalone page from a
   preface alone.
2. A useful caveat that most of the patterns — **including the event-driven material — apply to a
   monolith, not only to microservices** (raw L86), which echoes the monolith point on
   [[bounded-context]].

**No concept pages were created from this source**, deliberately: the preface *names* the patterns
the book will teach but does not teach any of them (no definitions, decision rules, trade-offs, or
failure modes), so distilling one would mean padding.

## Dropped as out of scope / meta

Author bios and origin story, the MADE.com narrative beyond one identifying line, the TDD material,
specific Python tech choices (Flask, SQLAlchemy, pytest, Docker, Redis), typographical
conventions, licensing, O'Reilly boilerplate, and acknowledgements.

## Candidate for full ingestion

This is the summary's real value: the preface's **chapter map** shows the book covers a stack of
in-scope DDD patterns this wiki does **not** yet have pages for —

- Domain modelling & DDD (ch. 1, 2, 7)
- **Repository**, **Service Layer**, **Unit of Work** (ch. 2, 4, 5)
- Choosing the right **aggregate** and its relation to data integrity (ch. 7) — would extend
  [[aggregate]]
- **Domain Events**, **Message Bus**, **Handlers**; commands vs. events (ch. 8–11) — would extend
  [[domain-event]]
- **CQRS** (ch. 12) and Dependency Injection (ch. 13)

Recommendation: ingest the relevant chapters (1, 2, 4, 5, 7, 8–11) with `read-book` when the source
is available. That would fill the wiki's biggest current gaps — repositories, service layer, and
unit of work have no coverage at all.

## Reader discussion

None — a static book page with no comment thread.
