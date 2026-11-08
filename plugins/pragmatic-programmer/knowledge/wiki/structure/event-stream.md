---
title: Event stream
category: structure
summary: "Events treated as a collection that grows as they arrive, so they can be filtered, merged and zipped; the alternative is hand-kept timers, counters and buffers correlating asynchronous callbacks."
tags: [concept, events, reactive, streams, asynchrony]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

An event stream treats events as if they were a collection of data: a list that gets longer as events occur (p. 183). It adds the dimension of time that message passing lacks. The book introduces it for systems that must react to events in combination, where passing messages alone is not enough (pp. 182-183).

## From reactive values to streams

The book's entry point is a spreadsheet: a cell whose formula refers to another cell updates when that cell changes, so values react to changes in the values they use (p. 183). This wiki leaves frameworks that provide such data-level reactivity out, as library documentation.

Streams extend the idea from values to events. The appeal the book names is that a stream can be handled like any other collection: transformed, combined, filtered, even merged with ordinary collections, and it can be asynchronous, so code reacts to events as they arrive (p. 183).

## What the examples show

The book's listings use one reactive library, whose details are out of scope here. This wiki reads two behaviours as independent of it (pp. 183-185):

- Pairing a fixed list with a half-second timer yields one combined event every 500 ms. The pace of the combination is set by when both sides have a value.
- Launching three requests for ids 3, 2 and 1 through one stream runs them in parallel, and results appear in order of completion: id 2 at 82 ms, then the other two about 50 ms later.

The source of a stream can be swapped. The book replaces a static list of ids with one fed by users logging in, and the rest of the code stays the same (p. 185).

## Why the abstraction pays

The book's claim is that this spares you from thinking of time as something you have to manage: «Потоки событий обобщают синхронную и асинхронную обработку в общем удобном API.» (p. 185)

This wiki reads the practical test as follows. If code keeps its own timers, counters and buffers to relate one asynchronous event to another, that bookkeeping is what a stream replaces, where the project already has a stream library. For a single window with no such library, this wiki keeps the short hand-written list of [[state-machine-or-event-stream-or-pubsub]].

## Limits

The book's answer to exercise 20 names one cost: a stream could notify several accounting systems of an order, but those systems would then have to be designed around streams too, so publish-subscribe fits better there (p. 357). See [[observer-vs-publish-subscribe]].

This wiki notes another: the logic moves into chains of operators, and the order of results is no longer the order of the code, so anything depending on arrival order must be stated explicitly, as the ids example shows. For events that are merely ordered within one sequence, [[finite-state-machine]] is the lighter tool.

## Source

[[pragmatic-programmer]], Topic 29, Russian edition, pp. 182-185; p. 357 for the answer to exercise 20. The reading of the two behaviours as independent of the library, the practical test and the second cost are this wiki's own. Timings are the book's sample run and carry no general meaning. Related: [[event-driven-code]], [[programs-transform-data]].
