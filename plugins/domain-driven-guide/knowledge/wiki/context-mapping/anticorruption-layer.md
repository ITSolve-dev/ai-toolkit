---
title: Anticorruption Layer (ACL)
category: context-mapping
summary: An isolating translation layer a downstream context builds to consume an upstream system in terms of its own domain model, preventing foreign concepts from corrupting the local model.
tags: [pattern, context-mapping, integration, translation, autonomy, anticorruption-layer, adapter, separated-interface, value-object, hexagonal]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

An **Anticorruption Layer (ACL)** is the most defensive of the integration patterns: a downstream
[[bounded-context]] builds an isolating layer so it can use an upstream system "in terms of your own
domain model," without letting the upstream model leak in and corrupt it.

> "As a downstream client, create an isolating layer to provide your system with functionality of the
> upstream system in terms of your own domain model. This layer talks to the other system through its
> existing interface, requiring little or no modification to the other system. Internally, the layer
> translates in one or both directions as necessary between the two models." (raw L2483)

## When to use it

Simple translation layers suffice "when bridging well-designed Bounded Contexts with cooperative
teams." But "when control or communication is not adequate to pull off a shared kernel, partner, or
customer-supplier relationship, translation becomes more complex" and "takes on a more defensive tone"
(raw L2483). An ACL is also worthwhile even against cooperative, well-designed upstream contexts to
preserve local model purity — SaaSOvation uses ACLs downstream even while establishing open standards,
gaining isolation "with less complexity than needed when consuming a [[big-ball-of-mud]]" (raw L2501).

## Implementation

Vernon gives concrete structure (raw L2589–2591):

- A **Domain Service** is defined in the downstream context for each ACL; you may also put an ACL behind
  a **Repository** interface.
- If using REST, a client Domain Service implementation accesses a remote [[open-host-service]]. Server
  responses arrive as a [[published-language]] (e.g. XML or JSON).
- The downstream ACL **translates representations into domain objects of the local context**. Example:
  the *Collaboration Context* asks the *Identity and Access Context* for a User-in-Moderator-role
  resource, receives XML/JSON, and translates it into a `Moderator` [[value-object]] whose meaning is
  expressed in the *downstream* model, not the upstream one (raw L2591, L2611).

The **Translation Map** is the artifact that documents this: a logical map showing how a
representational state (e.g. XML) maps to a local [[value-object]] (raw L2609–2619).

A fuller ACL against the Identity and Access Context uses three collaborating roles (raw L2677–2683):

- `MemberService` — a **Domain Service** that is the *interface of the ACL*, providing
  `ProductOwner`/`TeamMember` objects; its `maintainMembers()` is invoked periodically by a
  `MemberSynchronizer` timer, not by normal clients.
- `IdentityAccessNotificationAdapter` — the **Adapter** that acts as client to the remote Open Host
  Service.
- `MemberTranslator` — translates the Published Language media into local concepts, updating the
  existing `Member` (subclasses `ProductOwner`, `TeamMember`) when it already exists.

## Worked example: Collaboration Context (Ch. 13, on-demand translation)

A second, on-demand ACL appears in Ch. 13. The *Collaboration Context* consumes the *Identity and Access
Context*'s [[open-host-service]] and translates a `user-in-role` representation into a `Collaborator`
[[value-object]]. Why translate rather than consume the JSON as-is? The collaboration team "is not
interested in primitive users and their roles" but in "domain-specific roles"; that some other model has
`User` objects assignable to a `Role` "is really not in the collaboration sweet spot" (raw L11941). The
ACL bridges that gap.

Generally an ACL has "a specialized Adapter and a translator" (raw L11998). Here three collaborators
form it (raw L11949):

- **`CollaboratorService`** — the interface expressing the ACL's operations in local terms: `authorFrom`,
  `creatorFrom`, `moderatorFrom`, `ownerFrom`, `participantFrom` (raw L11956). From its clients' viewpoint
  "the interface completely abstracts away the complexity of the remote system access and subsequent
  translations from the [[published-language|Published Language]] to objects that adhere to the local
  Ubiquitous Language" (raw L11966). Because it creates local types, it also functions as a
  [[factory-on-service|Service-based Factory]].
