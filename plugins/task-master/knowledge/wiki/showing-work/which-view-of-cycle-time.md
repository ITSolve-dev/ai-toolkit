---
title: Which View of Cycle Time
category: showing-work
summary: Choose by the question; a cumulative flow diagram for averages, a scatterplot with percentile lines for how long one item may take and for change over time, a histogram for the shape of the data, and neither for work still open.
tags: [decision-rule, visualization, cycle-time, flow-metrics]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Which View of Cycle Time

The views of [[cycle-time]] answer different questions, and the [[cycle-time-scatterplot]] and [[cycle-time-histogram]] hold the same data. The source keeps both because of what each hides:

> The Scatterplot is a temporal view of data that can show trends of dots over time. A Histogram is a condensed, spatial view based on the frequency of occurrence of Cycle Times.
>
> — [[vacanti-actionable-agile-metrics]], L2824

> Looking at the Scatterplot in Figure 10.1 it may not be obvious that the shape of the data is that in Figure 10a.1. Likewise, looking at the Figure in 10a.1 you may not be able to detect any patterns of Cycle Times over a given timeline.
>
> — [[vacanti-actionable-agile-metrics]], L2824

This page is the cycle time counterpart of [[which-chart-for-which-plan-question]].

## The choice

The first two columns follow the source for the first four rows. The last row and the "cannot ask" column are this wiki's reading.

| Question | View | Cannot ask |
|---|---|---|
| How long do items take on average? | [[cumulative-flow-diagram]] (L2586) | How long this one item may take, or at what probability |
| How long may one item take, at what probability? | Scatterplot with [[cycle-time-percentile-lines]] (L2650-L2664) | Whether the coming items resemble the past ones |
| Did cycle time change over this period? | Scatterplot, for its timeline (L2824) | Why it changed |
| What shape does the data have, and how long is the tail? | Histogram with the same percentile lines (L2822-L2824) | When any of it happened |
| What is open now, and how old is it? | Neither: Work Item Age, on [[flow-metrics]] | Anything, since both views count finished items only |

## Inputs and what would show the choice wrong

| Input | Read from |
|---|---|
| The question being asked | The request itself |
| Whether a dated answer is needed | Whether it is about one item, or a selection over a date |
| Enough finished items for a shape | Board history; the source gives no count in this passage |

This wiki reads a choice as wrong when the answer depended on something the view collapses. Two later facts show it: a period reported healthy from a histogram, while the scatterplot for the same dates shows a rising trend; or a forecast given from finished items, while open items already older than the top line turn up later.

A date for a single item comes from a line, stated with its probability. The source's reason for leaving averages behind is exactly this case: a completion date is its example of when an average is not good enough (L2586). This wiki notes that a question about a whole set of items by a date is a different one, which a per-item line does not answer. See [[service-level-expectation]], which is per item, and [[stating-plan-uncertainty]].

## Which holds under which setup

This wiki's resolution, on the source's position:

- **Flow setup:** the scatterplot is the default view, because a per-item forecast is the only one that setup has.
- **Iteration setup:** the plan questions on [[which-chart-for-which-plan-question]] come first, and a scatterplot is an optional addition, since cycle time under a period is capped in practice by its length.
- **Few finished items, any setup:** prefer the scatterplot and read individual dots, because a histogram's shape needs volume that a small board does not have.

## Failure modes

- Reporting only a histogram, which hides a drift in time.
- Reporting only an average, which hides the tail and the spread.
- Using a cycle time view to judge open work, when it can only show that work after it closes.
