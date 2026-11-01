---
title: A Velocity Trend Is Not a Forecast
category: reading-history
summary: Do not project a velocity trend forward; a rise is noted and not planned on, and a decline is a cause to find and remove rather than a rate to plan with.
tags: [rule, velocity, forecast, retrospective]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# A Velocity Trend Is Not a Forecast

A run of rising or falling velocities tempts a planner to extend the line. Cohn refuses in both directions, for different reasons.

## The rule

> many projects have too few iterations for velocity trends to become either apparent or relevant
>
> — [[cohn-agile-estimating-planning]], L4682

- **Upward:** "If I notice what appears to be a trend toward an increasing velocity I am pleased but don’t act on it." Cohn would "never draw a trend line" through his chart and predict a velocity of 20 for the next iteration (L4682).
- **Downward:** "I would figure out and remove the cause of the decline rather than plan on velocity continuing to drop" (L4682).

This wiki reads the asymmetry as the point of the rule: a rise changes nothing in the plan, while a fall changes what is done next. The forecast itself stays in the three values of [[velocity-range-forecast]].

## Reasoning

The stated basis is sample size: a project offers too few points for a slope to mean anything. Planning on a decline has a further cost, which this wiki adds: it accepts the fall as a fact about the future, so nobody asks what caused it.

## Signs of violation

These signs are this wiki's reading of the rule, and each raises a question rather than a verdict; see [[smell-is-not-a-finding]].

- A forecast uses a velocity above any value in the window, or a figure labelled as projected.
- A chart of velocity carries a fitted trend line.
- A plan is cut because velocity is falling, and no cause is recorded.

## Trade-off

If a decline is real and its cause cannot be removed, the eight-iteration mean keeps older, faster iterations for a while and overstates what will come. This wiki notes that the slowest-three figure partly covers this, and that the source does not address it.

## Agent executor note

Cohn's mechanism is the sample size, not human pace, so this wiki reads the rule as surviving an agent executing and a person steering. A step change from a new way of working is a different case from a trend, and this source does not treat it.
