---
title: "Source Summary — Architecture Patterns with Python (Cosmic Python)"
category: foundations
summary: Percival & Gregory's DDD-in-Python book ("Cosmic Python"), now ingested end to end via the large-source workflow — the Big Ball of Mud problem, the Dependency Inversion Principle, the tactical building blocks, the message-bus/events architecture, CQRS, dependency injection, and the epilogue/appendices on refactoring legacy systems, all around the MADE.com allocation example.
tags: [source-summary, source, cosmic-python, ddd, python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

**Source:** Harry Percival & Bob Gregory, *Architecture Patterns with Python* ("Cosmic Python", O'Reilly). Origin: <https://www.cosmicpython.com/book/> (full text, front matter through Appendix E). Raw extraction: `raw/web-page-cosmic-python-book.md`. Companion to the [[web-page-cosmic-python-preface]] summary of the same book's preface. Ingested via the large-source workflow in three batches.

## What the book is

A well-regarded, worked treatment of DDD and event-driven architecture implemented in Python, by **Harry Percival** (author of *Test-Driven Development with Python*) and **Bob Gregory**, both engineers at MADE.com. Its stated aim is to "introduce several classic architectural patterns and show how they support TDD, DDD, and event-driven services" and to "serve as a reference for implementing them in a Pythonic way." The authors stress these patterns "are mostly new to the Python world" but not new in themselves, and that the book "isn't a replacement for the classics in the field such as Eric Evans's *Domain-Driven Design* or Martin Fowler's *Patterns of Enterprise Application Architecture*." It does not merely name the tactical building blocks — it builds them chapter by chapter around one running example.

## The example domain (MADE.com allocation)

Every pattern is illustrated with MADE.com, "a European ecommerce company that sells furniture online" that "operates a global supply chain of freight partners and manufacturers." The business problem is a timing/optimization balancing act — deliver stock to warehouses so "we don't have unsold goods lying around," ideally shipping the sofa the day it is bought, against three-month container-ship lead times, damage, delays, and amended orders. The response is a [[domain-model]] of *allocation*: an `OrderLine` ([[value-object]]) allocated against a `Batch` ([[entity]]) of stock, later clustered under a `Product` [[aggregate]] per SKU, with `OutOfStock` as a [[domain-exception]].

## Three tools for managing complexity

The book organizes itself around three complexity-management tools: *Test-driven development* (mostly out of scope for this DDD wiki except where it shapes model isolation); *Domain-driven design* — "building a good model of the business domain" kept free of infrastructure concerns; and loosely coupled *(micro)services integrated via messages*. An important caveat, echoing [[bounded-context]]: the patterns are "absolutely applicable in a monolithic architecture" and do not require microservices.

## Distilled in this ingest (front matter → Appendix E)

**Part I — Building an architecture to support domain modeling.**

- **Introduction.** Establishes the *problem* (the [[big-ball-of-mud]] as "the natural state of software," diagnosed by "sameness of function") and the *one principle* the rest of the book applies (the [[dependency-inversion-principle]], the SOLID "D"). Introduces the [[domain-model]] as the pattern for the business layer.
- **Ch. 1, Domain Modeling** — the [[domain-model]] elicited in the [[ubiquitous-language]]; [[entity]], [[value-object]], [[domain-service]], [[domain-exception]].
- **Ch. 2, Repository Pattern** — the [[repository]] as an in-memory-collection illusion; [[persistence-ignorance]].
- **Ch. 3, Coupling and Abstractions** — [[coupling-and-cohesion]], [[abstractions]], [[decoupling-domain-logic-from-infrastructure]].
- **Ch. 4, Service Layer** — the [[application-service|service layer]] and its distinction from a [[domain-service]].
- **Ch. 5, TDD in High Gear and Low Gear** — [[test-coupling-vs-design-feedback]], [[domain-model-tests-as-living-documentation]], [[expressing-the-service-layer-in-primitives]].
- **Ch. 6, Unit of Work** — the [[unit-of-work]] transaction boundary that decouples service from data layer.
- **Ch. 7, Aggregates and Consistency Boundaries** — [[aggregate]] and the operational [[aggregate-consistency-boundary]] rule.

**Part II — Event-driven architecture.**

- **Ch. 8–11, Domain Events / Message Bus / Commands and Events / going async** — [[domain-event]] recorded on the aggregate and dispatched by the [[message-bus]]; [[commands-and-events]]; [[internal-vs-external-events]] and [[event-driven-integration]]; the [[infrastructure-leaking-into-the-domain-model]] anti-pattern the recorded-not-raised style avoids.
- **Ch. 12, CQRS** — [[command-query-separation]] scaled up to [[cqrs]]; the dedicated [[read-model]] and the [[reusing-the-write-model-for-reads]] anti-pattern.
- **Ch. 13, Dependency Injection (and Bootstrapping)** — explicit dependencies and the Composition Root (extending [[dependency-inversion-principle]]); [[ports-and-adapters]] as the general form of the Repository.

**Epilogue — "How do I get there from here?"** — applying the patterns to legacy systems: the [[big-ball-of-mud]] symptoms up close, [[refactoring-toward-ddd]] in place, the [[strangler-fig-pattern]] for wholesale replacement, and [[collaborative-domain-modeling]] as the recommended first step.

**Appendices.** B (Summary Diagram and Table) — capsule definitions folded into [[entity]], [[value-object]], [[aggregate]], [[repository]], [[domain-event]]. C (Do Everything with CSVs) and D (Repository/UoW with Django) — infrastructure-swap demonstrations folded into [[repository]] and [[unit-of-work]], plus the [[orm-coupled-domain-model]] anti-pattern. E (Validation) — [[validation]] (syntax/semantics/pragmatics) and [[tolerant-reader]].

## Dropped as out of scope / generic

Per the charter's exclusion of generic OOP/architecture not specific to DDD, and of framework tutorials: the encapsulation/abstraction walk-through with the DuckDuckGo API snippets, the responsibility-driven-design aside, the mechanics of layered architecture beyond its DIP inversion, the TDD mechanics and test-pyramid tooling except where they justify model isolation, and the Flask/SQLAlchemy/pytest/Docker/Redis/Celery plumbing (which the authors themselves call "minor implementation details"), including the messaging-reliability and event-schema-evolution material the book flags as hard and out of its own scope. All code is on GitHub (one branch per chapter); the online text is licensed CC BY-NC-ND.

## Reader discussion

None fetched — a static book site with no comment thread.
