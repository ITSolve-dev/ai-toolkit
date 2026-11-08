---
title: Refactor early and often
category: change
summary: "Another page's finding (duplicated logic, a misleading name, a clean-up TODO) left standing on or beside lines the change touches. This page rules on when to act, not on what is wrong."
tags: [rule, refactoring, technical-debt, timing]
paradigm: any
sources: [pragmatic-programmer, fowler-refactoring]
created: 2026-11-01
updated: 2026-11-07
---

Structural problems cost less to fix while they are small, and they do not stay small. The book's tip is «Выполняйте рефакторинг кода как можно раньше и чаще» (p. 262).

## Rule

When you notice code that is wrong in structure, change it soon, and do not defer it to a future that will have less room. The book says not to hesitate and that the change is best made at once (p. 261).

The book's reasoning is that the cost grows: fixing the problem later takes much more time, and later there are more dependencies to reckon with (p. 262). It rejects lack of time as an excuse, on that same ground. Its analogy is a growth that is easily removed while small and dangerous once it spreads (p. 262). Refactoring, like most techniques, is easier while the problems are small, as a routine part of programming (p. 262). This also connects to leaving no broken windows (p. 264; see [[broken-windows]] and [[software-entropy]]).

The claim that deferral costs more is argued by the book and not measured in it.

Fowler's *Refactoring* calls the same case litter-pickup refactoring: code that is understood but done badly, such as convoluted logic or near-identical functions one parameterized function could replace. He grades the timing by effort: if it is easy to change, he does it right away; if it is a bit more effort, he may note it and fix it when the immediate task is done; if it would take hours, he still makes it a little better (2nd ed., ch. 2, PDF pp. 63-64). **The two books, resolved per setting.** This wiki reads them as agreeing on a fix of minutes on lines the change touches: do it now. They part on a fix larger than the current task can absorb, where *The Pragmatic Programmer* still says at once and Fowler says after the task. This wiki follows Fowler there, since the first limit below already concedes that large work cannot start at once: record it, do it straight after the task, and leave the touched lines a little better meanwhile.

## Sign in code

This page has no defect sign of its own. It rules on when to act, and the sign is a relation: a structural finding of another page sits on or beside lines the change touches, and the change leaves it. Those pages own what is wrong:

- two passages encoding the same knowledge: [[dry]];
- a name stating something other than what the code now does: [[rename-when-meaning-drifts]];
- a comment admitting a defect or clean-up: [[broken-windows]].

Go to the owner to learn whether the finding holds, and come here to decide when to act on it. Whether to act now on a finding on lines a change touches is [[refactor-early-and-often]]; which code deserves the effort is [[where-to-refactor]]; the occasions in the course of work that call for refactoring are [[when-to-refactor]]. Two copies already standing in code are [[dry]]; a copy a diff adds as the route for a feature or fix, beside the function it copies, is [[preparatory-refactoring]]. The book's moment for tidying, right after new code passes a test (p. 261), is a time to act and not a sign. Two components that must always be edited together show only in the change history. The remaining triggers listed in [[refactoring]] (usage, performance, outdated knowledge) cannot be read from the code either. They need facts about how the system is used.

## When not to apply

- The work is too large to do in passing. Then you may be unable to start at once, and the book says to schedule it and tell users when it will happen and how it may affect them (p. 262).
- The code has no tests. Write them first ([[refactor-in-small-tested-steps]]).
- You are mid-way through a feature. This wiki resolves the conflict with [[do-not-refactor-while-adding-features]] as follows: do it now, as a separate change, before or straight after the feature. "Soon" never means "in the same change".
- The motive is taste. The book's footnote warns this can go too far, describing a developer who rewrote all the code he inherited only because he had his own naming conventions (p. 251).
- Replacement carries a schedule cost. The book accepts this on the stated assumption that acting costs less than not acting (p. 251), so the assumption needs to hold for the case at hand.

## Repair

1. Fix the structural problem you noticed, within the current piece of work's reach, as its own change.
2. Where that is not possible, record what to change, why, and how far it reaches. A bare TODO is not such a record, and it is the sign of [[broken-windows]].
3. Keep steps small, as in [[refactor-in-small-tested-steps]].

## Before and after

```
// before: the second copy was added this week
function invoiceTotal(lines):
    return sum(lines, l -> l.price * l.quantity) * 1.2

function quoteTotal(lines):
    return sum(lines, l -> l.price * l.quantity) * 1.2   // TODO merge with invoiceTotal
```

```
// after
function grossTotal(lines):
    return sum(lines, l -> l.price * l.quantity) * (1 + VAT_RATE)
```

## Source

[[pragmatic-programmer]], Topic 40, pp. 261-264, and Topic 38, p. 251, for the footnote and the schedule assumption. The sign as a relation, the split with the pages that own each finding, the resolution with feature work, the assignment against [[where-to-refactor]], repair steps 1-2 and the example are this wiki's own.

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 2, "Litter-Pickup Refactoring", PDF pp. 63-64: the case and its three tiers of timing. The resolution between the two books by the size of the fix is this wiki's own.
