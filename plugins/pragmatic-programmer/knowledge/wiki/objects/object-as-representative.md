---
title: Object as representative, not conduit
category: objects
summary: "A class whose objects only move data through themselves: its methods are procedures over fields that callers pass in or read out. An object should stand for the data it encapsulates and decide for itself how to answer requests."
tags: [concept, encapsulation, responsibilities, object-thinking]
paradigm: oop
sources: [elegant-objects]
created: 2026-11-02
updated: 2026-11-03
---

*Elegant Objects* rests its first chapter on one distinction. An object is a representative (представитель) of the data it encapsulates. It is not a conduit or adapter (переходник) between the outside world and its internal state, and it is not a set of procedures for manipulating encapsulated data (p. 22). The book's formula is «Объекты должны быть представителями, а не переходниками» (p. 22).

## The distinction

The book defines both terms (p. 22):

- A **conduit** just passes information through itself. It is neither strong nor clever enough to change that information or to act on its own.
- A **representative** is a self-sufficient entity that can make its own decisions and act on its own.

The book's example is a list of numbers filtered to its primes. The procedural version is a C function that takes two arrays, walks the first and marks positions in the second (p. 23). The book calls that function a conduit between two data sets (p. 24). The object version is a class `PrimeNumbers` that wraps the original list and behaves as a list in which only primes are visible. It does not let the caller manage the list or search it. In effect it declares that it is now the list: a caller that wants something done with the list asks the object, and the object decides how to respond, including whether to consult the original list at all (p. 24).

This wiki reads the test as follows: ask whether a caller of the object could describe it as a thing ("a list of primes", "an SQL record", "a pixel") or only as a job ("finds primes", "formats cash"). The book's own summary list on p. 24 pairs each thing with an ability: it is a list and can select by index; it is an SQL record and can return a cell as an integer; it is a file and can read its content from disk.

## Class as factory, not template

The book insists that a class is a factory of objects, not a template (pp. 17-20). Calling a class a template makes it, in the book's words, a passive, brainless body of code copied wherever needed (p. 20). The author wants the reader to see a class as an active manager of objects, a warehouse objects are taken from and returned to (p. 20). In his view the `new` operator is the simplest form of such a factory, and the Factory pattern only extends it with logic, such as choosing a subclass by a text name (p. 19). The author adds that he is not promoting the Factory pattern (p. 20).

This wiki records this as background to the naming and constructor rules. It has no sign in code of its own.

## Instantiation as composition

The book holds that in true object orientation, instantiating an object means composing smaller objects into a larger one. The only reason to do so is the need for a new entity that obeys a new contract (p. 36). The string "5" is wrapped in `Cash` because the string does not offer the methods needed, such as `cents()` (pp. 36-37). The object is built first and only later asked to work, and the two steps must not overlap (p. 37). That claim is the reasoning under [[constructors-without-code]].

## Encapsulation is delegation, not hiding

In Chapter 2 the book sets encapsulation against data hiding. Hiding data behind getters and setters is what plain data objects do; encapsulation means handing the object responsibility: «Суть инкапсуляции — в делегировании ответственности объекту.» (p. 50). This wiki reads a class that only stores fields behind accessors as having hidden its data without encapsulating anything in this sense, which is the object's side of [[tell-dont-ask]].

## No exemption for infrastructure objects

A reader proposed splitting objects into those that model reality and those (controllers, services, decorators, factories) that wire the first kind into an application, and exempting the second kind from the naming rule (p. 27). The author rejects the split: every object has its own scope, all other objects are external to it, and whether an object relates to reality «не имеет значения» (p. 28). All we know of an object is the behaviour its methods expose (pp. 27-28).

## Where this sits among other pages

- [[tell-dont-ask]] states the caller's side of the same idea: do not pull state out of an object, decide elsewhere and push the result back. This page states the object's side: it is the thing, so there is nothing to pull out.
- [[name-classes-for-what-they-are]] is the naming consequence, and [[builder-and-manipulator-names]] the same for methods.
- [[keep-objects-small]] and [[immutable-objects]] carry the book's view that an object's state is its identity.
- This wiki notes that the book's position is far stronger than common practice. Most codebases contain service and controller objects by design, and the frameworks they use often require them. The pages that draw on this concept therefore name the conventions that override it.

## Source

[[elegant-objects]]: pp. 17-20, 22-24, 27-28, 36-37, 50. The reading of the test as "describe it as a thing or a job", the reading of a class that only stores fields behind accessors, the links to [[tell-dont-ask]] and the remark on common practice are this wiki's own. The quotations on pp. 28 and 50 were checked against the page image.
