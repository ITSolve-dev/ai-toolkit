---
title: Cumulative Flow Diagram
category: showing-work
summary: A chart of cumulative arrivals to and departures from a process over time, with optional bands for the steps between; it carries WIP, approximate average Cycle Time and exact average Throughput at once, but only if it obeys six properties, only about the past, and it cannot show whether what left was any good.
tags: [concept, showing-work, cfd, flow-metrics, board-history, visualization, retrospective-analysis, kanban]
sources: [vacanti-actionable-agile-metrics, scrum-guide-2020]
created: 2026-11-02
updated: 2026-11-02
---

# Cumulative Flow Diagram

A Cumulative Flow Diagram (CFD) plots, over time, how many items have arrived at a process and how many have departed from it, and optionally the same for each step in between. Vacanti's first point is that CFDs "are all about arrivals and departures" ([[vacanti-actionable-agile-metrics]] L1164); the earliest reference he found, from the 1960s, called the chart a "Cumulative Arrival and Departures Diagram" (L1164). He presents it as "a concise, coherent visualization of the three metrics of flow" (L1174); see [[flow-metrics]] for what those count.

His claim for it is that one diagram shows WIP, Cycle Time and Throughput together, "albeit sometimes in the form of averages or approximate averages" (L1720). The claim is conditional: "You can only be guaranteed to calculate these metrics, however, if your graph obeys all six properties of a CFD" (L1720).

This page is descriptive: it fixes what the chart is, so other pages can use the name. The construction rule is [[cfd-built-from-entry-dates]] and the defects are [[malformed-cfd]]. The quantitative reading is [[reading-flow-metrics-off-a-cfd]] and the qualitative one is [[reading-a-cfd]].

## The six properties

> CFD Property #1: The top line of a Cumulative Flow Diagram _always_ represents the cumulative arrivals to a process. The bottom line on a CFD _always_ represents the cumulative departures from a process.
>
> — [[vacanti-actionable-agile-metrics]], L1236

> CFD Property #2: Due to its cumulative nature, no line on a CFD can ever decrease (go down).
>
> — [[vacanti-actionable-agile-metrics]], L1404

The other four concern what can be read from a chart:

- **Property #3.** The vertical distance between any two lines is the work in progress between the two workflow steps those lines represent (L1544).
- **Property #4.** The horizontal distance between any two lines is the Approximate Average Cycle Time for items that finished between those steps (L1584).
- **Property #5.** The chart shows only what has happened. "The data displayed on a CFD depicts only what _has_ happened for a given process. Any chart that shows any type of projection is not a CFD." (L1636)
- **Property #6.** The slope of any line between two reporting intervals is the exact Average Arrival Rate of the state in the succeeding band (L1668). Vacanti's corollary is that the same slope is also the exact average Throughput of the preceding step (L1670).

Vacanti means these strictly: "When I say “always” I mean “always”." (L1242). The properties are a definition as well as a description:

> A CFD is only a CFD if it obeys all six properties because only by following all of these properties can you be guaranteed to derive the correct quantitative metrics of flow off of your graph.
>
> — [[vacanti-actionable-agile-metrics]], L1758

## Anatomy

| Part | Meaning |
|---|---|
| X-axis | "some representation of a progression of time (usually calendar time)" (L1194) |
| Y-axis | "a cumulative count of items in the process" (L1206) |
| Band | "each different colored section on the graph" (L1218); one per workflow step (L1212) |
| Line | "the demarcation boundary of any band" (L1218); a band's bottom line is the next band's top line (L1218) |
| Top line of the CFD | The top line of the top-most band (L1226) |
| Bottom line of the CFD | "the top line of the bottom-most band" (L1226), not the X-axis |

Each intermediate band's top and bottom lines are that state's arrivals and departures (L1242).

## What is free and what is not

The author of the chart chooses the tick labels, the scale, and the reporting interval, which is the "frequency that you choose to add data to your chart" (L1202). Labels and interval need not match: the book's example reports daily and labels monthly (L1202). Interval and scale both change the picture (L1202, L1206), and Vacanti treats that as a tool for sharpening it.

This wiki reads that as a limit on comparison: two CFDs with different intervals or scales cannot be compared by shape, so a reading of a chart states its interval.

The outer lines are chosen once. "[T]he definition of the boundaries of your process is essentially up to you" (L1242), and once chosen they are the top and bottom lines. This wiki reads those boundaries as the project's [[started-and-finished-points]], so a CFD has the same dependency on those points as every other metric.

## How many bands

Two bands, arrivals and departures only, are "a perfectly valid CFD" (L1262). Bands for the steps between are "very advantageous and strongly recommended—but by no means necessary" (L1242). The source poses the trade-off as a question and does not settle it (L1262).

Vacanti also prefers showing "the queuing states or “Done” columns" (L1278) over showing each step as one layer, because "[a] widening of these layers could hint at something going wrong in our process" (L1278). A takeaway of his Chapter 5 repeats the advice: "Consider building CFDs that show both “Active” and “Done” states within workflow steps" (L1760). That is one more reason to separate [[active-versus-queued]] states on the board, and [[bulging-band-on-a-cfd]] says what a thick queue band raises.

