---
title: Iteration Length Versus Cycle Time
category: periods
summary: Compare a period's length with Cycle Time percentiles to learn the chance a story started on day one finishes inside it; if the 85th percentile exceeds the period, the period's commitment is not credible as stated.
tags: [decision-rule, iteration, cycle-time, percentiles, commitment]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Iteration Length Versus Cycle Time

This test compares a period's length with the observed Cycle Time distribution, to find out whether stories can fit in the period at all. It reads a commitment against history without any estimate.

The [[siemens-hs-case]] ran 30-day sprints against a 50th percentile of 21 days and an 85th percentile of 71 days:

> That means that any story that started at the beginning of a sprint had little better than 50% chance of finishing within the sprint.
>
> — [[vacanti-actionable-agile-metrics]], L4078

The source adds that 71 days "is 2.5 sprints" (L4078). Teams at Siemens were still "challenged to plan and complete stories in time-boxed sprint increments" (L4020-L4026), despite mature planning practice.

## The rule

If the 85th percentile of Cycle Time exceeds the period length, treat a commitment to finish stories inside the period as unsupported, and act on the distribution before planning harder. The 85th percentile is this wiki's working choice, following Siemens' own use of it for commitments (L4214); the chapter does not state this threshold for a period.

## Inputs and where they are read

- Period length, from the project setup.
- Cycle Time percentiles, from board history; see [[cycle-time-scatterplot]] and [[cycle-time-percentile-lines]]. They need the same start and finish points as the period's counting ([[started-and-finished-points]]).
- When in the period items start. This wiki notes that a story started mid-period has less time, so the source's day-one figure is a ceiling on the chance.

## What would show the choice wrong

Stories planned into a period finish inside it at a rate clearly above what the percentiles predict. This would mean the history is unrepresentative, for example because it mixes item kinds.

## What to do when it fails

The source's route is to reduce WIP, which lowers the distribution itself; see [[reduce-wip-before-raising-throughput]]. Cutting items smaller ([[hidden-wip-in-large-items]]) and changing the length ([[period-length]]) are the other levers; the source does not treat them here. Even after the change Siemens' 85th percentile was about 40 days (L4286), still above 30, which suggests in this wiki's reading that the improved process would still fail this test for a 30-day period. The chapter does not address this.

## Trade-offs

This wiki reads the cost as replacing a promise with a likelihood, which stakeholders who want a yes may find unsatisfying. Lengthening a period to fit the distribution also delays feedback. See [[commitment-over-a-period]] and [[estimate-versus-commitment]].

## Setting and transfer

The figures come from a large program with long dependencies, where a 30-day sprint was standard. This wiki reads the test itself as arithmetic that holds at any scale, given enough finished items to make the percentiles meaningful ([[how-much-flow-data]]).

## Agent executor note

This wiki's reading: with an agent executing, the Cycle Time compared must include the wait for a person's review, or the period will look easier to fill than it is.
