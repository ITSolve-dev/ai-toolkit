---
title: "Rule: Use Eventual Consistency Outside the Boundary"
category: aggregate-design
summary: When one command must trigger rules on other Aggregates, publish a Domain Event and let subscribers update each in its own transaction, instead of one large atomic change.
tags: [rule, rule-of-thumb, aggregate, eventual-consistency, domain-event, aggregate-design, consistency, cosmic-python]
sources: [book-implementing-ddd-vaughn-vernon, web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

The fourth [[aggregate]] rule of thumb, resting on an easily overlooked line from Evans' original Aggregate definition. It is the Aggregate-design application of the general principle in [[eventual-consistency]].

> Any rule that spans AGGREGATES will not be expected to be up-to-date at all times. Through even[t] processing, batch processing, or other update mechanisms, other dependencies can be resolved within some specific time. [Evans, p. 128] (raw L9081)

Hence: "if executing a command on one Aggregate instance requires that additional business rules execute on one or more other Aggregates, use eventual consistency." (raw L9083)

## How to implement it

An Aggregate command method publishes a [[domain-event]]; asynchronous subscribers each retrieve a *different* Aggregate and execute its behavior, each in its **own** transaction — obeying the one-instance-per-transaction rule (raw L9089-9109). In the book, `BacklogItem.commitTo(Sprint)` publishes `BacklogItemCommitted`, and a subscriber later creates a `CommittedBacklogItem` so the `Sprint` records the work (raw L9094-9113).

When `Task` and `BacklogItem` are separate Aggregates, `TaskHoursRemainingEstimated` is published on each re-estimate; a subscriber delegates to a [[domain-service]] that loads the `BacklogItem` and its `Task`s and calls `estimateTaskHoursRemaining()`, letting the Root transition status eventually (raw L9307-9328). An optimization: instead of loading all tasks 143 of 144 times needlessly, ask the [[repository]] for `sum(task.hoursRemaining)` from the database (raw L9330-9347).

**Failure handling:** if a subscriber's commit loses to concurrency contention, don't acknowledge the message; it is redelivered and retried in a fresh transaction until it succeeds or a retry limit is hit, after which you compensate or report for intervention (raw L9111).

## Ask the domain experts about delay

Before assuming atomicity is required, ask experts whether they can tolerate a delay between updating one instance and the others. "Domain experts are sometimes far more comfortable with the idea of delayed consistency than are developers," who are "usually indoctrinated with an atomic change mentality" — experts remember pre-automation business delays and often accept seconds, minutes, hours, even days (raw L9085-9087).

## The tie-breaker: "Whose job is it?"

When it's genuinely unclear whether to use transactional or eventual consistency, a technical preference (classic DDD leaning atomic, CQRS leaning eventual) is no answer. Evans' guideline:

> ask whether it's the job of the user executing the use case to make the data consistent. If it is, try to make it transactionally consistent... If it is another user's job, or the job of the system, allow it to be eventually consistent. (raw L9135)

This "exposes the real system invariants: the ones that must be kept transactionally consistent" (raw L9135). Applied to the `BacklogItem` status: if the *team member* setting the last task to zero should trigger completion, keep `Task` inside `BacklogItem` for transactional consistency; if a *product owner or the system* marks it done, tasks can be split off. The book concludes the answer is unclear enough that it "should be an optional application preference" — and that asking the question surfaced a new domain aspect (raw L9355-9361).

## Trade-off: UI staleness

Eventual consistency complicates the view. Options weighed (raw L9349-9353): displaying stale status (looks like a bug), background Ajax polling (mostly wasted requests — 143/144), Comet/Ajax Push (new tech, real effort), or simplest and safest — a visual cue that the status is uncertain with a suggested refresh. A [[large-cluster-aggregate]] may sometimes look like a way to *avoid* this, but at unacceptable performance cost.

## The Cosmic Python view — one aggregate per transaction, others via events

*Architecture Patterns with Python* reaches the same rule from the message-bus side. "People often ask, 'What should I do if I need to change multiple aggregates as part of a request?'" (raw L4151) — and the answer is *don't change them in one transaction*: "If we have two things that can be transactionally isolated (e.g., an order and a product), then we can make them *eventually consistent* by using events. When an order is canceled, we should find the products that were allocated to it and remove the allocations." (raw L4155)

The mechanism is three steps: (1) change **one** aggregate and commit it — satisfying its [[consistency-boundary]]; (2) that aggregate raises a [[domain-event]] recording the fact (`OrderCancelled`, `Deallocated`); (3) a handler on the [[message-bus]], in its *own* [[unit-of-work]] and transaction, loads and updates the *other* aggregate(s). Between step 1's commit and the handler completing, the system is momentarily inconsistent — hence *eventually* consistent — and the two aggregates are never mutated inside the same transaction.

Why not update both aggregates atomically? Because that re-couples them: it forces a shared transaction (and often a lock), exactly the coupling the aggregate boundary exists to prevent. Domain events "decouple aggregates and applications from one another" (raw L3726) while still propagating the change. The cost is giving up read-your-write immediacy across the boundary. Cosmic Python's failure modes echo the book's above:

- **Lost updates if events aren't reliably dispatched** — a crash between commit and publish leaves the second aggregate stale (reliable delivery is a messaging concern the book defers).
- **Temporary inconsistency is visible** — reads spanning both aggregates may see a half-applied change; the design must make that acceptable.
- **Ordering and idempotency** — handlers in separate transactions must tolerate reordering and re-delivery.

The operational form of this rule — one command modifies one aggregate atomically, everything else via events — is [[aggregate-consistency-boundary]].

## Related

[[aggregate]] · [[eventual-consistency]] · [[domain-event]] · [[reference-other-aggregates-by-identity]] · [[model-true-invariants-in-consistency-boundaries]] · [[reasons-to-break-aggregate-rules]] · [[consistency-boundary]] · [[aggregate-consistency-boundary]] · [[message-bus]] · [[unit-of-work]]
