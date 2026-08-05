---
title: "Source Summary — Implementing Domain-Driven Design (Vaughn Vernon)"
category: foundations
summary: Vernon's canonical DDD text ("the red book"), ingested end to end via the large-source workflow — strategy and architecture (Ch. 1–4) and the full tactical pattern language (Ch. 5–12: Entities, Value Objects, Services, Domain Events, Modules, Aggregates, Factories, Repositories) distilled across 97 pages of the wiki.
tags: [summary, book, ddd, strategic-design, tactical-design]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

**Source:** *Implementing Domain-Driven Design* by Vaughn Vernon (Addison-Wesley, 2013;
ISBN 978-0-321-83457-7) — the widely-cited "red book" that operationalizes Eric Evans' DDD with
concrete code, the running SaaSOvation case study, and first-class treatment of Domain Events.
Raw extraction: `raw/book-implementing-ddd-vaughn-vernon.md`.

## Relevance verdict — fully in scope

The book *is* this wiki's charter subject. It was ingested with the **large-source (map-reduce)
workflow**: chapters distilled in parallel against the `SCHEMA.md` charter lens, then merged by a single
writer. The ingest covers the **whole book** — front matter and strategy through the full tactical
pattern language — and **97 pages across the wiki draw on it**.

## What was distilled, by chapter

- **Front matter / Ch. 1 (Getting Started)** → [[domain-driven-design]], [[when-to-use-ddd]],
  [[domain-model]], and extended [[ubiquitous-language]], [[anemic-domain-model]], [[ddd-lite]].
- **Ch. 2 (Domains, Subdomains, and Bounded Contexts)** → [[subdomain]], [[core-domain]],
  [[problem-space-and-solution-space]], [[bounded-context-sizing]], [[blending-models-in-one-context]],
  and extended [[bounded-context]], [[ubiquitous-language]].
- **Ch. 3 (Context Maps)** → [[context-map]], [[upstream-downstream]], [[partnership]],
  [[shared-kernel]], [[customer-supplier-development]], [[conformist]], [[anticorruption-layer]],
  [[open-host-service]], [[published-language]], [[separate-ways]], [[big-ball-of-mud]],
  [[bounded-context-autonomy]].
- **Ch. 4 (Architecture)** → [[architecture-selection]], [[layered-architecture]],
  [[dependency-inversion-principle]], [[hexagonal-architecture]], [[application-service]], [[cqrs]],
  [[event-driven-architecture]], [[long-running-process]], [[event-sourcing]], [[rest-and-ddd]].
- **Ch. 5 (Entities)** → extended [[entity]], plus [[entity-identity-generation]],
  [[surrogate-identity]], [[entity-validation]], [[object-roles]], and extended [[anemic-domain-model]].
- **Ch. 6 (Value Objects)** → extended [[value-object]], plus [[whole-value]],
  [[side-effect-free-function]], [[standard-type]], [[value-objects-for-integration]],
  [[value-object-persistence]], and the [[data-model-leakage]] anti-pattern.
- **Ch. 7 (Services)** → [[domain-service]], [[domain-service-separated-interface]],
  [[application-service-vs-domain-service]].
- **Ch. 8 (Domain Events)** → [[domain-event]], [[domain-event-publisher]],
  [[domain-event-contract-design]], [[domain-event-enrichment]], [[event-store]],
  [[notification-log]], [[event-de-duplication]].
- **Ch. 9 (Modules)** → [[modules]], [[module-naming-conventions]], [[module-before-bounded-context]].
- **Ch. 10 (Aggregates)** → [[aggregate]] and the whole `aggregate-design` group:
  [[model-true-invariants-in-consistency-boundaries]], [[design-small-aggregates]],
  [[reference-other-aggregates-by-identity]], [[eventual-consistency-between-aggregates]],
  [[reasons-to-break-aggregate-rules]], [[aggregate-information-hiding]],
  [[aggregate-optimistic-concurrency]].
- **Ch. 11 (Factories)** → [[factory]], [[factory-method-on-aggregate-root]], [[factory-on-service]].
- **Ch. 12 (Repositories)** → [[repository]], [[collection-oriented-repository]],
  [[persistence-oriented-repository]], [[repository-vs-dao]], [[repository-type-hierarchies]],
  [[repository-only-persistence]], [[testing-repositories]], [[transaction-management]].

## Coverage — complete

Every core tactical building block now has its own page, so the earlier "forthcoming" gap is closed.
Appendix A's Event Sourcing / CQRS implementation material is distilled under [[event-sourcing]],
[[event-store]], [[functional-event-sourcing]] and [[cqrs]]. The raw extraction remains on disk for any
future deepening, but no pattern from the book is missing a page.

## How to read it

Authoritative and mainstream: this is the standard practical companion to Evans. Its prescriptions are
deliberately rules-of-thumb ("what usually works well or the thing to try first"), not laws — Evans
says as much in the Foreword. The SaaSOvation case study (Collaboration, Identity & Access, and Agile
PM contexts) recurs throughout and grounds most examples on the strategic pages.
