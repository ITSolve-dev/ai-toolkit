---
title: Which Chart for Which Plan Question
category: showing-work
summary: Choose the view by the question, the setup and the reader. Plan questions — iteration burndown for finishing this period, release burndown and velocity for overall progress and forecast, the bar chart for why, a parking lot chart for which themes, a feature Gantt for allocation, a planned-versus-earned table for what happened. Cycle time questions — a CFD for averages, a scatterplot with percentile lines for one item's time and for change over time, a histogram for shape, and neither for open work; a set of items by a date goes to Monte Carlo. Points-based views stay with the people steering; outside readers get time or count.
tags: [decision-rule, visualization, burndown, velocity, gantt, cycle-time, flow-metrics]
sources: [cohn-agile-estimating-planning, vacanti-actionable-agile-metrics]
created: 2026-11-01
updated: 2026-11-02
---

# Which Chart for Which Plan Question

Cohn uses each plan view for a different question and audience, and Vacanti's views of [[cycle-time]] answer different questions again. Picking the wrong one either hides the answer or invites a reading the chart cannot support. This page holds both choices: the plan views of an iteration and release setup, and the cycle time views of history.

## Inputs, and where each is read from

This list is this wiki's, since neither source states the inputs of the choice.

| Input | Read from |
|---|---|
| The question being asked | The request itself |
| The setup: iterations or flow, and whether the project estimates in points | Project configuration |
| The reader: the people steering, or someone outside the project | The request |
| Whether a dated answer is needed, and for one item or a set | The request |
| Enough finished items for a shape | Board history; the sources give no count |

**What would show a choice wrong.** Readers ask a question the chosen view cannot answer (the "cannot ask" column below), or an answer depended on something the view collapses. Two later facts of the second kind: a period reported healthy from a histogram, while the scatterplot for the same dates shows a rising trend; or a forecast given from finished items, while open items already older than the top line turn up later.

## Plan questions (iteration and release setup)

The first two columns follow Cohn. Audiences follow Cohn for the first three rows and are this wiki's for the rest. The "cannot ask" column is this wiki's reading.

| Question | View | Audience and rhythm | Cannot ask |
|---|---|---|---|
| Will we finish this iteration's work? | [[iteration-burndown]] | Team, daily ([[cohn-agile-estimating-planning]] L4575) | Whether what is finished is what was wanted |
| How far along is the release? | [[release-burndown-chart]] (L4641) | Stakeholders and participants, over the release (L4575) | Why the work moved, or what was learned and what risk was retired |
| Why did remaining work move? | [[release-burndown-bar-chart]] | A team past the simpler line chart, whose members do not argue over which side a change belongs on (L4402) | Completion apart from re-estimation |
| Which themes of the release are behind? | [[parking-lot-chart]] | Anyone wanting "a high-level view" (L4435) | Which tasks are done, or the trend |
| How much will fit by a date, or when does this finish? | Velocity chart with the three values ([[velocity-range-forecast]], L4649-L4678) | Product owner and team | Which features will land |
| What is planned for which iteration? | Feature-level Gantt ([[gantt-at-feature-level]]) | Anyone reading the plan | How far along anything is |
| What did we plan and what happened? | Story table ([[iteration-summary-plan-versus-fact]]) | Those reviewing the iteration | Anything forward-looking |

**Condition on the audience column.** A view in points (the burndowns, the parking lot, the velocity chart) goes to the people steering. Anything for a reader outside the project is converted to elapsed time or item count first, per [[points-or-time-and-count]], which has a burndown in points converted before it goes outside. This condition is this wiki's; Cohn's audiences assume points throughout.

**Flow setup.** A project with no iterations and no points has no burndown or velocity to draw. Its forecast questions go to the cycle time views below and to [[throughput-monte-carlo]].

### Reasoning

Cohn's stated purpose for the daily view is that team members "see daily variations in the burndown chart so that they can make adjustments in order to complete all the work of the iteration" (L4575). Over a release, the need is "insight into progress against and revisions to the release plan" (L4575).

