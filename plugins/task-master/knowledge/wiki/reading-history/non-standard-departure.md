---
title: Non-Standard Departure
category: reading-history
summary: How to record an item that leaves a step other than by finishing it; tag a departure into Done when the work is over, erase the entry date when the arrival was a mistake or the item will return, and never decrement a count. Started work that is dropped is the common case: move it to the finished state with a date and an abandoned tag, never delete it, so analytics can include or filter it and the CFD stays valid.
tags: [decision-rule, reading-history, moving-work, board-history, cfd, flow-metrics, method, abandoned-work, metrics, data-hygiene, cumulative-flow-diagram, segmentation, vacanti]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Non-Standard Departure

A non-standard departure is an item that leaves a step for any reason other than completing it: de-prioritized, de-scoped, too broken to test, no longer needed. Vacanti's shop example is the customer who walks in and turns straight round ([[vacanti-actionable-agile-metrics]] L1346). Decrementing a count is not an option (L1370, see [[cumulative-flow-diagram]]), so the choice is between two entries in the data:

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

When unsure, tag. A tag can be filtered out later, and an erased date cannot be recovered from the chart's data. Under which setups a task may go back at all is the lookup on [[board-rules-by-setup]].

**What would show the choice wrong:** an item treated as never arrived reappears on the board, or someone asks what became of work that the chart no longer shows.

## Erase in the derived data, not in history

The source speaks of erasing a timestamp. This wiki reads that as a step in deriving chart data: the board's history stays as it happened, and the derivation decides which entries count. History is what a later audit reads, and rewriting it would destroy the evidence that the item was on the board at all.

**Which derivation feeds age and Cycle Time.** The erasure applies to the per-step dates that draw the chart's lines, so that no line falls. It does not apply to an item's age or [[cycle-time]]. Those are read from the item's first entry at the started point in board history, so an item that left and came back keeps its whole span, including the time it was away, as [[unfinished-at-period-end]] requires for a returned task. The one exception is the second case of the test: an arrival that was a mistake, with nothing done and no return, is removed from age and Cycle Time as well, because the item was never really started. This resolution is this wiki's; the source discusses only the chart. Its cost: a returned item's Cycle Time is long by the time it was away, so a report states how many returned items it includes, and may give their time away separately.

## Trade-offs

- **A tag counts unless it is filtered.** The source offers filtering as an option (L1386). This wiki notes the consequence: a tagged exit left in the data adds to Throughput and enters Cycle Time as a very short item, so reports should state whether tagged exits are included. See [[flow-metrics]].
- **Erasing loses time.** An item erased from Test, sent back and later returned has one Test date, the later one, so its first stay blends into the earlier step. This wiki reads that as acceptable for the rare broken item and misleading if it is routine.

## Signs

- In board history, a task closes as not needed, not done, or similar, with no reason recorded.
- In board history, a task reaches a later step and moves to an earlier one with no reason recorded.
- On a chart, a line falls ([[cumulative-flow-diagram]]).

Frequent returns of items too broken to test are a question about what entry to that step requires, not about the chart. This wiki reads the case that way: the arrival was a mistake because the step's entry condition was not met. See [[smell-is-not-a-finding]].

## Abandoned work: the case of dropping started work

Accounting for abandoned work is the procedure for keeping dropped items in a board's data, so that a legitimate decision to stop does not corrupt later analysis. Vacanti's phrasing of why it matters: "it is absolutely necessary to account for them properly in your data" ([[vacanti-actionable-agile-metrics]] L2300). The wider choice between tagging a departure and erasing an arrival is set out above; this section is the case of work that was started and will not come back.

### The procedure

> Instead of just removing (or deleting) an item from your board never to be tracked again, it is probably best to mark that item as “finished” (whatever that means in your context), mark the date it was done, and then tag it with some attribute like “abandoned” or “discarded”.
>
> — [[vacanti-actionable-agile-metrics]], L2300

This wiki sets that out as five steps, taking the first and last from the surrounding text.

1. Decide the item stops, for a reason that stands on its own: see the exception in [[conservation-of-flow]].
2. Move it straight to the board's final state, from wherever it is. In Vacanti's example an item in Development goes immediately to Deployed (L2302).
3. Capture the current date.
4. Tag it with an abandoned or discarded attribute; the name is free (L2302).
5. Ask "Why did that happen?" and whether something "further upstream" could have avoided it (L2292-L2298).

The tag is one more way of segmenting work by type: whether it completed normally or not (L2300).

### What it buys

Vacanti's benefit is choice at analysis time: a [[cumulative-flow-diagram]] of all items, of only those finished normally, or of only the abandoned (L2304). And:

> not only have we not violated the principle of the CoF, but we can also guarantee that we will be able to generate a valid CFD for all of those views.
>
> — [[vacanti-actionable-agile-metrics]], L2304

This wiki reads the mechanism as: a deleted item either disappears from counts it was already part of, or lingers as forever-open work, and either way the record of what entered no longer matches what left.

### A tension in the source

Vacanti says both that correct accounting has "not violated" CoF (L2304) and that every abandoned start violated it and impaired predictability (L2334). This wiki reads these as two senses. The process sense is violated whenever work is dropped, which is why the upstream question exists. The data sense is preserved by accounting, which is why the charts stay valid. Treat the first as a thing to learn from, and the second as a thing to do every time.

### Signs of abandoned work handled badly

These are this wiki's transfer and raise a question rather than a verdict:

- History shows an item in a started state that no longer exists on the board: it was deleted.
- Started count exceeds finished plus open count over a period: something left without being recorded.
- Nothing is ever tagged abandoned on a board with a long history. Either nothing was abandoned, or it left some other way.
- A rising share of abandoned items: look upstream at when commitment happens ([[backlog-versus-commitment]]).

### Trade-offs and failure modes

The source does not name the cost. This wiki reads it as this: the final state now holds work that was never delivered. Any [[throughput]] or [[cycle-time]] reading that does not filter on the tag counts abandoned items as finished, and their short or long lives distort both. A count of finished work must therefore say whether it includes them. A board whose final state means something public, such as deployed, also reads falsely to anyone not filtering, which is why Vacanti's "whatever that means in your context" (L2300) is worth deciding deliberately.

The chapter closes on the same point: "just remember to account for that action appropriately in your data" (L2342).

### Agent note on abandoned work

Board history is kept mechanically, so this survives an agent executing and may be easier to enforce: dropping a task is an event a tool can record, rather than a habit someone has to remember. Keeping logged hours is not required for any of it.

## Positions

**Vacanti:** one backward move is allowed, for an item that cannot be tested at all. For ordinary defects he agrees with the forward-only rule: finding them does "not normally constitute an egregious enough offense to cause the item to be moved back to the development column" (L1416). He gives no reason for that.

**Wester:** forward only, see [[backward-movement]]. This wiki reads the two as compatible: Wester's case is an expected cycle, and Vacanti's exception is an arrival that should not have happened. Closing an item at intake is covered by [[closing-what-no-longer-applies]].

## Agent executor note

The bookkeeping does not depend on who executes. This wiki reads a result a person rejects as the ordinary-defect row, which is routine with an agent. A task that came back because the agent could not begin it is closer to the broken-item row, and this wiki has no source for treating it so.
