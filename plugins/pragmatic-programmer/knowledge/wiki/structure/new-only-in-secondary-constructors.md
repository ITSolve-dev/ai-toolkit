---
title: "`new` only in secondary constructors"
category: structure
summary: "`new Collaborator()` inside a method body or the primary constructor hard-codes a dependency the caller cannot replace (e.g. a network call in every unit test)."
tags: [rule, dependency-injection, coupling, constructors, testability]
paradigm: oop
sources: [elegant-objects]
created: 2026-11-03
updated: 2026-11-07
---

*Elegant Objects* (section 3.6) reduces dependency injection and inversion of control to one rule: an object must not instantiate its collaborators where it likes. It takes them as constructor arguments and stores them in fields; the only place `new` may appear is a secondary constructor that supplies a default to the primary one (see [[one-primary-constructor]]).

## Rule

Paraphrased from pp. 189-194:

- `new Exchange()` inside `Cash.euro()` is a hard-coded dependency: `Cash` is tied to `Exchange` and the tie cannot be removed without editing `Cash` (p. 189). If `Cash` ships as a binary library, a user testing their own `print()` cannot stop `five.euro()` from calling the stock exchange over HTTP on every test run (p. 191).
- The root is the `new` operator: objects that may instantiate others wherever they please will do so (p. 191). With `new` forbidden in methods, an object can only receive collaborators through its constructor and encapsulate them; the dependency still exists, but «теперь зависимость контролируем мы, а не он» (p. 191).
- The rule: «не используйте оператор new нигде, кроме вторичных конструкторов» (p. 192). A secondary constructor may supply a default (`Cash(value)` calls `this(value, new NYSE())`), while the primary constructor takes every dependency (pp. 191-192). Restated: «Единственное законное место оператора new — вторичные конструкторы» (p. 194); the same passage says that `new` in methods or primary constructors is always a mistake (p. 194).
- When a method must produce new objects (a `Requests` stream whose `next()` returns a fresh `SimpleRequest` per call), the book calls that method a violation of the rule (p. 193). The creation is itself injected: `Requests` holds a `Mapping<String, Request>`, the secondary constructor supplies one that builds `SimpleRequest`, and a test can inject a mapping that returns something else (pp. 192-193).

## Sign in code

- `new X(...)` in a method body, where `X` is a collaborator the method calls (a service, a gateway, a clock, an exchange rate source) rather than a new instance of the method's own class built from this object's state.
- `new X(...)` in the constructor that assigns the fields (the primary one): built from none of that constructor's arguments, so there is no way to pass a different `X`, or wrapping an argument. The book moves the wrap into a secondary constructor (pp. 35-36, 194).

Not this page's sign: `new` in a constructor that only delegates to another constructor of the same class (`this(value, new NYSE())`), which is the book's sanctioned place.

This wiki assigns the neighbouring cases as follows. This page owns a collaborator built with `new` inside the class that uses it. A collaborator reached through a static call, a singleton accessor or a global is [[global-data]] or [[no-static-methods]]. A field or parameter typed by a concrete class is [[public-methods-implement-interfaces]]. Parsing, validation or I/O in a constructor is [[constructors-without-code]]. Whether the class constructed is a collaborator whose behaviour the constructing object calls, or a part it keeps as its own state, decides between [[creator]] and [[new-only-in-secondary-constructors]]: a collaborator built with `new` inside the class that uses it is [[new-only-in-secondary-constructors]]; where a part or record is constructed, and in which class, is [[creator]]. A plain `new` of one fixed class, with no choice and no setup, is [[creator]] where a part or record is constructed and [[new-only-in-secondary-constructors]] where a collaborator is. A choice among concrete classes, or many lines of construction logic, made in a domain class is [[factory-object-for-creation]].

## When not to apply

- **Small, simple classes using no expensive resource.** The book itself says the hard-coded `new` does not necessarily cause problems «при условии, что классы небольшие, простые и не задействуют дорогих ресурсов вроде сети, диска, базы данных и т. п.» (p. 189), and calls the problem insignificant when the class is small (p. 191). The book still recommends the rule everywhere; this wiki reports it only when the instantiated class reaches network, disk, database, the clock or randomness, directly or through its own collaborators.
- **Returning a new instance of the object's own class.** The book counts a method that returns a new object of another class as a violation (`Requests.next()`, p. 193) and repairs it by injecting a factory object (pp. 192-193). Its own immutable `DefaultCash.multiply` returns `new DefaultCash(...)` (p. 51), and from that this wiki reads a new instance of the class's own kind as exempt. The book does not state the exemption.
- **The composition root.** A commenter argues `new` belongs at the top level of the program, with the rest built by other objects (Bartosz Miera, p. 194). This wiki notes that the book's own construction of the object tree also has to happen somewhere; `main` or the entry point that assembles objects is not a violation.
- **A project using a DI container.** This wiki reads the container as playing the role of the secondary constructor; the primary-constructor half of the rule (every dependency is a parameter) still holds.

## Repair

1. Add the collaborator as a final field and a parameter of the primary constructor; replace `new X()` in the method with the field.
2. If callers relied on the default, add a secondary constructor that passes `new X()` to the primary one (p. 193).
3. If the method must create objects per call, inject a factory/mapping object and call it instead of `new` (pp. 193-195).

## Before and after

```
class Cash
  private final dollars
  Cash(dollars) -> this.dollars = dollars
  euro() -> return new HttpExchange().rate("USD", "EUR") * this.dollars   // HTTP call to the exchange
```

```
class Cash
  private final dollars
  private final exchange
  Cash(dollars) -> this(dollars, new NyseExchange())   // secondary: the default
  Cash(dollars, exchange) ->                           // primary: takes everything
    this.dollars = dollars
    this.exchange = exchange
  euro() -> return this.exchange.rate("USD", "EUR") * this.dollars

// in a test
new Cash(5, new Exchange.Fake(1.15)).euro()
```

The "before" reaches a remote resource through `HttpExchange`, so the book's small-class limit does not exempt it. The "after" has `new` only in the secondary constructor; the test passes a fake shipped with the interface, per [[prefer-fakes-over-mocks]].

## Source

- [[elegant-objects]], section 3.6, pp. 189-194: the hard-coded dependency (p. 189), the binary-library and unit-test scenario (p. 191), injection through the constructor (p. 191), secondary constructors and the rule (pp. 191-192), the `Requests`/`Mapping` case (pp. 192-193), the restatement (p. 194), the composition-root comment (p. 194, a reader, not the author). Section 1.3, pp. 35-36, for the wrap moved into a secondary constructor; section 2.3, p. 51, for `DefaultCash.multiply`. The quotations on pp. 192 and 194 were checked against the page image; the others are transcribed from a noisy OCR layer.
- This wiki's own: the exemption for a new instance of the class's own kind, the DI-container and composition-root limits, the signs' wording, the assignment of neighbouring cases, and the pseudocode pair.
