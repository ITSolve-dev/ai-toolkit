---
title: Null field hides another class
category: objects
summary: "A field initialised to null and filled by a later setter, or a group of fields set only in one mode, with code branching on `field != null` to decide what kind of object this is (Fowler's temporary field)."
tags: [rule, null, class-design, cohesion, initialization]
paradigm: oop
sources: [elegant-objects, object-oriented-thought-process, fowler-refactoring]
created: 2026-11-02
updated: 2026-11-07
---

Bugayenko argues that a field which may hold NULL instead of useful information usually marks a class doing the work of several. Whether the field is set tells the code which of those classes the object really is (pp. 84-86). He returns to NULL in general in later sections. This page covers only fields left uninitialised.

## Rule

Do not leave a field null, to be filled later. Either construct the object with every value it needs, or do not construct it. Asked in the comments how immutability prevents null references, the author says he instantiates the object with all required arguments or throws an exception (p. 91).

The book treats the scattered `if (name != null)` checks and the NullPointerException risk as the lesser cost (p. 85). The main cost is maintainability: it is hard to tell when the object is an object and when it has become something else. Asked why a `User` would ever need an uninitialised name, the author answers that usually «нам на самом деле нужен другой класс» (p. 85), and that the class was never introduced. The result is one oversized class that is at once a user, a buyer, an employee and a database record. Initialisation tells them apart: a set name means a buyer, NULL means a plain user (pp. 85-86). Making objects immutable removes the null fields and so forces small, cohesive classes (p. 86).

### Weisfeld recommends the null start

Weisfeld's *The Object-Oriented Thought Process* recommends the practice this page reports. His no-argument `Cabbie` constructor sets `name = null; myCab = null;`, and he calls assigning null to attributes a «рациональная методика программирования» (p. 92): the null tells later code whether the value has been set properly, and the code checks for null before use so that an unassigned `myCab` is not used as if it held a cab (pp. 92-93). His two cases are of different kinds: a value the user will enter later, and an absent relation, an `Employee.spouse` for an employee who may not be married (p. 93). He also says initialising attributes in constructors is always a good idea (p. 93), which agrees with [[initialize-every-member-in-every-constructor]]; the disagreement is only about null as the chosen initial value.

This wiki resolves the books per case. The spouse is an optional association that does not change what the object is, so it is [[association-cardinality-in-field-types]], and an explicit optional value puts the check where the type requires it rather than in the caller's memory. A value "filled later" is [[initialize-every-member-in-every-constructor]] when the object is unusable until it arrives, as a `Cabbie` with no cab cannot `giveDestination`; it becomes this page's sign only where code branches on the null to act as a different kind of object. Weisfeld's own second constructor, `Cabbie(name, serialNumber)`, builds a complete object (p. 93); this wiki reads that constructor as the repair. He notes that some platforms forbid null for strings and use an empty string instead (p. 93); this wiki does not carry that over, because an empty-string sentinel hides absence the same way null does.

### The temporary field of *Refactoring*

Fowler and Beck's chapter on smells in *Refactoring* names the same shape **Temporary Field**: a class "in which a field is set only in certain circumstances" (2nd ed., ch. 3, Temporary Field, PDF p. 95). Their reason is the reader's expectation: such code is hard to understand "because you expect an object to need all of its fields", and a reader cannot tell why a field is there when it seems unused (PDF p. 95). Their repair agrees with Bugayenko's split: Extract Class to give the "orphan variables" a home, Move Function to put the code that concerns them into the new class, and Introduce Special Case to make an alternative class for when the variables are not valid, which can remove the conditional code (PDF p. 95; see [[null-object-or-optional]]).

## Sign in code

- A field left null by the constructor and filled by a setter, and code that branches on whether it is null to choose behaviour, such as `if (this.name != null) … else …`, especially when the branches act like different kinds of object.
- A field or group of fields assigned only on one path (one mode or one method), which other methods test for being set before they act (Temporary Field, PDF p. 95). This wording is this wiki's.

A field left null by the constructor and filled by a setter, and code that branches on whether it is null to choose behaviour, is [[null-field-hides-another-class]]. A check that only rejects use before the field is set (Weisfeld's `myCab`, p. 93) is [[initialize-every-member-in-every-constructor]] (class side) or [[temporal-coupling]] (call side). An optional association whose absence the code must handle (`Employee.spouse`) is [[association-cardinality-in-field-types]]. A field left null and filled by a setter with no branch on its nullness is [[immutable-objects]] (class side) or [[temporal-coupling]] (call side). Other fields reassigned after construction belong to [[immutable-objects]]. Fields that only carry intermediate results between the methods of one algorithm, set when it starts and read by nothing else, are [[pass-state-dont-hoard-it]]; fields valid only in one circumstance, which other code tests for being set before it acts, are [[null-field-hides-another-class]].

## When not to apply

- This wiki's own limit: a genuinely optional attribute that does not change what the object is (a middle name, an optional comment) is not a hidden class. There, the repair is an explicit optional value or a separate constructor, not a new class.
- A framework the project depends on fills the field after construction: the project convention overrides the book, and the hidden-class question applies only to the branch on null. This limit is this wiki's own.
- A field whose value really arrives after construction from outside the object's control (user input the object must exist before), and whose absence every operation of the class handles. The null, or better an optional value, then records a real state. This limit is this wiki's own.
- Lazy caching of a computed value (p. 77, see [[immutable-objects]]) leaves a field null until first use, but it does not change the object's kind. The class split does not apply. This reading is also this wiki's own.

## Repair

1. Find the kinds that the null check distinguishes, and give each its own class, composing or wrapping the shared part.
2. Let each class take all of its fields in the constructor.
3. Where a constructor cannot get a required value, make it throw instead of storing null.
4. Where the code branches on the fields being unset, the class for that case can be a special case that does the neutral thing (Fowler's Introduce Special Case, PDF p. 95).

## Before and after

```
class User
  final field id
  field name = null
  method setName(txt)
    this.name = txt
  method greet()
    if this.name != null
      return "Dear " + this.name   // behaves as a buyer
    return "Hello, guest " + this.id
```

```
class User
  final field id
  constructor(id)
  method greet()
    return "Hello, guest " + this.id

class Buyer
  final field user
  final field name
  constructor(user, name)
  method greet()
    return "Dear " + this.name
```

## Source

Bugayenko, *Elegant Objects*, Java Edition, Russian translation (Piter, 2018), section 2.6, pp. 84-86, and the comment answer on p. 91; see [[elegant-objects]]. This wiki's own: the signs as worded, the optional-attribute limit, the caching limit, the shape of the repair and the pseudocode. The book names the merged roles but shows no split.

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]]: p. 92 (the null-initialising constructor, null as a sound practice), p. 93 (checking for null before use, input entered later, `Employee.spouse`, the empty string on some platforms, initialising in constructors, the two-argument constructor). The quotation was checked against `raw/`. This wiki's own for that part: the per-case resolution against *Elegant Objects* and the routing of `myCab` and `spouse` to neighbouring pages, the reading of the two-argument constructor as the repair, and the late-input limit.

Fowler and Beck, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Temporary Field", PDF p. 95: the smell, the reader's expectation, Extract Class, Move Function and Introduce Special Case. This wiki's own for that part: the split with [[pass-state-dont-hoard-it]] and the wording of the one-path sign.
