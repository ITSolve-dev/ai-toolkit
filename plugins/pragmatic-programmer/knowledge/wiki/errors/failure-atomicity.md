---
title: Failure atomicity
category: errors
summary: "A method assigns one field and then reaches a check or call that can throw before assigning the rest, so a failure leaves the object half-updated; or the code saves fields to temporaries to roll back by hand."
tags: [rule, failure-atomicity, exceptions, mutation]
paradigm: any
sources: [elegant-objects]
created: 2026-11-02
updated: 2026-11-03
---

Failure atomicity means that an operation either produces a whole, consistent object or fails, and leaves no state in between. Bugayenko counts it among the benefits of [[immutable-objects]] (pp. 79-81), and takes the term from Bloch's *Effective Java*.

## Rule

An operation that can fail must not change state before the point where it may fail. Immutable objects meet this for free, because they compute everything and only then build a new object: «Неизменяемые объекты избавлены от такого недостатка, поскольку ничего не модифицируют внутри себя» (p. 80). The book grants that a mutable object can be made atomic too, but says that doing so takes special care, adds complexity and makes mistakes more likely (p. 81). Its example saves `dollars` in a temporary and restores it before throwing. The book finds the code confusing even with two fields, and notes that a field is easy to miss as the object grows (p. 81).

## Sign in code

- Inside one method, an assignment to a field of the receiver is followed by a check that throws, or a call that can fail in a correct program (I/O, parsing, validation, a remote call), or an early return, and only after that are the remaining fields assigned.
- Manual rollback: a field copied to a local variable (`before = this.x`) and written back just before a `throw`.

A method that writes a field of the receiver and can then throw or return before its remaining writes belongs to [[failure-atomicity]]; a field bound by a rule and exposed to a plain setter or a public write belongs to [[class-invariant]]. A resource acquired and not released on the failure path is [[exception-safe-release]].

## When not to apply

- If the method assigns nothing until every check has passed, the object is already atomic, and there is no finding even though it is mutable. The book's claim is that mutability makes this hard to keep, not impossible (p. 81).
- This wiki's own limit: an object that is discarded as soon as the error happens (a local object that is never seen again after the throw) cannot be observed half-updated, so the defect has no effect there.
- This wiki's own limit: deliberate partial progress, such as a batch that records how far it got and reports it on failure, is the method's contract, not a defect.
- This wiki's own limit: state that an enclosing transaction rolls back on the failure (a database row mapped inside one transaction) is not left half-updated where anyone can see it.

## Repair

1. Preferably, make the class immutable: run all checks, and return the new object, as in `new Cash(dollars * f, cents * f)`, as the last statement.
2. If the class must stay mutable, move every check that can throw ahead of the first field assignment.
3. Compute the new values into locals, then assign them all together at the end.
4. Use hand-written rollback only as a last resort.

## Before and after

```
method mul(factor)
  this.dollars = this.dollars * factor
  if centsOverflow(factor)
    throw error              // dollars already changed, cents not
  this.cents = this.cents * factor
```

```
method mul(factor)
  if centsOverflow(factor)
    throw error              // nothing has changed yet
  return new Cash(this.dollars * factor, this.cents * factor)
```

## Source

Bugayenko, *Elegant Objects*, Java Edition, Russian translation (Piter, 2018), section 2.6, pp. 79-81; see [[elegant-objects]]. This wiki's own: the signs as worded, the split with [[class-invariant]] and [[exception-safe-release]], the mutable repair (checks first, assignments last), the limits on discarded objects, deliberate partial progress and enclosing transactions, and the pseudocode. The reading of p. 81 was checked against the page image.
