---
title: Order comparisons along the number line
category: complexity
summary: "A range test written with the variable first in both halves (i > MIN and i < MAX, x >= lo && x <= hi): rewrite as MIN <= i and i <= MAX, or i < MIN or MAX < i for outside the range."
tags: [rule, boolean-expressions, comparisons, range-check, readability]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

A numeric comparison is easier to check when its operands appear in the order they lie on the number line. McConnell asks that range tests be laid out from smallest to largest, so the reader can picture the interval the code accepts (*Code Complete*, section 19.1, pp. 433-434).

## Rule

Write comparisons so the terms run from left to right, smallest to largest: «Идея в том, чтобы расположить элементы по порядку слева направо» (p. 433). For a value inside a range, the bounds go at the edges and the value in the middle: `MIN_ELEMENTS <= i and i <= MAX_ELEMENTS`. For a value outside it, the value goes at the edges and the bounds in the middle: `i < MIN_ELEMENTS or MAX_ELEMENTS < i` (p. 433). With a single bound, place the value on the side where it should lie when the test succeeds: `i < MIN_ELEMENTS` if it should be smaller, `MIN_ELEMENTS < i` if larger (p. 434). The book contrasts this with `( i > MIN_ELEMENTS ) and ( i < MAX_ELEMENTS )`, which does not let the reader picture the test (p. 434).

## Sign in code

- A two-sided range test in which the variable is the left operand of both comparisons, so one uses `>` and the other `<` (`x > lo and x < hi`, `x >= lo && x <= hi`).
- An outside-range test in which the variable is first in both halves (`x < lo or x > hi`).
- A range test whose two halves are written in opposite directions with the bounds in no fixed place, so inclusive and exclusive ends must be worked out operand by operand.

## When not to apply

The book states one conflict: putting constants on the left of `==` to catch accidental assignment contradicts this ordering, and McConnell prefers the ordering and relies on compiler warnings (p. 436). Further limits are this wiki's own:

- Where the language offers chained comparisons or a range construct (`lo <= x <= hi`, `x in lo..hi`), use it; it states the same picture with one mention of the variable.
- For a single comparison against a bound, the gain is small, and a project convention of writing the variable first should win; this page fires on two-sided tests.
- A comparison of two variables with no fixed order between them (`a < b` where either may be larger) has no number line to follow.

## Repair

1. Identify the interval the test accepts, with its inclusive and exclusive ends.
2. Inside the range: write `lower <op> value and value <op> upper`, using only `<` or `<=`.
3. Outside the range: write `value < lower or upper < value`.
4. If the language has a range construct or chained comparison, use that instead.

## Before and after

Before: the reader must flip one comparison to see the interval.

```
if lineCount > MIN_LINES and lineCount <= MAX_LINES:
    accept()
if temperature < LOW or temperature > HIGH:
    alarm()
```

After: the code reads in the order of the number line.

```
if MIN_LINES < lineCount and lineCount <= MAX_LINES:
    accept()
if temperature < LOW or HIGH < temperature:
    alarm()
```

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, section 19.1, pp. 433-434 and 436. The rule, the inside and outside layouts, the single-bound placement, the counterexample and the stated conflict with constants-on-the-left are the book's. The signs, the limits other than that conflict, and the pseudocode are this wiki's own. Related: [[name-complex-conditions]], [[stair-step-lookup-boundaries]].
