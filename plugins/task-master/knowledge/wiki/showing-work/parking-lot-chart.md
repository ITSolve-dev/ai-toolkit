---
title: Parking Lot Chart
category: showing-work
summary: One box per theme in a release, each showing its story count, total estimate and percent complete, so a whole release fits on a page. It shows where progress sits across themes, and not which tasks are done or the trend over time.
tags: [method, visualization, themes, retrospective-analysis, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Parking Lot Chart

A parking lot chart, from Jeff DeLuca (2002), summarizes a release by theme. Each [[theme]], a grouping of stories, gets a large box annotated with its name, the number of stories, their total estimate, and the percentage of those points complete ([[cohn-agile-estimating-planning]] L4410).

This is unrelated to the [[parking-lot]] on a board, which is an area for items waiting on an outside party. The two share only a name.

## Example

From the source's figure (L4415-L4419): Swimmer Demographics has 8 stories, 36 points, 50%; Reporting has 12 stories, 41 points, 100%; Security has 4 stories, 18 points, 33%. The 50% means 18 of the 36 points are done.

Boxes may also be coloured to say whether a theme is "done, on schedule, needs attention, or significantly behind schedule" (L4419).

## The question it answers

Which parts of a release are done and which are behind, at a glance. The source values it for "compressing a great deal of information into a small space" and says all of a release's themes can often fit on one page (L4421). The summary describes it as "a high-level view of a team’s progress toward implementing the various themes" (L4435).

## The question it cannot ask

- Which tasks are done: "We cannot tell how many of the specific user stories are done." (L4419)
- Whether the release will finish on time, or how the picture is changing. A box is a snapshot with no trend, and a percentage against a moved total looks like progress lost. [[release-burndown-chart]] answers these. This point is this wiki's.
- Why a theme is behind: [[release-progress-forces]] answers that.

## Interaction with counting

The percentage is of points, so it should follow [[all-or-nothing-counting]] at the level of tasks: a theme's percent is the sum of whole estimates of complete tasks over the theme's total. This wiki reads this as a condition for the chart to mean anything. A percentage typed in by hand is partial credit at theme level. The source does not say so explicitly, and its 50% example is consistent with it.

## Failure mode

A colour with no stated test. The labels "needs attention" and "significantly behind schedule" are named in the source without a threshold, and a judgement presented as a colour reads as a measurement. Sign: boxes with the same percentage and different colours, and no stated reason. This failure mode is this wiki's.

## Applicability

The chart needs tasks grouped by theme, and that grouping is read from the board. With a few people on a small release there may be too few themes for the chart to add anything beyond a list. This caution is this wiki's. It has no dependency on who executes the work.
