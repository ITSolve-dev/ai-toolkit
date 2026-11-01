---
title: Natural Order of Work
category: ordering
summary: Most dependencies between stories just follow the order estimates assumed; working out of that order adds enabling tasks but rarely lengthens a project, and when it does the reason for reordering justifies it.
tags: [rule, dependencies, ordering, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Natural Order of Work

The natural order of a set of stories is the sequence "that makes sense to both developers and the product owner" ([[cohn-agile-estimating-planning]] L3210), and it is usually the sequence assumed when they were estimated (L3212). Cohn's claim is that dependencies following that order are not a problem, and that departing from it has a cost that can be read in advance.

## What leaving the order costs

> When stories are worked on in a sequence other than what was assumed when estimating, during iteration planning the team will often have to include additional tasks that make it possible to work on stories in the new order.
>
> — [[cohn-agile-estimating-planning]], L3212

Cohn's example shows a swimmer's fastest times before building the screens that add swimmers. The team must design the tables earlier and put a swimmer into the database directly (L3214-L3216). This wiki reads that as a dependency that is a sequence and not a wait: nobody is blocked, the prerequisite can be stood in for, and the price is extra work ([[sequence-versus-wait]]).

## Does it take longer

Cohn's answer is "Two answers: Probably not and it doesn’t matter." (L3218).

- **Probably not:** "all we’ve done is shift some tasks from one user story to another" (L3220). The later story gets cheaper by what the earlier one absorbed. Any shift of estimate between the two usually washes out, and Cohn has seen it lean slightly pessimistic, because the extra point is done but not credited, slightly understating velocity (L3222-L3226).
- **It doesn't matter:** the order was chosen for a reason, such as addressing a technical risk earlier or getting earlier feedback, which can "potentially save a month or two of rework near the end of the project" (L3228).

Both answers are coaching judgement, unmeasured. The second depends on a good reason existing: Cohn says "presumably" (L3228).

## The rule

This statement of the rule is this wiki's. Order by value and risk, and let a dependency change the order only when the enabling work costs more than the gain from going early. When going out of order, add the enabling work explicitly. Cohn's own condition covers the estimates: if the shift is significant, "re-estimate the stories involved as soon as you decide to work on them in other than the natural order" (L3226).

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The assumed order | Dependencies stated in task text, and what each estimate assumed |
| The enabling work | What the later task needs that does not exist yet |
| The reason to go early | Risk or feedback named on the task |

The choice was wrong if the risk the reordering addressed never materialized or the early feedback changed nothing. It was also wrong if the enabling work was thrown away instead of being absorbed by the later task, which breaks Cohn's first answer.

## Trade-off

Going out of order spends work earlier and asks for stand-ins, such as hand-entered data. That is accepted in exchange for learning sooner. The stand-ins need removing or absorbing later.

## Agent executor note

A natural order is understood by people who share a picture of the product. An executor that guesses does not recall what the estimate assumed. This wiki therefore reads the assumed order as a fact the task must state, including what it expects to exist already ([[recoverable-versus-task-only-facts]]). The accounting about velocity concerns a team's numbers and carries over unchanged.

## Related

Tasks with no ordering constraint are on [[independent-tasks]]. Whether to leave a dependency or stub it out is on [[handling-a-sequence-dependency]]. Ranking itself is on [[ordering-by-value-and-urgency]]. A low-ranked story that has to move up because something needs it is on [[value-order-versus-technical-necessity]].