- **`UserInRoleAdapter`** — reaches out to the remote system, issues the `GET`, and on `200` invokes the
  translator; on `204` returns null; otherwise throws (raw L11998).
- **`CollaboratorTranslator`** — reads `username`, `firstName`, `lastName`, `emailAddress` from the
  representation via a `RepresentationReader` (relying on the media-type contract) and instantiates the
  correct `Collaborator` subclass (`Author`, `Creator`, `Moderator`, `Owner`, `Participant`) — these
  creators act as [[factory|Factories]] (raw L11968).

## Separated Interface: keep the technical part out of the domain

The ACL uses a **Separated Interface** (Fowler): the interface lives in the inner hexagon as part of the
domain model, but "the implementation is technical and should not reside in the Domain Layer"
(raw L11966). `TranslatingCollaboratorService` therefore sits in a [[modules|Module]] of the
**Infrastructure**, at the outside of the [[hexagonal-architecture]] where the Ports and Adapters live
(raw L11996).

## Immutable, unsynchronized copies

The translated `Collaborator` Values are [[value-object]]s: "There is no effort made to keep
`Collaborator` Value instances synchronized with the Identity and Access Context. They are immutable and
can only be fully replaced, not modified." (raw L12130) If a name or e-mail changes upstream, the change
is *not* propagated downstream — because "those kinds of changes rarely occur, so the team made the
decision to keep this particular design simple and not attempt to synchronize" (raw L12175). This is a
deliberate trade-off; the *Agile Project Management Context* (the kept-in-sync example above) has
different design goals — see [[duplicating-information-across-bounded-contexts]].

## Alternative implementation: via a Repository

An ACL can also be implemented as a [[repository]]. But since repositories "are typically used to persist
and reconstitute [[aggregate]]s, creating Value Objects by that means seems misplaced" — whereas "if our
goal is to produce an Aggregate from an Anticorruption Layer, a Repository may be a more natural source"
(raw L12177). So: Adapter+Translator for producing Value Objects; Repository-style ACL when the output is
an Aggregate.

## Trade-offs and failure modes

The cost of an ACL is the translation code you must build and maintain; the benefit is a local model
that stays pure. "By cleanly separating Bounded Contexts, we are able to keep each Context pure, while
applying data from other Contexts to express concepts in our own." (raw L2689)

The key failure mode is **adopting too much from the foreign model**: "What if you find the
translations overly complex, requiring a lot of data copying and synchronization, making your
translated object look a lot like the one from the other model? Perhaps you are using too much from the
foreign Bounded Context… thus causing confusing conflict in your own model." (raw L2625) A related smell
is **hybridization** — letting a `ProductOwner` and `TeamMember` become a disguised
`UserOwner`/`UserMember` because they absorbed too many traits of the remote `User` (raw L2645). The
remedy is minimalism: translate only the state the local model actually needs (see
[[bounded-context-autonomy]]).

## Related

- [[open-host-service]], [[published-language]] — the upstream protocol and vocabulary an ACL consumes.
- [[conformist]] — the opposite choice (no translation, adopt the upstream model).
- [[bounded-context-autonomy]] — the "translate only what you need" discipline.
- [[duplicating-information-across-bounded-contexts]] — the snapshot-vs-synced trade-off behind the immutable-copies decision.
- [[factory-on-service]], [[factory]] — the ACL's Adapter/Translator act as Service-based Factories producing local types.
- [[integrating-bounded-contexts]], [[hexagonal-architecture]] — the integration setting and where the technical ACL lives.
- [[value-object]] — what the Collaboration-Context ACL produces (immutable `Collaborator`).
- [[big-ball-of-mud]] — the case where an ACL is most necessary.
- [[context-map]] — where the ACL is labelled (abbreviated ACL).
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
