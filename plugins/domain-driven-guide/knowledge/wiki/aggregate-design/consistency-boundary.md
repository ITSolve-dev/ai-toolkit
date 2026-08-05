---
title: Consistency Boundary
category: aggregate-design
summary: The explicit region — realized by an aggregate — inside which invariants are guaranteed and every operation must end consistent; it maps to a single database transaction and is how a system stays consistent without locking everything.
tags: [concept, consistency-boundary, aggregate, invariant, transaction, concurrency, performance, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Consistency Boundary

A **consistency boundary** is the explicit line drawn around a small set of objects that must be kept consistent with one another. Everything inside is guaranteed to satisfy its [[invariants-and-constraints|invariants]] at the end of every operation; nothing outside is required to be consistent with what is inside at that moment. In this codebase the boundary is *realized* by an [[aggregate]]: each aggregate is one consistency boundary responsible for maintaining its own invariants.

> "Each basket is a single *consistency boundary* responsible for maintaining its own invariants." (raw L3262)

Making the boundary explicit is what lets us "build high-performance software without compromising maintainability" (raw L3153).

## The problem it solves: consistency vs. concurrency

In a single-threaded, single-user app, maintaining an invariant like *available quantity >= 0* is easy: allocate one line at a time and raise an error when stock runs out. **Concurrency** breaks this. Multiple order lines may be allocated simultaneously, possibly at the same time as changes to the batches themselves. The usual fix is database **locks**, but locking the whole `batches` table for every one of hundreds of thousands of order lines an hour causes deadlocks and performance collapse.

The tension is fundamental:

> "Maintaining our invariants inevitably means preventing concurrent writes; if multiple users can allocate `DEADLY-SPOON` at the same time, we run the risk of overallocating." (raw L3235)

But there is no invariant linking `DEADLY-SPOON` to `FLIMSY-DESK`, so those *can* safely change at once. The consistency boundary encodes exactly this distinction: serialize writes *within* a boundary, allow full concurrency *between* boundaries.

## One boundary = one transaction

The practical rule is that each change to an aggregate runs in a single database transaction, and a transaction touches only one aggregate instance. We load the entire object (e.g. the whole basket) as a single blob, mutate it, and commit — we do not modify two customers' baskets in one transaction, because there is no use case that requires them to be consistent together.

> "The aggregate will be the boundary where we make sure every operation ends in a consistent state. This helps us to reason about our software and prevent weird race issues." (raw L3276)

This is the same transaction boundary the [[unit-of-work]] wraps, and the operational rule built on top of it — one command per aggregate, everything else via events — is [[aggregate-consistency-boundary]].

## Smaller is better

Because the boundary is what gets locked/serialized, its size directly governs both correctness and throughput:

> "We want to draw a boundary around a small number of objects—the smaller, the better, for performance—that have to be consistent with one another, and we need to give this boundary a good name." (raw L3276)

Deciding *which* objects go inside is the subject of [[choosing-aggregate-boundaries]]; enforcing the boundary against real concurrent writers is [[aggregate-concurrency-control]].

## Failure modes

- **Boundary too large** (e.g. "lock the whole `batches` table"): serializes unrelated work, causing deadlocks and performance woes.
- **Boundary too small / spanning invariants across boundaries**: two aggregates that actually share an invariant can be updated concurrently and violate it, because nothing serializes them together.
- **Multi-aggregate transactions**: modifying several aggregates in one transaction quietly recreates a big lock and reintroduces the race conditions the boundary was meant to remove.

## Related

- [[aggregate]] — the object that *is* the boundary
- [[invariants-and-constraints]] — what the boundary guarantees
- [[choosing-aggregate-boundaries]] — how big to draw it and around what
- [[aggregate-concurrency-control]] — optimistic vs. pessimistic enforcement
- [[aggregate-consistency-boundary]] — the one-command-one-aggregate rule that operationalizes it
- [[unit-of-work]] — the transaction wrapper that makes one boundary atomic
