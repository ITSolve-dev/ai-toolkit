---
title: Check-then-act must be atomic
category: types-and-state
summary: "`if resource.count > 0` followed by a separate `resource.take()`, or read-modify-write across two calls, on something concurrent code reaches: the value can change between the check and the act."
tags: [rule, concurrency, atomicity, race-condition]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

A decision taken from a read, and the update that decision justifies, have to be one indivisible step. Otherwise two actors can both pass the check and both act on it.

## Rule

The book's case is two waiters serving one remaining slice of pie: each reads a count of one, each promises the slice, and one then fails and has to apologise. Replace the display case with a joint bank account and the waiters with card terminals and the same thing happens (pp. 219-220). The cause: «извлечение и обновление подсчета кусков пирога не является атомарной операцией, поскольку базовое значение может измениться посредине данной операции» (p. 221).

The general form of the rule, that any check and the act resting on it must be one operation, is this wiki's reading of that case. It adds that in the book's sequence the promise to the customer comes between check and take, so an externally visible commitment is made on a stale view. That commitment is what cannot be taken back.

## Sign in code

The book shows the first shape; the others are this wiki's own, and all need code that can run concurrently.

- `if resource.has_some()` followed by a separate `resource.take()` on a shared resource.
- Read-modify-write across two calls: `x = store.get(); store.set(x + 1)`.
- `if not exists(path): create(path)`.
- `if account.balance >= amount: account.balance -= amount`.
- Any step with a side effect placed between the check and the update.

Whether the code runs concurrently may not be visible from the function. [[shared-state-is-incorrect-state]] says what to report in that case. With no concurrent reach at all, `if account.balance >= amount: account.balance -= amount` is [[tell-dont-ask]].

## When not to apply

These limits are this wiki's own; the book does not state any.

- Only one piece of code can reach the resource.
- The check is an early rejection and an atomic operation repeats it behind the scenes, so losing the race is handled.
- The result is advisory, such as a displayed count, and nothing is committed on it.

## Repair

The book's repair is to change the API so the check and the take happen in a single call on the resource, which returns the item or nothing (p. 222). The caller stops looking at the count. That call must itself be protected: moving access to one place does not make it atomic, as [[lock-belongs-to-the-resource]] explains (p. 223).

This wiki adds that where the storage offers a conditional update or compare-and-swap, that primitive serves as the single call.

## Before and after

```
if account.balance >= amount:
    notify_payee(amount)
    account.balance -= amount
    transfer(amount)
```

```
if account.withdraw_if_covered(amount):   // check and debit are one guarded call
    notify_payee(amount)
    transfer(amount)
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020, see [[pragmatic-programmer]]: the restaurant and bank cases, pp. 219-221; the combined API call, p. 222; its need for protection, p. 223.

This wiki's own: the rule in its general form, the remark on the promise, the shapes other than the first under `## Sign in code`, the assignment against [[tell-dont-ask]], all of `## When not to apply`, and the mention of conditional update and compare-and-swap. The pseudocode is this wiki's own.
