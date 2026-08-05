---
title: "Aggregate Information Hiding: Law of Demeter and Tell, Don't Ask"
category: aggregate-design
summary: Two design principles for keeping Aggregate state changes behind the Root's surface interface, so clients never reach into and mutate interior parts.
tags: [technique, aggregate, law-of-demeter, tell-dont-ask, information-hiding, implementation, aggregate-design]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

Two complementary principles govern how clients interact with an [[aggregate]]'s interior, both stressing information hiding so that only the Root mutates Aggregate state (raw L9451-9504).

## Law of Demeter

The *principle of least knowledge*: a client should know as little as possible about a server object's structure. The client may ask the server to perform a command on its surface interface, but "must not reach into the server, ask the server for some inner part, and then execute a command on the part" (raw L9455). Operationally, a method may invoke methods only on: (1) itself, (2) its parameters, (3) objects it instantiates, and (4) directly-held part objects (raw L9457). It is the more restrictive principle — it disallows *all* navigation into Aggregate parts beyond the Root.

## Tell, Don't Ask

Objects should be **told** what to do. A client must not ask a server for its inner parts, decide based on their state, and then drive the server — it should tell the server via a command on its public interface (raw L9459). Similar motivation to Law of Demeter, but "Tell, Don't Ask may be easier to apply broadly": it permits navigation past the Root for *querying*, while still insisting that *modification* of Aggregate state belongs to the Aggregate, not the client (raw L9504).

## Worked example

`Product` exposes a public `reorderFrom(BacklogItemId, int)` that iterates its `backlogItems` and delegates to each `ProductBacklogItem.reorderFrom(...)` (raw L9465-9477). `ProductBacklogItem`'s only state-modifying method is declared **protected**, so clients cannot invoke it:

```java
public class ProductBacklogItem extends ConcurrencySafeEntity {
    protected void reorderFrom(BacklogItemId anId, int anOrdering) {
        if (this.backlogItemId().equals(anId)) {
            this.setOrdering(anOrdering);
        } else if (this.ordering() >= anOrdering) {
            this.setOrdering(this.ordering() + 1);
        }
    }
}
```

`Product.backlogItems()` is still public, seemingly exposing interior parts — but clients "may use those instances only to query information from them." Because the parts' only mutator is protected, "clients cannot determine the shape of `Product` by deep navigation" and are given *least knowledge*; the returned collection "may represent no definite state of `Product`" (raw L9482). The result: `Product` "limits knowledge about itself, is more easily tested, and is more maintainable" (raw L9502).

## Choosing between them

Weigh the competing forces: Law of Demeter is more restrictive (no navigation past the Root at all); Tell, Don't Ask allows read navigation while reserving mutation to the Aggregate. "You may thus find Tell, Don't Ask to be a more broadly applicable approach to Aggregate implementation." (raw L9504)

## Related

[[aggregate]] · [[aggregate-optimistic-concurrency]] · [[reference-other-aggregates-by-identity]] · [[entity]]
