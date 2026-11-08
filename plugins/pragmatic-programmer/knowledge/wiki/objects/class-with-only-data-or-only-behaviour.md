---
title: Class with only data or only behaviour
category: objects
summary: "A class with no fields whose name is an action, created only to call one method on another object's data (new DatabaseInitialization().run(db)); or a field-less class whose methods all take the same one record and work only on its fields, while that record has only fields and accessors (Cab and CabService)."
tags: [rule, responsibilities, data-class, naming, encapsulation, cohesion]
paradigm: oop
sources: [code-complete, object-oriented-thought-process, larman-applying-uml-and-patterns, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

McConnell lists two kinds of class to avoid, mirror images of each other (p. 152).

## Rule

- **Eliminate irrelevant classes.** If a class has only data and no behaviour, ask whether it is really a class; perhaps demote it, making its data members attributes of one or more other classes (p. 152). A margin note says such a class is usually called a structure (p. 152).
- **Avoid classes named after verbs.** A class with only behaviour and no data is usually not really a class; consider turning a class such as `DatabaseInitialization` or `StringBuilder` into a method of some other class (p. 152).

Weisfeld's *The Object-Oriented Thought Process* names the behaviour-only class as one of the main mistakes of programmers coming to objects from structured design: «создание класса, который обладает поведениями, но не имеет своих данных» (p. 100). Such a class forgoes the benefits of encapsulation; a class is meant to be a complete package of the data and the behaviour of one whole thing, such as a taxi (p. 100). This wiki reads his mistake as the split form of the pair McConnell lists: one class holds the data, its partner the behaviour, and each is the half of a class the other lacks.

## Sign in code

- A class with no fields whose name is an action or gerund, created only to call one method on data that belongs to another object. This page owns that shape.
- A class with no instance fields, or only injected collaborators, whose public methods each take the same record as an argument and read or write that record's fields, while the record's class has only fields or accessors. The two usually share a name (`Order` and `OrderProcessor`, `Cab` and `CabService`). This sign is this wiki's own reading of Weisfeld's mistake (p. 100), which the book states without code.

This wiki assigns the neighbouring cases as follows. A class whose public methods are only accessors over its fields is [[no-getters-and-setters]]; a bare read or write of a field is [[uniform-access]]. On such a class, this page supplies Code Complete's alternative repair: where a search shows one class holds all the logic about its data, fold the fields into that class instead of moving behaviour into the data class. A class whose name ends in -er or names a job is [[name-classes-for-what-they-are]], which owns the name; this page owns the absence of data. A class of only static methods is [[no-static-methods]]. Larman warns that overused [[pure-fabrication]] turns functions into objects, and that its usual symptom is that most of the data inside the objects is passed to other objects to reason with it (*Applying UML and Patterns*, 3rd ed., 25.2, PDF p. 588, via [[larman-applying-uml-and-patterns]]); this wiki reads that symptom as the record-and-service shape, which this page owns. For the split pair: a field-less class whose methods all take the same one record and read or write only its fields, while the record has only fields or accessors, is [[class-with-only-data-or-only-behaviour]]; where its methods each read and write several data-only classes, [[god-class]] owns it; a single method of an otherwise sound class that reads another object and writes back is [[tell-dont-ask]].

Fowler's **Data Class** smell, a class with fields and accessors and nothing else (*Refactoring*, 2nd ed., ch. 3, PDF pp. 97-98), is the accessor shape, so this wiki puts it on [[no-getters-and-setters]] with Fowler's repairs and his exception for an immutable result record. This page keeps the field-less class and the split pair.

## When not to apply

- Data structures passed across a boundary (messages, DTOs, records in code built on data and functions) are data on purpose. The book only notes, in a margin note, that such a class is called a structure (p. 152); the boundary limit is this wiki's own.
- A stateless class that implements an interface so it can be substituted (a strategy) carries behaviour a caller chooses at run time, so it is not a method in disguise. Larman agrees that there is nothing inherently wrong with creating "function" or "algorithm" objects, as long as representational classes keep their responsibilities (25.2, PDF p. 588); this wiki's reading of that as a limit on this page is its own.
- Code written in a functional style (`paradigm: fp`), where data and functions are kept apart on purpose and the data is immutable. This limit is this wiki's own.
- A coordinator that works across several objects, none of which owns all the data it touches. This limit is this wiki's own.

## Repair

Turn a behaviour-only class into a method of the class whose data it works on. For a data-only class with one user, move its fields into that user. For the split pair, move each method that reads only the record's fields into the record's class, make the fields it used private, and delete the behaviour class once it is empty or keep it only for what spans several objects.

## Before and after

```
class DatabaseInitialization { run(db) { db.createSchema(); db.seed() } }
new DatabaseInitialization().run(db)
```

```
class Database { initialize() { createSchema(); seed() } }
db.initialize()
```

The split pair (Weisfeld's taxi, p. 100):

```
class Cab
  public plate
  public fuel

class CabService
  refuel(cab, litres)
    cab.fuel = cab.fuel + litres
  canDrive(cab)
    return cab.fuel > 0
```

```
class Cab
  private plate
  private fuel
  refuel(litres)
    fuel = fuel + litres
  canDrive()
    return fuel > 0
```

## Source

- [[code-complete]], p. 152: both rules, the examples, the margin note on structures.
- Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]], ch. 5, p. 100: the behaviour-without-data mistake, its loss of encapsulation, the class as a complete package. The quotation was checked against `raw/`. This wiki's own for that part: the reading as the split pair and the second sign.
- Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 25.2, PDF p. 588: the overuse of Pure Fabrication, its usual symptom, and function objects as not wrong in themselves. This wiki's own for that part: reading the symptom as the record-and-service shape, and the strategy limit.
- Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Data Class", PDF pp. 97-98. The routing of that smell to [[no-getters-and-setters]] is this wiki's own.
- This wiki's own: both signs, the owner assignments, all four limits, the repair wording and the pseudocode.

Related: [[reasons-to-create-a-class]], [[god-class]].
