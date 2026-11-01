---
title: Right-Sizing, Not Same-Sizing
category: cutting-work
summary: Neither Little's Law nor limiting WIP requires equal-sized items, so cutting work merely to equalize size is the wrong fix while excess WIP and assumption violations remain; where a project estimates, the case for similar sizes on other grounds stands.
tags: [decision-rule, sizing, decomposition, predictability, wip]
sources: [vacanti-actionable-agile-metrics, cohn-agile-estimating-planning, kanban-playbook-right-sizing]
created: 2026-11-02
updated: 2026-11-02
---

# Right-Sizing, Not Same-Sizing

This decision rule separates cutting work so that it is the right size from cutting work so that all items are the same size. [[littles-law]] carries no same-size requirement: "That is because no such requirement exists." ([[vacanti-actionable-agile-metrics]] L1062). Vacanti says most people assume both the law and limiting WIP need equal items, and that this "is simply not true" (L1062-L1068).

## The reasoning

Vacanti gives two reasons, limiting himself to brief points (L1068).

1. **The law works on averages.** It concerns what all items look like on average, not each item individually (L1070). The wine-rack result is the same whether bottles are 20cl or 2 litres (L860).
2. **Size variance is probably not the main problem.** "[T]he variability in work item size is probably not the variability that is killing your predictability" (L1072). He names too much WIP and frequent assumption violations as the bigger problems, and says these are generally easier to fix than arbitrarily equalizing sizes (L1072).

This is a practitioner claim about relative size of effect, stated without data in this chapter. This wiki keeps the mechanism, that averages absorb item variance in the relation, and treats the ranking of causes as something to check on a given board.

## The test

When a board is unpredictable and someone proposes making items uniform:

- **Inputs:** whether the assumptions on [[littles-law-assumptions]] hold, and whether WIP is stable. Both are read from board history.
- **If they fail:** fix those first. Same-sizing addresses the likely smaller cause.
- **If they hold and predictability is still poor:** size may matter, and then "it would be more about right-sizing your work and not same-sizing your work" (L1072). Vacanti defers the details to his Chapter 12.
- **What would show the choice wrong:** with the assumptions holding, the Cycle Time outliers on the board trace repeatedly to the largest items ([[hidden-wip-in-large-items]]).

## What this does not license

This wiki's reading, not the source's: the section is about flow averages and does not say that size is irrelevant to cutting. A cut made for other reasons is untouched by it, such as splitting a task so that it can be finished without waiting and its result presented once. Those tests come from the plugin's design and have no source, as the charter records. Failing them is not an argument for same-sizing either. They set a boundary for each task, while same-sizing is a target across tasks.

## Signs of the misapplied practice

This wiki's reading: a split whose only stated reason is that the piece is bigger than its neighbours, or a backlog being resized while the open count keeps rising. In both, attention is going to item uniformity while WIP stays unaddressed.

## Positions

**Vacanti:** no size requirement exists, and size is probably not what hurts predictability (L1062-L1072).

**Cohn:** size does matter to flow: "One of the best ways to reduce variability is to work with reasonably small and similarly-sized units of work." ([[cohn-agile-estimating-planning]] L4875). He adds that estimates are better within one order of magnitude and that small stories fit an iteration ([[size-spread]]).

**Kanban Playbook:** the size question is whether an item will likely finish within the SLE, with no target of uniformity ([[kanban-playbook-right-sizing]]). This is right-sizing with a test attached.

## Which holds under which setup

The two authors disagree about how much size variance matters, and neither measures it. The resolution is this wiki's.

- **A project that estimates:** keep [[size-spread]] for near-term work, because its reasons from estimating and from fit are untouched by Vacanti's point. Do not cut further only to narrow the spread while a check in the test above is failing.
- **A flow setup with no estimates:** there is no spread to read, so the test is the one on [[size-ceiling]], whether an item likely finishes inside the SLE.
- **Under either:** the order of checks above applies, so assumptions and WIP are read before size is blamed.

## Trade-off

Leaving items unequal keeps individual Cycle Times more spread, so a single item's age says less than it would on a board of uniform items. This wiki notes that Vacanti's claim is about averages, and that it gives no assurance about any one item.

## Agent executor note

This wiki's reading: the arithmetic survives, since averages do not depend on the executor. Cohn's estimating reason concerns human estimators and is untested for agents ([[size-spread]]), which leaves the flow argument as the live one. Whether an agent's run time varies with task size as a person's does is not shown by either source.
