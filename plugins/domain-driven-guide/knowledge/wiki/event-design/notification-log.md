---
title: Notification Log (RESTful Event Notifications)
category: event-design
summary: Publishing stored domain events as Atom-style RESTful resources that consumers pull — a current log plus immutable archived logs chained by hypermedia links, made scalable through HTTP caching.
tags: [pattern, notification-log, rest, atom, event-design, pull-model, caching, integration]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

A **Notification Log** publishes stored [[domain-event]]s as RESTful, Atom-style resources that consumers **pull**, providing Publish-Subscribe semantics without a broker. "It's actually based on Atom concepts" (raw L7673). It is one of two styles for forwarding stored Events from an [[event-store]]; the other is push-based messaging middleware (see [[event-driven-integration]]).

## When it fits — pull, not queue

"The REST style ... works best when used in an environment that follows the basic premises of Publish-Subscribe" — "many consumers are interested in the same events ... available from a single producer" (raw L7663-7665). It "follows the basic Publish-Subscribe pattern, even though it uses the _pull model_ instead of the _push model_" (raw L7667). It breaks down as a **Queue**: "if one or a few consumers are required to pull from multiple producers ... in a specific sequence, you will probably quickly feel the pain" (raw L7669).

## Current log and archived logs

Events are grouped into fixed-size logs (the examples use 20). Clients `GET` the well-known **current log** URI (`//iam/notifications`), which "contains the very latest notifications" (raw L7675). When it fills to 20 it "is automatically archived" (raw L7679). Logs chain via hypermedia `Link` headers — `rel=self`, `rel=previous`, `rel=next` — forming "a virtual array of all Events from the most recent Event back to the very first Event" (raw L7689-7708).

**Client-driven tracking.** "The onus is on the client, not the server, to track the next notification to apply" (raw L7699). The client stores the id of its most recently applied notification, walks back through linked logs to find it, then applies all newer Events **in chronological order** — "Unless the oldest Events are applied first in the order in which they occurred, the changes ... could well cause bugs" (raw L7677).

**Stable, immutable resources.** An archived log "can no longer be altered ... it will always be the same" (raw L7683); "Events previously added to any log must never change" (raw L7687), so a client's "applied once and for all times" guarantee holds. The current log's URI uses the full id range (e.g. `61,80`) even before it fills, "because the resource must remain stable over its entire lifetime" for caching (raw L7714-7720).

## Caching = scalability

Because resources are stable, HTTP caching carries the load: the current log may be cached briefly (`Cache-Control: max-age=60`) and archived logs long (`max-age=3600`) since they never change (raw L7749-7775). Clients can use `max-age` as a polling/sleep interval, so "an ill-behaved client can never hurt performance or availability of the notification producer" (raw L7773). Server-side, a request for an archived log "warms the cache for all other clients" (raw L7775).

## Implementation notes

Logs are computed, not stored: `NotificationService.currentNotificationLog()` / `notificationLog(id)` build a `NotificationLog` by reading a range of `StoredEvent`s from the [[event-store]] and wrapping each in a `Notification` — "there is no need to actually persist any Notification instances or whole logs. We can just manufacture them each time" (raw L7972). The current log id is derived from the total Event count modulo the log size (raw L7873-7890). A JAX-RS `NotificationResource` serves the two `GET` endpoints (raw L8003-8044).

## De-duplication

With the pull model, "de-duplication is not really a factor. Client receivers need to save only the most recently applied notification identity" (raw L8298) — contrast the push/messaging style, which does require [[event-de-duplication]].

Related: [[event-store]], [[domain-event]], [[event-driven-integration]], [[event-de-duplication]], [[bounded-context]].
