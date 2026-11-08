---
title: Error guessing and classes of bad and good data
category: testing
summary: "Checklist procedure for test inputs: too little, too much, wrong kind, wrong size and uninitialized data; nominal, minimum normal and maximum normal configurations; compatibility with old data; plus a kept list of past errors."
tags: [method, testing, error-guessing, test-selection]
paradigm: any
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

Formal techniques ([[structured-basis-testing]], [[data-flow-testing]], [[equivalence-partitioning]]) are complemented by heuristic ones. **Error guessing** is creating tests from reasoned guesses about where errors are likely, from intuition or past experience (p. 504). Its power grows with a kept **list of errors made before**, the same list chapter 21 recommends for inspections (p. 504; see [[code-inspection]]). [[boundary-value-analysis]] covers one of its most productive areas (p. 504); the data classes below are others.

## Bad data classes

Beside boundaries, test for (pp. 505-506):

- **too little data**, or none;
- **too much data**;
- **the wrong kind of data**, i.e. invalid data;
- **the wrong size of data**;
- **uninitialized data**.

In the payroll example, too little data is already covered by tests 2 (no employees) and 12 (ten unpaid employees); wrong size is hard to construct there; three new tests follow: 100,000,000 employees (too much data, the threshold depending on the system), a negative salary, and a negative number of employees (wrong kind) (p. 506). These are the material for the tests [[test-the-contract]] asks for.

### Fowler's boundary probes

Fowler's *Refactoring* runs the same classes as probes, after the happy path: "Think of the boundary conditions under which things might go wrong and concentrate your tests there" (2nd ed., ch. 4, Probing the Boundaries, PDF p. 114). He describes the stance as "playing the part of an enemy to my code" (PDF p. 114). His probes, in his order (PDF pp. 113-115): the empty collection whenever there is a collection, such as a province with no producers; zero, then negative numbers; a blank string where text becomes a number, because input fields limited to digits can still be left empty; and input of the wrong shape, such as a string where a list is expected.

The probes raise design questions as much as they catch bugs. A negative demand giving a negative profit leads Fowler to ask whether the minimum should be zero, in which case the setter should raise an error or clamp the value (PDF p. 114). This wiki reads that as a step of the procedure: where nobody knows the outcome a probe should have, the question is about the unit's contract ([[state-the-contract]]), not only about the test.

A probe can end in an error rather than a failed check. Many frameworks report an unanticipated exception during setup differently from a failure, where a verify step sees a value outside what was expected (PDF p. 115). Fowler ties how the code should treat malformed input to where it comes from: a trusted part of the same code base, or an external source such as a JSON request (PDF p. 115); this wiki hands that decision to [[barricade]]. When the tests only protect a refactoring, Fowler would probably discard a test that pins such an unanticipated error, because "Refactoring should preserve observable behavior" and an error of that kind lies outside it (PDF p. 116).

## Good data classes

The nominal case can hold an error too, and is easy to forget while hunting for errors (p. 506). Test:

- **nominal cases**: middle-of-the-road, expected values;
- **minimum normal configuration**: the set of minimum values from the normally expected range, not a boundary of one variable. Examples: saving an empty spreadsheet, saving an empty document in an editor; in the payroll example, a group of one employee (test 16) (p. 506);
- **maximum normal configuration**: the set of maximum expected values (pp. 506-507);
- **compatibility with old data**: given old inputs, a replacement must produce the old outputs, except where the old version was wrong (p. 507; see [[regression-testing]]).

The book stresses that the minimum normal configuration is useful for groups of elements, not just one, and differs from a boundary in that it stays inside the normally expected range (p. 506).

## Procedure

This wiki's arrangement of the book's lists:

1. Keep a project list of errors found earlier; for each new unit, add a test for each listed error that could occur in it.
2. Walk the five bad-data classes for each input; add a test where one is not already covered.
3. Walk the four good-data classes for the unit as a whole.
4. Merge with existing tests where a test already lies in a class; the book reuses tests 2 and 12 this way.
5. For each probe, write down the outcome the code should have before running it; an outcome nobody can state goes back as a question about the contract.

## Limits

Fowler warns against schemes that aim to test every combination, because of diminishing returns (PDF p. 116): the classes here follow risk ([[test-by-risk-not-by-method]]), not a combinatorial rule.

This wiki adds: "too much data" is a stress-flavoured test, and where a unit's input size is bounded by a validated caller, the excess-data test belongs at that caller. The book applies old-data compatibility when an old application or routine is replaced by a new one (p. 507). This wiki adds that it also applies where the unit reads data persisted, or produced, by an earlier version.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 22.3, pp. 504-507, via [[code-complete]]. The classes, the payroll tests and the replacement setting of old-data compatibility are the book's; the procedure, the excess-data limit and the persisted-data extension are this wiki's own.

Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 4, "Probing the Boundaries", PDF pp. 113-116: the probes and their order, the enemy stance, the design question, errors against failures, where malformed input comes from, discarding a test that pins an unanticipated error, and diminishing returns. This wiki's own for that part: step 5 and the reading of the design question as a contract question.
