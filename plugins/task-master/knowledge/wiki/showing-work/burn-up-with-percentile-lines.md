---
title: Burn-Up Chart with Percentile Lines
category: showing-work
summary: A projection chart, which is not a CFD, marked with lines at the release date minus percentile cycle times, so it shows which items still have what chance of making a release.
tags: [method, visualization, forecasting, burn-up, cfd, percentile, release-planning]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Burn-Up Chart with Percentile Lines

A **burn-up chart with percentile lines** adds to a projection chart a marker at the completion date minus a percentile of cycle time, so that the start date of each item says something about its chance of making the release. Vacanti offers it to anyone who insists on burn-up projections: "might I suggest you augment your charts with the percentiles off of your Scatterplot?" ([[vacanti-actionable-agile-metrics]] L3618).

## A projection makes it not a CFD

Vacanti is strict on the name: "any CFD with a projection on it is not a CFD" (L3584), and he calls such charts Burn Up or Projection Charts (L3590). He gives two reasons: a projection needs a backlog on the chart, but "CFDs should not have backlogs on them" (L3590); and "CFDs are for looking backward, they are not for making projections about the future" (L3590). He adds that this is no defect of the projection view itself, which "can potentially be very useful" (L3590) when used correctly.

**Sign:** a chart presented as a [[cumulative-flow-diagram]] that shows a backlog band or a trend line beyond today (its signs of malformation). The question to check is whether it is being read as a record of what happened or as a promise.

## Procedure

The steps below follow L3618.

1. Start from the arrival and departure data used for a CFD.
2. Choose a completion date for the project or release, and extend the X-axis to it.
3. Draw a vertical line at that date.
4. From the [[cycle-time-scatterplot]], take the cycle time at the 85th percentile, "or whatever percentile you feel comfortable with" (L3618).
5. Subtract it from the completion date and draw a second vertical line there, labelled with the percentile.

## How to read it

Vacanti's reading: "any item that is started before that 85<sup>th</sup> percentile line has a greater than 85% chance of making the release" (L3620), and "Any item started after that line has a less than 85% chance of making the release" (L3620). Further lines at other percentiles can communicate the falling chance of late-started items (L3620). He also notes that the items making up the throughput line before the completion date will be in the release (L3620).

The use he names is ordering: "Product owners (or customers) can then use that information to help guide them in the selection of what items should be started next." (L3628). This wiki reads that as an input to choosing what starts next near a release: an item that starts after the line carries its stated lower chance, which can be weighed against the value of the item.

## What the chart cannot ask

The chart answers "what chance does an item started on this date have?", and does not answer "how many items will be in?". Vacanti: "this chart will not tell you the exact number of items that will be in any given release" (L3622), and he argues no chart will deterministically. He proposes the better question: "what is the likelihood of getting at least X number of work items finished by a particular date" (L3622), which is the territory of [[throughput-monte-carlo]].

## Limits

These limits are this wiki's reading, not the source's. The percentile is per item and comes from past cycle times, so the reading holds only while those times still describe the process. If many items are started just ahead of the line, WIP rises and the history no longer applies; the sign is a jump in in-progress count near the line. Later fact that would show the reading wrong: well under 85% of the items started before the line reach the release.

## See also

[[service-level-expectation]], [[straight-line-projection]], [[forecast-range-and-probability]], [[release-burndown-chart]]
