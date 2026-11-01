---
title: Accounting for Abandoned Work
category: reading-history
summary: When started work is dropped, do not delete it; move it to the finished state, record the date, and tag it as abandoned, so analytics can include or filter it and cumulative flow diagrams stay valid.
tags: [method, abandoned-work, metrics, data-hygiene, cumulative-flow-diagram, segmentation, vacanti]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Accounting for Abandoned Work

Accounting for abandoned work is the procedure for keeping dropped items in a board's data, so that a legitimate decision to stop does not corrupt later analysis. Vacanti's phrasing of why it matters: "it is absolutely necessary to account for them properly in your data" ([[vacanti-actionable-agile-metrics]] L2300). The wider choice between tagging a departure and erasing an arrival is on [[non-standard-departure]]; this page is the case of work that was started and will not come back.

## The procedure

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

## What it buys

Vacanti's benefit is choice at analysis time: a [[cumulative-flow-diagram]] of all items, of only those finished normally, or of only the abandoned (L2304). And:

> not only have we not violated the principle of the CoF, but we can also guarantee that we will be able to generate a valid CFD for all of those views.
>
> — [[vacanti-actionable-agile-metrics]], L2304

This wiki reads the mechanism as: a deleted item either disappears from counts it was already part of, or lingers as forever-open work, and either way the record of what entered no longer matches what left.

## A tension in the source

Vacanti says both that correct accounting has "not violated" CoF (L2304) and that every abandoned start violated it and impaired predictability (L2334). This wiki reads these as two senses. The process sense is violated whenever work is dropped, which is why the upstream question exists. The data sense is preserved by accounting, which is why the charts stay valid. Treat the first as a thing to learn from, and the second as a thing to do every time.

## Signs

These are this wiki's transfer and raise a question rather than a verdict:

- History shows an item in a started state that no longer exists on the board: it was deleted.
- Started count exceeds finished plus open count over a period: something left without being recorded.
- Nothing is ever tagged abandoned on a board with a long history. Either nothing was abandoned, or it left some other way.
- A rising share of abandoned items: look upstream at when commitment happens ([[just-in-time-commitment]]).

## Trade-offs and failure modes

The source does not name the cost. This wiki reads it as this: the final state now holds work that was never delivered. Any [[throughput]] or [[cycle-time]] reading that does not filter on the tag counts abandoned items as finished, and their short or long lives distort both. A count of finished work must therefore say whether it includes them. A board whose final state means something public, such as deployed, also reads falsely to anyone not filtering, which is why Vacanti's "whatever that means in your context" (L2300) is worth deciding deliberately.

The chapter closes on the same point: "just remember to account for that action appropriately in your data" (L2342).

## Agent note

Board history is kept mechanically, so this survives an agent executing and may be easier to enforce: dropping a task is an event a tool can record, rather than a habit someone has to remember. Keeping logged hours is not required for any of it.
