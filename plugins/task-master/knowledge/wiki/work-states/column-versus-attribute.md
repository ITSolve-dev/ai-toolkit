---
title: Column Versus Attribute
category: work-states
summary: A column is for a stage that happens in a predictable place, after which work goes forward; anything fleeting that can land anywhere is an attribute marked on the task where it stands. A handoff passes the test and a block does not.
tags: [decision-rule, work-states, board-design, kanban]
sources: [wester-board-design, kanban-guide, kanban-playbook-workflow-states]
created: 2026-11-01
updated: 2026-11-01
---

# Column Versus Attribute

This test decides whether something that happens to work deserves a column on the board or a marker on the task. It comes from Wester's argument against Blocked and On Hold columns:

> While these columns do help us see wait, they do not represent a stage of a lifecycle that happens in a predictable place. Rather, they are fleeting attributes of work residing in a particular stage of its lifecycle. We use columns to display the lifecycle stages of work. So, we need to use other visual queues to denote fleeting attributes like this.
>
> — [[wester-board-design]], L49

Wester's other half separates a handoff from a block:

> Handoffs are expected parts of the workflow and, when they come back from the handoff, they can move directly to next column on the board. In this way they are different than blocked or on hold columns and it is a very good practice to represent them using columns.
>
> — [[wester-board-design]], L57

This wiki reads those two passages as a test of two questions. The post offers the distinction and not the test, so the framing is ours.

## The test

1. **Does it happen in a predictable place?** For a given kind of work, does it occur at the same point in the workflow each time?
2. **When it ends, does the task go forward?** Or does it have to return to where it was?

| Predictable place | Goes forward after | Result |
|---|---|---|
| Yes | Yes | A column: a stage or a handoff |
| No | Either | A marker on the task, in the state where it happened |
| Yes | No | A cycle: see [[backward-movement]] |

## Why

What breaks when an attribute becomes a column is threefold, in Wester's account (L51). The first is location: "you can no longer see where in the workflow you experienced the wait." The second is the limit: "teams often use these pseudo-stages as a place to stash work so they can get around their WIP limits." The third is the return, which brings "data issues caused by backwards movement". This wiki keeps these as mechanisms. Wester reports no measurement for them.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Where the event happens, across tasks of a kind | Board history |
| Where a task goes afterwards | Board history |

A column was wrong if tasks leaving it return to an earlier state, or if it stays empty apart from rare exceptions. A marker was wrong if it recurs in the same state for most tasks of a kind, since that is a stage nobody has drawn. The Kanban Playbook's illustration has that shape: "compliance updates always wait for a legal review that no column currently represents." ([[kanban-playbook-workflow-states]] L35). This wiki reads that wait as a handoff, because it is in a predictable place. The Playbook does not classify it.

## Sign of violation

- **In board state:** a column named Blocked, On Hold or the like, in the sense of Wester's "any other column with the same purpose" (L49).
- **In board history:** tasks entering a column from several different earlier states and leaving back to the state they came from.

## Positions

**Wester:** as above.

**Kanban Guide:** the Guide does not address it. It says "There are no specific guidelines for how a visualization should look." ([[kanban-guide]] L125), so the test does not conflict with it and does not draw authority from it.

**Kanban Maturity Model:** blocked items stay and are marked, which agrees. Its parking lot is a holding area, which does not agree. The disagreement is resolved on [[parking-lot]].

**Scrum Guide:** silent, because it has no columns.

## Agent executor note

The test concerns the work and survives. Two cases are common with an agent, and the reading of both is this wiki's.

- **The person steering reviews a result.** This happens in the same place every time, and the task goes forward afterwards, so it is a handoff and takes a column. It is not a block ([[waiting-versus-blocked]]).
- **An agent stops mid-run with a question.** This can happen anywhere, so it is a marker on the task in the state where it stopped.

Wester's further argument that a visible stop should be painful, "that’s kind of the point" (L53), is a claim about people. An agent feels nothing, so the pressure lands on the people steering. The reasons above do not depend on it.
