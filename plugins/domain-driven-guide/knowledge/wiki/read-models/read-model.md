---
title: Read Model
category: read-models
summary: A separate, read-optimized (often denormalized) view of your data — kept up to date via domain events — so queries stay simple, fast, and horizontally scalable.
tags: [pattern, read-model, cqrs, domain-event, denormalization, eventual-consistency, trade-offs, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Read Model

A **read model** (or view model) is a data representation built specifically for querying, kept separate from the write-optimized [[domain-model]]. It is the concrete payoff of [[cqrs]]: instead of assembling query results out of aggregates and repositories that were designed for writes, you maintain a copy of the data shaped for reads — frequently **denormalized** so a query is a trivial key lookup.

## The ladder of options

Cosmic Python walks up a ladder of increasingly decoupled read implementations, from reusing existing abstractions to a fully separate store (raw L5880):

| Option | Pros | Cons |
|---|---|---|
| Just use [[repository|repositories]] | Simple, consistent approach | Performance issues with complex query patterns |
| Custom queries with your ORM | Reuses DB config and model definitions | Adds another query language with its own quirks |
| Hand-rolled SQL against your normal tables | Fine control over performance, standard syntax | Schema changes must be mirrored into the queries |
| Extra denormalized tables as a read model | Much faster to query; update it in the same transaction as the write tables and you keep strong consistency | Slows writes slightly |
| Separate read store updated by events | Read copies are easy to scale out; views precomputed so queries are trivial | Complex technique |

## Why denormalize

Even with well-tuned indexes, "a relational database uses a lot of CPU to perform joins. The fastest queries will always be `SELECT * from mytable WHERE key = :value`" (raw L5737). A denormalized `allocations_view` table lets the query collapse to exactly that. Beyond raw speed, the deeper win is **scale**: writes need row locks to avoid race conditions, but "When we're *reading* data… there's no limit to the number of clients that can concurrently execute. For this reason, read-only stores can be horizontally scaled out." (raw L5742). Hence the tip: "Because read replicas can be inconsistent, there's no limit to how many we can have. If you're struggling to scale a system with a complex data store, ask whether you could build a simpler read model." (raw L5746)

## Keeping it up to date: use domain events

The hard part is synchronization: "Keeping the read model up to date is the challenge!" (raw L5748). Database views and triggers work but tie you to the database. The book's preferred technique is to reuse the event-driven architecture — add a second handler to the relevant [[domain-event]] that writes into the read model. For the `Allocated` event, an `add_allocation_to_read_model` handler simply `INSERT`s into `allocations_view`; a `Deallocated` event triggers a `remove_allocation_from_read_model` handler. This runs in a second [[unit-of-work|UoW]]/transaction after the write model commits, which is the source of the read side's [[eventual-consistency|eventual consistency]].

The strongest argument for this approach is **substitutability**: because the handlers hide the storage, the read model's backend can be swapped (e.g. from a SQL `allocations_view` to a Redis hash) and "the *exact same* integration tests… still pass, because they are written at a level of abstraction that's decoupled from the implementation" (raw L5866). Hence: "Event handlers are a great way to manage updates to a read model, if you decide you need one. They also make it easy to change the implementation of that read model at a later date." (raw L5871)

## Testing note

Drive the read-model integration test through the public entrypoint (the [[message-bus]] / command handlers), not by writing to storage directly: "That keeps our tests decoupled from any implementation/infrastructure details about how things get stored." (raw L5611). Setup puts commands on the bus; assertions read through the view.

## Related

- [[cqrs]] — the pattern this implements.
- [[command-query-separation]] — the method-level seed principle.
- [[read-model-projection]] — the event-sourcing sibling: subscribers projecting events into a queryable read model.
- [[domain-event]] — the update mechanism.
- [[reusing-the-write-model-for-reads]] — the failure mode that motivates a dedicated read model.
- [[repository]] · [[unit-of-work]] — the write-side abstractions the read side deliberately bypasses.
