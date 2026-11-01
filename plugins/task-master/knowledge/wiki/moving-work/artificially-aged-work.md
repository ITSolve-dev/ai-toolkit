---
title: Artificially Aged Work
category: moving-work
summary: An item that waits in a queue while others are pulled past it, or sits blocked with nobody working to free it, ages for reasons unrelated to its size and creates flow debt without any expedite lane.
tags: [failure-mode, flow-metrics, pull-policy, blocked, cycle-time]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Artificially Aged Work

A work item is artificially aged when its clock runs for reasons unrelated to the work itself: others are repeatedly pulled ahead of it, or it is blocked and nobody acts on the blocker. This is how [[flow-debt]] builds on a board with no expedite lane at all.

## Two forms

**Passed over in a queue.** The source's example is an item in the "Design Done" column that "just sits there and never gets pulled into “Development Doing”" because other items are constantly chosen over it ([[vacanti-actionable-agile-metrics]] L2482). Its verdict: "If so, then congratulations, you have Flow Debt." (L2482)

**Blocked and ignored.** "Another example of the creation of Flow Debt might be if you have blocked items that you ignore or do not actively work to get unblocked and moving again as quickly as possible" (L2490). This wiki reads that wording as saying a blocked item is not by itself debt: the ignoring is.

The source lists these with order-of-pull policies "whether they are explicit or not" (L2564), and states that other examples exist (L2500). An unwritten preference produces the same aging as a written one.

## Observable sign

This wiki states the signs from the source's two figures (L2488, L2498) as checks on board history:

- An item in a done-queue column, such as Design Done, with items that entered that column later already pulled past it.
- A blocked item with no recorded action on its blocker across a long stretch.
- At board level, the Approximate Average Cycle Time exceeds the exact one: [[approximate-versus-actual-cycle-time]].

The first two are questions rather than verdicts. This wiki adds a discriminator the source does not give: a long-lived item that nobody overtook may simply be large, which is a sizing question ([[hidden-wip-in-large-items]]). Overtaking, or an unattended blocker, is what marks it as aged. Pulling a later item first may also be a deliberate ordering decision, as on [[conditioning-flow]], in which case the question is whether the older item still belongs on the board.

## What it costs

The aged item pays one of the two [[flow-debt]] repayments. It finishes with a Cycle Time "much longer than they normally would have been" (L2444), which distorts the numbers later reported as capability, or it is dropped once its window has passed, and the time already spent is waste (L2452). The dropped case is where this meets [[closing-what-no-longer-applies]] and [[zombie-issue]].

The source's stable case names the opposite conditions: "you are not allowing items to stay blocked indefinitely, and you are not allowing items to queue arbitrarily" (L2522).

## Remedy and its cost

The source's direction is to make the policy explicit and consider restoring stability through it: "Think about what process policies you can put in place to restore some stability to your system." (L2542) It names no specific policy here. Pulling strictly by arrival would remove overtaking, but this wiki notes that doing so spends the freedom to order by value, so the trade sits with [[ordering-by-value-and-urgency]]. The chapter does not settle it.

## Agent executor

This wiki reads aging as independent of who executes, because the clock runs on the board. A person steering agents may produce the same sign through the review queue, with presented results waiting while newer ones are looked at first. The source does not address this.

## Related

[[expedite-lane]], [[active-versus-queued]], [[waiting-versus-blocked]], [[blocked-work-counts-against-wip]], [[lateness-passes-down-the-schedule]]
