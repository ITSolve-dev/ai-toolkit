---
title: Queue Buildup
category: moving-work
summary: Started work piling up without finishing, which Vacanti treats as the observable form of poor flow; the project feels it as work taking too long, and iterations do not by themselves prevent it.
tags: [failure-mode, flow, wip, queues, board-health]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Queue Buildup

A queue is a buildup of started work that is not finishing. Vacanti treats it as the main sign that flow, which he defines as "the movement and delivery of customer value through a process" ([[vacanti-actionable-agile-metrics]] L412), has gone wrong: "A telltale sign of a suboptimal flow is a large buildup of work somewhere in your process." and "Large queues generally mean no flow." (L414).

## Observable sign

The source gives the shape and leaves the reading to the reader. The signs below are this wiki's derivation.

- **On the board:** many items between the started and finished points, with ages growing and few finishing.
- **On the board:** one state holding far more items than those after it, which is where the buildup sits.
- **In history:** starts exceed finishes over a span of weeks.

A sign raises a question ([[smell-is-not-a-finding]]). A pile-up that the project declared intended, or one that clears on a known cycle, is not this failure. The source's word "large" has no number, so this wiki reads the sign as a trend against the project's own history and not as a threshold.

## How work gets stuck

The source says queues form "when work items that have been started just get stuck" (L416), and it lists four causes (L416-L422):

1. No resources are free to continue the item.
2. A manager mandates starting new work before current work has finished.
3. The people doing the work are pulled in several directions and cannot focus on one thing.
4. The item depends on "some external team or vendor".

The list is not exhaustive: "Work may get stuck for all of those reasons and more." (L424). Cause 4 is treated on [[waiting-versus-blocked]] and [[parking-lot]].

## Why it goes unseen

> Unfortunately, your project management framework makes you blind to queues. You are blind to them because you are never asked to look for them in the first place.
>
> — [[vacanti-actionable-agile-metrics]], L426

The author says what is felt instead is that "work takes too long to complete" (L428). This wiki reads that as the diagnostic trap: the complaint is about duration, so the response goes to duration, and the count of open work is never read. [[active-versus-queued]] covers the related case where a column hides waiting work.

## Responses that miss

> Traditional project management responses to elongated completion times might be to constantly refigure project plans, to continuously revisit resource assignments, and to force teams to work overtime. Not only do those actions not solve the core problem, but in most instances they tend to make things worse.
>
> — [[vacanti-actionable-agile-metrics]], L428

The source gives no measurement for "make things worse", so this wiki keeps the mechanism only: none of the three reduces what is open. Overtime is out of scope as a matter of managing people. The response that adds to the queue outright is on [[starting-more-work-when-cycle-time-is-long]].

## What to do

The source gives two moves in sequence. Once stuck work exists, "Management of flow, therefore, usually begins by attempting to “unstick” stuck work." (L424). The better move is earlier: "The best way to fix the problem of large queues is not to allow them to form in the first place." (L434). The preventive rule is on [[wip-control]].

## Which setup this applies under

The source says iterations do not protect a project: "you might assume that iterations or sprints insulate you from large queues" (L426), and it says that assumption fails if the symptoms on [[signs-of-poor-flow]] are present. [[wip-lengthens-cycle-time]] records that Cohn's iteration setup clears work in process by the calendar.

The resolution is this wiki's. Both can hold, because they concern different queues.

- **Iteration setup:** the period's end limits how long a queue lives only if unfinished work is actually returned and not rolled into the next period ([[unfinished-at-period-end]]). Inside the period a queue can still form, so read the count mid-period as well.
- **Flow setup:** no calendar clears anything, so the bound on [[wip-control]] is the only thing that limits the queue.

## Cost of preventing it

The cost falls on requesters: new work waits while old work finishes (L234).

## Agent executor note

Causes 1 and 3 depend on human capacity and attention, and this wiki does not expect them to survive at execution, since an agent can run in parallel and has no focus to lose. Causes 2 and 4 survive: a person steering can launch one more run as easily as a manager can mandate a start, and outside dependencies do not change. This wiki expects the queue to form at review, where finished runs wait for the few people steering, which matches its reading on [[wip-control]] and [[wip-lengthens-cycle-time]]. That reading is unmeasured.
