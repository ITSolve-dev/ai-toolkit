---
title: 6x2+1
category: periods
summary: A macro-cycle of six two-week periods followed by a one-week period in which the team picks its own work; what transfers is reserved capacity for work the normal queue crowds out, and its failure is the short period becoming a dumping ground for earlier sloppy work.
tags: [method, iterations, period-length, technical-debt]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# 6x2+1

6x2+1 is Cohn's macro-cycle for teams on two-week periods: "six two-week iterations followed by a one-week iteration" ([[cohn-agile-estimating-planning]] L3512). During the two-week periods the owner of the order sets the work. During the one-week period "the team chooses its own work" (L3512). By this wiki's arithmetic the cycle is 13 weeks long.

## The method

1. Run six two-week periods in the normal way.
2. Run one one-week period whose content is chosen by the people doing the work, for what they see as priority work for the project.
3. Start the next cycle.

Cohn's examples are refactorings felt to be too risky in the middle of other periods, experiments with relevant new technology, automating legacy manual tests, and working on an upcoming large feature that has not had enough attention (L3512).

## What it is for

Cohn's stated reason is strain: endless two-week periods wear on a team because "a deadline is never further away than next week" (L3512), and the week can be "very reinvigorating" (L3514). Morale is outside this wiki's scope, so that benefit is noted and not used.

This wiki keeps a second purpose found in the same passage: the week is time to "work off some of the technical debt" (L3514). That is capacity reserved for work that the normal order crowds out, and it is the part that a board can show.

## Failure mode

> It is important to stress that this one-week iteration is not a dumping ground for the sloppy work of prior iterations.
>
> — [[cohn-agile-estimating-planning]], L3514

The distinction Cohn draws is between debt incurred while learning or inherited from before, and sloppiness from recent periods. **Sign in board history:** the short period is filled with tasks unfinished or reopened from the periods just before it. This sign is this wiki's. If it appears, the earlier periods were overfilled or their finished check was relaxed, and the short week is hiding that ([[unfinished-at-period-end]]).

## Interaction with fixed length

The cycle varies the length on purpose, which looks like a violation of the fixed-length rule in [[period-length]]. This wiki reads the difference as planned against reactive: the 6x2+1 pattern is fixed in advance and does not follow the size of the work. It should be recorded as setup, otherwise the sign on [[period-length]] fires on it. The short week should also be left out when comparing period results.

## Trade-off

One week in thirteen does not go to the prioritized order, so a new idea can wait longer ([[new-idea-latency]]). The source does not weigh this.

## Agent executor note

The strain mechanism does not survive for an agent executor, so the rhythm of the cycle has no human reason on that side. The reservation does survive, because an agent working through an ordered queue will never reach work that is never ordered. "The team chooses" cannot pass to the agent: this wiki reads the choice as belonging to the people steering, with the plugin proposing candidates. Whether a scheduled week beats a standing share of each period for such work has no evidence here.
