---
title: Reprioritize Before Each Iteration
category: ordering
summary: Selection starts from a refreshed order and not last period's; feedback from the review can pre-empt items, and unfinished work is a priority decision and not an automatic carry-over.
tags: [rule, ordering, iterations, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Reprioritize Before Each Iteration

The order a project had when it last planned is out of date by the next planning. Cohn says a project could take stories from the top of a ranked list each time, but that conditions change quickly and so "it is always worth a quick reconsideration of priorities" ([[cohn-agile-estimating-planning]] L3104).

## What changes the order

The main input Cohn names is the iteration review, where people seeing the results for the first time "will often have good new ideas that could preempt previously high priority items" (L3110). The second is what is left unfinished. By two days before the end of an iteration, he says:

> By that time, it’s normally clear if there will be unfinished work from the current iteration. This allows the product owner to decide if finishing that work will be a priority for the coming iteration.
>
> — [[cohn-agile-estimating-planning]], L3116

This wiki reads that as the useful part of the passage: unfinished work comes back as a question to be ranked and not as an automatic first item, which agrees with [[unfinished-at-period-end]].

The ranking criteria Cohn recalls are financial value, cost, what the team will learn, and risk reduced (L3112). The criteria for ranking are on [[prioritization-factors]], [[ordering-by-value-and-urgency]] and [[cost-of-delay]].

## Timing and its trade-off

Cohn's ideal is to wait until after the review, since "it’s hard to prioritize next iteration’s work if you are not entirely sure of what will be completed in this iteration" (L3112). In many organizations he reorders earlier so that review and planning fit into one day, then adjusts on the fly afterward (L3112, L3116). The trade-off is an order set before the last feedback is in. Meeting durations and scheduling are left out of this page as facilitation.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| What is likely unfinished | Board state near the end of the period |
| New feedback on presented results | Comments and new items following the presentation |
| The current order | The ordered backlog |

The choice was wrong if selected items were overtaken by feedback that was already available at planning, or if an item ranked up had to be dropped during the period because nothing about it had really changed.

## Sign of violation

These signs are this wiki's.

- **In board history:** the order unchanged across a period in which results were presented and new items arrived.
- **In board state:** tasks unfinished last period sitting first in the new one with no recorded decision.

An unchanged order alone raises a question, since nothing may have changed.

## Agent executor note

This rule depends on when information arrives, so this wiki expects it to hold for an agent executing. Cohn's distinction between a product owner who has seen everything and newcomers at a review assumes a person working alongside the team daily. With a few people steering, those newcomers may not exist, and the feedback then has to come from users or from the results themselves. The plugin can prepare the question but the decision stays with the people steering.

## Related

The wider practice of folding learning into a plan is on [[replanning-on-new-knowledge]]. The stage this happens in is on [[iteration-plan-versus-release-plan]].
