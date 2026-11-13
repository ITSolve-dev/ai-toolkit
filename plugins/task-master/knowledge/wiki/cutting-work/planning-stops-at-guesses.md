---
title: Planning Stops at Guesses
category: cutting-work
summary: Planning needs only enough design to name and size the work; tasks are guesses to be replaced when wrong, and the urge to draw a model during planning is the warning sign that planning has gone too deep.
tags: [rule, decomposition, design-depth, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Planning Stops at Guesses

Planning requires some idea of how the work will be done and no more than that. Cohn accepts design discussion as necessary, since "We can’t create a list of tasks if we don’t have some idea of how we’re going to do the work" ([[cohn-agile-estimating-planning]] L3258), then sets its limit.

## The limit

> A desire to do so is probably the best warning sign of taking the design too far during iteration planning.
>
> — [[cohn-agile-estimating-planning]], L3264

The desire Cohn means is the need to draw a class diagram or similar model. He gives the reason: "all that’s necessary at this point are guesses about the work that will be needed to complete the features" (L3266).

## Why that is safe

Cohn's guesses are cheap because they can be replaced:

> If you get into the iteration and discover the tasks are wrong, get rid of the initial tasks and create new ones. If an estimate is wrong, cross it out and write a new value.
>
> — [[cohn-agile-estimating-planning]], L3266

This wiki reads the depth limit as depending on that freedom. Planning can stop early only if a task list may be rewritten without ceremony. A project that treats the plan as fixed has to design further ahead or absorb the errors.

## Sign of violation

The first sign is Cohn's, and the others are this wiki's.

- **During planning:** someone needs a class diagram or similar model to proceed (L3264).
- **In task text:** a task states the internal design rather than the result and the boundaries.
- **In board history:** tasks and estimates from planning unchanged even after work revealed they were wrong, with the discrepancy carried in comments.

## Trade-off

Shallow planning means some tasks will be wrong and rework of the plan is expected. Deep planning avoids that and costs design effort on work that may not survive, the same bet examined on [[how-far-to-split-up-front]].

## Boundary with other topics

How to write a design is `spec-driven-guide`. Step-by-step expansion of a task is out of this wiki's scope. This page holds only how far a cut has to look into the how before it stops.

## Agent executor note

Cohn's safety valve relies on an executor who notices a wrong task and rewrites it. This wiki does not assume that of an agent, which may carry out a wrong task as written or fill the gap silently ([[agent-silence-is-not-completeness]]). So the replacement passes through the people steering, as a stop or a recut ([[overrun-triggers-a-recut]]), and the new record has to say what was actually decided ([[whoever-writes-the-plan-controls-it]]). The depth limit itself survives, but a task should say more about its boundaries than a human team's note card would ([[underspecified-task]]). That reading is this wiki's and unmeasured.
