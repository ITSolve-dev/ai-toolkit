---
title: Sequence Versus Wait
category: ordering
summary: A sequence constrains order and leaves work available; a wait stops work on someone else's clock. A wait belongs between tasks, not inside one.
tags: [decision-rule, dependencies, decomposition]
sources: [humanizing-work-splitting, radzikowska-waiting-blocked]
created: 2026-11-01
updated: 2026-11-01
---

# Sequence Versus Wait

Two tasks that cannot both proceed now stand in one of two relations, and the charter names the difference as a topic. In a sequence, one task must come first and the project can do it. In a wait, the project needs something from an outside party and cannot make it happen sooner. No ingested source draws this line directly. This page builds it from two sources, and the distinction and the rule below are this wiki's.

## The discriminating test

Who holds the prerequisite?

- **The project holds it: a sequence.** The dependency constrains order. Work is available, because the earlier task can be started. The Humanizing Work authors' stated dependencies are of this kind: "(given one card type already implemented)" ([[humanizing-work-splitting]] L269). See [[independent-tasks]].
- **An outside party holds it: a wait.** The dependency stops work on someone else's clock. The source's words are "waiting on an external group (another service, customer, or supplier)" ([[radzikowska-waiting-blocked]] L44). See [[waiting-versus-blocked]].

## The rule that follows

Cut so that a known wait falls between tasks and not inside one. A task that hits a wait after starting fails the charter's first working test, that a started task can be finished without waiting ([[unit-of-work]]). If the wait is known in advance, the part that depends on it becomes a separate task that does not start until the outside party has delivered.

## Sign of violation

- **In board history:** a task that moved to a parked or blocked state after starting, on a dependency that was knowable when the task was cut.
- **In task text:** a task whose scope includes getting something from an outside party and also building on the result.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Who holds the prerequisite | The task text and the request |
| Whether the wait is known in advance | The request and earlier tasks of the same kind on the board |

The classification was wrong if an item treated as a sequence stalled for lack of someone outside, or if an item treated as a wait turned out to be something the project could do itself.

## Why

What breaks is a started task. A sequence is resolved by ordering and costs nothing while it is in place, while a wait inside a task leaves it open, holding its place in the count on [[blocked-work-counts-against-wip]], with its context going stale. This reasoning is this wiki's.

## Cost

Cutting at the wait makes more tasks and leaves a result half-delivered until the outside party responds. A piece cut before a wait may also fail the test of having something to show ([[vertical-slice]]). If it does, keep the task whole and do not start it until the outside party delivers.

## Agent executor note

The distinction concerns who holds the prerequisite and does not depend on the executor. An agent adds weight to it, because a stopped agent run does not pick up where a person's memory would. That point is this wiki's and is unmeasured.
