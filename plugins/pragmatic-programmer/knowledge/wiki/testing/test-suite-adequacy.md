---
title: When a test suite is good enough
category: testing
summary: "Concept: a coverage figure offered as proof that a suite is good, or a suite that has to be edited more than the code it tests; neither says whether a defect would make some test fail, which is Fowler's working criterion."
tags: [concept, test-coverage, over-testing, confidence, test-suite-health]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Fowler holds that no good measurement says how much testing is enough (*Refactoring*, 2nd ed., ch. 4, "Much More Than This", PDF p. 117). His working criterion is subjective: "How confident are you that if someone introduces a defect into the code, some test will fail?" (PDF p. 117). A suite is good enough when he can refactor and trust a green run to mean he has introduced no bug. That is the property [[self-testing-code]] asks for, stated as a test of the suite.

## Coverage

Coverage analysis "is only good for identifying untested areas of the code, not for assessing the quality of a test suite" (PDF p. 117). The limit of coverage is on [[code-coverage]]. Which states a covered line can still fail in is [[test-state-coverage-not-line-coverage]]. Fault injection checks the confidence criterion directly for one spot in the code: [[sabotage-your-tests]].

## Over-testing

Fowler grants that a suite can hold too many tests. His sign is time: it happens "when I spend more time changing the tests than the code under test", and the tests feel as though they slow him down (PDF p. 117). He adds at once that over-testing is "vanishingly rare compared to undertesting" (PDF p. 117). This wiki adds a reading of its own: tests that break on a refactoring that kept behaviour the same pin the implementation rather than the behaviour, which is one concrete form of Fowler's time sign. That shape in a single test is owned by [[brittle-tests]].

## Iteration

Testing is iterative. A suite is rarely right the first time, and Fowler reviews it like production code: is it clear, does it need refactoring, are these the right tests (PDF p. 117). What to test first, when there is not time for everything, is [[test-by-risk-not-by-method]].

## Limits

Fowler concedes that the confidence criterion "doesn’t account for false confidence" (PDF p. 117). This wiki reads that as: a suite that has never been seen to fail can produce confidence it has not earned, which is why the criterion is checked by breaking the code on purpose rather than by asking the author.

Related: [[adding-tests-to-existing-code]], [[all-tests-pass-always]].

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 4 "Building Tests", section "Much More Than This", PDF p. 117: the absence of a measure, the confidence question, the limit of coverage, the time sign of over-testing and its rarity, iteration and the false-confidence admission. This wiki's own: the reading of tests broken by a behaviour-preserving refactoring as pinning implementation, the reading of the false-confidence limit, and the links to the owning pages.
