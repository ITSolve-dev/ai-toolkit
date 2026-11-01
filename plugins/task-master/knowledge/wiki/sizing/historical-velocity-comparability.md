---
title: When Historical Velocity Can Be Reused
category: sizing
summary: Past velocity carries over only when little has changed; seven questions test it, and any no means either setting the history aside or widening its range to 60-160%.
tags: [decision-rule, velocity, history, release-planning]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# When Historical Velocity Can Be Reused

A team's past [[velocity]] predicts the next project only to the degree the two situations match. Cohn says historical values are "of the greatest value when very little has changed between the old project and team and the new project and team", and "Any personnel or significant technology changes will reduce the usefulness of historical measures of velocity" ([[cohn-agile-estimating-planning]] L3608).

## The test

Ask of the old and new situation whether each is the same (L3610-L3622):

- Technology
- Domain
- Team
- Product owner
- Tools
- Working environment
- The people who made the estimates

## Decision

| Answers | Action | Source |
|---|---|---|
| All yes, typically a new release of the product the team just worked on | Use the history, still as a range: mean plus or minus a few points, or best and worst iterations over two or three months | L3624 |
| Any no | "think twice", or keep the history and widen it: prior-release mean times 0.6 and 1.6 | L3626-L3634 |

Worked example: 150 points over ten iterations is a mean of 15, which becomes 9-24 (L3626-L3634). The multipliers and their limits are on [[cone-of-uncertainty]].

The source does not say how many nos should rule the history out altogether. This wiki reads that as a judgement left to the planner, where the choice between the two responses to a no is not settled by the count.

## Why the last question matters

This wiki reads the seventh question as carrying a mechanism the others do not: velocity counts points, and points are relative to whoever assigned them. A mean taken in one team's [[story-points]] says nothing about another estimator's scale, even where the executors are unchanged.

## Where the inputs come from

Team, tools and technology are read from the project's own records. The history itself is read from the earlier project's board. If the earlier board has no finished iterations to average, there is no history, and [[choosing-velocity-estimate-approach]] falls through to the next option.

## What later fact shows the choice wrong

The first observed iterations fall outside the range built from history. That is the signal to drop the history and use actuals, as [[choosing-velocity-estimate-approach]] requires in any case.

## Agent executor note

The transfer here is ours, and it is a reading, not a finding. The questions map onto an agent-run project as: the same repository and stack, the same domain, the same people writing and accepting tasks, the same agent setup, and the same estimators. A change of model or agent tooling would count as a no under "tools" or "team". Cohn's source cannot say how much such a change moves velocity, so the plugin should treat it as a reason to widen the range, not as a known correction.
