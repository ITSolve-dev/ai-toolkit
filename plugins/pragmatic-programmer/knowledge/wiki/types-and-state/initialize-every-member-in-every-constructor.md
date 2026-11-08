---
title: Initialize every data member in every constructor
category: types-and-state
summary: "A constructor leaves a declared required field unassigned, with no initialiser at its declaration, so the field's value after construction is accidental; or a constructor path sets a field to 0 or empty where a method needs another value (a divisor, an index, a required name), so the object exists in an unusable state."
tags: [rule, constructors, initialization, defensive-programming, invariant]
paradigm: oop
sources: [code-complete, object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

McConnell calls initialising all data members in all constructors a simple technique of defensive programming (p. 147).

## Rule

Initialise all data members in all constructors, where possible (p. 147).

Weisfeld's *The Object-Oriented Thought Process* states what the initial values must be. The constructor's most important function: «код, заключенный внутри конструктора, должен задать для нового созданного объекта его начальное, стабильное, надежное состояние» (p. 68). The method he gives is to decide on a stable state for every attribute and then initialise each attribute to it in the constructor, and not to rely on the compiler for initialisation (pp. 73-74). Two points sharpen it:

- **A default is not the same as a valid value.** «Инициализация значением 0 не всегда оказывается наилучшим вариантом» (p. 74). His example is an attribute later used as a divisor, where 0 leaves the application unstable. This wiki reads "valid" as valid for the methods that read the field, not zero or empty by habit.
- **Every constructor counts.** A class has several constructors because callers arrive with different amounts of data (p. 71). In his `DataBaseReader` the constructor that receives only a name still sets the start position explicitly (pp. 72-73). In chapter 5 he adds the default case: the object must be properly constructed in its default state, or a constructor must handle that case (p. 103), in the words «конструктор должен задать для объекта его начальное, надежное состояние» (p. 103).

He also advises always writing at least one constructor, because a compiler-supplied default disappears silently once another constructor is added (p. 69). Where the language has destructors, the matching duty is cleanup: releasing what the object acquired, or memory leaks until the system runs out (p. 104); that duty is owned by [[exception-safe-release]].

## Sign in code

- A constructor body that does not assign some field declared in the class, and the field has no initialiser at its declaration.
- Several constructors of one class, one of which leaves a field unset that another assigns.
- A field that a constructor path sets to 0, an empty string or another default that some method of the class uses where that value is illegal: a divisor, an index, a required name (Weisfeld's divisor, p. 74).

This wiki assigns the neighbouring cases as follows. A constructor that leaves a field unassigned is [[initialize-every-member-in-every-constructor]]; several constructors that each assign fields, without delegating to one, are [[one-primary-constructor]], and that repair, routing secondary constructors through the primary one, serves both pages. An object built empty and completed by setters at the call site is [[temporal-coupling]]; a public `initialize()` the other methods need first is [[semantic-interface-to-programmatic]]. An invariant that a setter can break is [[class-invariant]]. A field left null for a later setter is [[null-field-hides-another-class]] where code branches on the null, and [[immutable-objects]] or [[temporal-coupling]] otherwise. A check that only rejects use before the field is set (Weisfeld's `myCab`, p. 93) is [[initialize-every-member-in-every-constructor]] (class side) or [[temporal-coupling]] (call side). An optional association whose absence the code must handle (`Employee.spouse`) is [[association-cardinality-in-field-types]]. This page owns a required field a constructor leaves unset or sets to a non-null value its methods cannot use.

## When not to apply

This wiki adds these limits:

- A field whose language default is the intended initial value (an empty counter of zero) is initialised; the rule is about values left accidental.
- Lazily computed caches, created on first use behind one accessor, are a deliberate exception.
- Objects that a framework, serializer or ORM builds through a required no-argument constructor and fills by reflection follow the framework's convention.
- Where the compiler rejects a field left unassigned, the check is the compiler's, not this page's. That check does not cover the third sign: a field assigned 0 compiles.
- An object that cannot be valid until the caller supplies data the constructor does not have. The repair is to demand the data as a parameter or build the object through a factory; a placeholder value is not a repair.

## Repair

Assign every field in every constructor, preferably by having secondary constructors delegate to one primary constructor. For each field, take its value from the set the methods accept; where no such value is known at construction, add a constructor parameter rather than a sentinel, and check it there.

## Before and after

```
class Connection
    Connection(host)       { this.host = host }            // port, timeout unset
    Connection(host, port) { this.host = host; this.port = port }
```

```
class Connection
    Connection(host, port, timeout) { this.host = host; this.port = port; this.timeout = timeout }
    Connection(host)       : this(host, DEFAULT_PORT, DEFAULT_TIMEOUT)
```

A default that a method cannot use:

```
class Ratio
  field numerator
  field denominator

  constructor(numerator)
    this.numerator = numerator
    this.denominator = 0        // value() divides by it

  constructor(numerator, denominator)
    this.numerator = numerator
    this.denominator = denominator

  method value()
    return numerator / denominator
```

```
class Ratio
  field numerator
  field denominator

  constructor(numerator)
    this(numerator, 1)

  constructor(numerator, denominator)
    require denominator != 0
    this.numerator = numerator
    this.denominator = denominator

  method value()
    return numerator / denominator
```

## Source

- [[code-complete]], p. 147: the rule and its framing as defensive programming, paraphrased.
- Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]]: p. 68 (the constructor's most important function), p. 69 (always write a constructor), pp. 71-73 (several constructors, the `DataBaseReader` start position), pp. 73-74 (a stable state for every attribute, not relying on the compiler, 0 as a divisor), p. 93 (the null check on `myCab`, named in the owner assignment), pp. 103-104 (the default state, destructor cleanup). The quotations were checked against `raw/`.
- This wiki's own: the signs (the third included), the owner assignments, the limits, the repair through one constructor and a parameter instead of a sentinel, the reading of "valid" as valid for the methods, and the pseudocode.
