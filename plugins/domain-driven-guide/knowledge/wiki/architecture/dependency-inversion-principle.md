---
title: Dependency Inversion Principle (DIP) in a DDD stack
category: architecture
summary: Invert the Layers dependency so Infrastructure depends on abstractions defined by the Domain; Repository/Domain Service interfaces live in the domain model and their technical implementations live in Infrastructure, resolved via Dependency Injection.
tags: [principle, architecture, DIP, layers, dependency-injection, cosmic-python]
sources: [book-implementing-ddd-vaughn-vernon, web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

The **Dependency Inversion Principle (DIP)**, from Robert C. Martin, repairs the awkward dependency in a
plain [[layered-architecture]] where Infrastructure sits at the bottom yet must implement interfaces the
Domain owns. Its formal statement, as quoted: "High-level modules should not depend on low-level
modules. Both should depend on abstractions. Abstractions should not depend upon details. Details should
depend upon abstractions" (raw L3010).

## What it changes for DDD

Applied here, a low-level services component (Infrastructure) depends on interfaces defined by the
high-level components (UI, Application, Domain). Practically, Infrastructure is lifted *above* the other
layers so it can implement interfaces for all layers below it. A **Repository** interface such as
`BacklogItemRepository` is declared in the domain model, and its implementation
`HibernateBacklogItemRepository` lives in `...infrastructure.persistence` and implements that
domain-defined interface (raw L3031). Both Domain and Infrastructure now depend only on abstractions
defined by the domain model. The [[application-service|Application Layer]], as the domain's direct
client, depends on Domain interfaces and *indirectly* uses the Repository and technical **Domain
Service** implementations that Infrastructure supplies.

## Acquiring the implementations

Implementations are wired in via **Dependency Injection**, a **Service Factory**, or a **Plug In**.
Vernon's examples use Spring-provided Dependency Injection and sometimes a `DomainRegistry` service
factory that "uses Spring to look up references to beans that implement interfaces defined by the domain
model, including Repositories and Domain Services" (raw L3053). The core domain objects themselves never
couple to Infrastructure.

## Trade-offs and consequence

The payoff is testability and deferred decisions: teams can "stub out the UI and Infrastructure Layers
and concentrate on testing the Application and Domain" (raw L2849) and delay the persistence-technology
choice by developing against in-memory implementations behind Repository interfaces. Taken to its
conclusion, DIP blurs the layering entirely — "we might conclude that there are actually no longer any
layers at all" (raw L3055) — which is exactly the observation that motivates the symmetric
[[hexagonal-architecture]] (Ports and Adapters).

## The Cosmic Python view — the principle behind domain-model purity

*Architecture Patterns with Python* treats DIP as the single principle it uses to "systematically [turn]
the three-layered architecture inside out," and says "the whole of [part 1] is essentially a worked
example of implementing the DIP throughout an application" (raw L398, L405). It quotes the formal
statement in two halves: "High-level modules should not depend on low-level modules. Both should depend
on abstractions" (raw L412); "Abstractions should not depend on details. Instead, details should depend
on abstractions" (raw L414).

Its distinctive contribution is drawing the high/low distinction in *business*, not technical, terms:

- **High-level modules** are "the code that your organization really cares about" — the functions,
  classes, and packages dealing with real-world concepts (patients and trials, trades and exchanges)
  (raw L418). These are the [[domain-model]].
- **Low-level modules** are "the code that your organization doesn't care about" — filesystems, sockets,
  SMTP/HTTP/AMQP; stakeholders care "whether the high-level concepts work correctly," not "whether that's
  a cron job or a transient function running on Kubernetes" (raw L425).

Two clarifications keep the principle from being read too narrowly: "depends on" is broader than imports
or calls — "a more general idea that one module *knows about* or *needs* another module" (raw L433) — and
an *abstraction* is "a simplified interface that encapsulates behavior" (raw L436), the "famous extra
layer of indirection" (raw L454).

**Why — independent rates of change.** The justification is that domain and infrastructure change for
different reasons and at different costs, and neither should hold the other hostage: "High-level modules
should be easy to change in response to business needs. Low-level modules (details) are often, in
practice, harder to change" (raw L445) — renaming a function is cheap, while changing a database column
means "defining, testing, and deploying a database migration" (raw L448). You still want to be "*able* to
change your infrastructure details when you need to... without needing to make changes to your business
layer" (raw L451). The genuinely hard half is "details should depend on abstractions," which the book
concedes "is hard to imagine" (raw L459) and motivates through the concrete [[repository]]/service-layer
worked example rather than abstractly. Skip the indirection and dependencies drift "out of control" —
the [[big-ball-of-mud]].

### Ch. 13 — explicit dependencies and the Composition Root

The later "Dependency Injection (and Bootstrapping)" chapter turns DIP into a coding stance: **declare a
handler's collaborators as explicit arguments typed to abstractions, rather than reaching for them by
import.** "declaring an explicit dependency is an example of the dependency inversion principle—rather
than having an (implicit) dependency on a *specific* detail, we have an (explicit) dependency on an
*abstraction*" (raw L6003), because "Explicit is better than implicit" (raw L6007). An out-of-stock
handler that hardcodes `from allocation.adapters import email` becomes one that takes `send_mail:
Callable` (a simple port — see [[ports-and-adapters]]) handed in from outside.

The alternative it rejects is the idiomatic Python shortcut of importing a dependency implicitly and
`mock.patch`-ing it in tests, whose two failure modes the book names: **mock boilerplate everywhere**
(you "end up having to call `mock.patch` for *every single test*", raw L5990) and **coupling to import
mechanics** (monkeypatching `email.send_mail` ties you to `import email`; a trivial refactor to `from
email import send_mail` breaks every mock, raw L5996). The cost is stated honestly: explicit dependencies
are "unnecessary, strictly speaking, and using them would make our application code marginally more
complex. But in return, we'd get tests that are easier to write and manage." (raw L6001)

Once dependencies are declared abstractly, something must supply the concrete versions, "as early as
possible in the process lifecycle" (raw L6027). Doing it in every entrypoint duplicates cruft, and loading
it onto the [[message-bus]] "already has a job to do; it feels like a violation of the SRP" (raw L6027).
The solution is a single wiring place — a **Composition Root** ("a bootstrap script to you and me")
doing "a bit of 'manual DI' (dependency injection without a framework)" (raw L6029). The bootstrap script
declares default (production) dependencies but allows overriding them, does one-time init (e.g.
`orm.start_mappers()`), injects dependencies into handlers, and returns the ready-to-use bus (raw
L6142) — so a test calls the same bootstrap with fakes swapped in, sharing one wiring path with
production. A dedicated DI *framework* only earns its keep "if you find yourself needing to do DI at
multiple levels—if you have chained dependencies of components that all need DI" (raw L6507); manual DI
is otherwise enough.

## Related

- [[layered-architecture]] — the structure DIP repairs.
- [[hexagonal-architecture]] — the style DIP's conclusion leads to.
- [[ports-and-adapters]] — DIP as a per-dependency implementation technique (ports, adapters, fakes).
- [[application-service]] — the domain's direct client that depends on Domain interfaces.
- [[architecture-selection]] — introduced when a concrete testability/coupling risk appears.
- [[domain-model]] — the "high-level modules" DIP protects.
- [[repository]] — the canonical abstraction that lets details depend on the domain.
- [[big-ball-of-mud]] — the uncontrolled-dependency failure DIP prevents.
- [[book-implementing-ddd-vaughn-vernon]], [[web-page-cosmic-python-book]] — source summaries.
