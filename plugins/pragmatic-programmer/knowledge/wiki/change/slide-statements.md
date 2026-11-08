---
title: Slide Statements
category: change
summary: "Procedure for moving a fragment of code up or down within a function (to gather related lines before an extract, or to put a declaration by its first use) without changing behaviour: the four interference checks, CQS as the shortcut, smaller slides when a test fails."
tags: [method, refactoring, side-effects, command-query-separation]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Slide Statements (formerly Consolidate Duplicate Conditional Fragments) moves a fragment of code to another position in the same function. Fowler uses it mostly as a preparatory step. Related lines have to be together before Extract Function can take them, and "Putting related code into a clearly separated function is a better separation than just moving a set of lines together" (*Refactoring*, 2nd ed., ch. 8, PDF p. 252). Its simplest use is declaring a variable just before its first use rather than at the top of the function (p. 252). That placement is owned by [[initialize-close-to-first-use]]. This page is the procedure for moving lines safely.

Fowler separates two decisions: which slide you want, which depends on context, and whether you can do it, which depends on interference (p. 253).

## Interference checks

Examine the statements between the source and target positions. Abandon the slide if there is interference (pp. 252-253):

1. A fragment cannot slide backwards above the declaration of anything it references.
2. A fragment cannot slide forwards past anything that references it.
3. A fragment cannot slide over a statement that modifies something it references.
4. A fragment that modifies something cannot slide over anything that references what it modifies.

The short form is: "I can't slide one fragment of code over another if any data that both fragments refer to is modified by either one" (p. 254). Fowler warns that this is not complete. `a = a + 10` and `a = a + 5` can swap freely, so judging a slide means understanding "the operations involved and how they compose" (p. 255).

## Side effects and CQS

Code without side effects can be rearranged "to my heart's content, which is one of the reasons why wise programmers prefer to use side-effect free code as much as possible" (p. 254). Whether a call such as `retrieveOrder()` is side-effect-free depends on everything it calls, transitively. Fowler trusts it in his own code only because he follows [[command-query-separation]]; in an unknown codebase he would be more cautious (p. 254). This wiki reads that as: the CQS shortcut holds only where the codebase is known to follow CQS. Elsewhere, treat every call that returns a value as a possible writer.

Because mutable state is what blocks slides, Fowler first reduces it. With a variable reassigned for several purposes, he would apply Split Variable before sliding (p. 255). See [[one-variable-one-purpose]].

## Procedure

1. Choose the target position and run the four checks above.
2. Cut and paste the fragment, then test.
3. If a test fails, slide over less code or move a smaller fragment. A failure may also mean the slide is not worth doing yet (pp. 253, 255).

With complex data structures, interference is hard to see, so the tests carry the check. If the tests are unreliable, be more wary, or improve them for the code being worked on (p. 255).

## Conditionals

Sliding out of a conditional removes duplicate logic, and sliding into one duplicates the fragment into every branch (p. 255). The rule with a sign in code, identical statements at the same end of every branch, is [[identical-code-in-every-branch]].

## Fragment size

Swap Statement is the single-statement version. Fowler slides larger fragments by default and drops to one statement at a time only when a larger slide gives trouble, adding that "With more messy code, however, smaller slides end up being easier" (p. 256). Compare [[refactor-in-small-tested-steps]].

## Example

```
// before: discount declared far above its first use
discount = 0
pricingPlan = retrievePricingPlan()
order = retrieveOrder()
charge = pricingPlan.base + order.units * pricingPlan.unit
if order.isRepeat then discount = 0.05
```

```
// after: the declaration slid down to the line before its first use;
// nothing in between reads or writes the local discount, and no call
// can reach a local, so no check on the calls is needed
pricingPlan = retrievePricingPlan()
order = retrieveOrder()
charge = pricingPlan.base + order.units * pricingPlan.unit
discount = 0
if order.isRepeat then discount = 0.05
```

## Source

Fowler, *Refactoring*, 2nd ed., ch. 8, Slide Statements, PDF pp. 252-256 ([[fowler-refactoring]]): the uses, the two decisions, the four checks and their short form, the warning about composition, side effects and CQS, the procedure, conditionals and fragment size. This wiki's own parts are the reading that, outside a codebase known to follow CQS, every value-returning call counts as a possible writer, and the pseudocode, loosely after the book's pricing-plan example.
