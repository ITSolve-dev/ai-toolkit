---
title: Adding tests to existing code before refactoring
category: testing
summary: "Procedure for putting untested code under test before changing it: write the test with a placeholder, copy in what the code actually produces, inject a fault, see the test fail with expected and actual values, revert; then pin outputs, state changes and boundaries in that order."
tags: [method, characterization-test, fault-injection, legacy-code]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Before refactoring code that has no tests, Fowler first makes it self-testing (ch. 4, PDF p. 102). Chapter 4 gives his routine for this, built around one worry: a test that passes may not exercise the code the way its writer thinks. "Always make sure a test will fail when it should" (PDF p. 107).

## Procedure

1. **Write the test with a placeholder** for the expected value.
2. **Run it and copy in what the code actually produces.** Since the code is supposed to work, Fowler trusts its current output rather than working the value out by hand (PDF p. 110). The test now pins current behaviour. This wiki selects between the two ways Fowler gets an expected value: where the expected value can be checked by hand at a glance, check it, as with his hand-checked reference strings (ch. 1, PDF p. 10); otherwise copy the code's current output and treat any value that looks wrong as a question.
3. **Inject a fault** into the code under test, for example by multiplying a term by 2 (PDF p. 107).
4. **Check that the test fails**, and that the report shows the expected and actual values at the place of the fault (PDF p. 108).
5. **Revert the fault.**

Fowler sums this up as the pattern of writing with a placeholder for the expected value, replacing it with the code's actual value, injecting a fault and reverting it (PDF p. 110). Steps 3 to 5 are the general check in [[sabotage-your-tests]].

## Choosing what to pin

- Pin the main outputs of the unit first, then the behaviour that changes state, then the boundaries ([[test-by-risk-not-by-method]], [[test-data-classes]]).
- Remove duplication in the tests as in production code, but not by sharing a mutable fixture ([[fresh-fixture-per-test]]).
- Fowler would probably discard a test that only pins an unanticipated error, because refactoring need preserve only observable behaviour (PDF p. 116).
- Keep adding tests during the refactoring. Fowler notes that refactoring builds understanding of the program, and that turns up more gaps (PDF p. 116).

## Trade-offs and failure modes

- This wiki adds: copying the code's output pins its bugs too, so the test guards against change, not against error. A value that looks wrong once copied is a question to raise, not a value to pin silently. In the book, a negative profit for negative demand prompts exactly such a question (PDF p. 114).
- This wiki adds: a test never seen to fail can pass against broken code, for example by asserting on the wrong object or never reaching the code path. Injecting a fault is the cheap check against this.
- Adding tests to a system not designed for them may first need seams. Fowler defers that case to Feathers (ch. 2, Legacy Code, PDF p. 73; [[self-testing-code]]).

Related: [[refactor-in-small-tested-steps]], [[failing-test-before-the-fix]].

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 4, "Building Tests", PDF pp. 102, 107-110, 114 and 116; ch. 1, PDF p. 10, for hand-checked reference strings; ch. 2, "Legacy Code", PDF p. 73, for seams and Feathers. The numbered arrangement, the order of what to pin as a list, the choice between a hand-checked and a copied expected value, and the two trade-offs marked as this wiki's are this wiki's own.
