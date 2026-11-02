---
title: Size Spread
category: sizing
summary: Keep near-term tasks small and within about one order of magnitude of each other, and let distant work stay large; Vacanti adds that flow needs right-sizing, not same-sizing, and size variance is probably not the main cause of poor predictability, so WIP and Little's Law assumptions are checked before size is blamed.
tags: [rule, estimation, decomposition, cycle-time, decision-rule, sizing, predictability, wip]
sources: [cohn-agile-estimating-planning, vacanti-actionable-agile-metrics, kanban-playbook-right-sizing]
created: 2026-11-01
updated: 2026-11-02
---

# Size Spread

Size spread is how far apart the sizes of near-term tasks lie. [[size-ceiling]] asks how big one task may be. This rule asks how different tasks may be from each other, and how far ahead the smallness is needed. [[estimation-scale]] fixes the values an estimate may take and [[estimating-by-horizon]] decides how finely an item is written. This page holds the reason for keeping near-term sizes alike.

## The rule

Keep work about to start small and similar in size. Let work further out stay large.

> Functionality that will be added in the near future (within the next few iterations) should be decomposed into relatively small user stories, typically items that will take from one or two days up to no more than 10 days. We are best at estimating work that is all within one order of magnitude in size.
>
> — [[cohn-agile-estimating-planning]], L4931

Large items are allowed further down: "Larger user stories can exist further down a project’s prioritized list of work." (L4875). They are broken up as they near the top, when an iteration that takes them is beginning (L4875).

## Why

Three reasons are given, and the first is about flow and not estimation.

> A key influence on cycle time is the variability in the time it takes to develop a new feature. One of the best ways to reduce variability is to work with reasonably small and similarly-sized units of work.
>
> — [[cohn-agile-estimating-planning]], L4875

The second is estimating accuracy, stated as a claim about estimators in L4931 above. The third is fit: such stories are "small enough to be completed during one iteration for most teams" (L4931). Cohn attributes the flow argument to queuing theory through Poppendieck and Reinertsen and presents no measurement in this chapter (L4873).

## Figures and their conditions

"one or two days up to no more than 10 days" is practitioner guidance, hedged with "typically" (L4931). It is in human days and it reflects teams with iterations of a length the book assumes. "one order of magnitude" is a ratio and needs no such unit. "approximately" is attached to it at L4875.

## Further out

Smallness has a cost: "Of course, working with small user stories can become quite an effort on longer projects." (L4931). For a release plan looking "more than two or three months into the future", Cohn would either write larger stories, called epics, or estimate at the theme level, "to avoid decomposing large stories into small ones too far in advance" (L4931). [[how-far-to-split-up-front]] is where this is applied. The figure is tied to the source's assumption of human iterations.

## Sign of violation

- **On the board:** among tasks at the top of the order, the largest estimate is more than about ten times the smallest.
- **On the board:** a large item is about to enter a period unsplit.
- **On the board:** far-off work is already cut as finely as next week's.
- **In history:** time from start to finish varies widely among tasks at the same position in the order.

The signs are this wiki's derivation from L4875 and L4931.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Position in the order | The board |
| Estimates | Tasks, on one scale ([[size-ceiling]]) |
| Horizon of the plan | The release plan or milestone ([[planning-horizons]]) |

The choice was wrong if tasks at similar size still show widely spread cycle times, which points to a cause other than size, or if the fine-grained far-off tasks were later rewritten or dropped, which means they were cut too early.

## Agent executor note

Human days do not transfer ([[size-ceiling]]). The ratio should, as a starting point. This wiki reads the variability mechanism as surviving, since it comes from a queue and not from a person's nature, and an agent's queue often forms at review. The claim that "We are best at estimating" within one order of magnitude (L4931) is about human estimators and is untested for agents in any source here.

## Related

[[starting-more-work]] covers the other main influence on cycle time. [[hidden-wip-in-large-items]] covers what a large item conceals.

