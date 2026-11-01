---
title: Iteration Task Board
category: work-states
summary: Cohn's board for one iteration, with a row per story and columns To Do, Tests Ready, In Process, To Verify and Hours; only To Do and In Process are required states, and the rest are a marker, an optional handoff and a computed total.
tags: [concept, work-states, board-design, iterations]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Iteration Task Board

Cohn's task board is the layout he recommends for tracking one iteration. He gives it two jobs: "a convenient mechanism for organizing their work and a way of seeing at a glance how much work is left" ([[cohn-agile-estimating-planning]] L4457). It has one row per story and a fixed set of columns, shown in his Figure 20.1 (L4470). This page records that layout and classifies each column, because the columns mix several different kinds of thing under one word.

## Levels

Cohn's cards are a level below this wiki's task. His story is this wiki's task, and his task card is the piece of a story that the plugin does not produce ([[unit-of-work]]). So the row is the unit a board in this wiki tracks, and the cards inside it move across the columns. Applying these columns to whole tasks is this wiki's transfer, and Cohn does not make it.

## The columns, classified

The left column below is Cohn's. The classification is this wiki's, using [[column-versus-attribute]].

| Cohn's column | What he says it holds | Classification here |
|---|---|---|
| Story | The story card with its point estimate (L4465) | Row label, not a state |
| To Do | Task cards, each showing "the estimate of the work remaining to complete the task" (L4474) | Queued state |
| Tests Ready | A checkmark once the story's high-level tests are specified (L4482) | Marker on the row, not a stage cards pass through. See [[tests-specified-before-start]] |
| In Process | "cards that developers have signed up for" (L4484) | Active state |
| To Verify | A card awaiting "a fresh pair of eyes", when there is no test card (L4486) | Optional handoff: predictable place, goes forward afterwards |
| Done | Optional: a finished card "is removed from the task board" or moved to a Done column (L4486) | The finished point, if it is kept |
| Hours | The sum of hours remaining for the row (L4488) | Computed value, not a state. It feeds the [[iteration-burndown]] |

Two things this wiki takes from that classification:

- **Column does not mean state in this layout.** Only To Do and In Process are always stages. A check of a board against this layout should compare stages to stages, per [[judging-board-columns]], and not count columns.
- **Removing finished cards loses the finished point.** Cohn allows it because a paper board needs only the work left. This wiki reads that as unsafe for a board whose history is read later, since a task that leaves the board has no recorded crossing of [[started-and-finished-points]].

## To Verify: the discriminating criterion

Cohn separates two ways of checking finished work. Where a test card was written at planning, the finished programming card leaves and someone signs up for the test card. Where no test card exists, or a developer "would like a fresh pair of eyes to take a quick, verifying look", the card goes to To Verify (L4486). He says the column is one "that you may or may not need" and finds it useful "especially when working with a team that is learning how to become agile" (L4486).

This wiki reads the split as a question of whether the check is planned work or a handoff. At this wiki's level a test is part of the task's result and not a separate unit, so the first route does not transfer: the plugin does not produce a code card and a test card for one result ([[component-task-masquerading]]).

## What the board requires

Cohn requires flexibility of the board, not a form: it must "allow the team a great deal of flexibility in how they organize their work" (L4457), and that is what makes [[tasks-are-not-assigned-at-planning]] visible. He also admits equivalents, writing of the board "(or something equivalent to it)" (L4457). The physical details he gives are a matter of medium and this wiki drops them.

## Agent executor note

The classification concerns the work and survives. In the To Verify row, "a fresh pair of eyes" maps onto review by the person steering, which [[column-versus-attribute]] already treats as a handoff that takes a column. For an agent's output this wiki reads that column as required and not optional, because the executor cannot be the only check on its own result. That reading is this wiki's, and Cohn's reason for the column is about teams learning a habit.
