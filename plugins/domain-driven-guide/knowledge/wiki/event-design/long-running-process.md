---
title: Long-Running Process (Saga)
category: event-design
summary: An Event-Driven pattern coordinating parallel/distributed work — an executive starts multiple pipelines and a tracker (often an Aggregate) records completions keyed by a shared Process identity, embracing eventual consistency, deduplication, timeouts, and compensation on failure.
tags: [pattern, event-design, saga, process-manager, long-running-process, eventual-consistency, domain-event, messaging, compensation, idempotency]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

A **Long-Running Process** — often called a **Saga** — extends [[event-driven-architecture|Event-Driven]]
Pipes and Filters to parallel and distributed processing. Vernon prefers the name "Long-Running Process"
because "Saga" collides with an older transaction pattern (Garcia-Molina & Salem) (raw L3531).

## Executive and tracker

A single **executive** component (implemented as an [[application-service|Application Service]] or
Command Handler) initiates the parallel processing and tracks it to completion. It maintains a **state
tracker** — "a new Aggregate-like state object for tracking its eventual completion" (raw L3579) —
created when the process begins. For the simplest processes, executive and tracker can merge into a
single [[aggregate|Aggregate]]: a Port-Adapter message handler dispatches to an Application Service that
loads the Aggregate and delegates to a command method, and the Aggregate's own [[domain-event|Domain
Event]] signals its part is done (raw L3573).

Three design approaches are given (raw L3549): (1) a composite task tracked by an executive with a
persistent tracker object (the one taught in depth); (2) **partner Aggregates** that collaborate, one
holding overall state (Pat Helland's model); (3) a fully stateless process where each message enriches
the event with progress so state lives only in the messages.

## Core mechanics

- **Correlation** — assign a unique Process identity (e.g. a UUID) "carried by each of the associated
  Domain Events" so the executive knows which parallel run a completion event belongs to (raw L3569); it
  logs/finalizes only when completions with equal identities arrive. A method like `isCompleted()` on
  the tracker reports when all required branches are in.
- **Deduplication** — under at-least-once messaging, either have the executive check the tracker for an
  existing completion record and ignore duplicates (yet acknowledge them), or design the state object to
  be idempotent so duplicate recordings are absorbed (raw L3591).
- **Timeouts** — the tracker holds an inception timestamp plus an allowable-time constant. A *passive*
  check runs on each arriving completion event (`hasTimedOut()`); its weakness is that the process can
  hang past threshold if some completion never arrives. An *active* check uses an external timer (e.g. a
  JMX `TimerMBean`) that marks the process abandoned and publishes a failure event; its cost is more
  resources and a possible timer/event race (raw L3595).

## Worked example (Ch. 13): Create a Product with a Discussion

Ch. 13 develops a full cross-context Long-Running Process (there also called a *process manager* or
*saga*) that makes [[event-driven-integration]] usable for more than a single fire-and-forget
notification. SaaSOvation's *Create a Product* use case must create a `Product` in the *Agile Project
Management Context* and, if the collaboration add-on is enabled, an exclusive `Forum` + `Discussion` in
the *Collaboration Context*. It is driven entirely by [[domain-event]]s and commands:

1. `Product` is constructed and publishes `ProductCreated` (or, later, `ProductDiscussionRequested`)
   carrying an `isRequestingDiscussion` flag (raw L12673).
2. `ProductDiscussionRequestedListener` sees the flag and sends a `CreateExclusiveDiscussion` command to
   the Collaboration context's exchange (raw L12834).
3. Collaboration's `ExclusiveDiscussionCreationListener` creates the `Forum`/`Discussion`, which publish
   `ForumStarted`/`DiscussionStarted` (raw L12904).
4. Back in Agile PM, `DiscussionStartedListener` calls `ProductService.initiateDiscussion(...)`,
   transitioning the `Product`'s discussion from `REQUESTED` to `READY` with a `DiscussionDescriptor`
   (raw L12981).

The workflow's **state lives in the domain aggregate**: the `Product` holds a `DiscussionAvailability`
(`ADD_ON_NOT_ENABLED`, `NOT_REQUESTED`, `REQUESTED`, `READY`, and later `FAILED`) that *is* the process
state machine (raw L12687). Each step must be [[idempotency|idempotent]] — `initiateDiscussion()` does
nothing if already `READY`: "if the state is currently `READY`, the Long-Running Process has already
completed" (raw L13003).

## Design decision: who owns the process?

Vernon deliberately handles `ProductCreated` inside the *producing* context (Agile PM) rather than
letting Collaboration interpret it (raw L12853-L12855). In an event-driven architecture contexts are not
cleanly "upstream/downstream"; more importantly, "does `ProductCreated` actually have any meaning at all
to the *Collaboration Context*?" — it does not. Making Collaboration react to foreign creation events
would force it to "support any number of foreign Events as creation commands," coupling it to every
consumer's vocabulary. Owning the process locally also keeps a place to attach process management (the
tracker below). This is a concrete heuristic against leaking one context's [[ubiquitous-language]] into
another.

