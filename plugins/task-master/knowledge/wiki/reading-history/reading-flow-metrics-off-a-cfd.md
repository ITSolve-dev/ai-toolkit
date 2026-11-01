---
title: Reading Flow Metrics off a CFD
category: reading-history
summary: The procedure for reading WIP (vertical), Approximate Average Cycle Time (horizontal, backward, plus one unit) and exact average Throughput or arrival rate (slope) from a valid CFD, overall or between any two lines.
tags: [method, retrospective-analysis, cfd, flow-metrics, wip, cycle-time, throughput]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Reading Flow Metrics off a CFD

**Reading flow metrics off a CFD** is a three-part procedure against one chart: subtract vertically for WIP, subtract horizontally for Approximate Average Cycle Time, and take a slope for average Throughput or arrival rate. Each reading applies between the top and bottom lines for the whole process, or between any two lines for part of it ([[vacanti-actionable-agile-metrics]] L1540, L1622, L1684).

## Inputs

- A chart that obeys all six properties of a [[cumulative-flow-diagram]]; check this first, because the guarantee depends on it (L1720). See [[malformed-cfd]].
- The date, or date range, in question.
- The reporting interval. The steps are the same whether the interval is days, weeks or months (L1592-L1598).

## WIP: vertical distance

1. Take the date of interest.
2. Read the y-value of the upper line and the lower line at that date.
3. Subtract.

In the book's example, September 1 shows 290 on the top line and 200 on the bottom line, so total WIP is 90 work items (L1558). WIP in one step is the same subtraction across that step's band (L1570). The two lines may be any two: Vacanti's examples include Analysis Active, Development Done, and the span from Analysis Done to Test (L1540).

## Approximate Average Cycle Time: horizontal distance

1. Start at the date of interest on the bottom line.
2. Draw a horizontal line backward until it meets the top line.
3. Read the date at that intersection.
4. Subtract it from the bottom-line date.
5. Add one time unit.

For September 1 the line meets the top line at August 9; the subtraction gives 23 days and the added unit gives 24 (L1600-L1608). The reason for step 5 is on [[cycle-time-add-one-time-unit]].

The same reading works through one step or between any two lines (L1622). The direction is fixed, from the later line backward. The calculation "is only valid for items that have finished", and a line drawn forward may never meet its target (L1632).

## Average Throughput and arrival rate: slope

1. Choose the date range. The number of time units in it is the run.
2. Read the bottom line at both ends. The difference is the rise.
3. Divide rise by run.

From June 21 to November 16 the run is 148 days. The bottom line goes from 0 to 517, so the rise is 517, and average Throughput is 517 / 148 = 3.49 items per day (L1682). Substituting the top line gives the average arrival rate, and any other line gives the rate for that step (L1682-L1684). See [[throughput]].

## Report each number with its label

| Metric | Reading | Label it as | Applies to |
|---|---|---|---|
| WIP | Vertical | Total between two named lines | One reporting interval |
| Cycle Time | Horizontal, backward, plus one | Approximate average | Items finished at that date |
| Throughput, arrival rate | Slope | Exact average | The stated range |

The labels come from the source's insistence that only the slope is exact and the horizontal is not (L1646, L1656). This wiki adds that dropping them turns a sound reading into a false claim.

## Failure signs

This list is this wiki's own, drawn from the limits above. Each sign says what to check.

- A Cycle Time read off a chart with no "approximate": check for [[approximate-average-cycle-time]] being read as exact.
- A Cycle Time reported for a date with no finished items, or for work still open: check whether the horizontal line was drawn forward or the number came from elsewhere.
- A Throughput figure with no date range: the average cannot be checked, and a different range can give a different figure.
- Two Cycle Time figures compared across reports: check that both counted the added unit the same way.

## Transfer to this plugin

The book describes reading by eye from a drawn chart. This wiki's reading is that a plugin holding board history can compute the same quantities from the cumulative series, and has item dates besides. The labels still apply to anything derived the chart's way, since the horizontal reading stays approximate however precisely it is computed.
