---
title: Push Down Method and Push Down Field
category: objects
summary: "A superclass method or field that only one subclass, or a few, read, write or call (a quota field on Employee that only Salesman assigns), or that other subclasses override with an empty body or a throw: move it to those subclasses, provided callers already hold the subclass type."
tags: [rule, inheritance, cohesion, refactoring, push-down]
paradigm: oop
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

**Push Down Method** and **Push Down Field** move a member off a superclass and onto the subclasses that actually use it. They are the inverses of [[pull-up-method]] (Fowler, *Refactoring*, 2nd ed., ch. 12).

## Rule

When a method or field "is only relevant to one subclass (or a small proportion of subclasses)", Fowler removes it from the superclass and puts it only on those subclasses, because doing so "makes that clearer" (PDF p. 399). The superclass then states only what is true of every kind.

## Sign in code

- A superclass member is read, written or called only from code inside one subclass, or only by callers that hold a reference typed as that subclass. The second half is judged only after a caller search.
- A superclass field stays unset, or holds a default, for every subclass except one. This wiki's own example: a `quota` field on `Employee` that only `Salesman` assigns.

This wiki assigns the neighbouring cases as follows. A superclass member of the project's own that only one subclass, or a few, read, write or call, with no override in the others, is [[push-down-method-and-field]]; an empty override of it in the other subclasses is [[override-that-does-nothing]], and an override that throws or rejects is [[liskov-substitution-principle]]. A subclass that leaves inherited members unused while it supports the parent's interface is the faint form of Refused Bequest on [[delegate-to-services]].

## When not to apply

- Callers use the superclass type and call the member without knowing the subclass. Fowler: "I can only do this refactoring if the caller knows it’s working with a particular subclass—otherwise, I should use Replace Conditional with Polymorphism (272) with some placebo behavior on the superclass" (PDF p. 399). See [[replace-conditional-with-polymorphism]].
- This wiki adds, as its own reasoning: the member is a template-method hook or a default that subclasses are expected to override. Such a hook belongs on the superclass even if only one subclass overrides it today.
- **The smell is usually faint.** A parent member that most subclasses do not use is the traditional reading of Refused Bequest, and Fowler and Beck say "Nine times out of ten this smell is too faint to be worth cleaning" (ch. 3, Refused Bequest, PDF p. 98). Report it only where it confuses a reader of the superclass, such as a field left at its default in every other subclass; otherwise it is a question, as on [[delegate-to-services]].

## Repair

Method (Fowler, PDF p. 400): copy the method into every subclass that needs it, remove it from the superclass, test, remove it from each subclass that does not need it, test.

Field (Fowler, PDF p. 401): declare the field in every subclass that needs it, remove it from the superclass, test, remove it from each subclass that does not need it, test.

## Before and after

```
class Employee
  quota
  quotaAttainment(): return sales / quota

class Engineer extends Employee
class Salesman extends Employee

// callers: aSalesman.quotaAttainment()
```

```
class Employee

class Engineer extends Employee
class Salesman extends Employee
  quota
  quotaAttainment(): return sales / quota
```

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 12, Push Down Method, PDF pp. 399-400, and Push Down Field, PDF pp. 400-401: the rule, the caller-knows-the-subclass limit and the mechanics. This wiki's own: the signs, the assignment against [[override-that-does-nothing]], [[liskov-substitution-principle]] and [[delegate-to-services]], the hook limit and the pseudocode. Fowler and Beck, ch. 3, "Refused Bequest", PDF p. 98: the faint smell. This wiki's own for that part: when to report it. The quota example draws on Fowler's sales-quota illustration under Replace Type Code with Subclasses (PDF p. 402).
