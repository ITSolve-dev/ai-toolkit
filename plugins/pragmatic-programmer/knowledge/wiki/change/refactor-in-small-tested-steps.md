---
title: Refactor in small tested steps
category: change
summary: "A large restructuring diff with no intermediate green state, structural change applied to code that no test covers, or a refactoring started or continued while a test fails instead of backing out to the last green state."
tags: [rule, refactoring, testing, small-steps, checkpoints]
paradigm: any
sources: [pragmatic-programmer, code-complete, fowler-refactoring]
created: 2026-11-01
updated: 2026-11-07
---

Large structural change is made safe by making it out of many small ones, with a check after each. The book warns that hacking away at large chunks of code can leave you worse off than before you started (p. 263), and gives Fowler's guidance for avoiding this.

## Rule

Have good tests before you start and run them often. «Продвигайтесь короткими, осторожными шагами» (p. 263): move a field from one class to another, split a method, rename a variable.

The book's reasoning has two parts. Refactoring often means many small local changes that add up to a large one (p. 263). If you keep steps small and test after each, you avoid long debugging (p. 263), because you learn quickly whether a change broke something (p. 263). This wiki reads the mechanism as bounded search: after a failure, the cause lies in the last step. The general form is [[small-steps-with-feedback]].

*Code Complete* gives the same discipline in more operational detail, under the heading of safe refactoring (pp. 566-567); McConnell warns that refactoring, like any powerful tool, does harm when misused (p. 566). Its practices:

- **Save the code you start from**, in version control or a backup copy.
- **Keep each refactoring small**, so that all its consequences stay visible.
- **Do one refactoring at a time**, except for the simplest, recompiling and retesting before the next.
- **Write the list of steps** that leads from A to B; the book calls this a natural extension of the Pseudocode Programming Process ([[pseudocode-programming-process]]).
- **Keep a list of refactorings to do later.** One refactoring reveals the need for another; if it is not needed now, write it down instead of starting it.
- **Make frequent checkpoints**, so that a refactoring that goes sideways can be abandoned back to a working program.
- **Use the strictest compiler warnings** to catch small errors right after they are made ([[do-not-silence-warnings]]).
- **Retest** with regression tests, which presuppose a good test suite, and **add test cases** for new code while deleting tests the refactoring made obsolete.

Fowler's own *Refactoring* gives the working rhythm at first hand. He calls it the essence of the refactoring process: "small changes and testing after each change" (2nd ed., ch. 1, PDF p. 13). When a test fails after a small step, only a small change has to be considered to find the mistake; when too much is done at once, a mistake forces "a tricky debugging episode that can take a long time" (PDF p. 13). He commits to a private local repository after each successful refactoring, so that he can get back to a working state, and squashes those commits into more significant ones before pushing to a shared repository (PDF p. 14).

When a step goes wrong he does not debug forward: "whenever things get difficult, my first reaction is to take shorter steps" (PDF p. 28). If a test fails and he cannot see and fix the problem at once, he reverts to the last good commit and redoes the step in smaller pieces; he says this works because he commits so often and because small steps are what make him fast on difficult code (PDF p. 28). The steps in his example are very small: four separate commits to remove one accumulator variable ([[remove-loop-accumulator]]), and each variable rename inside a new function done one at a time (PDF pp. 22, 28).

He closes chapter 1 by naming "the rhythm of refactoring" as its most important lesson, and states the key as "recognizing that you go faster when you take tiny steps, the code is never broken, and you can compose those small steps into substantial changes" (PDF p. 55). Larger refactorings are sequences of such steps ([[split-phase]], [[move-function]], [[replace-conditional-with-polymorphism]]). He admits lapses: "I do sometimes get tired of doing it—and give mistakes the chance to bite me. Then I learn and get back into the rhythm" (PDF p. 46). In the middle of a step he uses a safety device: while moving conditional cases into subclasses, he makes the already-moved case in the superclass throw instead of deleting it, and says only that he likes the explicit throw (PDF p. 51). This wiki reads the reason as making a stray call to the old branch fail loudly. Chapter 2 gives the test that tells refactoring from other restructuring by step size ([[refactoring]]), and the suite the rhythm needs is [[self-testing-code]].

Chapters 4 and 5 turn the rhythm into two rules about the state of the suite. "Never refactor on a red bar": do not refactor while any test fails (ch. 4, PDF p. 109). And "Revert to green": when a step breaks a test, go back to the last state in which every test passed, usually the last version-control checkpoint, rather than repair forward (PDF p. 109). Fowler runs the tests that exercise the code being changed every few minutes and the full suite at least daily (PDF p. 108). The catalogue is written so that "each step of each refactoring is as small as possible", and the safe way is "to take very small steps and test after every one" (ch. 5, PDF p. 119). The size of a step is set by the situation: "the trickier the situation, the smaller the steps" (PDF p. 119). Fowler often takes larger steps than the mechanics describe, and when he hits a bug he backs out the last step and takes smaller ones (PDF p. 119). He treats the written mechanics as a checklist for the special cases each refactoring has, which are easy to forget, and offers them as one way among several that "work pretty well most of the time" (PDF p. 119). Each refactoring has a logical inverse, so a step can also be undone by its reverse (PDF p. 120). This wiki reads the red-bar rule as the precondition of the bounded search above: if the suite was not green before the step, a failure after it no longer points at the step ([[all-tests-pass-always]]).

