---
title: Prefer positive conditions
category: complexity
summary: "An if/else whose condition is a negation (if !ok … else …), a double negative such as !notFound, or several not-operators in one test: swap the branches, rename the flag positively, or apply De Morgan."
tags: [rule, boolean-expressions, negation, de-morgan, readability]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Most people find many negations hard to follow, so McConnell asks that conditions be written in positive form where the logic allows it (*Code Complete*, section 19.1, pp. 428-430). He gives three tools: swap the `if` and `else` blocks, rename the variable so its truth value flips, and apply De Morgan's laws.

## Rule

- In an `if` with an `else`, replace a negative condition with a positive one by swapping the blocks (p. 428). The book's verdict on the swapped version: «Второй фрагмент кода логически совпадает с первым, но его легче читать, потому что отрицательное выражение было изменено на положительное» (p. 429).
- Alternatively, rename the variable so the condition becomes positive: the book replaces `statusOK` with `ErrorDetected`, true when `statusOK` would be false (p. 429).
- Use De Morgan's laws to simplify tests with negations: invert both operands, swap `and` with `or`, and invert the whole expression (p. 429). The book's example turns `!displayOK || !printerOK` into `!(displayOK && printerOK)`, with no change to the branches (p. 429). Table 19-1 lists all eight forms (p. 430).

## Sign in code

- `if not X ... else ...`, where both branches are real work and neither is an early exit.
- A double negative: a negated flag whose name is already negative (`not notFound`, `!isNotReady`).
- Two or more `not` operators distributed over the operands of one `and`/`or` (`!a || !b`, `not a and not b`).

This wiki assigns the neighbours as follows. A condition that is hard to read because of its length is [[name-complex-conditions]]. The order of branches in a chain of status checks is [[nominal-path-first]]. A boolean compared to a literal `true` or `false` is [[test-a-value-by-its-kind]].

## When not to apply

The book itself notes a conflict: writing positive conditions sometimes runs against its advice to put the nominal case in the `if` block rather than the `else` (section 15.1, see [[nominal-path-first]]), and leaves it to the reader to weigh the two (p. 429, margin note). This wiki resolves it per setting. In a single `if`/`else` where one branch is the normal path and the other handles an error, the normal path goes first ([[nominal-path-first]]); where the branches are peers, prefer the positive test ([[prefer-positive-conditions]]).

- Where the normal path goes first at the cost of a negation, rename the flag to the sense in which the normal path is true (`if not errorDetected` → `if statusOk`), so the normal path is first and the test is positive.

Further limits, this wiki's own:

- A guard clause with no `else` (`if not valid: return`) is not this sign. The negation states the precondition, and inverting it would nest the whole body ([[guard-clauses]]).
- Renaming a flag to its opposite helps only if most uses read better afterwards; a rename that fixes one condition and creates `not errorDetected` in five others has moved the negation, not removed it.
- De Morgan can make an expression longer, as the book's example does with the outer negation. Apply it when the result names a single meaning (`not (displayOK and printerOK)`, "not both devices ready"), not mechanically.

## Repair

1. If the `if` has an `else` and both branches are peers, invert the condition and swap the blocks.
2. If the flag is named negatively, or most of its uses are negated, rename it to the positive sense and invert its assignments.
3. If several operands are each negated, factor the negation out with De Morgan, and if the inner expression has a meaning, name it ([[name-complex-conditions]]).

## Before and after

Before: the reader holds a negation through both branches.

```
if not statusOk:
    showRetryDialog()
else:
    showResult()

if not displayOk or not printerOk:
    queueForLater(job)
```

After: positive test, blocks swapped; negations factored out and named.

```
if statusOk:
    showResult()
else:
    showRetryDialog()

devicesReady = displayOk and printerOk
if not devicesReady:
    queueForLater(job)
```

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, section 19.1, pp. 428-430. The three techniques, the `statusOK`/`ErrorDetected` rename, the De Morgan example and table, and the noted conflict with nominal-case-first are the book's. The signs, the neighbour assignment, the per-setting resolution of that conflict, the guard-clause exception, the limits on renaming and on De Morgan, and the pseudocode are this wiki's own. Related: [[name-complex-conditions]], [[name-reads-at-the-call-site]].
