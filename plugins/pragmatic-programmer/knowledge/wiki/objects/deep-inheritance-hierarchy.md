---
title: Deep inheritance hierarchy
category: objects
summary: "An inheritance chain more than three of the project's own levels below the root, or a base class with more than about nine subclasses in all, so understanding a call at the leaf means reading several ancestors."
tags: [rule, inheritance, complexity]
paradigm: oop
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Inheritance exists to make code simpler; a deep hierarchy does the opposite (pp. 143-144).

## Rule

Avoid deep inheritance hierarchies (p. 143). Riel (1996) proposes at most six levels, from the "7±2" number. McConnell thinks that is too optimistic: «большинству людей трудно удержать в уме более двух или трех уровней наследования сразу» (p. 143). He reads 7±2 as a limit on the total number of subclasses of a base class rather than on levels (p. 143). Deep hierarchies significantly raise the number of defects (Basili, Briand and Melo, 1996), and anyone who has debugged one knows why (p. 143). Use inheritance to avoid duplication and to minimise complexity (p. 144).

## Sign in code

- A class whose ancestor chain, counting only the project's own classes, is more than three levels deep.
- A base class with more than about nine subclasses in all, at every level (the book's reading of 7±2, p. 143).
- A method at the leaf whose behaviour depends on overrides at two or more different levels above it.

This wiki assigns the neighbouring case as follows. A chain more than three of the project's own levels deep is [[deep-inheritance-hierarchy]], whose repair (flatten) comes first; at two or three levels, a call at the bottom resolving to a concrete ancestor is [[inheritance-tax]].

## When not to apply

- This wiki's reading: levels contributed by a framework or the standard library that the project does not read or override are not what a reader has to hold in mind, so only the project's own levels are counted.
- This wiki adds: the numbers are the author's judgement and one study's correlation, not a law. A fourth level whose classes add nothing a reader must track is a weaker finding than three levels of interleaved overrides.

## Repair

Flatten: collapse intermediate classes that add little, and turn variation along a second axis into a contained part (the Claws repair on [[override-that-does-nothing]], and [[containment-or-inheritance]]).

## Before and after

```
Vehicle <- MotorVehicle <- Car <- PassengerCar <- ElectricPassengerCar
```

```
Car { engine: Engine, use: Usage }      // Engine = Electric | Combustion
```

## Source

- [[code-complete]], pp. 143-144: the rule, Riel's six levels, the author's two or three, 7±2 as a limit on subclasses, the defect study.
- This wiki's own: the counting rule, the signs, the owner assignment with [[inheritance-tax]], the limits, the repair and the pseudocode.

Related: [[base-class-with-one-subclass]], [[subclass-that-differs-only-in-data]], [[do-not-reuse-names-of-non-overridable-methods]], [[private-data-not-protected]].
