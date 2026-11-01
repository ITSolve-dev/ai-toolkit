---
title: Release Burndown Bar Chart
category: showing-work
summary: A burndown drawn as bars whose top tracks completed and re-estimated work, and whose bottom tracks scope added or removed, so the two can be seen apart. More expressive, harder to read, and abandoned at the first argument over which side a change belongs on.
tags: [method, visualization, burndown, scope-change, retrospective-analysis, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Release Burndown Bar Chart

A variation of the [[release-burndown-chart]] that shows "the team’s velocity and the scope changes separately" ([[cohn-agile-estimating-planning]] L4340-L4346). Each bar is the work in the release as of the start of an iteration. Bars are used in place of lines to make the regions above and below zero distinct (L4355).

## Drawing rules

> - Any time work is completed, the top is lowered.
> - When work is re-estimated, the top moves up or down.
> - When new work is added, the bottom is lowered.
> - When work is removed, the bottom is raised.
>
> — [[cohn-agile-estimating-planning]], L4379-L4385

A bottom below zero means that overall work has been added to the release (L4355).

## Worked example

From the source (L4357): a release planned at 240 points, expected velocity 30, eight iterations. The first bar runs from 0 to 240. The team completes 30 and the owner identifies 50 more, so the second bar runs from –50 to 210. The release now needs 260 points.

Three readings follow (L4359-L4367): velocity is as expected, from the tops; a great deal was added, from the bottom; and the total exceeds the start, from the height of the bar.

## The questions it answers

- Is progress against planned work on course? Read the tops.
- Is scope moving, and in which direction? Read the bottoms.
- How much is left? Read the height.

## The question it cannot ask

The top conflates completion and re-estimation: rule 1 and rule 2 both move it. The source says tops show velocity (L4359), and then concedes a drop of 20 may be 30 completed with estimates raised (L4373). This wiki's reading is that the bar separates scope from everything else, and does not separate completion from re-estimation. Where that matters, use the split in [[release-progress-forces]].

As with the line chart, nothing says whether a change was a good one. The source: "Presumably work has been added because it will lead to a more valuable release." (L4361-L4365)

## When to use which

The source's rule has two conditions.

1. **Start with the line.** "the burndown bar chart is harder to understand so I almost always start a new team with the simpler burndown line chart" (L4402).
2. **Drop the bars at the first argument.** The chart is

> only for use in organizations mature enough not to argue about whether something belongs above the line or below the line
>
> — [[cohn-agile-estimating-planning]], L4402

The sign is plain: dispute over whether a change is scope or estimate. The response in the source is to revert to the line chart.

Inputs: whether the readers need scope apart from progress, which is read from whether the question being asked is why and not only when. What would show the choice wrong: readers misread the bars, or the chart becomes a contest over attribution.

## Trade-offs

"Clearly, there is a great deal more expressive power in drawing a burndown chart in this way. The drawback to it is that the meaning of the chart is not as immediately clear." (L4369)

## Agent executor note

The source's argument is social: someone gains by classifying a change one way. When the plugin computes the chart from board history, the classification comes from what happened: a task entering the release lowers the bottom, and an estimate edit moves the top. Two cases remain that history alone does not settle, and this wiki has no source for either. A split whose pieces sum to more than the parent is read here as re-estimation, and a task replaced by a differently worded one is read as a removal and an addition, which may overstate churn. A page generated this way should state its classification so a reader can dispute it, and the source's fallback to the line chart still holds.
