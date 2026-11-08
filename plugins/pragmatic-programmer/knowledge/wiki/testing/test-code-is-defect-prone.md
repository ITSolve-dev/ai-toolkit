---
title: Tests carry as many defects as the code they test
category: testing
summary: "A test computes its expected value with loops or branches that re-implement the code under test, so a shared mistake passes; tests hold as many defects as the code, so they are built and reviewed like code."
tags: [rule, test-quality, test-data]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell describes a familiar afternoon: hours spent reading correct code and recomputing results, until the defect turns out to be in the test data (pp. 512-513). He reports that this is common: «Зачастую сами тесты содержат не меньше, а то и больше ошибок, чем тестируемый код» (p. 513). The cause he gives is that tests are written on the fly, treated as disposable, and built with matching care. Defects in tests are more annoying than defects in the code, because finding them costs time and improves no code (p. 523, key points).

## Rule

Design and build tests as carefully as production code: step through each test's code, review and inspect the test data, plan tests early so they are not built on wrong assumptions, keep tests for regression rather than discarding them, and put unit tests into the project's test framework so they are not thrown away (p. 513).

## Sign in code

The signs are this wiki's own reading of the rule:

- The expected value is computed inside the test by a loop, a branch or a formula that repeats the logic of the code under test, so the test has room for the same defect and passes with it.
- A test contains conditional logic that decides what to assert (`if result.kind == X: assert ...`), so some runs assert nothing.

This wiki assigns the neighbouring cases as follows. A check that prints output for a person instead of asserting, or an ad-hoc driver outside the suite, is [[test-early-often-automatically]]. An expected value computed in the test by logic that repeats the code under test is [[test-code-is-defect-prone]]; an expected literal whose derivation cannot be checked mentally is [[test-values-checkable-by-hand]]. A test whose ability to fail was never seen is checked by [[sabotage-your-tests]]. A test some of whose paths assert nothing is this page when a branch selects the assertion; a test with no assertion on any path is [[test-that-verifies-nothing]]. This page owns test code whose own logic can be wrong.

## When not to apply

- A scratch probe run once to answer a question during debugging is not a test and owes no such care, provided it is not left behind posing as one. This limit is this wiki's own.
- An expected value computed by an independent route, such as a reference implementation, an inverse operation or a property, is an oracle, not a re-implementation; see [[property-based-testing]] and [[independent-checking-tool]]. This limit is this wiki's own.

## Repair

Make the expected value a literal, or derive it in one visible line from round inputs; remove branches that decide what to assert by splitting the test per case; review fixtures and test data as code; when a test fails, treat the test and its data as suspects alongside the code (p. 513).

## Before and after

```
test total_applies_discounts:
    items = [item(30), item(120), item(200)]
    expected = 0
    for i in items:
        expected += i.price * (0.9 if i.price > 100 else 1)
    assert total(items) == expected
```

```
test total_applies_discount_above_100:
    items = [item(30), item(120), item(200)]
    // 30 + 120 * 0.9 + 200 * 0.9
    assert total(items) == 30 + 108 + 180
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]]: pp. 512-513 (the anecdote, the claim and the four tips: check your work, plan tests as you plan development, keep tests, build unit tests into the test framework) and p. 523 (the key point on the cost of defects in tests). This wiki's own: the signs, the owner assignments, both limits, the repair beyond the book's tips, and the pseudocode.
