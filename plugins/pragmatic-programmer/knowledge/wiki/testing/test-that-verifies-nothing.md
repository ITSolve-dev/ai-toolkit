---
title: A test that verifies nothing
category: testing
summary: "A test only names or constructs a class and asserts nothing, or a later test already covers everything it touches; it adds edits on every rename and no information."
tags: [rule, testing, redundant-tests]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-07
---

A test with no real assertion still has a maintenance cost. It passes for the wrong reason, adds nothing beyond the tests that follow it, and has to be edited whenever the name it mentions changes.

## Rule

Do not keep tests that check nothing. The book's example is a test-first habit: before writing a class, the developer writes a test that merely references its name, watches it fail, writes an empty class, and watches it pass. «Но ведь этот тест совершенно ничего не проверяет!» (p. 268). The next test references the class too, so the first is no longer needed, and renaming the class later means more edits in the tests (p. 268).

## Sign in code

- A test body constructs an object or references a name and contains no assertion.
- The only assertion is that an object just constructed is not null, or that its type is the one just named.
- Another test in the same file necessarily exercises everything the test touches, with a stronger assertion.

This wiki assigns the neighbouring cases as follows. This page owns a test with nothing to check. A test some of whose paths assert nothing is [[test-code-is-defect-prone]] when a branch selects the assertion; a test with no assertion on any path is this page. A test that prints a value for someone to compare is [[test-early-often-automatically]]. A test whose assertion was removed counts here, and [[broken-windows]] sends it to this page. Redundant tests inside one class of a condition, while another class of that condition has no test, belong to [[equivalence-partitioning]]; a test whose every effect another test already asserts belongs to [[test-that-verifies-nothing]]. A test that asserts nothing, or that a later test fully covers, is [[test-that-verifies-nothing]]; tests spent on accessors that only read or write a field while risky logic in the same unit goes untested are [[test-by-risk-not-by-method]].

## When not to apply

- The book's complaint concerns tests left behind. This wiki's reading is that a throwaway red step during a cycle is harmless if it is deleted once a real test exists.
- This wiki does not count a deliberate smoke test of packaging or wiring, whose point is that a component loads at all and which nothing else covers. It should say so in its name.
- This wiki keeps a narrower test with a real assertion when its failure names the cause more precisely than the broader test's. [[test-the-contract]] and [[test-levels]] ask for such tests.

## Repair

Delete the test if another test subsumes it. Otherwise give it an assertion about behaviour.

## Before and after

Before: the first test adds nothing that the second does not.

```
test invoice_exists:
    Invoice()

test invoice_total:
    invoice = Invoice(lines = [line(10), line(5)])
    assert invoice.total() == 15
```

After:

```
test invoice_total:
    invoice = Invoice(lines = [line(10), line(5)])
    assert invoice.total() == 15
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020 ([[pragmatic-programmer]]): p. 268. This wiki's own: the second and third signs, the assignment of neighbouring cases (including [[equivalence-partitioning]]), all three limits, the repair's second sentence and the pseudocode. Related: [[test-driven-development]].
