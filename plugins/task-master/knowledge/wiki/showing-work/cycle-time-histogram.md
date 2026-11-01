---
title: Cycle Time Histogram
category: showing-work
summary: Bars counting finished items per cycle-time bin; the same data as a scatterplot condensed to show its shape, which in knowledge work is usually a hump on the left and a long right tail, at the cost of all information about when.
tags: [concept, visualization, cycle-time, flow-metrics]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Cycle Time Histogram

A cycle time histogram is a chart of frequency against cycle-time ranges: each bar counts how many finished items fell into that bin ([[vacanti-actionable-agile-metrics]] L2782, L2804). The source says histograms are "really just another view of the same data shown on a Scatterplot" (L2776), so it holds nothing a [[cycle-time-scatterplot]] does not. What it adds is a view of the shape.

The page is descriptive. The source treats histograms as an advanced topic and says "you need not master this analysis to be successful with the predictability concepts presented in this book" (L2774). This wiki reads that as a reason to treat the chart as optional: a project with a scatterplot and [[cycle-time-percentile-lines]] loses nothing it needs for a forecast.

## How it is built

Go through each data point and increment the bin whose range it falls in (L2804). The vertical axis is frequency, the horizontal axis the ranges (L2796, L2804). Percentile lines can be placed on it as on a scatterplot (L2822).

## The usual shape

> That is to say Histograms in our world usually have a big hump on the left and a long tail to the right.
>
> — [[vacanti-actionable-agile-metrics]], L2796

Why that shape occurs, and whether it is log-normal, Weibull or something else, the source declares "beyond the scope of this introductory book" (L2796). It claims only that "Knowing this shape can give you some insight to the problem areas of your process" (L2796) and that deep analysis is possible.

This shape is the source's ground for rejecting mean-and-deviation charts ([[pseudo-control-chart]]). The chapter asserts the shape and does not offer data for it beyond an example figure, so this wiki grades it as a practitioner's general observation, and notes that a project can check it against its own history in one chart.

This wiki reads two practical consequences. In a long right tail, the mean sits above the point most items reach, so an average overstates the typical item while still understating the slowest ones. And a report needs at least one high percentile, since the tail is where the surprises live. The same right-skewed shape, for one task's duration, is on [[completion-time-distribution]].

## More data, a sharper picture

The source illustrates with four six-sided dice, summing each roll into bins from 4 to 24, at 10, 100 and 5000 trials: "as the number of trials increases, the shape of the distribution sharpens" (L2806-L2818). Its lesson comes with a limit: "more data is usually better than less data when it comes to visualization (but do not be fooled into thinking you need massive amounts of data to be successful with a statistical approach)" (L2818).

This wiki adds two cautions. The dice illustrate sharpening and not the shape of cycle times, since a sum of dice does not have a long tail. And the source gives no count at which a shape can be trusted. On a small board, a histogram of a dozen items mostly shows the choice of bins, so there a scatterplot serves better.

## What it cannot ask

The source: "looking at the Figure in 10a.1 you may not be able to detect any patterns of Cycle Times over a given timeline." (L2824). A histogram collapses time, so a process that got slower looks the same as one that was always mixed. The choice is on [[which-view-of-cycle-time]].

Like the scatterplot, it counts finished items only, so this wiki notes that it says nothing about open work. See [[flow-metrics]].

## Later uses

The source keeps the chart for later material on classes of service and forecasting (L2776, L2844). This chapter does not carry those techniques.
