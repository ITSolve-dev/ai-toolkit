---
title: Collapse hierarchy
category: objects
summary: "A subclass (or its parent) left with an empty body, or with only a constructor that passes its arguments to super, after features were pulled up or pushed down: merge the two classes into one."
tags: [rule, inheritance, refactoring, hierarchy]
paradigm: oop
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Collapse Hierarchy merges a class into its parent or child once the two are "no longer different enough to be worth keeping separate" ([[fowler-refactoring]], ch. 12, PDF p. 423). Fowler places it in the course of reshaping a hierarchy, when pulling and pushing features around leaves a class and its parent no longer different enough (PDF p. 423).

## Rule

When a class and its parent no longer differ enough to justify two classes, merge them. Keep the one whose name makes most sense in the future; if neither name is better, pick one arbitrarily (PDF p. 423).

## Sign in code

Fowler gives the condition only as "not different enough". This wiki reads that as a shape in the code: a subclass whose body declares nothing, or only a constructor that passes its arguments straight to the parent, or a parent all of whose remaining members have been pushed down into its one child. In each case one class of the pair holds no field and no method of its own.

This wiki assigns the neighbouring shapes as follows. A subclass or parent left with no field and no method of its own (at most a constructor passing its arguments to super) is [[collapse-hierarchy]]; a base with exactly one derived class that both hold code of their own is [[base-class-with-one-subclass]]; a subclass that overrides only constants or fixed return values is [[subclass-that-differs-only-in-data]]. Subclasses made from a type code, each carrying fields or methods of its own kind, are [[replace-type-code-with-subclasses]]; a subclass that overrides only constants or fixed return values is [[subclass-that-differs-only-in-data]], even inside such a family.

## When not to apply

The book states no limit. The limits below are this wiki's own.

- The empty class is a type that callers outside the module, or a framework, name (a published extension point, or a marker type checked by a container). Removing it then changes an interface that this code does not own.
- The empty subclass is one of several siblings, and the others still differ from the parent. The subclass is then a variant that so far has nothing to add, and removing it loses a name that callers choose by.
- The empty class is a type that code selects by, even inside the module: a catch clause, a type test, a dispatch table. An exception subclass usually is one.

## Repair

Fowler's mechanics (PDF p. 423):

1. Choose which class to remove.
2. Move all the elements into the class that stays, with [[pull-up-method]] or [[push-down-method-and-field]].
3. Change references to the removed class so they name the class that stays.
4. Remove the empty class. Test.

## Before and after

```
class Notice
    field text
    field issuedOn
    method render(): ...

class StandardNotice extends Notice
    constructor(text, issuedOn): super(text, issuedOn)

n = new StandardNotice(t, d)
```

```
class Notice
    field text
    field issuedOn
    method render(): ...

n = new Notice(t, d)
```

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed. (Addison-Wesley, 2018), ch. 12, Collapse Hierarchy, PDF p. 423: the motivation, how to choose which class to remove, and the mechanics. This wiki's own: reading "not different enough" as one class of the pair being empty, the owner assignments, all three limits, and the pseudocode.
