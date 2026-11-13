---
title: Constant WIP Throughout the Process
category: moving-work
summary: A limit on the arrivals column alone does not balance flow; WIP must stay constant on average across the whole process, by per-step limits, one global limit, or a mix. The arrivals limit itself is average throughput divided by replenishments per interval, with a margin for variability: 5 items a week gives a limit of 5 weekly or 1 daily, rounded up to one below one.
tags: [rule, failure-mode, wip-limit, pull-system, kanban, flow, method, replenishment, throughput, arrivals-column, cadence]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Constant WIP Throughout the Process

The rule is that a process must hold a constant amount of work in progress, on average, from its arrival point to its departure point ([[started-and-finished-points]]). “You must make sure that a constant amount of WIP (on average) is maintained throughout the whole process.” ([[vacanti-actionable-agile-metrics]] L2156) The source calls this operating “a constant WIP style of pull system” (L2150), and it is the means by which [[conservation-of-flow]] actually holds. [[wip-control]] states the bound, and this page says why it has to reach the whole process.

## Why a limit at the front is not enough

“Setting a WIP limit on the arrivals column is a necessary—but not sufficient—means to balancing arrivals and departures.” (L2150)

The failure runs as follows (L2150-L2156). The arrivals column is limited and Test is not. Work is drawn into Test because nothing stops it, which the source calls “pulled (pushed, really)”. That draws work from the arrivals column, which looks like free capacity, so “the arrivals column will be replenished even though no work has been completed.” Items now arrive faster than they depart, and the arrivals limit has done nothing.

This wiki reads the mechanism as a leak: a limit controls the rate only if every step between it and the exit also blocks. The signal it sends is a pull, and a pull caused by anything other than a finish carries false information about capacity.

## How to hold it

“Constant WIP could be maintained either by expressly limiting Work In Progress at each step of your work flow or by setting one global limit for the whole process (or some mixture of both).” (L2168) The source does not rank these: “it does not really matter how you limit WIP throughout the whole system just as long as you do.” (L2168)

Having a limit is not the same as holding one ([[work-in-progress]]). The source stresses “any time you honor the WIP limit(s) you have set” over the act of setting them (L2150).

## Setting the arrivals column limit

This applies only where an arrivals column exists. Whether one is needed is on [[started-and-finished-points]]: the column "may be superfluous" when items can be pulled ad hoc with no coordination with an outside stakeholder (L2162-L2170), which is often the case for a few people steering an agent.

The limit on the arrivals column ([[started-and-finished-points]]) is set so that the Arrival Rate matches the Departure Rate, the balance [[conservation-of-flow]] requires. It is derived from what the process actually finishes, not from what the team would like to start.

### Inputs and where each comes from

| Input | Read from |
|---|---|
| Average Departure Rate per interval | Board history, or the CFD's bottom line; see [[throughput]] |
| Replenishments per interval | The team's replenishment cadence |
| Variability of the process | Spread of throughput across intervals |

### Procedure

1. Calculate average [[throughput]] from history. The source's example, chosen “for argument’s sake”, is weekly deployment and five items per week ([[vacanti-actionable-agile-metrics]] L2130).
2. Start from that number: “Since we are finishing five old items per week, that means we only want to start five new items per week.” (L2130) The limit is five.
3. Divide by replenishments per interval, because five assumes replenishment at the same cadence as deployment. The source divides "the original Arrival Rate number": replenishing daily in a five-day week gives 5 / 5 = 1, a limit of one (L2136).
4. Add a margin if the process varies. “[D]epending on the variability of our system, we might want to make that WIP Limit a little larger—say six or so—to make sure that our system is never starved for work” (L2136). The source states the margin on the weekly limit and divides the unmargined five; this wiki therefore adds it after dividing.

The figures are illustrative and hold only for that example. The method is the division, and the source gives no formula for the margin.

### The balance it strikes

The limit targets “a proper balance between having enough work to start such that your process is not starved and not having too much work such that work begins but just sits.” (L2158) The reasoning behind this is that queued work is delay, and “delay is the enemy of flow.” (L2158)

### What would show the limit wrong

The source names the two failure directions; these observations for them are this wiki's reading.

- **Too low:** the column is empty when downstream capacity is free, so the process starves.
- **Too high:** items wait on the column past the next replenishment, or the arrival line on a CFD still pulls away from the departure line.

Re-derive the limit when throughput changes materially, since the input is a measured average.

### Failure modes of the limit

- **Using the raw throughput with a different cadence.** This wiki's arithmetic from the source's example: a limit of five refilled daily admits up to 25 items a week against five finishing, five times too much.
- **Treating this limit as sufficient.** It is not, as the first section of this page says. A downstream column without a limit keeps drawing from this one, and it refills regardless of finishes.

### At small scale

The source's example divides evenly. At the scale of a few people, the quotient may fall below one: three items a week replenished daily gives 0.6. The source does not address this. This wiki rounds up to one, because the column refills only after a pull, and relies on constant WIP downstream to hold the actual rate.

Vacanti's Chapter 7 deliberately leaves open which items fill the column at replenishment (L2176).

## Signs

These are this wiki's application of the source's scenario; each raises a question to check.

- Some column between the first and the exit has no limit, and no global limit covers the board.
- The first column is refilled in a period when nothing crossed the departure point.
- A count of items in progress exceeds a stated limit in board history.
- Total WIP trends upward on a CFD despite a limit at the front; see [[reading-a-cfd]].

## Trade-offs

The cost of the rule is that a person or agent may be blocked from starting anything while a step downstream is full. The source accepts this implicitly, and warns the opposite way: “the further you stray away from this principle, the less predictable you will be.” (L2156)

The source's claim that honored limits always yield a balanced picture (L2150) concerns the balance only; it does not say the process is healthy, as [[cumulative-flow-diagram]] notes.

## Survival under an agent executor

The mechanism is a counting argument, so this wiki keeps it for an agent executor. The transfer here is ours: a board where an agent starts many items in parallel still needs the limit, because the items that pile up do so at the step the steering person must act on, not at the step the agent works on.
