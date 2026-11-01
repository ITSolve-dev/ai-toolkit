---
title: Fitting Stories into a Release
category: periods
summary: The procedure for filling a release; iterations times velocity gives capacity, stories are counted off an ordered list, and the result is tested against the release's conditions, worked through the SwimStats numbers.
tags: [method, iterations, release, estimation]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Fitting Stories into a Release

The core of release planning is one multiplication. Cohn calls it trivial at its simplest level: multiply expected velocity by the number of planned iterations, then select stories whose estimates fill that total ([[cohn-agile-estimating-planning]] L2947-L2951). The number of iterations alone does not give a duration: "we must also estimate the team’s rate of progress through that work" (L2745).

## Inputs and where each is read from

| Input | Read from | Source note |
|---|---|---|
| Conditions of satisfaction | The owner of the goal; see [[conditions-of-satisfaction]] | Comes first (L2802) |
| Story estimates | Estimates on every story that may be selected; see [[estimate-only-what-may-be-selected]] | L2810-L2812 |
| Iteration length | A chosen constant; "from one to four weeks" is the common range; see [[iteration-length]] | L2816 |
| Velocity | History first | "If the team has experience working together, your best bet is often to use the velocity the team exhibited most recently." (L2820) |
| Order | A prioritized list; see [[value-order-versus-technical-necessity]] | L2824 |

Figure 13.1 fixes only the ends: conditions first, selection last. The steps in between may be done in any sequence, and the whole is iterated until the conditions can best be met (L2796).

The velocity input has a stated limit: "Naturally, if the technology or business domain changed dramatically, it may not be appropriate to use a team’s past velocity." (L2820). See [[velocity]].

## The steps

1. Fix the driver, on [[date-driven-vs-feature-driven]].
2. **Feature-driven:** sum the estimates of the needed features and divide by velocity to get the number of iterations (L2832). This is [[deriving-duration-from-velocity]].
3. **Date-driven:** read the number of iterations from the calendar, multiply by velocity, and count that many points down the ordered list (L2834). This is the cut line of [[fixed-date-variable-scope]].
4. Check the result against the conditions. "In both cases, once a team has an initial answer, it is assessed against the organization’s goals for the project" (L2777). If it misses, change a condition and repeat (L2971).
5. If stories are placed into specific iterations, sum each iteration against velocity: the point of the estimate on every card is to verify "that each iteration holds the right amount of work" (L2842-L2846). How much to place is on [[release-plan-level-of-detail]].

## Worked numbers

Generic case: six months at two-week iterations is thirteen iterations; at twenty points each the release holds 13 × 20 = 260 (L2779).

SwimStats, a date-driven release with three people and a story list totalling 68 points (L2891, L2915-L2929):

- Three months gives six two-week iterations "followed by an extra week in case it’s needed" (L2937).
- Forecast velocity of 8 gives 6 × 8 = 48 points (L2907, L2937).
- The owner picks the first eight stories: 46 points (L2939).
- Developers show a 3-point story from the bottom of the list is necessary, making 49 (L2941).
- The owner drops an 8-point story: 41 points (L2943).
- The owner leaves the remaining 7 points unfilled rather than add a 3-point story, because "If the team gets even one point ahead of schedule, she’d prefer to add back the eight-point story she dropped." (L2943). Adding it back would make 49, which is one over the 48.

**Source errors in this example.** The text says "an estimated velocity of seven points per iteration" while computing with eight (L2937); the eight at L2907 is the consistent figure. The team is one programmer, one database administrator and one tester at L2891, and two programmers and a tester at L2907.

## Is the capacity a hard line?

The source presents both answers. "The 48 points is a fairly rough guess and an extra week is planned after the sixth iteration. Some teams may allow for 49 points under these circumstances." (L2941). The SwimStats team did not allow it and required a drop (L2943).

This wiki resolves that per setting. On a date-driven release with a real external date, treat capacity as a line and hold the buffer as buffer: spending the extra week on planned scope removes what protects the date, and leaves nothing to absorb variability ([[utilization-versus-slack]]). On a feature-driven release the line has less force, since the output is a duration and one point changes little. This resolution is the wiki's reading, built on the two positions the source reports.

## What later fact shows the plan wrong

Measured velocity diverging from the assumed figure over iterations, or iteration planning surfacing large surprises; both are the triggers on [[updating-the-release-plan]].

## Trade-off

The multiplication is only as good as a forecast velocity, and this wiki reads that figure as the softest input. The source calls its result "a fairly rough guess" (L2941). Precision in the sum of estimates does not make the plan more exact than that, and a single total carries the risks on [[single-date-plan]].

## Agent executor note

This wiki reads the arithmetic as carrying over, but only if velocity is measured for the actual setup of people and agent. The source's forecast rests on a human team's stable rate, and nothing here shows that rate is stable when an agent executes. Until a history exists, a capacity number from this method is an assumption to be stated, not a measurement.
