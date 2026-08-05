---
title: Domain-Driven Design (DDD)
category: foundations
summary: DDD as an interlocking pattern language with a strategic half and a tactical half, plus the orienting heuristics that the domain model is architecturally neutral and takes priority over architecture.
tags: [overview, ddd, strategic-design, tactical-design, pattern-language, ubiquitous-language]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

**Domain-Driven Design** puts a carefully crafted model of the business domain at the centre of the
software and expresses that model in the language the domain experts and developers share. Vaughn
Vernon's *Implementing Domain-Driven Design* frames DDD not as a set of independent tricks but as *a
large pattern language* — a web of patterns that only make sense in relation to one another.

> "The book *Domain-Driven Design* by Eric Evans presents what is essentially a large *pattern
> language.* A pattern language is a set of software patterns that are intertwined because they are
> dependent on each other." (raw L664)

A practical consequence: you cannot learn one DDD pattern in isolation. Reading about [[aggregate]]
pulls in [[entity]], [[value-object]], and **Repository**; reading about [[ubiquitous-language]] pulls
in [[bounded-context]]. This is why partial adoption is a recognized failure mode — see [[ddd-lite]].

## The two halves: strategic and tactical

**Tactical design** is the more technical half — the building-block patterns used *inside* a model:
[[entity]], [[value-object]], [[aggregate]], **Repository**, **Domain Service**, [[domain-event]],
**Factory**, **Module**. Vernon calls these the patterns that let you "take on a serious software
problem with the skill of a surgeon with a scalpel" (raw L528). Teams often reach for these first
because they feel like familiar object-oriented ground.

**Strategic design** is the "other half" (raw L530): [[bounded-context]], [[context-map]], and the
[[ubiquitous-language]] each context scopes, together with [[subdomain]] classification (core,
supporting, generic). Strategic design is what makes the tactical work pay off; skipping it produces
inferior models regardless of how clean the tactical code is (see [[ddd-lite]]).

## Big-picture ordering of the patterns

The *Guide to This Book* lays out how the pieces assemble (numbers are Vernon's pattern references):

- A **[[ubiquitous-language]] (1)** is applicable *within a single* **[[bounded-context]] (2)** — "a
  conceptual boundary where a domain model is applicable" (raw L684).
- **[[context-map]] (3)** patterns describe the relationships and integrations between bounded
  contexts.
- Some **Architecture (4)** surrounds each model — Hexagonal, Service-Oriented, REST, Event-Driven,
  CQRS, Event Sourcing — but the model itself should stay independent of it (see
  [[architecture-selection]]).
- Inside a bounded context you model *tactically*: an **[[aggregate]] (10)** is "composed of either a
  single **[[entity]] (5)** or a cluster of Entities and **[[value-object|Value Objects]] (6)** that
  must remain transactionally consistent" (raw L716), persisted via its **Repository (12)**.
- Stateless **Services (7)** perform "business operations that don't fit naturally as an operation on
  an Entity or a Value Object" (raw L720).
- **[[domain-event|Domain Events]] (8)** "indicate the occurrence of significant happenings in the
  domain" (raw L726) and can be published by Aggregates.
- **Modules (9)** organize cohesive domain objects — but must be named by the Ubiquitous Language, or
  "they will probably do more harm than good" (raw L732).

The Foreword notes that this edition elevates Domain Events to first-class status: "It places Domain
Events alongside Entities and Value Objects as the building blocks of a model" (raw L486).

## Orienting heuristics

**The model is architecturally neutral.** "Your strategically and tactically designed domain models
should be architecturally neutral" (raw L700). The domain model must not depend on the architecture,
persistence, or delivery mechanism around it.

**Prioritize the domain model over architecture.** "Architecture is important, but architectural
influences come and go. Remember to prioritize correctly, placing more emphasis on the domain model,
which has greater business value and will be more enduring" (raw L706). [[hexagonal-architecture|
Hexagonal architecture]] is recommended as a host precisely because it keeps the model at the heart
while letting other styles plug in around it.

**Prefer decisive rules of thumb over "it depends."** Evans explains why in the Foreword: "The honest
answer to almost any question in software development is, 'It depends.' That is not very useful to
people who want to learn to apply a technique… Rules of thumb don't have to be right in all cases.
They are what usually works well or the thing to try first" (raw L490). This is the stance behind the
concrete boundary rules in [[aggregate]] design.

## When to invest in DDD

DDD carries a cost and is not warranted for every project; the payoff is greatest for complex
core-business domains. The decision is worked through in [[when-to-use-ddd]], and the recurring trap for
teams that under-invest is [[ddd-lite]].

## Related

- [[when-to-use-ddd]] — deciding whether a project (and a subdomain) deserves the investment.
- [[ddd-lite]] — the failure of adopting only the tactical half.
- [[ubiquitous-language]], [[bounded-context]], [[subdomain]] — the strategic core.
- [[architecture-selection]] — how architecture surrounds a model without dictating it.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
