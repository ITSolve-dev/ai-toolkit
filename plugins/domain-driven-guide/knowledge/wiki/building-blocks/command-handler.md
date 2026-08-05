---
title: Command and Command Handler
category: building-blocks
summary: A serialized, named Command object representing an application operation, dispatched to a Command Handler that stands in for an Application Service method — enabling temporal decoupling, load balancing, competing consumers, and pluggable cross-cutting concerns.
tags: [pattern, command, command-handler, application-service, cqrs, messaging, event-sourcing]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

A **Command** is a serialized object naming an application operation and carrying its parameters — effectively a reified [[application-service|Application Service]] method call (see [[command-object]]). A **Command Handler** is the object the command message is delivered to; it stands in for (and is roughly equivalent to) the Application Service method it replaces. In [[event-sourcing|A+ES]] designs, commands and command handlers are an optional enhancement layered over the plain Application Service.

Start from an ordinary Application Service method:

```
public void LockCustomer(CustomerId id, string reason) {
  var eventStream = _eventStore.LoadEventStream(id);
  var customer = new Customer(stream.Events);
  customer.LockCustomer(reason);
  _store.AppendToStream(id, eventStream.Version, customer.Changes);
}
```

Serialize the method name and its parameters into a class, and you have a Command:

```
public sealed class LockCustomerCommand {
  public CustomerId CustomerId { get; set; }
  public string Reason { get; set; }
}
```

The handler is then a `When(LockCustomerCommand)` method that does exactly what the original method did. Commands are dual to [[domain-event|Events]] in their contract semantics:

> "Command contracts follow the same semantics as Events and can be shared across systems in a similar fashion." (raw L14672)

The distinction of intent matters: a **Command** expresses a request to do something (may be rejected); an **Event** records something that already happened (immutable fact). Both are serializable messages.

## Why bother — the payoffs of decoupling

Because commands are serialized messages sent over a queue, the client is decoupled from the service that handles them:

> "decoupling the client from the Service can enhance load balancing, enable competing consumers, and support system partitioning" (raw L14694)

- **Load balancing / competing consumers.** Run the same Command Handler on many servers; the messaging infrastructure delivers each queued command to one available handler (round-robin or more sophisticated).
- **Temporal decoupling.** The client is not blocked when the service is briefly unavailable (maintenance, upgrade). Commands sit in a persistent queue and are processed when a handler comes back online. > "This approach creates temporal decoupling between clients and the Application Service, leading toward more robust systems." (raw L14700)

## A uniform interface for cross-cutting concerns

Giving every handler a standard interface lets you patch in generic pre-/post-execution behavior. Note the dispatch mirrors the A+ES `Mutate()` trick:

```
public interface IApplicationService { void Execute(ICommand cmd); }
public void Execute(ICommand command) {
  ((dynamic)this).When((dynamic)command);   // like Mutate() dispatching to When()
}
```

With that shared interface you can wrap a handler in decorators for logging, auditing, authorization, validation, or error handling — added in one place, applied to all commands:

```
var service = new CustomerApplicationService(eventStore, pricingService);
var withLogging = new LoggingWrapper(service);  // times & logs every Execute
```

Because commands are serialized and dispatched centrally, error handling can also be centralized — e.g. on a concurrency-contention error (see [[optimistic-concurrency-control]]), retry X times using a Capped Exponential Back-off strategy, uniform and maintained in a single class.

## Trade-offs and scope note

Command/Command Handler is an application-layer and messaging concern rather than a core tactical DDD building block; it is included here because it directly shapes how [[application-service|Application Services]] and [[event-sourcing|A+ES]] Aggregates are invoked, and because A+ES almost always arrives together with [[cqrs|CQRS]], where the command side is exactly this. The cost is the additional infrastructure and asynchrony: a queue, message contracts, eventual processing, and the reasoning burden that comes with temporal decoupling.

## Failure modes

- Confusing Command and Event contracts — treating a rejectable request as an immutable fact (or vice versa) muddles the model.
- Introducing the messaging/queue machinery when the system does not need load balancing, competing consumers, or temporal decoupling — pure overhead over a direct Application Service call.

## Related

[[command-object]] · [[application-service]] · [[event-sourcing]] · [[optimistic-concurrency-control]] · [[cqrs]] · [[domain-event]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
