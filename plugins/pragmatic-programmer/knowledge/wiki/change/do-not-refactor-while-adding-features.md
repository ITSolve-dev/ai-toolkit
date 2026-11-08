---
title: Do not refactor while adding features
category: change
summary: "One step or one diff hunk both moves or renames code and changes what it computes; a change labelled refactor alters test expectations or adds tests for new behaviour. Two single-purpose steps sharing one commit are not this sign."
tags: [rule, refactoring, two-hats, change-safety, commits]
paradigm: any
sources: [pragmatic-programmer, fowler-refactoring]
created: 2026-11-01
updated: 2026-11-07
---

Refactoring is defined by keeping behaviour fixed, so a change that also adds behaviour has lost the only property that made it safe to check. This is the first of Fowler's three guidelines as *The Pragmatic Programmer* reports them (p. 263). Fowler's own *Refactoring* gives it as Kent Beck's metaphor of the two hats: when developing with refactoring, time is split between two distinct activities, adding functionality and refactoring, and at any moment the programmer knows which hat is on (2nd ed., ch. 2, PDF pp. 57-58).

## Rule

«Не пытайтесь выполнять рефакторинг, попутно добавляя функциональные возможности» (*The Pragmatic Programmer*, p. 263).

Fowler states the two hats. Under the feature hat, "I shouldn't be changing existing code; I'm just adding new capabilities", and progress is measured by adding tests and making them pass. Under the refactoring hat, "I make a point of not adding functionality; I only restructure the code" (PDF p. 57). While refactoring he adds no tests, unless he finds a case he missed earlier, and changes tests only to accommodate a change in an interface (PDF pp. 57-58).

The hats swap often, sometimes several times in ten minutes: start a feature, see that a different structure would make it easier, refactor, return to the feature, see the new code is awkward, refactor again (PDF p. 58). This wiki reads the rule as being about each step, not about long phases.

*The Pragmatic Programmer*'s definition supplies the reason: since external behaviour does not change, no new features are introduced (p. 260). This wiki extends that as follows. A test failure during a pure refactoring has one meaning, that the refactoring broke something. In a mixed step the same failure could be the new feature, an old test that the feature rightly invalidated, or a slip in the move. The tests stop answering the question.

## Sign in code

- One step, or one hunk of a diff, both moves, renames or splits code and changes what it computes: a behavioural edit sits inside the moved block, so the hunk cannot be read as a rename.
- A change described as a refactoring changes the expected values of existing tests, or adds tests for behaviour that did not exist before.
- Under a refactoring label, a test changes for a reason other than an interface change (a rename, a moved function, a new parameter).

This wiki assigns the neighbouring cases as follows. Test expectations changed inside a refactoring are [[do-not-refactor-while-adding-features]]; a change that is only structural and too large to judge is [[refactor-in-small-tested-steps]]. This page owns the split of a mixed step. Whether the structural part is worth keeping at all is [[know-when-to-stop]]'s question. The decision to restructure before the feature at all is [[preparatory-refactoring]].

## Sources disagree on commits

*The Pragmatic Programmer*'s report of Fowler's first guideline reads as asking for separate changes (p. 263). Fowler himself, in his 2nd edition, is "not convinced" that refactoring and feature work must go into different version-control commits: they are often closely interwoven, separating them is not worth the time, and it can strip the refactoring of the context that justifies it. He calls separate commits "not a selfevident principle—it's only worthwhile if it makes life easier" (PDF p. 65).

This wiki resolves it per setting. The hat rule holds for every step: each step is either structure or behaviour, and the tests confirm the structural ones unchanged. The commit split is a review convenience. It is worth making where the two are reviewed or reverted independently, or where the refactoring is large; it is not required where the refactoring is a few lines that exist only to admit the feature beside them. A single commit holding two clean steps is therefore not a sign under this page; a single hunk mixing them is.

## When not to apply

Neither book gives an exception to the hat rule. These limits are this wiki's own, except where marked.

- The structural edit is too small to count as a step, such as a local variable the new line would otherwise misname. A split there costs more than the mixed step risks.
- The new behaviour cannot be written in the old shape, and no intermediate state would pass the tests. Then the two go in together, and the change says so.
- The code has no tests. The reason above, that a failure has one meaning, then gives nothing. A split still helps a reader, but [[refactor-in-small-tested-steps]] comes first.
- A latent bug that nobody has observed yet may be fixed while refactoring, as Fowler allows (PDF p. 57). This wiki's own condition: fix it as a separate step under the feature hat, not silently inside a move.

## Repair

1. Stop the feature. Refactor first, under the refactoring hat, until the feature is easy to add ([[preparatory-refactoring]]).
2. Keep the tests unchanged during the structural step, except for interface changes the refactoring itself made.
3. Swap hats and add the behaviour with its own test.
4. If a hunk already mixes both, split the structural edit out first. Split into separate commits where review or revert needs it.

## Before and after

```
// before: one step, "tidy pricing"
- function price(order): ...
+ function netPrice(order):
+     base = linesTotal(order)
+     return base - loyaltyDiscount(order)     // new behaviour inside the rename
// test: expected value of price(...) edited to include the discount
```

```
// after
// step 1, refactoring hat: rename only; tests changed only for the new name
+ function netPrice(order):
+     return linesTotal(order)

// step 2, feature hat: new behaviour with a new test
+     return linesTotal(order) - loyaltyDiscount(order)
test netPrice applies loyalty discount
```

## Source

[[pragmatic-programmer]], Topic 40, pp. 260 and 263, reporting Fowler's guidance. [[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 2, "The Two Hats" (PDF pp. 57-58) and "Planned and Opportunistic Refactoring" (p. 65): the hats, the tests under each, the frequent swaps, the latent-bug allowance and the doubt about separate commits. This wiki's own: the account of what a test failure means, the reading of the rule as per step, the signs, the per-setting resolution of the commit question, the splits with [[refactor-in-small-tested-steps]], [[know-when-to-stop]] and [[preparatory-refactoring]], the first three limits, the separate-step condition on the fourth, the repair and the example.
