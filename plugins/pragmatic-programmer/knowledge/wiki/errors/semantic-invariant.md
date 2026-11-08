---
title: Semantic invariant
category: errors
summary: "A fixed requirement that decides what every failure path must do, as distinct from a policy that may change; check retries and recovery branches against it."
tags: [concept, invariants, requirements]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

A semantic invariant is an unchanging requirement, which the book describes as a kind of philosophical contract (p. 146). It sits above any one routine and steers design wherever failure has to be resolved.

## The book's case

The authors worked on a debit-card transaction switch. Its central requirement was that a cardholder's transaction must never be applied twice. Whatever the failure mode, an error had to mean refusing the transaction, never processing a duplicate (p. 146). The rule proved useful in complex error recovery and guided detailed design in many areas (p. 146). Stated plainly, the rule was that an error goes «в пользу потребителя» (p. 148).

## Invariant or policy

The book warns against confusing fixed rules with requirements that are only policies and may change with a new management (p. 147). A semantic invariant is central to what the thing is and must not bend to policy, which belongs with the more dynamic business rules (p. 147).

Once a requirement of this kind is found, the book says to make it a well-known part of the documentation and to word it clearly and unambiguously (pp. 147-148). The debit-card sentence is its model: short, unambiguous and applicable all over the system (p. 148).

## In code

This wiki reads the concept as a question for failure paths. For each retry, catch and recovery branch, ask which outcome the invariant allows when the state of the operation is unknown. In the debit-card case, a blind retry after a timeout breaks it, because the first attempt may have succeeded.

The book reuses the idea for memory: [[ownership-of-nested-structures]] fixes who releases aggregated data by setting a semantic invariant (p. 161). A condition on one class belongs to [[class-invariant]] instead.

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, [[pragmatic-programmer]]: pp. 146-148, 161. The failure-path reading and the timeout example are this wiki's own.
