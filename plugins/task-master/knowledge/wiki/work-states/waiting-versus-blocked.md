---
title: Waiting Versus Blocked
category: work-states
summary: Stopped work is waiting if an outside party holds it, an expected end is known and little or nothing can shorten it; once that end has passed it is blocked, and this wiki also classes as blocked whatever fails those conditions, a branch the source does not state.
tags: [decision-rule, work-states, dependencies, kanban]
sources: [radzikowska-waiting-blocked, kanban-guide, scrum-guide-2020, wester-board-design]
created: 2026-11-01
updated: 2026-11-02
---

# Waiting Versus Blocked

Work that has stopped is in one of two states, and they call for different handling: a waiting item can be set aside until a known time, and a blocked item needs someone to act. The test below comes from the Kanban Maturity Model position in [[radzikowska-waiting-blocked]].

The source defines waiting by three conditions:

> Sometimes a work item is waiting on an external group (another service, customer, or supplier) and stays in this state for a certain amount of time (e.g., by a certain date). When little or nothing can be done to shorten the waiting, the ticket representing the work item can be moved to a “parking lot” until the end of the expected time.
>
> — [[radzikowska-waiting-blocked]], L44

The source then defines the boundary by a clock:

> As soon as the agreed waiting time (service level expectation \[SLE\]) expires, mark and manage the work item as blocked (2).
>
> — [[radzikowska-waiting-blocked]], L53

This wiki reads those as giving a test with three questions and one transition, and that framing is ours. The source also says it recognizes "three types of blockers or waiting items" (L30), but the list did not survive extraction, so a finer division may exist.

## The test

An item is **waiting** only if all three hold:

1. The next step belongs to someone outside the project: another service, a customer or a supplier.
2. There is an expected end, as a date or an agreed time.
3. Little or nothing can be done to shorten it.

Otherwise it is **blocked**. A waiting item becomes blocked at the moment its expected end passes.

The "otherwise blocked" branch is this wiki's. The source defines only the expiry transition (L53), and the Kanban Maturity Model practice it cites describes the parking lot as for "currently waiting or blocked work requests dependent on another service or system" (VZ 3.9, L84), so the source's own line between the two is looser than this two-way test.

## Who resolves a blocked item

The source separates "what kind of blocking issues can be resolved autonomously by the teams" from those that "have to be escalated" (L38-L39). Its machinery of organizational roles and agreed policies assumes a larger organization. For a few people, this wiki reduces it to one question: can the people steering remove this themselves, or does it need someone else?

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Who holds the next step | The task's notes, and the reason it stopped |
| The expected end | The commitment the outside party gave |
| Whether it can be shortened | The people steering |
| Whether the end has passed | Today's date against the expected end, and board history |

The choice was wrong in one of two ways. An item called waiting was really blocked if someone chased it and it moved. An item called blocked was really waiting if it cleared on schedule with nobody acting.

## Agent executor note

The test does not depend on who executes, so it survives. An agent adds a case the source does not cover: a task stopped because it needs a decision from the person steering. That fails condition 1, since the person is inside the project, and it fails condition 3, since they can act now. So this wiki classes it as blocked, not waiting. That reading is ours, and it matters because this case is likely to be common.

A planned review is a different case, and this page used to group the two together. A person reviewing a finished result is not a stop. The review happens in a predictable place and the task goes forward afterwards, so under Wester's test it is a handoff with a state of its own ([[column-versus-attribute]]). The line runs between a review the workflow expects and a decision the executor unexpectedly needs in order to continue.

## Positions

**Kanban Maturity Model:** as above.

**Kanban Guide:** the Guide does not separate waiting from blocked, and has no transition at expiry. It names "Unblocking blocked work." ([[kanban-guide]] L135) and leaves the term undefined. Its SLE is not the source's "agreed waiting time": [[service-level-expectation]] sets out the two meanings.

**Scrum Guide:** the Guide has one word for both, "impediments", which the Scrum Master is to cause the removal of ([[scrum-guide-2020]] L162) and the Daily Scrum is to identify (L240). It draws no line by who holds the next step and has no expiry. The test on this page therefore adds something under an iteration setup and overrides nothing.

**Wester:** treats Blocked and On Hold alike, as "fleeting attributes of work" ([[wester-board-design]] L49), and does not separate them by who holds the next step. This wiki reads the two views as answering different questions. The Kanban Maturity Model's test says which state stopped work is in, and Wester's says how to draw it. A stopped task is in a state of work and is drawn as a marker. The word "wait" in Wester's post mostly means something else, a task ready for someone to take it ([[active-versus-queued]]).

## Related

How each state is handled on the board is on [[blocked-work-counts-against-wip]] and [[parking-lot]], and what a project states in advance about blocked work is on the first of those. Whether a stop should have been inside a task at all is on [[sequence-versus-wait]].
