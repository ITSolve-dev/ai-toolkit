---
title: Reduce WIP Before Raising Throughput
category: moving-work
summary: When Cycle Time is too long, cut work in progress before adding hours or capacity, because added capacity usually raises WIP faster than it raises Throughput.
tags: [decision-rule, wip, throughput, littles-law, capacity]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Reduce WIP Before Raising Throughput

This rule chooses between the two levers a simplified reading of [[littles-law]] leaves open when Cycle Times are too long: decrease WIP, or increase Throughput. The source's position, in the [[siemens-hs-case]], is that the first comes first.

> The problem with trying to impact Throughput in these ways is that most organizations actually end up increasing WIP faster than they increase Throughput.
>
> — [[vacanti-actionable-agile-metrics]], L4090

The levers it means are longer hours, mandatory weekends, borrowed staff and hiring (L4090). The source calls cutting WIP the "much more sensible and economical" choice (L4092). Siemens' managers reached the same view from the other direction: the overtime "may actually have been elongating the release completion date" (L4034). Overtime as a people practice is out of scope here, and only its flow effect is kept. Starting more items in place of adding capacity is the neighbouring failure on [[starting-more-work-when-cycle-time-is-long]].

## The rule

When Cycle Time is too long or rising, check whether work is entering faster than it leaves. If it is, stop starting work and hold a limit. Do not add capacity to a system that is already over-started.

## Inputs and where they are read

- Cycle Time percentiles and their trend, from board history; see [[cycle-time-scatterplot]].
- Arrival and departure rates, from the two boundary lines of a [[cumulative-flow-diagram]] or from counts of starts and finishes in history; see [[measuring-arrival-and-departure-rates]].
- Current open item count, from board state.

## What would show the choice wrong

The limit is held, arrivals match departures, and Cycle Time keeps growing or Throughput falls sharply. Then this wiki reads the constraint as sitting elsewhere: read [[bottleneck-on-the-cfd]] and the items themselves. Siemens' result was stabilization after limits; the chapter does not show a case where limits failed, so it offers no counter-example.

## Reasoning

The relation is the arithmetic of average WIP, Throughput and Cycle Time, so it holds at any team size, within the assumptions of [[littles-law]]. If WIP rises faster than Throughput, average Cycle Time rises (L4090). This wiki reads the practical step as follows: adding a person or a resource often adds new starts first and output later. How firm the direction is, given that the law fixes a relation and not a result, is on [[starting-more-work-when-cycle-time-is-long]].

This does not mean capacity never matters. Once flow was stable, Siemens did add capacity, and in a specific place: test automation, where the chart showed the shortfall (L4192), and a Tester instead of two Programmers in a what-if (L4224). This wiki reads the order as the rule: limit first, then add capacity only at the constraint the charts expose.

## Trade-offs

Stopping starts means visibly unstarted requests and people or agents with nothing new to do. It also goes against habit: at Siemens "mandating limits on work went against the grain of the then current beliefs" (L4100). See [[utilization-versus-slack]].

## Agent executor note

The transfer here is this wiki's own, and it is conditional. Launching another agent is the modern form of adding staff. It raises WIP at once. If a person's review is the constraint it adds nothing to Throughput, and the rule holds as stated. If execution is the constraint, parallel runs may raise Throughput for a while, as [[starting-more-work-when-cycle-time-is-long]] notes, and the failure appears only once review saturates. So the input to check first is where finished work is waiting. The source's figures do not transfer in either case.
