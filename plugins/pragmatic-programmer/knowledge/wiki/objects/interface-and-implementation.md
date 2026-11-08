---
title: Interface and implementation
category: objects
summary: "Concept: a class's interface is everything a caller can depend on (public signatures, return values and observable behaviour); everything else is implementation. A change a caller can observe is an interface change even when no signature moved, and a public signature naming a storage format or vendor type makes every implementation change an interface change."
tags: [concept, interface, encapsulation, information-hiding, data-hiding]
paradigm: oop
sources: [object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

Weisfeld builds encapsulation on one split. A class has an **interface**, through which every behaviour of its objects is invoked, and an **implementation**, which its users neither see nor depend on (ch. 1, p. 37). He calls separating the two one of the keys to good design (ch. 2, p. 52). The "users" of a class are the programmers who call it, not the end users of the application (p. 54). This page defines the split; the rules that keep it are on [[minimize-member-accessibility]], [[uniform-access]] and [[hide-third-party-apis]]. The wider ideas it sits in are [[abstraction]] and [[information-hiding]].

## What is in the interface

- **The public methods, never the attributes.** The interface should describe completely how users interact with the class, and in most object-oriented languages it is the set of public methods (p. 37). Attributes are not part of it: «Объявление атрибута как public нарушает концепцию скрытия данных» (p. 37).
- **The signature and the returned value.** To use a method a caller needs its name, its parameters and its return type (p. 30). The book separates a class's interface (its public methods) from a method's interface, its signature (p. 37). It also states that the interface includes the calling syntax and the values returned, and that if these hold, users do not care whether the implementation changed (p. 54).
- **Observable behaviour.** In the car example the engine is implementation and the steering wheel is interface, yet an engine change that causes a noticeable loss of power «в действительности будет изменением интерфейса» (p. 53). This wiki reads that as follows: the contract is what a caller can observe, not only what a compiler checks. Timing, ordering, error behaviour and units become part of it once callers rely on them.
- **A specification both sides honour.** A coal station and a nuclear station can be swapped behind the socket only if both deliver what the socket specifies; one giving alternating current and the other direct current breaks the toaster (pp. 38, 55).

Only what other objects need is shown: «Детали, не относящиеся к использованию объекта, должны быть скрыты от всех других объектов» (p. 36).

## What is implementation

Technically everything that is not the public interface is implementation (p. 65): attributes, private methods and their signatures, and the code inside public methods. Callers see a public method's calling structure, not its body (p. 66). The book's examples are a public `getSquare` calling a private `calculateSquare` (pp. 39-40), and a public `changePassword()` calling a private encryption method (p. 66). It adds that although the interface is how users see an object, the implementation is the object's real substance, because it holds the code that describes the object's state (p. 66).

## Why the split pays

Users do not care how a result is computed as long as it is right, so the implementation can change without touching their code (p. 38). In `IntSquare`, replacing hand-written multiplication with a library power function changes only the private method (pp. 39-40). The same goes for data: it can move from a file to a database without users changing any code (p. 40). In the `DataBaseReader` example the engine moves from Oracle to SQL Anywhere overnight, only the body of `open()` changes, and «не понадобилось бы изменять ни одной строки кода приложения» (p. 59).

The book attaches a proviso to the `myObject`/`Math` example: the sum's computation can change without changing `myObject`, «при условии, что средства для извлечения значения суммы останутся прежними» (p. 26). This wiki reads the proviso as the cost side: stability lasts only while the interface itself stays put, so each public member is a commitment that is expensive to take back. That reading is why [[minimize-member-accessibility]] starts from the smallest interface.

## Failure modes

The book warns that object-oriented classes can be designed badly, with their attributes left unrestricted: «вы можете создать плохой код с той же легкостью» as with any other method (p. 25). This wiki adds two failure modes:

- **Implementation leaking into the signature.** A public signature that names an implementation detail, such as a vendor type, a storage format or an internal collection, turns every implementation change into an interface change. For a vendor's types the owner is [[hide-third-party-apis]]; for storage-shaped names, [[storage-independent-names]]; for an internal collection, [[iterator]].
- **A "compatible" change that is not.** Keeping every signature identical while changing observable behaviour still breaks callers (p. 53). A reviewer who checks only signatures misses it; [[break-the-build-on-interface-change]] owns that shape.

## Related

[[abstraction]], [[information-hiding]], [[uniform-access]], [[minimize-member-accessibility]], [[abstract-intent-revealing-interface]], [[hide-third-party-apis]], [[polymorphism-or-type-switch]].

## Source

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]]: ch. 1, pp. 25-26, 30, 36-40; ch. 2, pp. 52-55, 59, 65-66. The quotations were checked against `raw/`, whose text layer is clean. This wiki's own: the extension of the contract to timing, ordering, errors and units, the reading of the p. 26 proviso as a cost, both failure modes and their owner pages.
