---
title: Review a conditional statement
category: complexity
summary: "A procedure for reviewing if, if-else-if and case code: nominal path first, the equality boundary (> against >=), else present or explained, if and else not swapped, chain order and completeness, case selector, arm length, default and fall-through."
tags: [method, conditionals, checklist, code-review]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell closes chapter 15 with a checklist for conditional statements (pp. 357-358). This page turns it into an order of questions to run against a piece of branching code, each pointing to the page that owns the finding.

## Procedure

**For each `if`-`then` / `if`-`else`:**

1. Is the nominal path obvious, and does the normal case follow the `if` rather than the `else`? See [[nominal-path-first]].
2. **Does the comparison branch correctly on equality?** The book: using `>` instead of `>=`, or `<` instead of `<=`, is the conditional analogue of an off-by-one error in indexing an array or a loop (pp. 346-347). Ask what happens when the two sides are equal, and check that this matches the specification. This wiki adds that the equal value is the boundary test to write ([[test-boundaries-and-realistic-use]]).
3. Is the `else` present, or is its absence explained? See [[document-the-missing-else]]. Is the `else` correct, and has it been tested (p. 350)?
4. **Are the `if` and `else` swapped?** Putting the code meant for the `if` into the `else`, inverting the logic, is a common error the book asks you to check for (p. 350). Read the condition aloud and confirm that each branch does what is meant in that case.
5. Is the then-branch empty? See [[no-empty-then-branch]].

**For each `if`-`then`-`else`-`if` chain:**

6. Are complex tests replaced by boolean function calls? See [[name-complex-conditions]].
7. Are the most likely cases tested first, and are the tests exclusive enough for the order to be safe? See [[order-branches-by-frequency]].
8. Are all cases covered, with a final `else` that reports the unexpected? See [[default-branch-catches-the-unexpected]].
9. Would a `case` be better, or is the chain right because the data is not simple? See [[case-or-if-chain]].

**For each `case` / `switch`:**

10. Are the cases ordered sensibly? See [[order-branches-by-frequency]].
11. Is each arm simple, with calls to routines where needed? See [[keep-case-arms-short]].
12. Does the `case` test a real variable, not a phony one built only to drive it? See [[case-or-if-chain]].
13. Is the `default` used only for a real default, and otherwise to detect and report unexpected values? See [[default-branch-catches-the-unexpected]].
14. In C-family languages, does every arm end with an exit, and is any intended fall-through marked? See [[avoid-case-fall-through]].

## Limits

The checklist is the book's; the order and the links are this wiki's. Steps 2 and 4 have no page of their own because their sign is a single comparison or a single swapped body, which a reader can only judge against the intended behaviour, not against the shape of the code. This wiki keeps them as review questions for that reason. Clean branching code may pass every step, and then the review's answer is that the code is fine as it is.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]], chapter 15: checklist, pp. 357-358; the equality boundary, pp. 346-347; the inverted `if`/`else` and testing the `else`, p. 350. The grouping, the order, the links to owner pages, the boundary-test addition, the exclusivity question in step 7, the read-aloud check in step 4 and the note on steps 2 and 4 are this wiki's own.
