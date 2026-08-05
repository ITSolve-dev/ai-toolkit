---
title: Side-Effect-Free Function
category: building-blocks
summary: An operation that produces output without modifying its object's state; every Value Object method must be one, realizing replacement over mutation and tying Values to Command-Query Separation.
tags: [pattern, tactical-pattern, cqs, immutability, functional, value-object]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

A **Side-Effect-Free Function** (Evans' term) is "an operation of an object that produces output but
without modifying its own state. Since no modification occurs when executing a specific operation, that
operation is said to be side-effect free" (raw L5417). Because a [[value-object]] is immutable, "the
methods of an immutable Value Object must all be Side-Effect-Free Functions" (raw L5419). Vernon breaks
it out as a distinct characteristic — rather than folding it into immutability — precisely so designers
don't reduce Values to mere attribute bags and "overlook one of the most powerful aspects of the
pattern" (raw L5419).

## Relationship to CQS and functional programming

These functions are the *Query* side of Bertrand Meyer's **Command-Query Separation (CQS)**: "A query
method is one that asks an object a question. By definition, asking an object a question must not change
the answer" (raw L5425). Pure functional languages enforce exactly this — they "allow nothing but
Side-Effect-Free Behavior, requiring all closures to receive and produce only immutable Value Objects"
(raw L5423). CQS raised to the architectural level is [[cqrs]].

## Replacement via a new Value

The idiomatic use is to compute a new Value from parts of the current one rather than mutate. Vernon's
`FullName.withMiddleInitial("L")` returns a *new* `FullName` built from the existing first and last
names plus a validated middle initial, so `name = name.withMiddleInitial("L")` reads far more
expressively than blind assignment of a freshly constructed instance (raw L5434). Crucially, this
"captures important domain business logic in the model rather than allowing it to leak out into client
code" (raw L5459) — the same anti-leak motivation as [[whole-value]]. The decision heuristic: "If you
think that a specific method cannot be side-effect free and must mutate the state of its own instance,
challenge your assumptions. Is there a way to employ replacement rather than mutation?" (raw L5495).

## When a Value references an Entity — pass Values, not Entities

May a Value's method modify an [[entity]] passed as a parameter? If it does, the method is not really
side-effect free and is hard to test. Vernon's `businessPriority.priorityOf(product)` (passing the
`Product` Entity) has three flaws (raw L5473):

1. It forces the Value to depend on and "understand the shape of this Entity." The goal: "limit a Value
   to depend on and understand only its own type and the types of its attributes" (raw L5473).
2. A reader cannot tell which parts of the `Product` are used — the expression is not explicit,
   weakening the model (raw L5475).
3. "Any Value method that takes an Entity as parameter cannot easily prove that it doesn't cause the
   Entity's modification, making the operation more difficult to test" (raw L5477).

The fix is to pass **Values**, not Entities: `businessPriority.priority(product.businessPriorityTotals())`,
asking the Entity to hand over a `BusinessPriorityTotals` Value. "This way you reach the greatest level
of Side-Effect-Free Behavior" (raw L5479). (In this particular example, continued refinement moves the
calculation into a **Domain Service** entirely.)

## Trade-off

Side-effect-free functions are trivially testable (their output depends only on inputs and immutable
state) and keep domain logic where it belongs, but they demand replacement discipline and can feel
verbose to designers used to in-place mutation. Vernon's answer is that reusing existing parts to build
the changed Value is "a very simple approach" and "need not be an impractical, or even ugly,
proposition" (raw L5385).

## Related

- [[value-object]] — the building block whose methods must all be side-effect free.
- [[whole-value]] — the structural characteristic; this is the behavioral one.
- [[entity]] — what should not be passed into a Value's methods.
- [[cqrs]] — CQS raised to an architecture pattern.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
