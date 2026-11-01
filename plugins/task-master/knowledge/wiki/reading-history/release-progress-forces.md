---
title: Forces on Release Progress
category: reading-history
summary: Work remaining in a release changes through three separate forces, work completed, requirements added or removed, and estimates revised, so explaining plan against fact means splitting a change in remaining work into these three before judging it.
tags: [method, retrospective-analysis, plan-versus-fact, scope-change, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Forces on Release Progress

A release plan states something like "over the next four months and eight two-week iterations we will complete approximately 240 story points" ([[cohn-agile-estimating-planning]] L4271). The question at any later point is where the team stands against that. Three things move the answer:

1. **Completed work:** reduces what is left.
2. **Changed requirements:** the owner adds or removes work. "If the product owner adds forty story points and the team completes thirty, the team is now further away from the end of the project." (L4273)
3. **Revised estimates:** the team learns something and changes the size of work still ahead (L4273).

The source's phrase is "completed work, changed requirements, and revised estimates" (L4275).

## Method

For the period being explained, read from board history:

1. The estimate total of tasks that crossed the finished point: completed.
2. The estimate total of tasks that entered the release, and of those that left: scope.
3. The sum of estimate changes on tasks still open: re-estimation.
4. Check that remaining at start, minus completed, plus scope change, plus re-estimation, equals remaining at end. A residual means the history is incomplete.

The steps are this wiki's; the source supplies the three forces and the burndown reading ([[release-burndown-chart]], [[release-burndown-bar-chart]]). When a re-estimate is justified at all is on [[re-estimate-when-relative-size-changes]].

## Reading the result

The three forces mean different things, and a higher total of remaining work is not itself a defect. The source says added work "may be the result of the team having learned something that directs them at a more valuable release" (L4332).

Whether scope growth matters depends on two inputs the source names: "whether the trend is likely to continue and how important the initial target release date is" (L4365). The first is read from the sequence of scope changes across periods. The second is not on a board and has to come from the people steering.

The source's example sign for attention is the state where "so far, more has been added than has been completed" (L4365). In that example 50 points were added against 30 completed (L4357), and the source says it may not be a concern. A sign here raises a question ([[smell-is-not-a-finding]]).

## Causes of slower net progress

The source lists for a fall to 20 from an expected 30: stories underestimated, re-estimation of remaining work, or absence (L4373). This wiki notes that the first shows in the completed total only over time, and the second shows as estimate changes. Only the third is outside the board, and for this wiki it is out of scope as a people matter.

## What this cannot show

The split says what moved the total. It does not say whether the change was worth making, and [[chosen-delay-versus-slip]] takes that question up for a later finish. Neither scope additions nor removals carry a judgement of value in the history, and prioritizing stays with the owner: "Prioritzation of work is still up to the product owner who can add or remove functionality as desired." (L4375; the spelling is the source's.)

## Failure mode

Reporting a single progress figure while scope grows. Sign: completed work looks steady and the release date recedes with no stated reason. The same sign appears when re-estimates are absorbed silently. This failure and its sign are this wiki's.

## Agent executor note

The method reads history and depends on no human executor. It requires estimates to change visibly on the task and not to be overwritten by a re-cut, or re-estimation vanishes from the split. This condition is this wiki's.
