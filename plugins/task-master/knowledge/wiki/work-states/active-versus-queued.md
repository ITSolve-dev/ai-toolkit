---
title: Active Versus Queued
category: work-states
summary: A board has to show whether a task is being worked on or is ready and waiting for attention, because an active column that hides queued work makes bottlenecks unreadable; this kind of waiting is inside the project and is not the outside wait of the parking lot.
tags: [rule, work-states, board-design, kanban]
sources: [wester-board-design, kanban-guide]
created: 2026-11-01
updated: 2026-11-01
---

# Active Versus Queued

A task inside the workflow is either being worked on or sitting ready for someone to take it. A board should show which. Wester's statement:

> In order to really focus on improving the flow of work through your system, you will want to visualize when work is actively being worked on versus when work is ready and waiting for attention.
>
> — [[wester-board-design]], L40

Wester then lists what that separation shows (L42-L44): bottlenecks, "seen by large queues directly to the left"; "unreasonable amounts of work sitting in active column, masking additional wait time"; and whether to reduce wait or speed up an activity. The practical advice is "A good practice is to use verbs for columns representing active work." (L45), and to split active columns into *Doing* and *Done* sub-columns (L45).

## The rule

For each state where work is done, a reader of the board can tell a task being worked on from a task that is ready and waiting. This can be done by a separate queue column or by sub-columns.

## Sign of violation

- **In board state:** a task in an active state with no work happening on it. With an agent this can be checked directly, since a run either exists or does not.
- **In board history:** tasks spending far longer in one active state than in the others, with no way to tell whether they were being worked on.
- **In board state:** a pile-up directly to the left of one state. This is Wester's sign, and it marks the bottleneck rather than a violation.

The first two signs are this wiki's wording of L43.

## Why

What breaks is the diagnosis. If waiting hides inside an active state, a long time in that state reads as slow work when it may be no work at all. The fix would then be aimed at the wrong thing, which is Wester's third point: "whether or not you should focus on reducing wait or speeding up certain activities." (L44).

## Cost

The rule adds states. A board with *Doing* and *Done* under each stage has twice as many places to look, and a board for a few people has few tasks to spread across them. This wiki reads this as a reason to add a queue only where tasks actually sit, which is what [[judging-board-columns]] checks.

## Three meanings of waiting

Three pages in this wiki use the word, and the word covers three different things.

| Page | What is waited for | Who holds the next step |
|---|---|---|
| This page | Someone to take the task | The project |
| [[waiting-versus-blocked]] | An outside party | Someone outside, with an expected end |
| [[sequence-versus-wait]] | A prerequisite | Someone outside |

Wester's sense is the first. A queued task is not stopped, and it does not go near a [[parking-lot]].

## Which holds under which setup

There is no disagreement to resolve. The Kanban Guide leaves column design open (L125 of [[kanban-guide]]), and the Scrum Guide has no columns. The rule holds on any board that has states.

## Agent executor note

The rule concerns the work and survives. An agent makes it easier to check, because whether a run is active is a fact and not a matter of asking someone. It also changes where the queues are likely to form. An agent takes work at once, so this wiki expects the large queue to sit in front of the people reviewing, and Wester's third question to answer itself: reduce wait, since speeding up the activity will not help. That expectation is unmeasured.
