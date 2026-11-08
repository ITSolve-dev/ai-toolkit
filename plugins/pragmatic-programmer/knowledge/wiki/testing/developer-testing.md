---
title: Developer testing
category: testing
summary: "Concept: what tests written by the code's own author can and cannot show; a passing suite never proves absence of defects, and authors overrate both their coverage (believed 95%, typically 50-60%) and the breadth of their cases."
tags: [concept, testing, coverage, test-first]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

**Developer testing** is the testing a programmer does on their own code during construction: unit tests (a whole class, routine or small program by one author, run in isolation), component tests (an element built by several people, still in isolation) and integration tests (two or more classes, packages or subsystems run together, started as soon as two testable classes exist). Regression and system testing sometimes join it (McConnell, pp. 490-491). Because the author knows the code, it is **white-box** testing, and the book focuses on it for that reason (p. 491). The test levels as Thomas and Hunt divide them are [[test-levels]].

## What testing is and is not

- **Testing finds errors; debugging finds their cause.** The book separates the two: testing detects, debugging (ch. 23) diagnoses and fixes (p. 491). See [[debugging-procedure]] for the second half.
- **Testing never proves the absence of errors.** No errors found may mean the program is clean or that the tests are weak or incomplete (p. 492).
- **Testing does not raise quality, it measures it.** McConnell's analogy: trying to improve software by testing more is like trying to lose weight by weighing yourself more often; what you ate decides the weight, and the construction techniques decide how many defects testing will find (p. 492). This wiki reads it as: a weak design is not repaired by a larger suite; the repair belongs in the code (see [[structured-basis-testing]] for how routine size alone drives the test count).
- **Exhaustive testing is impossible.** A program taking a 20-letter name, a 20-letter address and a 10-digit phone number has about 10^66 input combinations (p. 496). The art is therefore picking a few tests that each find *different* errors and dropping tests that cannot tell anything new, such as data resembling data already tested (p. 497). [[equivalence-partitioning]], [[boundary-value-analysis]] and [[test-data-classes]] are the selection tools.
- **Each testing stage alone typically finds under 50% of errors, and stages combined under 60%** (Jones 1998, cited p. 492); collaborative construction (reviews, inspections) finds more errors than testing at less than half the cost per error (Card 1987; Russell 1991; Kaplan 1995, p. 492), and testing must be combined with other techniques (p. 496). See [[defect-detection-techniques-are-complementary]].

## Why authors test their own code badly

The book names three biases (pp. 495-496):

1. **Clean tests over dirty tests.** Authors test that code works rather than try to break it. The rule with its sign is [[test-the-contract]].
2. **Optimistic coverage.** Programmers believe they reach 95% coverage; they typically reach 30% at worst, 80% at best, 50-60% on average (p. 496). The book's remedy is a coverage monitor (p. 497; see [[code-coverage]]) and a systematic case derivation such as [[structured-basis-testing]].
3. **Statement coverage taken as enough.** "100% statement coverage" is a start; McConnell calls the stronger "100% branch coverage" what is needed (p. 496). This wiki notes that the book's wording of it, every variable of every predicate getting at least one true and one false value, is closer to what is usually called condition coverage.

And one of attitude: a tester must **expect** to find errors. In Myers' study (1978) experienced programmers found on average 5 of 15 known defects, the best 9; the errors were visible in the output and went unnoticed (pp. 492-493).

## Practices the chapter recommends

- **Test each unit before combining it**, and add routines to a tested set one at a time. It is not easier to test this way, but a failure is then localised to the new routine or its interaction with the old ones (p. 494). This wiki reads the code-side sign as a test that first exercises several freshly written, untested routines together, so a failure cannot name its culprit.
- **Derive tests from each relevant requirement and each relevant design aspect**, then add detailed tests by basis and data-flow testing; at minimum every line runs once (pp. 494-495).
- **Keep a checklist of the errors this project, or earlier ones, made** and test against it (p. 495; see [[test-data-classes]] on error guessing).
- **Write tests first.** McConnell's reasons (p. 495): the effort is the same, only reordered; defects are found sooner and fixed cheaper; it forces some thought about requirements and design; a bad requirement shows because it is hard to test; kept tests still run after the code is written. He calls it one of the most effective techniques of the decade, but not a panacea, since it shares every limit listed above (p. 495). See [[test-driven-development]].

## Limits

This page describes testing by the author. The book is explicit that it is insufficient alone and must be complemented by independent testing and collaborative construction (p. 496). The percentages above are the cited studies' figures from the 1990s and earlier, not measurements of any current codebase.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 22.1-22.3, pp. 490-497, via [[code-complete]]. This wiki's own: the reading of the weighing analogy as a design point, the reading of the book's "branch coverage" as condition coverage, and the code-side sign of untested routines tested together.
