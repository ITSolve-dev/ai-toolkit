---
title: Measuring Arrival and Departure Rates
category: reading-history
summary: Count items crossing the arrival and departure points per unit of time, in the same unit, then compare the averages; a shared reporting unit does not require a shared cadence.
tags: [method, arrival-rate, departure-rate, throughput, cadence, metrics]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Measuring Arrival and Departure Rates

This method tells whether [[conservation-of-flow]] holds, by comparing how fast work enters the process with how fast it leaves. Both rates are counts, read from board history, and need no logged time.

## Procedure

1. Fix the [[arrival-point]] and the [[departure-point]]; the rates are meaningless without them.
2. Choose a unit of time. It “is completely up to you (day, week, every two weeks)” ([[vacanti-actionable-agile-metrics]] L2038).
3. Count new items placed on the arrivals column per unit (L2038). Count items crossing the departure line per unit, in the same way (L2062).
4. Average both and compare. “If those two averages come out to be the same, then you are in good shape.” The source's guess is that they will differ (L2064-L2070).

A CFD does the same comparison better and is the source's preferred form (L2074); see [[reading-flow-balance-on-a-cfd]].

## How much history

The period is “arbitrarily long”, though what is needed may be “perhaps as little as a few weeks” (L2064). The source gives this with no setting behind it, so this wiki treats it as a starting point and not a threshold. At a low item count, a few weeks may hold very few items, and this wiki reads a small gap between averages there as noise before reading it as imbalance.

## Unit versus cadence

These are two different things, and confusing them is the main trap here.

- **Unit of measurement** must be identical: “the unit of time you choose to measure the Arrival Rate must match the unit of time that you choose to measure your Departure Rate” (L2038).
- **Cadence** need not be: “choosing the same interval of time to measure arrivals and departures does not mean that the cadence of arrivals and departures must be the same.” (L2040)

A team may deploy every two weeks and replenish every week, and that “might be optimal given your specific context” (L2040). The cost is a conversion: data in two-week and one-week intervals must be brought to one unit before comparing, in either direction (L2040-L2046). Further, “whatever unit of time you choose for your reporting must be consistent across all metrics.” (L2046)

## Signs of a bad measurement

These are this wiki's application; each raises a question to check.

- Rates compared across different units, for example per-sprint departures against per-week arrivals.
- Arrivals counted from a backlog and not the arrivals column, which counts demand and not commitment.
- A departure average taken over intervals with batch deployment, in a unit shorter than the batch, which gives many zeros and spikes. Convert to the batch length first.

## What it cannot say

Equal averages say the rates match over the period. This wiki reads them as saying nothing about whether the process is healthy; see [[reading-flow-balance-on-a-cfd]].
