---
title: Steps to Predictability
category: reading-history
summary: Vacanti's four-step summary of the book; set policies on Little's Law's assumptions, collect WIP, Cycle Time and Throughput, visualize them, and act on the analytics.
tags: [method, flow-metrics, predictability, policies]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Steps to Predictability

The closing summary of *Actionable Agile Metrics for Predictability* compresses the book into a four-step loop: set policies, collect data, visualize it, act on it ([[vacanti-actionable-agile-metrics]] L3930-L3962). Its goal is an answer to the question "When will it be done?" (L3964); see [[predictability]].

## The steps

1. **Set process policies** "based on the assumptions of Little’s Law—including policies around how you define the boundaries of your process" (L3932). Do not start work faster than old work finishes, do not let items age arbitrarily, and minimize work that is started and never finished (L3934-L3938). See [[littles-law-assumptions]], [[process-policies-from-littles-law]] and [[process-boundaries]].
2. **Collect the basic metrics of flow** as the process runs: Work In Progress, Cycle Time, Throughput (L3940-L3946). See [[capturing-flow-data]] and [[flow-metrics]].
3. **Visualize them** in Cumulative Flow Diagrams and in Cycle Time Scatterplots and Histograms (L3948-L3950). See [[cumulative-flow-diagram]], [[cycle-time-scatterplot]], [[cycle-time-histogram]] and [[verifying-tool-flow-analytics]].
4. **Use the analytics to take action:** "Intervene when your process goes awry", "Identify improvements to policies to improve performance", and "Make forecasts" (L3952-L3962). See [[percentile-intervention-triggers]], [[actionable-metrics]] and [[forecast-range-and-probability]].

## Why the order matters

The source lists the steps without arguing for the sequence. This wiki reads it as a dependency chain, since each step consumes the one before: metrics are undefined without boundaries, a chart inherits the faults of its data ([[board-misuse-corrupts-flow-data]]), and an action or forecast inherits the faults of its chart.

The sign of a skipped step, in this wiki's reading, is a chart or forecast nobody can trace back to a stated boundary or to per-state dates. That raises a question to check; see [[smell-is-not-a-finding]].

## What is not kept

The source says "I promise that you will be predictable" (L3964). This wiki drops that as an assertion with no mechanism, so the page's weight rests on the individual steps.

The source's other point is about timing: "any delay in implementing these principles severely hampers your ability to be predictable" (L3966). This wiki reads the usable part as [[how-much-flow-data]]: starting does not have to wait for a large sample.

## Agent executor note

This wiki's reading: the loop does not depend on a human executor. For the plugin, its first three steps are preparation of material and the fourth is the person's call: charts can flag a problem, and the decision to intervene stays with whoever steers.

## See also

[[good-plan-test]], [[diagnosing-unfinished-work]], [[what-may-move]], [[siemens-hs-case]]
