---
title: "Domain Service: Separated Interface, Naming & Wiring"
category: building-blocks
summary: How to structure a Domain Service's implementation — whether to split interface from implementation, where to place it, how to name it, and how to decouple clients via a Service Factory or Dependency Injection.
tags: [decision, domain-service, separated-interface, dependency-inversion, hexagonal, dependency-injection, naming, implementation]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

Once you've decided you need a [[domain-service]], a second set of decisions concerns *how to structure its implementation*: whether to split the interface from the implementation, where each part lives, what to name them, and how clients obtain an instance. This page collects those trade-offs.

## Should the Service have a Separated Interface?

You must "decide whether or not your Service should have a **Separated Interface** [Fowler, P of EAA]" (raw L6567) — a separate interface type distinct from the implementing class.

**It is not mandatory.** For a Service with no technical implementation (like `AuthenticationService`), "is it really necessary to create a Separated Interface and implementation class, and in separate Layers and Modules? No, it is not, in fact, an absolute necessity" (raw L6645). SaaSOvation kept a single class named simply `AuthenticationService`.

**When it earns its keep:** when you genuinely expect *multiple* implementations, or the implementation is *technical*. Fowler's rationale: "A client that needs the dependency to the interface can be completely unaware of the implementation" (raw L6680). Example: different tenants might want specialized security standards.

Using a Separated Interface is "more a matter of style in cases where the Service is always domain specific and will never have a technical implementation or multiple implementations" (raw L6680).

## Placement (layering)

A *technical* implementation belongs outside the domain model: "If you are using the **Dependency Inversion Principle** or **Hexagonal**, you may decide to place this somewhat technical implementation class in a location outside the domain model. Technical implementations may be housed in a Module in the Infrastructure Layer" (raw L6586). The canonical split: `EncryptionService` interface lives in the domain model, while `MD5EncryptionService` resides in infrastructure (raw L6674). A *non-technical* Domain Service (interface + class combined) is declared in the same [[modules|module]] as its related [[aggregate]]s (e.g. the `identity` module alongside `Tenant`, `User`, `Group`) (raw L6584).

## Naming: avoid the `Impl` reflex

The common Java habit of `InterfaceNameImpl` is treated as a smell: "if your implementation class is named this way, it's probably a very good indication that you don't need a Separated Interface, or that you need to think more carefully about the name of the implementing class" (raw L6668). So `AuthenticationServiceImpl` "isn't a really good one" — but the over-specific `DefaultEncryptionAuthenticationService` "is not particularly useful either" (raw L6670), which is why the team collapsed to a plain `AuthenticationService` class.

When you *do* have multiple implementations, "name the class according to its specialty. The need to name each specialized implementation carefully is proof that specialties exist in your domain" (raw L6672). Vernon acknowledges the `Impl` camp is large but insists there is "a well-informed polar opposite... that has very sound reasons for avoiding that approach" (raw L6678).

## Wiring clients without coupling them to the implementation

Even with interface and class combined, clients can stay ignorant of the concrete type via:

- **Service Factory (e.g. `DomainRegistry`):** "the following use of the `DomainRegistry` as Service Factory will decouple the client from implementation" (raw L6680). The chapter's samples use `DomainRegistry` "for clarity... *though not necessarily indicating a preference*" (raw L6709).
- **Dependency Injection** (e.g. Spring `@Autowired`): "Since the client never instantiates the Service, it isn't aware that the interface and implementation are either combined or separated" (raw L6707).
- **Constructor injection or method parameters** — "the most explicit way to wire dependencies and make code testable"; the book's distributed source leans this way (raw L6709).

## Testability is not weakened by dropping the interface

"Eliminating the Separated Interface for nontechnical Domain Services will not weaken testability since any interfaces that the Service depends on can be injected or resolved by a test-configured Service Factory, or you could pass in as parameters instances of inbound and outbound dependencies" (raw L6676). And a reminder that even simple domain calculations "must be tested for correctness" (raw L6676). See the testing notes in [[domain-service]].
