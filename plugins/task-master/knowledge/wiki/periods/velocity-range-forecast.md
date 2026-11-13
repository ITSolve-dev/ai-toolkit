---
title: Velocity Range Forecast
category: periods
summary: Duration is derived, not estimated: remaining points divided by velocity, rounded up (or down only with a cut), mapped to a calendar, and recomputed after every period and scope change. From four closed iterations it is stated as a range from three values (most recent, mean of up to the last eight, mean of the slowest three), the slowest-three figure being what may be promised; a velocity trend is never projected, and rounding is not a buffer.
tags: [method, estimation, velocity, forecast, iterations, release-planning, planning-a-date, cohn, rule, retrospective]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Velocity Range Forecast

A velocity range forecast answers how much will fit by a date, or when a scope will finish, from a team's own recent velocity. It uses three values instead of one, so the answer is a range. Cohn presents it as the way to keep a forecast from claiming more than velocity can support. This wiki uses it once four or more iterations have closed. With three or fewer, and for every basis other than the project's own history, the range comes from [[choosing-velocity-estimate-approach]], whose table by count of closed iterations states the same boundary. The boundary is Cohn's: his Table 16.1 treats four or more iterations as one step, the mean times 0.90 and 1.10 (L3668), and he does not extend the cone past three or four (L3674). Using the three values from that point instead of the table's row is this wiki's choice, argued on [[choosing-velocity-estimate-approach]]. The single-value arithmetic is in *Deriving Duration from Velocity* (below).

## Why one velocity is not enough

The simple calculation divides remaining points by velocity and rounds up: 100 points at velocity ten is ten iterations ([[cohn-agile-estimating-planning]] L4641). Cohn's objection:

> measures of velocity are imprecise and we need to expect velocity to fluctuate
>
> — [[cohn-agile-estimating-planning]], L4643

Cohn's illustration is that a team averaging ten could run at seven or thirteen for the next few iterations, which turns ten iterations into "as few as eight or as many as fifteen" (L4643-L4647).

## The procedure

1. Take up to the last eight closed iterations. "If you don’t have eight iterations, use what you have." (L4658)
2. Compute three values (L4660-L4664): the velocity of the most recent iteration, the mean velocity, and the mean of the three slowest iterations. The chapter summary takes the slowest three from the same eight (L4791-L4795).
3. Apply each value to whichever side is fixed.
   - **Date fixed:** multiply by the iterations remaining to get points likely done.
   - **Scope fixed:** divide the remaining points by each velocity and round up to get iterations left. Cohn's text only states the rounding for the single-value case (L4641).
4. Report all three outcomes as a range, not their average.

Cohn describes the three as "a good picture of what just happened, a “long term” average, and a worst-case of what could happen" (L4666).

## Worked examples

Cohn's example (Table 21.1, L4672-L4678): velocities over eight iterations with a most recent of 19, a mean of 17, and a slowest-three mean of 14, with five iterations left before the release.

| Value | Velocity | Iterations | Points |
|---|---|---|---|
| Worst three | 14 | 5 | 70 |
| Last eight | 17 | 5 | 85 |
| Most recent | 19 | 5 | 95 |

The range is not read evenly. Cohn says a product owner "should feel comfortable that at least seventy additional story points will be added" but "probably should not take out advertising space on a blimp about anything beyond 85 more story points" (L4684). This wiki reads that as: the slowest-three figure is what may be promised, the mean is the ceiling for public statements, and the most-recent figure is possible but not promised.

The next example is this wiki's arithmetic, not Cohn's answer. His discussion question has 150 points remaining and velocities 10, 12, 13, 5, 14, 7, 6, 12, 16, 14 (L4801). The last eight give a mean of 10.9, a slowest-three mean of 6 (from 5, 6, 7), and a most recent of 14. That is 11, 14 and 25 iterations. This wiki reads the width of that range as the finding: it reports an unstable velocity that a single answer of 14 iterations would hide.

## Inputs and what would show the choice wrong

- **Points finished per closed iteration:** read from board history.
- **Remaining points or remaining iterations:** read from the current plan.
- **What shows it wrong:** this test is this wiki's, not Cohn's. Delivered work below the slowest-three figure, or repeatedly near that floor, means the window no longer describes current conditions, and the question is what changed.

## Limits and failure modes

- **Worst case is not the minimum.** This wiki notes that Cohn's "worst-case" (L4666) is a mean. In his sample the slowest-three mean is 14 while the slowest single iteration was 12 (L4654), so one iteration can fall below it.
- **Short history.** This wiki notes that with three or fewer iterations the slowest-three mean equals or nearly equals the overall mean. The range then looks narrow because data is missing, not because the forecast is precise. That is why this wiki uses the method only from four closed iterations, and the observed range below that ([[choosing-velocity-estimate-approach]]).
- **Sign of misuse:** a forecast quoting one velocity, usually the latest or best. See [[forecast-range-and-probability]].

