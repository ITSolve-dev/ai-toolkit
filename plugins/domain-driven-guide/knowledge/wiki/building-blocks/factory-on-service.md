---
title: Factory on Service (Service-Based Factory)
category: building-blocks
summary: A Service designed as a Factory that produces local Aggregates or Value Objects, used when integrating Bounded Contexts to translate foreign objects into local model types.
tags: [pattern, factory, domain-service, bounded-context, anticorruption-layer, context-mapping, translation]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

A [[domain-service|Service]] can be designed as a [[factory|Factory]]. Vernon reaches for this form chiefly when **integrating [[bounded-context|Bounded Contexts]]**: a Service that talks to a foreign context and returns freshly created local objects is, by definition, functioning as a Factory. The construction it performs is genuinely complex — it involves a remote call and a translation — which is exactly the situation Factories exist for.

## The example: CollaboratorService

The Collaboration Context needs to refer to people, but it does not speak of *users*. In its Ubiquitous Language, humans are **authors, creators, moderators, owners, and participants**. Those concepts live in a different context (Identity and Access), which only knows users and roles. The `CollaboratorService` bridges the two by producing `Collaborator` instances from a tenant and a user identity:

```java
public interface CollaboratorService {
    public Author authorFrom(Tenant aTenant, String anIdentity);
    public Creator creatorFrom(Tenant aTenant, String anIdentity);
    public Moderator moderatorFrom(Tenant aTenant, String anIdentity);
    public Owner ownerFrom(Tenant aTenant, String anIdentity);
    public Participant participantFrom(Tenant aTenant, String anIdentity);
}
```

> Since new objects that are derived from the abstract base `Collaborator` are created by the Service, it actually functions as a Factory. (raw L9879)

The produced `Collaborator` subclasses (`Author`, etc.) are simple [[value-object|Value Objects]]: an abstract `Collaborator` base holds `identity`, `name`, and `emailAddress` as plain strings, and each subclass adds only constructors, `equals()`, `hashCode()`, and `toString()`.

## Why a Service, and where it lives

The *interface* belongs to the domain model, but the *implementation* is technical, so it is housed in a [[modules|Module]] in the **Infrastructure Layer** (raw L9909). The implementation `UserRoleToCollaboratorService` collaborates with two helpers:

- **`UserInRoleAdapter`** — the [[anticorruption-layer|Adapter]] that "is responsible only for communicating with the foreign Context" (raw L9952). It calls the [[open-host-service|Open Host Service]] of the Identity and Access Context to confirm the user is actually in the named role (e.g. `"Author"`).
- **`CollaboratorTranslator`** — "responsible only for translation that results in creation" (raw L9952). It maps the [[published-language|Published Language]] response into a local `Author` Value Object.

Together these form an [[anticorruption-layer|Anti-Corruption Layer]]: the foreign model's shape and vocabulary never leak into the Collaboration Context.

## Why this matters

The payoff is conceptual and lifecycle separation between the two contexts:

> We've managed to separate the life cycles and conceptual terminologies from the two Bounded Contexts by means of a Service-Based Factory. (raw L9948)

A *user* in one context becomes an *author* or *moderator* in the other, on demand, with the correct `Tenant` carried through — and neither model has to know the other's classes. This is the Factory motivation of "encapsulate all complex assembly and does not require the client to reference the concrete classes" applied across a context boundary.

## When to use it

- You need to turn foreign objects (from another Bounded Context) into local model types, and that turning involves a remote confirmation plus translation.
- You want the creation of local types to read as domain behavior (`authorFrom(...)`) rather than as integration plumbing exposed to callers.

Much of the surrounding integration machinery (Anti-Corruption Layer, Published Language, Open Host Service) is a context-mapping concern; this page covers only the Factory aspect. See the deeper treatment under [[integrating-bounded-contexts]].

## Related

[[factory]] · [[factory-method-on-aggregate-root]] · [[domain-service]] · [[bounded-context]] · [[anticorruption-layer]] · [[published-language]] · [[open-host-service]] · [[value-object]] · [[integrating-bounded-contexts]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
