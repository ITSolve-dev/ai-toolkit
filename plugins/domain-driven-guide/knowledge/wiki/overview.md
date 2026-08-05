# Overview

A team reference for Domain-Driven Design's tactical and strategic patterns. Pages are grouped
by the domain's own pattern families; the live catalog is `index.md`.

Vaughn Vernon's *Implementing Domain-Driven Design* ("the red book" — [[book-implementing-ddd-vaughn-vernon]])
is now ingested end to end via the large-source workflow, from the front matter through Appendix A on
Event Sourcing. It is the wiki's canonical anchor: both halves of DDD are filled out in depth, and the
earlier practitioner sources remain cross-linked into the same pages.

Percival & Gregory's *Architecture Patterns with Python* ("Cosmic Python" — [[web-page-cosmic-python-book]])
is now **also ingested end to end** (front matter through Appendix E), a Python-implemented, event-driven
counterpoint. Its treatment is fused directly into the shared building-block pages ([[repository]],
[[unit-of-work]], [[aggregate]], [[domain-event]]) and it contributes several groups of its own — the
read side ([[cqrs]] / [[read-model]]), design principles, testing strategy, and a legacy-refactoring
playbook.

## Groups so far

- **`foundations/`** — what DDD is and whether to use it. [[domain-driven-design]] (the pattern
  language and its two halves), [[when-to-use-ddd]] (the investment decision + scorecard), plus the
  book source summary ([[book-implementing-ddd-vaughn-vernon]]).
- **`building-blocks/`** — the tactical building blocks and the application tier. Model objects:
  [[entity]] (with [[entity-identity-generation]], [[entity-validation]], [[surrogate-identity]],
  [[object-roles]]), [[value-object]] (with [[whole-value]], [[side-effect-free-function]],
  [[standard-type]], [[value-object-persistence]]), [[aggregate]], [[domain-model]], [[domain-service]]
  (with [[domain-service-separated-interface]]), and [[modules]] (with [[module-naming-conventions]]).
  Persistence and lifecycle: the [[repository]] family ([[collection-oriented-repository]],
  [[persistence-oriented-repository]], [[repository-only-persistence]], [[repository-type-hierarchies]],
  [[repository-vs-dao]], [[transaction-management]], [[testing-repositories]]), the [[unit-of-work]]
  transaction seam, and the [[factory]] family
  ([[factory-method-on-aggregate-root]], [[factory-on-service]]). The application tier (Ch. 14):
  [[application-service]] (vs a Domain Service — [[application-service-vs-domain-service]]),
  [[command-object]], [[command-handler]], [[presenting-aggregate-state]], [[use-case-optimal-query]].
- **`aggregate-design/`** — aggregate boundary rules and invariant enforcement.
  [[model-true-invariants-in-consistency-boundaries]], [[design-small-aggregates]],
  [[reference-other-aggregates-by-identity]], [[eventual-consistency-between-aggregates]] /
  [[eventual-consistency]], [[reasons-to-break-aggregate-rules]], [[aggregate-information-hiding]],
  [[aggregate-optimistic-concurrency]], plus the event-sourcing corollaries [[focused-aggregates]] and
  [[given-when-then-specification]].
- **`subdomains/`** — the problem-space classification. [[subdomain]] (core/supporting/generic),
  [[core-domain]], [[problem-space-and-solution-space]].
- **`context-mapping/`** — strategic design: the [[bounded-context]], the [[ubiquitous-language]] it
  scopes, [[bounded-context-sizing]], [[module-before-bounded-context]], and the
  relationships/integrations between contexts — [[context-map]], [[upstream-downstream]],
  [[partnership]], [[shared-kernel]], [[customer-supplier-development]], [[conformist]],
  [[anticorruption-layer]], [[open-host-service]], [[published-language]], [[separate-ways]],
  [[big-ball-of-mud]], [[bounded-context-autonomy]], [[integrating-bounded-contexts]],
  [[duplicating-information-across-bounded-contexts]], [[idempotency]], [[event-driven-integration]],
  [[value-objects-for-integration]], [[domain-events-vs-integration-events]], [[tolerant-reader]],
  [[composing-multiple-bounded-contexts-in-the-ui]], plus source summaries (e.g. [[web-page-ddd-guide-2026]]).
- **`architecture/`** — architecture styles that host a DDD model without dictating it.
  [[architecture-selection]] (risk-driven), [[layered-architecture]],
  [[dependency-inversion-principle]], [[hexagonal-architecture]], [[ports-and-adapters]], [[cqrs]],
  [[rest-and-ddd]].
- **`event-design/`** — domain events, event-driven modelling, and the full Event Sourcing / A+ES suite.
  [[domain-event]], [[domain-event-publisher]], the Cosmic Python [[message-bus]] with its
  [[commands-and-events]] and [[internal-vs-external-events]] distinctions, [[event-driven-architecture]],
  [[long-running-process]],
  [[notification-log]], [[event-de-duplication]], [[event-store]], [[event-sourcing]] (A+ES) — with
  [[aggregate-snapshot]], [[optimistic-concurrency-control]], [[read-model-projection]],
  [[functional-event-sourcing]], and the event-contract-design guidance ([[domain-event-enrichment]],
  [[value-objects-in-contracts]], [[domain-event-contract-design]]), plus source summaries (e.g.
  [[web-page-event-sourcing-guide]]).
- **`anti-patterns/`** — DDD failure modes and misapplications. [[anemic-domain-model]] (tactical),
  [[ddd-lite]] (skipping strategic design), [[blending-models-in-one-context]] (mixing two Languages
  in one model), [[data-model-leakage]] (persistence dictating the model), [[large-cluster-aggregate]]
  (the oversized aggregate), [[infrastructure-leaking-into-the-domain-model]] (I/O reaching into the
  model), [[reusing-the-write-model-for-reads]] (forcing reads through the write model), and
  [[orm-coupled-domain-model]] (framework fat models welded to the ORM).
- **`design-principles/`** — cross-cutting design guidance (mostly Cosmic Python). [[abstractions]],
  [[coupling-and-cohesion]], [[decoupling-domain-logic-from-infrastructure]], and [[validation]]
  (syntax / semantics / pragmatics, validate at the edge).
- **`testing/`** — where to place tests in a DDD codebase. [[test-coupling-vs-design-feedback]],
  [[domain-model-tests-as-living-documentation]], [[expressing-the-service-layer-in-primitives]].
- **`read-models/`** — the CQRS read side. [[command-query-separation]] (the seed principle) and
  [[read-model]] (the denormalized, event-updated read side).
- **`refactoring-toward-ddd/`** — moving a legacy system toward DDD. [[refactoring-toward-ddd]]
  (in place) and the [[strangler-fig-pattern]] (wholesale replacement via event interception).
- **`domain-modeling/`** — [[collaborative-domain-modeling]] (event storming, CRC, event modeling).

New groups appear as sources introduce topics that no existing group covers (see the grouping
principle in `SCHEMA.md`).
