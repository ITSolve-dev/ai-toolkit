---
title: Prioritization Factors
category: ordering
summary: Cohn's four things to weigh when ordering work are financial value, cost, new knowledge and risk removed; the last two are what a sort by value and cost leaves out, and urgency is not on the list.
tags: [concept, ordering, prioritization, risk, learning]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Prioritization Factors

Cohn ([[cohn-agile-estimating-planning]]) replaces the instruction to prioritize on business value with four factors. He calls that instruction "the vague and mostly useless advice of “prioritize on business value.”" (L1710), because it does not say what business value is.

## The four factors

| Factor | Cohn's wording | Question it asks | Read from |
|---|---|---|---|
| Value | "The financial value of having the features" (L1712) | What would be made or saved? If that cannot be priced, how much do users want it? | The person steering. It is a task-only fact ([[recoverable-versus-task-only-facts]]) |
| Cost | "The cost of developing (and perhaps supporting) the new features" (L1714) | What does it take, now and later? | The size estimate, [[cost-per-story-point]], [[cost-now-versus-cost-later]] |
| New knowledge | "The amount and significance of learning and new knowledge created by developing the features" (L1716) | What will we know afterwards that we do not know now? | [[end-and-means-uncertainty]] |
| Risk | "The amount of risk removed by developing the features" (L1718) | What could still derail this, and does doing this settle it? | [[risk-value-quadrants]] |

This wiki notes a detail of the wording. The last two factors measure what doing the work removes, not how alarming the work looks. A risky feature that settles nothing else, and that could simply be dropped, scores low on this definition.

## Why four and not two

> Because most projects are undertaken to either save or make money, the first two factors often dominate prioritization discussions. However, proper consideration of the influence of learning and risk on the project is critical if we are to prioritize optimally.
>
> — [[cohn-agile-estimating-planning]], L1720

This wiki reads that as naming the failure directly: an order built from value and cost alone looks complete and has two inputs missing ([[ordering-by-one-factor]]). The two-sided form of the argument is on [[tradeoff-needs-cost-and-benefit]].

## Value when it cannot be priced

A financial estimate usually covers a period of "the next few months, quarters, or possibly years" (L1726). It needs a new number of sales, the average sale including follow-on sales and maintenance agreements, and the timing of sales increases (L1734). Where such figures exist, the forecast is on [[sources-of-return]] and the comparison on [[financial-measures-for-themes]]. Because that is hard, Cohn allows a substitute: "it is possible to use non-financial measures of desirability to represent value." (L1734). [[ordering-by-value-and-urgency]] is this wiki's existing substitute for a project with no revenue to point at.

## Relation to cost of delay

Cohn's list has no urgency factor. In this chapter, timing appears only as an input to a value estimate (L1734), whereas [[cost-of-delay]] treats how fast value drains as an ingredient of its own. This wiki resolves the difference by setting, and the resolution is ours:

- If waiting changes little, because the work ships in one release and its value does not leak before then, value over cost gives the base order.
- If waiting drains value, [[ordering-by-value-and-urgency]] and [[cost-of-delay-over-duration]] give the base order.
- In both settings, knowledge and risk then move items, because the cost-of-delay pages have no slot for them. The procedure is [[combining-prioritization-factors]].

## Agent executor note

This wiki reads value and cost as concerning the result and its price, so they survive. The two factors that need a closer look are knowledge and risk, because part of what Cohn counts depends on who the people are. See [[end-and-means-uncertainty]].
