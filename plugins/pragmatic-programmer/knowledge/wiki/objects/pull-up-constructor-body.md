---
title: Pull Up Constructor Body
category: objects
summary: "Every subclass constructor repeats the same assignments or calls after super() (this.name = name; if isPrivileged() then assignCar()): move them into the superclass constructor through the super call, or into a pulled-up method called at the end when ordering prevents it."
tags: [rule, inheritance, constructors, duplication, refactoring]
paradigm: oop
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

**Pull Up Constructor Body** moves statements that every subclass constructor repeats into the superclass constructor. Fowler reaches for it where [[pull-up-method]] would be his first move, because constructors have special rules about what can be done in what order (*Refactoring*, 2nd ed., ch. 12, PDF p. 395).

## Rule

Common code in subclass constructors goes into the superclass constructor, reached through the `super` call. Any constructor parameters the common code uses become parameters of that call. Fowler describes the usual shape: "Do the common elements first (with a super call), then do extra work that the subclass needs" (PDF p. 397). Common code that has to run after subclass-specific initialisation cannot move into the superclass constructor; it is extracted into a method and pulled up as a method instead (PDF pp. 398-399).

## Sign in code

- Every subclass constructor assigns the same field from the same parameter, such as `this.name = name` after `super()`.
- Every subclass constructor ends with the same call or conditional, as in Fowler's `if (this.isPrivileged) this.assignCar()`, commented "every subclass does this" (PDF p. 398).

## When not to apply

- The shared statement depends on state that only the subclass sets, so it cannot run inside the superclass constructor, which runs before that state exists. Fowler's `isPrivileged` reads a `grade` field assigned in the subclass (PDF p. 398). Use the extract-and-pull-up route instead.
- Fowler: "If this refactoring starts getting messy, I reach for Replace Constructor with Factory Function (334)" (PDF p. 396). A factory frees creation from the constructor's ordering rules ([[factory-function-over-constructor]]).
- This wiki adds, as its own reasoning: if the statements look alike but assign different meanings (a field with the same name holding a different unit in each subclass), the duplication is a chance likeness ([[coincidental-duplication]]).
- This wiki adds: where the project forbids code in constructors beyond assignments ([[constructors-without-code]]), only the assignments move up; a call such as `assignCar()` is that page's finding first.

## Repair

Fowler's mechanics (PDF p. 396):

1. Define a superclass constructor if none exists, and make sure the subclass constructors call it.
2. Use [[slide-statements]] to move the common statements to just after the `super` call.
3. Move the common code into the superclass constructor, and add to the `super` call any constructor parameters it references.
4. Test.
5. For common code that cannot move to the start, use [[extract-function]] and then [[pull-up-method]].

## Before and after

```
class Employee extends Party
  constructor(name, id, monthlyCost)
    super()
    this.id = id
    this.name = name
    this.monthlyCost = monthlyCost

class Department extends Party
  constructor(name, staff)
    super()
    this.name = name
    this.staff = staff
```

```
class Party
  constructor(name)
    this.name = name

class Employee extends Party
  constructor(name, id, monthlyCost)
    super(name)
    this.id = id
    this.monthlyCost = monthlyCost

class Department extends Party
  constructor(name, staff)
    super(name)
    this.staff = staff
```

The late-common-code case:

```
class Manager extends Employee
  constructor(name, grade)
    super(name)
    this.grade = grade
    if isPrivileged() then assignCar()     // every subclass does this

class Director extends Employee
  constructor(name, grade)
    super(name)
    this.grade = grade
    if isPrivileged() then assignCar()
```

```
class Employee
  finishConstruction()
    if isPrivileged() then assignCar()

class Manager extends Employee
  constructor(name, grade)
    super(name)
    this.grade = grade
    finishConstruction()

class Director extends Employee
  constructor(name, grade)
    super(name)
    this.grade = grade
    finishConstruction()
```

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 12, Pull Up Constructor Body, PDF pp. 395-399: the motivation, the mechanics, the factory-function escape and the late-common-code case. This wiki's own: the sign as worded, the chance-likeness and constructors-without-code limits, and the pseudocode, including the second subclass `Director`.
