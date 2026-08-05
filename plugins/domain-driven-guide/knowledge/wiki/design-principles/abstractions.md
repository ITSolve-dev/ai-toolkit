---
title: Abstractions
category: design-principles
summary: A good abstraction is a simpler thing inserted between two systems that hides the messy details and reduces the kinds of dependencies the caller has on the callee — letting you change the hidden side without disturbing the caller. Its core trick is separating what you want from how it happens.
tags: [concept, abstraction, separation-of-concerns, what-vs-how, seam, design-principles, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

An **abstraction** is a deliberately simpler thing placed between two subsystems so that the caller depends on the abstraction rather than on the messy details behind it. A recurring theme of the Cosmic Python approach — and the reasoning behind DDD's [[repository]] and ports-and-adapters style — is that *simple abstractions hide messy details*, which is what lets a domain model stay clean and testable.

## What makes a good abstraction

A good abstraction reduces [[coupling-and-cohesion|coupling]] by cutting the *number of kinds* of dependencies the caller has on what it calls. Because it is simpler than the thing it hides, the caller has fewer ways to depend on it:

> The abstraction serves to protect us from change by hiding away the complex details of whatever system B does — we can change the arrows on the right without changing the ones on the left. (raw L1541..1543)

The measure of a good abstraction is therefore not "how much does it wrap" but "how few kinds of dependency does it leave exposed." The [[repository]] is the DDD example: the domain depends only on `add`/`get`, not on SQL, sessions, or connection pools.

## The core trick: separate *what* from *how*

> We're going to separate *what* we want to do from *how* to do it. (raw L1689)

In the book's file-sync example, this means having the core logic emit a *description* of the intended effects rather than performing them — a list of commands like `("COPY", src, dst)`, `("MOVE", old, new)`, `("DELETE", path)` (raw L1692..1695). The *what* (which files to copy/move/delete) is computed as plain data; the *how* (actually touching the filesystem) is applied separately.

This is the same move DDD makes repeatedly: a [[domain-event]] names *what happened* without dictating *how* handlers react; a [[command-object|command]] names *what is requested* independently of execution. Representing external effects as a data structure or small DSL is what makes the interesting logic testable and portable.

## Heuristics for finding the right abstraction

Finding the right abstraction is hard; the book offers questions to ask (raw L1940..1951):

- Can I choose a familiar data structure to represent the state of the messy system, and imagine a single function that returns that state? (In the example: a `dict` of hash → path.)
- Can I separate the *what* from the *how* — use a data structure or DSL to represent the external effects I want, independent of how I make them happen?
- **Where can I draw a line between my systems — where can I carve out a *seam* to stick the abstraction in?**
- What is a sensible way to divide things into components with different responsibilities? What implicit concepts can I make explicit?
- What are the dependencies, and what is the core business logic?

That last question — *what is the core business logic, versus everything else* — is the DDD question. Identifying it and giving it a clean abstraction over the messy parts is precisely how the domain model is kept isolated. See [[decoupling-domain-logic-from-infrastructure]].

## Trade-off

Abstractions are not free: each one is indirection to learn and maintain. The payoff is extensibility and testability.

> Designing for testability really means designing for extensibility. We trade off a little more complexity for a cleaner design that admits novel use cases. (raw L1916)

The failure mode is the opposite of too many abstractions: coupling business logic directly to low-level details. In the worked example, the difference algorithm couldn't run without `pathlib`, `shutil`, and `hashlib`, which made every test slow and unwieldy (raw L1640..1656).

## Related

- [[coupling-and-cohesion]] — why an abstraction reduces coupling.
- [[decoupling-domain-logic-from-infrastructure]] — applying the *what/how* split to the domain model.
- [[repository]] — the canonical DDD abstraction over storage.
- [[domain-event]] · [[command-object]] — model elements that name *what* independently of *how*.
- [[web-page-cosmic-python-book]] — source summary (Ch. 3, "A Brief Interlude: On Coupling and Abstractions").
