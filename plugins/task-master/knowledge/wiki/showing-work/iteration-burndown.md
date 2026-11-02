---
title: Iteration Burndown
category: showing-work
summary: A chart of hours remaining by day within an iteration, summed from the board once a day. Cohn finds it useful for iterations of two weeks or longer and unnecessary for one-week ones, where the trend arrives too late.
tags: [method, visualization, burndown, iterations, retrospective]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Iteration Burndown

An iteration burndown is the chart for one question: at today's rate of change in remaining work, will this iteration's selection finish? Cohn defines it plainly: it "plots hours remaining by day" ([[cohn-agile-estimating-planning]] L4506), and the summary puts hours remaining on the vertical axis and the iteration's days on the horizontal one (L4549). It differs from a [[release-burndown-chart]] by covering "only the work of the current iteration" (L4549).

## How to build it

"To create an iteration burndown chart, simply sum all of the hours on your task board once per day and plot that on the chart." (L4515). The input is the remaining estimate on each open item, totalled by row ([[distinguishable-work-states]]). So the chart is only as honest as the discipline in [[overrun-triggers-a-recut]].

## When it earns its place

Cohn's condition is the iteration's length:

> If you’re using one-week iterations, it probably isn’t necessary. By the time a trend is visible on an iteration burndown chart, a one-week iteration will be over.
>
> — [[cohn-agile-estimating-planning]], L4502

He reports the chart as "extremely useful with iteration lengths of two weeks or longer" (L4506). This wiki reads the condition as a general one: the chart earns its place only if a trend can show while there is still time to act on it. Cohn gives the two lengths and not the general form.

## What it cannot answer

The points below are this wiki's reading of how the chart is built.

- **Why the line moved.** Remaining rises when an estimate is corrected, and falls when a card is dropped from To Do in a swap ([[bug-allocation]]). The line alone cannot separate work done from work reassessed or removed.
- **Whether the remaining figure is right.** It sums estimates, so a stale board draws a calm line.
- **Which task is in trouble.** A row total or age of open work answers that, and [[work-item-age]] covers age.
- **Anything about the period's goal.** A selection can be burning down while the goal slips ([[mid-period-change]]).

## Failure modes

- **Flat line with tasks finishing.** Sign: tasks reach done while the total barely falls. This wiki reads that as remaining estimates being raised or work added at the same rate, and the question to ask is which.
- **Line that drops only at the end.** Sign: no change for most of the period, then a fall. This wiki reads that as a board updated in a batch, or work that finishes all at once, since a task's estimate can't fall until someone updates it.

## Agent executor note

Hours are the weak part. Cohn's input assumes someone restating hours remaining each day, and this wiki reads hours as meaning little for an agent run. This wiki's untested proposal is to sum the remaining size steps of unfinished tasks, read from board state, which needs nobody to keep anything. The chart's single daily sample also assumes tasks that live for days. With agent-executed tasks that finish within a day, the same length-of-period reasoning may rule the chart out for short periods. Nothing in this source tests either point.

## Which holds under which setup

The resolution is this wiki's.

- **Iteration setup, two weeks or longer:** draw it, from board state.
- **Iteration setup, one week:** probably unnecessary (Cohn, L4502). This is a hedged judgement that the chart is not worth drawing, not a defect, so a burndown kept for one-week iterations is not a finding. The question to raise is whether a trend arrived in time to act.
- **Flow setup:** there is no period total to burn down, so the question does not arise, and age of open work against an expectation does that job ([[service-level-expectation]]).
