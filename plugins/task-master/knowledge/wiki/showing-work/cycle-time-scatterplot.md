---
title: Cycle Time Scatterplot
category: showing-work
summary: A chart with one dot per finished item, placed at its finish date and its cycle time; it shows each item's time rather than an average, gives percentiles, the trend across a period and outliers to investigate, and says nothing about work still open. Its condensed form, the cycle time histogram, shows the distribution's shape (usually a hump on the left and a long right tail) at the cost of all information about when.
tags: [concept, visualization, cycle-time, flow-metrics, board-history, histogram]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Cycle Time Scatterplot

A cycle time scatterplot is a chart with one dot per finished work item: the X-axis is the process timeline, and the Y-axis is the item's [[cycle-time]] ([[vacanti-actionable-agile-metrics]] L2616, L2620). The source introduces it as the step past averages: a [[cumulative-flow-diagram]] gives a good idea of how long items take "_on average_", but "there are going to be times when doing analysis based solely on average is not going to be good enough (things like forecasting a completion date come to mind, for example)" (L2586).

This page says what the chart and its histogram form are, and how one organization used it. For the choice between this chart and its neighbours, see [[which-chart-for-which-plan-question]]. For reading its shapes, see [[reading-a-cycle-time-scatterplot]].

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

Left alone, the chart is "a random set of dots" (L2632). The structure comes from [[cycle-time-percentile-lines]], drawn across it. The same data, condensed by frequency, is the histogram below.

The source says a scatterplot can carry other metrics too, such as throughput or bugs per feature, and that in this book the unqualified word means the cycle time version (L2598).

## The histogram form

A cycle time histogram is a chart of frequency against cycle-time ranges: each bar counts how many finished items fell into that bin (L2782, L2804). The source says histograms are "really just another view of the same data shown on a Scatterplot" (L2776), so it holds nothing the scatterplot does not. What it adds is a view of the shape.

The source treats histograms as an advanced topic and says "you need not master this analysis to be successful with the predictability concepts presented in this book" (L2774). This wiki reads that as a reason to treat the chart as optional for a single item's forecast: a project with a scatterplot and percentile lines loses nothing it needs to state one item's time and probability. The source keeps histograms for "Forecasting" (L2776) and "forecast modeling techniques" (L2844), and reads simulation output as a histogram (L3300; [[throughput-monte-carlo]]), so the chart is not optional where a simulation's result is shown.

**How it is built.** Go through each data point and increment the bin whose range it falls in (L2804). The vertical axis is frequency, the horizontal axis the ranges (L2796, L2804). Percentile lines can be placed on it as on a scatterplot (L2822).

**The usual shape.**

> That is to say Histograms in our world usually have a big hump on the left and a long tail to the right.
>
> — [[vacanti-actionable-agile-metrics]], L2796

Why that shape occurs, and whether it is log-normal, Weibull or something else, the source declares "beyond the scope of this introductory book" (L2796). It claims only that "Knowing this shape can give you some insight to the problem areas of your process" (L2796) and that deep analysis is possible.

This shape is the source's ground for rejecting mean-and-deviation charts ([[pseudo-control-chart]]). The chapter asserts the shape and does not offer data for it beyond an example figure, so this wiki grades it as a practitioner's general observation, and notes that a project can check it against its own history in one chart.

This wiki reads two practical consequences. In a long right tail, the mean sits above the point most items reach, so an average overstates the typical item while still understating the slowest ones. And a report needs at least one high percentile, since the tail is where the surprises live. The same right-skewed shape, for one task's duration, is on [[completion-time-distribution]].

**More data, a sharper picture.** The source illustrates with four six-sided dice, summing each roll into bins from 4 to 24, at 10, 100 and 5000 trials: "as the number of trials increases, the shape of the distribution sharpens" (L2806-L2818). Its lesson comes with a limit: "more data is usually better than less data when it comes to visualization (but do not be fooled into thinking you need massive amounts of data to be successful with a statistical approach)" (L2818).

This wiki adds two cautions. The dice illustrate sharpening and not the shape of cycle times, since a sum of dice does not have a long tail. And the source gives no count at which a shape can be trusted. On a small board, a histogram of a dozen items mostly shows the choice of bins, so there a scatterplot serves better.

**What it cannot ask.** The source: "looking at the Figure in 10a.1 you may not be able to detect any patterns of Cycle Times over a given timeline." (L2824). This wiki reads that as a consequence of collapsing time: a process that got slower looks the same as one that was always mixed. Like the scatterplot, it counts finished items only, so this wiki notes that it says nothing about open work. See [[flow-metrics]].

**Later uses.** The source keeps the chart for later material on classes of service and forecasting (L2776, L2844). This chapter does not carry those techniques.

## How Siemens HS used it

The Siemens case ([[vacanti-actionable-agile-metrics]]) used the chart in three ways.

**Percentiles.** The plot for the release before Kanban showed "50% of all stories finished in 21 days or less" and "85% of stories were finishing in 71 days or less" (L4078). Comparing these with the sprint length is the test on [[iteration-length-versus-cycle-time]]. A percentile is not a bound. The chapter itself slips, saying a release "yielded Cycle Times of 43 days or less" (L4154) when it means the 85th percentile. This wiki reads that as a warning for any report: keep the likelihood attached ([[forecast-range-and-probability]]).

**The trend.** Siemens' pre-Kanban release showed Cycle Times "getting longer and longer and longer" (L4078), and the source calls this "not a picture of a very predictable process" (L4088). A flat band after a change was its sign of stabilization (L4126-L4132). See [[conservation-of-flow]].

**Outliers.**

> By using the Scatterplot, teams could clearly see stories whose Cycle Time exceeded normal ranges, perform root cause analysis and take steps and actions to prevent recurrence.
>
> — [[vacanti-actionable-agile-metrics]], L4192

This wiki reads the procedure as taking the items above the agreed percentile, reading each one's history, naming a cause, and recording it for retrospective analysis. The chapter does not define "normal ranges". [[reading-a-cycle-time-scatterplot]] says which items are worth the look.

## What it cannot ask

This wiki reads four limits from the construction.

- **Open work is invisible.** A dot appears only when an item finishes, so an item that has been open for months contributes nothing until it closes. The chart lags in exactly the case that matters, as [[flow-metrics]] says of cycle time generally. Age of open work has to be read separately ([[work-item-age]]).
- **Start dates are hidden.** Position on the X-axis is the finish date, so two dots side by side may have started far apart.
- **It carries no cause.** A dot high on the chart says an item took long and does not say why. It raises a question; see [[smell-is-not-a-finding]].
- **It says nothing about value.** A dot records that an item finished, not whether the finish was useful.

## Not a Control Chart

The source insists that this chart is neither a Control Chart nor a Run Chart (L2766). It has no objection to Run Charts as such (L2720). The chart usually sold under the first name is the defect on [[pseudo-control-chart]].

## Read from history

This wiki notes that the chart needs only the started and finished timestamps of finished items, so it comes from board history without logged hours, measured against the project's [[started-and-finished-points]].

## Agent executor note

This wiki's reasoning, unmeasured: the construction is timestamps and counts, so it survives an agent executing. A few people steering an agent produce few dots, and there the dots themselves are the useful reading, since each can be opened and checked, and percentiles are rough ([[how-much-flow-data]]); Siemens' percentiles rest on many stories from one large program. An agent-run item's dot includes the time its result waited for a person, so a high dot may be a review delay and not an execution problem. A change in how work is executed makes older dots incomparable.
