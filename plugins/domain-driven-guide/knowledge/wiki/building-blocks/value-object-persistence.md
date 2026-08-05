---
title: Persisting Value Objects
category: building-blocks
summary: Strategies for storing Value Objects along with their owning Aggregate — denormalize into the parent row, serialize a collection into one column, back a collection with a hidden surrogate key, or use a join table — chosen without letting persistence corrupt the model.
tags: [technique, persistence, orm, aggregate, value-object]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

Value Objects are not persisted on their own; they are stored and reconstituted *with* the [[aggregate]]
that contains them. "All of the following examples are based on the assumption that an Aggregate is being
added to or read from its **Repository**, and its contained Values are persisted and reconstituted
behind the scenes along with the Entity — such as the [[aggregate|Aggregate Root]] — that contains them"
(raw L5974). The overriding constraint is to persist without triggering [[data-model-leakage]]:
"maintain a domain model perspective rather than a persistence perspective" (raw L5988).

## Strategy 1 — Denormalize a single Value into the parent's row (preferred)

The common and cleanest case: store each attribute of the Value in separate columns of the *parent
Entity's* table row. "Its attributes are stored in the same database table row as its parent Entity
object. This makes the storage and retrieval of Values clean and optimized and prevents any persistence
store leakage into the model" (raw L5984). Nested Values denormalize too — Vernon maps
`BusinessPriority.ratings.benefit` to a `business_priority_ratings_benefit` column, so no joins are
needed even for deeply nested Values, and the object navigation path still maps cleanly to a queryable
SQL column (raw L6057). A column-naming convention following the navigation path keeps this legible.

## Strategy 2 — Serialize a collection into a single column

A `List`/`Set` of Values can be serialized to one text column. Trade-offs to weigh before choosing (raw
L6075):

- **Column width** — if the element count or per-element serialized width is unbounded, the text can
  overflow the column/row byte limits; avoid it then.
- **Not queryable** — serialized attributes cannot appear in SQL query expressions.
- **Custom user type** — requires a serialization/deserialization type (one well-designed
  implementation can serve all Value collections).

## Strategy 3 — Back a collection with a database entity + hidden surrogate key

The "very straightforward" approach for collections: treat the Value type as a *data-model* entity — its
own table, its own primary key — while keeping it a Value in the domain. This "*must not* lead to
wrongly modeling a concept as an Entity in the domain model just because it is best represented as a
database entity for the sake of persistence. It is the object-relation impedance mismatch that in some
cases requires this approach, not a DDD principle" (raw L6091).

Vernon hides the surrogate key in a **Layer Supertype**: an abstract `IdentifiedDomainObject` holds a
`protected long id`, and `IdentifiedValueObject` extends it as a marker so "the modeling challenge it
addresses [is] more explicit" (raw L6136). His `GroupMember` (a Value) extends `IdentifiedValueObject`
and is collected by the `Group` [[aggregate|Aggregate Root]] as a `Set<GroupMember>` (raw L6161).
Persistence caveat: for **whole-collection replacement**, call the collection's `clear()` before
reassigning, or the ORM leaves orphaned rows in the store (raw L6190). See [[surrogate-identity]] for the
same hiding technique on Entities.

## Strategy 4 — Join table (composite-element)

An ORM can persist a Value collection to a dedicated join table keyed by the parent's foreign key, with
no surrogate key on the Value. Vernon finds it limiting enough to "[deserve] general avoidance" (raw
L6250) because: it still requires a join; if the collection is a `Set`, **no attribute may be `null`**
(all attributes form the composite key used to delete an element); and the mapped Value type **may not
itself contain a collection** (raw L6242). He prefers Strategy 3's hidden surrogate key.

## Enum Standard Types

Enum [[standard-type]]s (e.g. `GroupMemberType`) need a custom user type to persist their text
representation — the underlying column just holds `GROUP`/`USER` as a small `VARCHAR` (raw L6305).

## Guiding principle

Choose the mapping that keeps the domain model clean: prefer denormalization; when the impedance
mismatch forces a Value to be stored as a database entity, hide the surrogate identity so "even
developers in the model must look hard to detect any notion of persistence leakage" (raw L6238). See
[[data-model-leakage]] for the mindset this protects.

## Related

- [[value-object]] — the building block being persisted.
- [[data-model-leakage]] — the anti-pattern these techniques must not trigger.
- [[aggregate]] — Values are persisted with their owning Aggregate.
- [[surrogate-identity]] — the hidden-surrogate-key technique reused here.
- [[standard-type]] — enum persistence via a custom user type.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
