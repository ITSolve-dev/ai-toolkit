---
title: Backlog Versus Commitment
category: work-states
summary: A backlog is a container of candidates, not committed or prioritized work; commitment happens when capacity exists, so a backlog belongs inside a process's boundaries, and on its CFD, only if it really has been committed, a choice that moves the start of Cycle Time.
tags: [decision-rule, work-states, ordering, cfd, flow-metrics, kanban, scrum]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Backlog Versus Commitment

A backlog holds candidates, and an item is committed only once the project has taken it on with capacity to do it. Vacanti objects less to backlogs than to what the word implies. In his experience people assume two things ([[vacanti-actionable-agile-metrics]] L1468-L1472):

1. "That items placed in a backlog are somehow committed to (or that they otherwise inherently have value)"
2. "That items placed in a backlog are somehow prioritized."

His position:

> A backlog, therefore, is merely a convenient container for these candidate ideas. Commitment does not happen until a team actually has capacity, and prioritization does not happen until at the time of commitment
>
> — [[vacanti-actionable-agile-metrics]], L1474

The just-in-time mechanics are deferred to his Chapter 8 (L1480). This wiki takes the discriminating criterion to be whether the item has been committed to, and not whether it is written down. On a board the commitment has a place: the [[arrival-point]] column.

## On a chart

A backlog band is the visible form of this decision, because Property #1 of the [[cumulative-flow-diagram]] makes the top line the arrivals. Plotting a backlog says its items have arrived.

> If you do not want to signal that items in your backlog have been committed to, then do not include a backlog band on your chart. If you do want communicate that backlog items have been committed to, then, by all means, display the backlog. That decision, as we are about to see, could have serious ramifications for your Cycle Time calculation.
>
> — [[vacanti-actionable-agile-metrics]], L1482

The source holds both that "any diagram that shows a backlog is not a CFD" for the most part (L1464) and that one "could definitely have a CFD that looks like Figure 4.16" subject to all the properties (L1482). This wiki reads the second as the rule and the first as the usual case: a backlog is a legitimate band exactly when it lies inside the process boundary, and usually it does not. A backlog plot can still be useful as something other than a CFD: "I am not saying that a chart that shows a backlog is not useful—far from it." (L1484).

The Cycle Time consequence is promised and not worked through in that chapter. This wiki reads it from Property #1: if the backlog is the top band, arrival is entry into the backlog, so Cycle Time starts there and includes all the waiting among candidates. See [[started-and-finished-points]].

## The rule

| Input | Read from |
|---|---|
| Where the project says commitment happens | The project's stated [[started-and-finished-points]] |
| Whether items in the pile are in fact worked in the order and on the terms stated | Board history |

Put the started point where commitment happens. Keep anything before it out of the process, out of flow metrics, and off the CFD.

**Sign of violation:** a CFD band or a metric's start falls in something that "sounds like" a backlog (L1530); or Cycle Time is dominated by the time before any active state; or a long list of unstarted items is read as a promise. Each raises a question and is no verdict, per [[smell-is-not-a-finding]].

**What would show the choice wrong:** items past the supposed commitment point are routinely dropped, which means commitment happens later than stated; or items outside it are treated as owed, which means it happens earlier.

## Which holds under which setup

The resolution here is this wiki's. The source says the principles apply to Scrum or XP style processes as well (L1248) and does not map them.

- **Flow:** commitment is the pull into the first started state, which fits the source directly.
- **Iterations:** commitment falls at the selection for the period, so the pile before it stays outside the boundary and the items selected are inside it.

## Tension with ordering

The claim that "prioritization does not happen until at the time of commitment" (L1474) sits against the pages in `ordering`, which rank a pile ahead of time. This wiki reads a rank on uncommitted items as a proposal for the next commitment decision: useful, cheap to change, and owed to nobody. On that reading Vacanti's point survives as the warning that a rank is not a promise. See [[estimate-is-not-a-promise]] for the same separation applied to size.

## Agent executor note

The distinction between a candidate and a commitment does not depend on the executor. "Capacity" does. An agent can start nearly anything, so capacity on such a board is more plausibly the person's ability to steer and review, as [[wip-per-executor]] considers. That reading is ours and untested.
