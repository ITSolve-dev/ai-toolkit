---
title: Straight-Line Projection of a Release Date
category: periods
summary: Extending a throughput trend line to the backlog line yields a date with no probability, built on an average and on a shape that is usually an S-curve; tolerable as a gut check, and under iterations only in range form.
tags: [failure-mode, estimation, forecasting, burn-up, throughput, s-curve]
sources: [vacanti-actionable-agile-metrics, cohn-agile-estimating-planning]
created: 2026-11-02
updated: 2026-11-02
---

# Straight-Line Projection of a Release Date

A **straight-line projection** extends a trend line from the throughput line of a burn-up chart until it meets the backlog line, then reads the date below the intersection as the release date. Vacanti's example of the reasoning: "If a backlog has 100 items in it and the team is averaging 10 items per week" ([[vacanti-actionable-agile-metrics]] L3592), the trend line gives the date. He does not recommend it for a completion date, "because both approaches are based on averages and neither give a probability of success" (L3634, the other approach being [[littles-law]]).

## What breaks

1. **It rests on an average**, with every problem in [[forecast-from-an-average]] (L3594).
2. **Both lines move.** Vacanti notes "variability in both the Backlog and Average Throughput" (L3596), and that a single projected view "could cause managers to either panic or be overly confident depending on which way the variability pendulum swings on any given day" (L3596).
3. **There is no date range**, so it fails [[forecast-range-and-probability]] (L3598).
4. **Delivery is often not a line.** Vacanti observes that "any time you start a project with zero WIP and end with zero WIP, the resulting pattern of the Throughput line on the CFD mimics an “S-curve”" (L3606), and that "Using a straight line to approximate an S-curve is problematic at best and dangerous at worst." (L3606). See [[reading-a-cfd]].

## The patch that does not repair it

Advocates draw optimistic and pessimistic lines for backlog and throughput, which gives several intersections and hence a range. Vacanti grants this is better but asks how the lines were determined, and then: "But most importantly, what is the probability of hitting this range?" (L3604). This wiki reads that as a discriminating test for any cone-style chart: a range drawn by judgement meets half the rule, and the missing half is the one that makes it checkable.

## Sign

A release or project date read from the intersection of a trend line and a backlog line, with or without optimistic and pessimistic variants, and with no stated probability. The question to check is how the date will be used, as below.

## Decision: when it is tolerable

- **Gut check.** Vacanti allows it for "a quick gut check on project status" (L3608), but adds "any insight you may gain is certainly not actionable" (L3608), since acting on it "would probably be akin to tampering" (L3608).
- **A stabilised process.** Vacanti concedes the method degrades less under good process discipline: "If you truly can keep continuous WIP, minimally violate the assumptions of Little’s Law, not introduce CoS, then this type of approach might be good enough." (L3610-L3616). His stance there is permissive: "If it is and it works for you, then, great, keep doing it." (L3616)
- **Anything else.** A commitment should come from a method that yields a probability: [[service-level-expectation]] for one item, [[throughput-monte-carlo]] for many. A burn-up can be kept and improved with [[burn-up-with-percentile-lines]].

The inputs to this choice are read from board history: whether WIP stayed continuous or the project began and ended at zero, and whether classes of service were used. This wiki's reading of what would show the choice wrong is a projected date that keeps shifting from one reading to the next, as the second problem above predicts.

## Which holds under which setup

Cohn reads a finish date off a straight edge laid along a release burndown ([[release-burndown-chart]]). This wiki reads that as the same projection from the other direction. The resolution is this wiki's and follows the one on [[littles-law-does-not-forecast]]. A single date read off any straight edge is a gut check under every setup. Under an iteration setup the division stays acceptable as a forecast only as a range with its basis ([[velocity-range-forecast]], [[stating-plan-uncertainty]]). Under a flow setup, percentiles replace it.

## Trade-off

The method is cheap and is easily explained to anyone reading the chart. Vacanti dismisses the heavier alternative of fitting S-curves, because those methods also come "with no range and probabilities attached" (L3606) and the effort is better spent on modern forecasting methods (L3606).

## See also

[[forecast-from-an-average]], [[forecast-range-and-probability]], [[littles-law-does-not-forecast]], [[throughput-monte-carlo]], [[velocity-trend-is-not-a-forecast]]
