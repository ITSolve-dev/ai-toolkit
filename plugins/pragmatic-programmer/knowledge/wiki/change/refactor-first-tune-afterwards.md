---
title: Refactor first, tune afterwards
category: change
summary: "A structural improvement declined or reverted for speed with no measurement (a loop kept fused, a temp kept for one lookup, a split undone), justified by a comment, review remark or commit message citing performance; finish the refactoring, then measure and tune."
tags: [decision-rule, performance, refactoring, loops, temporary-variables]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Several refactorings in Fowler's example make the code do more work: a lookup runs three times per iteration instead of once ([[replace-temp-with-query]]), and one loop becomes three ([[remove-loop-accumulator]]). He expects readers to object, and answers in two parts. Most of the time the cost is not noticeable, because most programmers, even experienced ones, "are poor judges of how code actually performs", and the performance of software usually depends on a few parts of the code (ch. 1, PDF p. 27). When a refactoring does have a significant cost, he usually does it anyway, because well-factored code is easier to tune; tuning may reverse some of the refactoring, but more often allows a more effective improvement, leaving code "both clearer and faster" (PDF p. 27).

This wiki assigns the neighbouring cases as follows. A structural improvement declined or reverted for speed with no measurement (a loop kept fused, a temp kept for one lookup) is [[refactor-first-tune-afterwards]]; a statement-level trick written for speed with no measurement is [[premature-code-tuning]]. A loop body computing unrelated results is [[one-loop-one-job]], which owns the shape; where speed is the stated reason for keeping it fused and no measurement backs that, [[refactor-first-tune-afterwards]] answers the reason. Where to put a fix once a measurement exists is [[fix-performance-at-the-right-level]].

## Rule

Fowler's advice: "Most of the time you should ignore it. If your refactoring introduces performance slowdowns, finish refactoring first and do performance tuning afterwards." (PDF p. 27).

## Sign in code

- A comment citing speed beside a fused loop (one body accumulating several totals and building output) or a lookup kept in a temp, with no profile or timing naming that code as a hot spot.
- Where the diff, review or history is in hand: a review remark or commit message giving speed as the reason to keep that shape, or a refactoring reverted because it repeats a loop or a call, with no timing before and after.

The sign is the stated speed reason together with the missing measurement; the fused loop alone is [[one-loop-one-job]]'s.

## When not to apply

- Fowler's own qualification: "most of the time" is not always; a measured, significant slowdown is tuned, and the tuning may reverse part of the refactoring (PDF p. 27).
- This wiki's limit: the repeated work is not cheap in kind, such as a file, network or database read, a system call, or a loop over a collection large enough that the profile already names it; then the split or the repeated call is designed with the cost in view ([[fix-performance-at-the-right-level]]).
- This wiki's limit: the repeated call has side effects or is not deterministic, so repeating it changes behaviour, not only speed.
- This wiki's limit: the sequence can be traversed only once (a stream, a network read), so a split loop is not available; [[one-loop-one-job]] states the same limit.

## Repair

Proceed with the refactoring. If performance is a requirement, measure after it and tune only the parts the measurement names, on the now well-factored code ([[code-tuning-procedure]]).

## Before and after

```
// before: kept fused "for speed", never measured
// perf: one pass is faster
for perf in invoice.performances:
    credits += creditsFor(perf)
    text += line(perf)
    total += amountFor(perf)
```

```
// after: split; timed before and after, no difference worth a fused loop
for perf in invoice.performances: text += line(perf)
text += footer(totalAmount(invoice), totalCredits(invoice))
```

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 1, "Removing Total Volume Credits", PDF pp. 19, 27. The rule, its reasoning and its qualification are the book's. This wiki's own: the signs, the limits on expensive, side-effecting or single-pass work, the selecting sentences against [[premature-code-tuning]] and [[one-loop-one-job]], and the pseudocode.
