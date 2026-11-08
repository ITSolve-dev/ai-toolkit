---
title: One verification per test
category: testing
summary: "One test case asserts two or more independent results of the code under test (shortfall, then profit, then the effect of a change), so the first failed assertion stops the test and hides whether the others hold."
tags: [rule, assertions, setup-exercise-verify, arrange-act-assert]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Fowler states a general rule: "it’s wise to have only a single verify statement in each it clause" (ch. 4, Modifying the Fixture, PDF p. 112). His reason is diagnostic. A test stops at its first failed check, so later checks never run, and that "can often hide useful information when you’re figuring out why a test is broken" (PDF p. 112).

## Rule

Put one verification in each test case. When a test checks several things, split it into separate tests over the same fixture and the same exercise step.

A test has phases, variously called setup-exercise-verify, given-when-then or arrange-act-assert (PDF p. 112). It takes the fixture, exercises it and verifies the outcome. Common early phases can move into a shared per-test setup. Fowler names an implicit fourth phase, teardown, which is usually left to the framework ([[fresh-fixture-per-test]]).

## Sign in code

A single test case with two or more assertions about independent results of the code under test. Several assertions that describe one result, such as the fields of one returned value, are a weaker case. This wiki's test: the assertions follow different exercise steps, or they check one step and a failure of either would not explain a failure of the other.

## When not to apply

- Fowler keeps two checks in one test when he feels "the two are closely enough connected": shortfall and profit after one change of production (PDF p. 112). He keeps the option to split them later. This wiki reads that limit as covering two checks of one exercise step where a failure of one explains a failure of the other, as shortfall and profit both derive from the total production the change updates.
- This wiki adds: a framework that reports every failed assertion in a test, instead of stopping at the first, removes the reason for the rule.

## Repair

Move each independent assertion into its own test. Keep the exercise step in each test, or move it into setup if all the tests share it. Name each test after what it checks, so that the report says which one failed (Fowler on naming tests, PDF p. 107).

## Before and after

```
test "province":
    asia = Province(sampleData())
    assert asia.shortfall == 5
    asia.price = 25
    assert asia.profit == 355          # never runs if shortfall is wrong
    asia.demand = 0
    assert asia.profit == 0
```

```
beforeEach: asia = Province(sampleData())

test "shortfall":    assert asia.shortfall == 5
test "higher price":
    asia.price = 25
    assert asia.profit == 355
test "zero demand":
    asia.demand = 0
    assert asia.profit == 0
```

Related: [[self-testing-code]], [[test-that-verifies-nothing]].

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 4, "Modifying the Fixture", PDF p. 112, and on naming tests, PDF p. 107. The sign as worded, the test by exercise step, the reading of Fowler's exception, the limit for frameworks that report every failure, and the pseudocode are this wiki's own.
