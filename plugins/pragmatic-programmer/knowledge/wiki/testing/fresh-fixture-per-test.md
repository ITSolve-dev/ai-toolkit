---
title: Build a fresh fixture for each test
category: testing
summary: "A mutable test object built once at suite, class or module scope, or in a run-once hook, and read by several tests; strongest when a test changes it, so results depend on run order."
tags: [rule, fixture, test-isolation, nondeterminism]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Each test should start from a newly built fixture, meaning the data and objects it needs, rather than share one built once for the whole suite. Fowler calls the shared mutable fixture "a petri dish that’s primed for one of the nastiest bugs in testing—a shared fixture which causes tests to interact" (ch. 4, Add Another Test, PDF p. 110).

## Rule

Build the fixture in a per-test setup hook, or inside the test itself, so that every test gets its own copy (PDF pp. 110-111).

What breaks when this is ignored: when one test changes the shared object, later tests see the changed state, and results depend on the order the tests run in. Fowler calls that "a nondeterminism in the tests that can lead to long and difficult debugging at best, and a collapse of confidence in the tests at worst" (PDF p. 111). He also warns that declaring the reference constant does not protect it, because a constant reference does not make the object's content constant (PDF pp. 110-111).

Fowler gives a second reason for a shared setup hook over construction repeated in each test: it tells the reader that every test in the group starts from the same standard fixture, which becomes familiar, so the tests read as probes of its characteristics (PDF p. 111).

## Sign in code

A test group in which several tests read a mutable object built once outside any per-test setup: at suite, class or module scope, or in a run-once hook. The sign is strongest when at least one test changes that object. In its weaker form nothing changes it yet, but nothing prevents it either. Final or const on the variable does not remove the sign if the object itself can be changed.

## When not to apply

- The fixture is truly immutable: a value object, frozen data or a read-only resource (PDF p. 111).
- Building a fresh fixture is measurably slow. Fowler says this is rarely noticeable (PDF p. 111). A shared fixture is then a deliberate choice, and it needs a discipline that no test changes it, often with an explicit teardown that resets it (Modifying the Fixture, PDF p. 112).
- This wiki adds: a variable declared at suite scope and assigned in the per-test setup hook is the repair, not the defect.

## Repair

1. Declare the fixture variable at group scope, but leave it unassigned.
2. Assign a newly built fixture in the framework's per-test setup hook.
3. Remove the construction from the tests, so that they use the standard fixture.
4. If a shared fixture is kept for speed, make it immutable, or add a teardown that restores it after each test.

With all setup in the per-test hook, the framework discards the fixture between tests, so teardown can be taken for granted (PDF p. 112).

## Before and after

```
suite "province":
    asia = Province(sampleData())        # built once, mutable, shared

    test "shortfall":
        assert asia.shortfall == 5
    test "change production":
        asia.producers[0].production = 20 # changes the shared object
        assert asia.shortfall == -6
    test "profit":
        assert asia.profit == 230         # passes or fails by run order
```

```
suite "province":
    asia = none
    beforeEach:
        asia = Province(sampleData())     # new object for every test

    test "shortfall":
        assert asia.shortfall == 5
    test "change production":
        asia.producers[0].production = 20
        assert asia.shortfall == -6
    test "profit":
        assert asia.profit == 230
```

Related: [[self-testing-code]], [[one-verification-per-test]], [[random-failures-suspect-concurrency]].

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 4, "Add Another Test", PDF pp. 110-111, and "Modifying the Fixture", PDF p. 112, for teardown. The sign as worded, its weaker form, the limit on a variable reassigned per test, the repair steps as listed, and the pseudocode, modelled on the book's province example, are this wiki's own.
