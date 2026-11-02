---
title: Release Burndown Chart
category: showing-work
summary: A line of work remaining at the start of each iteration that answers how much is left and the net rate and gives a forecast by straight edge; scope growth shows as a rise, it cannot say why progress changed or show risk retired and learning gained, and the forecast assumes nothing changes. The bar form separates scope change (the bottom) from completion and re-estimation (the top), and is dropped at the first argument over which side a change belongs on.
tags: [method, visualization, burndown, forecasting, velocity, release-planning, retrospective-analysis, cohn, scope-change]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
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

This wiki's test of the forecast, since Cohn says "A team's burndown is never perfectly smooth" (L4427) and one off-line point shows nothing: the projected finish moves by more than one period across successive readings, or the release does not finish in the projected iteration.

Three limits are this wiki's reading of that condition.

- It averages over all periods since the start, so an early one-off is extrapolated. A single scope addition counts as a permanent slowing of the rate.
- A flat or rising line gives no date. The source's own numbers show it: from 240 to 260 after one iteration (L4357), the straight edge never reaches the axis. This should be reported as no forecast, not as a far date.
- It gives a point and no range. The chart shows a likely finish, and any promise needs the range treatment on [[forecast-range-and-probability]].

The case's trendline in Chapter 23 rests on two points, and its speaker says "Probably" (L6467). The same speaker values each new point as "news I can trust about the progress we’re making" (L6463), even when it is bad news. This wiki reads an early line as deserving a range for that reason.

## A burnup is not a failure

The line can rise. The source's cases are remaining work re-estimated upward, as when user interface proved harder (L4330), and work added, where a team completed its 30 points while the owner identified 40 more (L4334). The source's summary says a team's burndown "is never perfectly smooth" (L4427). The realistic example shows progress as "inconsistent" after three iterations (L4330).

## The case: a rise drawn as a rise

Chapter 23's fictional case draws the chart by hand on a CEO's whiteboard in a meeting of about 15 minutes (L6398, L6408, L6416-L6420), and he asks to keep it: "I want to update that every two weeks." (L6484). With 132 points less 34 after two periods, the trendline puts the finish "during the eighth iteration" (L6429; Figures 23.5-23.6).

When 35 points were added, the line went "up to 133 points" as a vertical segment (L6448, Figure 23.7). A new trendline at 17 points per period then runs from that height to the new finish (L6467, Figure 23.8).

This wiki reads two qualifications from that, both to the sections above.

- The start-of-iteration values net completion and addition together (L4431). The vertical segment keeps them apart on one line, so a scope increase cannot pass for negative progress. That works only where the addition is a single dated decision that someone chose to draw this way.
- The new trendline restarts from the new height at measured velocity. A straight edge from 132 through 133 would give no date, which is the flat-line limit above, while the restart gives eight more iterations. Where a rise is a known single event, forecast from [[velocity]] and not from the slope of the whole line ([[velocity-range-forecast]]).

## The question it cannot ask

Why the line moved. This wiki notes that a rise from added scope and a rise from revised estimates look the same, and a shallow segment can come from slow completion, offsetting re-estimates, or added work. When the question is why, use *The Bar Form* (below) or the split in [[release-progress-forces]].

The chart also says nothing about which parts of the release are behind: that is the parking lot chart on [[which-chart-for-which-plan-question]].

The height also invites a misreading, and the case shows it. The CEO's first response was:

> Hmm, that doesn’t look so good. After two iterations, you’re no better off than where you started.
>
> — [[cohn-agile-estimating-planning]], L6457

The programmer's reply was that the height does not show what was gained: risky parts retired, a valuable feature discovered early, more trust in the plan.

> yes we still have as much work to do as we thought four weeks ago but now I’m more confident in the plan than I was four weeks ago.
>
> — [[cohn-agile-estimating-planning]], L6459

This wiki reads that exchange as a statement of what the chart cannot ask. Risk retired, learning and the value of the scope do not appear on it, so anyone presenting it has to say them in words. The chart also cannot tell a well-judged scope increase from an unjudged one, and [[chosen-delay-versus-slip]] carries that test.

