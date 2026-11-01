---
title: Expedite Lane
category: moving-work
summary: An expedite lane is exempt from the board's other limits and can block started work, so its own WIP limit, often one, is the only bound on the flow debt it creates.
tags: [rule, kanban, wip-limit, expedite, flow-metrics]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Expedite Lane

An expedite lane is a separate swimlane on a Kanban board for work allowed to overtake everything else. The source treats it as "One great example of a process taking on Flow Debt" ([[vacanti-actionable-agile-metrics]] L2422). The rule is to keep the lane's WIP limit extremely low, because the lane is exempt from the other limits and its own limit is the only thing bounding what it borrows.

## The usual policies

The source describes these as what most systems do (L2432):

- The lane has "an extremely low WIP limit", "often set to one".
- Lane items "can violate WIP limits at each step in the workflow".
- An expedite "is pulled immediately for work" and may “jump the queue” ahead of other ready work.
- If nobody is free, "many teams will block other items to free up team members" for it.

From these the source concludes that "it is so important to be extremely conservative when setting the WIP limit on an expedite lane" (L2432).

The limit covers the lane as a whole. In the worked example, a limit of one means "only one work item can be in progress in that whole lane at any given time", wherever it sits among Ready, Design, Development and Test (L2440).

## What breaks when it is ignored

In the source's example the expedite reaches Development with no developer free, so the team blocks one or more of the three items in progress. "What has happened is that the team has chosen to artificially age one item (or more) in order to shorten the Cycle Time of another." (L2440) That is [[flow-debt]], and the bill arrives as longer Cycle Times on the blocked items or as discarded work. Blocked items still count against the limit; see [[blocked-work-counts-against-wip]].

## The sign

All of these read from board history or state:

- More expedites open at once than the lane's limit.
- The lane is never empty over a long stretch.
- Other items become blocked at the moment an expedite enters, and stay blocked until it leaves.

The first two are the source's speculative signals (L2468). The third is the source's example stated as a check. How many expedites are too many is resolved on [[hedge-speculative-ponzi]].

## Trade-off

The lane is not condemned: the source allows "very good reasons" to take on hedge-class debt (L2478). Its cost is paid in the predictability of everything else on the board, and a lane that exists makes the exception easy to invoke. The hedge test adds a stricter option than the usual policy, letting existing work finish before the expedite is picked up (L2466). This wiki reads that option as cheaper in debt and slower for the expedite; which holds depends on whether the delay cost of the expedite outweighs the aging of what would be interrupted. See [[cost-of-delay]] and [[interrupting-started-work]].

## Class of service

The source says the chapter was avoiding a term: "Class of Service" (CoS) "is exactly what I am talking about" (L2550). It objects to the usual implementation rather than the idea, saying that "most teams do not know how to implement it properly" (L2550). The full argument, deferred to Chapter 13 (L2552), is on [[class-of-service]]. Chapter 13 also goes further than this page's rule: a low limit bounds concurrency and not frequency, so a lane limited to one and never empty is the failure on [[standing-expedite-lane]].

## Agent executor

The blocking step in the source rests on no people being free. This wiki reads the limit as still applying with an agent executing, since what the lane spends is whatever is scarce, which for a few people steering agents is likely their review and attention. The source does not test this.

## Related

[[flow-debt]], [[what-may-move]], [[wip-control]], [[board-rules-by-setup]], [[priority-inflation]], [[kanban-guide]]
