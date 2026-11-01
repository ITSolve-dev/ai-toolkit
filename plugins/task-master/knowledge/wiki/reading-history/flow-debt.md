---
title: Flow Debt
category: reading-history
summary: Cycle Time taken from some in-progress items to finish others sooner; it is repaid as longer Cycle Times or discarded work, and either way as less predictability.
tags: [concept, flow-metrics, cycle-time, predictability, expedite]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Flow Debt

Flow debt is Vacanti's name for what happens when some work finishes faster than it normally would at the expense of other work already in progress. Capacity is not created by favouring an item, so the time has to come from somewhere, and the items it came from age while nobody acts on them.

> Flow Debt is when Cycle Time is artificially reduced for some items of Work In Progress by “borrowing” Cycle Time from other items of work in progress.
>
> — [[vacanti-actionable-agile-metrics]], L2418

The source says the favouring can happen "either explicitly or implicitly" (L2420), so it need not be a decision anyone recorded, and that "This new ability to complete some items faster than they normally would have finished must have come from somewhere." (L2420)

## Where it comes from

The chapter's takeaways name three sources (L2558-L2564): classes of service, blockers, and "Other order of pull policies in place (whether they are explicit or not)".

- An expedited item takes capacity from items already started: [[expedite-lane]].
- An item left in a queue or left blocked ages while others pass it: [[artificially-aged-work]].

The source is explicit that a lane is not required: "an explicit expedite lane is not the only way to incur Flow Debt" (L2480).

## How it is repaid

The source gives two forms of repayment (L2444-L2452).

1. **Longer Cycle Times.** Passed-over items eventually finish, with Cycle Times far longer than normal. The average that was trusted turns out wrong, "because the metrics you had collected did not include this debt" (L2444).
2. **Discarded work.** Passed-over items are dropped because their window of value has closed, and "any effort or time that has been spent on progressing them through the system immediately becomes waste" (L2452). The source marks this as a violation of [[conservation-of-flow]].

> Either way, Flow Debt is repaid in the form of less predictability for your process.
>
> — [[vacanti-actionable-agile-metrics]], L2454

The source adds that repaying does not restore predictability while it happens. "Items that finish with large amounts of Flow Debt attached to them skew Cycle Time numbers." (L2516) The resulting variability means "we must communicate a larger range for the SLA of our process" (L2516), which ties debt directly to [[service-level-expectation]].

The chapter's closing takeaway gives the mechanism under both: the aged items must eventually leave the system, and that "leads not only to longer overall Cycle Times, but more variability in your Cycle Time data" (L2578).

## The trap when reading metrics

This wiki draws a consequence the source implies but does not state as a warning: while debt accumulates, the exact average falls, because only the favoured items have finished and the borrowed-from items are not yet in the calculation. A falling average [[cycle-time]] can therefore be borrowing rather than improvement. The check is [[approximate-versus-actual-cycle-time]]. A single falling number is a question to check, in the sense of [[smell-is-not-a-finding]].

## Trade-off

Debt is not forbidden: "I do not want you to conclude that all Flow Debt is bad." (L2456) The source compares a reasonable amount to a mortgage, which is good debt "assuming they can be repaid" (L2478). The working question it leaves is whether the debt can be serviced: "are you able to service the Flow Debt that you have taken out?" (L2478) [[hedge-speculative-ponzi]] turns that into questions about the board.

The source says the same reasoning extends beyond flow: "the concepts in this chapter can be applied to any type of debt that you may incur in your process (e.g., technical debt)" (L2502). It offers this as an aside and supplies no mechanism for it.

## Whether it survives an agent executing

The source's examples depend on people: "no developers were available" (L2440) and blocking items "to free up team members" (L2432). This wiki reads the mechanism as surviving an agent executor, with the scarce resource changed. An item's age runs on the board regardless of who executes, so any item nobody is acting on still ages. Where several tasks can run at once, the borrowing is likely to happen at the steering person's attention and review rather than at execution. The source does not test this.

## Related

[[flow-metrics]], [[cumulative-flow-diagram]], [[littles-law]], [[interrupting-started-work]], [[blocked-work-counts-against-wip]], [[lateness-passes-down-the-schedule]]
