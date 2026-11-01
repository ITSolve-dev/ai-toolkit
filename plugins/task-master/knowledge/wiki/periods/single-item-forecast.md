---
title: Forecasting a Single Item from Cycle-Time Percentiles
category: periods
summary: To forecast one item, epic or project, collect the cycle times of finished items of the same type, pick a percentile, and state the corresponding range with that probability.
tags: [method, estimation, forecasting, cycle-time, percentile, sla]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Forecasting a Single Item from Cycle-Time Percentiles

A **single-item forecast** answers "when will this one thing finish?" by reading a percentile off the recorded cycle times of finished items of the same type. Vacanti calls this "very straightforward" ([[vacanti-actionable-agile-metrics]] L3632) and identifies it with the SLA method of his scatterplot chapter (L3632, L3642), which this wiki keeps on [[service-level-expectation]]. It satisfies [[forecast-range-and-probability]] because the percentile is the probability and the cycle time at that percentile bounds the range.

## Procedure

1. Collect "the Cycle Time data for the all same types of work items" (L3568), as a [[cycle-time-scatterplot]] does.
2. Vacanti's next step: "You will just choose the percentile that you want to attach to your forecast and use the corresponding range." (L3574)
3. State both numbers together. His example is that "a typical work item completes in 43 days or less 85% of the time" (L3580).

## Inputs and where they come from

- **Cycle times of finished items:** board history, read from when an item entered and left the states being measured.
- **Item type:** the board's work types. Type is the discriminator: "If the work items we are interested in were epics or projects, for example, then we would need to capture the Cycle Time data for epics or projects" (L3580). This wiki reads that as a prohibition on forecasting an epic from story history; a percentile from another type answers another question.
- **Percentile:** a choice, not a finding. Vacanti later says "85<sup>th</sup> percentile (or whatever percentile you feel comfortable with)" (L3618). The choice is made as on [[choosing-a-service-level-expectation]].

## Numbers and their conditions

The 43 days at 85% comes from one sample scatterplot of one team's user stories (L3574-L3580). It is an illustration of the form, not a benchmark, and 85% is not given as a recommended level beyond that example.

## What would show it wrong

The source does not state this; the following is the wiki's own check. If materially more than 15% of later items of that type exceed the 85th-percentile value, the history no longer represents the current process and the percentile needs rereading. The precondition is on [[forecast-needs-a-stable-process]].

## Limits

These limits are this wiki's reading, not the source's.

- **Clock start.** A cycle time runs from the start of work, so the method gives a duration once an item starts. A date for an unstarted item also depends on when it will start, which this method does not supply.
- **Few people, little history.** The chapter gives no minimum sample. On a small project with few finished items of a type, the percentile rests on very few points, and the statement should say how many ([[cycle-time-percentile-lines]]).

## Agent executor note

This wiki's reading: the mechanism is an empirical distribution, so it does not depend on human pace and survives an agent executing. It does depend on the history coming from the same way of working: cycle times recorded under human execution, or under a different setup for steering an agent, do not describe the current process.

## See also

[[forecast-range-and-probability]], [[forecast-from-an-average]], [[burn-up-with-percentile-lines]], [[monte-carlo-simulation]]
