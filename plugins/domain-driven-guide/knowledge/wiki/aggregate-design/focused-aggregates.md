---
title: Focused Aggregates
category: aggregate-design
summary: Event Sourcing removes the persistence friction of adding new aggregates, so A+ES designs trend toward smaller, behaviorally focused aggregates — reinforcing the small-aggregate rule of thumb without violating invariant protection.
tags: [guideline, aggregate, aggregate-design, event-sourcing, small-aggregates, bounded-context]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

## What it is

**Focused Aggregates** is an aggregate-sizing guideline that emerges under [[event-sourcing|A+ES]] (Aggregates plus Event Sourcing). Because event sourcing removes most of the persistence overhead of introducing a new [[entity|Entity]] or [[aggregate|Aggregate]], designs built on A+ES tend to decompose a real-world concept into several small, behaviorally focused aggregates rather than one large one. It is the event-sourcing corollary of the general [[design-small-aggregates|small-aggregate rule]].

## Why the bias shifts

With traditional persistence, adding or enriching an entity is expensive: "We need to create new tables and define new mapping schemata and Repository methods" (raw L15388). That friction quietly pushes designers to "add onto an existing Aggregate rather than to create a new one," which inflates aggregates over time. A+ES inverts this economic pressure — new aggregates are cheap to persist (just a new event stream), so the natural pull is toward smaller units: "In my experience, Aggregates designed using A+ES tend to be smaller, which is one of the primary Aggregate Rules of Thumb" (raw L15390).

## Concrete example

For a SaaS company, one real-world customer is modeled as distinct aggregates, each focused on one behavioral aspect, potentially in different [[bounded-context|Bounded Contexts]] with different technology:

- `Customer:505` — billing, invoicing, general account management.
- `Security-Account:505` — users and access permissions.
- `Consumer:505` — actual service consumption.

The `Consumer` aspect may need to "deal with consuming thousands of messages for customers each second" and be hosted "in auto-scaling cloud fabric," while less demanding aspects live in cheaper environments (raw L15400). Same identity suffix (`:505`), different aggregates and contexts.

## The counter-rule (failure mode)

Small is a bias, not a mandate. "Aggregates should never be designed to be arbitrarily small. We always want to design Aggregates to protect true business invariants, and doing so may cause any given Aggregate to be composed of multiple Entities and a number of Value Objects" (raw L15402). Shrinking an aggregate below the boundary of a true invariant just relocates the consistency problem into fragile cross-aggregate coordination — the classic over-decomposition mistake (see [[model-true-invariants-in-consistency-boundaries]]). The A+ES advantage is that it *lets* you reach for the smallest boundary that still protects the invariant, not that smaller is always better.

## Behavior-first modeling

A+ES also enables a modeling order that puts language before structure: "start domain modeling by defining the core of your Ubiquitous Language by defining the primary incoming Commands and outgoing Events... Only at a later stage would we actually group some concepts as Aggregates, based on similarity, relevance, and business rules" (raw L15404). Even as a throwaway spike, this clusters aggregate boundaries around real behavior instead of table structure. See [[given-when-then-specification]] and [[functional-event-sourcing]] for related behavior-first techniques.

## Related

[[aggregate]] · [[design-small-aggregates]] · [[model-true-invariants-in-consistency-boundaries]] · [[event-sourcing]] · [[bounded-context]] · [[ubiquitous-language]] · [[value-object]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
