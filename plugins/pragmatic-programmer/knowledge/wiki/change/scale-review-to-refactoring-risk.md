---
title: Scale care to refactoring risk
category: change
summary: "A refactoring that reshapes a routine or class interface, a persisted schema or a boolean expression shares one step (one commit) with other refactorings, in a diff small enough to judge, so the risky move is not isolated."
tags: [decision-rule, refactoring, review, risk]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell asks for care in proportion to a refactoring's risk (pp. 567-568).

## Rule

Decide the procedure by the kind of refactoring (pp. 567-568):

- **Low risk.** The book's example is the refactoring «замена магического числа на именованную константу», which it calls relatively safe (p. 567). Several such refactorings may be done together, with regression tests and no formal review.
- **Higher risk.** Refactorings that change a class or routine interface, a database schema or a boolean test. Do them one at a time, and have someone review the change or refactor in a pair, in addition to compiler checks and unit tests (pp. 567-568).

The same section warns that small changes are where programmers are least careful; the figures and the moral are on [[find-bugs-once]], which owns a small fix with no test.

## Sign in code

A refactoring that reshapes a routine's parameters or return, a public member of a class, a persisted schema, or a boolean expression (De Morgan, reordered or merged conditions) sits in the same step as other refactorings, so it cannot be judged or reverted on its own.

Whether a step was reviewed or paired is not in the code; ask for it rather than assume it.

This wiki assigns the neighbouring cases as follows. Restructuring of code no test covers, or a large structural diff with no green state between its steps, is [[refactor-in-small-tested-steps]]; a refactoring of an interface, a schema or a boolean expression that shares its step with other refactorings is [[scale-review-to-refactoring-risk]]. A change that alters behaviour, such as `<` turned into `<=`, is not a refactoring: inside a refactoring it is [[do-not-refactor-while-adding-features]], and as a fix with no test it is [[find-bugs-once]]. A loop bound flipped until a test passes is [[check-loop-boundaries-by-hand]]; a public interface change that callers will not notice at build time is [[break-the-build-on-interface-change]].

## When not to apply

- Naming a literal needs no separate review by the book's own scale (p. 567); this wiki puts renaming a local in the same class.
- This wiki notes that an automated, tool-verified rename of a public member is lower risk than a hand edit, though the interface still changes for callers outside the tool's reach.

## Repair

Split the step: put each risky refactoring in its own commit, add a test that pins the result it must keep if none does, and get a review or pair on it. Leave the low-risk refactorings batched ([[refactor-in-small-tested-steps]]).

## Before and after

```
// before: one commit
//   rename local tmp to total
//   reorder parameters of charge(amount, account) to charge(account, amount)
//   rewrite  not (expired and unpaid)  as  not expired or not unpaid
```

```
// after: three commits, tests green after each
// 1. rename local tmp to total
// 2. reorder parameters of charge; test pins charge(account, 10) == old result
// 3. rewrite the condition by De Morgan; test pins all four expired/unpaid cases; reviewed
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition: [[code-complete]], section 24.4, pp. 567-568. The risk scale and the procedure for each level are the book's, paraphrased except where quoted; the quotation was transcribed from the extracted text. The signs, the assignment against neighbouring pages, the reading of "boolean test" as a behaviour-preserving rewrite of a condition, the limit on renaming a local and on automated renames, the repair as phrased and the example are this wiki's own.
