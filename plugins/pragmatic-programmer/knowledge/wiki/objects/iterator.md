---
title: "Iterator: traverse without exposing the collection's structure"
category: objects
summary: "A function only loops over its argument yet declares it as a concrete collection class (or an array plus an index or length); a class returns its internal collection field so callers can loop over it; or a loop outside a collection's class walks its storage (backing-array indexes, node links)."
tags: [rule, encapsulation, collections, information-hiding, patterns]
paradigm: any
sources: [object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-07
---

Weisfeld picks Iterator as his behavioural pattern, calling it one of the most widely used and noting that several languages build it in (p. 296). An iterator is a standard way to walk a collection one element at a time, and the pattern «обеспечивает скрытие информации, сохраняя защищенной внутреннюю структуру коллекции»; several iterators can be created without interfering with one another (p. 297).

The book's own listing works against its point. Its `iterate()` method takes an `ArrayList<String>`, the concrete type, though it only loops over the elements, and the prose under it describes `hasMoreElements()` over a vector while the code uses a for-each loop (p. 297). This wiki takes the principle from the prose and uses the listing as the shape of the "before".

## Rule

In the book's terms, traversal goes through an iterator so that the collection's internal structure stays hidden, and independent traversals do not disturb one another (p. 297).

## Sign in code

The signs are this wiki's own, derived from the book's information-hiding claim. The first sign's concrete-class half is this wiki's transfer, not the book's claim: a traversal over a concrete list sees nothing of its structure, and the cost is that every caller must hold that one class.

- A function that only loops over its argument declares it as a concrete collection class (a particular list or vector), or takes an array together with an index or length.
- A class returns its internal collection field so callers can loop over it, and come to depend on how it is stored.
- A loop outside a collection's own class walks its storage details: indexes into a backing array, node links.

This wiki assigns the neighbouring cases as follows. A getter that hands out the mutable collection a rule between fields depends on is [[class-invariant]]; a returned internal collection that callers mutate, or a setter that stores the caller's collection, is [[encapsulate-collection]]; a returned internal collection that callers only loop over, where the concern is dependence on its storage type, is [[iterator]]. A parameter or field typed by a concrete collection class is [[iterator]]; one typed by a concrete project class is [[public-methods-implement-interfaces]]. An accessor pair for every field is [[no-getters-and-setters]]. A representation detail visible where a value is used, beyond collections, is [[information-hiding]].

## When not to apply

- The caller genuinely needs what only the concrete type offers: indexed access, a known ordering, a size taken before the loop. The requirement is then part of the interface, not a leak. This limit is this wiki's own.
- Inside the collection's own class, where knowing the storage is its job. This limit is this wiki's own.
- Where the language idiom or the project prescribes the traversal type, the idiom decides the spelling; the rule asks only that callers do not see storage. This limit is this wiki's own.

## Repair

This repair is this wiki's own.

1. Declare the parameter or return type as the narrowest iterable abstraction the language offers.
2. Where a class holds a collection, give it a method that yields its elements, or an iterator over them, instead of a getter for the field.
3. Move loops that walk storage into the collection's class.

## Before and after

```
function printAll(names: ArrayList<String>)    // only iterates, yet names the concrete list
  for name in names: print(name)

class Roster
  private names: ArrayList<String>
  getNames(): ArrayList<String>                // hands out the internal collection
    return names
```

```
function printAll(names: Iterable<String>)
  for name in names: print(name)

class Roster
  private names: ArrayList<String>
  members(): Iterable<String>                  // read-only traversal; storage stays private
    return readOnlyView(names)
```

## Source

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), ch. 15, via [[object-oriented-thought-process]]: the choice of pattern (p. 296), information hiding and independent iterators, the listing and its mismatch with the prose (p. 297). The quotation was checked against `raw/`. This wiki's own: all signs, the owner assignments, the limits, the repair and the pseudocode. The concept of the pattern is [[design-pattern]].
