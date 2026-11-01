---
title: Starting More Work When Cycle Time Is Long
category: moving-work
summary: Responding to long Cycle Times by starting more items raises WIP and makes items take longer; lowering WIP is the first thing to consider, though the law alone does not guarantee that result.
tags: [failure-mode, wip, cycle-time, pull, board-rules]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Starting More Work When Cycle Time Is Long

This failure mode is the response to long [[cycle-time]] of starting additional items sooner, which raises [[work-in-progress]] and lengthens the very thing it was meant to shorten. Vacanti calls it "the exact opposite intervention of what they should do: they start more work" ([[vacanti-actionable-agile-metrics]] L906).

## The mechanism

The reasoning Vacanti attributes to such managers: items take so long that new ones must start as soon as possible in order to finish on time, regardless of what is already in progress. Items then take longer still, so the pressure to start sooner grows, and the cycle feeds itself (L906). His general statement is that, on average, the more things worked on at once, the longer each takes to finish (L906). [[wip-lengthens-cycle-time]] gives Cohn's account of the same queue. Two neighbours differ in the trigger or the lever: [[starting-new-work-when-blocked]] is the same move set off by a stopped item, and [[reduce-wip-before-raising-throughput]] is the choice against adding capacity.

## Observable sign

This wiki's reading of where it shows in board history: over consecutive windows, the open-item count and Cycle Time rise together, and new starts continue while existing items are ageing or blocked. As with any sign here, it raises a question ([[smell-is-not-a-finding]]). It is not a verdict.

## The rule

"[I]f Cycle Times are too long then the first thing you should consider is lowering WIP" (L906). Vacanti concedes that this "feels uncomfortable" (L906).

- **Inputs:** average WIP and average Cycle Time across recent windows, and starts against finishes. All are read from board history.
- **What would show it wrong:** WIP fell, and Cycle Time did not improve or Throughput dropped in proportion.

## How firm the rule is

This wiki qualifies the source here. Vacanti calls the link "simple, incontrovertible mathematical fact" (L916), but what the law guarantees is narrower. In his forecasting section he says: "All Little’s Law will say is that an increase in average WIP will result in a change to one or both of average Cycle Time and average Throughput" (L1086). This wiki reads the two passages together as follows: the mathematics fixes the relation, while the direction of the advice is a claim that Throughput will not fall as far as WIP does. That is a strong default for a process limited by concurrency, not a theorem.

He also names a case where it does nothing: changing a WIP limit may leave total average WIP unchanged, for example after "a clear systemic bottleneck" (L1046). See [[wip-limit-is-not-wip]].

## Trade-offs

Lowering WIP means saying no to starting something now, so requests wait longer before entry even as items move faster once started. This wiki notes that lowering WIP moves waiting out of the process; it does not remove demand.

## Agent executor note

This wiki's reading, not the source's: the mechanism depends on where the constraint sits, so it does not transfer automatically. If execution is parallel and cheap, adding concurrent items may raise Throughput for a while, and the failure would appear only once review saturates. Long Cycle Time with results sitting unreviewed would then be the same failure in a new place: more items started in front of the person who has to accept them. This has not been tested against a real board, and the sign above applies either way.
