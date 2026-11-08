---
title: Event-driven code
category: structure
summary: "Reacting code with no chosen strategy, so that handlers tangle together: map the shape of the problem to a state machine, observer, publish-subscribe or an event stream."
tags: [concept, events, coupling]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

Event-driven code is organised to react to events. The book defines an event as the availability of some information: «Событие представляет собой доступность некоторой информации.» (p. 176) It can come from outside, like a button click or a stock quote update, or from inside, like a finished computation or a search result, and it can be as small as fetching the next item of a list (p. 176).

## Why build this way

The book's claim is that applications behave better in the real world when designed to respond to events, feeling more interactive and using resources better (p. 176). It also claims that event-handling code can be more responsive and better decoupled than its linear counterpart (p. 185).

Its warning runs the other way as well: without a deliberate strategy, such applications quickly become masses of tightly coupled code (p. 176). The book also notes that some events are easy to miss, such as a user logging in or a line in a file matching a pattern (p. 185).

## Four strategies

The book offers four strategies (p. 177). The right-hand column is this wiki's reading of when each fits; the book describes the strategies and does not give this mapping as a list.

| Strategy | Fits when |
|---|---|
| [[finite-state-machine]] | what an event means depends on the events before it, in one sequence |
| Observer ([[observer-vs-publish-subscribe]]) | listeners can know the source and run inside it |
| Publish-subscribe ([[observer-vs-publish-subscribe]]) | producers and consumers should not know each other |
| [[event-stream]] | events must be combined, or their timing matters |

## Worked choices in the book

The closing exercise asks which technology, or combination, fits each of four cases (p. 186), and the appendix reasons through them (pp. 356-357). [[state-machine-or-event-stream-or-pubsub]] holds those cases with their signs and repair.

The book says few of its answers have a single correct solution (p. 20), so [[pragmatic-programmer]] treats them as the authors' line of reasoning and not as the correct form.

## Source

[[pragmatic-programmer]], Topic 29, Russian edition, pp. 176-177, 185-186; pp. 356-357 for the answer to exercise 20. The mapping column is this wiki's own. Related: [[coupling]].
