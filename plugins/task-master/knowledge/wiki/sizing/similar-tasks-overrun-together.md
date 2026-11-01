---
title: Similar Tasks Overrun Together
category: sizing
summary: Durations of similar tasks are correlated, so when the first overruns the rest are likely to, and errors do not cancel; revise the siblings' estimates instead of expecting to make up the time.
tags: [rule, estimation, refinement, board-history]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Similar Tasks Overrun Together

Cohn's point is that the durations of software tasks are not statistically independent: how long one takes says something about how long its neighbours will take. Two consequences follow, which are that errors do not cancel in a total, and that an overrun on one task is evidence about the others.

> Activities are said to be independent if the duration of one activity does not influence the duration of another activity.
>
> — [[cohn-agile-estimating-planning]], L608

Cohn's contrast cases are coin flips and a house, where the time to excavate a basement says nothing about the time to paint the walls, so a late finish on one can be offset by an early finish on another (L608). His software case is a client application: if "the first screen takes 50% longer than scheduled there is a good chance that each of the remaining screens are also going to take longer than planned." (L610). This wiki reads the 50% as an illustration and not a measured figure, and Cohn does not say the rest overrun by the same proportion.

## The rule

When the first of a group of similar tasks overruns its estimate, revise the estimates of the remaining ones upward, and do not plan on recovering the time.

> The real knowledge we should gain in a situation like this is that when an activity takes longer than planned, all similar activities are also likely to take longer than planned.
>
> — [[cohn-agile-estimating-planning]], L612

This wiki reads that as applying to any forecast that adds estimates. Cohn says "If the activities of a development effort are not independent then variations in completion time will not balance out." (L610), so a total that assumes errors will wash out overstates its own confidence.

## Sign of violation

- **In a comment or report:** Cohn's stock phrase, “Yes, I was late this time but I’ll make it up on the rest.” (L612).
- **In board history:** one of a set of similar tasks ran well past its estimate, and the estimates on the remaining ones did not change. This reading is this wiki's.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Estimate and actual of the first task | Task record and board history |
| Which tasks are similar | Task text: same kind of work, same parts of the system |
| Whether the overrun's cause is shared | The first task's record: was the cause particular to that task, or something the others will meet too |

The revision was wrong if the remaining tasks then finish at their original estimates. Cohn does not define "similar" and gives no multiplier, so this wiki sets none, and the third input is this wiki's own addition.

## Two meanings of independent

This word means something different on [[independent-tasks]]. There, Wake's sense is that tasks do not overlap and can be done in any order. Here, Cohn's sense is that their durations are uncorrelated. This wiki notes that the two are separate tests: a set of screens can pass the first and fail the second.

## When the first task really does pay for the rest

There is a real case where the first of a set absorbs most of the effort, as in Wake's "3 points for the first report, then 1 point for each of the others" ([[independent-tasks]]). Cohn rejects the belief that first-item learning makes up an overrun, describing it as a belief that "the knowledge gained from completing the first activity will allow the remaining similar activities to be completed more quickly than called for in the plan." (L612). This wiki reads the two as compatible: Cohn's rule concerns variance against the plan. If the plan already priced the first item higher, then an overrun beyond that price is still evidence about the rest, and the shared infrastructure does not excuse it.

## Why

What breaks if this is ignored is the earliest warning a plan gets. The first overrun is available well before the total is at risk, and treating it as a one-off leaves the plan wrong for the whole of the set. [[overrun-triggers-a-recut]] acts on the overrunning task. This rule acts on its siblings.

## Cost

This wiki notes that revising on one data point will sometimes overcorrect for a task whose trouble was particular to it, which is why the cause is an input.

## Agent executor note

The mechanism sits in the work, in shared unknowns and shared difficulty, so it survives an agent. This wiki adds that the excuse is weaker still with an agent: the expected recovery rests on knowledge carried from the first item to the next, and an agent carries that only if it is written down somewhere the next run reads. That point is unmeasured.