## Conditions

The figure of eight is a practitioner's habit, not a measured cutoff. Cohn's reasons are that "Many teams stay together that long" and that older data "starts to feel like ancient history" (L4658). The sample team has four people on two-week iterations (L4688, L4711-L4717).

This wiki reads the arithmetic as surviving an agent executing and a person steering, because it uses only points finished per period. The reason for the window does not transfer as written. Staleness there would come from a change in who steers, in how the agent works, or in how tasks are sized, and no source here tests that. A project with no iterations has no velocity; see [[flow-metrics]].

See also [[filling-a-period]], [[iteration-summary-plan-versus-fact]].

## Deriving Duration from Velocity

Duration is computed, not estimated: total size divided by velocity gives a number of iterations, and iteration length turns that into a calendar span. Cohn's summary states it directly:

> The duration of a project is not estimated as much as it is derived by taking the total number of story points and dividing it by the velocity of the team.
>
> — [[cohn-agile-estimating-planning]], L1056

This is the mechanical half of [[size-versus-duration]].

### Procedure

The procedure is Cohn's (L1021); the board-reading column is this wiki's mapping.

| Step | Action | Input read from |
|---|---|---|
| 1 | Sum the point estimates of all desired features | Estimates on the tasks in scope |
| 2 | Divide total size by [[velocity]] to get iterations | Past velocity from board history, or an estimate if none exists |
| 3 | Round: up, or remove enough scope to land on the lower whole number | The fractional result |
| 4 | Multiply by iteration length and count forward on a calendar | Iteration length, start date |

### Worked example

Cohn's example, with constructed figures (L1021): 100 points at a velocity of 11 per two-week iteration gives 100 ⁄ 11 = 9.1 iterations. He offers two options:

> We can either round that up to 10 iterations or find one point to remove so that it becomes 9 iterations.
>
> — [[cohn-agile-estimating-planning]], L1021

Cohn takes the conservative option, 10 iterations, which gives twenty weeks, and counts twenty weeks forward on the calendar (L1021).

### Limits

Cohn flags the method as a first approximation: "This very simplistic explanation of release planning works for now." (L1023). He says it is extended in Part IV, and that the example was simple because it used past velocity, whereas velocity must sometimes be estimated (L1023-L1029).

This wiki reads three limits from the chapter as written. The output is a single date with no range, which is what [[forecast-range-and-probability]] warns about. It assumes the total is complete, so unestimated items understate it, which is why [[estimating-underspecified-work]] matters here. It assumes the rate holds for the whole span. A derived date is also still an estimate until someone decides to hold to it, per [[estimate-versus-commitment]].

### Failure modes

These signs are this wiki's derivation. Each raises a question to check.

- **Rounding down with no cut.** The plan shows the lower number of iterations while the scope still divides to a fraction above it. In the example, 9 iterations with 100 points still in scope. Cohn allows 9 only with a point removed.
- **A date with no division behind it.** The date cannot be reproduced from the size total, the rate and the iteration length.
- **A stale rate.** The date was derived from a planned velocity and not recomputed after observed velocity differed.

### What would show the result wrong

This wiki reads two later facts as showing it: observed velocity over the first iterations differing from the rate used, or the total size changing. Either one calls for recomputing the date, not for re-estimating the work by default; see [[velocity-self-correction]] and [[re-estimate-when-relative-size-changes]]. The recomputation is on *Reforecasting a Release from Velocity* (below).

### Which setup this applies under

The resolution here is this wiki's. The method presumes iterations. A milestone without fixed periods needs a rate per unit of calendar time in their place, which this chapter does not address; [[velocity]] states what that rate can be under each setup. Whether a unit is ended by a date or by a content set is on [[planning-horizons]].

### Agent executor note

The transfer here is this wiki's, not Cohn's. The division holds for any rate. Its value depends on whether the rate is stable in the given setup, which is the open question recorded on [[velocity]].

## Reforecasting a Release from Velocity

Reforecasting recomputes a release date from what has been measured, where *Deriving Duration from Velocity* (above) produced the first figure. The fictional case study in Chapter 23 of [[cohn-agile-estimating-planning]] (L4961) runs the same arithmetic four times across its first two periods, each time after a period closes or the scope moves. How often to look again is on [[replanning-on-new-knowledge]]. This section holds the computation.

### Procedure

The steps are this wiki's statement of what the case does.

