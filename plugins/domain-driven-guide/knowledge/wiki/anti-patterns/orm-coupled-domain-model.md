---
title: ORM-coupled domain model (framework fat models)
category: anti-patterns
summary: Building the domain model directly on a CRUD framework's ActiveRecord ORM — convenient early but obstructs complex domain modeling, because the model is a DB row, framework tooling can bypass invariants, and the fat-models approach runs into cross-app scalability problems.
tags: [anti-pattern, coupling, orm, fat-models, active-record, django, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# ORM-coupled domain model (framework "fat models")

A recurring failure mode when applying DDD inside a CRUD-oriented framework (Django is the worked example) is coupling the domain model **directly to the framework's ActiveRecord ORM**. The same coupling that makes early development fast starts to actively obstruct modeling once the domain becomes a web of stateful rules.

## Why it fights complex domains

The framework is optimized for a specific sweet spot:

> "the entire reason that Django is so great is that it's designed around the sweet spot of making it easy to build CRUD apps with minimal boilerplate. But the entire thrust of our book is about what to do when your app is no longer a simple CRUD app." (raw L7696)

Because an ActiveRecord model *is* a database row, it cannot also be a persistence-ignorant domain object (see [[repository]]): "our ActiveRecord and our domain model can't be the same object" (raw L7684..7687). Any logic pushed into the model is logic coupled to the DB schema and migrations.

## The two symptoms

1. **Tooling that bypasses your invariants.** Generic CRUD tooling edits rows directly, ignoring the domain's state-change rules: "Things like the Django admin, which are so awesome when you start out, become actively dangerous if the whole point of your app is to build a complex set of rules and modeling around the workflow of state changes. The Django admin bypasses all of that." (raw L7698)
2. **Fat models don't scale.** The "fat models" approach — "push as much logic down to your models as possible, and apply patterns like [[entity|Entity]], [[value-object|Value Object]], and [[aggregate|Aggregate]]" (raw L7708) — is viable for moderate complexity, but "people find that the fat models approach runs into scalability problems of its own, particularly around managing interdependencies between apps" (raw L7712..7714). Note this is the *opposite* extreme from the [[anemic-domain-model]] yet still a coupling problem: behavior is present but welded to the persistence layer.

## Remedies / decision heuristics

- **Extract a business-logic / domain layer** between views/forms and the ORM, keeping `models.py` minimal: "extracting out a business logic or domain layer to sit between your views and forms and your `models.py`, which you can then keep as minimal as possible." (raw L7715..7716)
- **Low-cost first step:** "put a `logic.py` into every Django app from day one" to keep forms, views, and models free of business logic; it "can become a stepping-stone for moving to a fully decoupled domain model and/or service layer later" (raw L7722). It may start out working on framework model objects and only later become fully decoupled onto plain Python structures (raw L7724).
- **Reads:** "you can get some of the benefits of CQRS by putting reads into one place, avoiding ORM calls sprinkled all over the place." (raw L7727) — see [[cqrs]] and [[read-model]].
- **Module boundaries:** decouple domain/read modules from the framework's app hierarchy, because "Business concerns will cut across them." (raw L7729)
- **Full [[repository]] + [[unit-of-work]] + [[application-service|service layer]]** decouple you from the framework and DB entirely, but are "quite a lot of work" whose short-term payoff is mainly faster unit tests (raw L7704) — worth it only once complexity or slow tests justify it.

## Related

- [[repository]] — the pattern (with its Data Mapper vs ActiveRecord distinction) this anti-pattern guards against.
- [[unit-of-work]] · [[application-service|service layer]] — the full decoupling stack.
- [[anemic-domain-model]] — the opposite extreme (behavior drained *out* of the model).
- [[cqrs]] · [[read-model]] — where the "reads in one place" remedy leads.
- [[persistence-ignorance]] — the property ActiveRecord coupling destroys.
