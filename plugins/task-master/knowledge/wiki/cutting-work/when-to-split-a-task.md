---
title: When to Split a Task
category: cutting-work
summary: Three triggers for cutting a task; it exceeds any iteration, it exceeds the room left in this one, or a decision sits close enough to its estimate that a better estimate would change the decision. A task above the ceiling must be cut before work starts and not when it is written, so one far from the top may stay large.
tags: [decision-rule, decomposition, splitting, estimation]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
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

## Cut now or leave it large

A task can be known to be too big long before it has to be cut. The fictional case study in Chapter 23 (L4961) states the position in a coach's voice:

> It’s OK for us to have some big stories, and it’s perfectly fine for us to estimate them with big values. But we need to remember that we’ll have to split them up before working on them so that each fits into an iteration.
>
> — [[cohn-agile-estimating-planning]], L5363

The strong engine story, estimated at 20, is left whole. Asked whether it needs splitting as the weak engine was, the coach says "No, we can do that later, when we’re closer to working on that story" and gives the reason: "We’ll know more then and there’s nothing to gain by splitting it today." (L5451).

**The test.** Cut now if work on the task is close, or if cutting it now gives something usable today. Otherwise record its large estimate and leave it. The deadline is firm in both cases: no task above the ceiling starts. This wording is this wiki's arrangement of the chapter's two reasons.

**A gap in the source.** The same meeting cuts the 20-point weak engine at once (L5385-L5395) and keeps the 20-point strong engine (L5445-L5451), and it states a reason only for keeping one. This wiki's reading is that the weak engine is the earlier work and the strong one depends on what building it teaches. The chapter does not say so, and order has not been discussed at that point.

**Relation to the other rule on timing.** [[how-far-to-split-up-front]] asks how many pieces to enumerate when a large request is cut, and its input is whether starting will teach what the work is. This section asks when to cut at all, and its input is distance from starting. This wiki reads them as agreeing on the mechanism, that work done earlier teaches. The ratio on [[size-ceiling]] carries the same condition, since it applies only once a task nears the top of the order. The opposite move, combining entries finer than this stage needs, is on [[initial-task-inventory]].

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
| Closeness to starting | The task's position in the order |
| Whether a cut now pays | Whether it would change an estimate, an order or a decision someone faces now |

The choice to leave a task whole was wrong if the decision would have gone differently once the real size was known, or if, in board state, a task above the ceiling sits at the top of the order or has already started. The choice to cut for accuracy was wrong if the pieces' estimates led to the same decision the rough number had already supported. A cut was too early if, in history, its pieces were rewritten or thrown away before any of them started, which is the cost "We’ll know more then" (L5451) predicts. These tests are this wiki's.

## Trade-off

Cutting for an estimate spends work on items that may never be done, and Cohn's example avoids that cost: the rough number was "good enough" (L2591). The cost of not cutting is carrying an uncertain number on the plan. A large number stays in any total and it is the least accurate kind (L5363), so a forecast over the list is weakest where the deferred tasks sit. The rule also relies on someone cutting the task when it nears the top.

## Agent executor note

The example is one client anecdote with no measurement. The test sits with whoever decides, so it survives an agent executing. Cohn's assumption that smaller pieces estimate better is a claim about human estimators, and [[size-ceiling]] records that no source here tests it with agents.

Deferring concerns what is known when, so this wiki expects it to survive, with two shifts that no source tests. "We’ll know more then" holds only if the results of earlier tasks reach whoever cuts the later one, so a person has to read them, as on [[how-far-to-split-up-front]]. And the deadline is harder with an agent: a person handed an oversized task may stop and ask, while an agent may simply start, so the check belongs before a task can be taken ([[unit-of-work]]).
