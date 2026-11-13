---
title: Defect Inside or Outside the Iteration
category: intake
summary: A defect found in the iteration is part of the work that made it and finishes with that work; one found later is ranked like any other item, because outside an iteration a bug fix and a feature are the same kind of thing.
tags: [decision-rule, triage, defects, iterations, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Defect Inside or Outside the Iteration

Cohn divides defects by when they are found, not by how severe they are. One side is part of finishing the work, and the other is new work to be ranked.

## Inside the iteration

Cohn's position is that "An agile team has the goal of fixing all bugs in the iteration they are discovered." ([[cohn-agile-estimating-planning]] L3200). The estimate either includes fixing or there is a separate "correct bugs" task, and Cohn's preference is "identifying a single task but not considering it complete until all of its tests pass" (L3200). He adds that teams become able to do this as they grow proficient, "especially through relying on automated testing" (L3200), so it is a goal and not a starting condition.

## Outside the iteration

> A defect found later (or not fixed during the iteration it was discovered) is treated the same as a user story. Fixing the defect will need to be prioritized into a subsequent iteration in the same way any other user story would be. Outside of an iteration, the whole idea of a defect starts to go away. Fixing a bug or adding a feature become two ways of describing the same thing.
>
> — [[cohn-agile-estimating-planning]], L3202

This wiki reads the last sentence as a consequence for triage: from that point a defect gets no separate ordering lane and is compared by the same criteria as everything else ([[ordering-by-value-and-urgency]]). Severity enters through that comparison. How much of a period goes to such defects, and how one enters mid-period, is on [[bug-allocation]].

## The decision, by setup

The flow case is this wiki's, since Cohn writes only about iterations.

- **Iteration setup:** was it found within the iteration where the faulty work was done, and is it fixable there? If yes, it belongs to that task, which is not finished until the tests pass. If no, it is a new item and gets ranked.
- **Flow setup:** the boundary has no period to rest on, so this wiki uses the task's finish point ([[started-and-finished-points]]). Found before the finish point, it is part of the task. Found after, it is a new item.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Which task produced the defect | The report and the linked task |
| Whether that task is finished, or its iteration still open | Board state |
| Whether its fix fits the current period | Capacity on [[iteration-capacity]] |

The choice was wrong if a defect treated as part of a task turned out to be a separate change, for instance if fixing it grew larger than the task. It was also wrong if a defect ranked as new work was left low while the feature that caused it was presented as finished.

## Sign of violation

These signs are this wiki's.

- **In board history:** a new item filed for a defect in a task still open in the same period, and that task then closed as finished.
- **In board state:** defects held in a separate queue that is never compared with features.
- **In task state:** a finished task whose tests fail.

## Trade-off

Holding a task open until tests pass slows the count of finished work inside a period. Treating every later defect as a story means an accepted defect can sit unfixed for a long time, which is deliberate, and it is worth saying so to whoever reported it.

## Agent executor note

The rule rests on a test run and on when a defect was found, so this wiki expects it to survive an agent executing. This wiki adds that an agent's report that a task is complete is not evidence that tests pass: done is what a check shows ([[testable-acceptance]]). Intake of a defect report is on [[incoming-report-content]] and [[triage-procedure]].
