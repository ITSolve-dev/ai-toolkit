---
title: Entity vs Aggregate
category: building-blocks
summary: The two are different categories, not neighbouring patterns — an Entity is a single object defined by identity and continuity, while an Aggregate is a transactional-consistency boundary around a cluster whose root happens to be an Entity. Every aggregate root is an entity; not every entity is an aggregate.
tags: [comparison, entity, aggregate, aggregate-root, consistency-boundary, identity, building-blocks]
sources: [book-implementing-ddd-vaughn-vernon, web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Entity vs Aggregate

A recurring point of confusion — the [[aggregate]] chapter itself calls the pattern "one of the least
well understood" (IDDD raw L8680). The clearest framing is that **[[entity]] and [[aggregate]] answer
different questions**, and one contains the other.

## They are different categories

- An **[[entity]]** is a *single object* defined by **individual identity and continuity through
  change**, not by its attributes: "An Entity is a unique thing and is capable of being changed
  continuously over a long period of time" (raw L3833). Its hallmark is *identity equality* — "we can
  change their values, and they are still recognizably the same thing" (raw L890).
- An **[[aggregate]]** is a *boundary around a cluster* of entities and value objects with exactly one
  **root**, whose defining property is transactional consistency: "*Aggregate* is synonymous with
  *transactional consistency boundary*" (raw L8912).

So an entity is a *thing*; an aggregate is a *boundary of atomic change* drawn around one or more things.

## The bridge: an aggregate root is an entity, but not every entity is an aggregate

Every aggregate has exactly one **root, and that root is an entity** with a globally unique identity.
The converse fails: an entity can be an *interior member* of an aggregate rather than an aggregate in its
own right. In Cosmic Python's allocation model, `Product` is the aggregate and `Batch` is an entity
*inside* it — reachable only through the root: "The only way to modify the objects inside the aggregate
is to load the whole thing, and to call methods on the aggregate itself" (raw L3247). `Batch` has
identity equality (so it is an entity) yet is never addressed from outside (so it is not an aggregate).

| | **[[entity]]** | **[[aggregate]]** |
|---|---|---|
| What it is | one object | a boundary around a cluster |
| Defined by | identity + lifecycle continuity | the invariants that must stay transactionally consistent |
| Answers | "is this the same thing over time?" | "what changes together, atomically?" |
| Visibility | may be interior ("private") | the model's "public" class; the sole entrypoint (raw L3273) |
| Persistence | — | repositories return *only* aggregates (raw L3396) |

## Different concerns, different rules

An entity's job is to own only the data and logic tied to its identity and lifecycle (see [[entity]]).
An aggregate's job is to guarantee a set of invariants holds inside one transaction — and that job
carries rules an entity alone never does:

- **One instance modified per transaction** (raw L8914) — see [[aggregate-consistency-boundary]].
- **Reference other aggregates by identity, not by pointer** — see
  [[reference-other-aggregates-by-identity]].
- **Cross-aggregate rules propagate via [[domain-event|events]] and eventual consistency** — see
  [[eventual-consistency-between-aggregates]].
- **Drawn by transactional analysis, not object-graph convenience** — "we cannot correctly reason on
  Aggregate design without applying transactional analysis" (raw L8914); ignoring this yields the
  [[large-cluster-aggregate]] failure.

## The subtle overlap: entities can hold invariants too

An entity *can* hold an invariant — "a state that must stay transactionally consistent throughout the
Entity life cycle" (raw L4744). The difference is *scope*: when the invariant spans **several** objects,
the **aggregate** is what enforces it atomically. A lone entity guards its own state; the aggregate
guards the consistency of the whole cluster behind its root.

> **In one line:** Entity is about *"this is the same thing over time"*; Aggregate is about *"these
> things change together, atomically, behind one root."* The root of every aggregate is an entity; not
> every entity is an aggregate.

## Related

- [[entity]] · [[aggregate]] — the two patterns compared here.
- [[value-object]] — the identity-free counterpart an aggregate also clusters.
- [[consistency-boundary]] · [[aggregate-consistency-boundary]] — what makes an aggregate more than a cluster.
- [[reference-other-aggregates-by-identity]] · [[eventual-consistency-between-aggregates]] — the boundary rules.
- [[large-cluster-aggregate]] — the failure mode of confusing "objects that relate" with "objects that must be consistent".
