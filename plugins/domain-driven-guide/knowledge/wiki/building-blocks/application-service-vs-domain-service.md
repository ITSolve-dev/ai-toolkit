---
title: Application Service vs Domain Service
category: building-blocks
summary: The stark distinction between a thin application-layer coordinator (transactions, security, task orchestration) and a domain-layer service that holds significant business logic — and how to tell where a piece of logic belongs.
tags: [guidance, application-service, domain-service, layering, anti-pattern, leaking-domain-logic]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

One of the most common confusions in a DDD codebase is treating an [[application-service|Application Service]] and a [[domain-service|Domain Service]] as the same kind of thing. They are not. "It is a mistake to consider Application Services to be the same as **Domain Services**. They are not. The contrast should be stark" (raw L13828).

## The distinction

| | Application Service | Domain Service |
|---|---|---|
| Layer | Application layer | Domain model |
| Contains business logic? | No — thin coordinator | Yes — "significant process... in the domain" [Evans] |
| Responsibilities | Task coordination of one use-case flow per method, transaction control, security authorization | Domain behavior that doesn't naturally belong to a single [[entity|Entity]] or [[value-object|Value Object]] |
| Depends on | Repositories, Domain Services, Aggregates | Aggregates, Value Objects, Repositories, other Domain Services |

The rule of thumb: "*Keep Application Services thin, using them only to coordinate tasks on the model*" and "push all business domain logic into the domain model, whether that be in Aggregates, Value Objects, or Domain Services" (raw L13828).

## The worked example that makes it concrete

Provisioning a tenant is the book's demonstration. The Application Service `provisionTenant()` delegates to a domain `TenantProvisioningService`, which performs (raw L14028-14032):

1. Instantiate a new `Tenant` [[aggregate|Aggregate]] and add it to its [[repository|Repository]].
2. Assign a new administrator — provisioning the Administrator role and publishing the [[domain-event|Domain Event]] `TenantAdministratorRegistered`.
3. Publish the Domain Event `TenantProvisioned`.

Steps 2 and 3 are domain behavior. If the Application Service did them itself, "we would be seriously leaking domain logic out of the model" (raw L14034). By placing all three in the Domain Service, the code "place[s] this 'significant process... in the domain' [Evans]" while the Application Service "properly follow[s] the definition of Application Service by managing the transaction, security, and the task of delegating" (raw L14034).

## The failure mode

The symptom of getting this wrong is a **fat Application Service** with several lines of orchestration, conditionals, and rule checks — which produces an [[anemic-domain-model|Anemic Domain Model]] underneath (aggregates that are bags of getters/setters). The test: if a method on the Application Service does more than *retrieve → delegate → commit*, ask whether the extra steps are domain process that belong in a Domain Service or Aggregate.

## Related

[[application-service]] · [[domain-service]] · [[aggregate]] · [[anemic-domain-model]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
