---
title: "Encapsulate Variable: the mechanics"
category: structure
summary: "Procedure for mutable data whose scope is wider than one function (a module-level variable, a public field): route every read and write through a getter and setter, test after each replaced reference, then restrict the variable's visibility; make the getter return a copy where callers must not change the shared value. Not needed for immutable data or one function's temps."
tags: [method, refactoring, encapsulation, mutable-state, global-data]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

**Encapsulate Variable** (formerly Self-Encapsulate Field and Encapsulate Field) puts a widely accessed piece of mutable data behind a pair of functions and then narrows the visibility of the data itself (*Refactoring*, 2nd ed., ch. 6, PDF pp. 151-156). Fowler presents it as the step that turns a hard data move into an easy function move.

Whether data should be reachable this widely is [[global-data]], which owns the sign and whose repair starts with this procedure. Fields of a structure with no routines of its own written from several call sites: [[replace-direct-data-manipulation-with-adt]]. A collection field leaking through its getter is [[encapsulate-collection]]. A public field read or written outside its class is [[uniform-access]]'s sign; [[encapsulate-variable]] is its repair procedure.

## Why it comes first

A function can be moved or renamed while the old one stays as a forwarding function. Data cannot: "If I move data around, I have to change all the references to the data in a single cycle" (PDF p. 151). Encapsulation is how Fowler turns "the difficult task of reorganizing data into the simpler task of reorganizing functions" (PDF p. 151). It also gives one place to watch changes and to add validation or consequential logic to updates (PDF p. 151).

His habit: "make all mutable data encapsulated like this and only accessed through functions if its scope is greater than a single function" (PDF p. 151), and "The greater the scope of the data, the more important it is to encapsulate" (PDF p. 151). In legacy code he encapsulates opportunistically: whenever he has to change or add a reference to such a variable, he encapsulates it first, which keeps coupling to shared data from growing (PDF p. 151).

## Procedure

Fowler's mechanics (PDF p. 152):

1. Create functions to read and to update the variable.
2. Replace each reference with the getter and each assignment with the setter, testing after each replacement.
3. Restrict the visibility of the variable by the language's means (private, module-private). Fowler's JavaScript technique, moving the variable and its accessors into their own file and exporting only the accessors, is one such means (PDF p. 153). That proves no reference was missed and stops new direct access.
4. Where visibility cannot be restricted, rename the variable to something awkward and test; remaining references then show up.
5. If the value is a record, go on to encapsulate the record ([[replace-direct-data-manipulation-with-adt]]).

Fowler strongly dislikes one function serving as both getter and setter, told apart only by whether an argument is passed (PDF p. 154).

## Encapsulating the value, not only the reference

The basic steps control reassignment of the variable, not changes to the structure it holds: a caller that gets the record can still change its fields, and every other holder sees the change (PDF p. 154). Fowler's two options (PDF pp. 154-155):

- **The getter returns a copy.** His favourite, used "particularly often with lists" (PDF p. 155). Callers may change their copy without touching the shared data.
- **The getter returns a read-only wrapper,** so an attempt to assign a property fails. He uses it as a temporary detector: find the mutations, remove them or give them proper modifying functions, then switch the getter to a copy.

Copying in the setter too is worthwhile when no link to the source must be kept: a copy "prevents accidents due to changes on that source data", its cost is usually negligible, and the alternative may be "a long and difficult bout of debugging in the future" (PDF p. 155). Both copy and wrapper work one level deep; nested records need more (PDF p. 155).

Returning a copy breaks callers that rely on changing the shared data; Fowler relies on tests to find them (PDF p. 155). This wiki reads that as: before switching a getter to a copy, look for callers that write through what it returns.

## Where it stops

- **Immutable data.** Encapsulation is "much less important for immutable data": no hook is needed before updates, and the data can be copied rather than moved, so old references need not change (PDF p. 151).
- **One function's scope.** A temp inside a small function is not hard to move (PDF p. 151).
- **Self-encapsulation inside a class.** Fowler finds routing a class's own field references through accessors excessive: a class big enough to need it needs splitting anyway, and self-encapsulating a field is useful only as a step before splitting the class (PDF p. 151; see [[keep-objects-small]]). Projects that follow *Elegant Objects*' ban on getters and setters reach the same end by another route ([[no-getters-and-setters]]); this pointer is this wiki's own.
- **Encapsulation is not the end state.** This wiki repeats the reading on [[global-data]]: behind accessors the data is still mutable and shared, so narrowing its scope comes next.

## Example

```
// before: a module-level record, read and reassigned anywhere
var defaultOwner = {first: "Martin", last: "Fowler"}

function assignOwner(ship):
    ship.owner = defaultOwner

function resetOwner():
    defaultOwner = {first: "Rebecca", last: "Parsons"}
```

```
// after: private to its module, reached only through functions; readers get a copy
module-private var ownerData = {first: "Martin", last: "Fowler"}

function defaultOwner():
    return copy(ownerData)

function setDefaultOwner(arg):
    ownerData = copy(arg)

function assignOwner(ship):
    ship.owner = defaultOwner()

function resetOwner():
    setDefaultOwner({first: "Rebecca", last: "Parsons"})
```

Renaming a widely used variable starts with this procedure; see [[name-length-matches-scope]].

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 6, "Encapsulate Variable", PDF pp. 151-156: data versus functions, the habit and the scope rule, opportunistic encapsulation, the mechanics, the dislike of overloaded accessors, the copy and wrapper options, copying in the setter, the one-level caveat, tests for broken callers, and the limits on immutable data, one-function scope and self-encapsulation. This wiki's own: the assignment of the sign to [[global-data]] and its neighbours, the advice to look for callers writing through a getter, the pointer to *Elegant Objects*, the not-the-end-state reading, and the pseudocode.
