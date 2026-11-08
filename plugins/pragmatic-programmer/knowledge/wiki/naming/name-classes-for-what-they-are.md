---
title: Name a class for what its objects are
category: naming
summary: "A class name ends in -er or -or (Manager, Handler, Helper, Validator, Formatter, Sorter), in -able, or in Util/Utils, and names a job done to data rather than the thing its objects encapsulate."
tags: [rule, naming, class-names, object-thinking]
paradigm: oop
sources: [elegant-objects]
created: 2026-11-02
updated: 2026-11-06
---

*Elegant Objects* holds that a class name must say what its objects are, not what they do. A name built from a job, typically ending in -er, marks a set of procedures rather than an object. The book's statement is «Имя класса не должно происходить от названия функциональности, предоставляемой его объектами!» (p. 21).

## Rule

Look at what the objects of the class encapsulate and name that (p. 23). The book's examples (pp. 20-24):

- `CashFormatter`, which holds a dollar amount and formats it as text, becomes `Cash`, `USDCash` or `CashInUSD`, and its method `format()` becomes `usd()` (p. 21).
- A class that picks primes out of a list is not `Primer`, `PrimeFinder`, `PrimeChooser` or `PrimeHelper`, but `PrimeNumbers`, which behaves as a list showing only primes (p. 23).
- The book lists as bad: Manager, Controller, Helper, Handler, Writer, Reader, Converter, Validator (with -or equally harmful), Router, Dispatcher, Observer, Listener, Sorter, Encoder, Decoder. It offers as counterexamples: Target, EncodedText, DecodedData, Content, SortedLines, ValidPage, Source (pp. 21-22).
- Names ending in Util or Utils are another bad case: utility classes, which the book treats in a later section (p. 24).

In the reader discussion the author extends the rule. `ILogger` should become `ILog`, since a log is a record of events (p. 25). Observer and Listener become `EventTarget` and `EventSource` (pp. 25-27). Suffixes in -able (`Serializable`, `Cloneable`, `Cacheable`, `Printable`) are no better than -er, because `Printable` says the object can be printed but nothing about what it is. The author grants that they are technically convenient and still advises against them (p. 26).

The reasoning under the rule is [[object-as-representative]]. A name ending in -er tells the reader that the thing is not an object but a set of procedures that manipulate some data, a procedural habit carried over from C, COBOL and BASIC (p. 22). A reader asked what to do if they really want a class that is a set of functions. The answer was that they want a library of procedures, not a class (p. 27).

## Sign in code

- A class or interface name ends in a doer suffix (-er, -or) or in -able, -Util or -Utils, and its body holds a method named for a processing verb that either takes the data in as an argument (`PrimeFinder.find(numbers)`) or transforms a field the constructor stored (`CashFormatter.format()`).
- A class is named for a verb of processing (Finder, Chooser, Helper, Processor) while its constructor stores a collection or a value, and its methods only transform it.

This page owns the name of a class or an interface. A class whose name ends in -er or names a job is [[name-classes-for-what-they-are]], which owns the name; [[class-with-only-data-or-only-behaviour]] owns the absence of data. A name joined with "and" is a prompt to look for clusters on [[class-interface-coherent-abstraction]]. The name of a method belongs to [[builder-and-manipulator-names]] or [[name-by-role]], as those pages divide it: a method that returns a value and is named with a verb belongs to [[builder-and-manipulator-names]], whose repair names what comes back by its role; a method that returns nothing and is named for its mechanism belongs to [[name-by-role]]. A returning method named with a noun for its mechanism belongs to [[name-by-role]] unless it is a general-purpose utility. The name of a variable or a parameter belongs to [[name-by-role]]. A class name that is vague and is explained by a doc comment on the class is [[tests-instead-of-documentation]], whose repair renames it by this page.

## When not to apply

- The book exempts nouns whose -er no longer denotes a doer, such as `computer` and `user`: a user is a person interacting with the system, not something that uses (p. 22). There are few such exceptions, the book adds.
- This wiki adds that a name fixed by a framework or a protocol, such as a controller class the framework discovers by suffix or an interface the platform defines (`Serializable`, `Runnable`), keeps its name. Renaming it breaks the binding and gains nothing.
- This wiki adds that the project's established naming convention overrides this page where the codebase is consistently built of services and handlers, and the change is not part of a deliberate move to this book's style. See [[follow-local-naming-culture]]. A single class renamed against that convention leaves one object among a hundred procedures.
- This wiki adds that renaming alone does not repair the design. A class renamed from `PrimeFinder` to `PrimeNumbers` that still exposes `find(list)` is the same procedure under a noun. Only the repair below, which changes the shape of the class, satisfies the rule.

## Repair

1. Find what the objects encapsulate: the field or fields the constructor stores.
2. Move the data the procedure takes as an argument into the constructor, so the object holds it.
3. Make the result something the object is or offers: let it behave as the collection, value or document it represents (`PrimeNumbers` iterates as a list).
4. Name the class for that thing, and name its methods by [[builder-and-manipulator-names]].

## Before and after

```
class PrimeFinder:
    method find(numbers): list
        result = []
        for n in numbers:
            if is_prime(n): result.append(n)
        return result

primes = PrimeFinder().find(numbers)
```

```
class PrimeNumbers implements Iterable:
    constructor(origin: Iterable)
        this.origin = origin
    method each(visit)
        for n in this.origin:
            if is_prime(n): visit(n)

primes = PrimeNumbers(numbers)
```

## Source

[[elegant-objects]]: pp. 20-28, including the reader discussion on pp. 25-28. This wiki's own: the signs as worded, the division of method names between [[builder-and-manipulator-names]] and [[name-by-role]], the framework and convention limits, the limit that a rename alone is no repair, the repair steps and the pseudocode, which follows the book's Ruby `PrimeNumbers` (p. 23) in shape.