## The sign

Remaining points rise between two periods. This wiki reads that as scope added or open estimates raised, to be checked against the board's record of each. It raises a question and gives no verdict ([[smell-is-not-a-finding]]).

## Trade-offs

Its virtue is that it is "easy to understand and can be quickly explained to anyone in the organization" (L4340). This wiki notes that its cost is that one line merges every force.

## Which setup this applies under

- **Iteration setup:** as above, for any release with several periods.
- **Flow setup:** the source ties the axis to iterations. This wiki's reading is that the chart still draws against calendar intervals, but the forecast then rests on a rate with no period commitment under it. See [[flow-metrics]].

## Agent executor note

This wiki notes that the chart is computed from board history and needs nobody to keep it, provided estimates exist and changes to them are retained. For a few people on a short release, a line with few points forecasts weakly; the source's example reads it after three of eight iterations (L4336). This caution is this wiki's.

## The Bar Form

A variation of the line chart (above) that shows "the team’s velocity and the scope changes separately" ([[cohn-agile-estimating-planning]] L4340-L4346). Each bar is the work in the release as of the start of an iteration. Bars are used in place of lines to make the regions above and below zero distinct (L4355).

### Drawing rules

> - Any time work is completed, the top is lowered.
> - When work is re-estimated, the top moves up or down.
> - When new work is added, the bottom is lowered.
> - When work is removed, the bottom is raised.
>
> — [[cohn-agile-estimating-planning]], L4379-L4385

A bottom below zero means that overall work has been added to the release (L4355).

### Worked example

From the source (L4357): a release planned at 240 points, expected velocity 30, eight iterations. The first bar runs from 0 to 240. The team completes 30 and the owner identifies 50 more, so the second bar runs from –50 to 210. The release now needs 260 points.

Three readings follow (L4359-L4367): velocity is as expected, from the tops; a great deal was added, from the bottom; and the total exceeds the start, from the height of the bar.

### The questions it answers

- Is progress against planned work on course? Read the tops.
- Is scope moving, and in which direction? Read the bottoms.
- How much is left? Read the height.

### The question it cannot ask

The top conflates completion and re-estimation: rule 1 and rule 2 both move it. The source says tops show velocity (L4359), and then concedes a drop of 20 may be 30 completed with estimates raised (L4373). This wiki's reading is that the bar separates scope from everything else, and does not separate completion from re-estimation. Where that matters, use the split in [[release-progress-forces]].

As with the line chart, nothing says whether a change was a good one. The source: "Presumably work has been added because it will lead to a more valuable release." (L4361-L4365)

### When to use which

The source's rule has two conditions.

1. **Start with the line.** "the burndown bar chart is harder to understand so I almost always start a new team with the simpler burndown line chart" (L4402).
2. **Drop the bars at the first argument.** The chart is

> only for use in organizations mature enough not to argue about whether something belongs above the line or below the line
>
> — [[cohn-agile-estimating-planning]], L4402

The sign is plain: dispute over whether a change is scope or estimate. The response in the source is to revert to the line chart.

Inputs: whether the readers need scope apart from progress, which is read from whether the question being asked is why and not only when. What would show the choice wrong: readers misread the bars, or the chart becomes a contest over attribution.

### Trade-offs

"Clearly, there is a great deal more expressive power in drawing a burndown chart in this way. The drawback to it is that the meaning of the chart is not as immediately clear." (L4369)

### Agent executor note

This wiki reads the source's caveat as social: the source says only that the chart needs teams "mature enough not to argue" (L4402) and "may cause arguments in some organizations" (L4433), and the motive, that someone gains by classifying a change one way, is this wiki's reading. When the plugin computes the chart from board history, the classification comes from what happened: a task entering the release lowers the bottom, and an estimate edit moves the top. Two cases remain that history alone does not settle, and this wiki has no source for either. A split whose pieces sum to more than the parent is read here as re-estimation, and a task replaced by a differently worded one is read as a removal and an addition, which may overstate churn. A page generated this way should state its classification so a reader can dispute it, and the source's fallback to the line chart still holds.
