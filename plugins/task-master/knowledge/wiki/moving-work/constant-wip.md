---
title: Constant WIP Throughout the Process
category: moving-work
summary: A limit on the arrivals column alone does not balance flow; WIP must stay constant on average across the whole process, by per-step limits, one global limit, or a mix.
tags: [rule, failure-mode, wip-limit, pull-system, kanban, flow]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Constant WIP Throughout the Process

The rule is that a process must hold a constant amount of work in progress, on average, from its [[arrival-point]] to its [[departure-point]]. “You must make sure that a constant amount of WIP (on average) is maintained throughout the whole process.” ([[vacanti-actionable-agile-metrics]] L2156) The source calls this operating “a constant WIP style of pull system” (L2150), and it is the means by which [[conservation-of-flow]] actually holds. [[wip-control]] states the bound, and this page says why it has to reach the whole process.

## Why a limit at the front is not enough

“Setting a WIP limit on the arrivals column is a necessary—but not sufficient—means to balancing arrivals and departures.” (L2150)

The failure runs as follows (L2150-L2156). The arrivals column is limited and Test is not. Work is drawn into Test because nothing stops it, which the source calls “pulled (pushed, really)”. That draws work from the arrivals column, which looks like free capacity, so “the arrivals column will be replenished even though no work has been completed.” Items now arrive faster than they depart, and the arrivals limit has done nothing.

This wiki reads the mechanism as a leak: a limit controls the rate only if every step between it and the exit also blocks. The signal it sends is a pull, and a pull caused by anything other than a finish carries false information about capacity.

## How to hold it

“Constant WIP could be maintained either by expressly limiting Work In Progress at each step of your work flow or by setting one global limit for the whole process (or some mixture of both).” (L2168) The source does not rank these: “it does not really matter how you limit WIP throughout the whole system just as long as you do.” (L2168)

Having a limit is not the same as holding one ([[wip-limit-is-not-wip]]). The source stresses “any time you honor the WIP limit(s) you have set” over the act of setting them (L2150).

## Signs

These are this wiki's application of the source's scenario; each raises a question to check.

- Some column between the first and the exit has no limit, and no global limit covers the board.
- The first column is refilled in a period when nothing crossed the departure point.
- A count of items in progress exceeds a stated limit in board history.
- Total WIP trends upward on a CFD despite a limit at the front; see [[reading-flow-balance-on-a-cfd]].

## Trade-offs

The cost of the rule is that a person or agent may be blocked from starting anything while a step downstream is full. The source accepts this implicitly, and warns the opposite way: “the further you stray away from this principle, the less predictable you will be.” (L2156)

The source's claim that honored limits always yield a balanced picture (L2150) concerns the balance only; it does not say the process is healthy, as [[reading-flow-balance-on-a-cfd]] notes.

## Survival under an agent executor

The mechanism is a counting argument, so this wiki keeps it for an agent executor. The transfer here is ours: a board where an agent starts many items in parallel still needs the limit, because the items that pile up do so at the step the steering person must act on, not at the step the agent works on.
