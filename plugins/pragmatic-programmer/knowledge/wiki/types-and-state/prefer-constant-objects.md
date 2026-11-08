---
title: Prefer constant objects
category: types-and-state
summary: "A class whose state is a final reference to a mutable container changed by its own add/put/remove, filled by a run of such calls straight after new and then passed on, where a copy-returning with() would make it constant."
tags: [rule, immutability, constant, state]
paradigm: oop
sources: [elegant-objects]
created: 2026-11-03
updated: 2026-11-03
---

Section 3.4 of *Elegant Objects* draws two conclusions from the distinction on [[immutable-versus-constant-object]]. First, every object should be immutable, that is, loyal to the one entity it represents; the book claims any system, games and mobile apps included, can and should be built entirely from immutable objects (p. 166). Second, among immutable objects the constant ones are preferable: «Очевидно, что лучше использовать константные объекты, поскольку они проще для проектирования, поддержки и понимания.» (p. 166).

## Rule

1. An object never changes the coordinates of the entity it represents. A `File` stays on its path, a `WebPage` on its URI. That part is the rule on [[immutable-objects]].
2. This wiki reads the preference as a split by where the entity lives. Where the entity can live in the object itself (a money amount, a set of options), make the object constant: an operation that would change it returns a new object instead (`ConstantList.with(x)`, pp. 162-163).
3. Where the entity is outside the object (a file, a web page, a database row, in the book's reading also a block of memory), keep the object immutable and let its methods act on the entity.

## Sign in code

- A class whose state is a final reference to a mutable container changed by its own add/put/remove, filled by a run of such calls straight after new at a visible construction site and then passed on.

This wiki assigns the neighbouring cases as follows. A field reassigned after construction, a setter included, is [[immutable-objects]]. This page owns a container mutated in place behind a final reference, which the book still counts as immutable (pp. 163-165). Such a container used in `equals`/`hashCode` while the object sits in a hashed collection is [[mutable-hash-key]]. Such a container reached by concurrent code is [[shared-state-is-incorrect-state]].

## When not to apply

- Large or hot collections where copying on every `with()` costs more than the program can afford; the book's own `ConstantList` copies the whole array per element (p. 163). There the book's immutable-but-not-constant list, which mutates memory it owns behind a fixed reference, is the form it accepts (pp. 163-165). The cost judgement is this wiki's own.
- Objects that represent an entity outside the program; they cannot be constant, and forcing them to cache a snapshot misrepresents the entity. This reading is this wiki's own.
- Where the project's language or framework requires mutable objects (a framework that fills objects through setters, an ORM entity), the project's convention overrides this rule at that boundary; this wiki reads the rule as still applying to the objects behind it.
- The book's claim that whole systems should be built only from immutable objects is a stance, not a sign; this page enforces only the sign above.

## Repair

- Replace the mutating method with one that copies and returns a new instance; make the container field final, assign it only in the constructor, and never expose it for writing.
- At call sites, bind the result of each `with()`.

## Before and after

Before:

```
class Recipients
    final items: mutable list of Email
    constructor()
        this.items = new mutable list
    add(email)
        items.append(email)
    all() = items

r = new Recipients()
r.add(a)
r.add(b)
send(message, r)
```

After:

```
class Recipients
    final items: list of Email
    constructor(items = [])
        this.items = copyOf(items)
    with(email) = new Recipients(items + [email])   // copy, new object
    all() = readOnlyView(items)

r = new Recipients().with(a).with(b)
send(message, r)
```

The before is filled by `add` calls straight after `new` and then passed on, so none of the page's limits excludes it, and it reassigns no field, so the sign belongs here rather than on [[immutable-objects]]. The after reassigns no field and mutates no container.

## Source

Bugayenko, *Elegant Objects*, Java Edition, Russian translation (Piter, 2018), section 3.4, pp. 157-166; see [[elegant-objects]]. The preference for constants and the claim about whole systems are the book's (p. 166). This wiki's own: the split of rules 2 and 3 by where the entity lives (for a set of numbers the book offers both forms, pp. 162-163), the sign, the assignment of neighbouring cases, the cost limit, the outside-entity limit, the framework limit and the pair. Quotations are transcribed from OCR and must be checked against the page image.
