---
title: "Source Summary — Гайд по эвент-сорсингу (Event Sourcing Guide)"
category: event-design
summary: A practitioner's guide to event sourcing, mined for its DDD-relevant content on domain events, aggregates as consistency boundaries, and the domain-vs-integration event boundary.
tags: [summary, event-sourcing, domain-events, aggregates]
sources: [web-page-event-sourcing-guide]
created: 2026-07-25
updated: 2026-07-25
---

**Source:** "Гайд по эвент-сорсингу" (Event Sourcing Guide), a Russian-language Habr article by
a practising backend engineer (payment systems), with a companion example repo
(`github.com/aurokk/event-sourcing`). Origin: <https://habr.com/ru/articles/717774/>.
Raw extraction: `raw/web-page-event-sourcing-guide.md`.

## What it is

A hands-on guide to event sourcing (ES): what it is, how it reshapes application design, the
questions to answer before adopting it, event-store technology trade-offs, and when to use ES
vs. not. It is opinionated field experience, not a formal reference.

## Relevance verdict — partly in scope

ES is largely infrastructure/plumbing, which this DDD wiki does not collect. But the article's
**domain-modelling core is in scope** and was distilled into these pages:

- [[domain-event]] — the definition of a domain event (immutable record of a past fact), the
  **event-vs-command** distinction, the rule that reconstitution must not re-run domain
  validation, and the contrast with command sourcing.
- [[aggregate]] — the aggregate as a **consistency + transactional boundary**, its clean mapping
  onto an event stream, and boundary enforcement via optimistic concurrency.
- [[domain-events-vs-integration-events]] — the strategic point that domain events must stay
  inside one bounded context; sharing them across services makes them a coupling contract.

## What was set aside, and why

Deliberately dropped as out-of-scope for a DDD charter (event-sourcing plumbing / tooling):

- **Event-store technology selection** (MySQL, MongoDB, Azure CosmosDB, EventStoreDB, Kafka) —
  infrastructure comparison, not a DDD concept.
- **Scaling** read/write load, log sharding, head-of-line blocking — infrastructure.
- **UI consistency** patterns (task-based UI, front/back-end polling) — infrastructure.
- **Physical data deletion / GDPR** handling — infrastructure.
- **Actors / Orleans** as a wrapper over aggregates — framework tooling (a modelling curiosity,
  but tool-specific).
- **CQRS** — presented as a natural consequence of ES (separate read/write models). DDD-adjacent
  but not named in this wiki's charter; noted here, no page created.

## How to read it

Authoritative as lived experience from someone building event-sourced payment systems; the
domain-event and aggregate framing is sound and aligns with mainstream DDD. Treat the
technology verdicts as one engineer's opinion (the author says as much), and note the strong
"Kafka is not an event store by default" stance is contested.

## Reader discussion

The article has 100+ comments (JavaScript-loaded; not captured by the HTML adapter — fetched
separately from the comments endpoint). Held to a stricter bar than the author's own text, only
two points cleared it and are recorded on the relevant pages, attributed to their commenters:

- **powerman** — challenges how principled the domain-vs-integration event split really is →
  recorded on [[domain-events-vs-integration-events]].
- **linefight** — optimistic concurrency via a unique `(AggregateType, AggregateId, EventId)`
  index to enforce the aggregate boundary → recorded on [[aggregate]].

Dropped: double-charge / eventual-consistency worries (gandjustas, powerman), skepticism about
ES's value (tsvettsih, blib), and auditability anecdotes (gybson_63, dph) — all about ES
applicability/plumbing rather than a DDD pattern, or unreasoned opinion.
