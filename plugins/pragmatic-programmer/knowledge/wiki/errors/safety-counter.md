---
title: Safety counter
category: errors
summary: "A loop in critical code that walks a linked structure or waits on an external condition with no bound on its iterations; or, the reverse, a lone safety counter in one loop that no project standard requires."
tags: [rule, loops, termination, defensive-code, assertions]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

A safety counter is a variable incremented on every pass of a loop and checked against a limit, so that a loop which runs far more often than it should is detected (p. 371). McConnell offers it for programs where any error would be catastrophic, as a way to make sure all loops end. He then limits it sharply.

## Rule

- Consider safety counters in programs where an error would be catastrophic (p. 371). His example walks a linked list with `node = node->Next` until `Next` is null. The counter increments each pass and asserts when it reaches `SAFETY_LIMIT` (p. 371).
- «Счетчики безопасности не панацея» (p. 371). Added one at a time, they increase complexity and can introduce errors of their own. Because they are not in every loop, they are forgotten when the loops that have them are changed. Introduced as a project standard for critical loops, they are expected, and their code is no more error-prone than any other (p. 371).

This wiki reads that as a decision by setting. A safety counter belongs to a convention, not to a loop.

The book uses the same device for recursion that has no simple stopping test, with the counter kept outside the call so that it does not restart (pp. 387-388); that case is on [[recursion-safeguards]].

## Sign in code

- In critical code: a loop that walks a linked structure (`next`, `parent`) or waits on an external condition with no bound on its iterations, or, under a project standard that requires safety counters, without the standard's counter.
- Without such a standard: a single loop carrying an ad hoc iteration cap with a magic limit, unlike every other loop around it.

A loop that walks a linked structure or waits on an external condition, in code that is not critical, where neither the header nor a stated invariant shows why it ends, is [[check-loop-boundaries-by-hand]]'s. In critical code the same loop is this page's.

## When not to apply

- Loops whose termination follows from their header, such as a `for` over a fixed range or iteration over a finite collection. This wiki's own limit: a counter there adds only noise.
- Adding a counter to code that is not critical and has no such standard. McConnell's case for the counter is limited to programs where an error is catastrophic (p. 371).
- Where the cause of non-termination is known, fix that cause, for example by detecting the cycle. This wiki's own limit: a counter is a net, not a repair (see [[fix-the-root-cause]]).
- A bound that is part of the loop's specification, such as a number of retry attempts or the iteration limit of a numeric method, is not a safety counter, and the second sign does not fire on it. This wiki's own limit.

## Repair

1. If the project is critical, adopt the counter as a written standard with one named helper or pattern, so every critical loop has the same shape.
2. Fail loudly at the limit, as the book's example does with an assertion (see [[assert-the-impossible]], [[crash-early]]).
3. Without a standard, remove a lone ad hoc cap and argue termination instead (see [[check-loop-boundaries-by-hand]]).

## Before and after

```
// before: critical code, list may be corrupted into a cycle
// project standard: every critical loop carries a LoopGuard
do:
    node = node.next
    ...
while node.next != null
```

```
// after: the project's standard guard
guard = LoopGuard(SAFETY_LIMIT)
do:
    node = node.next
    ...
    guard.tick()                  // asserts "internal error: safety limit" past the limit
while node.next != null
```

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 16.2, p. 371; the recursion case ch. 17.2, pp. 387-388. The reading as a decision by setting, the extension of the first sign beyond the book's linked list (waits on an external condition), the second sign, the first, third and fourth limits, repair steps 1 and 3, the `LoopGuard` helper and the assignment against [[check-loop-boundaries-by-hand]] are this wiki's own.
