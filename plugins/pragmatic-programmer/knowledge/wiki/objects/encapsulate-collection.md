---
title: Encapsulate a collection field
category: objects
summary: "A getter returns the object's own mutable collection field (return this.items), or a setter stores the caller's list as is, so clients add, remove or sort the member list without the owning class seeing it."
tags: [rule, encapsulation, collections, mutation, accessors]
paradigm: oop
sources: [fowler-refactoring, code-complete]
created: 2026-11-07
updated: 2026-11-07
---

Fowler's *Refactoring* (2nd ed., ch. 7, "Encapsulate Collection", PDF pp. 194-199) names a common mistake in code that already looks encapsulated. The field is private and has a getter, but the getter hands out the collection itself, so "that collection’s membership can be altered without the enclosing class being able to intervene" (PDF p. 195). In his words: "While the reference to the field is encapsulated, the content of the field is not" (PDF pp. 197-198).

## Rule

Give the owning class modifier methods for the collection, usually `add` and `remove`, so that every change goes through it. Make the getter return a protected view, a read-only proxy or a copy, never the raw collection. If a setter for the whole collection has to stay, make it store a copy of the list it receives (PDF pp. 195-196, 198).

The reasoning: changes that go through the owner give it "the opportunity to modify such changes as the program evolves" (PDF p. 195). A team habit of leaving collections alone is not enough, because "a mistake here can lead to bugs that are difficult to track down later" (PDF p. 195).

## Sign in code

- A getter whose body returns the collection field itself (`return this.courses`), with no copy and no read-only wrapper.
- Client code calls a mutating operation on what that getter returns: `person.courses().add(c)`, `.remove(…)`, `.clear()`, or an in-place sort.
- A setter assigns the caller's collection to the field directly (`this.courses = list`), so the caller keeps an alias to the object's state.

This wiki assigns the neighbouring cases as follows. A getter that hands out the mutable collection a rule between fields depends on is [[class-invariant]]; a returned internal collection that callers mutate, or a setter that stores the caller's collection, is [[encapsulate-collection]]; a returned internal collection that callers only loop over, where the concern is dependence on its storage type, is [[iterator]]. A class whose public methods are only accessors over its fields is [[no-getters-and-setters]]. A collection reached through a chain of more than two accessors is [[train-wreck]]. A copy constructor that shares the original's mutable fields is [[prefer-deep-copy]]. Module-level or widely shared mutable data handed out by a getter is [[encapsulate-variable]]'s procedure under [[global-data]]'s sign. Fields of a structure with no routines of its own written from several call sites: [[replace-direct-data-manipulation-with-adt]]. This page owns one object's own collection field leaking out through its accessor or coming in through its setter.

*Code Complete* agrees: if a class returns a collection, have it return a read-only collection and provide routines to add and remove elements (section 24.3, p. 560, via [[code-complete]]).

## When not to apply

- **Immutable collections.** If the collection type cannot be changed, returning it leaks nothing. This limit is this wiki's own: Fowler's motive is mutable data (PDF p. 194).
- **Huge collections.** A copy can cost real time. Fowler says most lists are not that big and points to the general rule of measuring before optimising (PDF p. 195; [[premature-code-tuning]]). Where a copy has been measured as too expensive, use a read-only view.
- **Mixing mechanisms.** Fowler's condition: "What’s important here is consistency within a code base. Use only one mechanism" (PDF p. 196). Where the code base has settled on proxies or on copies, follow it.

## Repair

1. Encapsulate the field behind an accessor if that has not been done (PDF p. 196).
2. Add `add` and `remove` methods on the owner. Decide what `remove` does with an element that is absent: Fowler defaults to raising an error and lets the caller pass an alternative (PDF p. 198).
3. Remove the setter for the whole collection if nothing needs it; otherwise make it store a copy (PDF p. 196).
4. Change every client that mutates the collection to call the new methods, testing after each change (PDF p. 196).
5. Make the getter return a copy or a read-only proxy (PDF p. 196).

Keep the getter returning a collection. Fowler rejects the variant that never returns a collection and turns `aCustomer.orders.size` into `aCustomer.numberOfOrders`: it "adds a lot of extra code and cripples the easy composability of collection operations" (PDF p. 195).

Trade-offs between the two views, as Fowler gives them: a copy may surprise a programmer who expects changes to reach the source, though "in many code bases, programmers are used to collection getters providing copies" (PDF p. 195). A proxy shows later changes of the source and a copy does not, which seldom matters because such lists are held briefly (PDF pp. 195-196). His stance: "I’d rather copy them unnecessarily than debug errors due to unexpected modifications" (PDF p. 199), and a class managing a collection "should always give out copies" (PDF p. 199).

## Before and after

```
class Person
    private courses = []
    courses(): return this.courses
    setCourses(list): this.courses = list

// client
for name in readCourseNames(file)
    person.courses().append(new Course(name))
```

```
class Person
    private courses = []
    courses(): return copy(this.courses)
    addCourse(c): this.courses.append(c)
    removeCourse(c, ifAbsent = raise NotFound)
        if not this.courses.contains(c): ifAbsent()
        else this.courses.remove(c)

// client
for name in readCourseNames(file)
    person.addCourse(new Course(name))
```

Reading the collection stays composable: `person.courses().filter(isAdvanced).count()` still works on the copy.

## Source

Fowler, *Refactoring*, 2nd ed., ch. 7, "Encapsulate Collection", PDF pp. 194-199 ([[fowler-refactoring]]). The rule, the repair steps, the rejected variant, the consistency condition, the size remark and the copy/proxy trade-offs are Fowler's. The signs, the immutable-collection limit and the assignments against neighbouring pages are this wiki's own.

McConnell, *Code Complete*, 2nd ed., Russian edition, [[code-complete]], section 24.3, p. 560: the same refactoring, with a read-only collection and add and remove routines. The pseudocode is this wiki's own, after Fowler's Person/Course example.

Related: [[minimize-member-accessibility]], [[immutable-objects]], [[no-getters-and-setters]].
