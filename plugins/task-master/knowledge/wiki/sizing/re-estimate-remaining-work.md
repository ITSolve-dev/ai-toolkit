---
title: Re-estimate Remaining Work
category: sizing
summary: An estimate of what is left on an open item is changed the moment someone learns it is wrong, and one far off is replaced by two or three items; the trigger is discovery, earlier than an overrun, and a whole task's size step follows a stricter rule.
tags: [rule, estimation, iterations, board-history]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Re-estimate Remaining Work

This rule treats an estimate on an open item as a current statement of what is left, not a promise made at planning. On Cohn's board each card "shows the estimate of the work remaining to complete the task" ([[cohn-agile-estimating-planning]] L4474), and:

> The developers are encouraged to change the estimate on any task card on the board at any time. For example, if I start working on a card and realize that the estimate of two hours on it is wrong, I will go over to the task board, cross out the two, and replace it with perhaps a six. If I believe the estimate is even further off, I may rip up that task card and replace it with two or three task cards, each with its own estimate.
>
> — [[cohn-agile-estimating-planning]], L4488

## The discriminating criterion

Cohn separates two responses by how wrong the estimate is: an estimate that is wrong gets overwritten, and one "even further off" gets replaced with several cards. His only example of the first is a two becoming a six, so a threefold miss still stays on one card. He gives no threshold for the second, and this wiki does not invent one.

## Levels and conditions

The passage concerns hours on sub-story task cards. The story's points are not touched in this chapter, so this page does not support changing a task's size step in mid-flight. Two numbers are involved, and this wiki keeps them under two rules. A remaining figure says what is left and moves whenever belief moves. A size step says how big a task is relative to others, and it changes only under [[re-estimate-when-relative-size-changes]], which refuses to change it for slow progress alone. Cohn does not connect the two chapters, and the distinction is this wiki's.

This wiki transfers the rule to a whole task by shape only: at its own level, a task found to be bigger than its step is reported and recut, per [[overrun-triggers-a-recut]] and [[size-ceiling]].

What Cohn adds to that page is the trigger. [[overrun-triggers-a-recut]] fires when a task outlives its expectation. His fires at discovery, "if I start working on a card and realize" (L4488), which can come much earlier.

## The rule

When anyone working on a task learns that it is bigger than stated, that is recorded then and not left until the end. A remaining figure, where the project keeps one, changes at once. A task too big for its step is reported and recut.

## Sign of violation

- **In board history:** a task took far longer than its step usually takes, and it was neither recut nor annotated while it was open.
- **In board history:** where a project keeps remaining figures, none changed across a whole period in which some tasks overran. This wiki reads that as a sign the board's remaining figures are stale, so any [[iteration-burndown]] drawn from them is too.

Cohn states the practice. These signs are this wiki's.

## Why

The remaining figure is what the daily sum and the burndown read: "I usually sum the hours for each row every morning." (L4488). An estimate left as planned makes those totals report the plan and not the state of the work. This wiki adds that a change has to stay visible on the task, or [[release-progress-forces]] cannot separate it from completed work.

Cohn prefers this figure to the opposite one, how much has been spent; that argument is on [[comparing-estimate-to-actual]].

## Cost

The totals can rise during a period, which can read as a slip when it is only a correction. The cost is also a habit that someone must keep up, and that burden is why a board's estimates go stale.

## Agent executor note

Cohn's mechanism is a developer who walks to the board. An agent will not do that unless told, and it has no standing to rewrite scope ([[mid-period-change]]). So this wiki reads the transfer as a report: an agent that finds a task bigger than stated stops and says so, and the person steering changes the estimate or recuts. That reading is this wiki's. A discovery that a task is underspecified, and not big, calls for fixing its text ([[overrun-triggers-a-recut]]).
