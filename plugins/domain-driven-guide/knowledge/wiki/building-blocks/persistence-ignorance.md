---
title: Persistence Ignorance
category: building-blocks
summary: The principle that the domain model should know nothing about how its objects are loaded or saved, keeping it free of dependencies on any particular database technology.
tags: [concept, persistence-ignorance, orm, dependency-inversion, classical-mapping, building-blocks, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

**Persistence ignorance** is the principle that the domain model should not know anything about how its objects are stored or retrieved. It is what an ORM is really there to buy you:

> "The most important thing an ORM gives us is *persistence ignorance*: the idea that our fancy domain model doesn't need to know anything about how data is loaded or persisted. This helps keep our domain clean of direct dependencies on particular database technologies." (raw L1125)

It is the goal that the [[repository]] pattern operationalizes at the data-access boundary; this page is about the model itself and the mapping technique that keeps it clean.

## Why: the domain model on the inside

A layered architecture keeps UI, logic, and database separate, each layer depending only on the one below. DDD pushes further — the domain model should be at the center of an *onion*, with dependencies flowing *inward* toward it:

> "But we want our domain model to have *no dependencies whatsoever*. We don't want infrastructure concerns bleeding over into our domain model and slowing our unit tests or our ability to make changes." (raw L1087)

A persistence-ignorant model is fast to unit-test (no database or fixtures to stand up) and cheap to change.

## The anti-pattern: the naive ORM model

Following the typical ORM tutorial, you declare model classes that inherit from the ORM's `Base` and whose attributes are `Column` definitions. This looks convenient but inverts the dependency the wrong way — the model is now *coupled to database columns*:

> "our pristine model is now full of dependencies on the ORM ... How can it be separate from storage concerns when our model properties are directly coupled to database columns?" (raw L1148)

This is a common route into an [[anemic-domain-model]]: classes that are really table rows dressed up as objects. The domain is no longer ignorant of storage.

## The technique: classical mapping (invert the dependency)

The alternative is to define the database schema *separately* from the domain classes, and to define an explicit **mapper** that binds one to the other (SQLAlchemy calls this a *classical mapping*). The domain classes stay plain Python objects; a `start_mappers()` function wires them to tables at runtime.

The crucial property is the direction of dependency:

> "The ORM imports (or \"depends on\" or \"knows about\") the domain model, and not the other way around." (raw L1173)

If `start_mappers()` is called, instances load and save transparently; if it is never called, "our domain model classes stay blissfully unaware of the database" (raw L1181). You still get the ORM's benefits — migrations via Alembic, querying through your domain classes — without the coupling. This is the [[dependency-inversion-principle]] applied to persistence.

## Payoff

Because the model is decoupled, the persistence layer becomes replaceable:

> "the domain model stays \"pure\" and free from infrastructure concerns. We could throw away SQLAlchemy and use a different ORM, or a totally different persistence system, and the domain model doesn't need to change at all." (raw L1213)

A concrete illustration: deciding to move allocations from `Batch` onto `OrderLine`. With plain-old-Python objects you "can change a `set()` to being a new attribute, without needing to think about the database until later" (raw L1487) — whereas with an ActiveRecord framework like Django you would have to define and reason through a database migration *before* you could run any tests.

## Trade-off and failure mode

Persistence ignorance is not absolute purity. The further your model strays from the object-oriented paradigm, the harder the mapping becomes:

> "you may find it increasingly hard to get the ORM to produce the exact behavior you need, and you may need to modify your domain model." (raw L1215)

This is an architectural trade-off, and the authors invoke the Zen of Python — "Practicality beats purity!" (raw L1220). The failure mode to watch for is over-investing in purity on a simple app: for thin CRUD the decoupling is more work than it is worth (see the trade-offs in [[repository]]). The investment pays off in proportion to domain complexity.

## Related

- [[repository]] — the abstraction that operationalizes persistence ignorance at the data boundary.
- [[dependency-inversion-principle]] — the principle behind pointing the ORM at the domain, not the reverse.
- [[anemic-domain-model]] — the failure the naive ORM model slides into.
- [[aggregate]] · [[entity]] · [[value-object]] — the model elements kept persistence-ignorant.
- [[web-page-cosmic-python-book]] — source summary.
