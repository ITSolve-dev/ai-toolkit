---
title: Immutable object versus constant object
category: types-and-state
summary: "A class with only final fields whose methods do I/O or mutate an encapsulated collection is treated as a value: cached, compared, or shared on the assumption that it returns the same answer each time."
tags: [concept, immutability, identity, state, equality]
paradigm: oop
sources: [elegant-objects]
created: 2026-11-03
updated: 2026-11-03
---

In section 3.4 of *Elegant Objects* Bugayenko answers the objection that the world is mutable and so cannot be modelled with immutable objects. His answer separates two things usually merged under "immutable", and the separation decides what a reader may assume about a class. It is the detail the book promised in section 2.6, where it said only that an immutable object is not necessarily a constant one (p. 91; see [[immutable-objects]]).

## Definitions in the book

- An object is a representative of an entity outside its scope: a file on disk, a web page, an associative array, this month's calendar (p. 159; see [[object-as-representative]]). A block of memory joins that list later, on pp. 165-166.
- Its **state** is the coordinates of that entity: the URI of a `WebPage`, the path of a `File` (pp. 159-160).
- An object is **immutable** when it never changes those coordinates during its life. The book's word is loyal: «неизменяемый объект верен сущности реального мира, которую он представляет» (p. 162). A mutable object can switch to another entity, so it is disloyal.
- A **constant** object is the edge case of immutability in which the state *is* the entity: a `ConstantList` holding its array, whose `with(x)` returns a new list with the elements copied (pp. 162-163). `String`, `URI` and `Double` are constants in this sense (p. 158).

Under these definitions a `WebPage` whose `content()` performs an HTTP GET and returns something different each time is immutable, and so is one with a `modify(content)` that performs a PUT (pp. 158, 164). An `ImmutableList` with a final field holding a linked list and an `add()` that appends to it is also immutable in the book's reading: the list modifies the memory it represents, not its own coordinates. The book makes this explicit with a hypothetical `Memory` class and a C++ version whose pointers are `const` (pp. 164-165).

## Identity

The book holds that an immutable object has no identity of its own: its identity coincides with its state (p. 160). Two `WebPage` objects with the same URI represent the same page and behave the same, so `equals` and `hashCode` are computed from the URI (p. 161). Mutable objects need identity apart from state, because their state changes (p. 161).

## What each guarantees

The book itself says that «Почти все, что говорилось о неизменяемых объектах в разделе 2.6, относилось к константным объектам» (p. 166), so the guarantees argued in section 2.6 belong to constants. This wiki spells out what each term then promises, and this is where the concept changes code:

- A **constant** promises that every method returns the same result for the same arguments. It can be cached, memoized, used as a map key by content, and shared between threads without coordination.
- An object that is **immutable but not constant** promises only that it will keep talking to the same entity. Its results can change between calls, and calls can have effects. It is not safe to cache, to treat as a value in a pure function, or to share between threads unless the entity itself is safe to share.

Mario T. Lanza raises exactly this in the book's discussion: calling an immutable shell an immutable object breaks arguments in which immutability carries guarantees, such as a pure function returning the same result each call (p. 169). Jacob Zimmerman notes that idempotence is an ideal to aim for but impossible for an object that represents a file (p. 167). Bugayenko accepts the point and keeps his redefinition (p. 169).

This wiki reads the disagreement per setting: when code relies on repeatable results (caching, memoization, equality by content, concurrent sharing, pure functional code), the requirement is a *constant*, and the book's broader "immutable" is not enough. When code only needs an object that will not be re-pointed at a different file or URL, the book's "immutable" is the right test.

## Signs this concept explains

- An object whose fields are all final, whose methods perform I/O or mutate an encapsulated container, used as a cache key, memoized, or passed to code documented as pure. No rule page owns this shape; this concept page explains it and reports nothing on it alone.
- `equals`/`hashCode` computed from a field that is a mutable container: the hash can change while the object sits in a set. That shape is owned by [[mutable-hash-key]].
- The word "immutable" in a class name or comment on a class with an `add`/`modify`/`write` method.

## Related

- [[prefer-constant-objects]]: the book's preference between the two kinds, and the rule that owns the container-mutation sign.
- [[shared-state-is-incorrect-state]], [[class-invariant]].

## Source

Bugayenko, *Elegant Objects*, Java Edition, Russian translation (Piter, 2018), section 3.4, pp. 157-169, returning to section 2.6; see [[elegant-objects]]. The book's: that section 2.6's arguments concerned constants (p. 166). This wiki's own: the itemised statement of what each kind guarantees, the per-setting reading of Lanza's objection and the signs. The quotation from p. 166 was checked against the page image; the others are transcribed from OCR and must be checked against it.
