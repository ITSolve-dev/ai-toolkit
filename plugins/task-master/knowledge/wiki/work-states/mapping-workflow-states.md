---
title: Mapping Workflow States
category: work-states
summary: Derive a board's states by tracing recent tasks of different kinds, listing what actually happened to them, noting what was skipped and where they waited, and grouping similar activities; the states are containers and the activities are what happen inside them.
tags: [method, work-states, board-design, kanban]
sources: [kanban-playbook-workflow-states, kanban-guide, scrum-guide-2020]
created: 2026-11-01
updated: 2026-11-01
---

# Mapping Workflow States

This method derives a board's states from how work actually moved, so that the columns are not a guess. Its core is one distinction from the Kanban Playbook:

> States are containers. Activities are what happen inside them. Work enters a state at a point in time and exits when it is ready to move forward. That is what makes flow visible and measurable.
>
> — [[kanban-playbook-workflow-states]], L18

The Playbook adds a limit: "Understanding the activities your work goes through helps you design states that make sense. It does not mean every activity becomes a column." (L20). This wiki reads those together as the reason the procedure ends with grouping and not with a list of activities.

## The procedure

The Playbook gives this as a story (L35). The numbered form is this wiki's.

1. **Take recent tasks of different kinds.** The illustrated team uses a bug fix, a feature request and a compliance update. Three is what that team did, and it is not a stated minimum. The point is that the kinds differ.
2. **List every activity that happened to each**, as it happened and not as it was supposed to.
3. **Note what was skipped and where work waited.** The illustrated team finds that "the bug fix skipped the spec step entirely" and that "compliance updates always wait for a legal review that no column currently represents." (L35).
4. **Group similar activities across the tasks.** Each group is a candidate state.
5. **Judge the candidates** against [[distinguishable-work-states]].

## What skipping it costs

The Playbook names three defects: "If you skip this step, you will likely end up with too many states, states that overlap, or states that do not reflect how work actually moves." (L20). Its illustration shows the sign on a board. Work items are "sitting in "In Development" for days with no movement. Nobody is sure if the item is being worked on, waiting for a dependency, or just forgotten." (L33).

This wiki reads that as the [[active-versus-queued]] failure seen from a different direction, and uses it as the test of a finished mapping: from the board alone, can a reader say what is happening to each task? Mapping was done badly if the answer is no.

## A project with no history

The Playbook assumes recent work exists. A new project has none. This fallback is this wiki's and no source states it: start with the fewest states the distinctions on [[distinguishable-work-states]] need, run some tasks, and map them when they have finished. The Playbook's warning applies to treating such a start as a design. It is a placeholder until history exists.

## Positions and setups

**Kanban Guide:** states are required, as "One or more defined states" ([[kanban-guide]] L112). How to find them is not addressed, and the Playbook supplies that. The Guide's allowance that an item may have more than one started or finished point (L111) fits step 3: a kind of work that skips a state may simply have a different path.

**Scrum Guide:** no states, so no mapping. It does ask that the Sprint Backlog be "a highly visible, real-time picture of the work" ([[scrum-guide-2020]] L297), which says a plan must be visible and not how to draw it.

The method applies to any board with states, under any setup, because it reads the work and not the methodology.

## Agent executor note

The Playbook's team walks through items together, and its test of readiness is that people can describe the work "without debate or confusion" (L24). Neither transfers. For an agent-run project the trace comes from board history, commits and run records, which the plugin can read, and the test becomes whether a task's state can be told from the board. The agent adds activities a person would not list, such as long exploration inside a run, and those are invisible on the board unless something records them. Whether that matters to state design is not addressed by any source here.
