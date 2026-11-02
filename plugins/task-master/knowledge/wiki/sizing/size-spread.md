---
title: Size Spread
category: sizing
summary: Tasks near the top of the order are kept small and within about one order of magnitude of each other, because similar sizes reduce variability in cycle time and estimate better; work further out stays large until it nears the top.
tags: [rule, estimation, decomposition, cycle-time]
sources: [cohn-agile-estimating-planning]
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
