---
title: Sabotage your tests
category: testing
summary: "Procedure for a test whose ability to fail was never seen: inject the fault it guards against, confirm it goes red for that reason, and strengthen it if it stays green."
tags: [method, test-quality, mutation, regression]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

A test is code and can be wrong. The only direct evidence that a test detects a fault is watching it detect one, so the method is to introduce the fault on purpose and see what the test does.

## Why

Thomas and Hunt argue that if nobody can write perfect software, nobody can write perfect tests either, so tests need testing themselves (p. 334). They compare a suite to a security system, which is best checked by trying to break in (p. 335). The tip reads «Пользуйтесь саботажем для проверки своих тестов» (p. 335).

## Procedure

The book gives two scales.

**One test.** «Как только вы напишете тест для выявления конкретной программной ошибки, вызовите ее намеренно и убедитесь, что тест предупредит о ней.» (p. 335).

**A suite.** If you take testing seriously, the book says, make a separate branch of the source tree, plant bugs deliberately and confirm the tests catch them (p. 335).

This wiki spells the steps out as follows:

1. Take the test and the line of production code it is meant to guard.
2. Change that line to the fault: flip a comparison, drop a check, return a constant, shift a boundary by one.
3. Run the test. It should go red, and its message should point at the fault.
4. If it stays green, the test does not pin that behaviour. Strengthen the assertion or the input.
5. If it goes red for another reason, such as a crash in setup, that is not evidence. Fix the test and repeat.
6. Revert the change. Doing this on a separate branch, as the book says, keeps sabotage out of the main line.

This wiki notes that the suite-level practice is what tooling calls mutation testing. The book does not use that name in this passage.

## What it exposes

This wiki lists the defects the method tends to find:

- An assertion that cannot fail: it checks only that no exception was raised, or compares a value with itself. See [[test-that-verifies-nothing]].
- A test that asserts what a mock was told to return.
- A boundary that is never pinned, as in the example below. See [[test-state-coverage-not-line-coverage]].
- A test that is filtered out and never runs.

## Worked example

The tests stay green after `age >= 18` is changed to `age > 18`, so the boundary is not pinned:

```
function is_adult(age):
    return age >= 18

test "adults":
    assert is_adult(30)
    assert not is_adult(5)
```

After strengthening, the same sabotage turns the test red:

```
test "adults":
    assert is_adult(30)
    assert not is_adult(5)
    assert is_adult(18)
    assert not is_adult(17)
```

## Limits and cost

The book addresses suite-level sabotage to those who take testing seriously (p. 335). This wiki reads that as a step beyond the baseline, not as part of it. This wiki adds that sabotaging a whole suite multiplies its run time by the number of planted faults, so it suits a small critical module better than a full code base. This wiki also notes that a planted change that does not alter behaviour cannot be caught, so a surviving change is not automatically a gap.

The book extends the idea to disabling running services with Chaos Monkey (p. 335). That level is system operation and falls outside this wiki's scope.

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation (Dialektika, 2020), see [[pragmatic-programmer]], pp. 334-335.

This wiki's own: the numbered steps beyond the book's two sentences, the mutation-testing gloss, `## What it exposes`, the worked example, and the cost and surviving-change points in `## Limits and cost`.
