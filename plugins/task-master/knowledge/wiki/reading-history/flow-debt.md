---
title: Flow Debt
category: reading-history
summary: Cycle Time taken from some in-progress items to finish others sooner, by expedites, blockers or pull order; items passed over in a queue or left blocked age artificially. It is repaid as longer Cycle Times or discarded work, and either way as less predictability. It is detected by comparing the CFD's approximate average Cycle Time with the exact one (greater means accumulating, less means repaying, about equal means neither; roughly 10% and 50% as guides), and graded by Minsky's hedge, speculative and Ponzi questions on whether it can be repaid.
tags: [concept, flow-metrics, cycle-time, predictability, expedite, failure-mode, pull-policy, blocked, method, cumulative-flow-diagram, decision-rule, failure-sign]
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
- An item left in a queue or left blocked ages while others pass it: artificially aged work, below.

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

This wiki draws a consequence the source implies but does not state as a warning: while debt accumulates, the exact average falls, because only the favoured items have finished and the borrowed-from items are not yet in the calculation. A falling average [[cycle-time]] can therefore be borrowing rather than improvement. The check is the comparison of the approximate and the actual average, below. A single falling number is a question to check, in the sense of [[smell-is-not-a-finding]].

## Trade-off

Debt is not forbidden: "I do not want you to conclude that all Flow Debt is bad." (L2456) The source compares a reasonable amount to a mortgage, which is good debt "assuming they can be repaid" (L2478). The working question it leaves is whether the debt can be serviced: "are you able to service the Flow Debt that you have taken out?" (L2478) The Minsky test below turns that into questions about the board.

The source says the same reasoning extends beyond flow: "the concepts in this chapter can be applied to any type of debt that you may incur in your process (e.g., technical debt)" (L2502). It offers this as an aside and supplies no mechanism for it.

## Artificially aged work

A work item is artificially aged when its clock runs for reasons unrelated to the work itself: others are repeatedly pulled ahead of it, or it is blocked and nobody acts on the blocker. This is how flow debt builds on a board with no expedite lane at all.

### Two forms

**Passed over in a queue.** The source's example is an item in the "Design Done" column that "just sits there and never gets pulled into “Development Doing”" because other items are constantly chosen over it ([[vacanti-actionable-agile-metrics]] L2482). Its verdict: "If so, then congratulations, you have Flow Debt." (L2482)

**Blocked and ignored.** "Another example of the creation of Flow Debt might be if you have blocked items that you ignore or do not actively work to get unblocked and moving again as quickly as possible" (L2490). This wiki reads that wording as saying a blocked item is not by itself debt: the ignoring is.

The source lists these with order-of-pull policies "whether they are explicit or not" (L2564), and states that other examples exist (L2500). An unwritten preference produces the same aging as a written one.

### Observable sign

This wiki states the signs from the source's two figures (L2488, L2498) as checks on board history:

- An item in a done-queue column, such as Design Done, with items that entered that column later already pulled past it.
- A blocked item with no recorded action on its blocker across a long stretch.
- At board level, the Approximate Average Cycle Time exceeds the exact one: the comparison of averages below.

The first two are questions rather than verdicts. This wiki adds a discriminator the source does not give: a long-lived item that nobody overtook may simply be large, which is a sizing question ([[hidden-wip-in-large-items]]). Overtaking, or an unattended blocker, is what marks it as aged. Pulling a later item first may also be a deliberate ordering decision, as on [[conditioning-flow]], in which case the question is whether the older item still belongs on the board.

### What it costs

The aged item pays one of the two repayments above. It finishes with a Cycle Time "much longer than they normally would have been" (L2444), which distorts the numbers later reported as capability, or it is dropped once its window has passed, and the time already spent is waste (L2452). The dropped case is where this meets [[closing-what-no-longer-applies]] and [[zombie-issue]].

The source's stable case names the opposite conditions: "you are not allowing items to stay blocked indefinitely, and you are not allowing items to queue arbitrarily" (L2522).

### Remedy and its cost

The source's direction is to make the policy explicit and consider restoring stability through it: "Think about what process policies you can put in place to restore some stability to your system." (L2542) It names no specific policy here. Pulling strictly by arrival would remove overtaking, but this wiki notes that doing so spends the freedom to order by value, so the trade sits with [[ordering-by-value-and-urgency]]. The chapter does not settle it.

