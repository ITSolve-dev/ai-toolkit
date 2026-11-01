---
title: Waiting Versus Blocked
category: work-states
summary: Stopped work is waiting if an outside party holds it, an expected end is known and nothing can shorten it; otherwise, or once that end has passed, it is blocked.
tags: [decision-rule, work-states, dependencies, kanban]
sources: [radzikowska-waiting-blocked]
created: 2026-11-01
updated: 2026-11-01
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

The test does not depend on who executes, so it survives. An agent adds a case the source does not cover: a task stopped because it needs a decision or a review from the person steering. That fails condition 1, since the person is inside the project, and it fails condition 3, since they can act now. So this wiki classes it as blocked, not waiting. That reading is ours, and it matters because this case is likely to be common.

## Positions

**Kanban Maturity Model:** as above. Other methodologies' positions will be added here as sources are ingested. The transition at expiry is the part of this test most likely to differ among them.

## Related

How each state is handled on the board is on [[blocked-work-counts-against-wip]] and [[parking-lot]]. Whether a stop should have been inside a task at all is on [[sequence-versus-wait]].