## Right-Sizing, Not Same-Sizing

This decision rule separates cutting work so that it is the right size from cutting work so that all items are the same size. [[littles-law]] carries no same-size requirement: "That is because no such requirement exists." ([[vacanti-actionable-agile-metrics]] L1062). Vacanti says most people assume both the law and limiting WIP need equal items, and that this "is simply not true" (L1062-L1068).

### The reasoning

Vacanti gives two reasons, limiting himself to brief points (L1068).

1. **The law works on averages.** It concerns what all items look like on average, not each item individually (L1070). The wine-rack result is the same whether bottles are 20cl or 2 litres (L860).
2. **Size variance is probably not the main problem.** "[T]he variability in work item size is probably not the variability that is killing your predictability" (L1072). He names too much WIP and frequent assumption violations as the bigger problems, and says these are generally easier to fix than arbitrarily equalizing sizes (L1072).

This is a practitioner claim about relative size of effect, stated without data in this chapter. This wiki keeps the mechanism, that averages absorb item variance in the relation, and treats the ranking of causes as something to check on a given board.

### The test

When a board is unpredictable and someone proposes making items uniform:

- **Inputs:** whether the assumptions on [[littles-law]] hold, and whether WIP is stable. Both are read from board history.
- **If they fail:** fix those first. Same-sizing addresses the likely smaller cause.
- **If they hold and predictability is still poor:** size may matter, and then "it would be more about right-sizing your work and not same-sizing your work" (L1072). Vacanti defers the details to his Chapter 12.
- **What would show the choice wrong:** with the assumptions holding, the Cycle Time outliers on the board trace repeatedly to the largest items ([[hidden-wip-in-large-items]]).

### What this does not license

This wiki's reading, not the source's: the section is about flow averages and does not say that size is irrelevant to cutting. A cut made for other reasons is untouched by it, such as splitting a task so that it can be finished without waiting and its result presented once. Those tests come from the plugin's design and have no source, as the charter records. Failing them is not an argument for same-sizing either. They set a boundary for each task, while same-sizing is a target across tasks.

### Signs of the misapplied practice

This wiki's reading: a split whose only stated reason is that the piece is bigger than its neighbours, or a backlog being resized while the open count keeps rising. In both, attention is going to item uniformity while WIP stays unaddressed.

### Positions

**Vacanti:** no size requirement exists, and size is probably not what hurts predictability (L1062-L1072).

**Cohn:** size does matter to flow: "One of the best ways to reduce variability is to work with reasonably small and similarly-sized units of work." ([[cohn-agile-estimating-planning]] L4875). He adds that estimates are better within one order of magnitude and that small stories fit an iteration (the rule at the top of this page).

**Kanban Playbook:** the size question is whether an item will likely finish within the SLE, with no target of uniformity ([[kanban-playbook-right-sizing]]). This is right-sizing with a test attached.

### Which holds under which setup

The two authors disagree about how much size variance matters, and neither measures it. The resolution is this wiki's.

- **A project that estimates:** keep the rule at the top of this page for near-term work, because its reasons from estimating and from fit are untouched by Vacanti's point. Do not cut further only to narrow the spread while a check in the test above is failing.
- **A flow setup with no estimates:** there is no spread to read, so the test is the one on [[size-ceiling]], whether an item likely finishes inside the SLE.
- **Under either:** the order of checks above applies, so assumptions and WIP are read before size is blamed.

### Trade-off

Leaving items unequal keeps individual Cycle Times more spread, so a single item's age says less than it would on a board of uniform items. This wiki notes that Vacanti's claim is about averages, and that it gives no assurance about any one item.

### Agent executor note

This wiki's reading: the arithmetic survives, since averages do not depend on the executor. Cohn's estimating reason concerns human estimators and is untested for agents (the rule at the top of this page), which leaves the flow argument as the live one. Whether an agent's run time varies with task size as a person's does is not shown by either source.