### Agent executor note on aged work

This wiki reads aging as independent of who executes, because the clock runs on the board. A person steering agents may produce the same sign through the review queue, with presented results waiting while newer ones are looked at first. The source does not address this.

### Related to aged work

[[expedite-lane]], [[active-versus-queued]], [[waiting-versus-blocked]], [[blocked-work-counts-against-wip]], [[lateness-passes-down-the-schedule]]

## Detecting it: approximate versus actual average Cycle Time

This method tests a board's history for flow debt by comparing two averages over the same items and interval. One is the Approximate Average Cycle Time read from a [[cumulative-flow-diagram]]. The other is the exact Average Cycle Time computed from the data behind that chart. Their difference is the point of the exercise, which is why the approximation is worth having when the exact figure is available.

### Inputs and where they come from

- **Approximate Average Cycle Time:** the horizontal distance between two lines on the CFD, per CFD Property #4, which "represents the Approximate Average Cycle Time for items that finished between the two workflow steps represented by the chosen two lines" ([[vacanti-actionable-agile-metrics]] L2380).
- **Exact Average Cycle Time:** computed "from the very data used to build the CFD to begin with" (L2396). Both are read from board history, with no logged hours involved.
- **The interval:** the reading holds only "for the time interval under consideration" (L2506).

### Why the comparison means anything

The source ties it to [[littles-law]] Assumption #4:

> Little’s Law Assumption #4: For the time period under consideration, the average age of WIP should neither be increasing nor decreasing.
>
> — [[vacanti-actionable-agile-metrics]], L2394

The source says the comparison shows "if we can expect our exact Average Cycle Time to grow, decline, or stay the same over time", and that growth or decline means "a violation of Little’s Law assumption #4 which means that our predictability is in jeopardy" (L2396).

### The three readings

| Comparison | Reading | What it means for predictability |
|---|---|---|
| Approximate greater than exact | Accumulating flow debt (L2414, L2572) | Some items were favoured; others are ageing and not yet counted |
| Approximate less than exact | Paying off flow debt (L2506, L2574) | Items that "languished in progress are now finally completing" and inflate the average (L2508) |
| Roughly equal | Neither accumulating nor repaying (L2522, L2576) | "You are not overloaded with expedite requests, you are not allowing items to stay blocked indefinitely, and you are not allowing items to queue arbitrarily." (L2522) |

The source treats the first two as both risky, since accumulating and repaying each damage predictability (L2406, L2510-L2516). The mnemonic it offers is “scenario three is where you want to be.” (L2406)

### Conditions on the reading

- **The system must be otherwise stable.** "these conclusions can only be drawn assuming we are running an otherwise stable system (i.e., nothing about the underlying system design has changed materially)" (L2518). The sign to check first is a change to the board's columns, limits or policies inside the interval.
- **Equality does not certify health.** The source warns "That is not to suggest that there are not any other areas of your process that are unhealthy" (L2524), so a match clears flow debt and nothing else.

### How different is different

The source gives a rough guide and refuses a threshold. Some gap is expected because one figure is an approximation. "If the difference is about 10%, then you might not get too excited. However, if the difference is 50%, then that might be a pretty good clue to take action." (L2536) The answer is otherwise "highly context specific" (L2534), learned over time. These two percentages are a practitioner's rule of thumb from no stated dataset, and the source gives no minimum number of finished items.

This wiki adds a caution for a board worked by a few people, which the source does not address: with few finished items, one item can move an average a long way. Before reading a large gap as debt, look at which items produce it.

### What later fact would show the reading wrong

This wiki derives the check from the two forms of repayment (L2444-L2452). A reading of "accumulating" predicts that the passed-over items will either finish with unusually long Cycle Times, raising the exact average, or be discarded. If neither happens over following intervals, the gap was approximation error or a change in the system.

### Related to the comparison

[[cumulative-flow-diagram]], [[littles-law]], [[smell-is-not-a-finding]], [[service-level-expectation]], [[flow-metrics]]

## Can it be repaid: hedge, speculative or Ponzi

