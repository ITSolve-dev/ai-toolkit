---
title: Replace an overloaded primitive with a class
category: types-and-state
summary: "Two different quantities (money and temperature, a price and a quantity, ids of two different entities) share one bare int, float or string type, so assigning, adding or comparing one with the other compiles; or one domain value held as a primitive whose range or format check, comparison or formatting (priority == \"high\" or \"rush\", slicing an area code out of a phone string) is written out again at several use sites."
tags: [rule, primitive-obsession, types, value-types]
paradigm: any
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

A primitive type can stand for an endless number of real-world things, so the compiler cannot tell them apart. McConnell's example: if both money and temperature are integers, nothing warns about `bankBalance = recordLowTemperature` (p. 555).

## Rule

When a common entity is represented by a primitive, consider a small class for it, so the compiler can type-check it and assignments can be validated (p. 555).

Fowler's **Primitive Obsession** adds the behaviour side. Many programmers are "curiously reluctant" to create small types for their domain, such as money, coordinates or ranges (*Refactoring*, 2nd ed., ch. 3, Primitive Obsession, PDF p. 93). The result is money handled as plain numbers, physical quantities that ignore units (inches added to millimetres), and a lot of code like `if (a < upper && a > lower)` (PDF p. 93). Strings are the commonest case: "Representing such types as strings is such a common stench that people call them “stringly typed” variables" (PDF p. 93). Fowler adds that, if nothing else, a proper type can hold consistent display logic (PDF p. 93).

The catalogue entry **Replace Primitive with Object** (formerly Replace Data Value with Object and Replace Type Code with Class; ch. 7, PDF pp. 199-204) starts from a fact recorded as a number or string that stops being simple. His example is a telephone number held as a string that later needs formatting and area-code extraction: "This kind of logic can quickly end up being duplicated around the code base" (PDF p. 200). The trigger is wanting to do something with the value other than print it; at first the class only wraps the primitive, but "once I have that class, I have a place to put behavior specific to its needs" (PDF p. 200). He reports that many experienced developers count it among the most valuable refactorings, though it often seems counterintuitive to a new programmer (PDF p. 200).

## Sign in code

- A primitive field or variable whose kind or unit is carried only by its name or a comment (`balance: int // cents`), declared beside a value of another kind with the same primitive, so assigning, comparing or adding one to the other compiles (p. 555).
- A routine with two or more parameters of one primitive type that mean different quantities (`charge(int customerId, int amountCents)`), so the call site gives no guard against mixing them.
- A domain value held as a primitive whose rule, such as a range check or a format check, is written out again at each of two or more use sites (`if amount > 0 and amount < limit` in several routines), where a type could hold the rule once. This sign is this wiki's reading of Fowler's range example (PDF p. 93), of his phone-number motivation (PDF p. 200), where formatting and area-code extraction get duplicated, and of his priority example (PDF pp. 200-204), where the operation is a comparison against string literals.

