---
title: Boundary value analysis
category: testing
summary: "Procedure for a comparison like x < max or x >= limit with no test at max-1, max and max+1, or arithmetic and totals over several inputs with no test of all inputs at their extremes together."
tags: [method, testing, off-by-one, test-selection]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

**Boundary value analysis** writes tests at the edges of conditions, where off-by-one errors live. McConnell calls boundaries one of the most productive areas of testing, because developers often write `num - 1` for `num` or `>=` for `>` (p. 504). It is a form of error guessing (see [[test-data-classes]]) and completes [[equivalence-partitioning]], which picks values inside classes.

## Simple boundaries

For a range of values less than `max` there are three cases: the largest value below `max`, `max` itself, and the smallest value above `max`. Three tests rule out the common errors (p. 504). For the book's condition `withheld < MAX_GOVT_RETIREMENT` the tests are `MAX - 1` (the true side, reusing basis test 1), `MAX + 1` (the false side, reusing test 3) and a new test for `withheld == MAX` (p. 505). Existing tests from [[structured-basis-testing]] are reused by choosing their values at the boundary. The same analysis applies to the minimum and maximum allowed values of a variable (p. 505).

## Compound boundaries

A subtler boundary depends on a combination of variables (p. 505):

- multiplying two large positive numbers, two large negative numbers, or one of them zero;
- every string passed in being unusually long;
- totals across a large group: the book adds a test of 1000 employees each earning 250,000 a year, to see what happens to the accumulated sums (test 11), and its opposite, a group of ten employees with no salary (test 12).

This wiki reads compound boundaries as the place where overflow, precision loss and accumulated-limit errors show, none of which single-variable boundaries reveal; see [[integer-overflow-and-division]].

## Procedure

This wiki's arrangement of the book's cases:

1. For each comparison in the routine, write tests at the value just on the true side, exactly on the boundary, and just on the false side.
2. For each input's allowed minimum and maximum, do the same.
3. For each arithmetic expression or accumulation over several inputs, add tests where all operands are at extremes together: all large, all negative, one zero.
4. Reuse existing tests by moving their values to the boundary before adding new ones.

## Sign in a test suite

This wiki's own: a comparison such as `x < max` in the code with no test at `max` itself, the case that distinguishes `<` from `<=`; an accumulator or product over several inputs with no test of all inputs at their maximum. A limit the code declares belongs to [[test-the-contract]]. A comparison in the routine's own logic, which declares no limit of the input, belongs to [[boundary-value-analysis]]. A divisor, index or length derived from arguments that never reaches zero or empty in a test is the neighbouring rule [[test-state-coverage-not-line-coverage]]; tests that all run one direction or sign of real use are [[test-boundaries-and-realistic-use]].

## Limits

This wiki adds: for inputs with no order (identifiers, enumerations without order) there is no boundary, so use [[equivalence-partitioning]] instead. Where the type itself cannot hold the out-of-range value, the outside-of-boundary test is replaced by a test at the type's limit.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 22.3, pp. 504-505, via [[code-complete]]. The three-case rule, the compound examples and the payroll tests are the book's; the procedure list, the sign, the neighbour assignments and the limits are this wiki's own.