This rule classifies how a process takes on flow debt, borrowing the three debtor types of the economist Hyman Minsky (spelled "Minski" in the source). A hedge borrower can service principal and interest, a speculative borrower only the interest, and a Ponzi borrower must "constantly issue new debt in order to service the old" ([[vacanti-actionable-agile-metrics]] L2374). Applied to a board, the question is whether expediting leaves room to repay what it borrowed.

The source caps the effort: "I am not advocating that you spend a lot of time on this classification" (L2472). The classification serves one question, "are you able to repay the debt that you are taking out?" (L2472-L2478, joined across a page break)

### The test

| Type | A yes to these places the board here | Where to read it |
|---|---|---|
| **Hedge** (L2460-L2466) | Are expedites more the exception than the rule? Is only one item, or a WIP-limited number, ever in the process at a time? Does time without expedites allow finishing work that was blocked for earlier expedites? May existing work finish before an expedite is picked up? | Board history: intervals with an expedite open, peak concurrent expedites against the limit, and whether blocked items resume afterwards |
| **Speculative** (L2468) | Is there never a time without expedited work of some kind? Is the expedite WIP limit routinely violated? | Board history: whether the expedite count ever reaches zero, and how often it exceeds the limit |
| **Ponzi** (L2470) | Is all work treated as an expedite? Do expedites take all capacity so normal items never get worked? Are pull criteria based "not on explicit policies but on whomever is screaming the loudest"? | Board history for the first two; the stated pull policy, if there is one, for the third |

The source's verdicts are hedged: a yes means you are "probably" running that kind of system (L2466, L2468). It advises a speculative system to "explore some options to apply more rigor to your expedite process" (L2468).

### What a Ponzi process looks like from outside

"You will never be able to repay the debt you have accumulated and any notion of total process predictability is gone." (L2470) The source's practical consequence is that starting normal work there is self-deception, because "That normal work will almost never complete, or it will swapped out for other work, or it will finish far too late for anyone to care." (L2470)

Those three outcomes are observable: normal items that stay open, normal items removed in favour of others, and normal items finishing after their value is gone.

### What later fact would show the choice wrong

This wiki derives this from the repayment forms above. A board classed as hedged should see passed-over items finish in the following quiet time at near-normal Cycle Times. If they finish far beyond the usual range or are discarded, the board was not hedged. Approximate average Cycle Time running persistently above the exact one over several intervals points the same way.

### Reading the edges

The source leaves mixed answers unresolved, for instance rare expedites that nevertheless exceed the limit. This wiki files a mixed result under the more severe type, as a question to check rather than a verdict, per [[smell-is-not-a-finding]].

The source also pulls against itself. It reports as normal policy that an expedite "is pulled immediately for work" (L2432), yet one Hedge question asks "are you allowed to finish existing work before the expedite is picked up?" (L2466). This wiki reads the first as a description of what most systems do and the second as the test, so a board that always interrupts started work fails that question even with rare expedites. See [[interrupting-started-work]].

The questions assume a visible expedite class. Because an explicit lane is not the only route to debt (L2480), this wiki applies them to a board with no lane by counting items that jumped ahead of the queue.

### Trade-off

Hedge debt is acceptable and sometimes right: "there are going to be some very good reasons to take on “Hedge” Flow Debt from time to time" (L2478). The classification costs little, but it invites an argument about labels; the source says what matters is the conversation about repayment (L2502).

### Related to the Minsky test

[[expedite-lane]], [[priority-inflation]], [[urgent-versus-important]], [[cost-of-delay]]

## Whether it survives an agent executing

The source's examples depend on people: "no developers were available" (L2440) and blocking items "to free up team members" (L2432). This wiki reads the mechanism as surviving an agent executor, with the scarce resource changed. An item's age runs on the board regardless of who executes, so any item nobody is acting on still ages. Where several tasks can run at once, the borrowing is likely to happen at the steering person's attention and review rather than at execution. The source does not test this.

## Related

[[flow-metrics]], [[cumulative-flow-diagram]], [[littles-law]], [[interrupting-started-work]], [[blocked-work-counts-against-wip]], [[lateness-passes-down-the-schedule]]
