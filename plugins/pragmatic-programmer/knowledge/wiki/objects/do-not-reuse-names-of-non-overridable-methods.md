---
title: Do not reuse the names of non-overridable base methods
category: objects
summary: "A subclass declares a method with the same name as a private or non-overridable method of its base, so a reader takes it for a polymorphic override."
tags: [rule, inheritance, naming]
paradigm: oop
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Some languages let a derived class declare a function with the same name as a private function of its base. A reader of the derived class may conclude the function is polymorphic, though it only has the same name (p. 142).

## Rule

Do not "override" non-overridable member functions; the book restates it as: do not use the names of the base class's non-overridable methods in derived classes (p. 142).

## Sign in code

A method in a subclass whose name and parameters match a private, final or non-virtual method of an ancestor, without any override marker.

## When not to apply

This wiki adds: where the language makes an accidental match impossible or flags it, the tooling already covers it and this page has nothing to add, since the charter leaves such checks to the tooling.

## Repair

Rename the subclass method after what it does, or make the base method overridable if overriding was intended.

## Before and after

```
class Order       { private validate() }
class RushOrder extends Order { validate() }    // reads as override, is not
```

```
class Order       { private validate() }
class RushOrder extends Order { validateDeadline() }
```

## Source

- [[code-complete]], p. 142: the rule and its reason.
- This wiki's own: the sign, the limit, the pseudocode.
