---
title: Date-Driven Versus Feature-Driven
category: periods
summary: The test for which factor is fixed in a release, the date with scope negotiable or a feature set with the date following from it, and which computation each one takes.
tags: [decision-rule, iterations, release, period-versus-milestone]
sources: [cohn-agile-estimating-planning, flow-metrics-scrum-teams]
created: 2026-11-01
updated: 2026-11-02
---

# Date-Driven Versus Feature-Driven

A release usually has one preeminent condition, and Cohn says many projects are either date-driven or feature-driven ([[cohn-agile-estimating-planning]] L2804).

> A date-driven project is one that must be released by a certain date but for which the feature set is negotiable.
>
> — [[cohn-agile-estimating-planning]], L2804

> A feature-driven is one that we would probably like to release as soon as possible but consider the completion of a set of features more important.
>
> — [[cohn-agile-estimating-planning]], L2804

This wiki reads [[fixed-date-variable-scope]] as the first of these. Its "When it does not hold" section is the second, which Cohn names here.

## The test

Ask which gives way when the two collide. If the date holds and stories fall out, the release is date-driven. If the stories hold and the date moves, it is feature-driven. The phrasing is this wiki's, and it is the same question as the period-versus-milestone test on [[release-versus-iteration]] and [[commitment-over-a-period]], asked of one release.

**Input and where it comes from.** The answer comes from whoever owns the goal for the release: it is part of the [[conditions-of-satisfaction]]. An external event is the strong case. SwimStats is date-driven because the swim season starts on a fixed date and the release has to be out a month earlier, so something must ship in three months "even if it is only the basics for small swim teams" (L2891).

## What each choice computes

| | Date-driven | Feature-driven |
|---|---|---|
| Fixed | Iterations, from the calendar | The set of needed features |
| Computed | Points that fit: iterations × velocity | Iterations needed: sum of estimates ÷ velocity |
| Output | How far down the ordered list the line falls | When it finishes |
| Computed without points | How many items by the date, at a chosen probability | Days until the items finish, at a chosen probability |

Source for both columns: L2832-L2834, and for the last row [[flow-metrics-scrum-teams]] L1392-L1408 and L1422-L1428, on [[throughput-monte-carlo]]. The mechanics and the worked numbers are on [[fitting-stories-into-a-release]], and the feature-driven division on [[deriving-duration-from-velocity]].

## What would show the choice wrong

This wiki's reading, not the source's: the board's history shows it. A release labelled date-driven whose date moved while the scope stayed intact was feature-driven in fact. One labelled feature-driven in which stories were quietly dropped to hold a date was date-driven in fact. Either way the release plan should be recomputed with the real fixed factor.

## Trade-off and limits

Both choices give up something. Date-driven accepts less than was wanted, and the order of the list decides what is lost, which makes [[value-order-versus-technical-necessity]] matter most here. Feature-driven accepts an open end date, and the source still frames it as wanting release "as soon as possible" (L2804), so this wiki does not read it as a licence to take longer.

The source says "Many", not all, and gives no test for a project where neither is preeminent. This wiki reads that as: such a project has unresolved conditions, and the question goes back to the person setting the goal rather than being settled by the plugin.

## Agent executor note

This wiki reads the split as being about what the goal-owner will give up, so it survives unchanged when an agent executes. It is a question to ask at project setup, since the plugin cannot read it from a board.
