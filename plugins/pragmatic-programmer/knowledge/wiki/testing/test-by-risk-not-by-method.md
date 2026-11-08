---
title: Test by risk, not by method
category: testing
summary: "A suite with tests for accessors that only read or write a field, while a function in the same unit with branches, loops, sorting or side effects on other objects has no test, or only a happy-path one."
tags: [rule, risk-driven-testing, test-selection, diminishing-returns]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Fowler chooses tests by where bugs are likely, not by covering every public method. "Testing should be risk-driven; remember, I’m trying to find bugs, now or in the future" (ch. 4, Add Another Test, PDF p. 109). He looks at everything the class should do and tests it for any conditions that might make it fail, and he says this is not the same as testing every public method (PDF p. 109).

## Rule

Spend tests where the code is complex and errors are likely. This wiki lists these as calculations, logic with several steps, setters with side effects and boundary inputs. Do not write tests for accessors that only read and write a field (PDF p. 109). Fowler's advice is to look at where the code becomes complex and to consider the likely areas of error in a function (Probing the Boundaries, PDF p. 116).

The reasoning is about effort and morale as much as coverage. Fowler argues that trying to write too many tests usually leads to writing too few, and that testing has diminishing returns, so an attempt to test every combination can discourage someone into writing none (PDF pp. 109, 116). Hence: "It is better to write and run incomplete tests than not to run complete tests" (PDF p. 109), and "Don’t let the fear that testing can’t catch all bugs stop you from writing tests that catch most bugs" (PDF p. 116).

In the book's example Fowler skips the plain setters. He tests the production setter because it updates derived totals elsewhere, so it has behaviour worth checking (Modifying the Fixture, PDF p. 112).

## Sign in code

This wiki reads the sign as a relation between the tests and the code: the suite tests accessors that only read or write a field, while a function in the same unit with branches, loops, sorting or side effects on other objects has no test, or only a happy-path one.

This wiki assigns the neighbouring cases as follows. A test that asserts nothing, or that a later test fully covers, is [[test-that-verifies-nothing]]; tests spent on accessors that only read or write a field while risky logic in the same unit goes untested are [[test-by-risk-not-by-method]]. A suite that feeds only valid nominal input to a unit is [[test-the-contract]].

## When not to apply

- An accessor that updates derived state elsewhere is worth a test (PDF p. 112). This wiki adds parsing and validation; the book's parsing setters went untested as simple setters until they were probed at the boundaries (PDF pp. 112, 114).
- This wiki adds: a project convention or a published contract that requires a test for every public operation, as in a library's API conformance suite.
- Fowler says over-testing exists but is "vanishingly rare compared to undertesting" (Much More Than This, PDF p. 117). This wiki reads that as: this rule is no licence to cut tests from a suite that is already thin.

## Repair

Delete the tests of trivial accessors if they cost upkeep. Then add tests for the complex function: the main outputs first, then the boundaries ([[test-data-classes]], [[boundary-value-analysis]]). An accessor with a side effect gets a test of that side effect, through what it affects.

## Before and after

```
test "name getter":   p = Producer(data); assert p.name == "Byzantium"
test "cost setter":   p.cost = 12;        assert p.cost == 12
test "price setter":  prov.price = 25;    assert prov.price == 25
# no test of profit, which sorts producers and allocates demand
```

```
test "profit":            assert asia.profit == 230
test "change production": # the setter updates the province's total
    asia.producers[0].production = 20
    assert asia.shortfall == -6
test "zero demand":       asia.demand = 0; assert asia.profit == 0
```

Related: [[self-testing-code]], [[code-coverage]].

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 4, "Add Another Test" (PDF p. 109), "Modifying the Fixture" (PDF p. 112), "Probing the Boundaries" (PDF pp. 114, 116) and "Much More Than This" (PDF p. 117). The hyphen in "risk-driven" is restored where the extraction dropped it. The sign as a relation between tests and code, the assignments against neighbouring pages, the list of risky code in `## Rule`, parsing and validation in the first limit, the contract-conformance limit, `## Repair`, the reading of the over-testing remark, and the pseudocode are this wiki's own.
