---
title: Test coupling vs. design feedback trade-off
category: testing
summary: The central trade-off governing where to place tests in a DDD codebase — tests near the domain model give strong design feedback but couple tightly to implementation, while tests near the service layer or HTTP API survive refactors cheaply but reveal nothing about fine-grained object design.
tags: [heuristic, testing, tdd, domain-model, service-layer, coupling, refactoring, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

Every automated test couples the test suite to the code it exercises. In a layered DDD codebase this produces a spectrum: the closer a test sits to the [[domain-model]], the more design feedback it gives you and the more tightly it glues the model into a particular shape; the closer it sits to the [[application-service|service layer]] or the HTTP API, the freer you are to refactor the internals underneath it. Choosing a level is therefore not a matter of taste but of deciding, for a given piece of work, whether you value **design feedback** or **freedom to change** more right now.

## The glue insight

Tests are not free coverage. They are commitments:

> Every line of code that we put in a test is like a blob of glue, holding the system in a particular shape. The more low-level tests we have, the harder it will be to change things. (raw L2539)

The purpose of a test is to pin a *property of the system* so it can't drift while you work — that the API returns 200, that the session commits, that orders are still allocated (raw L2533). The flip side is unavoidable: "if we want to change the design of our code, any tests relying directly on that code will also fail" (raw L2535).

## The test spectrum

The book arranges the three test levels along three correlated axes (raw L2547):

- **Domain tests** — high feedback, high barrier to change, focused coverage.
- **Service-layer tests** — the middle: moderate feedback, lower coupling, high coverage.
- **API tests** — low feedback, low barrier to change, high system coverage.

Domain tests let you "listen to the code" — XP's phrase — and notice when an object is hard to use or smells, which triggers a redesign (raw L2549). You only get that feedback working close to the target code: "A test for the HTTP API tells us nothing about the fine-grained design of our objects, because it sits at a much higher level of abstraction" (raw L2551). Conversely, API tests let you "rewrite our entire application and, so long as we don't change the URLs or request formats, our HTTP tests will continue to pass" (raw L2553) — confidence for large-scale changes like a database schema migration.

## The high-gear / low-gear decision rule

The operative heuristic is a cycling metaphor (raw L2574): start in a **low gear** to overcome inertia, shift to **high gear** to move efficiently once running, and drop back down when a hill or hazard appears.

- **High gear (test against the service layer)** for routine work: "Most of the time, when we are adding a new feature or fixing a bug, we don't need to make extensive changes to the domain model... we prefer to write tests against services because of the lower coupling and higher coverage" (raw L2566). Examples given: writing an `add_stock` function or a `cancel_order` feature (raw L2568).
- **Low gear (test against the domain model)** when "starting a new project or when hitting a particularly gnarly problem... so we get better feedback and executable documentation of our intent" (raw L2572).

## Failure mode

The misapplication this chapter targets is over-testing the model: "often we see teams writing too many tests against their domain model. This causes problems when they come to change their codebase and find that they need to update tens or even hundreds of unit tests" (raw L2531). The symptom is a refactor of the model breaking a large fan-out of low-level tests. The remedy is to move the bulk of coverage up to the service layer and reserve domain tests for design exploration — see [[domain-model-tests-as-living-documentation]] and [[expressing-the-service-layer-in-primitives]].

## Related

- [[domain-model-tests-as-living-documentation]] — the payoff of the high-feedback end.
- [[expressing-the-service-layer-in-primitives]] — the technique that makes service-layer tests fully decouple from the model.
- [[application-service]] — the "service layer" whose tests sit in the middle of the spectrum.
- [[domain-model]] — the target of the high-coupling, high-feedback tests.
- [[web-page-cosmic-python-book]] — source summary (Ch. 5, "TDD in High Gear and Low Gear").
