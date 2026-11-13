---
title: Overrun Triggers a Recut
category: sizing
summary: A task that outlives the 85th percentile of time lived on its size step (or the SLE) is recut, unblocked or explained; a discovery that a task is bigger than stated is recorded when it is made, a remaining figure moving at once while the size step changes only by the relative-size rule.
tags: [rule, estimation, smart, board-history, iterations]
sources: [wake-invest, ambig-swe, kanban-guide, scrum-guide-2020, cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Overrun Triggers a Recut

A task carries an expectation of how long it should live, and passing that expectation forces a decision about the task. This is the part of Wake's "Time-boxed" criterion that transfers from his sub-story tasks to this wiki's unit ([[unit-of-work]]).

> A task should be *time-boxed*: limited to a specific duration. This doesn’t need to be a formal estimate in hours or days, but there should be an expectation so people know when they should seek help. If a task is harder than expected, the team needs to know it must split the task, change players, or do something to help the task (and story) get done.
>
> — [[wake-invest]], L114

This wiki keeps "split the task" and drops "change players", since assigning people is outside the charter.

## The rule

When a task in an active state outlives the expectation for its size, recut it, unblock it, or say why it stays as it is. Leaving it to run on is the violation. The three responses are this wiki's reading of Wake's "split the task ... or do something to help the task".

## Sign of violation

Board history shows a task in an active state for longer than the 85th percentile of time lived by finished tasks on the same size step, with no split, no state change and no recorded reason in that time. The percentile is this wiki's choice, borrowed from the SLE convention ([[service-level-expectation]]); Wake sets no figure. It is a distribution per step read from history, not a duration converted from one item's points ([[story-points-do-not-convert-to-hours]]), and it fires on about one task in seven by construction, where a typical-time threshold would fire on about half ([[completion-time-distribution]]). Where the step has too few finished tasks to read a percentile ([[how-much-flow-data]]), the period's end is the trigger. The sign is read from board history and needs no logged hours, because the charter reads time a task lived from history and leaves hour tracking out.

## Why

This wiki reads what breaks if ignored as the signal itself. An overrunning task is the first evidence that it was cut or described wrongly, and that evidence loses its value once the task quietly finishes late.

## Cost

This wiki reads the cost as interrupting some tasks that were nearly done. The rule accepts that cost in exchange for not discovering a wrong cut at the end.

## Agent executor note

Wake's mechanism is a person who notices the expectation has passed and seeks help. That part rests on a human executor. An agent has no such habit unless it is given one, so this wiki moves the check to the board and to the person steering, who reads age from history. The expectation itself survives; the self-report does not.

An agent's overrun may also mean something different from a person's. The Ambig-SWE footnote on Claude Sonnet 4 in the Hidden setting reports:

> The model compensates for the lack of information with increased exploration and solution attempts leading to substantially higher evaluation costs.
>
> — [[ambig-swe]], L155

The authors repeat the point at L159: Claude Sonnet 4 "extensively explores the codebase and attempts multiple solutions to overcome the lack of information". This wiki reads that as a second diagnosis for an overrun: with an agent, a task running long may be an [[underspecified-task]] and not a big one. The evidence is one model on stripped issues, and it concerns cost and not age on a board, so the reading is a hypothesis to check first when an overrun appears. It does not establish the cause. The response is then to fix the task text and not to split it.

## Positions

**Kanban Guide:** the expectation is the [[service-level-expectation]]. The Guide lists among the forms of active management "Ensuring work items do not age unnecessarily, using the SLE as a reference." ([[kanban-guide]] L134). This wiki reads that as giving the rule a number that comes from history and not from a size step. An item's age is compared with the SLE while it is open, so the sign fires before the item finishes late. The Guide does not say what to do when age passes the SLE, and the three options above are this wiki's, from Wake.

**Scrum Guide:** it has no expectation per item. What it inspects daily is the goal: "The purpose of the Daily Scrum is to inspect progress toward the Sprint Goal and adapt the Sprint Backlog as necessary" ([[scrum-guide-2020]] L234). The only item-level limit is the period itself ([[unfinished-at-period-end]]). This wiki reads that as a later and coarser trigger, since a task can overrun for most of a period with nothing firing.

## Which holds under which setup

- **Flow setup:** age against the SLE.
- **Iteration setup:** the 85th percentile of time lived on the size step, as in the sign above, with the period's end as the backstop and as the trigger where the step's history is thin. Wake gives the expectation and no method for setting it; the percentile is this wiki's.
- **Iterations with a WIP control:** either, and the SLE if the project keeps one.

## Re-estimate Remaining Work

This rule treats an estimate on an open item as a current statement of what is left, not a promise made at planning. On Cohn's board each card "shows the estimate of the work remaining to complete the task" ([[cohn-agile-estimating-planning]] L4474), and:

> The developers are encouraged to change the estimate on any task card on the board at any time. For example, if I start working on a card and realize that the estimate of two hours on it is wrong, I will go over to the task board, cross out the two, and replace it with perhaps a six. If I believe the estimate is even further off, I may rip up that task card and replace it with two or three task cards, each with its own estimate.
>
> — [[cohn-agile-estimating-planning]], L4488

### The discriminating criterion

Cohn separates two responses by how wrong the estimate is: an estimate that is wrong gets overwritten, and one "even further off" gets replaced with several cards. His only example of the first is a two becoming a six, so a threefold miss still stays on one card. He gives no threshold for the second, and this wiki does not invent one.

### Levels and conditions

The passage concerns hours on sub-story task cards. The story's points are not touched in this chapter, so this section does not support changing a task's size step in mid-flight. Two numbers are involved, and this wiki keeps them under two rules. A remaining figure says what is left and moves whenever belief moves. A size step says how big a task is relative to others, and it changes only under [[re-estimate-when-relative-size-changes]], which refuses to change it for slow progress alone. Cohn does not connect the two chapters, and the distinction is this wiki's.

This wiki transfers the rule to a whole task by shape only: at its own level, a task found to be bigger than its step is reported and recut, per the rule at the top of this page and [[size-ceiling]].

What Cohn adds to that rule is the trigger. The rule at the top of this page fires when a task outlives its expectation. His fires at discovery, "if I start working on a card and realize" (L4488), which can come much earlier.

### The rule

When anyone working on a task learns that it is bigger than stated, that is recorded then and not left until the end. A remaining figure, where the project keeps one, changes at once. A task too big for its step is reported and recut.

### Sign of violation

- **In board history:** a task took far longer than its step usually takes, and it was neither recut nor annotated while it was open.
- **In board history:** where a project keeps remaining figures, none changed across a whole period in which some tasks overran. This wiki reads that as a sign the board's remaining figures are stale, so any [[iteration-burndown]] drawn from them is too.

Cohn states the practice. These signs are this wiki's.

### Why

The remaining figure is what the daily sum and the burndown read: "I usually sum the hours for each row every morning." (L4488). An estimate left as planned makes those totals report the plan and not the state of the work. This wiki adds that a change has to stay visible on the task, or [[release-progress-forces]] cannot separate it from completed work.

Cohn prefers this figure to the opposite one, how much has been spent; that argument is on [[comparing-estimate-to-actual]].

### Cost

The totals can rise during a period, which can read as a slip when it is only a correction. The cost is also a habit that someone must keep up, and that burden is why a board's estimates go stale.

### Agent executor note

Cohn's mechanism is a developer who walks to the board. An agent will not do that unless told, and it has no standing to rewrite scope ([[mid-period-change]]). So this wiki reads the transfer as a report: an agent that finds a task bigger than stated stops and says so, and the person steering changes the estimate or recuts. That reading is this wiki's. A discovery that a task is underspecified, and not big, calls for fixing its text (the rule at the top of this page).
