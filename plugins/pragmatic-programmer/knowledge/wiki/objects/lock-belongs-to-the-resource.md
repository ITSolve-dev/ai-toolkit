---
title: The lock belongs to the resource
category: objects
summary: "Callers acquire and release a lock around access to an object, the lock sits beside the data rather than inside it, or the same lock/unlock pair repeats at several call sites: one forgotten caller breaks the protection."
tags: [rule, concurrency, encapsulation, locking]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

A guard kept by convention protects only as long as every caller remembers it. Moving the guard into the resource makes it a property of the object rather than a habit of its users.

## Rule

A semaphore is a thing only one party can hold at a time (p. 221). The book's main objection to using one from the outside is that «такой подход оказывается работоспособным лишь в том случае, если все, кто имеет доступ к прилавку-витрине, соглашаются на условие пользоваться семафором» (p. 222). One developer who writes code that ignores the convention brings the mess back (p. 222).

The book locates the flaw in the design: «ответственность за защиту доступа к прилавку с пирогом возлагается на тех, кто им пользуется» (p. 222). The remedy is to centralise control in the resource, changing its API so one call does the whole job (p. 222).

The book then corrects a typical misconception. Having one entry point is not protection, because the method «все равно может быть вызван из нескольких одновременно выполняющихся потоков» (p. 223), so the lock moves inside it rather than disappearing.

## Sign in code

The shapes are this wiki's own, drawn from the book's listings.

- `lock.acquire()` at a call site, around access to another object.
- The same acquire/release pair at two or more call sites for the same data.
- A lock declared next to the data, as a sibling global or a separate field that callers reach.
- A public field, or a getter returning a mutable collection, on an object whose other accessors are guarded.
- A single access method with no guard in its body, on an object that a thread start, a task spawn or a shared handle in view reaches from more than one thread.

This wiki assigns the neighbouring cases as follows. This page owns who holds the lock, and where both fire it is the one reported, since its third repair step covers [[release-lock-on-every-path]]. A held section that makes an outgoing call or spans more than this object is the candidate on [[actor-model]], because moving the lock cannot shorten it.

## When not to apply

These limits are this wiki's own.

- The critical section spans several resources, so no single one can own it. See [[composite-resource]].
- The code is a private helper called only while the class's guard is already held.
- Nothing in view hands the object to a second thread or owner.
- The cost: the book's move means the API grows a method for each combined operation (p. 222). This wiki adds that the guard is held for everything that method calls. In the book's listing that includes a sales-data update (p. 223), so a slow or re-entrant call inside the guard blocks every other user.

## Repair

1. Make the data private to the resource.
2. Add a method for each operation callers were composing under the lock, with check and update inside it, as in [[check-then-act-must-be-atomic]].
3. Put the guard inside those methods, in a form that releases on every path: [[release-lock-on-every-path]].
4. Delete the lock from the callers.

Steps 1 to 3 follow the book's sequence on pp. 222-223. The numbering and step 4 are this wiki's own.

## Before and after

```
// caller A
accounts_lock.acquire()
account.balance -= amount
accounts_lock.release()

// caller B, written later
account.balance += refund     // no lock: the protection is gone
```

```
class Account:
    private balance
    private guard

    method debit(amount):
        guard.protect:
            balance -= amount

    method credit(amount):
        guard.protect:
            balance += amount

// callers
account.debit(amount)
account.credit(refund)
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020, see [[pragmatic-programmer]]: semaphores, p. 221; the convention problem and the central API, p. 222; the misconception, p. 223.

This wiki's own: `## Sign in code`, `## When not to apply` except the cited API growth, and step 4 of `## Repair`. The pseudocode is this wiki's own.
