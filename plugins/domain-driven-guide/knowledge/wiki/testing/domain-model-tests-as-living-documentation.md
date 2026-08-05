---
title: Domain-model tests as living documentation
category: testing
summary: Tests written in the ubiquitous language flesh out the model, guide its design, and serve as executable documentation for newcomers — but they couple tightly to a specific implementation and must be replaced or deleted when that implementation is refactored.
tags: [concept, testing, tdd, ubiquitous-language, living-documentation, design-feedback, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

Tests written directly against the [[domain-model]], phrased in the [[ubiquitous-language]], do double duty: they drive the model's design and they document it. This is the payoff at the low-feedback-cost, high-design-feedback end of the [[test-coupling-vs-design-feedback]] spectrum, and it is the reason to write domain tests at all despite their coupling cost.

## Tests as a design driver

Writing a behaviour as a domain test first surfaces the objects and collaborations the model needs. The book's own chapter-1 tests "helped us to flesh out our understanding of the objects we need. The tests guided us to a design that makes sense and reads in the domain language" (raw L2555). The confidence check is linguistic: "When our tests read in the domain language, we feel comfortable that our code matches our intuition about the problem we're trying to solve" (raw L2557). A test that reads awkwardly is a signal the model or its naming is wrong — the code smell that triggers a redesign.

## Tests as documentation

Because they are written in the domain language, these tests explain the model to people, not just to CI:

> Because the tests are written in the domain language, they act as living documentation for our model. A new team member can read these tests to quickly understand how the system works and how the core concepts interrelate. (raw L2561)

A domain test such as `test_prefers_current_stock_batches_to_shipments` (raw L2511) reads as a statement of an allocation rule, not as a mechanical assertion — that is what makes it documentation.

## The coupling cost, and the disposal rule

The same closeness that yields feedback is the coupling that constrains change. These tests are exploratory sketches with a limited lifespan:

> We often "sketch" new behaviors by writing tests at this level to see how the code might look. When we want to improve the design of the code, though, we will need to replace or delete these tests, because they are tightly coupled to a particular implementation. (raw L2563)

The practical guidance that follows: keep domain tests for starting a project or working through a gnarly modelling problem, and be willing to throw them away once the design settles, moving durable coverage to the [[application-service|service layer]] via [[expressing-the-service-layer-in-primitives]]. Treating exploratory domain tests as permanent regression tests is the misapplication that leads to the tens-or-hundreds-of-tests-to-update problem described in [[test-coupling-vs-design-feedback]].

## Related

- [[test-coupling-vs-design-feedback]] — the spectrum this page sits at one end of.
- [[expressing-the-service-layer-in-primitives]] — where durable coverage moves once the design settles.
- [[ubiquitous-language]] — what makes these tests readable as documentation.
- [[domain-model]] — the target of these tests.
- [[web-page-cosmic-python-book]] — source summary (Ch. 5, "TDD in High Gear and Low Gear").
