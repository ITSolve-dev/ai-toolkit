---
title: Observer or publish-subscribe
category: structure
summary: "A method doing other work loops over callbacks inline and a callback in view blocks (I/O, network, a lock) or raises a failure that work does not handle; or code publishes on a channel and its next lines depend on what a subscriber did."
tags: [decision-rule, events, observer, publish-subscribe, coupling]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-07
---

Both patterns let code react to events. They differ in who has to know whom. In Observer, a source keeps a list of clients, each of which registered directly, usually by passing a function reference, and when an event occurs the source walks the list and calls each function with the event (p. 181). In publish-subscribe, publishers and subscribers connect through named channels implemented in separate code, and that communication happens outside the application code and potentially asynchronously (p. 182).

## Rule

Use Observer when listeners can reasonably know the source and can afford to run inside it. Use a channel when producers and consumers should not know each other, or when handling should not hold up the producer.

The book's costs on each side:

- **Observer** couples, because every observer must register with the observable. Callbacks are typically handled synchronously, so it can introduce performance bottlenecks (p. 182).
- **Publish-subscribe** removes both problems and lets code be added or replaced, potentially while the application runs, without changing existing code (p. 182). Its cost is that a system using it heavily is hard to understand: «глядя на издателя, нельзя сразу же увидеть, какие именно подписчики связаны с конкретным сообщением» (p. 182).

The book also treats these as different in build cost. Observer takes so little code that it is its example of when not to use a library, while a basic publish-subscribe system can be built but rarely needs to be, since a library is usually available (pp. 181-182).

## Sign in code

These signs are this wiki's own, since the book states costs and not signs.

- **Observer has outgrown its place:** a method that does other work iterates over registered callbacks inline, and a registered callback in view makes a blocking call (I/O, network, a lock) or raises a failure the source's own work does not handle. A loop without a guard is not the sign by itself, since nearly every Observer loop lacks one. A listener importing the source only to register is what Observer is (p. 181), so that strengthens this sign and is not a sign alone.
- **A channel is doing Observer's job:** code publishes on a channel and the next lines depend on what a subscriber did, by reading state or waiting for it. The publisher is decoupled in form only.

The book's own cost, that a publisher cannot show its subscribers, is not visible at one site. Judging it needs a reader who can search every subscription of a channel name across the code, so this page records it as a reason and not as a sign.

This wiki assigns the neighbouring cases as follows. A model that calls concrete reacting classes directly, with no listener interface yet, is [[observer-publisher-knows-only-interface]]; once a publisher has listeners, how the notification runs is [[observer-vs-publish-subscribe]].

## When not to apply

- Observer has served for decades and is especially common in user interfaces, where callbacks report interaction (p. 182). The book does not ask for it to be replaced there.
- This wiki reads the choice as not worth moving when source and listeners sit in one module and callbacks are brief, because the coupling costs then little.
- Publish-subscribe is essentially only a message-passing system. For reacting to events in combination, the book says something more is needed (pp. 182-183): see [[event-stream]].
- Whether channels should cross process or machine boundaries is outside this wiki's scope. This page covers the choice inside one application.

## Repair

From Observer to a channel:

1. Name a channel for the event.
2. Replace the callback loop in the source with one publish.
3. Replace each registration with a subscription, removing the listener's import of the source.
4. Where the reason is delay or failure, use an asynchronous channel. The book says only that delivery is potentially asynchronous (p. 182), and a synchronous channel leaves the callback in the same call path.

From a misused channel to a direct call: if the publisher needs the outcome, call the function directly and take its result.

These steps are this wiki's own; the book describes the patterns and not the migration.

## Before and after

```
// before: listeners know the source and run inside pay()
module Checkout:
    listeners = []
    function onPaid(callback):
        listeners.append(callback)
    function pay(order):
        charge(order)
        for callback in listeners:
            callback(order)

// in the receipts module; sendReceipt calls the mail service
Checkout.onPaid(sendReceipt)
```

```
// after: both sides know only the channel
module Checkout:
    function pay(order):
        charge(order)
        channels.publish("order.paid", order)   // returns at once; delivery is asynchronous

// in the receipts module
channels.subscribe("order.paid", sendReceipt)
```

## Source

[[pragmatic-programmer]], Topic 29, Russian edition, pp. 181-183: both patterns, their costs and the point about libraries. This wiki's own: the rule's phrasing as a choice, the signs, the limit on one module, the repair and the example. Related: [[event-driven-code]], [[coupling]].
