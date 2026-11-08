---
title: Make base class data private, not protected
category: objects
summary: "An abstract base class declares protected fields that subclasses read or assign directly; with a concrete parent the same shape is inheritance-tax."
tags: [rule, inheritance, encapsulation, coupling]
paradigm: oop
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell quotes Bloch: «наследование нарушает инкапсуляцию» (p. 145). Deriving from a class gives privileged access to its protected methods and data (p. 145).

## Rule

Make all data private rather than protected. If a derived class really needs a base attribute, give the base class protected access methods (p. 145). The coupling list on p. 139 states the same: private rather than protected base data weakens the coupling of derived classes to the base.

## Sign in code

A field declared protected (or the language's equivalent of subclass-visible) in a base class, and a subclass method that reads or writes it by name.

This wiki assigns the neighbouring case as follows. When a subclass reads a protected field of its parent: if the parent is concrete, [[inheritance-tax]] owns it; if the parent is abstract, [[private-data-not-protected]] owns it. A protected field referenced only from inside its own class, with no subclass touching it, is [[smallest-scope-first]].

## When not to apply

- A framework or project convention that requires subclass-visible fields (generated subclasses, mapped base entities): the convention governs. This limit is this wiki's own.
- Languages without access control rely on naming conventions; the rule then applies to the convention, decided at work time. This limit is this wiki's own.

## Repair

Make the field private; add a protected method naming what the subclass needs from it. This wiki adds: a protected accessor that merely returns a mutable field exposes the same thing, so the accessor is for what the subclass needs, not for the field.

## Before and after

```
abstract class Shape     { protected points: List }
class Polygon extends Shape { area(): uses points[i].x ... }
```

```
abstract class Shape     { private points: List ; protected vertex(i): Point ; protected vertexCount(): Int }
class Polygon extends Shape { area(): uses vertex(i).x ... }
```

## Source

- [[code-complete]], p. 139 (coupling rules), p. 145 (the rule and Bloch's quotation).
- This wiki's own: the sign, the owner assignment with [[inheritance-tax]], both limits, the note on accessors that return a mutable field, the pseudocode.
