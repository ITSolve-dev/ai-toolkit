---
title: Test-driven development
category: testing
summary: "A run of new tests exercises one internal representation and none calls the operation the requirement names, or a test only references a class name: the test-first cycle is producing green bars, not progress."
tags: [method, testing, tdd]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

Test-driven development (TDD) is a working cycle in which a failing test comes before the code that satisfies it. This wiki keeps only what bears on code in front of a reader: the order of writing cannot be seen there, while two kinds of misuse can.

## Misuse that shows in code

The book endorses the method and warns against slavery to it (p. 268). Two of its warnings leave a mark in the tests.

- **Redundant tests,** such as one that only references a class name (p. 268). See [[test-that-verifies-nothing]].
- **Polishing an easy part.** Solving a problem test by test can encourage endless polishing of easy parts while neglecting the reason the code is being written (p. 268). The book's case is a test-driven sudoku solver that refined the board's representation over five blog posts and was then abandoned (p. 269).

This wiki's sign for the second: a run of new tests exercises one internal representation, and none calls the operation the requirement names. This wiki's check, its reading of the book's advice to stop periodically: name which requirement the last test moved closer. If no requirement can be named, the cycle is polishing.

The book's other two warnings, excessive time spent on full coverage and design that works upward from the bottom (p. 268), have no sign in code and are not used here.

## What not to report

The book accepts testing alongside the coding where test-first is awkward or useless (p. 274), so this wiki does not report the order of writing. It reports a test that is missing: see [[find-bugs-once]] and [[test-early-often-automatically]]. Testing later is another matter: the book says that it really means «не тестировать вовсе» (p. 274).

## Limits

Dave Thomas reports stopping writing tests for a couple of months and finding little change, because long practice let him think about tests without writing them. He then noted what this ignores: tests also communicate with other developers. He now writes tests for code shared with others or relying on the peculiarities of external dependencies (p. 275).

This wiki reads that as a limit on the claim that thinking is the whole benefit. Absent tests still cost the reader of shared code, so the sidebar is no licence to skip them on a shared module.

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020 ([[pragmatic-programmer]]): pp. 268-269, 274-275. This wiki's own: the sign for polishing, the end-of-cycle check, the decision not to report the order of writing, and the reading of the sidebar's limit. Related: [[test-is-first-client]].
