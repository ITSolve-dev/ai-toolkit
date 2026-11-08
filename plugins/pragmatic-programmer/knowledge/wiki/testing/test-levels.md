---
title: Test levels
category: testing
summary: "Unit, integration, validation and performance tests answer different questions; an integration test re-checking one module's logic, or a failure reproducible in one module with no unit test, shows a level misused."
tags: [concept, unit-test, integration-test, validation, performance]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

Kinds of test differ by the question each can answer, and a suite is judged by whether each question has been asked somewhere. Thomas and Hunt use a fishing image: small fine nets, the unit tests, catch minnows, and large coarse nets, the integration tests, catch killer sharks. Some fish escape, so holes are patched as they are found (p. 332). The list below is, in their words, a starting point and not exhaustive (p. 333).

## Unit testing

A unit test is code that exercises one module, and it is the base of every other kind of test: «Если отдельные части программы не работают по отдельности, они не будут работать и вместе.» (p. 333). The book expects all modules to pass their unit tests before work moves on (p. 333). See [[test-the-contract]].

## Integration testing

Integration testing shows how well the main subsystems work together. The book ties it to contracts: where contracts are in place and well tested, integration problems are easy to detect, and otherwise integration becomes a breeding ground for bugs. In its words, «интеграция зачастую оказывается единственным и самым крупным источником программных ошибок в системе» (p. 334). The authors treat it as an extension of unit testing, which checks only how the subsystems honour their contracts (p. 334). See [[design-by-contract]].

## Validation and verification

These ask whether what users asked for is what they actually need, and whether their wishes match the system's functional requirements: «От бездефектной системы, дающей отрицательные ответы на эти вопросы, вряд ли будет много проку.» (p. 334). The book warns to take a sober view of end users' access patterns and how they differ from developers' test data (p. 334). See [[test-boundaries-and-realistic-use]].

## Performance testing

Performance and stress testing ask whether the software meets its requirements under real conditions, with the expected number of users, connections or transactions per second, and whether it scales. Some applications need specialised hardware or software to imitate load believably (p. 334).

## Applying the levels

This wiki draws three working criteria from the book's division. None of them is stated by the book.

- A failure that can be shown on one module, but is caught only at integration level, means a unit test is missing. Add it at the lower level, because it runs faster and points at the cause.
- An integration test that re-checks a module's internal logic duplicates a unit test. It should target the seam: what one subsystem promises and the other relies on.
- Test data invented by the developer shows what the developer expected. Inputs shaped like real use belong in validation, which is the gap the book's warning on access patterns names.

How far these levels reach is taken up by [[test-state-coverage-not-line-coverage]], and how to check the tests themselves by [[sabotage-your-tests]]. Where tests should run is covered by [[test-environment-matches-production]].

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation (Dialektika, 2020), see [[pragmatic-programmer]], pp. 332-334.

This wiki's own: `## Applying the levels`.
