---
title: Message Bus
category: event-design
summary: A simple publish-subscribe dispatcher that maps each domain-event type to a list of handler functions, providing the wiring that lets recorded domain events trigger side effects; the book converges on having the Unit of Work collect and publish events after commit.
tags: [pattern, message-bus, event-design, domain-event, unit-of-work, repository, pub-sub, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Message Bus

The **message bus** is the dispatch mechanism that connects [[domain-event|domain events]] recorded by the model to the handlers that respond to them. It is deliberately tiny: a publish-subscribe system usually implemented with a `dict`.

> "A message bus basically says, 'When I see this event, I should invoke the following handler function.' In other words, it's a simple publish-subscribe system. Handlers are *subscribed* to receive events, which we publish to the bus." (raw L3947..3949)

This is application-layer plumbing rather than a domain building block, but it is inseparable from how [[domain-event|domain events]] are used in practice, so it belongs with event design.

## The minimal implementation

```python
def handle(event: events.Event):
    for handler in HANDLERS[type(event)]:
        handler(event)

def send_out_of_stock_notification(event: events.OutOfStock):
    email.send_mail("stock@made.com", f"Out of stock for {event.sku}")

HANDLERS = {
    events.OutOfStock: [send_out_of_stock_notification],
}  # type: Dict[Type[events.Event], List[Callable]]
```

Handlers are keyed by event *type*; `handle()` looks up the list and calls each (raw L3952..3963). The email-sending code — infrastructure — now lives in a handler, never in the model or the [[application-service|service layer]].

## No concurrency, by design

> "the message bus as implemented doesn't give us concurrency because only one handler will run at a time. Our objective isn't to support parallel threads but to separate tasks conceptually, and to keep each UoW as small as possible. This helps us to understand the codebase because the 'recipe' for how to run each use case is written in a single place." (raw L3965)

The point of the bus is *conceptual separation of tasks*, not parallelism.

## Publishing: three ways to get events onto the bus

The recorded events must be *collected from aggregates and published*. The book shows three variants, in increasing elegance:

1. **Service layer explicitly collects.** After `product.allocate(line)` and `uow.commit()`, the service layer passes `product.events` to `messagebus.handle(...)` inside a `try/finally`. "the service layer explicitly collects events from aggregates and passes them to the message bus." (raw L3999)
2. **Service layer creates and raises events directly.** Instead of the model recording the event, the service checks the result (`if batchref is None:`) and calls `messagebus.handle(events.OutOfStock(line.sku))` itself (raw L4002..4020). Also used in production; a matter of trade-offs.
3. **Unit of Work collects and publishes (the preferred solution).** The [[unit-of-work]] already has a `try/finally` and knows every [[aggregate]] in play through the [[repository]], so it is the natural place to spot and dispatch events.

> "we'd like to show you what we think is the most elegant solution, in which we put the unit of work in charge of collecting and raising events." (raw L4023)

## The UoW + repository `.seen` collaboration

In the preferred design, `commit()` runs `_commit()` (implemented by subclasses) and then `publish_events()`, which walks every aggregate the repository has `.seen` and pops each aggregate's `.events` onto the bus:

```python
def commit(self):
    self._commit()
    self.publish_events()

def publish_events(self):
    for product in self.products.seen:
        while product.events:
            event = product.events.pop(0)
            messagebus.handle(event)
```

For this to work the [[repository]] tracks loaded aggregates in a `set` called `.seen`: the base `add()` and `get()` populate `.seen` and delegate to subclass-implemented `_add()` / `_get()` (raw L4030..4092). The payoff: the [[application-service|service layer]] becomes *totally free of event-handling concerns* — it just loads the aggregate, calls a method, and commits (raw L4098..4113).

## Trade-offs and failure modes

- **Handler failure is unresolved here.** The book asks what happens if one of the handlers fails and defers error handling to a later chapter — see [[commands-and-events]]. A naive bus offers no retry/atomicity for handlers.
- **Events dispatched after commit** means side effects fire on already-persisted state; a failing handler cannot roll back the committed transaction.
- **Requires discipline in test fakes.** Fakes for the repository/UoW must call `super().__init__()` and implement the underscore methods so `.seen` tracking works — a small but real maintenance cost the book judges worthwhile.

See also: [[domain-event]], [[unit-of-work]], [[repository]], [[application-service|service layer]], [[eventual-consistency-between-aggregates]], [[internal-vs-external-events]].