This wiki's rule for the choice, which is not the source's:

| Input | Read from |
|---|---|
| Which states the board distinguishes | Board columns and history |
| The question being asked | The person asking |

Use two bands for "are we taking in more than we finish". Use a band per state, with queues separate, for "where does work wait". The choice was too coarse if the total widens and no band says where. A chart cannot show a state the board does not record.

## Which question it answers

Vacanti claims "both quantitative and qualitative insight into problems—or potential problems—in our process" (L1174).

| Question | Where it is read | What the number is |
|---|---|---|
| How much work is in progress at this date, overall or in a step? | Vertical distance | Total WIP between the two lines |
| How long did items finishing on this date take, on average? | Horizontal distance, drawn backward | Approximate average only; see [[approximate-average-cycle-time]] |
| How fast did work leave, or arrive, over this range? | Slope of a line | Exact average; see [[throughput]] |

## Which question it cannot ask

[[what-a-cfd-cannot-answer]] holds the limits on cause, bottleneck and health. The rest are these.

- **What will happen.** "[I]f you would like to do projections on a graph, then what you want is a something other than a CFD." (L1484). A horizontal line drawn forward "could cause you to never intersect the top line of the bottom-most band" (L1632). Vacanti does not dismiss forecasting. He says projections need "a completely different chart—and more probably a completely different approach (like Monte Carlo Simulation)" (L1638-L1644). See [[monte-carlo-simulation]] and [[which-chart-for-which-plan-question]].
- **How long any particular item took, or the exact average.** The items entering at one end of the line are not necessarily the items leaving at the other (L1646).
- **How long unfinished work has been open.** The Cycle Time calculation "is only valid for items that have finished" (L1632). This wiki reads that as meaning the age of open work has to come from item-level data and not from the chart. See Work Item Age on [[flow-metrics]].
- **What a shape means, without context.** Vacanti lists as a myth that "It is possible to make a qualitative assessment of a CFD without understanding its context" (L1770).
- **Every broken assumption of [[littles-law]].** "[M]any times an assumption violation will not clearly reveal itself on a CFD." (L1284). Vacanti's remedy is to know the assumptions and "map them to the context in which the data was collected" (L1284). This wiki concludes that a clean chart is not a clean process.
- **What left, or how.** The turnstiles of his shop example "would not track how long each individual spent in the shop, nor would they be able to tell us if a departing individual made a purchase or not" (L1314). This wiki reads that as a general limit: a departure means an item crossed the finish boundary, and says nothing about the result. Tasks that deliver nothing raise the bottom line as well as tasks that deliver, which is the illusion noted on [[flow-metrics]].

## Signs that a chart is not a CFD

The signs are on [[malformed-cfd]]. Each raises a question about how the chart was built, and numbers read from such a chart lose the guarantee (L1758). This wiki adds one that belongs to the reader and not to the chart: a number read off the chart and labelled an exact Cycle Time. The chart may be sound, but the reading is wrong; see [[approximate-average-cycle-time]].

## Segmenting

Flow data can be viewed whole or as a CFD of one or more subtypes: only user stories, only defects, or stories and maintenance combined (L1712-L1718). Vacanti also names filtering by release and by a custom field relevant to the context, and challenges the reader to think about which attributes to collect and filter on (L1718).

Filtering across teams or at portfolio level (L1718) belongs to another scale and does not apply to a few people steering an agent. This wiki's reading is that filtering by type or release does carry over, provided the attribute is present on the task, since it cannot be recovered from the chart afterwards.

## Myths the book lists

The takeaways of Vacanti's Chapter 5 name four common myths (L1762-L1770). Each is handled on its own page.

| Myth | Page |
|---|---|
| It is always correct to build a CFD from work item count data at each reporting interval | [[cfd-built-from-entry-dates]] |
| A horizontal line represents an exact Cycle Time or an exact average Cycle Time | [[approximate-average-cycle-time]] |
| It is always ok to represent a traditional backlog on a CFD | [[backlog-versus-commitment]] |
| It is possible to make a qualitative assessment of a CFD without understanding its context | [[reading-a-cfd]] |

## Positions

**Vacanti:** the principles "apply regardless of the particular methodology that has been chosen" (L1254), and a board as simple as To Do, Doing, Done qualifies (L1248). Projections are excluded from the chart.

**Scrum Guide:** lists "cumulative flows" among practices "to forecast progress" ([[scrum-guide-2020]] L202).

**Which holds:** this wiki resolves the disagreement by tense. Under any setup the chart itself records what happened, and a forecast is made elsewhere from the same dates. The resolution is ours.

## Scale and agent executor note

The properties and the anatomy are arithmetic over state changes, so they survive an agent executing and hold at any team size. Vacanti's claims about the chart's value come from his experience with human teams, with no measurement behind them.

His running example covers 517 departures over 148 days, about 3.49 items per day, with 90 items in progress on one date (L1558, L1682). That is much larger than a board kept by a few people. A sparse board gives a stepped line, and this wiki's reading is that a horizontal reading from it is coarser than the example suggests. Whether a CFD says much on a board moving a few items a week is untested here.
