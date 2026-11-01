---
title: Diagnosing Unfinished Work
category: reading-history
summary: A task left unfinished at period end has at least three candidate causes, too large, underestimated or too much selected, and each points to a different fix, which matters more than how the task is counted.
tags: [decision-rule, retrospective-analysis, iterations, sizing, failure-mode, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Diagnosing Unfinished Work

When a task crosses a period's end unfinished, the useful question is why. The source places this above the bookkeeping:

> How they count such a story is less important than that they determine why it happened and how they can prevent it from happening again.
>
> — [[cohn-agile-estimating-planning]], L4302

What counts toward the period is settled separately by [[all-or-nothing-counting]] and [[unfinished-at-period-end]].

## The three causes

The source names them in two places. L4300 is unconditional:

> If a team has unfinished stories at the end of an iteration, they are working with features or stories that are too large.
>
> — [[cohn-agile-estimating-planning]], L4300

L4302 then lists two others: the story was underestimated, or "too many stories were pulled into the current iteration". This wiki resolves the tension by treating L4300 as the first suspicion and not a verdict, since the source's own next paragraph supplies causes under which size is not at fault.

## Telling them apart

The source gives causes and remedies. The inputs below are this wiki's, read from the board.

| Cause | Inputs and where they are read | Remedy from the source |
|---|---|---|
| **Too large** | The task's estimate against [[size-ceiling]]; the task was active for most of the period | Split into smaller stories, ideally before the period starts (L4300) |
| **Underestimated** | The estimate raised during or after the period; other tasks of the same type also ran long ([[similar-tasks-overrun-together]]) | Identify "what type of work was underestimated or forgotten" and take care with that type next time (L4302) |
| **Too much selected** | The selected total against recent [[velocity]]; several tasks unfinished, some never started, none individually large | Plan iterations more carefully ([[filling-a-period]]) (L4302) |

The causes can combine. This wiki reads a single unfinished task as pointing to its size or estimate, and several small ones unfinished, some not started, as pointing to the selection.

## What would show the diagnosis wrong

These facts are this wiki's.

- Called too large: after the split, the pieces still do not finish in a period, so size was not the cause or the split was poor ([[choosing-between-splits]]).
- Called underestimated: the next task of that type runs long despite the correction, so the type was misidentified.
- Called overselected: a smaller selection next period still leaves work unfinished.

## Why it matters

This wiki notes that the fixes differ, and the wrong one does nothing. Splitting a task will not help a period that was overfilled, and selecting less will not help a task above the size at which it should have been cut. The source's reason for small work is "Small stories lead to a steady flow through the development process." (L4300).

## Failure mode

The same task or the same kind of task unfinished across several periods, with counting debated and no cause recorded. Sign in board history: repeat selection of a task with no change to its estimate, cut, or the size of the selection. It is the case [[overrun-triggers-a-recut]] takes up for a single task.

## Which setup this applies under

- **Iteration setup:** as above.
- **Flow setup:** the "too much selected" branch has no counterpart, because nothing is selected for a period. The question becomes whether WIP is uncontrolled ([[wip-control]]). The other two branches survive, triggered by age and not by the calendar. This mapping is this wiki's.

## Agent executor note

The source's underestimation remedy is to "try to remember" (L4302). That mechanism is memory, and it does not survive an agent executing or a few people between sessions. This wiki's transfer: the finding has to be written where the next estimate reads it. The diagnosis itself is read from the board and survives.
