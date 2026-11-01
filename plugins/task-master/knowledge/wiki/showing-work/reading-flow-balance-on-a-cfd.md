---
title: Reading Flow Balance on a CFD
category: showing-work
summary: A CFD shows arrival and departure rates as slopes, WIP as vertical distance and approximate cycle time as horizontal distance; diverging lines signal imbalance, but a tidy chart proves nothing about health.
tags: [method, cumulative-flow-diagram, cfd, arrival-rate, departure-rate, visualization]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Reading Flow Balance on a CFD

A [[cumulative-flow-diagram]] answers one question quickly: are arrivals and departures balanced? “One of the best ways to visualize whether arrivals and departures are balanced is to visualize them via a CFD.” ([[vacanti-actionable-agile-metrics]] L2206) It replaces the plain comparison of averages in [[measuring-arrival-and-departure-rates]], which the source treats as the weaker method (L2074). The general procedure for reading numbers off the chart is [[reading-flow-metrics-off-a-cfd]].

## What to read

| Question | Where on the chart |
|---|---|
| Arrival Rate | Slope of the top line of the topmost layer (L2094) |
| Departure Rate, or [[throughput]] | Slope of the top line of the bottommost band (L2094) |
| WIP | Vertical distance between arrivals and departures (L2108) |
| Approximate Average [[cycle-time]] | Horizontal distance between arrivals and departures (L2108) |

Each layer corresponds to one board step (L2094). The arrivals column appears on the chart; a backlog does not (L2028).

## Two ways to read it

**Quantitative.** Calculate the slopes. The source's example board gives 3.72 items per day arriving and 2.74 departing, so items arrive faster than they leave by about one item a day (L2094). Those figures belong to that illustrative chart and are not a benchmark.

**Qualitative.** No calculation is needed: “we can quite quickly do a qualitative assessment of the health of our system.” (L2096)

## What the shape means

- **Lines diverging.** Work arrives faster than it departs. As the arrival line pulls away, WIP grows and approximate average cycle times lengthen (L2118). This is the failure on [[conservation-of-flow]], with its chart form on [[mismatched-arrivals-and-departures]]. The action is to “get arrivals to match departures” (L2128), which starts with [[arrivals-column-wip-limit]].
- **Lines roughly parallel.** Average arrivals equal average departures (L2146-L2148). The source says any process that limits WIP throughout, and honors the limits, gets this picture (L2150); see [[constant-wip]].

The earlier part of a diverged chart is also evidence: where the lines were closer, WIP was smaller and cycle times shorter (L2118). This wiki reads that as a way to date when the imbalance began.

## What it cannot ask

A balanced chart is necessary and not sufficient. “[H]aving a pretty CFD is not a guarantee of a healthy system, but it is certainly a pretty decent start.” (L2148) The takeaway is stated flatly: “Pretty CFD pictures could still mask underlying process problems.” (L2212) See [[what-a-cfd-cannot-answer]].

Vacanti's Chapter 7 defers the specifics. This wiki notes that the chart shows averages and bands, not any single item, so it cannot say which items are aging or whether started items finish, which the source raises as a separate violation (L2196). Another chart or history reading has to answer those.

## Failure modes

- **Reading a smooth chart as success.** The sign is a report that cites balance with no look at item ages or abandoned work.
- **Reading horizontal distance as an exact cycle time.** The source names it “Approximate Average Cycle Time” throughout (L2108): it is an approximation of an average, and no single item's time can be read from it. See [[approximate-average-cycle-time]].
