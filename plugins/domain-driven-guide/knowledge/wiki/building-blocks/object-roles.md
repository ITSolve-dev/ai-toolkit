---
title: Object Roles
category: building-blocks
summary: Modeling an entity so it presents different faces per client or use case via interfaces — with the object-schizophrenia hazard and fine-grained role interfaces as the safer path.
tags: [technique, tactical-pattern, entity, roles, interfaces, object-schizophrenia, failure-mode]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

**Object roles** let a single [[entity]] present different faces to different clients or use cases,
typically via interfaces. (This is distinct from a security `Role`, which in the Identity & Access
Context is itself an Entity and [[aggregate]] root — raw L4608.)

> "In object-oriented programming, generally interfaces determine the roles of an implementing class…
> a class has one role for each interface that it implements." (raw L4612)

## Blending roles onto one object

You *can* make one object play `User` and `Person` (class `HumanUser implements User, Person`) when
objects show overlapping characteristics (raw L4616). But blending complex interfaces is hard, and a
`User` might instead be a system — pushing toward a general `Principal` and runtime type resolution /
late binding (raw L4632).

### Failure mode: object schizophrenia

A forwarding/delegation design (a `UserPrincipal` dispatching to `personPrincipal`/`systemPrincipal`)
suffers **object schizophrenia**:

> "…the situation where the objects delegated to don't know the identity of their originating object.
> There is confusion inside the delegates as to who they really are." (raw L4690)

Passing the originating identity into the delegate forces the `Principal` interface to change —
undesirable. As [Gamma et al.] warn, "Delegation is a good design choice only when it simplifies more
than it complicates." (raw L4690)

## Fine-grained role interfaces

Udi Dahan's approach [Dahan, Roles]: many small single-operation interfaces, e.g.
`IAddOrdersToCustomer` and `IMakeCustomerPreferred`, each implemented **by `Customer` itself** (raw
L4694). Advantages:

- The Entity's role **changes per use case** (raw L4710).
- **Specialized fetching strategies** — the persistence layer keys off the requested interface type `T`
  in `session.Get<T>(id)` to load the Entity in exactly the shape the use case needs, falling back to a
  default strategy otherwise (raw L4710).
- Behind-the-scenes **hooks** (e.g. a use-case-specific validator run as the Entity is persisted) can
  attach to a role (raw L4726).
- Implementing on the Entity itself **avoids object schizophrenia** — no delegation to separate classes
  (raw L4728).

## Simplest practical use

The most practical use is also the simplest: an interface to **hide implementation detail** from
clients — expose exactly what clients may use and nothing more, even when a tool or framework forces
ugly public methods onto the implementation class (raw L4736). Whatever the choice, "ensure that the
Ubiquitous Language holds sway over any technical preferences" (raw L4738) — see [[ubiquitous-language]].

## Related

- [[entity]] — the object that plays roles.
- [[aggregate]] — a security `Role` is itself an Aggregate root, not an object role.
- [[ubiquitous-language]] — must govern role/interface naming over technical convenience.
- [[value-object]] — the identity-free counterpart building block.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
