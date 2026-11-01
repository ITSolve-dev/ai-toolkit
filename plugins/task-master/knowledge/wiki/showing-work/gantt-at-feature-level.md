---
title: Gantt Chart at Feature Level
category: showing-work
summary: A Gantt chart is acceptable for showing which features sit in which iteration if it stops at features, runs each bar for the whole iteration, and names no individuals.
tags: [rule, visualization, gantt, iterations]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Gantt Chart at Feature Level

Cohn rejects the usual use of a Gantt chart but keeps one form of it. "Gantt charts have earned a bad reputation, but this is because of how they are often used to predict, schedule, and coordinate tasks", while the same chart "can be a great tool for showing the allocation of features to iterations" ([[cohn-agile-estimating-planning]] L4607). The chart answers one question: what is planned for which iteration.

## The three conditions and their signs

The conditions and reasons are Cohn's. The signs are this wiki's.

| Condition | Reason given | Sign of violation |
|---|---|---|
| Stop at features; do not decompose into tasks | Features, not tasks, add value (L4609) | Rows are tasks |
| Each feature spans its whole iteration | Availability comes at iteration end (L4611-L4617) | A bar shorter than its iteration |
| No resource allocation | The whole team is responsible (L4637) | Names against rows |

> Because it is the completion of features, rather than the completion of the tasks that add up to a feature, that adds value to a product, the Gantt chart is drawn showing features.
>
> — [[cohn-agile-estimating-planning]], L4609

Cohn calls the result a *feature breakdown structure* rather than a work breakdown structure (L4609).

> A feature may be done mid-way through an iteration but it is not made available to the organization until the end of the iteration so that is what the Gantt chart reflects.
>
> — [[cohn-agile-estimating-planning]], L4611-L4617

In Figure 21.1 every story has the dates of its iteration, July 1-14 or July 15-29 (L4621-L4629). The chapter summary repeats that the chart "should not be taken below the feature breakdown level" and that features are "shown as in process for the entire duration of the iteration" (L4789).

## What it cannot ask

This wiki reads the chart as unable to show progress, because every bar is the full iteration by construction. It also cannot show when within an iteration something will finish. Progress belongs to burndown charts; see [[which-chart-for-which-plan-question]].

## Which setup this applies under

This wiki reads the full-length bar as tied to Cohn's stated release point. If a project can release a feature as soon as it is done, the bar overstates its delivery date. In a setup with no iterations, there is nothing for the chart to allocate into.

## Agent executor note

The no-names condition rests on whole-team responsibility, a human team arrangement. This wiki reads the condition as still holding with an agent executing, since a name would not say who did the work. Whether a person steering should appear for review is not addressed here.

Related: [[release-plan-level-of-detail]], [[vertical-slice]], [[sequence-versus-wait]], [[activity-based-plan]].
