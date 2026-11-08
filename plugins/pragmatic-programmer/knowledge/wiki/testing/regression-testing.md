---
title: "Regression testing: the same tests every time, automated"
category: testing
summary: "A test that failed after a change was deleted, or its expected value edited to match the new output, with no stated reason the old expectation was wrong; regression testing means the same automated tests every time, old ones kept."
tags: [rule, regression, automation, test-suite]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Regression testing confirms that a change has not taken the program a step back (pp. 518-519). McConnell's point is about sameness: if different tests run after each change, nobody can say no new defect came in. Tests may be added as the system grows, but the old ones stay (p. 519). Its root is compatibility with old data: given old inputs, a replacement must produce the old outputs, except where the old version was wrong (p. 507).

Automation is not optional here: «Единственный практичный способ управления регрессивным тестированием — его автоматизация» (p. 519). People running the same tests over and over lose concentration; Beizer is cited that manual testing has an error rate comparable to the code under test and that only about half of manual tests are run properly (p. 519). The listed gains of automation are fewer mistakes, more frequent runs, earlier detection, and so less large-scale rework later (p. 519). A file comparison of actual against expected output is an automated regression check the book names: if the files differ, a regression was found (p. 515).

## Rule

Keep every test that once passed and run the whole set, unchanged, automatically, after every change. An expectation changes only when the old one encoded a defect or a requirement changed, and the change says which.

## Sign in code

This wiki's own signs:

- In a change, a test that was passing is deleted, or its expected value is edited to equal the new output, and neither the change nor the test states what was wrong with the old expectation.
- A golden or expected-output file is regenerated in the same change that alters the behaviour it records, with no line saying the old output was wrong.

This wiki assigns the neighbouring cases as follows. A check that prints output for a person, or a hand-run step, is [[test-early-often-automatically]]. A test kept but switched off is [[all-tests-pass-always]]. A fixed defect with no test pinning it is [[find-bugs-once]]. This page owns an existing expectation removed or rewritten to fit new output.

## When not to apply

- A test whose expected value encoded the old version's defect is correctly changed: the book's compatibility rule excepts cases where the old method was wrong (p. 507). The change then states it.
- A requirement that deliberately changed the behaviour changes the expectation; this wiki reads the rule as asking only that the change name the requirement.
- A test deleted because it pinned an implementation detail the change removed, with visible behaviour unchanged ([[brittle-tests]]), or because it no longer protects anything ([[all-tests-pass-always]]), is not a regression; the change says which. This limit is this wiki's own.
- Exploratory manual testing that looks for new defects is a different activity and is not replaced by this rule. This limit is this wiki's own.

## Repair

Restore the deleted test or the old expectation, then decide which side is wrong: if the code regressed, fix the code; if the old expectation was wrong, change it and record why beside the assertion or in the change.

## Before and after

```
// change to round_price(); test edited in the same change
test price_rounding:
-   assert round_price(2.125) == 2.13
+   assert round_price(2.125) == 2.12
```

```
// the expectation kept; the regression fixed in round_price()
test price_rounding:
    assert round_price(2.125) == 2.13   // half-up to cents, per pricing rules
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]]: p. 507 (compatibility with old data), p. 515 (file comparison), pp. 518-519 (regression testing and automation), p. 523 (key point). This wiki's own: both signs, the owner assignments, the second, third and fourth limits, the repair and the pseudocode. Related: [[test-code-is-defect-prone]], [[code-coverage]].
