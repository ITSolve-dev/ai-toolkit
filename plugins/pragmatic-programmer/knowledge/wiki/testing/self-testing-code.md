---
title: Self-testing code
category: testing
summary: "Concept: an automated suite fast enough to run after every small step and sure to fail on a programming error; what refactoring rests on. Without it, only tool-automated safe refactorings remain, or tests inserted at seams first. Its payoff is that a failure points at the last few minutes of change."
tags: [concept, testing, self-testing-code, refactoring, legacy-code, seams]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Self-testing code, in Fowler's sense, is code accompanied by "a suite of automated tests that I can run and be confident that, if I made an error in my programming, some test will fail" (ch. 2, PDF p. 76). He calls it the first foundation of refactoring. In chapter 1 the same idea is a tip: "Before you start refactoring, make sure you have a solid suite of tests", and the tests must be self-checking (PDF p. 10); what that demands of one test is [[test-early-often-automatically]].

## Why refactoring needs it

Mistakes during refactoring "aren't a problem provided I catch them quickly" (PDF p. 71). Each refactoring is small, so a failure points at a small change, and if the fault is still not found the work can be reverted to the last working version. Catching errors quickly requires a comprehensive suite that runs fast, so that running it often is not deterred (PDF p. 71). The payoff Fowler states: when a test fails, the change since tests last passed is "only a few lines of code" (PDF p. 72), which makes the bug easy to find. That is also his answer to the worry that refactoring introduces bugs: without self-testing code, he grants, the worry is reasonable (PDF p. 72).

This wiki reads two properties out of that, both checkable: the suite must be automated and must run in a time short enough to run after each step. A suite that exists but takes long enough to be run only before a commit does not give the few-lines guarantee.

## Without it

- **Safe automated refactorings only.** In an environment with good automated refactorings, those can be trusted without running tests; the menu shrinks but useful work remains (PDF p. 72). A related style uses only refactorings proven safe, followed step by step, which teams have used on large poorly tested code bases; it is language-specific and Fowler does not cover it (PDF p. 72). See [[automated-refactoring]].
- **Legacy code.** "If you have a big legacy system with no tests, you can't safely refactor it into clarity" (PDF p. 73). Adding tests is harder than it sounds, because a system is easy to put under test only if it was designed for it. Fowler defers to Feathers' *Working Effectively with Legacy Code*: find seams where tests can be inserted. Creating seams is itself refactoring done without tests, much more dangerous but a necessary risk, and the place where safe automated refactorings help most (PDF p. 73).

## How the habit pays (ch. 4)

Chapter 4 gives the reasoning from Fowler's own experience. He first wrote tests that printed values to the console for him to check, found it boring and did it rarely. The step that changed things was putting the expected values into the tests, so that a run reports only success or the failures: "Make sure all tests are fully automatic and that they check their own results" (ch. 4, PDF p. 101). What a single test owes on this point is [[test-early-often-automatically]].

His argument is about where debugging time goes: fixing a bug is quick, and finding it is slow. If the tests passed a few minutes ago and fail now, the bug is in the code written since, which is still fresh in mind. He calls the suite "a powerful bug detector that decapitates the time it takes to find bugs" (PDF p. 101). The value comes from automatic checking and frequent running together. His cadence is to run the tests for the code being worked on at least every few minutes, and all tests at least daily (PDF p. 108).

- **Test first.** Fowler calls writing the test before the code one of the most useful times to write it: it asks what has to be done, keeps attention on the interface rather than the implementation, and gives a clear point at which coding is finished (PDF p. 102). He recommends TDD and does not develop it in this book; see [[test-driven-development]].
- **Cost.** Tests are a lot of extra code. His answer is that the debugging time saved pays for them, and that a small amount of testing gives surprisingly large benefits (PDF pp. 101-102).
- **Unit tests as the backbone.** Most tests in a self-testing system are unit tests, each covering a small area and running fast (PDF p. 116). This wiki adds that a slow test gets run less often, and that brings back the long bug hunt.
- **The suite is maintained like code.** Fowler says he works on the test suite constantly, as much as on the main code (PDF p. 117).

How to choose and shape the tests is on [[test-by-risk-not-by-method]], [[fresh-fixture-per-test]] and [[one-verification-per-test]]; putting untested code under test first is [[adding-tests-to-existing-code]].

## Relations

The step discipline this concept makes safe is [[refactor-in-small-tested-steps]]. What a test should pin, and what makes it brittle, is [[brittle-tests]]; keeping old tests running after each change is [[regression-testing]].

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 1, "The First Step in Refactoring" (PDF p. 10); ch. 2, "Testing" (PDF pp. 71-72), "Legacy Code" (pp. 72-73), "Refactoring and the Wider Software Development Process" (p. 76). Ch. 4, "Building Tests", PDF pp. 101-102, 108, 116-117: self-checking tests, the debugging-time argument, the cadence, test first, the cost, unit tests as the backbone, and the suite maintained like code. This wiki's own: the two checkable properties and the reading of a slow suite. The note that a slow test brings back the long bug hunt is also this wiki's own.
