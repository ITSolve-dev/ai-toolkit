---
title: Release Burndown Chart
category: showing-work
summary: A line of work remaining at the start of each iteration that answers how much is left and the net rate and gives a forecast by straight edge; it cannot say why progress changed, and the forecast assumes nothing changes.
tags: [method, visualization, burndown, forecasting, retrospective-analysis, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Release Burndown Chart

A release burndown chart plots work remaining against iterations: points or ideal days on the vertical axis, iterations on the horizontal, with a value taken at the start of each iteration ([[cohn-agile-estimating-planning]] L4306-L4310). The source credits Schwaber and Beedle (2002).

## The question it answers

The chart is drawn to show:

> the two most important numbers we can use to see if a project is on track: how much work is remaining and the team’s rate of progress net of all changes to the scope of the project
>
> — [[cohn-agile-estimating-planning]], L4336

The word to keep is net. "A key to interpreting a release burndown chart is understanding that it shows the team’s net progress—that is, their progress minus any work added to the release." (L4431). This wiki reads a segment of the line as therefore not being [[velocity]].

## The forecast

The source's method: "Simply line up a straight edge between the 240 points on the vertical axis and the number of points currently remaining in the project. Where the straight edge intersects the horizontal axis is when you can expect the project to finish." (L4336)

Inputs: the starting total and the current remaining, both read from the chart.

Condition: it says when the project is likely to finish "if all factors affecting the project remain unchanged" (L4340).

What would show it wrong: the next period's point falls off the projected line.

Three limits are this wiki's reading of that condition.

- It averages over all periods since the start, so an early one-off is extrapolated. A single scope addition counts as a permanent slowing of the rate.
- A flat or rising line gives no date. The source's own numbers show it: from 240 to 260 after one iteration (L4357), the straight edge never reaches the axis. This should be reported as no forecast, not as a far date.
- It gives a point and no range. The chart shows a likely finish, and any promise needs the range treatment on [[estimates-as-ranges]].

## A burnup is not a failure

The line can rise. The source's cases are remaining work re-estimated upward, as when user interface proved harder (L4330), and work added, where a team completed its 30 points while the owner identified 40 more (L4334). The source's summary says a team's burndown "is never perfectly smooth" (L4427). The realistic example shows progress as "inconsistent" after three iterations (L4330).

## The question it cannot ask

Why the line moved. This wiki notes that a rise from added scope and a rise from revised estimates look the same, and a shallow segment can come from slow completion, offsetting re-estimates, or added work. When the question is why, use [[release-burndown-bar-chart]] or the split in [[release-progress-forces]].

The chart also says nothing about which parts of the release are behind: that is [[parking-lot-chart]].

## Trade-offs

Its virtue is that it is "easy to understand and can be quickly explained to anyone in the organization" (L4340). This wiki notes that its cost is that one line merges every force.

## Which setup this applies under

- **Iteration setup:** as above, for any release with several periods.
- **Flow setup:** the source ties the axis to iterations. This wiki's reading is that the chart still draws against calendar intervals, but the forecast then rests on a rate with no period commitment under it. See [[flow-metrics]].

## Agent executor note

This wiki notes that the chart is computed from board history and needs nobody to keep it, provided estimates exist and changes to them are retained. For a few people on a short release, a line with few points forecasts weakly; the source's example reads it after three of eight iterations (L4336). This caution is this wiki's.
