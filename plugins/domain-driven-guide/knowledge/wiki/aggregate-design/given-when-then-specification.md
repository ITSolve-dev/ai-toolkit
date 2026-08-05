---
title: Given-When-Then Aggregate Specification
category: aggregate-design
summary: An event-sourced aggregate testing style — Given past events, When a method/command is invoked, Expect resulting events or an exception — that verifies behavior through the event contract, decoupled from internal state, and doubles as a Ubiquitous-Language specification.
tags: [technique, testing, aggregate, event-sourcing, specification, ubiquitous-language, aggregate-design]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

## The shape of the test

[[event-sourcing|Event Sourcing]] gives aggregate tests a natural *Given-When-Expect* form (raw L15788):

1. **Given** — events in the past.
2. **When** — an aggregate method is called.
3. **Expect** — the following events *or* an exception.

Mechanically: "Past Events are used to set up the state of an Aggregate at the beginning of the unit test" (replayed to reconstitute state), the method under test is executed with test arguments and mock [[domain-service|Domain Services]], and "we assert the expected results by comparing Events produced by an Aggregate with expected Events" (raw L15796).

## Why it reduces test fragility

The assertions are made against the [[aggregate|Aggregate]]'s behavioral contract — the events it emits — not its private fields. "We stay decoupled from the internals of the Aggregate state. This helps to reduce test *fragility* because development teams can change and optimize each Aggregate implementation in any way, as long as the behavioral contracts are fulfilled as confirmed by the unit tests" (raw L15800). This is the opposite of state-snapshot assertions, which break on every internal refactor even when behavior is unchanged.

## Specifications in the Ubiquitous Language

The technique extends upward: express the *When* clause as a [[command-object|Command]] passed to the [[application-service|Application Service]] hosting the aggregate, and "express the unit test as a *specification* expressed completely in the terms of our Ubiquitous Language, either through code or by creating a DSL" (raw L15802). Such specifications can be printed as human-readable use cases domain experts can read (raw L15804), for example:

```
[Passed] Use case 'Add Customer Payment - Unlock On Payment'.
Given:
  1. Created customer 7 Eur 'Northwind' ...
  2. Customer locked
When:
  Add 'unlock' payment 10 EUR via unlock
Expectations:
  [ok] Tx 1: payment 10 EUR 'unlock'
  [ok] Customer unlocked
```

This makes the test a shared artifact between developers and domain experts, reinforcing the [[ubiquitous-language|Ubiquitous Language]] rather than hiding behavior behind implementation detail.

## Related

[[aggregate]] · [[event-sourcing]] · [[domain-event]] · [[ubiquitous-language]] · [[functional-event-sourcing]] · [[focused-aggregates]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
