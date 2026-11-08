---
title: Equivalence partitioning
category: testing
summary: "Procedure for when several tests feed inputs from the same class (three salaries all below a threshold) while another class of the same condition has no test: one representative per class, drop the rest."
tags: [method, testing, test-selection]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

**Equivalence partitioning** formalises a simple idea: if two tests find the same errors, only one is needed (p. 503). A condition in the code, or a rule in the specification, splits the values of an input into classes that the code treats alike; one test per class suffices, and more tests in the same class add nothing. It applies the broader principle in [[developer-testing]]: choose tests that find *different* errors (p. 497).

## Procedure

1. For each input, find the conditions that split its values: comparisons in the code, or rules in the specification.
2. Each side of each split is a class. In the book's example, `withheld < MAX_GOVT_RETIREMENT` gives two classes: below the constant, and equal or above (pp. 503-504).
3. Pick one representative per class. Other parts of the program may impose other partitions on the same variable, requiring more values; in the book's routine only two are needed (p. 504). Within a class, pick a value whose expected result can be checked by hand ([[test-values-checkable-by-hand]]).
4. Drop tests whose inputs fall in a class already represented, except values that [[boundary-value-analysis]] places on or beside an edge.
5. Pair the class edges with [[boundary-value-analysis]]: partitioning picks a value inside each class, boundary analysis picks the values on and beside the edge.

## When it adds something

McConnell says plainly that equivalence partitioning tells little new once [[structured-basis-testing]] and [[data-flow-testing]] are done. It is most useful when (p. 504):

- the tests are designed from the outside, from the specification rather than the source; or
- the data is complex and that complexity is poorly reflected in the program's logic, so the code has fewer branches than the domain has cases.

This wiki reads the second case as a review hint: if the specification's classes outnumber the code's branches, either the code collapses cases it should distinguish or the specification over-distinguishes, and a test per specification class will show which.

## Sign in a test suite

This wiki's own: several tests whose inputs all fall in one class of a condition, while another class of the same condition has no test. Redundant tests inside one class of a condition, while another class of that condition has no test, belong to [[equivalence-partitioning]]; a test whose every effect another test already asserts belongs to [[test-that-verifies-nothing]].

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 22.3, pp. 497, 503-504, via [[code-complete]]. This wiki's own: procedure steps 1, 3 (second sentence), 4 (with its exception) and 5, the review hint, the sign and the assignment against [[test-that-verifies-nothing]].
