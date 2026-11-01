---
title: When to Split a Task
category: cutting-work
summary: Three triggers for cutting a task; it exceeds any iteration, it exceeds the room left in this one, or a decision sits close enough to its estimate that a better estimate would change the decision.
tags: [decision-rule, decomposition, splitting, estimation]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# When to Split a Task

Cohn gives two occasions for cutting a task, which he calls a story, and divides the first in two, which makes three triggers (L2583, L2591, L2725 of [[cohn-agile-estimating-planning]]). Two are about fit and one is about knowledge. The third is conditional, and that condition is the useful part: size alone is not a reason to cut work that is still far away.

## The triggers

**It does not fit any iteration.** Cohn says "a user story should be split when it is too large to fit within a single iteration" (L2583), and "there’s no choice but to split the story into two or more stories" (L2579). This is the outer bound on [[size-ceiling]].

**It does not fit the iteration being planned.** A task may fit an iteration in general and still be too big now, because "it won’t fit within the iteration being planned because there isn’t enough room" (L2583). This wiki adds a limit to that trigger: a piece cut to fill leftover room still has to pass [[unit-of-work]] and be a [[vertical-slice]]. If the only piece that fits has nothing to show, the task waits for a later period and is not cut to fill the room. How much a period takes is on [[filling-a-period]].

**A decision depends on a better estimate.** "it can be useful to split a large user story (an epic) if a more accurate estimate is necessary" (L2591). Cohn's example shows when it is not necessary. A product owner weighing features for customer service representatives at other companies wrote one large story, and the team estimated it at 70 points:

> She knew there was a great deal of uncertainty in the estimate, but even if the estimate were off by 100% these features were still worth doing. If 70 story points had put her on the border of whether or not to include the CSR features in the release, she could have chosen to split the large story and have the team estimate the smaller stories.
>
> — [[cohn-agile-estimating-planning]], L2591

This wiki reads that as the test: stretch the estimate across its uncertainty and see whether the decision changes. If it holds at both ends, a rough number is enough and cutting buys nothing. If it flips, cut, because the cut is what removes the uncertainty.

## Timing

Cohn places splitting late: "As user stories rise to the top of the release plan, meaning they will be implemented soon, they often need to be split." (L2579). This wiki reads that as agreement with [[how-far-to-split-up-front]] and [[estimating-by-horizon]]: a large item further out stays large unless a decision needs otherwise. The third trigger is the exception, and it applies at any distance.

## Under which setup

The resolution is this wiki's, and Cohn does not address a project without iterations.

- **With iterations:** all three triggers apply as stated.
- **Without iterations:** the first two have no denominator. Use the setup rules on [[size-ceiling]] in their place. The third trigger still holds wherever a decision depends on a number.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The task's estimate | The task, on the project's scale |
| Iteration capacity and remaining room | Board history and the current period, where iterations exist |
| The decision resting on the estimate | The request, or the person steering |
| The estimate's uncertainty | The estimator's statement; Cohn gives no figure beyond the 100% in his example |

The choice to leave a task whole was wrong if the decision would have gone differently once the real size was known. The choice to cut for accuracy was wrong if the pieces' estimates led to the same decision the rough number had already supported. Both tests are this wiki's.

## Trade-off

Cutting for an estimate spends work on items that may never be done, and Cohn's example avoids that cost: the rough number was "good enough" (L2591). The cost of not cutting is carrying an uncertain number on the plan.

## Agent executor note

The example is one client anecdote with no measurement. The test sits with whoever decides, so it survives an agent executing. Cohn's assumption that smaller pieces estimate better is a claim about human estimators, and [[size-ceiling]] records that no source here tests it with agents.
