---
title: All tests pass, all the time
category: testing
summary: "A test is switched off instead of fixed: a skip or expected-failure marker with no stated condition, a commented-out body, or an exclusion by name in configuration. One tolerated failure hides the next."
tags: [rule, testing, test-suite-health]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

A test suite only reports something when its normal state is fully green. Once some failures are accepted as normal, a new failure no longer stands out.

## Rule

«Культура тестирования означает прохождение всех тестов в любое время» (p. 274). If tests that never pass are ignored, it becomes easier to neglect all the tests, and a vicious circle begins (p. 274; see [[software-entropy]] and [[broken-windows]]).

## Sign in code

- A test carries a skip or expected-failure marker with no stated condition for when it stops applying.
- A test body is commented out.
- A test is excluded from the suite in configuration, by name.

This wiki notes that the book's own case, a test left red and ignored, shows in the build's history and not in the code. Only the switched-off form can be pointed at here.

This wiki assigns the two neighbouring shapes by whether the test is switched off. This page owns a test that exists and is switched off. A check that needs a person to run or read it, or new logic with no test, belongs to [[test-early-often-automatically]]. [[broken-windows]] sends a switched-off test here and does not board it, because a skip with a stated condition is this page's record of it.

## When not to apply

The book's wording, «в любое время», admits no exception (p. 274). This wiki adds a limit: a skip with a stated condition is tracked and not ignored, such as a test that applies only on another platform, or one tied to a named open defect with an owner. The test of the limit is whether a reader of the marker can tell when it stops applying.

## Repair

Fix the test or the code it exposes. If the test no longer protects anything, delete it, and say so in the change: a passing test deleted or rewritten to fit new output is [[regression-testing]]. If neither can happen now, record the reason and the condition on the marker, so the skip cannot quietly become permanent.

## Before and after

Before: nobody can tell why it is off or whether it still matters.

```
skip test refund_after_partial_shipment:
    assert refund(order_with_partial_shipment()) == 40
```

After: a real failure was exposed and fixed, and the test runs again.

```
function refund(order):
    return sum(price of unshipped lines of order)

test refund_after_partial_shipment:
    assert refund(order_with_partial_shipment()) == 40
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020 ([[pragmatic-programmer]]): p. 274. This wiki's own: the signs and their assignment against [[test-early-often-automatically]], [[broken-windows]] and [[regression-testing]], the note on what the code can show, the limit, the repair and the pseudocode.
