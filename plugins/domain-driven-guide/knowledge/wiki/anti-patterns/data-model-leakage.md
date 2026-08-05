---
title: Data Model Leakage (Entity-Think)
category: anti-patterns
summary: Letting the persistence/data model dictate the domain model — modeling a concept as an Entity merely because storage represents it as a row with a primary key.
tags: [anti-pattern, entity-think, persistence, data-model, value-object]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

**Data model leakage** is the anti-pattern of letting the relational/data model drive the domain model.
Its most common symptom is *entity-think*: modeling a concept as an [[entity]] — giving it identity and
a life cycle — only because the database stores it as a row with a primary key, when the concept is
really a [[value-object]].

## Origin: everything mapped to a table

Vernon's SaaSOvation teams "went overboard with their use of Entities… From project inception they
followed the popular mode of thinking that every element of their domain model needed to map to its own
database table, and that all their attributes should be easily set and retrieved through public accessor
methods. Since every object had a database primary key, the model was tightly stitched together into a
large, complex graph" (raw L5192). This came "from the data modeling perspective that most developers
have when unduly influenced by relational databases." The cost was real: "getting caught in the tide of
entity-think was not only unnecessary, it was also more costly in development time and effort" (raw
L5192). It is the sibling of the [[anemic-domain-model]] — both begin by modeling the database instead of
the domain.

## The four questions that break the leak

When the object-relational impedance mismatch forces a Value to be stored as a database entity (its own
table, its own primary key — which happens when persisting a *collection* of Values via ORM), do not
conclude the domain concept is an Entity. Keep a domain-model perspective by asking (raw L5988):

1. Is the concept a *thing*, or does it *measure, quantify, or describe* a thing as one of its
   properties?
2. If modeled correctly, must it possess all or most of the [[value-object]] characteristics?
3. Am I considering an Entity **only** because the underlying data model must store the object as a
   database entity?
4. Am I using an Entity because the domain genuinely requires unique identity, I care about individual
   instances, and I must manage continuity of change?

"If your answers are 'Describes, Yes, Yes, and No,' you should use a Value Object" (raw L5998). The
impedance mismatch "in some cases requires this approach, not a DDD principle. If there were a perfectly
matched persistence style available to you, you'd model the concept as a Value type and never give
database entity characteristics a second thought" (raw L6091).

## The governing principle: subordinate the data model

> "Design your data model for the sake of your domain model, not your domain model for the sake of your
> data model." (raw L6002)

Do the former and you keep a domain-model perspective; do the latter and "your domain model will tend to
serve merely as a projection of your data model" (raw L6004). Referential integrity, indexes, and
foreign keys are fine where needed, but "its entities, primary keys, referential integrity, and indexes
simply must not drive the way you model domain objects. DDD is not about structuring data in a
normalized fashion. It is about modeling the Ubiquitous Language in a consistent [[bounded-context]]"
(raw L6008). Reporting/BI should run against a dedicated model, not production data, freeing the backing
data model to serve the domain (raw L6006).

## Symptom and remedy

- **Symptom:** a concept has identity, a table, and a primary key, yet you never care about *which*
  instance it is, only about its attributes — and two equal-valued instances are interchangeable. That
  is a Value wearing an Entity's persistence clothing.
- **Remedy:** model it as a Value; hide the persistence surrogate identity. Vernon's `GroupMember` is
  stored as a database entity (`tbl_group_member` with an `id` primary key and a foreign key to
  `tbl_group`) yet remains a Value in the domain: "In the domain model `GroupMember` is clearly a Value
  Object. Appropriate steps have been taken… to carefully hide any persistence concerns" (raw L6238).
  See [[value-object-persistence]] for the hidden-surrogate-key technique.

## Related

- [[value-object]] — what entity-think wrongly promotes to an Entity.
- [[entity]] — the building block, legitimately used only when question 4 is 'Yes'.
- [[value-object-persistence]] — how to store Values as DB entities without leakage.
- [[surrogate-identity]] — the hidden identity that keeps persistence out of the model.
- [[anemic-domain-model]] — the sibling anti-pattern, also rooted in data-thinking.
- [[bounded-context]] — the unit whose language the model should reflect.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
