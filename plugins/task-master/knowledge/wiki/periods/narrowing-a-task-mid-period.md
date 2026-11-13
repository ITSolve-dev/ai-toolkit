---
title: Narrowing a Task Mid-Period
category: periods
summary: When a task proves larger than planned during a period, whoever owns scope decides at once to move it out, split it, or reduce its acceptance criteria; the standard of done is never what gives.
tags: [decision-rule, iterations, commitment, acceptance-criteria, cohn]
sources: [cohn-agile-estimating-planning, scrum-guide-2020]
created: 2026-11-01
updated: 2026-11-01
---

# Narrowing a Task Mid-Period

A task found to be bigger than planned during a period needs a decision then, and not a report at the end. The source's instruction is that when a story cannot be completed as planned, developers and customer team "need to collobartively resolve the issue as soon as it’s discovered" ([[cohn-agile-estimating-planning]] L4296; the spelling is the source's).

## The options

The source lists these (L4296, L4300):

1. **Move it out** of the period.
2. **Split it**, keep what can finish, and move the rest to a later period.
3. **Reprioritize**, given what is now known about its cost.
4. **Reduce its acceptance criteria** and accept it under them.

The limit on the fourth:

> They wouldn’t go so far as to accept a buggy or untested version of the story but they may reduce performance requirements, handling of special cases, and so on.
>
> — [[cohn-agile-estimating-planning]], L4296

## Inputs

- The revised size: read from a raised estimate, or from the executor's report that the task is larger than its text said.
- What remains of the period: read from the selected tasks still unfinished.
- The task's priority against what else is selected: read from the order ([[ordering-by-value-and-urgency]]).
- Whether a portion stands alone: the split must leave something that is complete by itself ([[vertical-slice]]).

The decision belongs to whoever owns scope (L4296, L4300).

## What would show the choice wrong

This list is this wiki's.

- The kept portion also fails to finish: the split or the remaining capacity was misjudged.
- A task accepted under reduced criteria comes back as a defect or as a new request for the part removed. The criteria were not reducible, and the owner should have moved the task out.

## Sign of violation

These signs are this wiki's derivation from L4296.

- **In board history:** a task's estimate rose during the period and no decision followed: same scope, same criteria, same period.
- **In board history:** a task sat in an active state to the period's end and the first recorded reaction came after the end.
- **In a task's text:** criteria changed with no statement of who decided and what became of the removed part.

## Discriminating criterion: narrowing versus lowering quality

This page sits against a sign on [[mid-period-change]], which treats a task crossing the finished point against a relaxed check as a breach of the Scrum Guide's "Quality does not decrease" ([[scrum-guide-2020]] L196). The two positions are reconciled as follows, and the reconciliation is this wiki's reading.

- **The standard of done does not move.** Tested, integrated, not known broken. Cohn agrees: no buggy or untested version.
- **A task's own acceptance criteria may move,** by decision of the scope owner, before the task finishes. The Scrum Guide allows this too: "Scope may be clarified and renegotiated with the Product Owner as more is learned." ([[scrum-guide-2020]] L198).

The test is who changed what. A recorded decision that shrinks what the task promises is narrowing. A task passing while a check of the standard of done was skipped is lowering quality. Reduced performance requirements are the hard edge: Cohn places them on the allowed side, and a project with a stated performance floor in its standard of done cannot use that case.

## Trade-offs

This comparison is this wiki's. Narrowing keeps a period's result and spends the removed part, which then needs a home or an explicit drop. Moving out is cleaner, costs the period's result, and leaves partial work to go stale ([[unfinished-at-period-end]]).

## Which setup this applies under

- **Iteration setup:** as above.
- **Flow setup:** there is no period to rescue. The trigger is age, and the response is the recut in [[overrun-triggers-a-recut]]. Options 2 and 4 remain open; option 1 does not apply. This mapping is this wiki's.

## Agent executor note

The source's decision is between two parties, and with a few people steering an agent they are often one. The rule on standing survives unchanged, and it matters more with an agent: an agent under a failing check can make the task pass by reducing what it promises. This wiki's reading is that an agent may propose a narrowing and may not apply one. It stops and reports, in line with [[mid-period-change]], and criteria are changed only by the person steering. Prompt detection improves, since an agent's report arrives at the moment it stops.

Related: [[commitment-over-a-period]], [[all-or-nothing-counting]], [[diagnosing-unfinished-work]], [[testable-acceptance]].
