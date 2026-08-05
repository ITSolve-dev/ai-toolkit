---
title: Unit of Work
category: building-blocks
summary: An abstraction over atomic operations that wraps a business transaction, tracks the objects touched during it, and commits or rolls them back as a single unit — the piece that fully decouples the service layer from the data layer and provides a single entrypoint to persistent storage (and to repositories).
tags: [pattern, unit-of-work, repository, service-layer, persistence, atomicity, transaction, context-manager, dependency-inversion, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Unit of Work

The **Unit of Work (UoW)** pattern is an abstraction over the idea of *atomic operations*. Where the [[repository]] pattern abstracts persistent storage, the UoW abstracts the *transaction* — the boundary within which a set of changes either all succeed together or are all discarded. In the Cosmic Python treatment it is the final piece that ties the [[repository]] and [[application-service|service layer]] patterns together:

> "If the Repository pattern is our abstraction over the idea of persistent storage, the Unit of Work (UoW) pattern is our abstraction over the idea of *atomic operations*. It will allow us to finally and fully decouple our service layer from the data layer." (raw L2752)

Without a UoW, the entry point (e.g. a Flask handler) talks to three layers at once — it starts a database session, instantiates a repository over that session, and calls a service to do the work. With a UoW, the entry point does only two things: it initializes a unit of work and invokes a service. The service collaborates with the UoW (the authors "like to think of the UoW as being part of the service layer"), and neither the service function nor the web framework needs to talk to the database directly (raw L2764).

## What it gives you

The UoW is "a single entrypoint to our persistent storage, and it keeps track of what objects were loaded and of the latest state" (raw L2794). Concretely it buys three things (raw L2799):

- **A stable snapshot** of the database to work with, so the objects in play don't change halfway through an operation.
- **All-or-nothing persistence** — a way to persist every change at once, so a mid-operation failure can't leave the system in an inconsistent state.
- **A simple persistence API and a handy place to get a repository** — repositories are reached *through* the UoW (`uow.batches`), not wired up separately.

## Shape: a context manager

The idiomatic Python realization is a context manager, which visually groups the code that must happen atomically. The abstract interface is minimal — a repository attribute, plus `commit`/`rollback` and the `__enter__`/`__exit__` setup/teardown hooks:

```python
class AbstractUnitOfWork(abc.ABC):
    batches: repository.AbstractRepository

    def __exit__(self, *args):
        self.rollback()          # rollback on exit unless commit() already ran

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
```

A concrete implementation supplies the real transactional machinery. In `__enter__` it starts a database session and instantiates a real [[repository]] bound to that session; in `__exit__` it closes the session; `commit()`/`rollback()` delegate to the session. The concrete class is attached only at the outside edge of the system, so the [[application-service|service layer]] depends on the *abstract* UoW alone (raw L2965) — an application of the [[dependency-inversion-principle]].

A service reads as one atomic block:

```python
def allocate(orderid, sku, qty, uow: AbstractUnitOfWork) -> str:
    line = OrderLine(orderid, sku, qty)
    with uow:
        batches = uow.batches.list()   # repo reached through the UoW
        ...
        batchref = model.allocate(line, batches)
        uow.commit()                    # explicit commit when done
    return batchref
```

## Design decision: explicit commit, rollback by default

Two deliberate choices shape the pattern's safety properties, and they are judgment calls the authors argue for explicitly.

**Explicit commit rather than implicit.** An alternative UoW could commit automatically on the happy path (`__exit__` calls `self.commit()` when no exception occurred) and roll back only on an exception, saving a line of client code. The authors prefer requiring an explicit `uow.commit()`:

> "This is a judgment call, but we tend to prefer requiring the explicit commit so that we have to choose when to flush state." (raw L3025)

The payoff is that the software is *safe by default*: "The default behavior is to *not change anything*. In turn, that makes our code easier to reason about because there's only one code path that leads to changes in the system: total success and an explicit commit. Any other code path, any exception, any early exit from the UoW's scope leads to a safe state." (raw L3028)

**Rollback by default.** On exiting the `with` block without a commit, the UoW rolls back — and the rollback "has no effect if `commit()` has been called" (raw L2877), so it rolls back to the last commit. The reasoning: "we prefer to roll back by default because it's easier to understand; this rolls back to the last commit, so either the user did one, or we blow their changes away. Harsh but simple." (raw L3033)

## Atomic grouping in practice

Because the whole `with uow:` block is one transaction, multi-step operations become easy to reason about — every step inside commits together or not at all. Deallocate-then-reallocate is the canonical example: "If `deallocate()` fails, we don't want to call `allocate()` ... If `allocate()` fails, we probably don't want to actually commit the `deallocate()` either." (raw L3055). Likewise, correcting a batch's purchased quantity may force deallocating an unknown number of order lines in a loop; if anything fails partway, none of the changes should be committed (raw L3075). This transactional boundary is the same boundary aggregate design cares about — one transaction per [[consistency-boundary]] — which is why the UoW sits naturally beneath [[aggregate]] persistence.

## Swapping the backing store (Appendices C & D)

Two appendices re-implement the *same* abstract UoW over different stores, showing that infrastructure is
genuinely decoupled.

**CSV files (Appendix C).** `CsvUnitOfWork` subclasses `AbstractUnitOfWork`, builds a `CsvRepository` for a
folder and exposes it as `self.batches`; its `commit()` rewrites `allocations.csv` from every batch's
allocations and its `rollback()` is a no-op. Once that adapter exists the CLI collapses to "a bit of code
for reading order lines, and a bit of code that invokes our *existing* service layer" (raw L7417) — `main()`
just iterates the orders CSV and calls `services.allocate(orderid, sku, qty, uow)`. The service and domain
layers are untouched by the DB→files switch, exactly the "couple of new `Repository` and `UnitOfWork`
classes" promise the [[repository]] page cites. Caveat: this CSV `commit()` rewrites the whole file and its
`rollback()` does nothing — a teaching illustration with no real atomicity or isolation, unlike a
database-backed UoW wrapping a genuine transaction.

**Django, a non-instrumenting ORM (Appendix D).** With SQLAlchemy the session *instruments* the live domain
objects, so `commit()` auto-flushes whatever changed. Django does not instrument the domain instances (the
domain object is separate from the ActiveRecord — see [[repository]]), so the UoW must do the bookkeeping by
hand: "the `commit()` command needs to explicitly go through all the objects that have been touched by every
repository and manually update them back to the ORM." (raw L7646). Concretely `commit()` iterates the
repository's `seen` set — every aggregate loaded or added — calls `update()` on each to push it back through
the translation layer, then commits; transactions are driven explicitly, since "`set_autocommit(False)` was
the best way to tell Django to stop automatically committing each ORM operation immediately, and to begin a
transaction." (raw L7642). The lurking failure mode is **silent lost updates**: if a touched aggregate is not
registered in `seen` (or not flushed in `commit()`), its changes never reach the database even though the
transaction commits. Testing the real rollback/commit behaviour requires `pytest-django`'s
`mark.django_db(transaction=True)` (raw L7621).

## Trade-offs

SQLAlchemy's `Session` object is already itself a Unit of Work: every time you load an entity the session begins tracking changes to it, and when the session is flushed all changes persist together (raw L3115). So why abstract it away?

- **Simplification.** The Session API is rich and supports operations the domain doesn't want or need; the custom `UnitOfWork` "simplifies the session to its essential core: it can be started, committed, or thrown away." (raw L3127)
- **A home for repositories.** Reaching [[repository]] objects through the UoW is a usability win that a plain SQLAlchemy `Session` doesn't offer (raw L3131).
- **Dependency inversion.** The service layer depends on a thin abstraction, with the concrete implementation attached at the system's outer edge — echoing SQLAlchemy's own advice to "keep the life cycle of the session (and usually the transaction) separate and external" (raw L3141).

The cost is the usual one for any hand-rolled abstraction over a capable library: an extra layer of indirection and code to maintain over machinery the ORM already provides. When the persistence layer is not an ORM with a built-in UoW, or when transactional semantics need to stay hidden from the domain, the abstraction earns its keep; over a thin CRUD app it can be ceremony.

## Failure modes

- **Implicit/auto-commit designs** re-introduce multiple code paths that change state, undermining the "safe by default" property — an exception or early return might still have flushed partial work.
- **Doing transactional work outside the `with` block**, or committing per-repository-call, defeats the atomic-grouping guarantee and can leave the system half-updated.
- **Leaking session/ORM details** (raw `session.execute`, flush timing, ORM-specific query objects) up through the UoW into the service or domain layer re-couples the layers the pattern exists to separate.

## Related

- [[repository]] — the storage abstraction the UoW hands you access to.
- [[application-service|service layer]] — the orchestration layer that owns the `with uow:` transaction script.
- [[aggregate]] — the consistency boundary that the UoW's transaction boundary should line up with.
- [[consistency-boundary]] — one transaction per boundary is exactly what the UoW enforces.
- [[dependency-inversion-principle]] — why the service depends on the abstract UoW, not the concrete one.
- [[message-bus]] — in the fuller design, the UoW collects and publishes an aggregate's [[domain-event|domain events]] after commit.
