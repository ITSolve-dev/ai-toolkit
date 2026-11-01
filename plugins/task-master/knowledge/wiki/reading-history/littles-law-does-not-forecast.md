---
title: Little's Law Does Not Forecast
category: reading-history
summary: The law is exact only looking back over a completed period and is a relationship of averages; use it for measurement and rough gut-checks, and never as the basis of a commitment.
tags: [rule, forecasting, retrospective, flow-metrics, predictability]
sources: [vacanti-actionable-agile-metrics, cohn-agile-estimating-planning]
created: 2026-11-02
updated: 2026-11-02
---

# Little's Law Does Not Forecast

[[littles-law]] describes a period that has already finished. It does not predict a coming one. Vacanti: "The first thing that you need to know about Little’s Law is that it is concerned with looking backward over a time period that has completed" ([[vacanti-actionable-agile-metrics]] L1078). Little's own phrasing, quoted by Vacanti, is that "we are in the measurement business, not the forecasting business" (L1078-L1084).

## What it cannot do

Vacanti's worked example: a team has average WIP of 20 items, average Cycle Time of 5 days and average Throughput of 4 items a day. Raising WIP to 40 and holding Cycle Time at 5 does not yield 8 items a day, "even if you add staff to the keep the WIP to staff ratio the same" (L1086). The law says only that a change in WIP results in a change to Cycle Time, Throughput or both, and that the result will still obey the relation. It does not say what the change will be (L1086).

His forecasting chapter gives two independent reasons (L1096 defers them to it):

1. **Assumptions cannot be foreseen.** It is "impossible to predict which of the Law’s assumptions will be violated in the future and how many times they will be violated", and "each violation of an assumption invalidates the exactness of the law" (L3550).
2. **It is a relationship of averages.** "You never want to make a forecast based on an average." (L3552). The law does not care about the underlying probability distributions, so it gives no probability, and a statement without one is not a forecast (L3560). See [[forecast-from-an-average]] and [[forecast-range-and-probability]].

## The rule

Vacanti draws the line by what the number is used for, so the input is the use, read from the plan or the question asked.

- **Allowed:** measuring a completed period, and quick estimates about the future, as a "quick gut-check to decide if something like a project is worth any further exploration" (L1098). A "gut check validation of a forecast for a _qualitative_ determination is perfectly acceptable" (L3562).
- **Not allowed:** the basis of a commitment. "I would not, however, make any commitments, staff hiring or firing decisions, or project cost calculations based on this type of calculation alone" (L1098). Chapter 14 repeats it: "you would not want to make any staffing, cost, or project commitments based on these back-of-the-envelope calculation type calculations" (L3562).

## Observable sign

This wiki's reading of where the violation shows: a date, plan or promise whose only derivation is open items divided by average Throughput, or a plan that expects Throughput to scale with added WIP. The question to check is whether the number was used to sanity-check a forecast or to produce one. The same applies to a plugin's own output. A figure computed this way must be labelled a rough check and must not be offered as a delivery date.

## What to use instead

Conformance comes first. Once a process mostly matches the assumptions, its data can be trusted and it is "probabilistically predictable", at which point something like [[monte-carlo-simulation]] on historical data can be used with some confidence in its results (L1088-L1094). Once distribution information exists, "we are going to run away from Little’s Law for forecasting" (L3564). The checks are on [[littles-law-assumptions]] and the policies on [[process-policies-from-littles-law]].

Vacanti adds that predictability is not mainly about forecasts: "The bigger part of predictability is operating a system that behaves in a way that we expect it to" (L1100). See [[predictability]].

## Discriminating test

Measuring asks what the averages were over a finished window. Forecasting asks what they will be. Only the first is the law; the second is a rough estimate whose quality depends on whether the future keeps the past's conditions.

## Positions

**Vacanti:** a forecast from averages is at most a gut-check (L1096-L1098).

**Cohn:** divides remaining points by measured velocity and repeats after every period ([[reforecasting-a-release-from-velocity]]). This wiki reads that as the same arithmetic as the sign above, in points per period and not items per day: both divide what is open by a mean rate.

## Which holds under which setup

The resolution is this wiki's, and it turns on how the figure is stated, since neither source tests its method against the other's. A single date from a division is a gut-check under any setup. Under an iteration setup, Cohn's division is acceptable as a forecast only in the form this base already requires: a range built from several velocity values ([[velocity-range-forecast]]), with its basis stated and redone each period ([[stating-plan-uncertainty]]). That keeps the method and answers Vacanti's objection to a deterministic result, though a range taken from a few means is not the probabilistic modelling he asks for. Under a flow setup the per-item forecast is [[service-level-expectation]].

## Trade-off

This wiki notes the cost of the rule: a rough figure is cheap, and refusing to promise from it means waiting for enough history to forecast probabilistically. A new project has no such history, so a gut-check may be all that is available. It should then be presented as exactly that.

## Agent executor note

The rule concerns arithmetic on past averages, so it survives. In this wiki's reading the warning weighs more with an agent: a change of model or review practice changes the system the history describes, so the assumption that the future keeps the past's conditions fails sooner.
