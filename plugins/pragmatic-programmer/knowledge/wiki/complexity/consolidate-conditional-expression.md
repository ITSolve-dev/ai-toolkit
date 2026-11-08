---
title: Consolidate conditional expression
category: complexity
summary: "Two or more consecutive if-checks, or nested ifs with nothing else in the outer one, that each end in the same action or return the same value (if a return 0; if b return 0; if c return 0), written as separate tests that look independent: combine them into one condition with or/and, then name it."
tags: [rule, conditionals, boolean-expressions, refactoring, extract-function]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Fowler's *Consolidate Conditional Expression* folds a series of different checks that lead to the same action into a single check with a single result (*Refactoring*, 2nd ed., ch. 10, PDF pp. 293-295). The refactoring is usually a step on the way to naming the condition, which [[name-complex-conditions]] owns.

## Rule

Where a series of conditional checks differ but the resulting action is the same, combine them with `and` and `or` into one condition (p. 293). Fowler gives two reasons. First, a sequence of separate checks with the same effect "looks like I'm carrying out a sequence of separate checks that just happen to be close together" (p. 293), while the reality is one check made of several. Second, the combined condition sets up Extract Function, which "replaces a statement of what I'm doing with why I'm doing it" (p. 293).

The combining rule is mechanical: "Sequences combine with or, nested if statements combine with and." (p. 294). When a mix of both appears, Fowler uses Extract Function liberally, because things are likely to get messy (p. 295).

## Sign in code

- Two or more `if` statements in a row whose bodies are identical (the same `return` value, the same assignment or the same call), each testing a different condition. Fowler's example: three early `return 0` lines on seniority, months disabled and part-time status (p. 294).
- Two nested `if`s where the outer one has no `else` and no statements besides the inner `if`, so the inner body runs only when both hold (p. 295).
- A run of guard clauses at the top of a routine that all return the same result; Fowler names this as the follow-up to [[guard-clauses]] (p. 297).

This wiki assigns the neighbours as follows. A run of separate checks with one shared result is [[consolidate-conditional-expression]]. Once they are one expression, a condition that is long or whose purpose is unnamed is [[name-complex-conditions]]. A run of checks with *different* results, each a precondition before the main work, is [[guard-clauses]].

## When not to apply

- **The checks are truly independent** and should not be read as one. Fowler: "If I consider it to be truly independent checks that shouldn't be thought of as a single check, I don't do the refactoring." (p. 293). This wiki reads the test as: would a reader want to know which of the reasons fired? If the checks carry different meanings that the code already distinguishes (a different reason code, a different log line), keep them separate.
- **A condition has a side effect.** The mechanics start with "Ensure that none of the conditionals have any side effects." (p. 293). This wiki gives the reason: combining with `or`/`and` short-circuits, so a side-effecting test may stop running. Separate query from modifier first ([[command-query-separation]]).
- **The results only look the same.** This wiki adds: two `return 0` where one zero means "not eligible" and the other "nothing owed yet" are two values that happen to coincide, and merging hides the distinction. The reader checks what each result means in the code (its name, its callers' use) before merging; a guess that they will diverge later is not a sign.

## Repair

1. Check that no condition has a side effect; split any that do.
2. Take two of the statements and combine their conditions: `or` for a sequence, `and` for nesting. Test.
3. Repeat until all are one condition.
4. Consider extracting the resulting condition into a function named for what it means (p. 294), as in [[name-complex-conditions]].

## Before and after

```
function disabilityAmount(employee)
    if employee.seniority < 2 then return 0
    if employee.monthsDisabled > 12 then return 0
    if employee.isPartTime then return 0
    ... compute amount ...
```

```
function disabilityAmount(employee)
    if isNotEligibleForDisability(employee) then return 0
    ... compute amount ...

function isNotEligibleForDisability(employee)
    return employee.seniority < 2
        or employee.monthsDisabled > 12
        or employee.isPartTime
```

Nested form:

```
if employee.onVacation then
    if employee.seniority > 10 then
        return 1
return 0.5
```

```
if employee.onVacation and employee.seniority > 10 then return 1
return 0.5
```

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 10, *Consolidate Conditional Expression*, PDF pp. 293-295, and *Replace Nested Conditional with Guard Clauses*, p. 297: the rule, both reasons, the independence limit, the side-effect precondition and the combining rule. The pseudocode follows the book's examples in this wiki's own notation. The signs as worded, the reader's test for independence, the limit on results that only look alike and the neighbour assignment are this wiki's own.
