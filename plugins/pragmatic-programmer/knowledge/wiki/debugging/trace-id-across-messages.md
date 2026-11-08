---
title: Trace id across messages
category: debugging
summary: "Message types and handler log lines carry no identifier copied from the incoming message to the outgoing ones: in an actor or message-driven flow the path of one request cannot be rebuilt from the logs."
tags: [rule, debugging, tracing, message-passing]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

When work passes through messages, there is no call stack to read. A single identifier carried along the flow gives that path back.

## Rule

The book says systems built on actors, blackboards or microservices need good tooling to follow messages and facts as they move. Its suggested technique: «можно ввести однозначный идентификатор трассировки при инициализации конкретной прикладной функции, а затем распространить его среди всех заинтересованных акторов» (p. 237). What happened can then be reconstructed from the log files (p. 237).

## Sign in code

These shapes are this wiki's own.

- A message type with no identifier field for the originating request.
- A handler that builds outgoing messages without copying the identifier from the incoming one.
- A handler that generates a new identifier per message instead of reusing the one it received.
- A handler's log call omits the identifier the message carries.

## When not to apply

These limits are this wiki's own.

- The flow is one synchronous call stack, where a stack trace already shows the path.
- The messaging layer injects and carries the identifier itself. Check that it does before reporting.
- A consumer merges many messages into one result. One identifier cannot name all their origins, so the outgoing message needs a list of them.

## Repair

1. Generate the identifier where the flow starts, as the book says (p. 237).
2. Carry it in every outgoing message, as the book says (p. 237). This wiki notes that one handler that forgets it cuts the chain.
3. Log it in every handler. This step is this wiki's own statement of what reconstruction from logs requires.

## Before and after

```
on "order"(msg):
    log("order received")
    send(stock, "reserve", item = msg.item)
```

```
on "order"(msg):
    log("order received", trace = msg.trace)
    send(stock, "reserve", item = msg.item, trace = msg.trace)
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020, see [[pragmatic-programmer]]: the technique, p. 237.

This wiki's own: `## Sign in code`, `## When not to apply`, the note in step 2 of `## Repair`, and step 3. The pseudocode is this wiki's own. Related: [[actor-model]], [[blackboard]], [[trace-statements]].
