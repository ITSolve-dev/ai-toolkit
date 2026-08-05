---
title: Expressing the service layer in primitives
category: testing
summary: A decoupling technique — rewrite service-layer functions to accept primitive arguments instead of domain objects, and set up test state through service use cases rather than by hand-building model objects, so the service layer and its tests depend only on the service API, leaving the domain model free to refactor.
tags: [technique, testing, service-layer, application-service, decoupling, fakes, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

The [[application-service|service layer]] forms a stable API over the [[domain-model]]. Testing against that API — rather than against model internals — "reduces the amount of code that we need to change when we refactor our domain model. If we restrict ourselves to testing only against the service layer, we won't have any tests that directly interact with 'private' methods or attributes on our model objects, which leaves us freer to refactor them" (raw L2537). But a service layer that *accepts and returns domain objects* still leaks the domain into its callers and tests. Fully decoupling it is a technique in three moves.

## 1. Accept primitives, not domain objects

Instead of taking a domain object:

`def allocate(line: OrderLine, repo: AbstractRepository, session) -> str:` (raw L2583)

widen the signature to primitives:

```
def allocate(orderid: str, sku: str, qty: int, repo: AbstractRepository, session) -> str:
```
(raw L2586)

Callers — including tests — no longer need to construct an `OrderLine`. This is the concrete meaning of the book's closing rule of thumb: "Express your service layer in terms of primitives rather than domain objects" (raw L2737).

## 2. Stop hand-building model objects for setup

Even with primitive parameters, tests still instantiate `Batch` to seed the repository: "if one day we decide to massively refactor how our `Batch` model works, we'll have to change a bunch of tests" (raw L2600). An intermediate fix is a factory fixture on the fake, e.g. `FakeRepository.for_batch(ref, sku, qty, eta)` (raw L2612), which at least "move[s] all of our tests' dependencies on the domain into one place" (raw L2622). See the fake repositories discussed on [[repository]].

## 3. Seed state through service use cases

The fuller move is to add the missing use case — an `add_batch` service — and set up test state by *calling it*, removing every domain dependency:

```
def test_add_batch():
    repo, session = FakeRepository([]), FakeSession()
    services.add_batch("b1", "CRUNCHY-ARMCHAIR", 100, None, repo, session)
    assert repo.get("b1") is not None
    assert session.committed
```
(raw L2628)

Now allocation tests read purely in service terms — `services.add_batch(...)` then `services.allocate(...)` — "depend[ing] on only the service layer itself, leaving us completely free to refactor the model as we see fit" (raw L2670).

## The completeness heuristic

The diagnostic that motivates the whole technique:

> In general, if you find yourself needing to do domain-layer stuff directly in your service-layer tests, it may be an indication that your service layer is incomplete. (raw L2634)

Doing domain setup by hand in a service test is the symptom; the cure is usually a missing service use case.

## Caveat and downstream payoff

Don't invert the tail wagging the dog: "Should you write a new service just because it would help remove dependencies from your tests? Probably not. But in this case, we almost definitely would need an `add_batch` service one day anyway" (raw L2650). Add the service because the application needs it; the test decoupling is a bonus. The same completeness pays off at the edges — an `add_batch` API endpoint lets end-to-end tests drop hardcoded SQL fixtures and "be free of... the direct dependency on the database" (raw L2673). Book's ideal: "you'll have all the services you need to be able to test entirely against the service layer, rather than hacking state via repositories or the database" (raw L2739).

## Related

- [[test-coupling-vs-design-feedback]] — the trade-off this technique optimizes.
- [[domain-model-tests-as-living-documentation]] — the exploratory tests this replaces with durable ones.
- [[application-service]] — the service layer being expressed in primitives.
- [[repository]] — the fake repositories used to seed test state.
- [[web-page-cosmic-python-book]] — source summary (Ch. 5, "TDD in High Gear and Low Gear").
