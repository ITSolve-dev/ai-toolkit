---
title: "Validation: syntax, semantics, and pragmatics"
category: design-principles
summary: Where validation belongs in a DDD/layered system — split preconditions into syntax, semantics, and pragmatics; validate structure and meaning at the edge to keep the domain model clean, and let the domain model own pragmatic (business-rule) validation.
tags: [guideline, validation, domain-model, preconditions, service-layer, business-rules, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Validation: syntax, semantics, and pragmatics

**Validation** establishes *preconditions* on the inputs to an operation: inputs that meet the criteria are *valid* and the operation proceeds; inputs that don't are *invalid* and the operation exits with an error (raw L7749). The recurring architectural question — "does validation belong with my business logic in the [[domain-model]], or is it an infrastructural concern?" — has no single answer; the useful move is to split validation into three subtypes and place each where it keeps the domain model simple and uncluttered.

## Three subtypes of validation

Borrowed from linguistics:

- **Syntax** — the structure and shape of a message. Examples: an `Allocate` command must have an order ID, a SKU, and a quantity; a quantity is a positive integer; a SKU is a string. These are validated *at the edge of the system*. Rule of thumb: "a message handler should always receive only a message that is well-formed and contains all required information" (raw L7779).
- **Semantics** — the *meaning* of a message. A message can be perfectly well-formed yet nonsense (e.g. `{"orderid": "superman", "sku": "zygote", "qty": -1}`). Semantic concerns are validated at the message-handler / service layer with contract-based preconditions — e.g. a `product_exists` precondition that raises `ProductNotFound` if the SKU is unknown — keeping the service-layer flow "clean and declarative" (raw L7986).
- **Pragmatics** — understanding the message *in context*, i.e. the actual business rules. "allocate three million units of `SCARCE-CLOCK`" is syntactically and semantically valid but cannot be complied with because the stock isn't available (raw L8044). Pragmatics is managed by the domain model.

## Validate at the edge; keep the domain model clean

The guiding principle is to keep invalid data out of the interior of the system: "we don't want to code defensively inside our domain model. Instead, we want to make sure that requests are known to be valid before our domain model or use-case handlers see them" (raw L7883). This is *validating at the edge of the system*, and it keeps the domain model free of endless checks and asserts. The motivation is concrete: "invalid data wandering through your system is a time bomb; the deeper it gets, the more damage it can do, and the fewer tools you have to respond to it" (raw L7889).

Validation is a natural cross-cutting concern for the [[message-bus]] and entrypoints: entrypoints care only about getting a message in and reporting success/failure, the bus validates and routes, and handlers focus purely on use-case logic.

## Pragmatics is the domain's job

Once syntax and semantics are checked at the edges, "the domain is the place for the rest of your validation. Validation of pragmatics is often a core part of your business rules" (raw L8042). The load-bearing heuristic for *where a check lives* is:

> if a rule *can* be tested inside our domain model, then it *should* be tested in the domain model. (raw L8031)

Two counter-cautions:

- Don't push *all* business logic out into edge/precondition checks — that hollows out the model (a slide toward the [[anemic-domain-model]]) and puts rules where they can't be unit-tested against the model.
- Precondition checks that touch state (e.g. a `batch_is_new` idempotency check) must use the *same* [[unit-of-work|Unit of Work]] as the main use-case logic, "otherwise, we open ourselves to irritating concurrency bugs" (raw L8028).

## Failure modes

- **Defensive clutter in the domain model:** structural/type checks that belong at the edge leak inward, obscuring the business rules the model is supposed to express.
- **The mirror image:** real business rules (pragmatics) implemented as shallow edge or precondition checks instead of in the model — losing testability and cohesion, and quietly draining the model toward anemia.

## Related

- [[tolerant-reader]] — the edge-side integration stance that decides *how much* to validate incoming messages from other systems.
- [[domain-service]] — where cross-entity business operations (pragmatic rules) live.
- [[anemic-domain-model]] — the failure mode of a rule-less model.
- [[message-bus]] · [[unit-of-work]] — the seams where edge validation and stateful preconditions sit.
