---
title: Invariants and Constraints
category: aggregate-design
summary: A constraint restricts the states a model may enter; an invariant is a condition that must always hold when an operation completes. Enforcing them is much of what domain logic is for.
tags: [concept, invariant, constraint, consistency, domain-logic, business-rules, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Invariants and Constraints

Much of the domain logic we write exists to enforce the rules of the business. Two closely related terms describe those rules, and the distinction is worth keeping precise because [[aggregate|aggregates]] and [[consistency-boundary|consistency boundaries]] are designed specifically to protect them.

> "a *constraint* is a rule that restricts the possible states our model can get into, while an *invariant* is defined a little more precisely as a condition that is always true." (raw L3182)

- A **constraint** limits which states are legal. Example: in a hotel-booking system, *double bookings are not allowed*.
- An **invariant** is a condition that is always true — specifically, true *whenever an operation finishes*. Example: *a room cannot have more than one booking for the same night*. The constraint (no double bookings) supports the invariant.

> "The *invariants* are the things that have to be true whenever we finish an operation." (raw L3178)

## Invariants hold at operation boundaries, not every instant

The qualifier "whenever we finish an operation" is the key subtlety. A model is permitted to pass through temporarily-inconsistent intermediate states, as long as it lands in a consistent one. The book's example: to seat a VIP we may shuffle bookings around in memory, and mid-shuffle we might momentarily be double-booked —

> "our domain model should ensure that, when we're finished, we end up in a final consistent state, where the invariants are met. If we can't find a way to accommodate all our guests, we should raise an error and refuse to complete the operation." (raw L3191)

So the domain model has two obligations: (1) reach a consistent final state, or (2) refuse the operation and raise an error. It must never silently commit a state that violates an invariant.

## Examples from the allocation domain

The allocation model carries two representative rules:

- *"An order line can be allocated to only one batch at a time."* (raw L3197) — the invariant is that a line is allocated to zero or one batch, never more. Nothing in the original code explicitly stopped `Batch.allocate()` being called on two different batches for the same line.
- *"We can't allocate to a batch if the available quantity is less than the quantity of the order line."* (raw L3209) — the invariant is that a batch's available quantity must stay `>= 0`, so stock is never oversold.

## Why this matters for aggregate design

Invariants are what decide which objects must be consistent *with each other*, and therefore which objects belong in the same aggregate. Two objects covered by a shared invariant must be changed together inside one boundary; two objects with no invariant spanning them can be changed independently and concurrently. As the book puts it about allocating two different SKUs at once: "It's safe to allocate two products at the same time because there's no invariant that covers them both. We don't need them to be consistent with each other." (raw L3240)

## Related

- [[consistency-boundary]] — the region within which invariants are guaranteed
- [[aggregate]] — the object that enforces its members' invariants
- [[choosing-aggregate-boundaries]] — using invariants to draw the boundary
- [[aggregate-concurrency-control]] — keeping invariants true under concurrent writes
- [[model-true-invariants-in-consistency-boundaries]] — Vernon's parallel rule that only a *true* invariant justifies clustering objects
