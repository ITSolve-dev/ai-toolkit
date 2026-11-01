---
title: Actionable Metrics
category: reading-history
summary: A test for whether a metric earns its place; it suggests a specific intervention, it predicts something asked of the project, and it costs little to collect, and a metric that changes no decision over several periods is dropped.
tags: [decision-rule, retrospective-analysis, flow-metrics, audit]
sources: [vacanti-actionable-agile-metrics, kanban-guide]
created: 2026-11-02
updated: 2026-11-02
---

# Actionable Metrics

This test decides whether a project, or the plugin reporting on it, should keep a metric. Vacanti defines the class:

> Actionable Metrics for Predictability: The set of metrics that will suggest specific interventions that will result in the outcomes you are expecting.
>
> — [[vacanti-actionable-agile-metrics]], L462

## The test

A metric stays if it passes all three. The criteria are the source's, and their combination into a keep-or-drop test is this wiki's.

1. **It suggests an intervention.** The source's definition above. Its negative example is the advice left once traditional metrics run out: “Work Harder”, “Estimate Better”, “Plan Better”, “Hope”, “Pray”, “Cry” (L482).
2. **It predicts something asked of the project, or informs a decision.** The source cites Eric Ries (spelled "Reis" in the text): "The only metrics that entrepreneurs should invest in are those that help them make decisions." It then cites Troy Magennis: "If a metric does not offer predictive power, then capturing that metric is waste." (L470).
3. **It is cheap to collect.** "There is no point in tracking a metric if it is going to bankrupt you to do so." (L472). For this base, this wiki reads a metric that needs someone to keep it up as failing here, since the charter puts logged hours out of scope.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The metric's values over recent periods | Board history |
| What was decided after it moved | Board history, or an answer from the people steering |
| What it takes to produce | Whether it follows from state-change timestamps or needs someone to enter it |

Keeping a metric was wrong if it is reported across several periods and no decision changes. Dropping one was wrong if, after a missed date, its history shows it had moved in time to act. These two tests are this wiki's, and no source states them.

## Do not take the source's word for its own metrics

The author applies the test to his own metrics and says they pass: "By definition, then, tracking these metrics offer predictive power and will help us make better decisions." (L470). This wiki does not accept that as evidence. The argument rests on his having "suggested" that these metrics answer customers' questions, so the conclusion restates the premise. WIP in particular passes only once a project has a stated bound, because "too big" (L440) triggers nothing without one. The same test applies to [[flow-metrics]] as to velocity.

## Cost

Dropping a metric breaks its history, so a later comparison has nothing to read. A metric also needs a few periods before it can be judged, so the test cannot fairly be run on a new one.

## Positions

The [[kanban-guide]] states the same limit in its own terms: the metrics are "meaningless unless they can inform one or more of the three Kanban practices" ([[flow-metrics]], quoting the Guide at its L168). [[smell-is-not-a-finding]] applies the same caution to signs.

## Agent executor note

The test concerns the metric and the decision, so it survives. An agent adds one risk: it can produce any number of metrics at no effort, which removes the cost criterion as a natural brake. This wiki reads criterion 1 as what must hold the line in that case.
