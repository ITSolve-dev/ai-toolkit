---
title: Binary search debugging
category: debugging
summary: "Use when a failure sits in a long stack trace, a large failing input, a large region of code or an unknown change across releases, and candidates are being checked one by one; or a new defect appeared after an edit and looks unrelated to it, and nobody has diffed against the last working version."
tags: [method, debugging, bisection, regression, version-control, diff]
paradigm: any
sources: [pragmatic-programmer, code-complete]
created: 2026-11-01
updated: 2026-11-06
---

Binary search debugging halves the suspect space on each probe, so the effort grows with the logarithm of the candidates and not with their number. The book applies the method to three spaces (p. 130) and compares a linear scan, which is O(n), with binary search, which is O(log n) (p. 129).

## What the method needs

A probe with a yes or no answer: at this point, has the fault already appeared? This wiki adds a precondition the book implies: the suspect space must be ordered so that the answer stays the same on one side of the fault. Where the fault appears and disappears, halving can discard the half that holds it.

## Stack frames

When a huge stack trace must show which function corrupted a value, pick a frame near the middle and check whether the error is already visible there (p. 130). If it is, look at earlier frames, otherwise at later ones, and repeat (p. 130). With 64 frames, the book counts no more than six attempts (p. 130).

## Input data

The typical case is a program that passes all test data and a week in production, then fails on one specific data set (p. 129). Copy the data set, feed it to a local copy of the program and confirm that it still fails (p. 129). Split the set in two, check whether the error shows with either half, and continue until the smallest failing set remains (p. 130). This wiki adds that the result can become the test in [[failing-test-before-the-fix]].

## Code

McConnell applies the same halving to the program itself, under the tip "narrow the suspicious region of code" (p. 535). Rather than test the whole program, class or routine, test a smaller piece; more effectively, remove parts of the program systematically and see whether the error still occurs.

1. **Remove about half.** «Попробуйте удалить в первый раз примерно половину кода» (p. 535). If the error disappears, it is in the removed half; if it persists, the defective code is still present. Halve the guilty half and repeat (p. 535).
2. **Choose the cheapest way to remove code.** With many small routines, comment out calls; otherwise disable blocks with comments or preprocessor directives. With a debugger nothing need be removed: set breakpoints or skip routine calls and watch whether the error disappears (p. 535).
3. **Widen the region if halving finds nothing.** Focusing on a small region pays only if the defect is certainly there. «Если дефект не удается найти в конкретной области кода, рассмотрите вероятность того, что его в ней нет» (p. 535). Widen it and bisect again; see [[mental-set-in-debugging]].
4. **Integrate incrementally to keep the search small.** Add pieces to a system one at a time; if a new error appears after adding one, remove it and test it separately (p. 536).

The same halving finds an elusive syntax error: remove part of the code and recompile (p. 538).

## Releases

For a defect introduced some releases ago, write a test that fails on the current release, then pick a version midway between it and the last version known to work (p. 130). Rerun the test to decide which way to narrow (p. 130). The book notes that this depends on good version control, and that many such systems automate the process by choosing releases from test results (p. 130). *Code Complete* adds the cheaper first probe: run an old version, and if it does not fail, diff the versions or read the version-control log for recent changes (p. 535).

Chapter 28 gives the same move as one use of source-code control: when a new error appears after a change and seems unconnected to the edits, compare the new version of the code with the old one, and if that does not help, look at an even older version (p. 652). Version control makes this possible because it can return any registered version of any file and list the changes made in each, with every check-in recording why the file changed (pp. 652-653). The same chapter names what history protects against: without change control a routine that has had several fixes and grown new defects cannot be returned to its last working version, and code can look better tested than it is because the version that passed the tests was an older one (p. 649).

This wiki's reading, as a procedure for the case "a defect appeared after an edit and looks unrelated to it":

1. Find the last version known to work.
2. Diff it against the current code and treat every hunk as a suspect, including the ones that seem unrelated, since "seems unrelated" is exactly the situation the book describes.
3. If the diff holds many hunks, or the good version is several commits back, stop stepping back one version at a time and halve the range as above.

Its limits, also this wiki's own: it needs a version that worked, so a defect present since the code was written is left to [[debugging-procedure]]; it finds the change that exposed the defect, which may have uncovered a latent defect elsewhere, so it ends the search for *when* and not always for *where*; and it loses most of its power when each commit bundles many unrelated edits, which is why small single-purpose changes ([[refactor-in-small-tested-steps]], [[one-change-at-a-time]]) keep the search space small.

## Failure modes

The following three are this wiki's own.

- The failing input or code needs two parts together, so each half passes alone. Keep a fixed part and halve the rest, and stop at the smallest set whose removal makes the error vanish rather than at a single line. *Code Complete*'s remark that a cause is often a combination of factors (p. 534) is the reason.
- A release in the range does not build or run, so the probe gives no answer. Skip it and take a neighbour.
- The test used as a probe is itself flaky, so a single wrong answer discards the half holding the defect. Fix the probe first.

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation: [[pragmatic-programmer]], pp. 128-130. The three applications, the six-attempt figure and the mention of automation are the book's. The monotonic-probe precondition, the link to [[failing-test-before-the-fix]] and the failure modes are this wiki's own.

McConnell, *Code Complete*, 2nd ed., Russian edition: [[code-complete]], section 23.2, pp. 534-538. The halving of code, the ways to remove it, the old-version probe, widening the region, incremental integration and the syntax-error case are that book's, paraphrased except where quoted; quotations were transcribed from the extracted text with line-break hyphens joined. The extension of the first failure mode to code is this wiki's own. Section 28.2, pp. 649, 652-653: comparing new and old versions when a new error seems unrelated, returning to any version, the change log, and what uncontrolled changes cost; the diff procedure, its third step and its limits are this wiki's own.