How much review a step needs is decided on [[scale-review-to-refactoring-risk]].

## Sign in code

- The code being restructured has no test that exercises it.
- One change combines several kinds of restructuring across many files, or renames, extractions and loop changes of one function, with no intermediate commit in which the tests pass. This wiki reads the second half as the sign of Fowler's per-step commit lapsing (PDF pp. 14, 46).
- A restructuring step committed on top of a failing test, or a sequence of fix-up commits after a refactoring broke a test, where the history shows no return to the last green state. This sign is this wiki's reading of Fowler's red-bar and revert-to-green rules (PDF p. 109).
- A refactoring diff leaves tests for routines that no longer exist, or adds new routines with no test. This sign is this wiki's reading of *Code Complete*'s "add test cases, delete obsolete ones" (p. 567).

Test expectations changed inside a refactoring mean that behaviour moved too. Test expectations changed inside a refactoring are [[do-not-refactor-while-adding-features]]; a change that is only structural and too large to judge is [[refactor-in-small-tested-steps]]. Restructuring of code no test covers, or a large structural diff with no green state between its steps, is [[refactor-in-small-tested-steps]]; a refactoring of an interface, a schema or a boolean expression that shares its step with other refactorings is [[scale-review-to-refactoring-risk]].

## When not to apply

- There are no tests and none can be written without restructuring first. Fowler names the way out: in an environment with good automated refactorings he trusts them even without running tests, using only those that are safely automated, though he would still rather have self-testing code (ch. 2, PDF p. 72); restructuring to insert tests into legacy code is more dangerous without tests but a necessary risk (PDF p. 73). This wiki adds that the smallest such moves are used only until a test can be attached.
- *Code Complete* exempts the simplest refactorings from strict one-at-a-time and allows several low-risk ones together with regression tests only (pp. 566-567).
- An IDE's automated refactoring changes many files in one operation (p. 264). The step is large in lines and small in kind. This wiki still runs the tests afterwards.
- Fowler takes larger steps when the code is easy and shortens them when it gets difficult, and admits he does not always take steps as short as in his example (PDF p. 28). The size of a step follows how hard the code is; this wiki does not report a step for being larger than the book's.
- The fine-grained local commits are a working aid; Fowler squashes them before sharing (PDF p. 14). A shared history without them is not a violation of this page, so long as each step was tested before the next.
- The aim is replacement, not improvement. A rewrite is restructuring, not refactoring ([[refactoring]]), and this rule does not govern it.

This wiki reads slower progress as the cost of following the rule. The book asks for the activity to be done slowly, carefully and attentively (p. 263), and does not call that a cost.

## Repair

1. Before touching the structure, add tests pinning current behaviour, and start from a fully green suite (Fowler, PDF p. 109).
2. Write the list of steps, and park unrelated refactorings on a separate later-list. Name the next step. It should be one move.
3. Make it, compile with warnings on, run the tests, commit as a checkpoint.
4. If the tests fail and the cause is not obvious at a glance, revert to the last commit and redo the step in smaller pieces; do not debug forward (Fowler, PDF p. 28).
5. Add tests for code the step created; remove tests for code it removed.
6. Repeat until the large change has happened.

## Before and after

```
// before: one change
//   renamed Customer to Account
//   moved billing fields to a new class
//   split process() in three
//   tests run at the end, 14 failing
```

```
// after: a sequence, tests green at each line
// 1. add tests for process()
// 2. rename Customer to Account
// 3. move field billingAddress to Billing
// 4. move field taxCode to Billing
// 5. extract validate() from process()
// 6. extract charge() from process()
```

## Source

[[pragmatic-programmer]], Topic 40, pp. 263-264, reporting Fowler's guidance. The bounded-search reading, the signs, the split with [[do-not-refactor-while-adding-features]], the limits other than those credited to the books below, the reading of the cost, repair step 4 and the example are this wiki's own.

[[code-complete]], McConnell, 2nd ed., Russian edition, section 24.4, pp. 566-567, citing Fowler (1999): the list of safety practices and the exemption for the simplest refactorings. The third sign, the assignment against [[scale-review-to-refactoring-risk]] and repair steps 2, 3 and 5 as phrased are this wiki's own.

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 4, PDF pp. 108-109, and ch. 5, "Format of the Refactorings" and "The Choice of Refactorings", PDF pp. 119-120: the cadence of test runs, the red-bar and revert-to-green rules, the smallest-step catalogue, step size by difficulty, backing out to smaller steps, the mechanics as a checklist and the inverses. This wiki's own for that part: the reading of the red-bar rule as a precondition of the bounded search, and the sign drawn from both rules. Ch. 1, PDF pp. 13-14, 22, 28, 46, 51, 55: the rhythm, the local commits and squash, the revert-and-redo-smaller rule, the small steps of the example, the lapse, the throwing safety device and the closing lesson. Ch. 2, PDF pp. 72-73: refactoring without tests through safe automated refactorings, which is the first limit. This wiki's own for that part: the reading of the throw as a loud failure for stray calls, the reading of a combined commit as a lapsed rhythm, and the two limits drawn from Fowler's flexible step size and his squash.
