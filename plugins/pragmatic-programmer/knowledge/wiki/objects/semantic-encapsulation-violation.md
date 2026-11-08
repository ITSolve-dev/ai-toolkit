---
title: Semantic violations of encapsulation
category: objects
summary: "Caller code skips a documented call, borrows another class's constant, or keeps a reference because it knows what the other class does inside (skips `connect()` since `retrieve()` connects anyway), or a class demands an undocumented behaviour from its clients."
tags: [rule, encapsulation, coupling, contracts, class-interface]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

## Rule

Syntactic encapsulation is easy: declare internals private. Semantic encapsulation is much harder, and McConnell tells the reader to be very, very wary of violating it (p. 138). His examples of how a client violates it semantically:

- not calling class A's `InitializeOperations()`, because you know `PerformFirstOperation()` calls it automatically;
- not calling `database.Connect()` before `employee.Retrieve(database)`, because you know `Retrieve` connects if needed;
- not calling `Terminate()`, because you know `PerformFinalOperation()` already did;
- using a pointer or reference to object B, created by object A, after A goes out of scope, because you know A keeps B in static storage;
- using class B's `MAXIMUM_ELEMENTS` instead of class A's, because you know they are equal.

All of them share one problem: the client depends on the class's private implementation, not on its public interface. Whenever you look at a class's implementation to learn how to use it, you are programming not to the interface but through it, to the implementation (p. 138). McConnell's margin quotes P. J. Plauger: «Если для понимания того, что происходит, нужно увидеть реализацию, это не абстракция» (p. 138).

The class side of the same contract: **do not make assumptions about the class's clients.** A class should honour the contract stated by its interface and assume nothing about how it will or will not be used. McConnell's warning sign is a comment such as "initialise x, y and z to 1.0, because DerivedClass fails on 0.0": the class asks more of its clients than it should (p. 137).

Chapter 5 of the same book names the phenomenon semantic coupling (pp. 98-99; [[semantic-coupling]]).

## Sign in code

- A documented call, such as `connect`, `init`, `close` or `terminate`, is skipped, with a comment or commit note explaining that the other method already does it.
- A constant or limit of one class is used for a different class because the values happen to match.
- A reference returned by an object is kept beyond that object's lifetime, relying on how it stores the referent.
- A comment in a class tells callers to use particular values or a call order because of an internal or a subclass quirk.

This wiki assigns the neighbouring cases as follows: a documented call the caller skips, or another class's constant it borrows, because it knows the implementation belongs to [[semantic-encapsulation-violation]]; a reliance on runtime type to [[avoid-introspection-and-casting]]; on shared mutable state to [[global-data]]; a reliance on what the callee does with a value the caller passes belongs to [[semantic-coupling]]. A comment in a class that demands particular values or a call order from callers and gives an internal or subclass quirk as the reason is [[semantic-encapsulation-violation]]. A precondition on a value or on the object's state stated only in a comment, and a public `initialize` the class declares as required before its other methods, are [[semantic-interface-to-programmatic]]. An order between two calls stated only in a comment, with no state the callee could check, is [[temporal-coupling]].

## When not to apply

- The behaviour is part of the documented contract, for example "`retrieve` connects lazily". Relying on a stated guarantee is programming to the interface. The test is whether the fact is in the interface or only in the implementation. This limit is this wiki's own.
- Both sides are private parts of one class or module, which share the implementation by design. This limit is this wiki's own.

## Repair

- On the client side: make the calls the interface asks for, and use the constant that belongs to the class you are talking to.
- On the class side: either promise the behaviour in the interface (document it and keep it), or make the dependency impossible. Fail on a call without a connection, or remove the separate `init`. Making it impossible links to [[semantic-interface-to-programmatic]].
- For an assumption about clients: fix the class so it works with any input its interface admits, or state the requirement in the interface and check it.

## Before and after

```
// before: relies on retrieve() connecting internally
emp = employee.retrieve(db)
```

```
// after: follows the interface
db.connect()
emp = employee.retrieve(db)
// or, better: retrieve takes a ConnectedDb that cannot exist unconnected
```

## Related

- [[uniform-access]]
- [[mixed-abstraction-levels-in-interface]]

## Source

[[code-complete]], ch. 6.2, Russian edition, pp. 137-139 (p. 139 continues: programming through the interface destroys encapsulation; ask the class's author rather than read the implementation), and ch. 5, pp. 98-99, for semantic coupling. The quotation from Plauger was joined across a margin hyphen in raw ("ре-ализацию") and must be checked against the page image. The signs, the owner assignments, the limits and the repair are this wiki's own.
