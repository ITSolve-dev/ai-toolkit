---
title: Code coverage measurement
category: testing
summary: "Concept: testing without a coverage monitor typically exercises only 50-60% of the code; the monitor names untested lines, which call for more tests, but covered lines are not thereby tested."
tags: [concept, coverage, structured-testing]
paradigm: any
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

A coverage monitor records which code a test run executed and which it did not (p. 516). McConnell cites Wiegers that testing done without measuring coverage typically exercises only 50-60% of the code (p. 516), and, from Beizer, that programmers who believe they reach 95% typically reach 50-60% (p. 496; see [[developer-testing]]). The monitor is most useful for systematic testing, because it tells whether a given test set covers the code completely; if the full set has run and code remains untested, more tests are needed (p. 516). The chapter checklist asks the same: is every line exercised by at least one test, checked by counting the minimum number of tests needed to execute each line (p. 522).

## What coverage does and does not tell

The book uses the monitor one way: code it reports as untested needs more tests (p. 516). The converse limit, which *Code Complete* does not state, Fowler does (PDF p. 117, quoted below): covered code is not thereby tested. This wiki gives the reason: a line can execute under a test that asserts nothing about its effect ([[test-that-verifies-nothing]]). Line coverage is also weaker than the data-flow criteria in the same checklist, which ask that every define-use path be tested and suspicious patterns such as define-define or define-exit be checked (p. 522); see [[data-flow-testing]], [[variable-state-anomalies]] and [[structured-basis-testing]]. Thomas and Hunt make the parallel point that states, not lines, decide correctness: [[test-state-coverage-not-line-coverage]]. This wiki therefore reads coverage as directing where to write tests, not as grading the tests written. Fowler states the limit in his own words: coverage analysis "is only good for identifying untested areas of the code, not for assessing the quality of a test suite" (*Refactoring*, 2nd ed., ch. 4, PDF p. 117). His criterion for the quality of a suite is on [[test-suite-adequacy]].

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, p. 496, p. 516 and the checklist on pp. 522-523, via [[code-complete]]. The reason for the converse limit (a line executed under a test that asserts nothing, [[test-that-verifies-nothing]]) and the reading of coverage as direction rather than grade are this wiki's own; the converse limit itself is Fowler's. Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 4, "Much More Than This", PDF p. 117: coverage identifies untested areas and does not grade a suite.
