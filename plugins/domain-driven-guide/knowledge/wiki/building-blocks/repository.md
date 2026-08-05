---
title: Repository
category: building-blocks
summary: A DDD building block that gives the illusion of an in-memory collection of all Aggregate instances of a type, providing global access, add/remove, and intent-named finders — one per Aggregate type, and only for Aggregates.
tags: [pattern, repository, building-block, aggregate, persistence, tactical-design, ports-and-adapters, cosmic-python]
sources: [book-implementing-ddd-vaughn-vernon, web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

A **Repository** is a tactical DDD building block that mediates between the domain and the persistence mechanism, giving each persistent [[aggregate]] type the *illusion of an in-memory collection* of all its instances. You place an Aggregate instance into its Repository, later retrieve the same whole object, mutate it, and its changes persist; remove it and it can no longer be retrieved. Evans' original definition frames it as: "For each type of object that needs global access, create an object that can provide the illusion of an in-memory collection of all objects of that type. Set up access through a well-known global interface. Provide methods to add and remove objects. ... Provide methods that select objects based on some criteria and return fully instantiated objects ... **Provide repositories only for aggregates**" (raw L9978).

## Only Aggregates have Repositories

The defining rule: "Strictly speaking, only Aggregates have Repositories" (raw L9996). Generally there is a **one-to-one relationship between an Aggregate type and a Repository** — every persistent Aggregate type has exactly one. The exception is when two or more Aggregate types share an object hierarchy, in which case they may share a single Repository (raw L9980) — see [[repository-type-hierarchies]].

The pattern's usefulness is contingent on actually using Aggregates: "If you are not using Aggregates in a given Bounded Context, the Repository pattern may be less useful. If you are retrieving and using Entities directly in an ad hoc fashion rather than crafting Aggregate transactional boundaries, you may prefer to avoid Repositories" (raw L9996). Some teams instead expose a persistence mechanism's `Session` or Unit of Work directly, or prefer Data Access Objects — but Vernon still advocates designing with Aggregates and Repositories. See [[entity]] for why using bare Entities without Aggregate boundaries weakens the case for Repositories, and [[repository-vs-dao]] for the Repository/DAO distinction.

## Two design flavors

Vernon distinguishes two Repository designs, chosen by what the backing persistence mechanism supports (raw L9998):

- **[[collection-oriented-repository]]** — the traditional design that mimics a `Set`; its interface hints at no persistence at all (no `save()`). Requires a persistence mechanism that tracks changes implicitly.
- **[[persistence-oriented-repository]]** — used when the store cannot implicitly track changes and you must explicitly `save`/`put` modified Aggregates.

## Interface anatomy

**Add / remove**, mirroring `java.util.Collection`: `add()`, `addAll()`, `remove()`, `removeAll()`. Vernon prefers a `void` return over `boolean`, because "answering `true` to an add-type operation does not guarantee success. The `true` results may still be subject to a transaction commit" — so `void` is the more accurate return type (raw L10157). `addAll()`/`removeAll()` are convenience only; a policy of "never add/remove multiple Aggregates per transaction" cannot actually be enforced by omitting them, since a client can always loop over `add()`/`remove()` (raw L10159).

**Finder methods**, named by domain intent rather than by query mechanics — e.g. `calendarEntryOfId(...)` (single instance by unique identity), `calendarEntriesOfCalendar(...)` (all instances for a parent), `overlappingCalendarEntries(..., TimeSpan)` (all entries over a contiguous date/time range) (raw L10168). Finders return *fully instantiated* Aggregates or collections of them. For queries that cut across Aggregate types, see [[use-case-optimal-query]].

**Identity generation** via `nextIdentity()`: the Repository conveniently answers a new globally-unique identity, used at construction time by whatever code instantiates a new Aggregate (raw L10191, raw L10196). One implementation simply returns `new CalendarEntryId(UUID.randomUUID()...)` — fast and reliable, without touching the data store (raw L10424). See [[entity]] for identity-creation techniques and the importance of timing identity assignment.

## Where the interface and implementation live

Place the **interface in the same [[modules|Module]]** (Java package) as the Aggregate type it stores — e.g. `CalendarEntryRepository` sits beside `CalendarEntry` in the domain model (raw L10153). The **implementation goes elsewhere**: either an `impl` sub-package directly under the domain module (a widely-practiced Java convention that keeps domain concepts separate from persistence code), or — as the sample Collaboration Context does — in the **Infrastructure Layer** (raw L10225). Locating the concrete `HibernateCalendarEntryRepository` in infrastructure uses the [[dependency-inversion-principle]]: the Infrastructure Layer sits logically above all others, so references run unidirectionally *downward* to the Domain Layer, and the domain depends only on the abstract interface (raw L10240).

## Removal is a policy decision

Some Aggregate types must *never* be physically removed — for referential integrity, historical/audit reasons, or because removal would be unwise, ill-advised, or illegal (raw L10161). Options: omit removal methods from the public interface entirely; implement them as **logical removal** (mark the Aggregate `disabled` / `unusable` / domain-specifically `logically removed`); or forbid removal via code review. Because "any methods on public interfaces are generally considered available for use," if removal is exposed but logically disallowed, prefer implementing logical rather than physical removal. See [[repository-only-persistence]] for the related stance that persistence (including deletes) flows only through the Repository, never through ORM cascades.

## The Cosmic Python view — the in-memory illusion and ports/adapters

*Architecture Patterns with Python* introduces the Repository as "a simplifying abstraction over data
storage, allowing us to decouple our model layer from the data layer" — one that "hides the boring
details of data access by pretending that all of our data is in memory" (raw L1035, L1243). If laptops
had infinite memory you would just manipulate objects directly, never calling `.save()`; the repository
preserves that programming model even though a database sits behind it — the goal being
[[persistence-ignorance]].

**Minimal interface — `add()` and `get()`.** "The simplest repository has just two methods: `add()` to
put a new item in the repository, and `get()` to return a previously added item" (raw L1263). The
discipline is self-imposed: "We stick rigidly to using these methods for data access... This
self-imposed simplicity stops us from coupling our domain model to the database" (raw L1265). An abstract
base class defines the contract (the *port*); a SQLAlchemy class implements it (an *adapter*):

```python
class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, batch: model.Batch): ...
    @abc.abstractmethod
    def get(self, reference) -> model.Batch: ...

class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session
    def add(self, batch):
        self.session.add(batch)
    def get(self, reference):
        return self.session.query(model.Batch).filter_by(reference=reference).one()
```

**Ports and adapters + fakes for testing.** This is the canonical hexagonal example: "`AbstractRepository`
is the port, and `SqlAlchemyRepository` and `FakeRepository` are the adapters" (raw L1456). Because the
abstraction is a thin wrapper over a `set`, a `FakeRepository` is trivial — yielding a design heuristic
worth remembering: "Building fakes for your abstractions is an excellent way to get design feedback: if
it's hard to fake, the abstraction is probably too complicated" (raw L1444).

```python
class FakeRepository(AbstractRepository):
    def __init__(self, batches):
        self._batches = set(batches)
    def add(self, batch):
        self._batches.add(batch)
    def get(self, reference):
        return next(b for b in self._batches if b.reference == reference)
```

**Who commits?** A deliberate design decision surfaced by the tests: "We keep the `.commit()` outside of
the repository and make it the responsibility of the caller" (raw L1347). This is the seam that later
motivates the Unit of Work pattern, which owns transaction boundaries.

**When NOT to use it.** The pattern is not universal: "If your app is just a simple CRUD... wrapper around
a database, then you don't need a domain model or a repository" (raw L1477). "For simple cases, a
decoupled domain model is harder work than a simple ORM/ActiveRecord pattern" (raw L1473); the payoff
scales with complexity — "the more complex the domain, the more an investment in freeing yourself from
infrastructure concerns will pay off" (raw L1479). This mirrors Vernon's own caution above that the
Repository loses value where you are not really using [[aggregate|Aggregates]].

### Query design — one aggregate per query, and the `.seen` set

Later chapters add two Cosmic Python refinements. First, a query heuristic on *what a Repository may
return*. A `get_by_batchref` finder lets a `BatchQuantityChanged` handler load the owning `Product` from a
batch reference:

```python
def get_by_batchref(self, batchref) -> model.Product:
    product = self._get_by_batchref(batchref)
    if product:
        self.seen.add(product)
    return product
```

The boundary rule: "So long as our query is returning a single aggregate, we're not bending any rules. If
you find yourself writing complex queries on your repositories, you might want to consider a different
design. Methods like `get_most_popular_products` or `find_products_by_order_id` in particular would
definitely trigger our spidey sense." (raw L4605). `get(sku)` and `get_by_batchref(ref)` are fine because
each yields exactly one `Product`; a finder returning rankings or cross-aggregate joins signals that read
concerns are being pushed into the write-side repository — the fix is a dedicated read model / [[cqrs]]
(see [[use-case-optimal-query]] for Vernon's parallel warning). This keeps the Repository aligned with the
[[aggregate-consistency-boundary]]: one load hands back one aggregate, so each transaction touches one
aggregate.

Second, the `.seen` set is how [[domain-event|domain events]] escape the model without the model knowing
about dispatch. Every getter that returns an aggregate does `self.seen.add(product)`, so after commit the
[[unit-of-work]] can walk `products.seen`, collect the events each aggregate recorded, and hand them to the
[[message-bus]] — any aggregate the Repository loaded (not only ones explicitly `add`ed) can contribute
events. A Repository that forgets to register a loaded aggregate in `.seen` would silently swallow its
events.

### Swapping infrastructure — the payoff (Appendix C, CSVs)

Appendix C demonstrates *why* the abstraction earns its keep by satisfying a last-minute request — read
batches/orders from CSVs and write an allocations CSV instead of the Flask API — with no rewrite:
"Switching to CSVs will be a simple matter of writing a couple of new `Repository` and `UnitOfWork`
classes, and then we'll be able to reuse *all* of our logic from the domain layer and the service layer."
(raw L7246). A `CsvRepository` subclasses `AbstractRepository` and exposes the same `get`/`add`/`list`;
its private `_load()` reads two files, parses dates, reconstructs `Batch` aggregates and re-attaches
allocated lines — all hidden behind "the familiar `.list()` API, which provides the illusion of an
in-memory collection of domain objects" (raw L7361). The appendix first shows the naive alternative —
inline CSV reading in `main()` — and names its symptom: once existing allocations must also persist, "we
could keep hacking about and adding extra lines to that `load_batches` function… but we already have a
model for doing that! It's called our Repository and Unit of Work patterns." (raw L7352). Accreting
persistence/reconstruction glue in an entry-point script *is* a reimplementation of Repository + [[unit-of-work]].

### Data Mapper vs ActiveRecord — the concrete repo's shape (Appendix D, Django)

Re-implementing the same *abstract* repository against Django's ORM exposes a structural point a single
implementation hides: **the shape of a concrete repository depends on whether the ORM is a Data Mapper or
an ActiveRecord.** The seam is still dependency inversion — "we use dependency inversion. The ORM (Django)
depends on the model and not the other way around." (raw L7590). But with SQLAlchemy's *classical mapper*
(a Data Mapper) the domain object and the persisted row can be the *same* object; Django's ORM is an
**ActiveRecord** — the model class *is* a row — so "our ActiveRecord and our domain model can't be the same
object. Instead we have to build a manual translation layer behind the repository." (raw L7684). That means
hand-written `to_domain()` / `update_from_domain()` boilerplate, plus two wrinkles: **upsert differs by
kind** — "for value objects, `objects.get_or_create` can work, but for entities, you probably need an
explicit try-get/except" (raw L7584), because an [[entity]] has stable identity to match whereas a
[[value-object]] is defined by its attributes — and relationships need custom handling. The payoff is still
decoupling and fast in-memory unit tests; the cost is that Repository+UoW on Django "feel[s] like more
effort than Flask/SQLAlchemy" and is worth it mainly once complexity or slow tests justify it (raw L7704).
Coupling the domain model directly to the ActiveRecord instead is the [[orm-coupled-domain-model]]
anti-pattern.

## Failure modes

- **Providing a Repository per Entity instead of per Aggregate** — violates Evans' "provide repositories only for aggregates"; a symptom is Repositories for internal Aggregate parts that should be reached only through their [[aggregate]] root.
- **Leaking persistence into the interface** — e.g. `save()` methods, ORM types, or boolean "success" returns that actually depend on a later commit; the interface should read as a collection, not a database gateway.
- **Ad-hoc bare-Entity access** — skipping Aggregate boundaries undermines the transactional-consistency guarantees Repositories are meant to bracket.

## Related

[[collection-oriented-repository]] · [[persistence-oriented-repository]] · [[repository-only-persistence]] · [[use-case-optimal-query]] · [[transaction-management]] · [[repository-vs-dao]] · [[repository-type-hierarchies]] · [[testing-repositories]] · [[persistence-ignorance]] · [[aggregate]] · [[entity]] · [[factory]] · [[modules]] · [[dependency-inversion-principle]] · [[bounded-context]] · [[unit-of-work]] · [[message-bus]] · [[aggregate-consistency-boundary]] · [[ports-and-adapters]] · [[orm-coupled-domain-model]] · [[book-implementing-ddd-vaughn-vernon]], [[web-page-cosmic-python-book]] — source summaries.
