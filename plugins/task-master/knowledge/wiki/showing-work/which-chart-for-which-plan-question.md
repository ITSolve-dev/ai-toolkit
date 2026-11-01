---
title: Which Chart for Which Plan Question
category: showing-work
summary: Choose the view by the question; iteration burndown for finishing this period, release burndown and velocity for overall progress and forecast, the bar chart for why, a parking lot chart for which themes, a feature Gantt for allocation, and a planned-versus-earned table for what happened.
tags: [decision-rule, visualization, burndown, velocity, gantt]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Which Chart for Which Plan Question

Cohn uses each plan view for a different question and audience. Picking the wrong one either hides the answer or invites a reading the chart cannot support.

## The choice

The first three columns follow Cohn. The "cannot ask" column is this wiki's reading.

| Question | View | Audience and rhythm | Cannot ask |
|---|---|---|---|
| Will we finish this iteration's work? | [[iteration-burndown]] | Team, daily ([[cohn-agile-estimating-planning]] L4575) | Whether what is finished is what was wanted |
| How far along is the release? | [[release-burndown-chart]] (L4641) | Stakeholders and participants, over the release (L4575) | Why the work moved, or what was learned and what risk was retired |
| Why did remaining work move? | [[release-burndown-bar-chart]] | A team past the simpler line chart, whose members do not argue over which side a change belongs on (L4402) | Completion apart from re-estimation |
| Which themes of the release are behind? | [[parking-lot-chart]] | Anyone wanting "a high-level view" (L4435) | Which tasks are done, or the trend |
| How much will fit by a date, or when does this finish? | Velocity chart with the three values ([[velocity-range-forecast]], L4649-L4678) | Product owner and team | Which features will land |
| What is planned for which iteration? | Feature-level Gantt ([[gantt-at-feature-level]]) | Anyone reading the plan | How far along anything is |
| What did we plan and what happened? | Story table ([[iteration-summary-plan-versus-fact]]) | Those reviewing the iteration | Anything forward-looking |

## Reasoning

Cohn's stated purpose for the daily view is that team members "see daily variations in the burndown chart so that they can make adjustments in order to complete all the work of the iteration" (L4575). Over a release, the need is "insight into progress against and revisions to the release plan" (L4575).

> Progress on a release burndown chart is a function of the amount of work remaining and the velocity of the team.
>
> — [[cohn-agile-estimating-planning]], L4641

> Burndown charts are the primary method for communicating about progress but they are often accompanied by a chart showing the development team’s velocity per iteration.
>
> — [[cohn-agile-estimating-planning]], L4791

This wiki reads the pairing as necessary: remaining work alone does not yield a date, and [[velocity-range-forecast]] supplies the rest.

## Failure modes

- Reading progress off a Gantt chart. This wiki notes that the bars are full-length by construction.
- Sending a forecast as one point drawn from a burndown. See [[stating-plan-uncertainty]].
- Sending many views at once. See [[status-buried-in-a-long-report]].

## Caution

Cohn's sample iteration burndown uses hours on its vertical axis (L4750). The charter excludes tracking spent hours, so this wiki reads the chart's question as usable and its unit as this source's choice. A burndown built here would need a unit the board already holds, as [[iteration-burndown]] proposes.

See also [[flow-metrics]].
