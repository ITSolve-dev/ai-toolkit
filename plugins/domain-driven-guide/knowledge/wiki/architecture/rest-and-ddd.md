---
title: REST and DDD — never expose the domain model directly
category: architecture
summary: Directly publishing the domain model as RESTful resources makes the interface brittle; instead decouple it either via a separate interface Bounded Context whose resources are built from Core Domain Aggregates but driven by use cases, or via standard media types (a Shared Kernel / Published Language).
tags: [heuristic, decision-rule, architecture, rest, bounded-context, published-language]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

A focused DDD decision rule (contributed by Stefan Tilkov) for combining REST with a domain model: **do
not directly expose a domain model via RESTful HTTP.** "This approach often leads to system interfaces
that are more brittle than they need to be, as each change in the domain model is directly reflected in
the system interface" (raw L3228). Mapping `/:user/:task` straight to a method returning a `Task` object
means any change to `Task`'s structure immediately alters the remote interface and can break clients
"even though we might only have changed something that's entirely irrelevant to the outside world" (raw
L3234).

Two alternatives decouple the interface from the [[core-domain|Core Domain]]:

1. **A separate Bounded Context for the interface layer** (the preferred, "classic" approach). Design a
   pure domain model untainted by infrastructure, then publish a remote interface as a set of RESTful
   resources that reflect the *use cases* the client needs — "which is very likely different from the
   pure domain model." Each resource is built from one or more [[aggregate|Aggregates]] of the Core
   Domain but the interface classes are "driven by the use cases." Decoupling lets you "make changes to
   the Core Domain and then decide in each individual case whether that change must be reflected in the
   system's interface model" (raw L3236). This is a form of [[bounded-context]] separation for the
   system interface.

2. **A standard media-type approach** (preferred when reusability/standardization dominates). Develop a
   domain model for each standard media type (e.g. *ical*), reusable across clients and servers. Vernon
   notes explicitly: "Such an approach is essentially a Shared Kernel or Published Language in DDD terms"
   (raw L3238) — see [[shared-kernel]] and [[published-language]].

## Choosing

The choice "depends to a large degree on the goals of the system designer in terms of reusability. The
more specialized the solution, the more useful the first approach"; the more generally useful or
officially standardized, "the more sense it makes to go with the second, media-type-centric approach"
(raw L3242). Either way the governing principle matches [[architecture-selection]]: the transport must
not drive the shape or size of the domain model. REST typically sits on a [[hexagonal-architecture|
Hexagonal]] foundation, the RESTful resource acting as an input Adapter that delegates to an
[[application-service|Application Service]].

## Related

- [[bounded-context]] — the separate interface context of approach 1.
- [[shared-kernel]], [[published-language]] — the DDD framing of approach 2.
- [[hexagonal-architecture]], [[application-service]] — where a REST resource plugs in.
- [[architecture-selection]] — the "transport must not size the model" principle.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
