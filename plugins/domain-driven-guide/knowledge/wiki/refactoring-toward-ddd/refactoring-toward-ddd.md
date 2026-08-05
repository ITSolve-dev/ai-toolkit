---
title: Refactoring Toward DDD (from a legacy system)
category: refactoring-toward-ddd
summary: An incremental strategy for moving an existing big ball of mud toward a DDD model in place — pick a concrete goal, extract use cases behind a service layer, pull I/O out of the domain, then identify aggregates and introduce domain events.
tags: [guide, refactoring, legacy, service-layer, use-cases, incremental-adoption, architecture-tax, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Refactoring Toward DDD (from a legacy system)

This is the "how to get there from here" strategy: how to migrate an existing [[big-ball-of-mud]] toward a domain-driven model **without a rewrite**, one bounded step at a time. It answers the developer stuck "here with my big ball of Django mud" who sees "no way to get to your nice, clean... model" (raw L6533).

## Start with a goal, and fund it

First decide *why*: "what problem are you trying to solve? Is the software too hard to change? Is the performance unacceptable? Have you got weird, inexplicable bugs?" (raw L6538) A clear goal lets you prioritize and, crucially, justify the work to the business. A practical tactic is to attach the cleanup to feature work — "Making complex changes to a system is often an easier sell if you link it to feature work... With a six-month project to deliver, it's easier to make the argument for three weeks of cleanup work. Bob refers to this as architecture tax." (raw L6542..6547)

## Extract use cases behind a service layer

"Start by working out the *use cases* of your system." (raw L6567) A UI action, a cron job, or a Celery task each maps to one use case, and "each of your use cases needs to have an imperative name: Apply Billing Charges, Clean Abandoned Accounts, or Raise Purchase Order" (raw L6570). Create a single function or class per operation whose job is *orchestration*. Each use case should (raw L6579..6588):

- Start its own database transaction if needed
- Fetch any required data
- Check any preconditions (the Ensure pattern)
- Update the domain model
- Persist any changes

Each "should succeed or fail as an atomic unit" (raw L6590). This is the first place to introduce a [[unit-of-work]] to control transactions — pulling all logic into one method "made the system easier to reason about" versus managers calling managers (raw L6592).

**Duplication beats chained calls.** "It's fine if you have duplication in the use-case functions... It's better to duplicate some code in a few places than to have use-case functions calling one another in a long chain." (raw L6594) If one use case must call another, note it and avoid long-running transactions; better still, move to a [[message-bus]] so a finished use case raises an event that a handler elsewhere consumes (raw L6878).

## Pull I/O out, toward a pure domain model

Use the extraction as an opportunity to "pull any data-access or orchestration code out of the domain model and into the use cases" and to "pull I/O concerns (e.g., sending email, writing files) out of the domain model and up into the use-case functions" (raw L6596). Abstractions ([[ports-and-adapters]]) keep handlers unit-testable even while performing I/O. The payoff: "you'll have a grasp of what your program actually *does*... We'll have taken a step toward building a pure domain model." (raw L6604)

## Then identify aggregates and add events

With orchestration localized, break the single object graph by identifying [[aggregate|aggregates]] and replacing direct object references with identifiers; introduce a [[message-bus]] and [[domain-event|domain events]] so writes change one aggregate at a time (raw L6795). For heavy reads, replace nested ORM loops with plain SQL — the first step toward a [[read-model|CQRS read model]].

## It is incremental, and messy is OK

You do not need to do it all at once: "you can absolutely adopt these techniques bit by bit. If you have an existing system, we recommend building a service layer to try to keep orchestration in one place. Once you have that, it's much easier to push logic into the model and push edge concerns like validation or error handling to the entrypoints." (raw L6869) When extraction would break tangled code, "Just copy and paste. It's OK to cause more duplication in the short term" — copy to a clean new place, then redirect callers and delete the mess (raw L6872). "Don't expect things to get instantly better, and don't worry if some bits of your application stay messy." (raw L6872)

## Failure modes to avoid while refactoring

- Use-case functions that call each other in long chains (re-creating the treasure hunt) — prefer duplication or a message bus.
- Long-running database transactions spanning several use cases.
- Leaving data access inside model objects, so "pure domain model" never actually arrives.

## Related

- [[big-ball-of-mud]] — the starting state this strategy escapes.
- [[strangler-fig-pattern]] — the alternative when you replace a subsystem wholesale rather than clean in place.
- [[collaborative-domain-modeling]] — the recommended first step before restructuring code.
- [[aggregate]] · [[domain-event]] · [[message-bus]] · [[unit-of-work]] · [[application-service|service layer]] — the building blocks the refactor introduces.
