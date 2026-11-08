---
title: "Floating values are approximate: no equality, no mixed magnitudes"
category: types-and-state
summary: "Two floating-point values compared with == or !=, a loop that accumulates a float and tests it for an exact value, a sum that adds a very small value to a very large one, or a fixed absolute epsilon over values of very different scale."
tags: [rule, floating-point, equality, rounding, arithmetic]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

*Code Complete* starts its floating-point section from one fact: many decimal fractions cannot be represented exactly in binary, so a floating value carries only a limited number of significant digits (Russian edition, p. 286). Two consequences show up as specific code shapes: exact comparison and addition across magnitudes.

## Rule

- **Do not compare floating values for equality.** Two routes to the same number need not produce the same result: «если 10 раз сложить 0,1, то 1,0 получается только в редких случаях» (p. 286). The book's Java loop adds 0.1 ten times and prints `Numbers are different.`, the running sum reaching 0.9999999999999999 (p. 287). Its repair is a function that reports two values equal when they differ by less than an accepted tolerance (p. 287), and it notes that a fixed tolerance may be wrong: it may have to be computed from the size of the values compared (p. 288).
- **Avoid adding or subtracting numbers of very different magnitude.** In 32 bits, 1 000 000.00 + 0.1 is probably 1 000 000.00, and 5 000 000.02 − 5 000 000.01 is probably 0.0 (p. 286). If such sums are needed, sort the values and add from the smallest; for a series, sum from the smallest term. The book says this minimises the error but does not remove it.
- **Rounding errors share the cause**, and the book lists repairs for them: a type of higher precision, a decimal type, or integers in a smaller unit (p. 288). Where the values are money, those repairs are [[exact-representation-for-money]].

## Sign in code

- `==` or `!=` between two floating-point expressions, or between a floating expression and a non-trivial literal (`if total == 1.0`).
- A loop whose exit condition tests a float accumulated inside it for an exact value: `while x != 1.0: x += 0.1`.
- A running sum into a float where the terms differ from the total by many orders of magnitude, such as adding small increments to a large balance or summing a long series from its largest term.
- A tolerance-based comparison whose tolerance is a fixed absolute constant while the values compared range over many orders of magnitude.

This wiki assigns neighbouring cases as follows. This page owns comparisons and accumulation on floating values. Money or other quantities that must balance exactly, stored in a floating type, is [[exact-representation-for-money]], whatever comparison is used on them. Mixed integer-floating comparisons are [[integer-overflow-and-division]].

## When not to apply

The book states no limits here. The limits below are this wiki's own:

- **Comparison with a value that was assigned, not computed**, such as a sentinel 0.0 set explicitly and tested before any arithmetic, is exact. The sign is a computed value on either side.
- **Values that are exactly representable throughout**, such as small integers held in a double and only added, compare exactly; the page fires on fractions and on division.
- **A language or library that offers an approximate-equality function** is the repair, not an exception; use it rather than writing one.
- **Cost when followed:** a tolerance is a decision about the domain. A tolerance chosen carelessly hides real differences, so a codebase-wide `EPSILON` is itself a sign to check.

## Repair

1. Replace exact comparison with a comparison within a tolerance, and choose the tolerance from the domain: absolute for values of known scale, relative to the operands' magnitude otherwise (p. 288).
2. Replace a loop exit on an accumulated float with a loop over an integer count, computing the float from the count.
3. For sums across magnitudes, add from the smallest term, or accumulate in a wider type.
4. Where the values must balance exactly, change the representation; see [[exact-representation-for-money]].

## Before and after

```
sum = 0.0
for i = 1 to 10
  sum = sum + 0.1
if sum == 1.0
  report("complete")

x = 0.0
while x != 1.0
  plot(x)
  x = x + 0.1
```

```
sum = 0.0
for i = 1 to 10
  sum = sum + 0.1
if nearly_equal(sum, 1.0, tolerance = TOLERANCE)
  report("complete")

for step = 0 to STEPS - 1
  plot(to_float(step) / STEPS)
```

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, chapter 12: representation and limited digits, p. 286; magnitudes and summing from the smallest, p. 286; equality, the 0.1 loop and its output, pp. 286-287; the tolerance function, p. 287; computing the tolerance from the values and the list of rounding repairs, p. 288. The quotation of p. 286 is transcribed from `raw/` and needs the page-image check. This wiki's own: the loop-exit and fixed-epsilon signs, all limits, the integer-count repair and the pseudocode.