This wiki assigns the neighbouring cases as follows. A range or format check on one domain value held as a primitive, written out again at two or more use sites, is [[replace-primitive-with-class]], whose type holds the check once; a compound condition over several values, or one not tied to a single domain value, is [[name-complex-conditions]]. Any other repeated fact is [[dry]]. This page owns different quantities mixable because they share a primitive. A closed set of alternatives held as integer codes is [[enum-instead-of-codes-and-flags]]; a closed set held as strings is [[replace-primitive-with-class]] where call sites validate it or compare its values by order or by membership in a subset (`== "high" or == "rush"`), and [[enum-instead-of-codes-and-flags]] where they only test equality with single alternatives (this split is this wiki's own); one quantity's primitive representation declared and compared across modules, so a change of representation spreads, is [[hide-secrets-behind-one-access-point]]; the same run of loose values passed together is [[group-related-data-into-a-structure]]; two arguments of the *same* quantity that can be swapped at a call site (two account ids) are [[match-arguments-to-parameters]], while arguments of *different* quantities sharing one primitive are this page. Two different kinds of value that share one primitive type, so that one can be assigned to, added to or compared with the other without complaint, are [[replace-primitive-with-class]]; one kind of value spelled with a built-in type at many declarations, so that a change of representation means editing each one, is [[define-domain-types]]. A parameter whose unit cannot be read from its name is [[name-by-role]]; two parameters of different kinds sharing one primitive, readable or not, are [[replace-primitive-with-class]].

## When not to apply

- This wiki's limit: a local value whose meaning is plain from one short scope, such as a loop index or a count, gains nothing from a class.
- The book's refactoring converts a primitive into a class when it needs added behaviour, such as stricter type control, or added data (p. 559). This wiki reads that as a limit: a primitive needing neither gains nothing from a class, and a distinct nominal type (not a transparent alias) is enough where the language offers one.
- **A value only stored and printed.** Fowler's trigger is wanting "to do something other than simple printing" (PDF p. 200). A primitive passed through and printed unchanged, with no formatting repeated at its use sites, has no behaviour to gather.
- This wiki's limit: a project convention, or a hot path that keeps bulk numeric data as primitives (arrays of samples), overrides this rule.
- This wiki's limit: at a boundary with a format or library that speaks primitives (serialisation, a database driver), the primitive belongs there; convert at that edge ([[convert-input-at-entry]]).

## Repair

Introduce the type, give it its validation and the operations that belong to it, and change signatures and fields to take it instead of the primitive. Fowler's name is Replace Primitive with Object. His mechanics (ch. 7, PDF pp. 200-204):

1. Encapsulate the field behind a getter and setter if it is not already ([[encapsulate-variable]]).
2. Create a value class whose constructor takes the existing value. Fowler prefers a conversion such as `toString` to a `value` getter, because asking for the string "should feel more like a conversion than getting a property" (PDF p. 202).
3. Make the setter build an instance and the getter return its conversion. Test.
4. Rename a getter the change has made misleading: once a `Priority` class exists, the getter returning its string is `priorityString` (PDF p. 202).
5. Move behaviour into the class (validation against the legal values, equality, ordering) and decide whether it is a value object; Fowler's `Priority` gets `equals` and is made immutable (PDF pp. 203-204; [[object-equality]], [[immutable-objects]]). Where the primitive is a type code that controls conditional behaviour, he uses Replace Type Code with Subclasses and then Replace Conditional with Polymorphism ([[polymorphism-or-type-switch]]); primitives that travel together are Extract Class and Introduce Parameter Object ([[group-related-data-into-a-structure]]) (PDF p. 93).

## Before and after

```
// before
balance: int          // cents
lowestTemperature: int
balance = lowestTemperature        // compiles
```

```
// after
balance: Money
lowestTemperature: Temperature
balance = lowestTemperature        // rejected by the compiler
```

Behaviour repeated at call sites, after Fowler's priority example:

```
// before
class Order
    priority: String

highCount = orders.filter(o -> o.priority == "high" or o.priority == "rush").count()

function expedite(o)
    if o.priority == "high" or o.priority == "rush"
        courier.book(o)
```

```
// after
class Priority
    legalValues = ["low", "normal", "high", "rush"]
    constructor(value)
        if value not in legalValues: raise Invalid(value)
        this.value = value
    higherThan(other): return index(this.value) > index(other.value)
    equals(other): return this.value == other.value
    toString(): return this.value

highCount = orders.filter(o -> o.priority.higherThan(Priority("normal"))).count()

function expedite(o)
    if o.priority.higherThan(Priority("normal"))
        courier.book(o)
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition: [[code-complete]], section 24.2, p. 555, and section 24.3, p. 559. The rule, the money-temperature example and the conversion of a primitive needing added behaviour or data are the book's. The wording of the first sign, the second sign, the assignments against neighbouring pages, the limits (including reading p. 559 as a limit) and the pseudocode are this wiki's own. Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Primitive Obsession", PDF p. 93: the reluctance, money, units and range checks, stringly typed values, display logic, and the three repairs. This wiki's own for that part: the repeated-rule sign. Ch. 7, "Replace Primitive with Object", PDF pp. 199-204: the phone and priority examples, the duplication, the printing trigger and its limit, the place for behaviour, the mechanics, the conversion preference, the getter rename and the value object. This wiki's own for that part: extending the third sign to comparisons and duplicated formatting, the split with [[enum-instead-of-codes-and-flags]] for string-valued closed sets, and the second pair.
