---
title: Prove it, don't assume it
category: debugging
summary: "A routine on the failing path is passed over because it is tested or long-used, though its tests never use the failing data, context or boundary."
tags: [rule, debugging, assumptions]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

Surprise during debugging is evidence that a belief about the code is false. This rule turns that surprise into a check of the belief, in the circumstances of the failure.

## Rule

The tip reads «Не предполагайте, а доказывайте» (p. 133). The book says the size of your surprise matches the size of your trust in the code, so a surprising failure means that at least one of your assumptions is wrong (p. 133). «Не обходите стороной подпрограмму или фрагмент кода, связанный с ошибкой, лишь потому, что твердо уверены в его работоспособности» (p. 133). The test of a suspect is whether it works «в таком контексте, с такими данными и при таких граничных условиях» (p. 133). A defect can sit in code used for years (p. 133). The checklist asks the same thing: if suspect code passes its unit tests, how complete are they, and what happens when they run with this data (p. 134)?

## Sign in code

- A routine lies on the failing path, its tests pass, and none of their inputs has the shape of the failing input.
- A comment on the path states a belief with no check beside it, such as a claim that a value can never be negative here. [[assert-the-impossible]] owns that shape. This page adds only that a reported failure runs through the line, so the belief is the first thing to check.
- A debugging note or commit clears a component by its age or its test status, with no run against the failure's data.

## When not to apply

The limits are this wiki's own.

- Code that is off the failing path. The rule covers what the failure touches and is not a demand to re-verify the whole system.
- A component already cleared by a run with the failure's actual data. Repeating that is noise.
- Order of work: [[select-isnt-broken]] still says to look at your own code before the platform. That rule decides what to examine first. This one decides what counts as clearing it, and a platform call cleared by reasoning alone is not cleared.

## Repair

1. List the routines on the failing path, including the ones you trust.
2. For each, run it with the failure's data and boundary conditions, in a test where possible.
3. Where a belief is stated in a comment, turn it into a check: see [[assert-the-impossible]].
4. Keep the case that exposed the false belief, then follow [[after-a-surprising-bug]].

## Before and after

```
// before: daysIn was skipped because it is tested and old
test "days in month":
    assert daysIn(2023, 1) == 31
    assert daysIn(2023, 2) == 28

// report: an invoice dated 29 February is rejected
```

```
// after: the trusted routine gets the failure's data
test "days in month":
    assert daysIn(2023, 1) == 31
    assert daysIn(2023, 2) == 28
    assert daysIn(2024, 2) == 29    // fails, so the belief was false
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation: [[pragmatic-programmer]], pp. 133-134. The rule, the link between surprise and trust, and the demand to check context, data and boundaries are the book's. The signs, limits, repair steps and pseudocode are this wiki's own.
