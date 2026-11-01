---
title: Release Plan
category: periods
summary: A high-level plan over a period longer than an iteration; a list of stories, its assumptions, and the destination that keeps iterations from being a sequence of false peaks.
tags: [concept, iterations, release, period-versus-milestone]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Release Plan

A release plan is the plan one level above an iteration. Cohn defines it plainly: "Release planning is the process of creating a very high-level plan that covers a period longer than an iteration." ([[cohn-agile-estimating-planning]] L2761). His typical figures are three to six months and three to twelve or more iterations, with the count depending on iteration length (L2761), and he adds that releases can run more or less often depending on the type of software (L2947). Those figures describe a human team shipping a product, and this wiki does not transfer them to a few people steering an agent as a target size. The level sits in [[planning-horizons]].

## What it is for

The source gives three reasons (L2763-L2767):

1. It decides how much must be developed and how long that takes before the product is releasable.
2. It conveys what is likely to be developed and when, which other planning depends on.
3. It is a guidepost. "Without the concept of a release, teams move endlessly from one iteration to the next." (L2767). "A release plan provides context that allows iterations to combine into a satisfying whole." (L2767).

The third reason is the one that carries a failure. Cohn's image is the hiker who heads for the highest visible peak, reaches it, finds it a false peak, and repeats (L2767). The cure he names is a plan "that shows a team’s current expectation of where they ultimately wish to arrive" (L2773). He calls this "a fundamental concern with any iterative process, not just agile ones" (L2767).

## What it contains

"The release plan itself is usually documented as simply a list of the user stories that will be developed during the project." (L2779). Items are stories, meaning descriptions of functionality to be delivered, not engineering tasks (L2781). What it deliberately leaves out is on [[release-plan-level-of-detail]].

Where the setting warrants it, the plan also states its key assumptions: who is on the team, how long the iterations are, when the first iteration starts and when the last finishes (L2783-L2789). This wiki reads those assumptions as what makes the plan checkable later: each is a fact that can be compared with what happened, and a change in one is a reason for [[updating-the-release-plan]].

## Period versus milestone

The line between the two is on [[release-versus-iteration]]. This wiki reads this chapter as agreeing with it: an iteration is bounded by the calendar, and a release is judged against its [[conditions-of-satisfaction]], of which a date is one that may be fixed. Whether the date or the scope gives way is the split on [[date-driven-vs-feature-driven]]. How stories are selected for it is [[fitting-stories-into-a-release]].

## Sign of the failure

This wiki's sign for the false-peak failure: iterations follow one another on a board and nothing above them names what they add up to, so asking what is left before something can ship has no answer from the board. The sign raises a question: a project of independent small fixes may have no release to name.

## Agent executor note

This wiki reads the guidepost reason as not depending on a human executor. It arguably strengthens, because an agent works the task in front of it and does not carry the destination between tasks unless something states it. The source does not address this.
