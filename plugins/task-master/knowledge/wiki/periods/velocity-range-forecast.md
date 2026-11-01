---
title: Velocity Range Forecast
category: periods
summary: Forecast from three velocity values (most recent, mean of up to the last eight, mean of the slowest three) to get a range of work by a date or of iterations for a scope, never one number.
tags: [method, estimation, velocity, forecast, iterations]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Velocity Range Forecast

A velocity range forecast answers how much will fit by a date, or when a scope will finish, from a team's own recent velocity. It uses three values instead of one, so the answer is a range. Cohn presents it as the way to keep a forecast from claiming more than velocity can support. It is the procedure for the case where observed history exists; [[velocity-estimate-range]] covers ranges for every other basis, and [[deriving-duration-from-velocity]] the single-value arithmetic.

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
- **Short history.** This wiki notes that with three or fewer iterations the slowest-three mean equals or nearly equals the overall mean. The range then looks narrow because data is missing, not because the forecast is precise.
- **Sign of misuse:** a forecast quoting one velocity, usually the latest or best. See [[stating-plan-uncertainty]].

## Conditions

The figure of eight is a practitioner's habit, not a measured cutoff. Cohn's reasons are that "Many teams stay together that long" and that older data "starts to feel like ancient history" (L4658). The sample team has four people on two-week iterations (L4688, L4711-L4717).

This wiki reads the arithmetic as surviving an agent executing and a person steering, because it uses only points finished per period. The reason for the window does not transfer as written. Staleness there would come from a change in who steers, in how the agent works, or in how tasks are sized, and no source here tests that. A project with no iterations has no velocity; see [[flow-metrics]].

See also [[velocity-trend-is-not-a-forecast]], [[filling-a-period]], [[iteration-summary-plan-versus-fact]].
