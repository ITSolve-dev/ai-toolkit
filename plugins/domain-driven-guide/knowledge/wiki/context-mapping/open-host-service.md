---
title: Open Host Service (OHS)
category: context-mapping
summary: An upstream context defines an open, well-documented protocol exposing its subsystem as a set of services that any client can integrate with.
tags: [pattern, context-mapping, integration, api, upstream-downstream, rest, open-host-service, conformist, shared-kernel, hexagonal]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

**Open Host Service (OHS)** is an upstream-side integration pattern. "Define a protocol that gives
access to your subsystem as a set of services. Open the protocol so that all who need to integrate with
you can use it." (raw L2485)

## Definition

Enhance and expand the protocol to handle new integration requirements — except when a single team has
idiosyncratic needs. In that case, "use a one-off translator to augment the protocol for that special
case so that the shared protocol can stay simple and coherent." (raw L2485–2487) The one-off-translator
rule is what keeps an OHS from being bent out of shape by every consumer. *(Definition largely quoted
from Evans, raw L2473.)*

## Implementation

OHS can be implemented as REST-based resources that client [[bounded-context]]s interact with; "we
generally think of Open Host Service as a remote procedure call (RPC) API, but it can be implemented
using message exchange." (raw L2583) In SaaSOvation the *Identity and Access Context* publishes a
`NotificationResource` — a RESTful resource exposing groups of published [[domain-event]]s, where every
event is available for consumption in order of occurrence and each client is responsible for avoiding
duplicate consumption (raw L2649).

## Relationship to other patterns

OHS is the upstream counterpart that a downstream [[anticorruption-layer]] talks to. It is "often
combined with" [[published-language]] — the OHS defines the *access protocol*, the Published Language
defines the *shared vocabulary* of the representations exchanged over it (raw L2491, L2581). On a
[[context-map]] it is abbreviated **OHS**.

## REST as an Open Host Service (Ch. 13)

When a context provides a rich set of RESTful resources through URIs, it is a kind of Open Host Service.
The HTTP methods `GET`, `PUT`, `POST`, `DELETE` combined with the resources they operate on form the
"set of open services," and because "a virtually unlimited number of resources — each with a unique
identity through a URI — can be created," the protocol can "handle new integration requirements as
needed" (raw L11785). The exchange representations are typically a [[published-language]] (a custom
media type).

**Autonomy limitation.** OHS-over-REST does not make clients fully autonomous: "since the RESTful
service provider must be directly interacted with whenever a resource is operated on, this style does
not permit clients to be completely autonomous" (raw L11787). If the host is down during integration,
dependent contexts cannot complete their operations — unless the consumer buffers the dependency behind
timers or messaging (see [[integrating-bounded-contexts]]).

## The key failure mode: don't expose your model

The SaaSOvation *Identity and Access Context* first considered simply exposing its domain model as
linked resources — letting clients `GET` a tenant and navigate its users, groups, and roles. "It seemed
natural at first" and "would afford clients with the greatest flexibility" (raw L11809). But Vernon's
diagnosis is sharp: that is **not** an Open Host Service.

> In reality that is not an Open Host Service but depending on the size of the shared model it would
> instead be a [[shared-kernel]] or a [[conformist]]. Publishing a Shared Kernel or accepting a
> Conformist relationship puts consumers into a tightly coupled integration with the consumed domain
> model. (raw L11811)

Such relationships "should be avoided if at all possible since they tend to run counter to the most
fundamental goals of DDD."

## Design around integrator use cases

The corrective is the "enhance and expand the protocol to handle new integration requirements" clause:
"you provide only what integrators need at present, and you understand those needs only by considering a
range of use case scenarios" (raw L11813). What integrators actually wanted was not the user/role model
but a single question — *can this user play this role?* Shielding integrators from the model "would
ultimately increase their productivity and make their dependent Bounded Contexts more maintainable"
(raw L11815). The resulting resource is a single purpose-built endpoint:

```
GET /tenants/{tenantId}/users/{username}/inRole/{role}
```

A `200` with a representation means the user plays the role; a `204 No Content` means the user does not
exist or does not play that role (raw L11801).

## How it wires into the architecture

In [[hexagonal-architecture]] (Ports and Adapters), the `UserResource` class is an **Adapter** for the
RESTful HTTP port. It delegates to `AccessService`, an [[application-service]] at the inner hexagon that
manages the use-case task and transaction. `AccessService` uses the [[repository|repositories]] to find
the `User` and `Role` [[aggregate]]s and calls `role.isInRole(user, groupMemberService)` — where
`GroupMemberService` is a [[domain-service]] that performs checks the `Role` itself should not own
(raw L11897). The response is rendered with a custom media type ([[published-language]]).

## Trade-offs

OHS trades bespoke point-to-point integrations for one open, reusable protocol: instead of custom
building a channel per consumer, you publish once and let all clients use it. The cost is the discipline
of protocol governance — keeping the shared protocol simple and coherent as new consumers arrive,
deflecting idiosyncratic demands into one-off translators rather than the shared surface. The Ch. 13
gain/give-up framing: you gain an open, versionable, extensible integration surface with the domain
model kept hidden and free to change; you give up full consumer autonomy (the provider must be
reachable) and the temptation-free flexibility of just handing over the model. Consumed via an
[[anticorruption-layer]] on the client side.

## Related

- [[published-language]] — the shared vocabulary usually paired with OHS.
- [[anticorruption-layer]] — the downstream consumer of an OHS.
- [[upstream-downstream]] — OHS is the upstream side of the relationship.
- [[conformist]], [[shared-kernel]] — the tightly-coupled relationships that exposing your model would degrade into.
- [[integrating-bounded-contexts]] — the broader set of integration styles OHS-over-REST belongs to.
- [[hexagonal-architecture]], [[application-service]], [[domain-service]] — how the RESTful OHS wires into the stack.
- [[context-map]] — where it is labelled OHS.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
