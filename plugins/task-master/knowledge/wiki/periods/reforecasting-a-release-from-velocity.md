---
title: Reforecasting a Release from Velocity
category: periods
summary: Divide remaining points by measured velocity, round up to whole periods, add elapsed periods, and repeat after every period and every scope change; rounding up leaves only the margin the fraction happens to give.
tags: [method, velocity, release-planning, planning-a-date, forecast, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-02
updated: 2026-11-02
---

# Reforecasting a Release from Velocity

Reforecasting recomputes a release date from what has been measured, where [[deriving-duration-from-velocity]] produced the first figure. The fictional case study in Chapter 23 of [[cohn-agile-estimating-planning]] (L4961) runs the same arithmetic four times across its first two periods, each time after a period closes or the scope moves. How often to look again is on [[updating-the-release-plan]]. This page holds the computation.

## Procedure

The steps are this wiki's statement of what the case does.

1. Remaining points = points in the release − finished points + points added.
2. Velocity = finished points per period, measured, using [[all-or-nothing-counting]]. The case averages the periods so far (L6364).
3. Remaining ÷ velocity, rounded up to whole periods.
4. Add elapsed periods and convert to a date.

## The case's runs

Conditions: two-week iterations, nine named characters of whom seven work on the project, and a release of 132 points. The figures are a narrative's, and they illustrate the mechanism without measuring anything.

| When | Remaining | Velocity | Ratio | Forecast | Lines |
|---|---|---|---|---|---|
| After period 1 | 116 | 16 | 7.25 | 8 more, 18 weeks total | L6267 |
| After period 2, old scope | 98 | 17 | 5.76 | During the eighth iteration, 16 weeks total | L6429 |
| After adding 35 points | 133 | 17 | 7.8 | 8 more, 20 weeks total | L6364-L6366, L6467 |
| Without 22 droppable points | 111 | 17 | 6.5 | 7 more, 18 weeks total | L6388 |

This wiki derives the 98 and 5.76 in the second row from the source's totals, because the source states only the result. The release was finished at 22 weeks and could have shipped at 20 (L6498-L6500), so the third row is the one that held.

## Rounding up is not a buffer

Rounding gives only the margin the fraction happens to leave. At 7.25 a character says "To be safe, let’s call that 8 more two-week iterations." (L6267). At 7.8 the same rounding is "cutting it awfully close" (L6368).

> However, if anything goes wrong—if a story is bigger than we think or if we slow down or if someone gets sick—we could take longer than eight more iterations.
>
> — [[cohn-agile-estimating-planning]], L6368

This wiki reads that as the reason a tight forecast needs either a range ([[velocity-range-forecast]]) or a named reserve of scope ([[droppable-stories-as-a-schedule-buffer]]). The case uses one averaged figure, which is simpler than the three values the book asks for elsewhere. Two periods is also a thin sample, and the case forecasts from it anyway while saying that a firmer figure comes later (L6249, L6498).

## What later fact would show it wrong

This wiki reads two later facts as showing a run wrong: velocity in later periods diverges from the figure used, or stories prove larger than estimated. Each run is therefore provisional, and the method's value is that the next run absorbs the news. Holding the first forecast while measured velocity says otherwise is the failure.

The sign is on the board: the release's stated date cannot be reproduced from the current remaining total, the measured velocity and the periods elapsed. This sign is this wiki's and raises a question ([[smell-is-not-a-finding]]).

## Which setup this applies under

The resolution here is this wiki's. The method presumes periods, since velocity is points per period. Without them the division needs another rate, and the source does not supply one ([[velocity]]).

## Agent executor note

This wiki reads the arithmetic as independent of who executes. Velocity must come from periods run under the same arrangement of people and agents, since a figure from another arrangement measures something else. This wiki reads the risk that "someone gets sick" as human, and a story proving bigger than thought as surviving unchanged.

The forecast is shown with [[release-burndown-chart]]. Comparing it with the outcome is [[chosen-delay-versus-slip]].
