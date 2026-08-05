---
title: Managing Transactions with Repositories
category: building-blocks
summary: Transactions belong in the Application Layer (a Facade/Application Service per use case), never in the domain model; Repositories must enlist in the same Session/Unit of Work the Application Layer started, and committing many Aggregates in one transaction is a concurrency trap.
tags: [guide, repository, transaction, application-service, aggregate, consistency]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

Transactions are an application-orchestration concern, not a domain concern. The domain model must stay ignorant of them.

> "The domain model and its encompassing Domain Layer is never the correct place to manage transactions. The operations associated with a model are usually too fine grained to themselves manage transactions and shouldn't be aware that transactions play a part in their life cycle." (raw L11002)

## Where transactions live: the Application Layer Facade

The standard placement is a [[application-service|Application Service]] / Facade — one coarse-grained business method per use-case flow:

> "When a Facade's business method is invoked by the User Interface Layer ... the business method begins a transaction and then acts as a client to the domain model. After all necessary interaction with the domain model is successfully completed, the Facade's business method commits the transaction it started. If an error/exception occurs that prevents completion of the use case task, the transaction is rolled back by the same managing business method." (raw L11004)

The method may manage the transaction **explicitly** (begin / commit / rollback in a try-catch) or **declaratively** (e.g. Spring's `@Transactional` annotation with a configured `transactionManager`), which "cuts down on clutter in the business method and allows you to focus on the task coordination itself" (raw L11097).

## Enlisting Repositories in the Application Layer's transaction

For the Repository's writes to actually commit or roll back with the use case, the [[repository]] implementation must share the very same Session / Unit of Work / transaction that the Application Layer opened:

> "To enlist changes to the domain model in a transaction, ensure that Repository implementations have access to the same Session or Unit of Work for the transaction that the Application Layer started." (raw L11028)

The common mechanism is a thread-bound Session (e.g. a `ThreadLocal<Session>` provider injected into both the transaction manager and the Repositories), typically wired by a dependency-injection / IoC container. "With any such persistence mechanism you must find a way to provide access to the same Session, Unit of Work, and transaction that the Application Layer is managing. Dependency injection works well for this" (raw L11167) — and where DI is unavailable, one can fall back to manually binding those objects to the current thread.

## The warning: do not span many Aggregates per transaction

A parting caution that ties transactions back to [[aggregate]] design. Modifying multiple Aggregates in a single transaction usually works fine in a unit test, then fails under production concurrency:

> "Be careful not to overuse the ability to commit modifications to multiple Aggregates in a single transaction just because it works in a unit test environment. If you aren't careful, what works well in development and test can fail severely in production because of concurrency issues." (raw L11173)

The fix is not more transaction machinery but revisiting the [[aggregate]] consistency boundaries — the rule that a single transaction should commit a single Aggregate, with other Aggregates updated eventually via [[domain-event]]s. See [[model-true-invariants-in-consistency-boundaries]] and [[eventual-consistency-between-aggregates]].

## Related

[[repository]] · [[application-service]] · [[aggregate]] · [[domain-event]] · [[book-implementing-ddd-vaughn-vernon]] — source summary.