1. Remaining points = points in the release − finished points + points added.
2. Velocity = finished points per period, measured, using [[all-or-nothing-counting]]. The case averages the periods so far (L6364).
3. Remaining ÷ velocity, rounded up to whole periods.
4. Add elapsed periods and convert to a date.
5. State the result as a range, from the three velocity values of the three-value forecast at the top of this page, with its basis. The single figure from steps 3 and 4 is a gut check ([[forecast-range-and-probability]]); the case stops at it, and this step is this wiki's.

### The case's runs

Conditions: two-week iterations, nine named characters of whom seven work on the project, and a release of 132 points. The figures are a narrative's, and they illustrate the mechanism without measuring anything.

| When | Remaining | Velocity | Ratio | Forecast | Lines |
|---|---|---|---|---|---|
| After period 1 | 116 | 16 | 7.25 | 8 more, 18 weeks total | L6267 |
| After period 2, old scope | 98 | 17 | 5.76 | During the eighth iteration, 16 weeks total | L6429 |
| After adding 35 points | 133 | 17 | 7.8 | 8 more, 20 weeks total | L6364-L6366, L6467 |
| Without 22 droppable points | 111 | 17 | 6.5 | 7 more, 18 weeks total | L6388 |

This wiki derives the 98 and 5.76 in the second row from the source's totals, because the source states only the result. The release was finished at 22 weeks and could have shipped at 20 (L6498-L6500), so the third row is the one that held.

### Rounding up is not a buffer

Rounding gives only the margin the fraction happens to leave. At 7.25 a character says "To be safe, let’s call that 8 more two-week iterations." (L6267). At 7.8 the same rounding is "cutting it awfully close" (L6368).

> However, if anything goes wrong—if a story is bigger than we think or if we slow down or if someone gets sick—we could take longer than eight more iterations.
>
> — [[cohn-agile-estimating-planning]], L6368

This wiki reads that as the reason a tight forecast needs either a range (the three-value forecast at the top of this page) or a named reserve of scope ([[choosing-a-buffer]]). The case uses one averaged figure, which is simpler than the three values the book asks for elsewhere. Two periods is also a thin sample, and the case forecasts from it anyway while saying that a firmer figure comes later (L6249, L6498).

### What later fact would show it wrong

This wiki reads two later facts as showing a run wrong: velocity in later periods diverges from the figure used, or stories prove larger than estimated. Each run is therefore provisional, and the method's value is that the next run absorbs the news. Holding the first forecast while measured velocity says otherwise is the failure.

The sign is on the board: the release's stated date cannot be reproduced from the current remaining total, the measured velocity and the periods elapsed. This sign is this wiki's and raises a question ([[smell-is-not-a-finding]]).

### Which setup this applies under

The resolution here is this wiki's. The method presumes periods, since velocity is points per period. Without them the division needs another rate, and the source does not supply one ([[velocity]]).

### Agent executor note

This wiki reads the arithmetic as independent of who executes. Velocity must come from periods run under the same arrangement of people and agents, since a figure from another arrangement measures something else. This wiki reads the risk that "someone gets sick" as human, and a story proving bigger than thought as surviving unchanged.

The forecast is shown with [[release-burndown-chart]]. Comparing it with the outcome is [[chosen-delay-versus-slip]].

## A Velocity Trend Is Not a Forecast

A run of rising or falling velocities tempts a planner to extend the line. Cohn refuses in both directions, for different reasons.

### The rule

> many projects have too few iterations for velocity trends to become either apparent or relevant
>
> — [[cohn-agile-estimating-planning]], L4682

- **Upward:** "If I notice what appears to be a trend toward an increasing velocity I am pleased but don’t act on it." Cohn would "never draw a trend line" through his chart and predict a velocity of 20 for the next iteration (L4682).
- **Downward:** "I would figure out and remove the cause of the decline rather than plan on velocity continuing to drop" (L4682).

This wiki reads the asymmetry as the point of the rule: a rise changes nothing in the plan, while a fall changes what is done next. The forecast itself stays in the three values of the three-value forecast at the top of this page.

### Reasoning

The stated basis is sample size: a project offers too few points for a slope to mean anything. Planning on a decline has a further cost, which this wiki adds: it accepts the fall as a fact about the future, so nobody asks what caused it.

### Signs of violation

These signs are this wiki's reading of the rule, and each raises a question rather than a verdict; see [[smell-is-not-a-finding]].

- A forecast uses a velocity above any value in the window, or a figure labelled as projected.
- A chart of velocity carries a fitted trend line.
- A plan is cut because velocity is falling, and no cause is recorded.

### Trade-off

If a decline is real and its cause cannot be removed, the eight-iteration mean keeps older, faster iterations for a while and overstates what will come. This wiki notes that the slowest-three figure partly covers this, and that the source does not address it.

### Agent executor note

Cohn's mechanism is the sample size, not human pace, so this wiki reads the rule as surviving an agent executing and a person steering. A step change from a new way of working is a different case from a trend, and this source does not treat it.