## Time-out and retry: TimeConstrainedProcessTracker

Because any message may be lost or delayed, a naive chain of listeners can stall forever. SaaSOvation
adds a reusable `TimeConstrainedProcessTracker` that "watches for processes whose allotted time for
completion has expired, and those that can be retried any number of times prior to expiring"
(raw L13009):

- The tracker is created when the process starts (`startDiscussionInitiation`), configured e.g. "retries
  every 5 minutes" / "3 total retries" (raw L13107), and its `ProcessId` is stored on the `Product`.
- A background timer calls `checkForTimedOutProcesses()`, which asks each timed-out tracker to
  `informProcessTimedOut()`, publishing a `ProcessTimedOut` subclass event (raw L13138).
- A `...RetryListener` reacts: on a full time-out (`hasFullyTimedOut()`) it runs **compensation**;
  otherwise it re-issues the request.
- On success, `tracker.completed()` stops further retries (raw L13321).

The tracker "is not part of the Core Domain. It is rather part of a technical Subdomain that any
SaaSOvation project can reuse" (raw L13013) — so its persistence relaxes strict [[aggregate]] rules (it
is isolated, one-to-one with its process, and unlikely to hit concurrency conflicts). See [[subdomain]].

## Compensation on failure

A full time-out triggers `Product.failDiscussionInitiation()`, which moves the discussion to a `FAILED`
state and clears the process id — "the simple compensation necessary to keep the `Product` in a sound
state" (raw L13221) — and emails the product owner for human intervention. Long-running processes replace
ACID rollback with **explicit compensating actions**.

Two message-handling cautions from this example: with at-least-once delivery, retried
`CreateExclusiveDiscussion` commands cause duplicate creation attempts, so the downstream operation must
be made idempotent (find-or-create), not have its retries disabled — see [[idempotency]]. And if sending
the initial command fails, either throw from `filteredDispatch()` to NAK and force redelivery, or retry
with a capped exponential back-off (raw L13335).

## Sophisticated multi-step processes

For workflows needing several confirmations, Vernon offers a `Process` interface and `AbstractProcess`
base class (which extends `Entity`, so an aggregate can *be* a process). Each concrete process defines
`completenessVerified()`, and the process is only marked complete when every required step (e.g.
`confirm1()` **and** `confirm2()`) has fired (raw L13525). `ProcessCompletionType` distinguishes
`NotCompleted` / `CompletedNormally` / `TimedOut`.

## Trade-offs and failure handling

Long-Running Processes "have nothing to do with distributed transactions. They require a mindset that
embraces eventual consistency" (raw L3601) — every participant is inconsistent with the others until the
executive receives final completion (see the eventual-consistency modeling in
[[bounded-context-autonomy]]). When infrastructure or a task fails, **compensation** may be required, and
"If compensation is mandatory, it could surpass the complexity of designing the success path" (raw
L3601); sometimes it is better to let business procedures accommodate the failure via workflow. The
reward is elegant distribution and parallelism — useful especially when integrating high-latency legacy
systems — yielding highly scalable, available systems. Some messaging platforms (NServiceBus,
MassTransit) provide Saga support directly.

## Related

- [[event-driven-architecture]] — the Pipes-and-Filters base this extends.
- [[event-driven-integration]] — the cross-context messaging integration the Ch. 13 process rides on.
- [[domain-event]] — the correlated messages that drive it.
- [[aggregate]] — the natural home of the state tracker (and of the `Product` process state).
- [[idempotency]] — the at-least-once tolerance every step of the process needs.
- [[subdomain]] — where the reusable `TimeConstrainedProcessTracker` lives (a technical Subdomain).
- [[event-store]] — the per-context log the driving events are appended to.
- [[bounded-context-autonomy]] — where the "eventual consistency is a modeled state" mindset is worked
  through.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
