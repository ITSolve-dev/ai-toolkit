---
title: Null object, optional value or exception for absence
category: types-and-state
summary: "An absent value is modelled with a null object none of whose used methods has an honest answer (each throws or returns a made-up value), or with an option type that two or more call sites unwrap with the same default, or that no path returns empty."
tags: [decision-rule, null, null-object, optional, absence]
paradigm: oop
sources: [elegant-objects, fowler-refactoring]
created: 2026-11-03
updated: 2026-11-07
---

Once null is ruled out ([[no-null-arguments]], [[never-return-null]]), absence still has to be expressed. *Elegant Objects* records a dispute between Bugayenko, who wants a **null object**, an object that behaves as the empty case, and a reader, Martin, who wants an **option type** (`Optional`, Scala's `Option`, Haskell's `Maybe`). Asked for a case where `Optional` beats null or exceptions, Bugayenko answers «Не думаю.» (p. 153). This page decides between the two per setting instead of recording the disagreement.

## Rule

Choose by who knows what absence should mean:

- **Exception** when absence means the request could not be honoured and no caller should continue as if it had been: fail inside the method with a message naming what was looked for ([[crash-early]]). The book lists it first among its answers (p. 211).
- **Collection** when the caller is searching and zero results are normal: return a collection, empty when nothing matched, and name the method in the plural (`users`, not `user`). The book admits this differs only slightly from null in technique, but finds it cleaner (p. 209).
- **Null object** when the interface itself has a natural behaviour for "nothing" that every caller would accept: a mask that matches every file, an empty collection, a logger that discards. The book's `AnyFile` is this case (p. 151). Bugayenko adds that a null object need not throw on every call: «Это может быть объект, который что-то может, а что-то не может.» (p. 157). His `NullUser` in section 4.1 answers `name()` and throws on `raise` (p. 210).
- **Option type** when callers differ in what absence should mean, so the decision has to stay with them. Martin's argument: the return type tells every user of the API that they may get nothing, without reading source or documentation, and the user, not the designer, decides whether to supply a default or throw (pp. 155-156).
- **None of them** when the value cannot be absent or has an obvious default. Martin: «Если значение не может отсутствовать или если есть осмысленное значение по умолчанию, не возвращайте Option» (p. 156).

## Sign in code

- A null object none of whose methods used by the code at hand has an honest answer: each throws or returns an invented value (Martin's example: does a missing employee's `areYouHappy()` return true, false, or throw, p. 156).
- Callers that test a null object for its nullness (`isNobody()`, `isEmpty()` before every use): the check null was meant to remove (Madmenyo's objection, pp. 153-155). Fowler's *Refactoring* keeps such a check at the one client whose response differs from the null object's common answer (2nd ed., ch. 10, Introduce Special Case, PDF p. 329); this wiki reads the sign as checks at most call sites, not a check at that one client.
- An option value that two or more call sites in the code at hand unwrap with the same default: the default is a behaviour of the interface and belongs in a null object.
- A function returning an option type with no path that returns the empty case.

This wiki assigns the neighbouring cases as follows. A raw null passed or returned is [[no-null-arguments]] or [[never-return-null]]. The choice between a null object, an option type and an exception once null is gone is [[null-object-or-optional]]. An exception thrown for an ordinary absence and caught round the call is [[exceptions-for-the-exceptional]]: whether the catch around the call turns the exception into ordinary flow. One sentinel value compared by several clients that mostly give it the same default answer is [[introduce-special-case]], which owns the repeated comparison and the steps that replace it; this page owns the choice of form once absence has to be expressed. An option type unwrapped with one default at several call sites is [[null-object-or-optional]]; a sentinel value (null, a magic string or number) compared at several clients is [[introduce-special-case]].

## When not to apply

- Where the project's language or conventions settle how absence is written (an idiomatic option type, nullable types tracked by the compiler, a house rule against option types in fields), that convention overrides the choice between null object and option; this wiki reads the criterion as still deciding whether absence should exist at all and whether it has a natural behaviour.
- The book rejects `Optional` outright, not on naming grounds: in section 4.1 as an envelope rather than the object asked for, foreign to object thinking and close to a null reference (pp. 209-210), and on p. 155 whatever the method is called. This wiki keeps the option branch only for callers that differ; where a checked option type is the project's convention, [[never-return-null]] states the setting.

## Repair

- A raw null returned for an absence ([[never-return-null]]): replace it with the form the rule above selects.
- Null object with no honest answer for the methods used: return an option type, or throw at the point of lookup, so the caller decides.
- Option unwrapped with one shared default at several call sites: move the default into a null object and return the interface.
- Option with no empty path: return the plain value.

## Before and after

Before (a null object that has no honest answer):

```
class NoEmployee implements Employee
    name() = ""
    isHappy() = false          // invented
    salary() = 0               // invented; payroll now pays nobody silently

function find(id): Employee
    row = db.lookup(id)
    if row is missing
        return new NoEmployee()
    return new DbEmployee(row)
```

After (absence returned to the caller, because callers differ):

```
function find(id): Maybe of Employee
    row = db.lookup(id)
    if row is missing
        return Nothing
    return Just(new DbEmployee(row))

report  = find(id).orElse(new Visitor())
payroll = find(id).orElseThrow(new EmployeeNotFound(id))
```

The before falls outside the null object's case, because `Employee` has no behaviour every caller would accept for "nobody". Where it has one, as `Mask` does, the pair on [[no-null-arguments]] applies instead.

## Source

Bugayenko, *Elegant Objects*, Java Edition, Russian translation (Piter, 2018), reader discussion after section 3.3, pp. 153-157, and section 4.1, pp. 209-211, for the collection branch, `NullUser` and the rejection of `Optional` as an envelope; see [[elegant-objects]]. The author's position is that `Optional` has no place in object thinking (p. 155); Martin's criterion is quoted from p. 156; Roland Bouman's doubt that a null object can do more than meaningless operations on a meaningless object is on p. 157. This wiki's own: the resolution by who knows what absence means, the conditions attached to the exception and collection branches (the book names both as answers, p. 211), the signs, the assignment of neighbouring cases and the pair. The quotations from pp. 153, 156 and 157 were checked against the page image.

Fowler, *Refactoring*, 2nd ed., ch. 10, "Introduce Special Case", PDF p. 329, via [[fowler-refactoring]]: the legitimate check at a divergent client. This wiki's own: reading the nullness-check sign as checks at most call sites.
