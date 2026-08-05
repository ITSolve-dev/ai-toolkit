---
title: Domain Event Enrichment
category: event-design
summary: A domain-event design rule of thumb — enrich events with identifiers and display properties so they satisfy ~80% of subscribers, resolving the tension between an event's minimal reconstitution payload and the richer data downstream projections need.
tags: [guideline, domain-event, event-design, event-sourcing, projection, rule-of-thumb]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

## The tension: events serve two masters

In [[event-sourcing|A+ES]], domain events carry a dual purpose: "Events are used both for Aggregate persistence and to communicate domain-level happenings around the enterprise by means of Event publishing" (raw L15500). The minimal payload sufficient to reconstitute an [[aggregate|Aggregate]] via [[event-sourcing]] is often too thin for downstream consumers.

## The worked example

A `ProjectArchived` event carrying only `ProjectId`, `ChangeAuthorId`, `ArchivedUtc`, and an optional comment is "rich enough to be used to reconstitute an archived `Project`" (raw L15515) — but a `ArchivedProjectsPerCustomer` [[read-model-projection|projection]] that wants project names, customer names, and project→customer assignments must then subscribe to and join *four* different event streams to build one view. Adding `ProjectName`, `Customer`, and `CustomerName` fields to the event collapses that join: the additional members "would not be essential for reconstituting the state of the corresponding Aggregate but would noticeably simplify our Event consumers" (raw L15531).

## The rule of thumb

"A Domain Event rule of thumb says to design them with enough information to satisfy 80 percent of subscribers, even though doing so would require Events to have more information than needed by a good number of subscribers" (raw L15553). Concretely, usually include:

- **Entity identifiers** that own/master the event, e.g. `CustomerId` for `Customer` (raw L15555).
- **Display-oriented properties** — names and similar fields used for presentation, e.g. `ProjectName`, `CustomerName` (raw L15557).

## Trade-offs and when it does not apply

These are "recommendations, not rules" (raw L15559). The payoff scales with distribution: "They usually work well for enterprises that have a lot of different Bounded Contexts. Monolithic Bounded Contexts benefit less from these suggestions, since they tend to maintain secondary lookup tables and Entity maps" (raw L15559). Over-enriching inside a monolith adds payload and coupling for little gain; under-enriching across many [[bounded-context|Bounded Contexts]] pushes join complexity into every subscriber. The cost side is real too — richer events duplicate data that can go stale relative to its source aggregate, and widen the event contract that must be versioned (see [[domain-event-contract-design]]).

## Related

[[domain-event]] · [[read-model-projection]] · [[domain-event-contract-design]] · [[bounded-context]] · [[event-sourcing]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
