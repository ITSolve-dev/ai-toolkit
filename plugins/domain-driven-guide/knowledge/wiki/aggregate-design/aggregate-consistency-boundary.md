---
title: Aggregate as Consistency Boundary (One Command, One Aggregate)
category: aggregate-design
summary: An aggregate is the unit of atomic consistency — one command modifies a single aggregate inside one unit of work and succeeds or fails in totality, while everything beyond it (cross-aggregate updates, bookkeeping, notification) propagates via domain events processed in separate transactions, yielding eventual consistency.
tags: [principle, rule, aggregate, consistency-boundary, eventual-consistency, unit-of-work, domain-event, transactions, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Aggregate as Consistency Boundary (One Command, One Aggregate)

The [[aggregate]] is the model's *consistency boundary*: the scope within which invariants must hold at all times, and the unit that is updated atomically. This page is the *operational rule* built on the [[consistency-boundary]] concept — how the boundary is enforced once the system is organized around commands and [[domain-event|domain events]]. Cosmic Python states it plainly: "We've carefully identified *aggregates* that act as consistency boundaries, and we've introduced a *UoW* that manages the atomic success or failure of an update to an aggregate" (raw L4914-4917). The [[unit-of-work]] is the transactional wrapper that makes one aggregate's update all-or-nothing.

## The failure mode it prevents

Inconsistent state arises "when only half an operation is completed" (raw L4906). The book's example: allocate three units of `DESIRABLE_BEANBAG` to an order but fail to reduce remaining stock, so "the three units of stock are both allocated *and* available, depending on how you look at it" (raw L4909-4911) — and later get double-allocated. Drawing the boundary around the `Product` aggregate removes the possibility: "either a particular order line is allocated to the product, or it is not — there's no room for inconsistent states" (raw L4920-4922). This is the antidote to the [[large-cluster-aggregate]] / leaky-boundary problems where invariants straddle multiple objects with no atomic guard.

## The decision rule: one command, one aggregate

The operative heuristic for sizing work: "When a user wants to make the system do something, we represent their request as a *command*. That command should modify a single *aggregate* and either succeed or fail in totality. Any other bookkeeping, cleanup, and notification we need to do can happen via an *event*. We don't require the event handlers to succeed in order for the command to be successful" (raw L4928-4931). See [[commands-and-events]] for why commands fail noisily and events fail independently.

## Eventual consistency between aggregates

The complement of the rule is that **aggregates are not required to be immediately consistent with each other**: "By definition, we don't require two aggregates to be immediately consistent, so if we fail to process an event and update only a single aggregate, our system can still be made eventually consistent" (raw L4924). So when a command updates one aggregate and raises events, a downstream event handler updating a *second* aggregate may lag or retry — the system reaches [[eventual-consistency]] without ever violating a within-aggregate invariant. The general rule of thumb is [[eventual-consistency-between-aggregates]].

## The reallocation flow — two units of work chained by an event

The worked example is changing a batch's quantity, which may force orders to be deallocated and then reallocated. The book splits it into two units of work chained by an event (raw L4487):

- **UoW 1 — `BatchQuantityChanged` handler:** the [[message-bus]] tells the domain model to change the batch quantity; the model emits one or more `AllocationRequired` events.
- **UoW 2 (or more) — `AllocationRequired` handler:** each emitted event is handled by the ordinary `allocate` handler, in its own transaction.

The deallocation and each subsequent reallocation therefore happen "in separate transactions. Once again, our message bus helps us to enforce the single responsibility principle, and it allows us to make choices about transactions and data integrity." (raw L4224) The event is the seam that lets you choose the transaction boundary deliberately.

## Trade-off / failure mode: two transactions, no atomicity

Splitting across units of work trades immediate consistency for decoupling, and the book warns about it directly:

> "When you split things out like this across two units of work, you now have two database transactions, so you are opening yourself up to integrity issues: something could happen that means the first transaction completes but the second one does not. You'll need to think about whether this is acceptable, and whether you need to notice when it happens and do something about it." (raw L4497)

So the failure mode is a *partial* update: the quantity change commits, the reallocation does not, and the system is left inconsistent until something detects and repairs it. Accepting this means designing for eventual consistency (detection, retries, compensation) rather than assuming the whole chain is atomic. Keep genuinely-must-be-atomic invariants inside a single aggregate/transaction; use cross-aggregate events only where eventual consistency is tolerable.

## Reliability pay-off and business alignment

Separating the core command from event-driven side effects means "things [can] fail in isolation, which improves the overall reliability of the system. The only part of this code that *has* to complete is the command handler that creates an order" (raw L5001-5004) — the part the customer actually cares about. In the VIP example (see [[domain-event]]), a busy email server or a bug in a secondary `History` aggregate must not stop the system from taking the customer's money. The boundaries are drawn to match reality: "we've deliberately aligned our transactional boundaries to the start and end of the business processes" (raw L5007) — a direct expression of the [[ubiquitous-language]].

## Trade-offs

- **Gain:** atomicity per aggregate, no half-done overallocation, independent failure of secondary work, higher resilience.
- **Give up:** immediate cross-aggregate consistency — you must accept eventual consistency and build recovery (idempotent retries, message replay) for the events that update other aggregates.
- **Failure mode if ignored:** trying to make everything commit together (raising and persisting all events in one transaction) couples unrelated concerns — "a busy email server can stop us from taking money for orders" (raw L4996), and a bug in one aggregate blocks the whole business process.

## Related

- [[consistency-boundary]] — the underlying concept this rule operationalizes
- [[aggregate]] · [[unit-of-work]] — the boundary and its transactional wrapper
- [[commands-and-events]] — commands fail noisily, events fail independently
- [[domain-event]] · [[message-bus]] — the message that carries the propagation and the dispatcher
- [[eventual-consistency]] · [[eventual-consistency-between-aggregates]] — the cross-aggregate rule of thumb
- [[repository]] — loads exactly one aggregate per query so each transaction touches one aggregate
