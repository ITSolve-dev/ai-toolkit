---
title: Published Language (PL)
category: context-mapping
summary: A well-documented shared language used as the common medium for translating domain information between two Bounded Contexts, into and out of which each side translates.
tags: [pattern, context-mapping, integration, translation, rest, domain-event, published-language, media-type, serialization, versioning, value-object]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

**Published Language (PL)** solves the vocabulary problem of integration. "The translation between the
models of two Bounded Contexts requires a common language. Use a well-documented shared language that
can express the necessary domain information as a common medium of communication, translating as
necessary into and out of that language." (raw L2489–2491) *(Definition largely quoted from Evans, raw
L2473.)*

## Relationship to Open Host Service

"Published Language is often combined with [[open-host-service]]." (raw L2491) The OHS defines *how* you
reach the upstream subsystem (the protocol); the Published Language defines *what the exchanged
representations mean* (the shared vocabulary). On a [[context-map]] it is abbreviated **PL**, usually
paired as OHS/PL on the upstream connector.

## Implementation

A Published Language "can be implemented in a few different ways but is many times done as an XML
schema." (raw L2585) When expressed with REST-based services it is rendered as *representations of
domain concepts* — XML, JSON, Google Protocol Buffers, even HTML for published web UIs. Advantages of
the REST rendering (raw L2585):

- Each client can specify its preferred Published Language, and the resources render representations in
  the requested content type.
- Hypermedia representations enable HATEOAS, making the language dynamic and interactive so clients
  navigate to linked resources.
- The language may be published using standard and/or custom media types (SaaSOvation mints a custom
  type such as `application/vnd.saasovation.idovation+json`, raw L2660).

A Published Language is also used in an **Event-Driven Architecture**, "where [[domain-event]]s are
delivered as messages to subscribing interested parties." (raw L2585–2587) See
[[event-driven-architecture]].

## The problem it solves: exchanging information across boundaries (Ch. 13)

The Ch. 13 treatment frames the PL as a **custom media type** (or its semantic equivalent): "We can
define such a reliable contract using a standards-based approach, which actually forms a Published
Language" (raw L11601). The specification — whether or not registered per RFC 4288 — "defines the
binding contract between producers and consumers and offers a foolproof means to exchange such media
without sharing the interface and class binaries." There are three broad ways to structure data crossing
a system boundary, each with distinct coupling costs:

1. **Language serialization (binary).** Serialize objects with the language's own facilities. Works only
   if all systems share the language and compatible hardware, and "requires you to deploy all the
   interfaces and classes of objects that are used across systems to each system" (raw L11591).
2. **Intermediate format (XML, JSON, Protocol Buffers).** Standard and portable, trading off richness,
   compactness, type-conversion performance, and version flexibility (raw L11593). You *may still* deploy
   the classes and unmarshal into type-safe objects — with the same recompilation coupling, plus "the
   danger of using the foreign objects freely in the consuming system as if they were our very own,"
   which violates the DDD strategic-design principles (raw L11597). Declaring it a [[shared-kernel]] does
   not indemnify this: "the convenience of objects that are shared between systems can lead you down a
   slippery slope."
3. **Media-type contract (Published Language).** Define a contract so consumers can "confidently use the
   data without deserializing it into object instances of specific classes" (raw L11601). No shared
   binaries.

## Notifications and Events as a Published Language

SaaSOvation exchanges [[domain-event]]s wrapped in `Notification` objects over both REST and messaging.
The media-type spec fixes the standard envelope (raw L11607): `notificationId`, `typeName` (the *fully
qualified class name*, e.g. `com.saasovation.agilepm.domain.model.product.backlogItem.BacklogItemCommitted`,
so subscribers can "precisely differentiate various `Notification` types"), `version`, `occurredOn`, and
the `event` payload, followed by per-Event-type specs.

The consuming side reads attributes via a `NotificationReader` / `RepresentationReader` using XPath-like
or dot-separated navigation, as strings or primitive types. You give up (raw L11603) property-accessor
navigation and compile-time type safety, IDE code completion, and the operational methods a real Event
class would provide. Vernon argues the missing methods are "not... a disadvantage, but rather as a
protection": the consumer "should be interested only in the data properties and should never be tempted
to use functionality that is part of a different model." Any calculation should be done by the producer
and shipped as "enriching Event data attributes."

## Versioning: immutable, eternally fixed events

Because every `Notification` and Event carries a version number, "you can key off of the version to read
specialized attributes in a specific version" and consumers can also treat any Event as if it were
version 1 (raw L11747). Thoughtful Event design lets most consumers stay on version 1 and "never have to
change or be recompiled when an Event changes." Events may safely hold stable [[value-object]]s (e.g.
`BacklogItemId`, `SprintId`, `TenantId`); because those held Values are "frozen in the structure,"
Events are "not only immutable, but also eternally fixed" — new Value versions never break reading of
older `Notification`s (raw L11763). When versions change significantly and often, "Protocol Buffers can
be far easier to use."

## Trade-offs

The benefit is a stable, documented contract that decouples the two models: neither side has to know
the other's internal model, only the shared language. The cost is maintaining that language as a
first-class published artifact — versioning it, documenting its media types, and translating into and
out of it at each boundary. A downstream [[anticorruption-layer]] consumes the Published Language and
translates its representations into local domain objects (e.g. a `Moderator` [[value-object]]).

Deploying classes everywhere is "well known"; the media-type contract is "a less traveled road"
(raw L11767). The right choice can differ by project stage: sharing classes may work when starting out,
while "a more decoupled, custom media type contract" fits production (raw L11775) — though teams often
live with whatever they started with.

## Failure modes

- Sharing model classes as the interchange mechanism → recompilation coupling and a polluted consumer model.
- Rationalizing shared classes as a [[shared-kernel]] to excuse the coupling.
- Verbose formats ignoring "network transport has cost" (see [[integrating-bounded-contexts]]).

## Related

- [[open-host-service]] — the protocol PL is usually paired with (it produces the PL).
- [[anticorruption-layer]] — the downstream consumer that translates PL into local concepts.
- [[event-driven-architecture]], [[event-driven-integration]] — where PL carries domain events as messages.
- [[integrating-bounded-contexts]] — the broader integration setting; "network transport has cost" applies to PL format choice.
- [[shared-kernel]] — the coupling that sharing classes (instead of a PL contract) degrades into.
- [[domain-event]], [[value-object]] — the payloads a PL carries; Values make Events eternally fixed.
- [[context-map]] — where it is labelled PL.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
