---
title: Process Boundaries
category: work-states
summary: Naming where work arrives and departs is the first act of adopting flow metrics, and crossings are counted on the date they happen, whatever an iteration is doing; where each point belongs is settled on started-and-finished-points.
tags: [rule, flow-metrics, wip, arrivals, departures, scrum]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Process Boundaries

Process boundaries are the two points on a workflow at which a work item is counted as having arrived to the process and as having departed from it. Where each point belongs is on [[started-and-finished-points]], and their board form is on [[arrival-point]] and [[departure-point]]. This page holds what Vacanti adds when he tells a team how to begin: name the boundaries first, and count across them on the date it happens. "the very first thing you need to do to get started is define the boundaries of your process" ([[vacanti-actionable-agile-metrics]] L3786).

## The rule

Decide three things, in this order.

1. **The arrival point.** "you must first decide on a point at which you consider work to have entered (or arrived to) your process" (L3786).
2. **The departure point.** The matching point at which work is considered to have exited (L3786).
3. **Which items between them count as WIP.** The choice belongs to the people running the process, and it is meant to be revisited: "make that choice and start tracking. As with anything, you can always tweak that decision later as you learn more" (L3798).

## Why it comes first

The boundaries are what make WIP a countable thing: "any work items between these two boundaries can be considered WIP" (L3786). Without them, the arrival rate, the departure rate and Cycle Time have no defined start or end, so [[flow-metrics]] cannot be read. This wiki reads the same dependency downstream: a [[malformed-cfd]] is often a boundary problem, because the top and bottom lines of the chart are defined as cumulative arrivals and departures (L3904).

## Boundaries are independent of iterations

The boundaries do not move with a sprint. "it is possible for work to arrive at any time during the sprint and it is possible for work to depart at any time during the sprint" (L3788). So: "any time work comes into your process—regardless of whether it is the beginning of a sprint or not—you need to count that work as arrived" (L3788), and the same holds for departure (L3788-L3796). Vacanti acknowledges this "may seem anathema to Scrum purists" (L3788).

This wiki resolves that per setup. Under an iteration setup, the commitment over the period and the counting of flow are two separate things: the period's plan stays on [[timeboxed-iteration]] and on its plan-versus-fact reading, while arrival and departure are recorded on their actual dates. Under a continuous setup there is no conflict to resolve.

## Signs of a violation

The source gives the rule and not its sign. The following signs are this wiki's reading, and each one raises a question to check and is not a finding (see [[smell-is-not-a-finding]]).

- WIP cannot be counted from the board without someone judging which items are in.
- In board history, arrival dates cluster on the first day of a sprint and departure dates on the last day, which suggests that work is being counted at the iteration edge and not at the boundary.
- Two reports of the same period give different WIP or Cycle Time because each assumed a different start point.

## What would show the choice wrong

The source names no test beyond continued tuning. This wiki's reading is that a boundary is badly placed when a large share of items sit long before or after it in a state nobody counts, since that time is then real waiting that no metric sees. The inputs are the workflow states and the time items spend in each, read from board history.

## Trade-off

Any choice excludes something. An early arrival point makes Cycle Time include queueing, and it brings a backlog inside the process ([[backlog-versus-commitment]]). A late arrival point gives shorter numbers and hides that wait. A person steering an agent can accept either, provided the choice is written down.

## Agent executor note

The mechanism here is definitional and does not depend on a human executor, so this wiki keeps the rule unchanged for work done by an agent and steered by a person.

## See also

[[started-and-finished-points]], [[littles-law-assumptions]], [[capturing-flow-data]], [[steps-to-predictability]]
