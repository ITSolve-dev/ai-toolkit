---
title: Class invariant
category: types-and-state
summary: "A field bound by a rule is public or has a plain setter, or a getter hands out the mutable collection the rule depends on. A method that can throw between two writes is failure-atomicity."
tags: [rule, invariants, encapsulation, collections, aliasing]
paradigm: any
sources: [pragmatic-programmer, code-complete, object-oriented-thought-process]
created: 2026-11-01
updated: 2026-11-07
---

An invariant is the condition a class guarantees to everyone calling it, as part of [[design-by-contract]]. The book notes that the name comes from Eiffel being object-oriented and that the idea is about state generally: functional code that passes state in and receives it updated benefits equally (p. 144).

## Rule

The invariant holds whenever control returns to a caller. It may lapse during a routine's internal work and must be true by the time the routine exits (p. 141). For that to be possible, «класс не может предоставить неограниченный доступ для записи к любому члену данных, принимающему участие в инварианте» (p. 141).

*Code Complete* lists the collection case among data-level refactorings as *encapsulate collection*: if a class returns a collection, several instances of it in play can cause synchronisation problems, so have the class return a read-only collection and provide routines to add and remove elements (p. 560).

Weisfeld's *The Object-Oriented Thought Process* shows the guarded mutator from the other side: a `setAge()` that refuses a value of 0 or less, and setters generally used to ensure some level of data integrity (p. 95). His own `setName` only assigns (p. 94); this wiki reads it as the plain setter of this page's first sign once a rule binds the field. How a no-check setter is judged on a class with no such rule is [[no-getters-and-setters]].

## Sign in code

- A field bound by a rule is public or has a plain setter: `discount` under a ceiling, `enrolled` under `capacity`, `balance` beside `overdraft_limit`.
- A getter hands out the mutable internal collection an invariant depends on, and a caller adds to or removes from the result (`course.students().add(s)` bypassing a capacity check).

This wiki assigns the neighbouring case as follows. A getter that hands out the mutable collection a rule between fields depends on is [[class-invariant]]; a returned internal collection that callers mutate, or a setter that stores the caller's collection, is [[encapsulate-collection]]; a returned internal collection that callers only loop over, where the concern is dependence on its storage type, is [[iterator]]. A method that writes a field of the receiver and can then throw or return before its remaining writes belongs to [[failure-atomicity]]; a field bound by a rule and exposed to a plain setter or a public write: on an entity under a mutable-entity convention [[class-invariant]], on a value whose state is its identity [[immutable-objects]]. A field that can be computed from others, such as `total` beside `lines`, is [[stored-derived-data]], which owns that sign and comes first, because removing the field removes the invariant. This page covers such a field only as a cache that survives there. A public field with no rule binding it is [[uniform-access]], and a read, a decision and a write back to the same object with no rule binding the field is [[tell-dont-ask]]. Where a rule binds the field, this page comes first, and the repair is the method on that page. Against [[immutable-objects]], this wiki resolves the setting as that page does: for a value whose state is its identity (money, dates, ranges, identifiers, anything compared by value, used as a key or shared between threads), [[immutable-objects]] applies. For an entity in a codebase whose convention models entities as mutable objects behind guarded mutators, a mutator that keeps a stated invariant is judged by [[class-invariant]], and [[immutable-objects]] does not fire on it alone.

## When not to apply

- A plain data record whose fields have no rule to protect.
- A getter that returns an immutable collection or a fresh copy, so callers cannot affect the owner's state. This limit is this wiki's own.
- The state in the middle of a routine: the book allows the lapse (p. 141).
- A private helper called only during an update, which need not restore the invariant on its own exit.
- A setter required by a persistence or serialisation layer, where the invariant is checked at the boundary that hands the object to the rest of the program.

## Repair

Remove the direct write. Replace it with an operation that updates all related fields together, return copies or read-only views with `add`/`remove` operations that keep the rule (p. 560), and order the writes so no exit falls between them. Where the invariant is checked with assertions, the book warns that the check must be called by hand before each exit (p. 145).

## Before and after

```
# before
class Account:
    public balance
    public overdraft_limit

account.balance = account.balance - 500   # nothing stops balance < -overdraft_limit
```

```
# after
class Account:
    # invariant: balance >= -overdraft_limit
    private balance
    private overdraft_limit

    method withdraw(amount):
        if balance - amount < -overdraft_limit: raise OverdraftExceeded
        balance = balance - amount

    method current_balance():
        return balance
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, [[pragmatic-programmer]]: pp. 141, 144, 145 for the rule, the third limit and the extension beyond classes. The signs, the assignment of the neighbouring case (including the split with [[failure-atomicity]] and the per-setting resolution with [[immutable-objects]]), the other limits (the persistence-layer setter included), the rest of the repair and the example are this wiki's own.

McConnell, *Code Complete*, 2nd ed., Russian edition, [[code-complete]], section 24.3, p. 560: the encapsulate-collection refactoring and its reason. The caller-mutation wording of the second sign and the copy limit are this wiki's own.

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]], pp. 94-95: `setName` and the refusing `setAge`. The reading of `setName` as this page's sign is this wiki's own.
