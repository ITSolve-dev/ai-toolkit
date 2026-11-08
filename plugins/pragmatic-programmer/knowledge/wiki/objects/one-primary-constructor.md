---
title: Make one constructor primary
category: objects
summary: "Two or more constructors of one class each assign the object's fields, so a check or conversion added to one of them is missing from the others."
tags: [rule, constructors, duplication, encapsulation]
paradigm: oop
sources: [elegant-objects]
created: 2026-11-02
updated: 2026-11-06
---

*Elegant Objects* asks that a class with several constructors assign its fields in exactly one of them, the primary constructor, and that every other, secondary constructor only prepare arguments and delegate to it. The principle as the book states it is that «инициализировать поля класса необходимо только в одном месте» (p. 32).

## Rule

Put field initialisation in one constructor. Secondary constructors convert or parse their arguments and call the primary one (`this(...)` in Java) (p. 30). The book's `Cash` takes a `float`, a `String` or an `int`. The first two delegate, and only the `int` constructor assigns `this.dollars` (p. 30). The author places the primary constructor last in the class, so that in a class with ten constructors written months ago he can scroll to the last one instead of searching (p. 30).

The reasoning is duplication. Without the principle each constructor assigns the field itself. A new requirement such as "the amount is always positive" then has to be added in three places, and with a primary constructor in one (p. 31). The author names complexity and duplication as the two worst enemies of maintainability (p. 33).

The book combines this with a preference for many constructors and few methods. Many constructors let a client create an object from whatever it holds (an int, a string such as `"$29.95"`, a float, a value and a currency) without converting first, so the client writes less code and repeats itself less (p. 29). Many public methods blur the class's focus (p. 29). The author's ideal is 2-3 methods and 5-10 constructors, and he says the figures «взяты из головы и не имеют строгого обоснования» (p. 28). This wiki records them as the book's heuristic and does not use them as a sign.

In languages without method overloading, the book's examples being Ruby, PHP and JavaScript, it keeps the principle through a map of arguments that one constructor dispatches on, delegating to itself, at the cost of far more verbose code (pp. 31-32). A reader combined this rule with [[constructors-without-code]] and a later rule about `new` into a new one: primary constructors do nothing but assign arguments to fields. The author agreed (p. 33).

## Sign in code

- Two or more constructors of one class assign the same field.
- A validation, normalisation or default appears in one constructor and is missing from a sibling that sets the same field.

A class in which more than one constructor assigns the fields is [[one-primary-constructor]]. A constructor that computes on its arguments before storing them, including a secondary constructor that parses before delegating, belongs to [[constructors-without-code]]. The book's own `Cash(String)` calls `Cash.parse()` before delegating on p. 30, a shape that section 1.3 then replaces with a wrapping object (p. 35).

## When not to apply

- A class with one constructor has nothing to consolidate.
- This wiki adds that where a language offers default or named arguments and the project's convention is one constructor with optional parameters, that convention reaches the same single place of assignment and overrides the book's many overloads. How the rule maps onto a given language is decided at work time.
- This wiki adds that the book's preference for many constructors serves the client only while each one accepts a different kind of input for the same meaning. Constructors that differ only in which optional field is set are a sign of a class that is too large: see [[keep-objects-small]].

## Repair

1. Pick the constructor whose parameters match the fields one to one, and make it the only one that assigns.
2. Rewrite every other constructor to call it, converting its arguments on the way. Under [[constructors-without-code]] the conversion is wrapping in an object rather than computing a value.
3. Move any check or default that was spread across constructors into the single place, or into the objects the fields hold.
4. Place the primary constructor where the project's readers will look for it. The book's habit is last.

## Before and after

```
class Cash:
    constructor(amount: float)
        this.dollars = to_int(amount)
    constructor(text: string)
        this.dollars = parse_dollars(text)
        assert this.dollars >= 0
    constructor(amount: int)
        this.dollars = amount
```

```
class Cash:
    constructor(amount: float)
        this(NonNegative(IntOf(amount)))
    constructor(text: string)
        this(NonNegative(DollarsIn(text)))
    constructor(amount: Number)
        this.dollars = amount
```

The before shows the sign: the non-negative check guards only the string path. The after has one assignment, and the conversions and the check are objects, so it carries no sign of [[constructors-without-code]] either. The book puts the check in the primary constructor (p. 31). Section 1.3 and the author's reply on p. 42 forbid checks in a constructor, so this wiki places it in a wrapping object.

## Source

[[elegant-objects]]: pp. 28-33, and p. 42 for the author's reply against checks in a constructor. This wiki's own: the placement of the check in a wrapping object, the signs as worded, the split with [[constructors-without-code]], the limits on single constructors, default arguments and optional-field overloads, the repair steps and the pseudocode.

Related: A constructor that leaves a field unassigned is [[initialize-every-member-in-every-constructor]]; several constructors that each assign fields, without delegating to one, are [[one-primary-constructor]], and that repair, routing secondary constructors through the primary one, serves both pages.
