---
title: Cycle Time
category: reading-history
summary: Cycle Time is the elapsed time a work item spends as WIP; it is measured in calendar time rather than active time because customers think in dates and most unpredictability sits in the waits, and names like Lead Time only mean anything once boundaries are stated.
tags: [concept, cycle-time, lead-time, flow, metrics, estimation, vacanti]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Cycle Time

Cycle Time is "The amount of elapsed time that a work item spends as Work In Progress" ([[vacanti-actionable-agile-metrics]] L652). It answers the customer's "When will it be done?" (L640) and is one of the [[flow-metrics]]. The definition comes from Hopp and Spearman's *Factory Physics* (L654) and depends entirely on [[work-in-progress]]: the clock starts and stops at the [[started-and-finished-points]].

Vacanti's point in tying it to WIP is that the arbitrariness goes away: "you essentially have control over when something is counted as Work In Progress in your process" (L654). A team sets those policies and runs its clock from them.

## Elapsed, not active

The rule that distinguishes this definition: count calendar time, not time spent working. The source says most other methodologies ask for active time only, and rejects that (L658-L664), for two reasons.

1. **Customers read dates.** The source's example: on March 1 a customer is told 30 days and expects the item "on or before March 31", while a team that meant business days expects to deliver "sometime around the middle of April" (L666).
2. **Active time hides the problem.** "It is the time that an item spends waiting or delayed (i.e., _not_ actively being worked) that is usually where most of your unpredictability lies." (L668) Measuring only active time removes what most needs examining.

**Sign:** a cycle-time figure in working days or hours, or one derived from logged effort. This also collides with the charter, which excludes logged hours: time a task lived is read from board history, and elapsed time is what that history provides.

## Why track it

Beyond answering "when", which feeds forecasting in the source's Chapter 14 (L694), the source gives three reasons.

- **A predictor of cost.** "Very generally speaking, the longer something takes to complete the more it is going to cost." (L696) The source hedges this itself.
- **The length of the feedback loop.** The source ranks this above cost: value is determined by the customer, so "Shortening Cycle Time will shorten the customer feedback loop." (L704) The failure it guards against is building something the customer does not need, slowly.
- **A view of process health**, via [[flow-efficiency]] (L706).

## Lead Time versus Cycle Time

The Kanban community mostly says Lead Time where Vacanti says Cycle Time (L672). His argument that matters here is that neither name carries its own boundaries: "one person’s Lead Time is another person’s Cycle Time and vice versa" (L680). His example is that the development team's Lead Time is just the Product Manager's Cycle Time through the development phase (L680). Lead Time suggests end-to-end, but what end-to-end means must still be defined (L680). Hopp and Spearman's alternative is Flow Time, which Vacanti says may communicate the meaning better (L692).

This wiki resolves the disagreement per setting by ignoring the label: when two sources or reports use these terms, compare their start and stop events, and use a figure only with those events stated. In this wiki Cycle Time means the elapsed time between a project's started and finished points. That is Vacanti's definition and the Kanban Guide's ([[flow-metrics]]). Cohn's cycle time is the same clock with its end fixed at delivered value ([[wip-lengthens-cycle-time]]), which is a choice of finished point and not another measure.

## What it is related to

[[wip-lengthens-cycle-time]] gives the mechanism by which open work lengthens it, and [[littles-law]] the relation of its average to the averages of WIP and Throughput. The chapter does not say how to summarize many items' cycle times, and a single figure is not its claim. The forecast built on this history is [[service-level-expectation]].

## Agent executor note

The definition and both reasons for elapsed time survive, since customers still read dates and waits still count. This wiki qualifies the cost claim: its mechanism is that time spent is paid for, which fits people working. With an agent executing, much of the elapsed time is likely to be queue and review, which costs little by the clock, so elapsed time is a weaker proxy for cost there. The feedback argument gets stronger, in this wiki's reading, because it does not depend on who did the work.
