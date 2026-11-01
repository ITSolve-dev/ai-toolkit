---
title: Approximate Versus Actual Average Cycle Time
category: reading-history
summary: Compare the average Cycle Time read off a CFD with the exact average from the same data; greater means accumulating flow debt, less means repaying it, roughly equal means neither.
tags: [method, flow-metrics, cycle-time, cumulative-flow-diagram, predictability]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Approximate Versus Actual Average Cycle Time

This method tests a board's history for [[flow-debt]] by comparing two averages over the same items and interval. One is the [[approximate-average-cycle-time]] read from a [[cumulative-flow-diagram]]. The other is the exact Average Cycle Time computed from the data behind that chart. Their difference is the point of the exercise, which is why the approximation is worth having when the exact figure is available.

## Inputs and where they come from

- **Approximate Average Cycle Time:** the horizontal distance between two lines on the CFD, per CFD Property #4, which "represents the Approximate Average Cycle Time for items that finished between the two workflow steps represented by the chosen two lines" ([[vacanti-actionable-agile-metrics]] L2380).
- **Exact Average Cycle Time:** computed "from the very data used to build the CFD to begin with" (L2396). Both are read from board history, with no logged hours involved.
- **The interval:** the reading holds only "for the time interval under consideration" (L2506).

## Why the comparison means anything

The source ties it to [[littles-law]] Assumption #4:

> Little’s Law Assumption #4: For the time period under consideration, the average age of WIP should neither be increasing nor decreasing.
>
> — [[vacanti-actionable-agile-metrics]], L2394

The source says the comparison shows "if we can expect our exact Average Cycle Time to grow, decline, or stay the same over time", and that growth or decline means "a violation of Little’s Law assumption #4 which means that our predictability is in jeopardy" (L2396).

## The three readings

| Comparison | Reading | What it means for predictability |
|---|---|---|
| Approximate greater than exact | Accumulating flow debt (L2414, L2572) | Some items were favoured; others are ageing and not yet counted |
| Approximate less than exact | Paying off flow debt (L2506, L2574) | Items that "languished in progress are now finally completing" and inflate the average (L2508) |
| Roughly equal | Neither accumulating nor repaying (L2522, L2576) | "You are not overloaded with expedite requests, you are not allowing items to stay blocked indefinitely, and you are not allowing items to queue arbitrarily." (L2522) |

The source treats the first two as both risky, since accumulating and repaying each damage predictability (L2406, L2510-L2516). The mnemonic it offers is “scenario three is where you want to be.” (L2406)

## Conditions on the reading

- **The system must be otherwise stable.** "these conclusions can only be drawn assuming we are running an otherwise stable system (i.e., nothing about the underlying system design has changed materially)" (L2518). The sign to check first is a change to the board's columns, limits or policies inside the interval.
- **Equality does not certify health.** The source warns "That is not to suggest that there are not any other areas of your process that are unhealthy" (L2524), so a match clears flow debt and nothing else.

## How different is different

The source gives a rough guide and refuses a threshold. Some gap is expected because one figure is an approximation. "If the difference is about 10%, then you might not get too excited. However, if the difference is 50%, then that might be a pretty good clue to take action." (L2536) The answer is otherwise "highly context specific" (L2534), learned over time. These two percentages are a practitioner's rule of thumb from no stated dataset, and the source gives no minimum number of finished items.

This wiki adds a caution for a board worked by a few people, which the source does not address: with few finished items, one item can move an average a long way. Before reading a large gap as debt, look at which items produce it.

## What later fact would show the reading wrong

This wiki derives the check from the two forms of repayment (L2444-L2452). A reading of "accumulating" predicts that the passed-over items will either finish with unusually long Cycle Times, raising the exact average, or be discarded. If neither happens over following intervals, the gap was approximation error or a change in the system.

## Related

[[flow-debt]], [[hedge-speculative-ponzi]], [[artificially-aged-work]], [[reading-flow-metrics-off-a-cfd]], [[littles-law-assumptions]], [[smell-is-not-a-finding]], [[service-level-expectation]], [[flow-metrics]]
