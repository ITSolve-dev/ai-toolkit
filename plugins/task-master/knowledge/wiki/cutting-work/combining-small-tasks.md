---
title: Combining Small Tasks
category: cutting-work
summary: Tasks too small to stand alone are joined and estimated as one, preferring related ones because that eases prioritizing; bug reports are the common case.
tags: [decision-rule, decomposition, estimation, bugs]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Combining Small Tasks

Combining is the opposite move to splitting, for items below a useful size. It answers a different defect from the combine on [[component-task-masquerading]]: that page joins pieces because each has nothing to show, and this one joins pieces because each is too small to be worth handling alone.

> Just as we may need to split large stories, we may need to combine multiple tiny stories. The combined stories are estimated as a whole rather than individually. When possible try to combine related stories as that will make it easier to prioritize them. It is very common to combine multiple bug reports and treat them as one unit.
>
> — [[cohn-agile-estimating-planning]], L2719

Cohn's summary repeats the case: "sometimes it is appropriate to combine user stories, especially in the case of bug fixes, which may be too small on their own" (L2731).

## The test

Combine when an item is well below the size band of [[size-ceiling]] and has a related neighbour. Cohn gives no figure for "tiny" beyond the band itself, so the threshold is this wiki's reading: an item whose estimate is below the smallest meaningful step of the project's scale.

The join has limits, and those are this wiki's reading. The combined item must still pass [[unit-of-work]]: once started it can be finished without waiting, and its result is presented once. Parts with different priorities should not be joined, since [[story-splitting-patterns]] gives that very difference as a reason to cut. Parts already known to repeat one report belong to [[duplicate-reports]] and not here.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Each item's size | The task, on the project's scale |
| Relatedness | The task text and the area of the code it names |
| Each item's priority | The order on the board |

The combine was wrong if one part held the others back, if the parts were separated again later, or if one part turned out far more urgent than the rest. These tests are this wiki's.

## Trade-off

A combined item loses the separate estimate, and the board shows one item where several reports came in. Cohn accepts the first cost by design ("estimated as a whole rather than individually", L2719). This wiki adds that the reports should stay reachable from the combined task, so that closing it can close them.

## How this differs from a related change

This wiki separates the two by when the work joins. Combining is done while planning, with an estimate and a priority for the whole. A [[related-changes-temptation]] arrives after sizing and is weighed against nothing. The relatedness that helps here does not excuse the change there.

## Agent executor note

Cohn's stated reason, easier prioritizing, sits with whoever orders the work, so it survives an agent executing. Whether an item is tiny has to be read on the project's own scale and not in human days. This wiki expects the saving for a few people steering to lie in review, where one combined result should cost less than several separate ones, but no source here tests that.
