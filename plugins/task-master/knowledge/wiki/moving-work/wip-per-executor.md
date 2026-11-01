---
title: WIP Per Executor
category: moving-work
summary: Cohn limits each developer to one or two cards in process at a time, for flow and against context switching. The number is about people and sub-story cards; what transfers to an agent is one task per run, alongside a workflow-wide bound.
tags: [rule, wip, iterations, board-state]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# WIP Per Executor

This rule bounds concurrent work by who holds it, not by the whole workflow. Cohn states it for the iteration task board:

> No one should sign up for more than one or two cards at a time. This helps maintain a consistent flow of work through the process and reduces the cost of context switching among multiple tasks.
>
> — [[cohn-agile-estimating-planning]], L4484

He keeps it in view with the layout: "As a constant reminder of this, when I have a team set up their task board I have them make the In Process column the width of one card." (L4484). Chapter 14 gives the same figure when tasks are left unallocated at planning, "one or two related tasks at a time" (L3051, on [[tasks-are-not-assigned-at-planning]]).

## Conditions on the number

The figure "one or two" is an experienced practitioner's advice with no measurement. It applies to a developer holding Cohn's task cards, which are pieces of a story and smaller than this wiki's task ([[unit-of-work]]). It does not say how many whole tasks one executor should hold, and this wiki does not carry the number up a level.

This wiki reads the one-card width as a reminder and not a bound: a column that narrow limits nothing by count once several people work the same row. Cohn calls it a reminder himself.

## The rule

One run of an agent holds one task. A person executing holds very few. Cohn's one or two is the figure this base has for that, and the study on [[multitasking]] points the same way with the limits stated there.

The first sentence is this wiki's transfer, from the charter's test that a result is presented once ([[unit-of-work]]). Cohn's allowance of two is not carried over to a run.

## Sign of violation

- **In board state:** one assignee or run holding several active tasks with no declared reason.
- **In board history:** one run moved two tasks to active and presented one combined result. This also points at a bad cut ([[compound-task-text-signs]]).

These signs are this wiki's. The first applies to the board's concurrency only. Whether a given person is overloaded is outside the charter.

## Why

Cohn names two effects, a consistent flow of work and a lower cost of context switching (L4484). He gives no figure for either here, and [[multitasking]] holds the study behind the second. This wiki keeps the first as a mechanism and treats the second under the note below.

## Cost

Cohn names none here. A blocked executor with a limit of one has nothing to do. Chapter 2 gives the reason for holding a second task: "With two value-adding tasks, if you become blocked on one you can switch to the other." (L627). This wiki reads the second card in his allowance the same way, as slack for a stopped task, though Chapter 20 does not connect the two. See [[blocked-work-counts-against-wip]].

## Agent executor note

Context switching is a human cost, and it does not survive as stated: an agent has no attention to fragment. A per-executor limit also restrains less with agents. Ten runs holding one task each pass this rule and still flood the people who review them. So the bound that matters there is the workflow-wide one in [[wip-control]], and this page only keeps a run from mixing two results.

## Which holds under which setup

The resolution is this wiki's.

- **Iteration setup with people executing:** [[wip-control]] says people's own hours restrain the moment. Cohn's limit is the explicit form of that restraint, and a project wanting one can state it.
- **Iteration or flow setup with an agent executing:** one task per run, plus the workflow bound.
- **Flow setup with people executing:** the workflow bound is required, and a per-person limit is one allowed extra, since the Guide leaves the form open ([[kanban-guide]] L139, quoted on [[wip-control]]).
