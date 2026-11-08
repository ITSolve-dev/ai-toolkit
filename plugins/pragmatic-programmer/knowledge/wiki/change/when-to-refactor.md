---
title: When to refactor
category: change
summary: "Use when deciding whether to refactor now: before a change (preparatory), on code that took thought to understand (comprehension), on bad code passed through (litter pickup, timed by refactor-early-and-often), and not at all for ugly code nobody needs to change."
tags: [method, refactoring, opportunistic-refactoring, legacy-code, timing]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Fowler describes refactoring as something he does "every hour I program" and lists the occasions on which it fits into the work (ch. 2, PDF pp. 61-67). This page turns those occasions into a decision a reader can run on the code in front of them.

This wiki assigns the neighbouring pages as follows. Whether to act now on a finding on lines a change touches is [[refactor-early-and-often]]; which code deserves the effort is [[where-to-refactor]]; the occasions in the course of work that call for refactoring are [[when-to-refactor]].

## The occasions

1. **Before a change: preparatory refactoring.** If the code would be easier to change in another shape, change the shape first ([[preparatory-refactoring]]).
2. **While reading: comprehension refactoring.** "Whenever I have to think to understand what the code is doing, I ask myself if I can refactor the code to make that understanding more immediately apparent" (PDF p. 63). Awkward conditionals and badly named functions are his examples. Following Ward Cunningham, Fowler says refactoring moves the understanding from his head into the code itself, and running the software tests that understanding (PDF p. 63). Early renames and splits of long functions let him see design issues he could not see before, which Ralph Johnson likens to wiping dirt off a window (PDF p. 63). Chapter 1 closes on the same loop: "Read the code, gain some insight, and use refactoring to move that insight from your head back into the code" (PDF p. 54).
3. **On bad code passed through: litter-pickup refactoring.** The code is understood but done badly: convoluted logic, near-identical functions that one parameterized function could replace (PDF p. 63). When to act on it, now or after the current task, is ruled on [[refactor-early-and-often]], which holds Fowler's timing beside *The Pragmatic Programmer*'s. The camping rule is also on [[easier-to-change]].

Fowler also names planned refactoring episodes, which "should be rare" (PDF p. 65), and long-term refactoring spread over weeks of a team's work (PDF p. 65; the library case is on [[parallel-change]]). This wiki treats both as settings of team process outside the code, not occasions a reader can find in it.

## When not to refactor

- The code is a mess but does not need modifying and can be treated as an API (PDF p. 67).
- Rewriting is easier than refactoring. Fowler cannot give a rule for that call; he often has to try refactoring for a while to find out (PDF p. 67).
- The refactoring is large and the change needing it small; the code is rarely touched; or the right improvement is not yet clear (PDF p. 68). These are judgement calls Fowler says he cannot quantify.

On legacy code, even with tests, he does not refactor the whole mess at once but improves the pieces he passes through, more in areas visited often, because frequent visits give the larger payoff (PDF p. 73).

## What the reader can point at

This wiki reads the occasions against code as follows. A function that took several minutes to understand because of its names or its conditional shape is a comprehension case; two near-identical functions found while working nearby are a litter-pickup case; neither is a reason to refactor a file the current task does not read. Fowler reports that among his colleagues too little refactoring is "far more prevalent than too much" (PDF p. 68); this wiki takes from that a review consequence: a reviewer who finds an easy litter-pickup fix in touched code should not dismiss it as scope creep.

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 1, "Final Thoughts" (PDF p. 54); ch. 2, "When Should We Refactor?" through "When Should I Not Refactor?" (PDF pp. 61-67), "Slowing Down New Features" (p. 68), "Legacy Code" (p. 73). This wiki's own: the reading against code, the review consequence, the treatment of planned and long-term refactoring as process settings, and the assignment against [[refactor-early-and-often]] and [[where-to-refactor]].
