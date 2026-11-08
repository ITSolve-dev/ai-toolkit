---
title: Structured basis testing
category: testing
summary: "Procedure to count the minimum tests a routine needs (1, plus each if/while/for/and/or, plus each case and a missing default) and derive one true and one false case per decision, so every statement runs."
tags: [method, testing, coverage, cyclomatic-complexity]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

**Structured basis testing** is McConnell's procedure for deriving the minimum set of tests that executes every statement of a routine, with each decision taken both ways (pp. 497-500). It differs from generic code coverage or logic coverage in aiming at the *minimum* number of tests for the same paths; coverage-driven testing can produce far more tests for the same logic (p. 497). The procedure is similar to the complexity measure of section 19.6 (p. 497), which this wiki keeps as [[decision-point-count]].

## Procedure

1. Start with **1** for the straight path through the routine.
2. Add **1** for each `if`, `while`, `repeat`, `for`, `and`, `or`, or their equivalents.
3. Add **1** for each `case`; if the `case` statement has no default branch, add **1** more.

The result is the minimum number of tests, not a guarantee: six arbitrary tests will almost certainly not cover the basis (p. 499). To make them cover it, walk the same keywords used for counting: each represents something that can be true or false, and the suite needs at least one test for each true and each false outcome (p. 499). An `and`/`or` operand is its own decision, so a condition `a and b` needs a test where it is false because `a` is false and another where it is false because `b` is false (the book's tests 4 and 5, p. 500).

## Worked shape

The book's payroll routine (pp. 498-499) has a `for` over employees containing three `if` statements, one with `&&`. Count: 1 + for + if + if + && + if = 6. The suite: (1) nominal, all conditions true; (2) loop condition false, no employees; (3) first `if` false; (4) second `if` false via its first operand; (5) second `if` false via its second operand; (6) third `if` false (p. 500).

```
count = 1                        // the routine
for each employee:               // +1 -> 2
    if withheld < MAX:           // +1 -> 3
        ...
    if wants and eligible:       // +1 (if) +1 (and) -> 5
        ...
    if eligiblePersonal:         // +1 -> 6
        ...
```

## What it does not cover

- **Data variation.** It guarantees only that all code executes (p. 500). Follow with [[data-flow-testing]], then [[equivalence-partitioning]], [[boundary-value-analysis]] and [[test-data-classes]].
- **Statement coverage is not branch coverage.** The book warns that most developers stop at 100% statement coverage (p. 496). This wiki reads the true/false-per-keyword step above as what moves the suite beyond it. See [[code-coverage]].

## Design consequence

The count grows quickly with routine complexity; shorter routines and boolean expressions with few `and`/`or` operators have fewer cases. McConnell names ease of testing as another reason to shorten routines and simplify boolean expressions (p. 500). This wiki reads the count as a review signal: a routine whose basis count is too large to write tests for by hand is a candidate for splitting ([[decision-point-count]], [[name-complex-conditions]]) rather than for a larger suite.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 22.3, pp. 496-500, via [[code-complete]]. The pseudocode is this wiki's; the reading of the count as a split signal extends the book's own remark on p. 500 and is this wiki's, as is the reading of the true/false step as what moves a suite past statement coverage.
