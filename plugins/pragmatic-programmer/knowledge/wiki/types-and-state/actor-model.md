---
title: Actor model
category: types-and-state
summary: "A lock held across several steps on shared data, with a decision or an outgoing call inside it, is the candidate; in code that claims to use actors, a handler reading another actor's fields, a message carrying a mutable object, or a module variable used from a handler breaks the model."
tags: [rule, concurrency, actors, message-passing]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

An actor is an independent virtual processor with its own private state and a mailbox. It sleeps until a message arrives, handles it, then takes the next message or sleeps again. While handling a message it can create actors, send messages to actors it knows, or move to a new state for the next message (p. 227). A process, usually a more general virtual processor from the operating system, can be held by convention to the same behaviour (p. 227).

## Rule

The book's tip is to use actors for concurrency without shared state: «Пользуйтесь акторами, чтобы достичь параллельности без общего состояния» (p. 228). The model is defined by four properties (pp. 227-228):

- There is no central control: nothing schedules what runs next or orchestrates the flow from input to output.
- The only state is in messages and in each actor's local state. Messages are visible only to the reader, and local state is unreachable from outside.
- Messages are one-way. For a reply, the sender includes its mailbox address and the reply arrives as an ordinary message.
- «Актор поочередно полностью обрабатывает каждое сообщение.» (p. 228)

The outcome is that «акторы выполняются одновременно, асинхронно и не используют совместно ничего общего» (p. 228). The book says no code for managing concurrency is needed, since there is no shared state, and no explicit end-to-end flow either (p. 232). The same code runs on one processor, on many cores or across machines (pp. 228, 232).

This wiki reads the book's restaurant rewrite as the point of it: the pie case checks its slices and removes one inside a single handler, and the waiter never sees the count. Check and act sit in one message, handled to completion, so the race of [[check-then-act-must-be-atomic]] is gone with no lock.

## Sign in code

The book names the candidate in a challenge: existing code that uses mutual exclusion to protect shared data (p. 233). This wiki narrows that, because a lock alone is ordinary: the candidate is a lock held across several steps on shared data, with a decision or an outgoing call inside it. The violations below are also this wiki's own, and apply to code that claims to use actors.

- A handler reading another actor's fields directly.
- A message carrying a reference to a mutable object that the sender keeps using.
- A module or global variable used from inside a handler.
- A handler that blocks waiting for a reply in the middle of handling a message.

This wiki assigns the neighbouring case as follows. A lock that callers hold around one object's data, with no outgoing call inside, is [[lock-belongs-to-the-resource]], whose repair moves the lock. This page's candidate is a held section that a moved lock cannot shorten.

## When not to apply

- This wiki adds that a short critical section around one value is often simpler with a lock than with a new actor.
- This wiki adds that a flow where the caller cannot continue without the answer fits awkwardly, since every reply has to return through a mailbox.
- This wiki adds that actors give no atomicity across actors. The book leaves pie with ice cream, including running out of either, as a challenge (p. 233); this wiki reads that as needing its own owner, as in [[composite-resource]].

## Repair

The book suggests prototyping: «Почему бы вам не опробовать прототип того же кода, написанного с помощью акторов?» (p. 233). The steps below are this wiki's own, shaped by the book's example of handlers keyed by message type that receive the message and the state and return the new state (pp. 228-230).

1. Take the data behind the lock and give it one actor as its local state.
2. Turn each guarded section into a message type and a handler.
3. Change callers to send messages, including where a reply should go.
4. Delete the lock.

## Trade-offs

- The price is understanding. «Такие подходы труднее осмыслить, поскольку они действуют по большей части косвенно.» (p. 236). The flow is in no one place, and the book's example output warns that the order may differ between runs (p. 231). Following it needs tooling such as [[trace-id-across-messages]] (p. 237).
- The book also counts deployment and maintenance, since there are many moving parts, offset by being able to replace single actors rather than the whole system (p. 237).

## Before and after

```
shared stock = {}
shared reservations = {}
guard = new Lock()

function reserve(order, item):
    guard.protect:
        if stock[item] == 0:
            return false
        stock[item] -= 1
        reservations[order] = item
        notify_warehouse(order, item)
        return true

function release(order):
    guard.protect:
        item = reservations.remove(order)
        stock[item] += 1
```

```
actor Stock:
    state stock = {}
    state reservations = {}

    on "reserve"(order, item, reply_to):
        if stock[item] == 0:
            send(reply_to, "refused", order)
            return
        stock[item] -= 1
        reservations[order] = item
        send(warehouse, "reserved", order, item)
        send(reply_to, "accepted", order)

    on "release"(order):
        item = reservations.remove(order)
        stock[item] += 1

// callers
send(stock_actor, "reserve", order, item, self)
send(stock_actor, "release", order)
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020, see [[pragmatic-programmer]]: definitions and properties, pp. 227-228; the restaurant example, pp. 228-231; no explicit concurrency, p. 232; the challenges, p. 233; the costs, pp. 236-237.

This wiki's own: the reading of why the race disappears, the narrowed candidate, the violations and the assignment under `## Sign in code`, the limits it marks as its own, and the numbered repair. The pseudocode is this wiki's own. Related: [[shared-state-is-incorrect-state]], [[blackboard]], [[event-driven-code]].
