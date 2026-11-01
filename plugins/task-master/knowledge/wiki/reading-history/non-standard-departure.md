---
title: Non-Standard Departure
category: reading-history
summary: How to record an item that leaves a step other than by finishing it; tag a departure into Done when the work is over, erase the entry date when the arrival was a mistake or the item will return, and never decrement a count.
tags: [decision-rule, reading-history, moving-work, board-history, cfd, flow-metrics]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Non-Standard Departure

A non-standard departure is an item that leaves a step for any reason other than completing it: de-prioritized, de-scoped, too broken to test, no longer needed. Vacanti's shop example is the customer who walks in and turns straight round ([[vacanti-actionable-agile-metrics]] L1346). Decrementing a count is not an option (L1370, see [[cfd-built-from-entry-dates]]), so the choice is between two entries in the data:

- **Tag the departure.** "[E]nter a departure timestamp and then “tag” that departure with a special reason", which allows filtering "that “bad” data if we choose to do so" (L1386). "This particular approach is potentially best for customers who leave a queue and we do not expect them to return." (L1386).
- **Erase the arrival.** "This strategy would be an acknowledgement that it was a mistake to ever have counted the arrival in the first place." (L1398). It "might be a better solution for items that we expect to return to the queue at a later date" (L1398).

Both are valid when building a CFD (L1400).

## The cases the source gives

| Case | Handling | Source |
|---|---|---|
| Arrives at the first step, then taken off the board (de-prioritized, de-scoped) | Remove the entry date, proceed as if it never arrived | L1408 |
| In Test, "so broken that it cannot even be tested" | Move back to the appropriate prior step, erase the Test date | L1416 |
| In Test, "no longer needed" | Move directly to Done with a departure date, flag it | L1416 |
| In Test, ordinary defect found | Stays in Test; not grounds for moving back | L1416 |
| Any item leaving the process unfinished, when counting | Count it in Done, tag it | L1442-L1448 |

The last row is broader than the first. Vacanti recommends counting exits in Done "regardless of how you collect your data" (L1442), while the first row erases an item that also left. The source does not reconcile them.

## The test

This wiki reconciles them with two questions, in order. The resolution is ours.

| Input | Read from |
|---|---|
| Will the item come back through this step? | The state it went to; the board's open items |
| Was the arrival a mistake, with nothing done in the step? | Time in state; the reason given on the task |

1. It will come back: erase the entry date for this step.
2. It will not come back and the arrival was a mistake: erase, as if it never arrived.
3. Otherwise, work was done and is over: departure into Done, tagged with a reason.

When unsure, tag. A tag can be filtered out later, and an erased date cannot be recovered from the chart's data.

**What would show the choice wrong:** an item treated as never arrived reappears on the board, or someone asks what became of work that the chart no longer shows.

## Erase in the derived data, not in history

The source speaks of erasing a timestamp. This wiki reads that as a step in deriving chart data: the board's history stays as it happened, and the derivation decides which entries count. History is what a later audit reads, and rewriting it would destroy the evidence that the item was on the board at all.

## Trade-offs

- **A tag counts unless it is filtered.** The source offers filtering as an option (L1386). This wiki notes the consequence: a tagged exit left in the data adds to Throughput and enters Cycle Time as a very short item, so reports should state whether tagged exits are included. See [[flow-metrics]].
- **Erasing loses time.** An item erased from Test, sent back and later returned has one Test date, the later one, so its first stay blends into the earlier step. This wiki reads that as acceptable for the rare broken item and misleading if it is routine.

## Signs

- In board history, a task closes as not needed, not done, or similar, with no reason recorded.
- In board history, a task reaches a later step and moves to an earlier one with no reason recorded.
- On a chart, a line falls ([[malformed-cfd]]).

Frequent returns of items too broken to test are a question about what entry to that step requires, not about the chart. This wiki reads the case that way: the arrival was a mistake because the step's entry condition was not met. See [[smell-is-not-a-finding]].

## Positions

**Vacanti:** one backward move is allowed, for an item that cannot be tested at all. For ordinary defects he agrees with the forward-only rule: finding them does "not normally constitute an egregious enough offense to cause the item to be moved back to the development column" (L1416). He gives no reason for that.

**Wester:** forward only, see [[backward-movement]]. This wiki reads the two as compatible: Wester's case is an expected cycle, and Vacanti's exception is an arrival that should not have happened. Closing an item at intake is covered by [[closing-what-no-longer-applies]].

## Agent executor note

The bookkeeping does not depend on who executes. This wiki reads a result a person rejects as the ordinary-defect row, which is routine with an agent. A task that came back because the agent could not begin it is closer to the broken-item row, and this wiki has no source for treating it so.
