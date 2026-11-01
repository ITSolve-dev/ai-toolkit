---
title: Buffer Versus Padding
category: sizing
summary: Padding is unexplained time hidden inside an estimate, while a buffer is derived margin shown on its own line and added to estimates with local safety removed, and the test is whether the extra can be traced and seen.
tags: [decision-rule, estimation, buffer, what-an-estimate-promises, failure]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Buffer Versus Padding

Padding and a buffer both add time, and only one of them is sound. Padding is "excess time arbitrarily added to an estimate" ([[cohn-agile-estimating-planning]] L4041): Cohn's case is thinking three days and saying five, just in case. By contrast, "A schedule buffer is a necessary margin of safety added to the sum of estimates from which local safety has been removed" (L4041).

## The test

This wiki puts the source's distinction as three questions; all three must pass for the extra to be a buffer.

| Question | Buffer | Padding |
|---|---|---|
| Where does it sit? | One line on the whole plan | Inside individual estimates |
| Where did the amount come from? | Derived from the spreads, [[project-buffer-sizing]] | A feeling, "just in case" |
| What are the estimates under it? | 50% figures | Already safe, 90% or thereabouts |

The last row is the costly one: "Adding a schedule buffer on top of already pessimistic, 90% estimates will result in an overly long schedule" (L4051). Cohn's caveat allows single-value estimates only if they "represent estimates at the 50% point" (L4051).

## Why padding appears

"Individuals add padding to an estimate if they expect to be beaten up if they are wrong" (L4041). This mechanism belongs to a human estimator. This wiki reads the transfer as follows: an agent has no fear of blame, but an agent or a person steering can still produce pessimistic numbers, by reasoning towards a safe answer or by being trained on what got punished. So the test applies to estimates from either, though the motive may not.

## Presenting a buffer

A buffer looks like padding to anyone who sees only the number: "a buffer (especially a schedule buffer) can appear to be padding" (L4055). The instruction is not to hide it: "You should not hide their existence or how they are used" (L4055). What must be shown is how the estimates and buffer were derived and that the result is a schedule everyone can hold "90–95%" confidence in (L4055).

Nor is a buffer idle time that can be reclaimed. Cohn's car-following analogy says "you fully expect to use up most of that buffer if forced to brake suddenly" (L4043). This wiki reads that as the reply to any proposal to trim a buffer because it looks unused at the start of a plan.

## Signs

These signs are this wiki's. Each raises a question to check.

- A plan with no buffer line but estimates that nobody will say are 50% figures, so the safety is hidden in them.
- A buffer line with no derivation from item spreads and no stated rule.
- In history, where estimates are in time or convert to it, nearly all items finishing at or under their estimate. This suggests they were not 50% figures; see [[completion-time-distribution]].

The opposite failure is cutting real [[local-safety]] from the estimates without adding any buffer back: that is the 1:10 airport plan, where "the slightest delay will cause me to miss my flight" (L3935).

## Trade-off

A visible buffer invites someone to negotiate it away, and hidden padding does not. Cohn accepts this cost by requiring disclosure. This wiki reads his reason as being that a padded plan cannot be read: nobody can tell how much protection it holds or where.
