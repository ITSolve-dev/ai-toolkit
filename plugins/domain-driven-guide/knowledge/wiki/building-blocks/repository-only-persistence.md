---
title: Repository-Only Persistence
category: building-blocks
summary: Vernon's rule of thumb that all Aggregate persistence flows through Repositories — never through the Aggregate itself or ORM life-cycle cascades. DDD experts avoid Aggregate-managed persistence.
tags: [heuristic, repository, persistence, aggregate, orm, anti-pattern]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

**Repository-only persistence** is the design stance that *all* [[aggregate]] persistence — inserts, updates, and deletes — flows through the [[repository]], and never through the Aggregate itself or through ORM life-cycle cascades. Its opposite is **Aggregate-managed persistence**, where the Aggregate (often via ORM cascade rules or life-cycle events) drives its own saving and deletion. Vernon states the position bluntly: "I am a strong opponent of Aggregate-managed persistence, and I strongly advocate Repository-only persistence" (raw L10354). He notes the debate is "passionate and never-ending" but offers the heuristic: "understand that DDD experts avoid Aggregate-managed persistence as a rule of thumb" (raw L10354).

## Why it matters

Keeping persistence in the Repository preserves the separation the [[repository]] pattern exists to provide: the domain model stays free of storage concerns, and clients are insulated from the persistence mechanism — including its exceptions (raw L10326). Delegating to ORM cascades scatters persistence logic into mapping configuration and Aggregate internals, making the effective transactional behavior harder to see and reason about.

## Concrete consequence: manage cascades by hand

The chapter's worked example is deleting an Aggregate with a one-to-one mapping. Because such relationships can't cascade the change automatically, the Repository must **explicitly delete both sides of the association** (raw L10328):

```java
public void remove(User aUser) {
    this.session().delete(aUser.person());
    this.session().delete(aUser);
}
```

The inner `Person` must be deleted first, then the `User` Aggregate root; otherwise the `Person` "will be orphaned in its corresponding database table" (raw L10352). Vernon deliberately implemented a one-to-one bidirectional association to demonstrate this troublesome case, but the advice is to avoid it: "In general this is a good reason to avoid one-to-one associations and instead use a constrained singular many-to-one unidirectional association" (raw L10352). The alternative — depending on ORM life-cycle events for part-object cascading deletes — is exactly the Aggregate-managed approach he avoids on purpose (raw L10354).

## Trade-off

Aggregate-managed / cascade-driven persistence is less boilerplate: the ORM handles part deletes for you. Repository-only persistence trades that convenience for explicitness and control — the deletion order and the both-sides delete live in readable Repository code rather than in mapping metadata. Vernon's guidance is to make an *informed* choice, while noting the expert default lands on Repository-only (raw L10354).

## Related

[[repository]] · [[collection-oriented-repository]] · [[aggregate]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
