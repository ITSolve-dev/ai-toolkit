---
title: Domain Event Contract Design
category: event-design
summary: Practices for durable event and command contracts in A+ES — make them immutable, serialize with a versioning-friendly format (tag-based like Protocol Buffers), and generate them from a compact DSL to cut friction and errors across an evolving domain model.
tags: [guideline, domain-event, event-design, event-sourcing, immutability, serialization, code-generation]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

## Immutability

Because the log is append-only, "Event Streams are considered to be immutable by nature" (raw L15607). To keep the code model consistent with that and avoid side effects, "Event contracts should be implemented as immutable" — in C#/.NET, mark fields read-only and set values only through the constructor (raw L15607). Mutable event objects invite accidental in-place edits that silently corrupt a stream that is supposed to be a permanent record. This mirrors ordinary [[value-object|Value Object]] discipline applied to events.

## Versioning-friendly serialization

Early in an [[event-sourcing|A+ES]] project the model evolves fast, so "it's wise to choose a serializer that favors versioning and renaming Events" (raw L15567). The failure mode is name-based serializers: with `DataContractSerializer` or a JSON serializer, renaming a member such as `Closed` to `ClosedUtc` "could easily break dependent consumers" or "produce buggy data" unless every consuming [[bounded-context|Bounded Context]] maps the rename (raw L15579).

**Protocol Buffers** avoids this because "it tracks contract members by integral tags, not names" (raw L15591) — properties can be renamed without breaking backward compatibility, and it produces a compact, fast binary form. Cross-platform alternatives noted: Apache Thrift, Avro, MessagePack (raw L15603). The principle generalizes beyond the specific library: bind consumers to stable tags/positions, not to field names, in any evolving event contract.

## Contract generation from a DSL

"Maintaining hundreds of Event (and Command) contracts manually is both tedious and error prone" (raw L15732). It is usually better to express contracts in a compact DSL (e.g. a `.proto`-like form such as `CustomerInvoiceWritten!(InvoiceId Id, InvoiceHeader header, ...)`) and generate the classes at build time. Benefits (raw L15776):

- Reduces development friction and enables faster modeling iterations.
- Reduces human error from manual boilerplate.
- "The compact representation allows us to keep all Event definitions on a single screen, providing a big-picture view... This can even serve as a terse glossary to the Ubiquitous Language" (raw L15780).
- Contracts can be versioned and distributed as compact definitions rather than source or binaries, aiding cross-team collaboration.

The same generation applies to command contracts. This ties event contracts directly back to the [[ubiquitous-language|Ubiquitous Language]]: the DSL becomes a readable, single-screen inventory of what happens in the domain.

## Related

[[domain-event]] · [[domain-event-enrichment]] · [[value-objects-in-contracts]] · [[value-object]] · [[ubiquitous-language]] · [[event-sourcing]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
