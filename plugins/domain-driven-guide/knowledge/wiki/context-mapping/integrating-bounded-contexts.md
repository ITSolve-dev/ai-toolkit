---
title: Integrating Bounded Contexts
category: context-mapping
summary: The concrete, code-level form of a Context Map — the three ways two Bounded Contexts integrate (RPC, messaging, RESTful HTTP), why messaging and REST are preferred over RPC, and how the Principles of Distributed Computing force integration toward autonomy.
tags: [concept, context-mapping, integration, bounded-context, messaging, rest, autonomy, distributed-systems]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

Every project of significance has multiple [[bounded-context]]s, and two or more of them will need to integrate. A [[context-map]] has two forms: a drawing that shows the relationships, and — the concrete one — *the code that actually implements them*. Integration is that second form. As Vernon puts it, "The second and far more concrete form is the code that actually implements those relationships." (raw L11527)

## The three straightforward ways to integrate

1. **RPC over an API.** One context exposes an API (SOAP, XML-over-HTTP, or similar) and another calls it via remote procedure calls. "This is one of the more popular ways to integrate, and since it supports a procedure call style, it is easily understood by programmers" (raw L11545). Familiar, but the most coupling and the least resilient.
2. **Messaging.** Systems interact through a message queue or a Publish-Subscribe mechanism; these gateways are effectively a service interface. A large body of technique exists here (Hohpe & Woolf). See [[event-driven-integration]].
3. **RESTful HTTP.** Not RPC: rather than calling parameterized procedures, systems exchange and modify resources identified by URIs using `GET`, `PUT`, `POST`, `DELETE`. With a little imagination these four express explicit intent — `GET` categorizes query operations, `PUT` can "encapsulate a command operation that executes on an [[aggregate]]" (raw L11549). See [[open-host-service]].

File-based and shared-database integration also exist, but doing so "could make you old before your time" (raw L11551).

## Why not RPC

The book focuses on **messaging** and **REST** and deliberately avoids RPC examples. The reason is resilience: "RPC has less resilience when our goal is to support autonomous services... A failed system that would normally provide an RPC-based API will prevent dependent systems from succeeding in their own operations." (raw L11559)

## Distributed systems are fundamentally different

Most integration trouble comes from developers who "gloss over its inherent complexity" — especially with RPC, because the inexperienced "imagine that any one remote call is as good as an in-process call" (raw L11565). That assumption causes **cascading failure** when a single component becomes even temporarily unavailable. Vernon restates the classic *Fallacies of Distributed Computing* as **Principles of Distributed Computing** — challenges to plan around, not just mistakes to avoid (raw L11567):

- The network is not reliable.
- There is always some latency, and maybe a lot.
- Bandwidth is not infinite.
- Do not assume that the network is secure.
- Network topology changes.
- Knowledge and policies are spread across multiple administrators.
- Network transport has cost.
- The network is heterogeneous.

## Achieving autonomy despite synchronous dependencies

Even a REST- or RPC-only dependency need not destroy a consumer's autonomy. You can "create the illusion of temporal decoupling by using timers or messaging in your own system" — reaching out to the remote system only when a timer elapses or a message is received (raw L11789). If the remote is down, the timer backs off or the message is negatively acknowledged and redelivered. This shifts burden onto your team to keep systems loosely coupled, "but that's a price you may have to pay to achieve autonomy." See [[bounded-context-autonomy]].

## Trade-offs

- **RPC:** easiest mental model; worst coupling and resilience.
- **Messaging:** best for autonomous services; most decoupled in time; more moving parts.
- **REST:** versatile and open (an [[open-host-service]]), but the provider must be reachable at operation time unless you buffer it behind timers/messaging.

## Failure modes

- Treating a remote call as an in-process call → cascading failure across many systems.
- Choosing RPC for convenience and inheriting a tightly coupled, fragile topology.
- Ignoring "network transport has cost" when picking verbose exchange formats — see [[published-language]].

## Related

[[open-host-service]] · [[published-language]] · [[anticorruption-layer]] · [[event-driven-integration]] · [[context-map]] · [[bounded-context]] · [[bounded-context-autonomy]] · [[domain-event]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
