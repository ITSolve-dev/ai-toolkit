---
title: Command Object (application input)
category: building-blocks
summary: A named object that encapsulates a request to an Application Service — taming long parameter lists, carrying only basic types, and optionally being queued to a temporally decoupled Command Handler.
tags: [pattern, command, application-service, command-handler, cqrs, input]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

A **Command object** encapsulates a request to the domain as an object, passed into an [[application-service|Application Service]] method (or dispatched to a handler). Vernon borrows the GoF definition: "Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations" (raw L14036). In DDD application usage "we might think of a Command object as a serialized method invocation" — interested in everything except the undo (raw L14036-14038).

## Why use one

The motivating smell is parameter noise. The sample `provisionTenant()` takes nine parameters, "probably at least a few too many" (raw L14036). A `ProvisionTenantCommand` collapses them into one object of basic types:

```java
public class ProvisionTenantCommand {
    private String tenantName;
    private String tenantDescription;
    private boolean isActive;
    private String administratorFirstName;
    // ... plus getters and setters
}
```

Properties matter here: "having public setters allows the Command to be populated by UI form-field-to-object mappers" (JavaBean or .NET CLR properties). The zero-argument constructor supports those mappers; a multi-argument constructor supports direct construction (raw L14074).

## More than a DTO

"You might think of the Command as a DTO, but it is truly more than that. Since the Command object is named for the operation that is to be carried out, it is more explicit" (raw L14074). A DTO is a shapeless data holder; a Command names an intent (`ProvisionTenantCommand`), which makes the application API self-documenting. It uses only basic types, never model objects, so it decouples clients from domain types (contrast the trade-offs in [[application-service]]).

## Command Handlers and temporal decoupling

A Command need not be handed directly to an Application Service method. "Besides this approach of dispatching to an Application Service API method... we could instead or in addition send Commands to a queue to be dispatched to a **Command Handler**" (raw L14090). "Consider a Command Handler to be semantically equivalent to an Application Service method, but temporally decoupled" — enabling greater throughput and scalability of command handling. This is the entry point into a [[cqrs|CQRS]]-style write side; see [[command-handler]] for the full pattern.

## Trade-offs

- **Gain:** clean single-argument service signatures, explicit named intents, mapper-friendly, queueable/loggable, decoupled from model types.
- **Give up:** the free validation and strong typing of [[value-object|Value Object]] parameters (a Command carries `String`s, not `EmailAddress`); an extra class per operation. As Vernon says throughout, "There is not necessarily a right or wrong way" between domain types, primitives/DTOs, and Commands.

## Related

[[application-service]] · [[command-handler]] · [[value-object]] · [[cqrs]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
