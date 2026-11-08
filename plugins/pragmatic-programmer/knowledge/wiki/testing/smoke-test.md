---
title: Smoke test
category: testing
summary: "Concept: a shallow end-to-end run of the whole built system that decides whether a build is fit for deeper testing; a pipeline whose only post-build check is that the build succeeded, or an entry point of the built system that no smoke-test step invokes, gives false confidence."
tags: [concept, smoke-test, integration, build, end-to-end]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

A smoke test is a relatively simple check, run after the whole system has been built, of whether the product "smokes" when executed (p. 686). McConnell pairs it with the daily build: every file is compiled, linked and assembled into an executable, and the smoke test is then run against it. The translator's note traces the term to electronics, where a device is switched on to see whether it smokes (p. 686).

## What it pins

The test exercises the whole system from end to end. It need not be exhaustive, but it must be able to find the major problems, and be thorough enough that a build passing it can be treated as stable for more thorough testing (p. 687). McConnell's minimum for a good build is that all files, libraries and components compile and link, and that it has no serious defects that prevent the program from starting or make its run unpredictable; in other words, that it passes the smoke test (p. 687).

This wiki reads the smoke test as the gate at one level of [[test-levels]]: it does not check any module's logic, only that the assembled whole starts and runs its main paths. A smoke test that re-checks a module's details belongs at the unit level instead.

## Failure modes

**A build without the test.** Without a smoke test, McConnell says, daily builds become long exercises that only confirm the code compiles every day without error (p. 687). The sign: a build pipeline whose only post-build step is that the build succeeded.

**A test that stopped growing.** The smoke test must evolve with the system: at first it may check something as simple as whether the system can say "Hello, World", later it may take ten minutes, an hour or more (p. 687). If it is not kept current, the daily build becomes self-deception: «разрозненный набор тестовых данных создает ложную уверенность в качестве продукта» (p. 688). This wiki takes from that a sign: an entry point or command the built system exposes that no smoke-test step invokes.

**Run by hand.** Without automation, building and smoke testing are impractical (p. 688). See [[test-early-often-automatically]].

**Run only centrally.** McConnell asks developers to smoke-test their own code against a private build before adding it, so that new code passes the check before it can affect the rest of the system (p. 688). This is practice advice with no sign in code; it is kept as the book's context. The checklist asks the same in short: is a smoke test run for every build, so you know whether the build works (p. 691).

A test that only loads a component and asserts nothing else is not a defect when it is a deliberate smoke test of packaging or wiring; [[test-that-verifies-nothing]] owns that distinction.

## Why it pays

The book's diagnostic argument: when the product is built and tested every day, a breakage is easy to place. If the system worked on day 17 and stopped on day 18, something between those two builds broke it (p. 686). This wiki reads it as the same localization that [[small-steps-with-feedback]] buys per step, applied per day; McConnell also notes that weekly builds lose almost all the advantages of frequent builds, because one broken week can mean several weeks to the next good build (p. 687).

## When not to apply

The book states no limit on the smoke test itself. It limits the frequency of integration around it: it judges literally continuous integration, every change every couple of hours, beyond reason for most projects, and says that if changes are synchronised daily there is no need to do so continuously (pp. 690-691). The transfer here is ours: a smoke test that has grown to an hour or more is no longer a quick gate before each change, and at that size it belongs to the scheduled build rather than to every commit.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 29.4, pp. 686-691; see [[code-complete]]. The definition, the good-build minimum, the requirement to keep the test current and automated, the private-build check and the day-17/day-18 argument are the book's; McConnell notes much of the section is taken from his *Rapid Development*, ch. 18 (p. 686). The quotation was transcribed from the extracted text and needs the page-image check. This wiki's own: the signs, the placement among test levels, the link to [[test-that-verifies-nothing]], and the limit on test size.
