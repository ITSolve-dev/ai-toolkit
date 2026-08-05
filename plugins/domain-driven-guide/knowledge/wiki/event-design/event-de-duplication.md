---
title: Event De-duplication (Idempotent Receiver)
category: event-design
summary: Protecting a subscriber from processing the same domain-event message twice — via idempotent domain operations or, more reliably, an idempotent receiver that tracks handled message ids.
tags: [pattern, event-de-duplication, idempotent-receiver, idempotence, messaging, event-design, domain-event]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

**De-duplication** protects a subscriber from processing the same [[domain-event]] message twice. "De-duplication is a necessity in environments where a single message published through a messaging system could possibly be delivered to subscribers more than once" (raw L7262). It applies to push-based messaging integration (see [[event-driven-integration]]); with pull-based [[notification-log]]s it is "not really a factor" (raw L8298).

## Why duplicates happen

Two mechanisms are described:

- **Broker redelivery on lost ack.** RabbitMQ delivers a message, the subscriber processes it, then fails before acknowledging; "RabbitMQ delivers the unacknowledged messages again" (raw L7264-7270).
- **Publisher-side non-atomicity.** When publishing out of an [[event-store]] whose persistence is not shared with the broker and without XA, the `PublishedMessageTracker` update can fail after the broker already received the messages; on retry, already-sent Events are sent "(again!)" (raw L7274-7284). This is the trade-off of the shared-store-avoidance approach in [[event-driven-integration]].

## Two ways to be idempotent

1. **Idempotent domain operation.** If the subscriber's model operation is naturally idempotent, duplicates are harmless. "An idempotent operation is one that can be executed two or more times in succession with results identical to those of executing the same operation only once" (raw L8290) — e.g. committing an already-committed `BacklogItem` to a `Sprint` is ignored, so "Event de-duplication is unnecessary" there (raw L7229). But designing domain objects to be idempotent "can be difficult, impractical, or even impossible" (raw L8292), and out-of-sequence Events can still cause errors.
2. **Idempotent receiver.** When the domain operation cannot be idempotent, make the *receiver* idempotent — "design the subscriber/receiver itself to ... refuse to execute an operation in response to a duplicate message" (raw L8294). This is the **Idempotent Receiver** pattern [Hohpe & Woolf] (raw L8286).

## Implementing an idempotent receiver

If the messaging product doesn't provide de-duplication, the receiver tracks handled messages: save the topic/exchange name plus the unique message id of every handled message, then "query for duplicates before handling each message" and ignore matches (raw L8294). Key rules:

- **Don't track only the latest id.** "messages can be received out of order ... a de-duplication query that checks for message IDs less than the most recent one would cause you to ignore some messages that were received out of order" (raw L8296).
- **Commit tracking with the model change.** "the tracking of handled message identity be committed along with any changes to the local domain model state. Otherwise, you will be unable to maintain tracking consistency" (raw L8300).
- **It's infrastructure, not domain.** "The handled message tracking is not part of the domain model ... only ... a technical work-around for common messaging idiosyncrasies" (raw L8294); obsolete tracking entries can be garbage-collected (raw L8296).

This is also why Events published outside their local context are given a unique identity (see the identity discussion in [[domain-event]]) (raw L7265-7269).

Related: [[domain-event]], [[event-driven-integration]], [[event-store]], [[notification-log]].
