---
title: Collection-Oriented Repository
category: building-blocks
summary: The traditional Repository design whose public interface mimics an in-memory Set — no save() — so clients never re-save modified Aggregates. Works only when the persistence mechanism tracks changes implicitly.
tags: [pattern, repository, collection-oriented, set-semantics, change-tracking, hibernate, persistence]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

A **collection-oriented Repository** is the traditional [[repository]] design whose public interface *mimics a simple in-memory collection* and "does not hint in any way that there is an underlying persistence mechanism, avoiding any notion of saving or persisting data to a store" (raw L10002). Vernon calls it the traditional approach "because it adheres to the basic ideas presented in the original DDD pattern" (raw L10002). Its counterpart is the [[persistence-oriented-repository]], used when the store cannot support these semantics.

## It mimics a Set, not just any collection

The specific collection to imitate is `java.util.Set`: every object added must be unique, and re-adding an object already contained is a benign no-op that does not change the collection's state (raw L10034). "Whatever the backing implementation with a specific persistence mechanism, you must not allow instances of the same object to be added twice" (raw L10051). The mechanism that enforces this is the Aggregate's globally unique identity, associated with its [[aggregate]] root: "It is this unique identity that allows the `Set`-like Repository to prevent adding the same Aggregate instances more than once" (raw L10049).

## No re-save

The second defining property: "when retrieving objects from a Repository and modifying them, you don't need to 're-save' them" (raw L10059). You retrieve the reference, invoke a command method to transition its state, and the collection still holds the very same mutated object — so a `save()` method "wouldn't make any sense" and none is provided (raw L10101). This is exactly how an in-memory `HashSet` behaves; the goal is to reproduce that behavior "but with a persistent data store instead" (raw L10105).

## Hard prerequisite: implicit change tracking

This design "requires some specific capabilities of the backing persistence mechanism" — it "must in some way support the ability to implicitly track changes made to each persistent object that it manages" (raw L10107). If your mechanism can't, the collection-oriented design won't work and you fall back to a [[persistence-oriented-repository]]. Three mechanisms are described (raw L10109):

1. **Implicit Copy-on-Read** — on read, the mechanism copies the whole object; at commit it compares its private copy to the client's and flushes any object with detected changes (Hibernate-style).
2. **Implicit Copy-on-Write** — the client is handed a thin proxy; on the first method invocation the proxy copies the managed object, tracks changes, marks it dirty, and flushes dirty objects at commit.
3. **Explicit Copy-before-Write** — TopLink's Unit of Work; the client must *explicitly* tell the Unit of Work it is about to modify an object, at which point a clone ("editing copy") is made. "The key point is that TopLink consumes memory only when it must" (raw L10127).

## Trade-off: convenience versus memory/CPU

Implicit copy-on-read/write buys transparent change tracking "requiring no explicit client knowledge or intervention" (raw L10115), which is what *allows* a collection-oriented Repository over a mechanism like Hibernate. But it is not free: "If your requirements demand a very high-performance domain with many, many objects in memory at any given time, this sort of mechanism is going to add gratuitous overhead, in both memory and execution" (raw L10117). Vernon is explicit that this is a trade-off to measure, not a taboo — "The use of any tool should be with full awareness of trade-offs." A domain that suffers this overhead is a reason to reach for an explicit-copy tool (TopLink/EclipseLink) or a [[persistence-oriented-repository]].

## Hibernate implementation notes

`add()`/`addAll()` delegate to Hibernate's `Session.saveOrUpdate()` — chosen precisely for `Set`-like semantics: re-adding the same `CalendarEntry` "makes it appear as a benign no-op" (raw L10324). Since Hibernate 3, updates are themselves no-ops because state modifications are tracked implicitly, so unless the objects are entirely new these methods do nothing. `remove()`/`removeAll()` use `Session.delete()`. Persistence exceptions are wrapped so clients stay insulated — e.g. a `ConstraintViolationException` on add is caught and rethrown as a client-friendly `IllegalStateException` (or a domain-specific exception): "since we are going to the trouble of abstracting away the implementation details ... we want to insulate clients from all such details, including exceptions" (raw L10326).

## TopLink implementation notes

TopLink separates Session from Unit of Work (Hibernate's Session is also its Unit of Work). New objects use `unitOfWork.registerNewObject()`, which *fails* if the instance is actually preexisting; the vanilla `registerObject()` behaves like `saveOrUpdate()` (raw L10464). To modify a preexisting Aggregate you must obtain its clone from a Unit of Work without leaking a persistence mindset into the interface. Two options preserve the collection illusion (raw L10480): `editingCopy(aCalendar)` returns a registered clone to edit, or `useEditingMode()` puts the whole Repository into a mode where subsequent finders auto-register queried objects and return clones. The latter "locks the Repository into use for Aggregate modifications" — which mirrors how Repositories tend to be used anyway: read-only or read-for-modification, reflecting Aggregates with "well-crafted boundaries that reflect a bias toward transactional success" (raw L10510).

## Failure modes

- **Choosing collection-oriented over a store that can't track changes implicitly** — silent lost updates, because there is no `save()` to catch the change; the symptom is mutated Aggregates not persisting.
- **Adopting implicit copy-on-read in a high-object-count, high-performance domain** — gratuitous memory/CPU overhead (raw L10117).
- **Adding an already-persisted Aggregate expecting it to "save" changes** — a no-op; re-adds are benign by design, they do not flush edits.

## Related

[[repository]] · [[persistence-oriented-repository]] · [[repository-only-persistence]] · [[aggregate]] · [[entity]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
