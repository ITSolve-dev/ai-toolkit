---
title: Repositories for Aggregate Type Hierarchies
category: building-blocks
summary: A small hierarchy of interchangeable (LSP) Aggregate subclasses can share one Repository whose finders return the common supertype; encoding type in identity or returning specific subclasses is a code smell — prefer a Standard Type property or role-based interfaces.
tags: [guide, repository, aggregate, inheritance, lsp, value-object, standard-type]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

When several closely related [[aggregate]] types extend a common domain-specific superclass and are meant to be used interchangeably, they can share a single [[repository]]. This page is about *that* use of inheritance — not about every Aggregate in a model extending a **Layer Supertype** for domain-wide plumbing, which is a different concern (raw L11179).

> "These kinds of hierarchies use a single Repository to store and retrieve instances of the separate types, because the client should use the instances interchangeably, and clients rarely if ever have to be aware of the specific subclass that they are dealing with at any given time, which reflects the Liskov Substitution Principle (LSP)." (raw L11181)

Example: an abstract `ServiceProvider` with concrete `WarbleServiceProvider` and `WonkleServiceProvider`, invoked generically:

```java
serviceProviderRepository.providerOf(id)
        .scheduleService(date, description);
```

## Why finders should return the supertype

The shared Repository's finders must answer the common superclass, not specific subclasses. If they returned specific types, "Clients would have to know which identities or other descriptive attributes of the Aggregates would lead to specific typed instances. Otherwise it could lead to an unmatched find or a `ClassCastException` when a matched instance of the wrong type is returned" (raw L11193).

## The code smells to avoid

1. **Type discriminator in the identity.** You could encode the subclass in the identity class and offer `warbleOf(id)` / `wonkleOf(id)` finders, but this "leads to two additional problems. The client must take on the responsibility of resolving and mapping identities to types" and couples clients to per-type operations (raw L11195). When such branching "becomes the norm rather than the exception, it indicates a code smell" (raw L11222).

2. **Splitting into per-type Repositories.** Reasonable only when there are just two or a few concrete subclasses. "When the number of concrete subclasses grows to several or many, most of which can be used completely interchangeably (LSP), it is worthwhile for them to share a common Repository" (raw L11222).

## Preferred alternatives

- **Standard Type as a property of the Aggregate** (not in the identity). A single concrete `ServiceProvider` holds a `ServiceType` and dispatches internally, so clients never see the branching:

```java
public void scheduleService(Date aDate, ServiceDescription aDescription) {
    if (type.isWarble())      this.scheduleWarbleService(aDate, aDescription);
    else if (type.isWonkle()) this.scheduleWonkleService(aDate, aDescription);
    else                      this.scheduleCommonService(aDate, aDescription);
}
```

  "Most of the time, this kind of situation can be completely avoided by designing type descriptive information as a property of the Aggregate (not in the identity)" (raw L11224). The [[standard-type|Standard Type]] is itself typically a [[value-object]]; if internal dispatch gets messy it can be modeled with the **State** pattern.

- **Role-based interfaces.** Have multiple Aggregate types implement a role interface such as `SchedulableService` (raw L11249). See [[object-roles|roles and responsibilities]].

The governing idea: "Even if inheritance is used, Aggregate polymorphic behavior can most often be carefully designed such that no special cases are surfaced to clients" (raw L11249).

## Related

[[repository]] · [[aggregate]] · [[value-object]] · [[standard-type]] · [[object-roles]] · [[entity]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
