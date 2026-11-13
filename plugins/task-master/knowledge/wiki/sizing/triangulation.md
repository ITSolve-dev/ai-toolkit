---
title: Triangulation
category: sizing
summary: Estimate a task by comparing it with several already-estimated tasks, one a step smaller and one a step larger, not with a single baseline; the comparison set is what keeps a scale step meaning one thing.
tags: [method, estimation, analogy, relative-estimation]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Triangulation

Triangulation is estimating by analogy against several reference items at once. It rests on the claim that "There is evidence that we are better at estimating relative size than we are at estimating absolute size (Lederer 1998; Vicinanza 1991)." ([[cohn-agile-estimating-planning]] L1288), which this wiki holds on Cohn's report and has not checked against the studies.

## Procedure

> When estimating this way you do not compare all stories against a single baseline or universal reference. Instead, you want to estimate each new story against an assortment of those that have already been estimated.
>
> — [[cohn-agile-estimating-planning]], L1290

1. Propose a step on the project's [[estimation-scale]].
2. Read a task or two already on the step below and on the step above.
3. Check the task sits between them. Cohn's example: "To decide if a story should be estimated at five story points, see if it seems a little bigger than a story you estimated at three and a little smaller than a story you estimated at eight." (L1290).
4. If it does not, move to the step where it does.

The steps are this wiki's arrangement of Cohn's example.

## Limit: the comparison needs similar sizes

Cohn says a ratio is only answerable when small: "Asking “Is this story fifty times as hard as that story” is a very different question than “Is this story about one-and-a-half times that one?”" (L1294). This wiki reads that as the reason triangulation stops working above the scale's range. An item with no neighbours of similar size goes to splitting, on [[estimation-techniques]], or to cutting, on [[size-ceiling]].

## Keeping a step's meaning

Cohn raises consistency in a setting this wiki does not otherwise use: a large team estimating in sub-groups. "What your team calls three story points or ideal days better be consistent with what my team calls the same." (L1348). His device is to estimate 10–20 stories jointly and hand each sub-group the set as a baseline (L1348). Sub-groups do not arise for a few people, so this wiki notes the figure and the setup and does not adopt them.

This wiki takes the mechanism: a step is defined by the tasks already on it, so the same scale can drift over a project's life if nothing is compared with earlier work. That drift over time is our extension, and the source discusses it only across groups.

## Failure signs

- **One baseline.** Sign: every estimate is justified against the same single task. The source forbids it and gives no observable sign, so the sign is ours.
- **A step that does not hold.** Sign: tasks on one step lived very different times on the board. This raises a question and is not proof: [[smell-is-not-a-finding]] applies, and waiting time on the board is not effort, per [[flow-metrics]]. If the pattern holds for a class of tasks, the response is on [[re-estimate-when-relative-size-changes]].

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The scale | Project setup |
| Reference tasks on neighbouring steps | Tasks already estimated, preferably finished, on the board |
| The task's contents | The task text |

The estimate was wrong if the finished task, compared afterwards with the same references, clearly belongs on another step.

## Agent executor note

The evidence for relative estimation concerns people. This wiki notes one property of triangulation that suits an agent: the reference set can be read from the board, so it does not depend on remembering. Whether an agent's comparisons are any good is untested in every source here. A new project has no reference set, so the first estimates fall back on expert opinion on [[estimation-techniques]], and this wiki reads those as the ones least worth trusting.
