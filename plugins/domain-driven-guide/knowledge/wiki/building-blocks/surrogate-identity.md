---
title: Surrogate Identity
category: building-blocks
summary: A second, ORM-only identity carried by an entity to satisfy tools like Hibernate, kept hidden so it doesn't leak persistence into the domain.
tags: [pattern, tactical-pattern, entity, identity, orm, persistence-leakage, layer-supertype]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

A **surrogate identity** is a second identity carried by an [[entity]] purely to satisfy an ORM, kept
distinct from the **domain identity** the model actually cares about.

## Why it exists

ORMs like Hibernate "want to deal with object identity on their own terms," preferring the database's
native type (e.g. a numeric sequence) as each Entity's primary key. When the domain requires a different
kind of identity, that conflict is resolved by keeping **two identities** (raw L4259):

> "One of the identities is designed for the domain model and adheres to the requirements of the domain.
> The other is for Hibernate and is known as a surrogate identity." (raw L4259)

## How to model it

Add a `long`/`int` attribute plus a DB column with a primary-key constraint, mapped through an `<id>`
element that "has nothing to do with the domain-specific identity" (raw L4261). Then **hide** it — an
exposed surrogate is persistence leakage:

> "Because the surrogate is not part of the domain model, visibility constitutes persistence leakage."
> (raw L4263)

Hide it behind a **Layer Supertype** [Fowler, P of EAA] — an abstract `IdentifiedDomainObject` base
class with `protected` (or `private`) accessors, so clients never see the surrogate while Hibernate
reflects into any visibility (raw L4265). Further Layer Supertypes can add optimistic-concurrency state
(see [[aggregate]]).

## Domain identity coexists

In the `tbl_user` example the surrogate `id` is the DB primary key, while the domain identity is a
separate composite unique key over `tenant_id_id` + `username` (raw L4330):

> "There is no need for the domain identity to play the role of database primary key. We allow the
> surrogate id to serve as the database primary key, which keeps Hibernate happy." (raw L4332)

Surrogate keys also serve as foreign keys elsewhere for referential integrity, audits, tool support,
and join optimization when reading [[aggregate]]s out of the database (raw L4334).

## Related

- [[entity]] — the building block that carries both identities.
- [[entity-identity-generation]] — how the *domain* identity is created; surrogate is the ORM's own.
- [[value-object-persistence]] — the same hidden-surrogate-key technique applied to persisted Values.
- [[data-model-leakage]] — the anti-pattern an exposed surrogate is a symptom of.
- [[aggregate]] — where the Layer Supertype also carries concurrency state.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
