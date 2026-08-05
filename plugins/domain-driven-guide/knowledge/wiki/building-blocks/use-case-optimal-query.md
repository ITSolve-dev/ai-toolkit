---
title: Use Case Optimal Query
category: building-blocks
summary: A Repository finder that runs a complex cross-Aggregate query and projects the result into a purpose-built Value Object; when many such finders accumulate it is a code smell signaling mis-drawn Aggregate boundaries or a case for CQRS.
tags: [pattern, repository, query, value-object, aggregate, cqrs, code-smell]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

A **use case optimal query** is additional [[repository]] behavior that goes beyond finding whole Aggregates by identity: it runs a complex query directly against the persistence mechanism and places the result into a purpose-built [[value-object]] shaped to a specific use case's display or reporting needs.

> "You might instead use what is called a *use case optimal query*. This is where you specify a complex query against the persistence mechanism, dynamically placing the results into a Value Object specifically designed to address the needs of the use case." (raw L10992)

This is legitimate because a Repository answering a Value rather than an [[aggregate]] is nothing new: a `size()` method — which mimics `java.util.Collection.size()` and returns an integer count — is itself "a very simple Value in the form of an integer count of the total Aggregate instances it holds. A use case optimal query is just extending this notion a bit to provide a somewhat more complex Value" (raw L10994). Vernon prefers `size()` over `count` precisely so the Repository keeps mimicking a collection (raw L10959).

## Why it exists: cross-cutting views

Some use cases render data that "may instead cut across types, possibly composing just certain parts of one or more Aggregates" (raw L10992). Rather than load several whole Aggregates in one transaction and stitch them together in memory, the use case optimal query projects exactly the fields the view needs into one flat Value Object — a "custom object as a superset of one or more Aggregate instances" that "is then consumed directly by the view renderer" (raw L13701). It is the leanest of the read-out techniques catalogued in [[presenting-aggregate-state]], skipping the DTO-assembly step entirely.

## Why a Value Object, not a DTO — and the single-store distinction

The deliberate choice of return type: "You design a Value Object, not a DTO, because the query is domain specific, not application specific (as are DTOs)" (raw L13701). The result stays part of the domain model's vocabulary — a read-optimized [[value-object]] tuned to one use case — which keeps the [[ubiquitous-language|Ubiquitous Language]] intact on the read path.

This is what distinguishes it from full [[cqrs|CQRS]]: the motivation (view-shaped reads) is the same, but "the use case optimal query uses a Repository against the unified domain model persistence store rather than a raw database (such as SQL) query against a separate query/read store" (raw L13703). One model, one store; only the query shape is optimized. That is also why it is a slippery slope — see below.

## Querying Aggregate parts — use with caution

A related, adjacent technique is querying *parts* of an Aggregate without going through the Root — e.g. fetching only the child Entities that match a criterion out of a large collection. This is strictly bounded:

- It is only legitimate "if the Aggregate allows for such access by navigation through the Root" — otherwise it "would violate the Aggregate contract" (raw L10990).
- It is a **performance** tool, not a convenience shortcut: "I think this should be used primarily to address performance concerns under conditions where navigation through the Root would cause an unacceptable bottleneck" (raw L10990). Never design it "as a mere shortcut for client convenience."

## Failure mode: *Repository masks Aggregate mis-design*

The key heuristic. If you find yourself creating many finder methods supporting use case optimal queries across multiple Repositories, it is a code smell:

> "this situation could be an indication that you've misjudged Aggregate boundaries and overlooked the opportunity to design one or more Aggregates of different types. The code smell here might be called *Repository masks Aggregate mis-design*." (raw L10996)

The diagnostic branch:

- **If your Aggregate boundaries are actually wrong** — redraw them; the proliferation of cross-cutting finders was the symptom.
- **If analysis shows the boundaries are well designed** and you still need these views — "This could point to the need to consider using CQRS" (raw L10998). See [[cqrs]], where a separate read model serves query concerns so the write-side [[aggregate]] design stays clean.

## Related

[[repository]] · [[value-object]] · [[aggregate]] · [[cqrs]] · [[presenting-aggregate-state]] · [[application-service]]. Heavy calculation that must run in the store (stored procedures, data-grid entry processors) is often better owned by a [[domain-service]] than baked into finder methods (raw L10988). See [[book-implementing-ddd-vaughn-vernon]] — source summary.
