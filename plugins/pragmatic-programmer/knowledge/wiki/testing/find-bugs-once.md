---
title: Find bugs once
category: testing
summary: "A diff fixes a defect and touches no test, or a comment stands in for a test: a warning about the failure, a note of a manual check, a snippet to paste into a REPL. The same bug can return unnoticed."
tags: [rule, regression, bug-fix, test-design]
paradigm: any
sources: [pragmatic-programmer, code-complete, fowler-refactoring]
created: 2026-11-01
updated: 2026-11-07
---

A bug that got past the tests shows a hole in them. Fixing the code closes the bug, and only a new test closes the hole.

## Rule

The tip reads «Обнаруживайте ошибки единожды» (p. 336). Thomas and Hunt call this the most important principle of testing and say most projects still do not apply it. Once a tester has found a bug, that should be the last time a person finds it: the automated tests are changed to check for it from then on, without exception, however trivial it is and however often the developer promises it will not recur (p. 336).

Their reasoning is that a bug can come back, and that nobody has time to hunt bugs the tests could have found, because that time is needed for writing new code, which brings new bugs of its own (p. 336).

In another chapter the book calls a print call or a snippet typed into a debugger or a REPL an ad hoc test, and says to formalize it at the end of a debugging session, because where the code has gone wrong once, more trouble is likely (p. 273). «Не отбрасывайте написанный вами специальный тест»: add it to the unit test suite (p. 273).

*Code Complete* explains why size is no excuse. It reports that the chance of a wrong change rises as the changed lines go from one to five and falls after that (Weinberg, 1983), that a first attempt at a change is wrong more than half the time (Yourdon, 1986b), and that programmers treat small changes lightly, do not ask for review and sometimes do not even run the program (p. 567). Its moral: «рассматривайте простые изменения так, как если бы они были сложными» (p. 567). One organisation that began reviewing one-line changes saw the share of faulty changes fall «с 55% до 2%» (Freedman and Weinberg, 1982; p. 567).

Fowler's *Refactoring* states the same habit: "When you get a bug report, start by writing a unit test that exposes the bug" (2nd ed., ch. 4, Much More Than This, PDF p. 117). He gives two reasons: the test keeps the bug from returning, and working out the bug and its test may show further gaps in the suite (PDF p. 117).

This wiki joins the tip on p. 336 and the ad hoc test of p. 273, because both end in a permanent test, and reads every escaped defect as leaving a check behind, whichever way it was found.

## Sign in code

- A diff that changes production code to fix a defect and changes no test, however small the fix: a one- to five-line change is the likeliest to be wrong (p. 567).
- A comment standing in for a test, with no test for that case: a warning not to pass a certain value with a bug reference, a note of a manual check, or a snippet to paste into a REPL.

This wiki assigns the two neighbouring shapes by whether a test exists. This page owns a fix with no test at all. A test or reproduction that exists and proves nothing, such as a test that also passes on the unfixed code or a list of manual steps, belongs to [[failing-test-before-the-fix]]. New logic with no test, in a diff that fixes no defect, is [[test-early-often-automatically]]. A refactoring of an interface, a schema or a boolean expression that shares its step with other refactorings is [[scale-review-to-refactoring-risk]].

## When not to apply

The book allows no exceptions. The following limits are this wiki's own:

- The fix removes the possibility of the fault, for example when a type makes the bad state unrepresentable. No test can express the old failure. If the bad value can still arrive at a conversion from outside, test that conversion instead.
- The failure was not in code: a mistyped setting, an outage, a bad deployment. There is no code behaviour to pin.
- A race that can be reproduced only by chance. A test that fails intermittently costs more than it protects. Make the timing controllable first. If that is impossible, say in the change why no test exists.
- The change is a text correction with no behaviour, such as a typo in a user-facing message, and a test would pin only the literal string. See [[brittle-tests]].
- A probe that only explored what the code was doing and showed nothing wrong has nothing to formalize.

## Repair

1. Write an automated test that reproduces the reported failure, and see it go red against the unfixed code. Where a debugging session left a probe, start from the input it exposed.
2. Make the fix and see the test go green.
3. Keep the test at the lowest level that reproduces the failure, so it stays fast and points at the cause. See [[test-levels]].
4. Remove the print call, the snippet or the comment that stood in for the test.
5. Ask what else the bug says the suite is missing, as Fowler does (PDF p. 117), and add the neighbouring cases ([[test-data-classes]]).

This wiki notes that step 1 also confirms the test can fail, which is the single-test form of [[sabotage-your-tests]].

## Before and after

Before. The fix is correct and nothing stops the defect returning:

```
function parse_quantity(text):
-    return to_int(text)
+    return to_int(trim(text))

# no test changed; the report said " 3" from the import file crashed
```

After:

```
function parse_quantity(text):
    return to_int(trim(text))

test "quantity with surrounding spaces, as in the import file":
    assert parse_quantity(" 3") == 3
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation (Dialektika, 2020), see [[pragmatic-programmer]], p. 336, for the rule and its reasoning, and p. 273 for ad hoc tests.

McConnell, *Code Complete*, 2nd ed., Russian edition, see [[code-complete]], section 24.4, p. 567, citing Weinberg (1983), Yourdon (1986b) and Freedman and Weinberg (1982), for the figures on small changes and the moral to treat them as complex. The book's remedy there is review; reading the figures as a reason for a test is this wiki's own, as is the assignment against [[scale-review-to-refactoring-risk]].

This wiki's own: joining the tip on p. 336 and the ad hoc test of p. 273 on one page, the reading that every escaped defect leaves a check, all of `## Sign in code` and the assignments against [[failing-test-before-the-fix]] and [[test-early-often-automatically]], all of `## When not to apply` (the book states no limits), all of `## Repair` except step 5, and the pseudocode.

Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 4, "Much More Than This", PDF p. 117: the test written first on a bug report, its two reasons, and step 5.
