---
title: Forecasting from an Average
category: periods
summary: A date derived from a mean carries no probability, because the mean's percentile is unknown until the distribution is known.
tags: [failure-mode, estimation, forecasting, averages, distribution]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Forecasting from an Average

**Forecasting from an average** means turning a mean, such as average throughput, average velocity or average cycle time, into a completion date. Vacanti rejects it outright: "You never want to make a forecast based on an average." ([[vacanti-actionable-agile-metrics]] L3552). The defect is that the result cannot carry a probability, so it fails [[forecast-range-and-probability]] by construction.

## Reasoning

Vacanti calls the average "a meaningless statistic unless you know something about the underlying distribution of the data from which the average was calculated" (L3552). Without the distribution, nobody knows which percentile the word "average" refers to:

> depending on the shape of the distribution, the mean could be significantly less than 50%, exactly 50%, or significantly more than 50%.
>
> — [[vacanti-actionable-agile-metrics]], L3558

Vacanti then closes the chain: "If we do not know the distribution, then we cannot give a probability of where the average falls. If we do not know a probability, then we cannot make a forecast." (L3560). This wiki reads the practical consequence as follows: a date from an average is not a coin-flip date either, since even "half the time" is an unsupported reading of it. The shape of real cycle times is on [[cycle-time-histogram]] and [[completion-time-distribution]].

## Sign

- A date whose working divides remaining items or points by an average rate.
- A figure labelled "average cycle time" or "average velocity" offered as the answer to "when?".
- A trend line through throughput read off as a release date; see [[straight-line-projection]].

The question each sign raises is whether the distribution behind the number is known and whether a probability was stated. The first sign also describes Cohn's division by velocity; that disagreement is resolved on [[littles-law-does-not-forecast]].

## What to do instead

Vacanti's direction is to acquire the distribution: "Further, I would argue it is worth investing in acquiring that knowledge." (L3564), and with it to leave average-based methods for percentile-based ones. For one item that is [[single-item-forecast]]; for several, [[monte-carlo-simulation]].

## Trade-off

A percentile needs per-item history, not one rate. This wiki notes that the board history already holds it, so the cost is reading and not logging.

## See also

[[littles-law-does-not-forecast]], [[straight-line-projection]], [[forecast-range-and-probability]]
