---
title: A Forecast Needs a Stable Process
category: periods
summary: Past flow data predicts the future only from a stable process; arrivals far outpacing departures, or a triangle-shaped Cycle Time scatterplot, say to question the data before forecasting from it.
tags: [rule, forecasting, flow-metrics, board-health, flow-debt]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# A Forecast Needs a Stable Process

A forecast built from past flow data is only worth what that data says about the future, so the process that produced it has to be predictable before the forecast is run. Vacanti puts the order plainly: "The first step in building a reliable forecast is to put in place a predictable process such that you can have confidence in the data that you are collecting." ([[vacanti-actionable-agile-metrics]] L3758). The rule is stated for [[monte-carlo-simulation]], but his conclusion applies it to forecasting methods generally: "Even the best forecasting methods, however, are going to be only as good as the data they are based on." (L3758).

## What breaks when it is ignored

A simulation samples the past to stand in for the future. If Cycle Times are climbing, the past is not a sample of what comes next:

> Ever increasing Cycle Times mean that any selection of data from a past timeframe is a poor indication of what might happen in a future timeframe.
>
> — [[vacanti-actionable-agile-metrics]], L3696

The result still comes out looking like a forecast. Of the unstable data in Figure 11.1 Vacanti asks: "Could you throw the Cycle Time data from Figure 11.1 into a Monte Carlo Simulation? Yes. Would the resulting forecast be reasonable? Probably not." (L3698). This wiki reads that as the reason the check has to happen before the run: on this account nothing in the output itself says the input was bad.

The source names this GIGO: "A forecast put together using bad data (from an unstable system, for example) produces something that either no one will like or no one will believe" (L3758).

## The two signs

Each sign raises a question about the data; neither is a verdict. Vacanti hedges them himself, saying such a process "might not be a great candidate" and calling the second one a "smell" (L3690, L3698).

- **Arrivals far outpacing departures on a cumulative flow diagram.** This is the shape of his Figure 7.5, which shows Cycle Times constantly increasing (L3696). Read from board history. What to check: whether work is entering faster than it leaves over the window the forecast would sample. See [[mismatched-arrivals-and-departures]].
- **A triangle-shaped Cycle Time scatterplot.** This is the shape of his Figure 11.1, also "the result of an inherently unstable process" (L3698). Read from board history. What to check: whether items have been left to age while newer ones finish, which is the Flow Debt he blames. See [[triangle-on-a-scatterplot]] and [[flow-debt]].

## Discriminating criterion: balanced arrivals are not enough

The first sign clearing does not clear the second. Matching arrivals to departures, the shape of Figure 7.8, mostly removes the problem of rising Cycle Times (L3696), "However, getting to a process that produces a CFD like Figure 7.8 is not necessarily good enough" (L3698). A balanced diagram can sit alongside a triangle scatterplot, and the culprit there is Flow Debt:

> Large accumulations of Flow Debt destabilize a process and make it imminently unpredictable.
>
> — [[vacanti-actionable-agile-metrics]], L3698

A check therefore has to read both charts. This wiki treats a pass on only one as an unfinished check.

## Applying the rule

This wiki states the rule for the plugin this way, as a reading of the passages above. When a date is to be forecast from history, read both charts over the window to be sampled. If either sign appears, say what it puts in doubt and do not present the forecast as sound until it has been checked. The later fact that would show the data was unsuitable is realised Cycle Times running past the forecast percentile.

## Trade-off

The source accepts that a project may have no suitable data yet, but only as a first step towards gathering it (L3688). This wiki reads the cost as follows: stabilising first delays a forecast someone may be asking for now. Producing one anyway from unstable data buys a number the source expects nobody to believe. A stated range with its doubt named may serve better than either, which is our suggestion and not the source's.

## Agent executor note

The mechanism is statistical and does not depend on a human executor, so it survives an agent executing and a person steering. The transfer here is ours: the same logic suggests that history from before a change in who or what executes the work is a poor sample of the process after it, since the past window no longer describes the process being forecast. The chapter does not discuss this case.
