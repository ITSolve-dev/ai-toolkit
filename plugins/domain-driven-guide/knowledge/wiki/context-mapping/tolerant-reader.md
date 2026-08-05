---
title: Tolerant Reader
category: context-mapping
summary: An integration stance for a downstream bounded context — read only the fields you need and validate them minimally (Postel's law), so your context stays robust as upstream systems change; a lightweight alternative to sharing message schemas.
tags: [pattern, tolerant-reader, integration, postels-law, bounded-context, anticorruption-layer, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Tolerant Reader

The **Tolerant Reader** pattern is an integration stance for the *consuming* side of a message or API: "extract only the fields we care about and do minimal validation of them" (raw L7873). It lets a downstream [[bounded-context]] stay robust while the systems it integrates with evolve independently.

## Postel's law

The pattern is a corollary of *Postel's law* (the *robustness principle*): "Be liberal in what you accept, and conservative in what you emit" (raw L7838). Be strict about the messages you *send* to other systems, and as lenient as possible about the messages you *receive*. The book notes this "applies particularly well in the context of integration with our other systems."

## Concrete guidance

- **Don't over-validate identifiers you don't own.** A SKU could be format-checked (two dash-separated words, etc.), but "as the allocation system, it's *none of our business* what the format of a SKU might be. All we need is an identifier, so we can simply describe it as a string" (raw L7854). Over-validating format breaks the moment an upstream releases `COMFY-CHAISE-LONGUE` or a supplier snafu produces `CHEAP-CARPET-2`. The same holds for order numbers, phone numbers, and most strings — ignore their internal structure. This is also a modelling choice: represent such an identifier as a plain string [[value-object]], not an over-specified format.
- **Ignore fields you don't depend on.** If the procurement system adds `reason` and `email` fields to a `ChangeBatchQuantity` message, simply ignore them (e.g. `ignore_extra_keys=True`).
- **Don't share message definitions between systems.** "Resist the temptation to share message definitions between systems: instead, make it easy to define the data you depend on" (raw L7877). Sharing a schema — or a shared validation library — couples the contexts and fails the robustness test.

Tip: "Validate as little as possible. Read only the fields you need, and don't overspecify their contents. This will help your system stay robust when other systems change over time" (raw L7875).

## DDD relevance and trade-offs

Tolerant Reader is how a downstream context defends itself against upstream change *without* imposing a shared model. It is the practical counter-argument to a [[shared-kernel]] assembled out of shared message schemas: sharing definitions creates exactly the tight coupling that context mapping exists to manage. Where an [[anticorruption-layer]] translates an upstream model into your own domain terms, Tolerant Reader is the lighter-weight cousin — minimal *reading* rather than full translation — appropriate when the upstream data maps cleanly enough that only field selection is needed.

Trade-off: by validating less at the wire, you accept messages you might otherwise have rejected, deferring meaning-checks to your own handlers (semantic [[validation]]) and to the domain model. You gain resilience to upstream change at the cost of catching bad data a little later and closer to home.

## Failure mode

Developers "*love* to validate this kind of thing in their messages, and reject anything that looks like an invalid SKU" (raw L7849) — and then break when the upstream legitimately changes format. Building or sharing a strict cross-system schema library is the same mistake at a larger scale.

## Related

- [[validation]] — the syntax/semantics/pragmatics split this feeds into.
- [[bounded-context]] — the downstream context Tolerant Reader protects.
- [[anticorruption-layer]] — the heavier translation cousin.
- [[shared-kernel]] — the coupling Tolerant Reader avoids.
- [[value-object]] — model borrowed identifiers as plain-string values, not over-specified formats.
