---
title: Commands vs. Events
category: event-design
summary: Both are messages, but a command captures intent (imperative, one recipient, fails noisily) while an event captures a past fact (broadcast, many listeners, fails independently); the distinction governs how domain events spread knowledge of successful commands.
tags: [concept, domain-event, commands, messaging, cqrs, message-bus, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Commands vs. Events

A **command** and an **event** are both *messages* — "instructions sent by one part of a system to another" (raw L4756) represented as dumb data structures (e.g. Python dataclasses). They are handled by the same machinery but under deliberately different rules, and the distinction is what makes [[domain-event|domain events]] a coherent modelling tool rather than just a callback mechanism.

## The two message types

**Commands capture intent.** "Commands are sent by one actor to another specific actor with the expectation that a particular thing will happen as a result" (raw L4762). Posting a form to an API handler sends a command. They are named with imperative-mood verb phrases — *allocate stock*, *delay shipment*, *change batch quantity*. Because a command "express[es] our wish for the system to do something" (raw L4764), "when they fail, the sender needs to receive error information" (raw L4765) — a command must fail *noisily*.

**Events capture facts.** "Events capture *facts* about things that happened in the past" (raw L4773) and are named in the past tense — *order allocated to stock*, *batch quantity changed*. An event is broadcast to all interested listeners; "we don't know who's going to pick it up" (raw L4767-4768). Consequently "senders should not care whether the receivers succeeded or failed" (raw L4773-4774) — events may fail *independently*. A key modelling use: "We often use events to spread the knowledge about successful commands" (raw L4771).

## The comparison (raw L4777-4781)

| | Event | Command |
|---|---|---|
| Named | Past tense | Imperative mood |
| Error handling | Fail independently | Fail noisily |
| Sent to | All listeners | One recipient |

These properties show up directly in the dispatch rules: a command has exactly one handler and any error bubbles up (fails fast), whereas an event can fan out to multiple handlers, each of which logs and swallows its own errors so one failure doesn't interrupt the rest — "The command dispatcher expects just one handler per command" and "Events go to a dispatcher that can delegate to multiple handlers per event" (raw L4879, L4856).

## Why this matters for domain modelling

Splitting messages this way lets you align the model with the business: the request a user makes becomes a named command modelling one unit of intent against a single [[aggregate-consistency-boundary|aggregate]], and every downstream consequence (bookkeeping, notification, cross-aggregate updates) becomes a [[domain-event|domain event]]. This is also what lets secondary work fail without failing the customer's core action — see [[aggregate-consistency-boundary]]. The naming discipline is part of the [[ubiquitous-language]]: commands read as the verbs stakeholders use, events as the facts they'd recite after the fact.

## Trade-off / framing note

The book introduces events before commands, but notes the reverse is common and that "Making explicit the requests that our system can respond to by giving them a name and their own data structure is quite a fundamental thing to do" (raw L5086-5088). The whole arrangement of events, commands, and a dispatcher is sometimes called the *Command Handler* pattern (raw L5088-5089) — see this wiki's [[command-handler]] page for Vernon's treatment. Beware over-indexing on the plumbing: the [[message-bus]] routing itself is application architecture, not a DDD pattern — the DDD payload is the *naming* and the *one-command-one-aggregate* consistency rule.

## Related

[[domain-event]] · [[message-bus]] · [[aggregate-consistency-boundary]] · [[ubiquitous-language]] · [[command-handler]] · [[command-object]] · [[command-query-separation]]
