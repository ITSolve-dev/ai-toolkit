---
title: CQRS — Command-Query Responsibility Segregation
category: architecture
summary: Split the model into a command (write) model of behavior-only Aggregates and a denormalized query (read) model tuned for views, kept in sync by Domain Events; justified only when cross-Aggregate view complexity is a real risk, otherwise it is accidental complexity.
tags: [architecture-pattern, architecture, cqrs, read-model, write-model, domain-event, eventual-consistency, cosmic-python]
sources: [book-implementing-ddd-vaughn-vernon, web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

**CQRS** raises Bertrand Meyer's object-level Command-Query Separation (CQS) to an architecture pattern.
CQS: "Every method should be either a command that performs an action, or a query that returns data to
the caller, but not both" (raw L3260) — a command mutates state and returns void; a query returns data
and causes no state change.

## The problem it solves

Rich domains produce views that cut across many [[aggregate|Aggregate]] types and instances, which is
painful to serve from **Repositories**. The unsatisfying alternatives are: query several Repositories and
assemble a DTO, add specialized finders to Repositories, or compromise the UX so views obey Aggregate
boundaries. "Most would agree that in the long run a mechanical and spartan user interface won't
suffice" (raw L3254).

## The split

Segregate query responsibilities from command responsibilities into two models:

- **Command model (write model)** — Aggregates have *only* command methods, no getters; Repositories are
  stripped to `add()`/`save()` plus a single `fromId()`/identity lookup — "A Repository could not be used
  to find an Aggregate by any other means" (raw L3272).
- **Query model (read model)** — a *denormalized* data model that delivers no behaviour, only data for
  display. Ideally one table per user-interface view type, even one per security role, so a manager's
  view component selects from a manager table view and a normal user cannot see it. Views are "cheap and
  disposable" (raw L3308), especially atop [[event-sourcing|Event Sourcing]], and can be rebuilt from
  replayed events.

## Keeping the two models in sync

When a Command Handler / [[application-service|Application Service]] executes a command method, the
command model publishes a [[domain-event|Domain Event]]; "This is essential to ensuring that the query
model is updated" (raw L3370). A dedicated subscriber consumes each event and updates the query model —
so events must be rich enough to produce the correct query-model state. CQRS does not *require*
[[event-sourcing]]; the command model can be persisted with an ORM as long as an event is still
published.

## Trade-offs: consistency

- **Synchronous** update — same database/transaction, fully consistent, but slower table updates that
  may breach the SLA.
- **Asynchronous** update — introduces **eventual consistency**: the UI may not immediately reflect the
  latest command. Mitigations discussed: temporarily display the just-submitted command data, or stamp
  each query record with its last-update time and show the data's age so users can request fresher data
  (a technique "lauded by some… and heavily criticized by others as a hack", raw L3428).

## Failure mode

CQRS is easy to over-apply. "if a user interface is not overly complex or [does not] regularly cut across
several different Aggregates in a single view, employing CQRS would serve to introduce accidental
complexity rather than necessary complexity. CQRS is the right choice when it removes a risk that has a
high probability of causing failure if ignored" (raw L3432) — the [[architecture-selection]] test.

## The Cosmic Python view — "a domain model is a write model"

*Architecture Patterns with Python* arrives at CQRS from the same seed, [[command-query-separation]], but justifies the architectural split with a specifically DDD argument: **everything a DDD codebase invests in — the [[aggregate]], the [[unit-of-work]], the [[domain-event|domain events]] pattern — "exists so we can enforce rules when we change the state of our system. We've built a flexible set of tools for writing data." (raw L5456).** None of that machinery helps reads: "a domain model is not a data model—we're trying to capture the way the business works… *Most of this stuff is totally irrelevant for read-only operations*." (raw L5652). This is "the chin-stroking-architect's justification for CQRS" (raw L5651).

The two halves have opposite characteristics, which is why segregating them pays off (raw L5480):

| | Read side | Write side |
|---|---|---|
| Behavior | Simple read | Complex business logic |
| Cacheability | Highly cacheable | Uncacheable |
| Consistency | Can be stale | Must be transactionally consistent |

The asymmetry is often dramatic: at MADE.com allocation might "process one hundred orders in an hour" but serve "one hundred product views per *second*" (raw L5461) — same domain, very different access pattern, and because "our customers won't notice if the query is a few seconds out of date" the reads can be made [[eventual-consistency|eventually consistent]] to perform better (raw L5471).

**Decision rule.** CQRS tracks the same complexity threshold as the [[domain-model]] itself: "If you're building a simple CRUD app, reads and writes are going to be closely related, so you don't need a domain model or CQRS. But the more complex your domain, the more likely you are to need both." (raw L5657). The honest retrospective caveat: "Often, your read operations will be acting on the same conceptual objects as your write model, so using the ORM, adding some read methods to your repositories, and using domain model classes for your read operations is *just fine*." (raw L5888). Full CQRS is warranted only when reads act on **different conceptual entities** than the write model — in the book's case the write model thinks in `Batches` for one SKU while users care about allocations for a whole order across multiple SKUs (raw L5892). Forcing a diverging read requirement through the write model past that point is the [[reusing-the-write-model-for-reads]] anti-pattern.

**Trade-off.** You gain reads that are simple, fast, cacheable, and horizontally scalable; you give up a second model (and possibly store) to keep in sync, plus eventual consistency instead of read-your-writes. The book's summary of the extreme end: "Complex technique. Harry will be forever suspicious of your tastes and motives." (raw L5886). See [[read-model]] for the concrete ladder of implementation options.

## Related

- [[event-sourcing]] — the pattern CQRS pairs with hand-in-glove (query model projected from events).
- [[domain-event]] — what keeps the read model in sync with the write model.
- [[application-service]] — the Command Handler that publishes the event.
- [[aggregate]] — the command-model unit stripped of getters.
- [[architecture-selection]] — the risk-driven test that governs whether to adopt CQRS.
- [[command-query-separation]] — the method-level seed principle CQRS scales up.
- [[read-model]] — the concrete read side and its ladder of implementation options.
- [[reusing-the-write-model-for-reads]] — the anti-pattern CQRS reacts against.
- [[book-implementing-ddd-vaughn-vernon]], [[web-page-cosmic-python-book]] — source summaries.
