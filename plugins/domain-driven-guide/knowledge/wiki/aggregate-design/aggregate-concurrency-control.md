---
title: Aggregate Concurrency Control
category: aggregate-design
summary: Enforcing an aggregate's consistency boundary against concurrent writers using optimistic locking (a version number on the aggregate root) or pessimistic locking (SELECT FOR UPDATE), with the trade-offs of each.
tags: [technique, concurrency, optimistic-locking, pessimistic-locking, version-number, aggregate, consistency-boundary, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Aggregate Concurrency Control

An [[aggregate]] defines a [[consistency-boundary]], but the boundary only holds if the database actually prevents two concurrent writers from committing conflicting changes to the *same* aggregate — while still allowing writers on *different* aggregates to proceed in parallel. The goal is a lock scoped to one aggregate (e.g. the rows for a single SKU), not the whole `batches` table.

> Requirements here "vary a lot from project to project. You shouldn't expect to be able to copy and paste code from here into production." (raw L3472)

## Optimistic locking with a version number

The primary technique is to put a single **version number** attribute on the aggregate root that acts as a marker for "the whole state change is complete", and make concurrent workers fight over it. Two transactions that both read `Product` at `version=3`, both call `Product.allocate()`, and both try to commit `version=4` will collide — the database lets only one succeed and rejects the other.

The number itself is incidental:

> "the number isn't important. What's important is that the `Product` database row is modified whenever we make a change to the `Product` aggregate. The version number is a simple, human-comprehensible way to model a thing that changes on every write, but it could equally be a random UUID every time." (raw L3538)

### Where does the version number live? Three options

The book weighs three placements (raw L3500–3516):

1. **In the domain** — add `version_number` to the `Product` constructor and have `Product.allocate()` increment it.
2. **In the service layer** — the version isn't strictly a domain concern; the service layer increments it before `commit()`.
3. **In the UoW/repository "by magic"** — the [[unit-of-work]]/repository increments on commit for any product it knows about.

Option 3 is rejected because it must assume *all* retrieved products changed, incrementing versions needlessly. Option 2 mixes state-mutation responsibility across service and domain layers, so it's "a little messy." The chosen trade-off is **Option 1 — in the domain**, even though the version isn't strictly domain logic, because it keeps mutation in one place:

```python
class Product:
    def __init__(self, sku, batches, version_number: int = 0):
        self.sku = sku
        self.batches = batches
        self.version_number = version_number
    def allocate(self, line: OrderLine) -> str:
        try:
            batch = next(b for b in sorted(self.batches) if b.can_allocate(line))
            batch.allocate(line)
            self.version_number += 1
            return batch.reference
        except StopIteration:
            raise OutOfStock(f"Out of stock for sku {line.sku}")
```

> "Version numbers are just one way to implement optimistic locking. You could achieve the same thing by setting the Postgres transaction isolation level to `SERIALIZABLE`, but that often comes at a severe performance cost. Version numbers also make implicit concepts explicit." (raw L3492)

### Enforcing it at the DB level

One concrete enforcement is raising the transaction isolation level, e.g. `isolation_level="REPEATABLE READ"` on the SQLAlchemy session. Under the concurrency ordering `read1, read2, write1, write2`, the second writer gets `could not serialize access due to concurrent update`, the version increments only once, and only one allocation gets through — verified by a test that spins up two threads doing a deliberately slow (sleep-injected) allocation.

## Pessimistic locking with SELECT FOR UPDATE

The alternative is pessimistic concurrency control via `SELECT FOR UPDATE`, expressed in SQLAlchemy as `.with_for_update()` in the repository's `get()`:

> "`SELECT FOR UPDATE` is a way of picking a row or rows to use as a lock... If two transactions both try to `SELECT FOR UPDATE` a row at the same time, one will win, and the other will wait until the lock is released. So this is an example of pessimistic concurrency control." (raw L3627)

This changes the concurrency pattern from `read1, read2, write1, write2 (fail)` to `read1, write1, read2, write2 (succeed)` — the second transaction blocks on the read rather than failing at the write.

## Optimistic vs. pessimistic — the trade-off

- **Optimistic (version numbers / REPEATABLE READ)**: writers don't block; conflicts are detected at commit and the loser must retry. Best when contention is low; wasted work when it is high. Makes the "something changed" concept explicit.
- **Pessimistic (SELECT FOR UPDATE)**: the second writer waits instead of failing, so no retry logic — at the cost of holding locks and reduced parallelism. Better under high contention.

The book calls the underlying hazard the **"read-modify-write" failure mode** (two transactions read the same state, both modify, both write) and declines to fully adjudicate the trade-offs — the right choice "vary[s] a lot based on business circumstances and storage technology choices" (raw L3663). A concurrency test like the one above lets you specify the behavior you want and run performance experiments.

## Failure modes

- **No write marker on the root**: if a change touches only inner rows and never modifies the aggregate root row, concurrent updates aren't detected and the [[consistency-boundary]] silently leaks.
- **Version-bump in the wrong layer** (Options 2/3): scatters mutation responsibility or bumps versions for unchanged aggregates.
- **Reaching for `SERIALIZABLE` everywhere**: correct but often severe performance cost versus a targeted version number or `FOR UPDATE`.

## Related

[[aggregate]] · [[consistency-boundary]] · [[invariants-and-constraints]] · [[unit-of-work]] · [[repository]] · [[aggregate-optimistic-concurrency]] — Vernon's parallel treatment of where to place the version.
