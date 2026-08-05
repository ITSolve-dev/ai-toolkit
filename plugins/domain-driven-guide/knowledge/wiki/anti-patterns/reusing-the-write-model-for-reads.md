---
title: Reusing the Write Model for Reads
category: anti-patterns
summary: Forcing read queries through the repository and domain model that were designed for writes — producing clunky helper methods, Python-side looping the database should do, and SELECT N+1 problems.
tags: [anti-pattern, read-model, repository, domain-model, select-n-plus-1, cqrs, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Reusing the Write Model for Reads (Anti-pattern)

A common instinct after investing in a rich [[domain-model]] and the [[repository]] pattern is to satisfy read/query requirements through those same abstractions — "After all the effort we put into building a nice domain model?… Isn't [the Repository] meant to be our abstraction around the database?" (raw L5580). Cosmic Python's chapter on [[cqrs]] deliberately explores this "seemingly simpler alternative" and shows it fights you, because **the write model was designed to enforce invariants, not to answer queries**.

## The symptoms

- **Grafted-on helper methods.** To answer "what's allocated for this order?" the repository needs a new `.for_order()` method, and the [[aggregate]] needs a new `.orderids` property — abstractions bent to a shape they weren't built for.
- **Work pushed into application code that belongs in the database.** The query ends up gathering `Product` aggregates, flattening their batches with a list comprehension, then filtering again in Python. The verdict: "reusing our existing repository and domain model classes is not as straightforward as you might have assumed. We've had to add new helper methods to both, and we're doing a bunch of looping and filtering in Python, which is work that would be done much more efficiently by the database." (raw L5644). "So yes, on the plus side we're reusing our existing abstractions, but on the downside, it all feels quite clunky." (raw L5646)
- **Conceptual mismatch.** The root cause: "a domain model that is designed primarily for write operations, while our requirements for reads are often conceptually quite different" (raw L5649). The write model thinks in `Batches` for one SKU; the reader wants allocations for a whole order across many SKUs.

## The ORM doesn't rescue you

Dropping to the ORM to query `Batch` objects directly looks tidier but isn't clearly better: "it took several attempts, and plenty of digging through the SQLAlchemy docs. SQL is just SQL." (raw L5682). Worse, ORMs invite the **SELECT N+1** problem — retrieving a list issues one query for the IDs and then a separate query per object, "especially likely if there are any foreign-key relationships on your objects" (raw L5690). (In fairness, the book notes SQLAlchemy avoids this well and supports explicit eager loading.)

## The correction

The symptoms are a signal that reads have outgrown the write model. The remedies, in order of commitment:

1. Apply [[command-query-separation]] — at minimum, physically separate read-only views from state-modifying handlers (a `views.py`), even without full CQRS.
2. Use hand-rolled SQL against the normal tables when the ORM/repository path is clunkier than plain SQL.
3. Build a dedicated [[read-model]] — a denormalized store kept current via [[domain-event|domain events]] — when reads act on genuinely different conceptual entities than writes.

Crucially, this is a threshold judgement, not a blanket rule: when reads act on the same conceptual objects as writes, adding read methods to your repositories and reusing domain classes is "*just fine*" (raw L5888). The anti-pattern is only reached when you keep forcing a diverging read requirement through a write-shaped model past the point where it hurts.

## Related

- [[cqrs]] — the pattern that resolves the tension.
- [[read-model]] — the dedicated read side this anti-pattern motivates.
- [[command-query-separation]] — the minimal split that helps even without full CQRS.
- [[repository]] · [[domain-model]] · [[aggregate]] — the write-side abstractions being misused.
