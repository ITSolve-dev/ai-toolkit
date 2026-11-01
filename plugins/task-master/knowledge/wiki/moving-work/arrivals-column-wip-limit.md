---
title: Setting the Arrivals Column WIP Limit
category: moving-work
summary: Derive the arrivals limit from average throughput divided by replenishments per interval, with a margin for variability; 5 items a week gives a limit of 5 weekly or 1 daily.
tags: [method, wip-limit, replenishment, throughput, arrivals-column, cadence]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Setting the Arrivals Column WIP Limit

This method sets the limit on an [[arrival-point]] column so that the Arrival Rate matches the Departure Rate, the balance [[conservation-of-flow]] requires. The limit is derived from what the process actually finishes, not from what the team would like to start.

## Inputs and where each comes from

| Input | Read from |
|---|---|
| Average Departure Rate per interval | Board history, or the CFD's bottom line; see [[measuring-arrival-and-departure-rates]] |
| Replenishments per interval | The team's replenishment cadence |
| Variability of the process | Spread of throughput across intervals |

## Procedure

1. Calculate average [[throughput]] from history. The source's example, chosen “for argument’s sake”, is weekly deployment and five items per week ([[vacanti-actionable-agile-metrics]] L2130).
2. Start from that number: “Since we are finishing five old items per week, that means we only want to start five new items per week.” (L2130) The limit is five.
3. Add a margin if the process varies. “[D]epending on the variability of our system, we might want to make that WIP Limit a little larger—say six or so—to make sure that our system is never starved for work” (L2136).
4. Divide by replenishments per interval, because five assumes replenishment at the same cadence as deployment. Replenishing daily in a five-day week gives 5 / 5 = 1, a limit of one (L2136).

The figures are illustrative and hold only for that example. The method is the division, and the source gives no formula for the margin.

## The balance it strikes

The limit targets “a proper balance between having enough work to start such that your process is not starved and not having too much work such that work begins but just sits.” (L2158) The reasoning behind this is that queued work is delay, and “delay is the enemy of flow.” (L2158)

## What would show the limit wrong

The source names the two failure directions; these observations for them are this wiki's reading.

- **Too low:** the column is empty when downstream capacity is free, so the process starves.
- **Too high:** items wait on the column past the next replenishment, or the arrival line on a CFD still pulls away from the departure line.

Re-derive the limit when throughput changes materially, since the input is a measured average.

## Failure modes

- **Using the raw throughput with a different cadence.** This wiki's arithmetic from the source's example: a limit of five refilled daily admits up to 25 items a week against five finishing, five times too much.
- **Treating this limit as sufficient.** It is not; see [[constant-wip]]. A downstream column without a limit keeps drawing from this one, and it refills regardless of finishes.

## At small scale

The source's example divides evenly. At the scale of a few people, the quotient may fall below one: three items a week replenished daily gives 0.6. The source does not address this. This wiki rounds up to one, because the column refills only after a pull, and relies on [[constant-wip]] downstream to hold the actual rate.

Vacanti's Chapter 7 deliberately leaves open which items fill the column at replenishment (L2176).
