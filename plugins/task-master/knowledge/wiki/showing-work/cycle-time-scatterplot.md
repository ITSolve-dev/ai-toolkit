---
title: Cycle Time Scatterplot
category: showing-work
summary: A chart with one dot per finished item, placed at its finish date and its cycle time; it shows each item's time rather than an average, gives percentiles, the trend across a period and outliers to investigate, and says nothing about work still open.
tags: [concept, visualization, cycle-time, flow-metrics, board-history]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Cycle Time Scatterplot

A cycle time scatterplot is a chart with one dot per finished work item: the X-axis is the process timeline, and the Y-axis is the item's [[cycle-time]] ([[vacanti-actionable-agile-metrics]] L2616, L2620). The source introduces it as the step past averages: a [[cumulative-flow-diagram]] gives a good idea of how long items take "_on average_", but "there are going to be times when doing analysis based solely on average is not going to be good enough (things like forecasting a completion date come to mind, for example)" (L2586).

This page says what the chart is and how one organization used it. For the choice between this chart and its neighbours, see [[which-view-of-cycle-time]]. For reading its shapes, see [[reading-a-cycle-time-scatterplot]].

## How it is built

1. When an item finishes, find its finish date on the X-axis.
2. Go up to its cycle time and plot a dot. An item that took seven days and finished on January 1, 2013 sits at that date and seven days (L2622).
3. Where several items share a date and a cycle time, the dots stack. A tool should mark the count, because a stack otherwise reads as one item (L2630).

The unit of the Y-axis and the frequency of the X-axis labels are free choices (L2616, L2620).

> A dot is always plotted on the day a given work item finishes.
>
> — [[vacanti-actionable-agile-metrics]], L2628

### One contradiction in the source

The chapter body says a scatterplot has "really no concept of a reporting interval" (L2622-L2628), unlike a cumulative flow diagram. Its closing takeaways say "The labels and reporting intervals on the chart are at the sole discretion of the graph’s creator." (L2764). This wiki resolves it in favour of the body, because the mechanism is stated there and the takeaway reads as a shorthand: axis labels are a free choice, and a dot's date is not. Binning dots into weeks would change the chart's data, not its labels.

## What the raw dots give, and what gives them structure

Left alone, the chart is "a random set of dots" (L2632). The structure comes from [[cycle-time-percentile-lines]], drawn across it. The same data, condensed by frequency, is a [[cycle-time-histogram]].

The source says a scatterplot can carry other metrics too, such as throughput or bugs per feature, and that in this book the unqualified word means the cycle time version (L2598).

## How Siemens HS used it

The [[siemens-hs-case]] used the chart in three ways.

**Percentiles.** The plot for the release before Kanban showed "50% of all stories finished in 21 days or less" and "85% of stories were finishing in 71 days or less" (L4078). Comparing these with the sprint length is the test on [[iteration-length-versus-cycle-time]]. A percentile is not a bound. The chapter itself slips, saying a release "yielded Cycle Times of 43 days or less" (L4154) when it means the 85th percentile. This wiki reads that as a warning for any report: keep the likelihood attached ([[stating-plan-uncertainty]]).

**The trend.** Siemens' pre-Kanban release showed Cycle Times "getting longer and longer and longer" (L4078), and the source calls this "not a picture of a very predictable process" (L4088). A flat band after a change was its sign of stabilization (L4126-L4132). See [[conservation-of-flow]].

**Outliers.**

> By using the Scatterplot, teams could clearly see stories whose Cycle Time exceeded normal ranges, perform root cause analysis and take steps and actions to prevent recurrence.
>
> — [[vacanti-actionable-agile-metrics]], L4192

This wiki reads the procedure as taking the items above the agreed percentile, reading each one's history, naming a cause, and recording it for retrospective analysis. The chapter does not define "normal ranges". [[internal-and-external-variability]] says which items are worth the look.

## What it cannot ask

This wiki reads four limits from the construction.

- **Open work is invisible.** A dot appears only when an item finishes, so an item that has been open for months contributes nothing until it closes. The chart lags in exactly the case that matters, as [[flow-metrics]] says of cycle time generally. Age of open work has to be read separately.
- **Start dates are hidden.** Position on the X-axis is the finish date, so two dots side by side may have started far apart.
- **It carries no cause.** A dot high on the chart says an item took long and does not say why. It raises a question; see [[smell-is-not-a-finding]].
- **It says nothing about value.** A dot records that an item finished, not whether the finish was useful.

## Not a Control Chart

The source insists that this chart is neither a Control Chart nor a Run Chart (L2766). It has no objection to Run Charts as such (L2720). The chart usually sold under the first name is the defect on [[pseudo-control-chart]].

## Read from history

This wiki notes that the chart needs only the started and finished timestamps of finished items, so it comes from board history without logged hours, measured against the project's [[started-and-finished-points]].

## Agent executor note

This wiki's reasoning, unmeasured: the construction is timestamps and counts, so it survives an agent executing. A few people steering an agent produce few dots, and there the dots themselves are the useful reading, since each can be opened and checked, and percentiles are rough ([[how-much-flow-data]]); Siemens' percentiles rest on many stories from one large program. An agent-run item's dot includes the time its result waited for a person, so a high dot may be a review delay and not an execution problem. A change in how work is executed makes older dots incomparable.
