---
title: Value Objects in Event and Command Contracts
category: event-design
summary: Using Value Objects (typed identifiers, cohesive composites) inside event and command contracts buys type safety, expressiveness, and invariant enforcement — but sharing those VOs across contexts forces a Shared Kernel vs Published Language trade-off.
tags: [guideline, value-object, event-design, domain-event, command, shared-kernel, published-language]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

## Why Value Objects in contracts

[[value-object|Value Objects]] "compose cohesive primitive types into an explicitly named immutable type" (raw L15626), and [[event-sourcing|A+ES]] event/command contracts benefit from them in three concrete ways.

**Typed identifiers over primitives.** Instead of a project identity being a bare `long`, model an explicit `ProjectId` VO. "We still use a `long` type to hold the actual identity number, but we use the `ProjectId` type to distinguish it from all others" (raw L15644).

**Static type safety.** A flat event constructor taking two `long`s lets a developer silently swap `customerId` and `projectId` — "an error that would not be caught by the compiler but might be found only through much debugging and frustration" (raw L15656). With `CustomerId` and `ProjectId` VOs, the compiler and IDE catch the mis-ordering immediately.

**Cohesion and invariant enforcement.** A `CustomerInvoiceWritten` event with a dozen flat fields is hard to work with; refactoring into `InvoiceHeader`, `InvoiceFooter`, and a `CurrencyAmount` VO makes it explicit and readable. The `CurrencyAmount` "could be enhanced with sanity check logic that prevents operations between amounts expressed in different currencies" (raw L15722) — the VO enforces its own invariants inside the contract. Guidance: "Wherever possible we should strive to employ Value Objects, whether for Command objects, Events, or Aggregate parts" (raw L15724).

## The deployment trade-off (strategic)

Here is the DDD tension. "Using Value Objects in Commands and/or Events would require deploying them together, or even creating a **Shared Kernel**" (raw L15726). For deeply complex domains, forcing a heavyweight [[core-domain|Core Domain]] VO into a [[shared-kernel|Shared Kernel]] purely so subscribers can deserialize it "would likely result in a brittle design" (raw L15726) — the shared kernel becomes a coupling liability for the wrong reason.

Two escape routes:

1. **Two sets of VO classes** — simple ones used only for type-safe deserialization of command/event data, and richer ones needed by the [[core-domain|Core Domain]], converting between them as needed (raw L15726). Cost: duplicated classes, potential accidental complexity.
2. **[[published-language|Published Language]]** — "standardize serialized Events as a Published Language" and consume notifications via dynamic typing, which "would eliminate the need for Event and Value Object types being deployed to the consuming subscribers" (raw L15728). Cost: you give up static typing on the consumer side.

"As with all approaches, this one has trade-offs that must be weighed" (raw L15728). The choice hinges on how many [[bounded-context|Bounded Contexts]] consume the events and how much you value compile-time safety versus deployment independence.

## Related

[[value-object]] · [[shared-kernel]] · [[published-language]] · [[core-domain]] · [[domain-event]] · [[domain-event-contract-design]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
