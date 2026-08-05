---
title: Hexagonal Architecture (Ports and Adapters)
category: architecture
summary: Cockburn's symmetric style splitting a system into an outside (Adapters transforming diverse clients and output mechanisms) and an inside (the application API + domain model); the inner boundary is the use-case boundary, and it forms the foundation for other DDD-friendly architectures.
tags: [architecture-pattern, architecture, ports-and-adapters, hexagonal, application-service, testing]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

The **Hexagonal Architecture**, codified by Alistair Cockburn and also called **Ports and Adapters**, is
the style Vernon recommends as the strong foundation for DDD applications. It produces *symmetry*: "many
disparate clients [can] interact with the system on equal footing" (raw L3059). It is the natural
destination of a [[dependency-inversion-principle|DIP]]-driven [[layered-architecture]], and "many teams
that say they are using a Layers Architecture are actually using Hexagonal instead" because they use
Dependency Injection (raw L3063).

## Outside and inside

Rather than front-end vs back-end, Hexagonal sees an **outside** and an **inside**. Each hexagon side is
a **Port** (a kind of input or output channel); each client type has its own **Adapter** that transforms
the client's protocol into the application's API. Several clients may share one input Port (e.g. HTTP for
browser/REST/SOAP) while another uses a different Port (e.g. AMQP/RabbitMQ). We usually don't implement
Ports ourselves — "Think of a Port as HTTP and the Adapter as a Java Servlet or JAX-RS annotated class"
or a message listener (raw L3083); the Adapter's job is to translate incoming data into parameters for
the application API.

## The inside is the use-case boundary

Design the inside per functional requirements, not per number of clients: "The application boundary, or
inner hexagon, is also the use case (or user story) boundary" (raw L3089). The application's API is
published as a set of [[application-service|Application Services]], which — exactly as in Layers — are the
direct clients of the domain model. On the output side, **Repository** implementations are **persistence
Adapters** (relational, document store, distributed cache, in-memory), and a separate messaging Adapter
publishes [[domain-event|Domain Events]] out a different Port.

## Trade-offs / advantages

The standout benefit is **testability**: "The entire application and domain model can be designed and
tested before clients and storage mechanisms exist" (raw L3128) — exercise an Application Service with
in-memory **Repositories** long before choosing HTTP/REST or a database. When designed properly "the
hexagon inside… will not leak to the outside parts" (raw L3130), yielding a clean application boundary.
Hexagonal is also *versatile*: it underpins SOA, REST, [[event-driven-architecture]], [[cqrs]],
[[event-sourcing]], and grid computing — "The Hexagonal style forms the strong foundation for supporting
any and all of those additional architectural options" (raw L3136). Cost is mainly a mindset shift.

## Related

- [[dependency-inversion-principle]], [[layered-architecture]] — the styles Hexagonal grows out of.
- [[application-service]] — the published inner API at the use-case boundary.
- [[rest-and-ddd]] — REST as an input Adapter on a Hexagonal foundation.
- [[event-driven-architecture]], [[cqrs]], [[event-sourcing]] — options Hexagonal underpins.
- [[architecture-selection]] — why it is the recommended default foundation.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
