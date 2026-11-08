---
title: Inheritance tax
category: objects
summary: "A subclass of a concrete class that reads the parent's fields, or a call site calling, through the subclass, a method declared only in the parent."
tags: [rule, inheritance, coupling, code-reuse]
paradigm: oop
sources: [pragmatic-programmer, fowler-refactoring]
created: 2026-11-01
updated: 2026-11-07
---

Inheritance taken in order to reuse code charges a recurring cost in [[coupling]]. The book says that developers inherit for one of two reasons: they dislike typing, or they like types (p. 200). The first motive pulls shared behaviour from a base class into subclasses. The second is covered by [[prefer-interfaces-for-polymorphism]]. This page is about the first.

## Rule

«Не платите налог на наследование» (p. 202). The reason is direct: «Наследование означает связывание» (p. 200). The child is coupled to its parent, the parent to its own parent, and so on. Code that merely uses the child is coupled to all of those ancestors too (p. 200).

The book's worked case has two failures in one change. Renaming a method on the parent breaks top-level code that only ever used the child, although what the child does internally should be none of that code's business. Renaming the parent's instance variable silently breaks the child, although a variable name is an internal detail of the parent (p. 201).

Fowler and Beck's chapter on smells in *Refactoring* counts the same dependency among the forms of **Insider Trading**: "Subclasses are always going to know more about their parents than their parents would like them to know", and when it is time to leave home, Replace Subclass with Delegate or Replace Superclass with Delegate (2nd ed., ch. 3, Insider Trading, PDF p. 96). The wider smell is on [[coupling]].

## Sign in code

This wiki reads the sign as any of these:

- A class extends a concrete class, and its own methods read or write a field declared in that parent.
- A call site invokes, on a variable of the subclass type, a method declared only in a concrete parent. This page owns that shape where the parent is the project's own class. Where the parent is a framework base class, it belongs to [[delegate-to-services]]. For a project parent, a call through the subclass to a parent method is [[inheritance-tax]]; the unused rest of the parent's API is the second sign of [[delegate-to-services]], judged only after a caller search.
- The inheritance chain is more than one level deep, and a method call at the bottom resolves to a method at the top.

Whether the subclass is ever used as its parent needs a search of its callers; this page names it as a question for [[choose-an-alternative-to-inheritance]], not a sign.

This wiki assigns the neighbouring cases as follows. [[final-or-abstract]] owns a subclass that overrides a method the parent implements. [[inheritance-tax]] owns a subclass that reuses a concrete parent by reading its fields or calling its methods without overriding them, or whose callers invoke, through it, methods declared only in a concrete parent. A final subclass that only supplies the abstract methods of an abstract parent whose implemented methods are final is refinement. [[final-or-abstract]] accepts it and [[inheritance-tax]] does not fire on it. A subclass that does both earns findings on both pages, with the repair of [[final-or-abstract]] applied first.

When a subclass reads a protected field of its parent: if the parent is concrete, [[inheritance-tax]] owns it; if the parent is abstract, [[private-data-not-protected]] owns it. A chain more than three of the project's own levels deep is [[deep-inheritance-hierarchy]], whose repair (flatten) comes first; at two or three levels, a call at the bottom resolving to a concrete ancestor is [[inheritance-tax]].

## When not to apply

The book's wording runs from «вы не должны больше пользоваться наследованием» (p. 202) to a heading saying that inheritance is rarely the answer (p. 207), and it names no case for keeping it. Which alternative fits depends on the goal (p. 207). The cases below are this wiki's own, except that the last reports *Refactoring*'s opposite view.

- A final subclass that only supplies the abstract methods of an abstract parent whose implemented methods are final is refinement. [[final-or-abstract]] accepts it and [[inheritance-tax]] does not fire on it.
- The parent is built for extension, with a narrow documented set of override points and no fields exposed to subclasses. The coupling is then to a contract.
- Parent and children live in one module, are owned together and change together. A change is then seen across all of them at once, which lowers the cost without removing it: where nothing checks field names, a rename can still break a child silently (p. 201).
- A framework requires a subclass and offers no other entry point. The book's example of a class losing control of its interface is a framework base class, and it shows delegation as the alternative (p. 204). Keep such a class thin and put the logic elsewhere: [[delegate-to-services]].
- ***Refactoring* disagrees.** Fowler and Beck subclass "to reuse a bit of behavior all the time" and find it "a perfectly good way of doing business" (ch. 3, Refused Bequest, PDF p. 98). This wiki resolves it per setting: where parent and child live in one module and change together (the limit above), a subclass taken for reuse is not a finding; where the parent is owned or changed elsewhere, or callers reach parent-only methods through the subclass, this page's sign holds.

## Repair

1. Decide what the inheritance was for: [[choose-an-alternative-to-inheritance]].
2. For code reuse, give the class a field of the former parent's type and forward only the operations it means to offer. See [[delegate-to-services]].
3. Replace direct reads of the parent's fields with calls.
4. Where several classes need the same methods, use [[mixins-share-functionality]].

## Before and after

```
class Buffer
    field items
    method put(x): append x to items

class Queue extends Buffer
    method take(): remove first of items

q = new Queue
q.put(job)
```

Renaming `put` breaks this call site, though it names only `Queue`. Renaming `items` breaks `Queue`.

```
class Buffer
    field items
    method put(x): append x to items
    method remove_first(): remove first of items

class Queue
    field buffer = new Buffer
    method put(x): buffer.put(x)
    method take(): buffer.remove_first()

q = new Queue
q.put(job)
```

A change inside `Buffer` now stops at the forwarding lines in `Queue`.

## Source

[[pragmatic-programmer]], Thomas and Hunt, 20th Anniversary Edition, Russian translation (Dialektika, 2020), topic 31, pp. 199-202, 204, 207. The rule, the two motives and the coupling reasoning are the book's. The signs and the limits are this wiki's own, apart from the book's framework example and its delegation alternative (p. 204). Repair step 3 and the split of project parents with [[delegate-to-services]] are this wiki's own. The sentence at p. 202 is reported as printed in the Russian edition and read literally. The pseudocode is this wiki's and does not use the book's listing.

Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Insider Trading", PDF p. 96: subclasses knowing their parents, and the two delegate refactorings; "Refused Bequest", PDF p. 98: subclassing to reuse behaviour as a good way of doing business. This wiki's own for that part: the per-setting resolution against *The Pragmatic Programmer*.
