---
title: Hedge, Speculative or Ponzi Flow Debt
category: reading-history
summary: Questions about expedite frequency, limit adherence and pull policy that place a board's borrowing in one of Minsky's three debtor types, to answer whether its flow debt can be repaid.
tags: [decision-rule, flow-metrics, expedite, predictability, failure-sign]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Hedge, Speculative or Ponzi Flow Debt

This rule classifies how a process takes on [[flow-debt]], borrowing the three debtor types of the economist Hyman Minsky (spelled "Minski" in the source). A hedge borrower can service principal and interest, a speculative borrower only the interest, and a Ponzi borrower must "constantly issue new debt in order to service the old" ([[vacanti-actionable-agile-metrics]] L2374). Applied to a board, the question is whether expediting leaves room to repay what it borrowed.

The source caps the effort: "I am not advocating that you spend a lot of time on this classification" (L2472). The classification serves one question, "are you able to repay the debt that you are taking out?" (L2472-L2478, joined across a page break)

## The test

| Type | A yes to these places the board here | Where to read it |
|---|---|---|
| **Hedge** (L2460-L2466) | Are expedites more the exception than the rule? Is only one item, or a WIP-limited number, ever in the process at a time? Does time without expedites allow finishing work that was blocked for earlier expedites? May existing work finish before an expedite is picked up? | Board history: intervals with an expedite open, peak concurrent expedites against the limit, and whether blocked items resume afterwards |
| **Speculative** (L2468) | Is there never a time without expedited work of some kind? Is the expedite WIP limit routinely violated? | Board history: whether the expedite count ever reaches zero, and how often it exceeds the limit |
| **Ponzi** (L2470) | Is all work treated as an expedite? Do expedites take all capacity so normal items never get worked? Are pull criteria based "not on explicit policies but on whomever is screaming the loudest"? | Board history for the first two; the stated pull policy, if there is one, for the third |

The source's verdicts are hedged: a yes means you are "probably" running that kind of system (L2466, L2468). It advises a speculative system to "explore some options to apply more rigor to your expedite process" (L2468).

## What a Ponzi process looks like from outside

"You will never be able to repay the debt you have accumulated and any notion of total process predictability is gone." (L2470) The source's practical consequence is that starting normal work there is self-deception, because "That normal work will almost never complete, or it will swapped out for other work, or it will finish far too late for anyone to care." (L2470)

Those three outcomes are observable: normal items that stay open, normal items removed in favour of others, and normal items finishing after their value is gone.

## What later fact would show the choice wrong

This wiki derives this from the repayment forms on [[flow-debt]]. A board classed as hedged should see passed-over items finish in the following quiet time at near-normal Cycle Times. If they finish far beyond the usual range or are discarded, the board was not hedged. [[approximate-versus-actual-cycle-time]] running persistently above equal over several intervals points the same way.

## Reading the edges

The source leaves mixed answers unresolved, for instance rare expedites that nevertheless exceed the limit. This wiki files a mixed result under the more severe type, as a question to check rather than a verdict, per [[smell-is-not-a-finding]].

The source also pulls against itself. It reports as normal policy that an expedite "is pulled immediately for work" (L2432), yet one Hedge question asks "are you allowed to finish existing work before the expedite is picked up?" (L2466). This wiki reads the first as a description of what most systems do and the second as the test, so a board that always interrupts started work fails that question even with rare expedites. See [[interrupting-started-work]].

The questions assume a visible expedite class. Because an explicit lane is not the only route to debt (L2480), this wiki applies them to a board with no lane by counting items that jumped ahead of the queue.

## Trade-off

Hedge debt is acceptable and sometimes right: "there are going to be some very good reasons to take on “Hedge” Flow Debt from time to time" (L2478). The classification costs little, but it invites an argument about labels; the source says what matters is the conversation about repayment (L2502).

## Related

[[expedite-lane]], [[artificially-aged-work]], [[priority-inflation]], [[urgent-versus-important]], [[cost-of-delay]]
