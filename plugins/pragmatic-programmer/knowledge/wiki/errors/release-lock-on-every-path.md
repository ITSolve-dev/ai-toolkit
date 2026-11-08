---
title: Release a lock on every path
category: errors
summary: "`lock()` and `unlock()` as plain statements in one body with a call that can raise, or a return, between them: an exception or early return leaves the lock held and later callers hang."
tags: [rule, concurrency, locking, resource-release]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

A lock released by a statement at the end of a block is released only if control reaches that statement. Every other exit leaves it held, and the failure shows up later and elsewhere, as a hang. This is the lock case of [[exception-safe-release]]; it gets its own page because the failure is a hang in other callers, and because releasing has a cost of its own.

## Rule

The book's listing guards a method with lock and unlock statements, and then notes that if an inner call raises, «семафор так и не будет разблокирован, и весь последующий доступ к прилавку с пирогом зависнет на неопределенное время» (p. 223). Release therefore goes in a block that always runs. The book says the mistake is common enough that many languages provide libraries which handle it automatically, through a form that takes the guarded code as a block (p. 223).

This wiki adds a second exit. The same listing, as extracted, has its `return` inside the guarded region and the unlock after it, so on this wiki's reading the ordinary path skips the release as well, not only the exceptional one. The book names only the exception.

## Sign in code

- `lock()` and `unlock()` as separate statements in one body, with a call between them and no `finally`, `ensure`, or scoped form. The book shows this shape.
- A `return`, `break` or `continue` between them. This shape is this wiki's own.
- An `unlock` as the last line of a function that returns earlier. This shape is this wiki's own.

This wiki assigns the neighbouring case as follows. This page owns a lock that may stay held. Callers locking around another object's data is [[lock-belongs-to-the-resource]], whose repair moves the lock and uses the scoped form in its third step, so that page alone is reported when both fire.

## When not to apply

These limits are this wiki's own.

- Nothing between lock and unlock can raise or exit. Even so, the scoped form costs little and survives later edits, so this is a reason not to report, not a reason to prefer the plain form.
- The lock is handed over deliberately, taken in one method and released in another, so it cannot be scoped. The hand-over should then be stated in the code.

## Repair

Use the language's scoped form, or a block that always runs. The book shows both (p. 223).

This wiki adds a check the book does not make: releasing on failure exposes whatever the guarded code left behind. If an exception can land between two updates, a waiting caller now sees half-applied state. Keep the updates after the last thing that can fail, or restore on the failure path.

## Before and after

```
guard.lock()
if queue.size > 0:
    audit(queue.peek())      // may raise: guard stays held
    return queue.pop()       // returns past the unlock
guard.unlock()
return none
```

```
guard.protect:
    if queue.size > 0:
        audit(queue.peek())
        return queue.pop()
    return none
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020, see [[pragmatic-programmer]]: the exception case and both fixes, p. 223.

This wiki's own: the reading that a `return` also skips the release, the shapes marked as its own, the assignment of the neighbouring case, `## When not to apply`, and the check on half-applied state. The pseudocode is this wiki's own. Related: [[lock-belongs-to-the-resource]].
