---
title: What a CFD Cannot Answer
category: showing-work
summary: A CFD cannot name a cause or fix, cannot locate a systemic bottleneck, and cannot prove health; a pretty chart can hide a dysfunctional process.
tags: [concept, cfd, visualization, bottleneck, flow-debt]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# What a CFD Cannot Answer

A [[cumulative-flow-diagram]] raises questions about flow, and several questions people bring to it are ones it cannot settle. This page holds the limits on cause, bottleneck, health and forecast, so that [[reading-a-cfd]] does not claim more than the chart can give. Its limits on the future, on single items and on open work are on the [[cumulative-flow-diagram]] page itself.

## Exact cause and exact fix

"Just like any visualization, a CFD is not going to tell you exactly what is wrong with your process or exactly how to fix it, but it is going to shine a light or a magnifying glass on the places to investigate." ([[vacanti-actionable-agile-metrics]] L1776) Vacanti adds: "CFDs are not going to do our jobs for us. They do not replace thinking." (L1778)

The conclusion of his Chapter 6 says a CFD "will also suggest the right actions to take for increased predictability" (L1954). This wiki reconciles the two passages by reading the later one as direction, and takes the first as the limit on what a finding may state.

## Where the bottleneck is

Vacanti leaves bottlenecks out on purpose, and dissents from the usual claim about CFDs: "I believe that the best you can do by just looking at a CFD is to pose some questions about some variability that may be occurring. It is impossible to spot a systemic bottleneck." (L1944) He prefers "Deming's and Shewhart's language of variability to that of Goldratt's language of the Theory of Constraints" (L1944), and defers the argument to his Chapter 13.

This wiki treats that as a rule for wording: a finding from a CFD says a step shows variability worth checking, and does not name a step as the bottleneck. The sign of a violation is a finding that says "bottleneck" and rests on the chart's shape alone. A bulge in one step is the closest temptation, and [[bulging-band-on-a-cfd]] explains why its cause may lie elsewhere. One passage of the book's Siemens case says the opposite, and [[bottleneck-on-the-cfd]] resolves it: a step may be named only with per-column numbers behind it.

## Whether the process is healthy

"it is possible to get a very pretty CFD picture but still have a very dysfunctional process underneath" (L1938). Vacanti's best example is the accumulation of [[flow-debt]] (L1938), which he treats in his Chapter 9. This wiki reads that as saying a clean chart removes the shape-based questions without clearing the board.

If a chart truly does look good, Vacanti moves to improvement (L1936):

- Can the lines get closer together by reducing WIP and so improving Cycle Time?
- Can the Throughput line get steeper?

## Forecasts beyond its assumptions

The predictive power of a CFD "depends almost entirely on how well your process obeys the assumptions behind Little's Law" (L1964-L1970). This wiki reads that as a precondition on any figure taken from the chart: when [[mismatched-arrivals-and-departures]] or a long flat stretch is present, the assumptions are in question, and so is the figure. See [[littles-law-assumptions]] and [[littles-law-does-not-forecast]].