> Progress on a release burndown chart is a function of the amount of work remaining and the velocity of the team.
>
> — [[cohn-agile-estimating-planning]], L4641

> Burndown charts are the primary method for communicating about progress but they are often accompanied by a chart showing the development team’s velocity per iteration.
>
> — [[cohn-agile-estimating-planning]], L4791

Cohn says the finish can be read "just by looking at the burndown chart" (L4336), and that the chart "tells us when the project is likely to finish if all factors affecting the project remain unchanged" (L4340). This wiki reads that as saying remaining work alone yields only a point date under "nothing changes"; a date that can be promised needs the velocity range ([[velocity-range-forecast]]).

## Cycle time questions (history, any setup)

The [[cycle-time-scatterplot]] and its histogram form hold the same data. The source keeps both because of what each hides:

> The Scatterplot is a temporal view of data that can show trends of dots over time. A Histogram is a condensed, spatial view based on the frequency of occurrence of Cycle Times.
>
> — [[vacanti-actionable-agile-metrics]], L2824

> Looking at the Scatterplot in Figure 10.1 it may not be obvious that the shape of the data is that in Figure 10a.1. Likewise, looking at the Figure in 10a.1 you may not be able to detect any patterns of Cycle Times over a given timeline.
>
> — [[vacanti-actionable-agile-metrics]], L2824

The first two columns follow the source for the first four rows. The last two rows and the "cannot ask" column are this wiki's reading.

| Question | View | Cannot ask |
|---|---|---|
| How long do items take on average? | [[cumulative-flow-diagram]] (L2586) | How long this one item may take, or at what probability |
| How long may one item take, at what probability? | Scatterplot with [[cycle-time-percentile-lines]] (L2650-L2664) | Whether the coming items resemble the past ones |
| Did cycle time change over this period? | Scatterplot, for its timeline (L2824) | Why it changed |
| What shape does the data have, and how long is the tail? | Histogram with the same percentile lines (L2822-L2824) | When any of it happened |
| How many items by a date, or when will this set finish? | [[throughput-monte-carlo]] (L1484; the question as framed at L3622) | How long any one item takes |
| What is open now, and how old is it? | Neither: [[work-item-age]], read against the same percentile lines | Anything, since both views count finished items only |

The source's reason for leaving averages behind is the single-item case: a completion date is its example of when an average is not good enough (L2586). This wiki reads that as: a date for a single item comes from a line, stated with its probability. A question about a whole set of items by a date is a different one, which a per-item line does not answer. See [[service-level-expectation]], which is per item, and [[forecast-range-and-probability]].

### Which holds under which setup

This wiki's resolution, on the source's position:

- **Flow setup:** the scatterplot is the default view for questions about one item; questions about a set by a date go to [[throughput-monte-carlo]].
- **Iteration setup:** the plan questions above come first. The scatterplot is required for the test on [[iteration-length-versus-cycle-time]], since the [[siemens-hs-case]] ran 30-day sprints against an 85th percentile of 71 days (L4078), and optional for the other questions.
- **Few finished items, any setup:** prefer the scatterplot and read individual dots, because a histogram's shape needs volume that a small board does not have.

## Failure modes

These are this wiki's readings.

- Reading progress off a Gantt chart: the bars are full-length by construction.
- Sending a forecast as one point drawn from a burndown. See [[forecast-range-and-probability]].
- Sending many views at once. See [[status-buried-in-a-long-report]].
- Sending a points-based view to a reader outside the project. See [[points-or-time-and-count]].
- Reporting only a histogram, which hides a drift in time.
- Reporting only an average, which hides the tail and the spread.
- Using a cycle time view to judge open work, when it can only show that work after it closes.

## Caution

Cohn's sample iteration burndown uses hours on its vertical axis (L4750). The charter excludes tracking spent hours, so this wiki reads the chart's question as usable and its unit as this source's choice. A burndown built here would need a unit the board already holds, as [[iteration-burndown]] proposes.

See also [[flow-metrics]].
