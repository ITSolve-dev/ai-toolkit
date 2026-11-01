---
title: Order by Value, Not Convenience
category: ordering
summary: A plan that assumes everything will be finished has no reason to order by value, so it orders for the builders' convenience, and when time runs out the features dropped may outrank the ones delivered.
tags: [rule, ordering, prioritization, board-history]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Order by Value, Not Convenience

Order matters because it decides what is lost when time runs out. Cohn names this the third cause of planning failure: "the work described by the plan is not prioritized by the value to the users and customer." ([[cohn-agile-estimating-planning]] L650).

> Many traditional plans are created with the assumption that all identified activities will be completed. This means that work is typically prioritized and sequenced for the convenience of the development team.
>
> — [[cohn-agile-estimating-planning]], L650

This wiki reads the assumption as the root of the fault. Cohn states its logic: "if all work will be completed then project customers have no preference about the sequence in which that work is done." (L654). This wiki adds that if everything really were finished the order would matter less, and the assumption is what fails: near the end the team drops features to meet the schedule (L654).

## The rule

Order work by the value of the result to whoever receives it, on the assumption that the plan may not be finished. How to rate value is on [[ordering-by-value-and-urgency]] and [[cost-of-delay]]. The wording is this wiki's.

## Sign of violation

- **In board history:** what was dropped or left unfinished outranks what was finished. This is Cohn's outcome: "some of the features dropped are of greater value than those that are delivered." (L654).
- **In a plan's reasoning:** the sequence is justified by what is efficient to build next, with no statement of value.
- **In a plan's assumptions:** no statement of what gives way if time runs short.

The last two are this wiki's. The third leans on an omission, which the charter does not accept as the sign of a rule that chooses, so it only supports the first two.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Value of each result | The task's stated purpose and the person steering ([[task-must-justify-itself]]) |
| Order forced by dependency | Stated dependencies ([[sequence-versus-wait]], [[independent-tasks]]) |

The order was wrong if, when work stops, a dropped task would have been chosen over one that was delivered. Cohn gives no method for rating value in this chapter.

## Why

What breaks is the plan's behaviour under failure. To the receiver the work seems to proceed in "a relatively haphazard order" (L654). This wiki reads the cuts at the end as then falling on whatever happened to be last, so the cut features are chosen by the calendar and not by anyone's judgement of worth.

## Cost

This wiki notes that value order can be less efficient to build, so it costs some rework or a less tidy sequence. A real dependency still constrains order, and [[independent-tasks]] gives the moves that reduce it.

## Agent executor note

The rule concerns what is lost when work stops, and does not depend on who executes it, so it survives. Convenience for a development team is a human cost, and an agent has less of it. This wiki adds that an agent's own sequencing, left unsupervised, has no knowledge of value unless the task carries it, so the failure can recur without a team's convenience being involved. That point is unmeasured.
