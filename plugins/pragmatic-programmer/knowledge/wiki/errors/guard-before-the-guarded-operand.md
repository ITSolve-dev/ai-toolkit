---
title: Guard before the guarded operand
category: errors
summary: "A condition that indexes, divides or dereferences before the check that makes it safe (item[i] != 0 and i < MAX; x/d > m && d != 0), or puts the guard under an operator or call that evaluates every operand: put the guard first under a short-circuit and, or nest the test."
tags: [rule, short-circuit, evaluation-order, boolean-expressions, defensive-code]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Many conditions are safe only because one operand is never evaluated when another has already decided the result. That safety rests on the language evaluating `and`/`or` with short-circuit and left to right. McConnell shows where it holds, where it breaks, and recommends not leaning on it where a reader may not see it (*Code Complete*, section 19.1, pp. 431-433).

## Rule

- An operand that is unsafe unless another holds (an index within bounds, a non-zero divisor, a non-null reference) must be evaluated only after that check. The book's example `while ( i < MAX_ELEMENTS and item[ i ] <> 0 )` fails on the last iteration under full evaluation, since `item[i]` is read with `i` equal to the bound (p. 431). Restructured as a loop on `i < MAX_ELEMENTS` with a nested `if item[i] <> 0`, it is correct whatever the evaluation rule (p. 432).
- With short-circuit evaluation, `( denominator != 0 ) && ( ( item / denominator ) > MIN_VALUE )` is safe, and the logically equivalent expression with the operands swapped divides by zero (pp. 432-433).
- An operator that evaluates all operands removes the protection: the book's example is Java's `&` and `|`, under which the guarded division fails even with the guard first (p. 433).
- The book's recommendation is to check how the language evaluates these operators, and «Еще лучше (поскольку читатель может не обладать вашей сообразительностью) использовать вложенные условия» that do not depend on evaluation order (p. 433).

The book also notes that reading an out-of-range element without changing it is not harmless: it confuses the reader and in many environments raises a run-time error or a protection fault (p. 432). Index discipline in general is [[array-index-discipline]].

## Sign in code

- In one condition, an operand that indexes, divides, dereferences or calls a method on a value, and the check that makes that value safe appears to its right in the same condition.
- The guard and the guarded operand joined by an operator that does not short-circuit: a bitwise `&`/`|` on booleans, or a function or method taking both as arguments (`all(i < n, item[i] != 0)`, `both(d != 0, x / d > m)`), since arguments are evaluated before the call.
- Both parts precomputed into variables before the test (`ok = d != 0; big = x / d > m; if ok and big`).

This wiki assigns the neighbouring case as follows. An index access with no guard at all is [[array-index-discipline]]; this page owns a guard that exists but is evaluated after, or alongside, what it protects.

## When not to apply

The book's preference for nested conditions is a hedge for readers and languages with unclear rules. This wiki resolves it per setting:

- Where the language guarantees short-circuit, left-to-right `and`/`or` and the guard comes first, the single expression is correct and is the common idiom; nesting adds a level of indentation for no safety. Keep the one-line form, and nest only where the guard is far from what it protects or the condition is long.
- Where the language's evaluation of the operator is unspecified or eager, nest the test; this is the book's case.
- Where the guard is a precondition the caller must already have met, the check belongs at the boundary, not in every condition: see [[caller-owns-the-precondition]].

## Repair

1. Find each operand whose evaluation can fail, and the check that prevents the failure.
2. Put the check to the left, joined by the language's short-circuit `and` (or `or` for the negated form).
3. If the operator or a function call would evaluate both, or the language does not guarantee order, nest: test the guard in an outer `if` or loop condition and the guarded expression inside it.
4. Do not precompute a guarded part into a variable ahead of its guard; if naming helps ([[name-complex-conditions]]), name the guard and compute the guarded part only after it.

## Before and after

Before: the division runs before its guard, and an eager call reads one past the end.

```
if (total / count) > THRESHOLD and count != 0:
    flag()

while all(i < n, items[i] != 0):
    i = i + 1
```

After: guard first under a short-circuit and, or nested where evaluation is eager.

```
if count != 0 and (total / count) > THRESHOLD:
    flag()

while i < n:
    if items[i] == 0: break
    i = i + 1
```

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, section 19.1, pp. 431-433. The array and division examples, the failure of the swapped operands, the non-short-circuit Java operators, the note on reading past the end, and the advice to check the language and prefer nested conditions are the book's. The generalisation to any eager construct (function arguments, precomputed variables), the signs, the split with [[array-index-discipline]], the per-setting resolution of nested versus single-expression form, the link to caller preconditions, and the pseudocode are this wiki's own. Related: [[distrust-external-input]], [[crash-early]].
