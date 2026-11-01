---
title: Gap on a Scatterplot
category: reading-history
summary: A gap means nothing finished in that interval, and it lines up with a flat bottom line on the CFD; stacks at sprint boundaries with thin data between them are the batch-transfer form.
tags: [failure-mode, scatterplot, batch-transfer, cycle-time, iterations]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Gap on a Scatterplot

A gap on a [[cycle-time-scatterplot]] is an interval with no dots. Vacanti defines it plainly: “Gaps in the dots on your Scatterplot means that no work items finished in that particular time interval.” ([[vacanti-actionable-agile-metrics]] L2922). It measures finishing, not working, so a gap does not show that nothing happened, only that nothing completed.

## Reading it

A gap is the same event as a flat section on the [[cumulative-flow-diagram]], as on [[flat-lines-on-a-cfd]]: “Flat lines on the CFD mean nothing completed; if nothing has completed then no dots will show up on your Scatterplot.” (L2922). This wiki reads the two charts as confirming each other, so the interval should match.

The causes Vacanti lists are the ones that flatten throughput on a CFD: “public holidays, external blockers, batch transfer, etc.” (L2922). The chapter's checklist says “Long periods of gaps in the data” (L3002) and gives no duration.

| Cause | How to tell |
|---|---|
| Holiday or planned absence | The interval matches a known calendar date; no action |
| External blocker | Items sat in place through the interval and share an outside dependency; see [[waiting-versus-blocked]] |
| Batch transfer | Gaps repeat on a rhythm, with stacks of dots between them |

The “how to tell” column is this wiki's, built on the causes Vacanti names. The inputs all come from board history and the project's calendar.

## Batch transfer: stacks at the boundary

Vacanti singles out the batch-transfer form, common on Scrum boards: “The stacks of dots that you see here are at the sprint boundaries when there is a mad rush to complete work items. But look at how the data thins out between those stacks.” (L2934). He leaves the assessment as questions: whether it is good or bad, and “what impact is this having on our predictability?” (L2934). The same event on a CFD is [[stair-steps-on-a-cfd]].

This wiki answers those per project setup, and the answer is ours rather than the source's.

- **Timeboxed setup.** Stacks at the boundary are the visible form of [[end-of-period-crunch]]. The question is which of two things is happening: work really finishing in a rush, or work finished earlier and only marked at the boundary. A rush is a process finding; a late mark means the dates misreport and the cycle times are inflated by the wait for the boundary.
- **Flow setup, no period boundary.** There is no boundary to explain a stack, so a repeating stack points at a batched handoff somewhere, such as review or release done on a rhythm.
- **In either setup, the effect on predictability.** The wiki reads stacked dots as measuring the cadence as much as the work: an item's cycle time then depends on where in the cycle it started. Percentiles taken from such data describe that mix, which is worth stating when a [[service-level-expectation]] is drawn from it.

**Later fact that would show the reading wrong:** finish dates spread out once the handoff or the boundary habit changes, or fail to, which also tells whether the stacks came from the policy assumed.

## Survival under an agent

The gap survives unchanged, since it reads finish events. This wiki's judgement is that the batch-transfer form becomes more likely with an agent executing and a person steering: an agent can finish several tasks while the person is away, so if “finished” means accepted, the dots land together on the review day. Whether such a stack is a defect depends on where the board's finished point sits; see [[started-and-finished-points]]. That transfer is the wiki's own and is unsourced. See also [[reading-a-cycle-time-scatterplot]].
