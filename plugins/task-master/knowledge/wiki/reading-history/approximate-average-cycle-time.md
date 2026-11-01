---
title: Approximate Average Cycle Time
category: reading-history
summary: The horizontal distance on a CFD gives an approximate average Cycle Time for finished items, not an exact Cycle Time and not an exact average, because the items entering at one end are not necessarily those leaving at the other.
tags: [concept, retrospective-analysis, cycle-time, cfd, failure-mode]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Approximate Average Cycle Time

**Approximate Average Cycle Time** is what the horizontal distance between two lines on a [[cumulative-flow-diagram]] gives: an estimate of how long, on average, items that finished at a chosen date took between the two workflow steps ([[vacanti-actionable-agile-metrics]] L1574, L1584). Vacanti is emphatic that each word of the name matters, because "there is a lot of misinformation or disinformation about CFDs out there" (L1646). The procedure is on [[reading-flow-metrics-off-a-cfd]], and the measure it approximates is [[cycle-time]].

## Three numbers that get confused

| Number | Where it comes from | Readable from the chart alone? |
|---|---|---|
| Cycle Time of an item | That item's own dates | No |
| Exact average Cycle Time | The item data behind the chart | Not without the data, or an understanding of the policies that generated the diagram |
| Approximate Average Cycle Time | Horizontal distance on the CFD | Yes |

## Why it is only approximate

- **Not an exact Cycle Time.** On the claim that the horizontal line gives one, the source says "It does not", because "the items that start on the top line of your Cumulative Flow Diagram (at the beginning of your horizontal line) are not necessarily the items that finish at the bottom line of your Cumulative Flow Diagram (at the end of your horizontal line)" (L1646).
- **Not an exact average either.** Unless we look at the data, or understand the policies behind the diagram, "the best we can say is that this horizontal calculation will lead to an Approximate Average Cycle Time" (L1646).

Vacanti finds the result remarkable for two reasons: subtracting two dates yields an average at all, and it does so even though the items at the two ends differ (L1618-L1620).

## What its quality depends on

The approximation "can be very good" (L1646), and how good is conditional:

> Interestingly enough, how good an approximation this calculation is will depend on how well we are adhering to the assumptions that make Little’s Law work.
>
> — [[vacanti-actionable-agile-metrics]], L1620

This wiki reads that as saying a reader should check the assumptions before trusting the figure. They are on [[littles-law-assumptions]]. The book also promises policies that make the approximation excellent, and does not give them at this point (L1646).

## Limit: finished items only

The calculation "is only valid for items that have finished", and the line must be drawn backward (L1632). This wiki reads that as excluding work still open, whose age needs Work Item Age on [[flow-metrics]] instead.

## Failure mode: the horizontal line read as exact

Vacanti lists "A horizontal line represents an exact Cycle Time or an exact average Cycle Time" among common myths (L1766).

- **What breaks:** a figure that describes no particular item gets used as though it did, for example as the time a specific item took or as what the next item will take. The second use also conflicts with [[cumulative-flow-diagram]] Property #5, since the chart says nothing about the future.
- **Observable sign:** a report giving a CFD-read Cycle Time without "approximate", attaching it to named items, or calling it the average with no source data behind it.
- **What to check:** compute the exact average from item dates and compare.

The sign and the check are this wiki's derivation from the source's argument.

## The gap is itself information

Vacanti calls this potentially the most important reason to keep the distinction:

> It turns out the comparison of the Approximate Average Cycle Time off of your CFD with the exact average Cycle Time from your real data can give you tremendous insight as to the health of your process.
>
> — [[vacanti-actionable-agile-metrics]], L1652

The specifics of that analysis are deferred to his Chapter 9 (L1652). This wiki notes that nothing in Chapter 5 says what a given gap means, so no threshold should be inferred from it.

## Trade-off

The reading is cheap, needing one chart and two dates. The cost is that it gives a single approximate average with no spread. This wiki's reading is that a plugin with board history should treat the exact average as the primary figure and the chart reading as the comparison, because item dates are available to it.
