---
title: Over-Disaggregation
category: sizing
summary: Splitting an item in order to estimate it helps until it can be compared, but past that point pieces go missing with no check that would show it and summed ranges grow too wide to use.
tags: [failure-mode, estimation, disaggregation, decomposition]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Over-Disaggregation

Over-disaggregation is splitting an item too finely in order to estimate it. Disaggregation is the right response to an item too big to compare, but Cohn warns: "However, you need to be careful not to go too far with this approach." ([[cohn-agile-estimating-planning]] L1296). This is about splitting to produce an estimate, which is a different act from cutting work for delivery on [[story-splitting-patterns]].

## What breaks

**Pieces go missing, and nothing shows it.** Cohn's example is estimating a golf score hole by hole, where it is easy to forget a hole while recreating the course. For golf the count of 18 is a check. "But, when disaggregating a story there is no such safety check." (L1298).

**Summed ranges blow up.** "Not only does the likelihood of forgetting a task increase if we disaggregate too far, summing estimates of lots of small tasks leads to problems." (L1300). For 18 holes each estimated at 3–8, the sum is 54–144. Of that range he says: "There’s no chance that I’ll do that well or that poorly." (L1300). Asked for the whole round, he would say 80–120, a much narrower and more useful answer (L1300).

This wiki reads the second point as arithmetic: the summed range assumes every piece lands at the same end at once, which the source does not spell out. That is why the whole-item estimate beats the sum.

## Figures and their conditions

The golf numbers are an invented illustration and nothing was measured. This wiki keeps the mechanism. Neither 18 pieces nor any other count is a threshold.

## Signs

- A task's estimate is the sum of many very small pieces, each with its own range.
- Work appears after starting that belongs to no listed piece. This is the forgotten piece showing up late, and [[overrun-triggers-a-recut]] handles what follows.
- The sum of the pieces is far from what anyone would say for the whole.

The source gives the failure and not these signs, so they are this wiki's. Each raises a question, per [[smell-is-not-a-finding]].

## Where to stop

Cohn gives no stopping point. This wiki's reading, from his reason for disaggregating at all (L1294): stop once the pieces can be compared with tasks already estimated, which is [[triangulation]]. Disaggregation then exists to restore comparison, and a further split adds no comparison.

This wiki notes the cost of stopping there: the estimate rests on a coarser look, and a piece that hides a surprise stays hidden. That is the trade-off in [[estimating-effort-by-purpose]].

## Agent executor note

This wiki reads the summing problem as arithmetic, so it holds for any estimator. The forgetting problem was stated for a person recreating a course from memory. An agent listing pieces does not forget in that way, but this wiki expects the absence of a check to carry over: nothing in a list shows what the list omits, which is the same concern as [[agent-silence-is-not-completeness]]. That extension is ours, and no source tests it. An agent can also produce a long fine breakdown cheaply, so the failure is easier to reach. A breakdown should not be accepted as a better estimate merely for being detailed.
