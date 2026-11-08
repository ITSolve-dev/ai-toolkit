---
title: Make interfaces programmatic rather than semantic
category: objects
summary: "A precondition on a value or state of an interface lives only in a comment ('x must be initialised first', 'pass a non-empty list'), or a class has a public initialize() its other methods need first, with no type, constructor or assertion enforcing it."
tags: [rule, class-interface, assertions, contracts, temporal-coupling]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

## Rule

Every interface has a programmatic part, made of the types and other attributes a compiler can check, and a semantic part, made of the assumptions about its use that a compiler cannot check. McConnell's examples are that method A must be called before method B, and that method A fails if data item 1 passed to it was not initialised first. The semantic part should be documented in comments, but interfaces should depend on documentation as little as possible: «Любой аспект интерфейса, который не может быть проверен компилятором, является потенциальным источником ошибок» (p. 134). His advice is to convert semantic elements into programmatic ones, by assertions or other means.

## Sign in code

- A doc comment or comment states a precondition on a value or on the object's state ("only valid after `connect()`", "pass a non-empty list") and nothing in the code checks it.
- An object can be constructed in a state where some of its public methods are not yet legal, such as a two-phase `new` + `initialize`, declared by the class.
- A parameter typed as a general primitive (string, int) carries a constraint stated only in prose ("must be an ISO country code").

This wiki assigns the neighbouring cases as follows. This page owns the class side: what the interface declares and fails to enforce. An order between calls on one object, stated only in a comment, where that object's own state could tell whether the first call happened, is [[semantic-interface-to-programmatic]]; an order across objects, or one the callee holds no state for, is [[temporal-coupling]]. Setters called in sequence at a call site after an empty constructor are [[temporal-coupling]]. A body that relies on an unstated condition it then indexes, divides or dereferences is [[state-the-contract]]. A caller that skips a documented call because it knows the implementation is [[semantic-encapsulation-violation]]. A comment in a class that demands particular values or a call order from callers and gives an internal or subclass quirk as the reason is [[semantic-encapsulation-violation]].

## When not to apply

- Checking a condition costs more than it protects on a hot path. Then keep the assertion where the build allows it and document the rest. This limit is this wiki's own.
- Some semantics cannot be made programmatic in the language at hand, such as performance or thread-safety guarantees. A comment is then the right and only form. The book allows for this: the semantic interface should still be documented (p. 134).
- A framework or the project's convention requires a no-argument constructor plus a lifecycle or `initialize` hook (serialization, dependency-injection containers, object-relational mappers). Then enforce the precondition with an entry assertion instead of splitting the type. This limit is this wiki's own.

## Repair

This wiki orders the repairs, preferring:

1. A **type or constructor** that makes the illegal state impossible: construct already initialised, or return a connected object from `connect()` and give the unconnected one no `retrieve`.
2. An **assertion or guard** at the method's entry that fails loudly when the precondition is not met.
3. A **comment**, only for what cannot be checked.

Options 1 and 3 are this wiki's elaboration. The book names assertions or other means.

## Before and after

```
// before
// NOTE: open() must succeed before read()
class Reader
  open(); read()
```

```
// after
class Reader
  static open(path) -> OpenReader
class OpenReader
  read()
```

## Related

- [[design-by-contract]]
- [[class-interface-coherent-abstraction]]

## Source

[[code-complete]], ch. 6.2, Russian edition, p. 134. The quotation was joined across a line-break hyphen in raw ("оши-бок") and must be checked against the page image. The repair order, the signs, the owner assignment and the limits are this wiki's own.
