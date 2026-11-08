---
title: Test early, often and automatically
category: testing
summary: "A test prints a value for a person to compare instead of asserting, needs a hand-run step, or new logic arrives in a diff with no test. A test that exists and is switched off is all-tests-pass-always."
tags: [rule, automation, test-suite, definition-of-done, self-checking, refactoring]
paradigm: any
sources: [pragmatic-programmer, code-complete, fowler-refactoring]
created: 2026-11-01
updated: 2026-11-07
---

A test only protects code while it runs and can fail on its own. Tests that are deferred or depend on a person checking the output give no warning at the moment the code breaks.

## Rule

Two tips belong together: «Тестируйте как можно раньше, чаще и автоматически» and «Программирование нельзя считать завершенным до тех пор, пока не пройдут все тесты» (both p. 333). Thomas and Hunt require the automated build to run every existing test (p. 333) and say never to rely on manual intervention in testing code (p. 337).

Their reasons: bugs grow quickly from small fish into man-eaters that are much harder to catch (p. 333), and manual procedures are left to chance, because repeatability is not guaranteed and different people read the same steps differently (p. 331). People cannot repeat a procedure as exactly as a computer does (p. 337).

McConnell reaches the same conclusion for regression testing: «Единственный практичный способ управления регрессивным тестированием — его автоматизация» (*Code Complete*, p. 519). He cites Beizer that manual testing has an error rate comparable to the code under test and that only about half of manual tests are run properly (p. 519). Keeping the same tests across changes is [[regression-testing]].

Fowler's *Refactoring* puts the same demand at the start of every refactoring. His tip: "Before you start refactoring, make sure you have a solid suite of tests." The tests must be self-checking (2nd ed., ch. 1, PDF p. 10). Before every refactoring the first step is the same, tests for that section of code, because even with refactorings structured to avoid mistakes he still makes them, and the larger the program, the more likely a change breaks something by accident (PDF p. 9). For `statement`, which returns a string, he builds a few invoices covering kinds of plays, generates their statements and compares each with a reference string he has checked by hand; the run is one keystroke and takes seconds, and the result is green, or red with the lines that differ (PDF pp. 9-10). Without that, he says, he would compare values by hand against a desk pad, and that would slow him down (PDF p. 10). His reasoning for the cost: writing what he wants twice, in the code and in the test, means a mistake has to be made consistently in both places to fool the detector, and the time spent building tests comes back as less time debugging (PDF p. 10). What the suite as a whole must provide for refactoring is [[self-testing-code]].

They also describe a mark of a well-run project: «качественно разрабатываемый проект отличается тем, что в нем больше тестового, чем рабочего кода» (p. 333). Knowing a test passed, they say, gives real confidence that the code it checked is ready (p. 333).

## Sign in code

- A test with no assertion that prints a value for someone to compare by eye.
- A test that works only after a step done by hand: a server started first, a file copied into place. A value present on only one machine belongs to [[test-environment-matches-production]].
- A diff adding new logic with no test in the same diff.
- Code that the task names as the target of a refactoring, and that no test exercises. A restructuring already under way on such code is [[refactor-in-small-tested-steps]]'s sign; this page owns the missing test before it starts.

This wiki assigns the two neighbouring shapes by whether the test is switched off. This page owns a check that needs a person, or that never arrived with the code. A test that exists and is switched off belongs to [[all-tests-pass-always]]. A fix of a defect with no test belongs to [[find-bugs-once]], and this page keeps new logic. A test with no assertion that prints nothing is [[test-that-verifies-nothing]]. A passing test deleted or rewritten to fit new output is [[regression-testing]].

## When not to apply

- Throwaway exploratory code that will not be kept. The rule is about code going into the product. This limit is this wiki's own.
- The ratio of test code to production code describes a project. It is not a target. This wiki does not treat a low ratio as a defect, because a suite can be large and still pin nothing. See [[sabotage-your-tests]].
- Some judgements stay with people. Whether a system is what users need is checked by validation, which the book treats separately (p. 334). See [[test-levels]].
- A hand-checked reference output (a golden string) compared by an assertion is a self-checking test, as Fowler uses it (PDF pp. 9-10); this wiki notes that its brittleness where the output format is meant to change is owned by [[brittle-tests]].
- Running everything has a cost. A slow suite gets run less often, which defeats the rule, so this wiki expects a slow suite to be split or sped up, not left out of the build.

## Repair

1. Replace printed output with an assertion on the expected value.
2. Move hand-run steps into the test's setup or a fixture.
3. Write the test together with the logic it checks.
4. Before a refactoring, wrap the current output in an assertion for a few inputs that cover the cases (each kind of item, values above and below each threshold), and run it from the framework in one step. Where the expected value can be checked by hand at a glance, check it; otherwise copy the code's current output and treat any value that looks wrong as a question ([[adding-tests-to-existing-code]]). The choice of covering inputs is this wiki's own.

## Before and after

Before:

```
test "invoice total":
    invoice = build_invoice(items)
    print(invoice.total)    # compare with the spreadsheet
```

After:

```
test "invoice total":
    invoice = build_invoice(two_items_at_10)
    assert invoice.total == 20
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation (Dialektika, 2020), see [[pragmatic-programmer]]: the tips, the growth of bugs, the build running all tests and the test-to-code mark on p. 333; manual procedures on pp. 331 and 337; validation on p. 334. McConnell, *Code Complete*, 2nd ed., Russian edition ([[code-complete]]): automation of regression testing and the Beizer figures on p. 519. Fowler, *Refactoring*, 2nd ed. ([[fowler-refactoring]]), ch. 1, "The First Step in Refactoring", PDF pp. 9-10: tests before refactoring, self-checking, the golden-string method, the desk-pad comparison and the double-entry reasoning.

This wiki's own: all of `## Sign in code` and its assignments (including the fourth sign against [[refactor-in-small-tested-steps]] and the assignments against [[all-tests-pass-always]], [[find-bugs-once]] and [[test-that-verifies-nothing]]), `## Repair`, the pseudocode, and every limit except the book's separate treatment of validation and Fowler's golden-string use; the pointer to [[brittle-tests]] is also this wiki's.
