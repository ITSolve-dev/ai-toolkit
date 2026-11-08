---
title: A field's type states the cardinality of its association
category: types-and-state
summary: "A field for an optional (0..1) association dereferenced at a use site with no absence check, while another site checks it; a to-many association held as a collection that may be null as well as empty, so callers test two kinds of 'none'; or a 1..n collection that a constructor may leave empty or a remove may empty, or a fixed upper bound with no check on add."
tags: [rule, cardinality, associations, null, optional]
paradigm: oop
sources: [object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

Every association between classes has a **cardinality**: how many objects take part, and whether taking part is required. Weisfeld, after Gilbert and McCarthy, defines it as the number of objects in an association together with whether participation is required or optional (p. 188). His worked case is an `Employee` with exactly one `Division` (required), one or more `JobDescription`s (required), at most one `Spouse` (optional) and any number of `Child`ren (optional) (pp. 188-189, table 9.1). The code he shows holds the to-many associations as arrays (p. 191).

Chapter 10 returns to the same `Employee` as diagram notation and calls the cardinality indicator «очень важная часть объектной модели» (p. 205). It writes the counts as 1, 0..1, 0..n and 1..n, and notes what separates the last two: an employee has at least one job description, whereas children may be absent (p. 205). A computer has exactly one motherboard and at least one memory module, up to what the motherboard supports, so with six known slots the count is 1..6 (pp. 204-205). The book also warns that a count is a modelling decision to revisit: in some settings one person works in two divisions, for instance in the mathematics and the computer science departments of a college (p. 205).

## Rule

For each association, settle the book's three questions: which objects interact with which, how many take part in each interaction, and whether the interaction is required (p. 188). Code using an optional association must handle its absence: «Важно, чтобы код проводил проверку на предмет условия null, а также обрабатывал его как допустимое условие» (p. 191). If there is no spouse, no `Spouse` method may be called, or the application may crash; the code has to process an `Employee` who has none (p. 191).

This wiki extends the rule to the many-sides: a 0..n association is a collection that may be empty, never a collection that may also be null. The book shows only arrays and the null check.

## Sign in code

These signs are this wiki's reading of p. 191.

- A field that the class leaves unset on some path (no constructor assigns it, or a setter or loader can clear it) is dereferenced at a use site with no check, while another site does check it: the cardinality lives in callers' habits, not in the type.
- A to-many association held as a collection that can be null as well as empty, so callers test both.
- A 1..n association (the book's job descriptions, p. 205) held in a collection that a constructor may leave empty, or from which a remove operation may take the last element with no check.
- A fixed upper bound the model states (the book's 1..6 memory slots, pp. 204-205) with no check where elements are added.

This wiki assigns the neighbouring cases as follows. A constructor that leaves a *required* field unassigned is [[initialize-every-member-in-every-constructor]]. A field left null by the constructor and filled by a setter, and code that branches on whether it is null to choose behaviour, is [[null-field-hides-another-class]]. A check that only rejects use before the field is set (Weisfeld's `myCab`, p. 93) is [[initialize-every-member-in-every-constructor]] (class side) or [[temporal-coupling]] (call side). An optional association whose absence the code must handle (`Employee.spouse`) is [[association-cardinality-in-field-types]]. Whether absence is a null object or an option type is [[null-object-or-optional]]. A method returning null on a not-found path is [[never-return-null]]. This page owns an optional association used without its absence being handled.

## When not to apply

These limits are this wiki's own.

- Where the language or the project expresses optionality in the type (an option type, non-nullable references, a null object), follow that convention instead of manual checks. The book's null check is how its Java example states the rule. Under the *Elegant Objects* convention, which forbids `NULL` ([[never-return-null]]), the rule reads: absence is representable and handled, as a distinct type or a null object.
- A field that every constructor assigns and nothing clears is not optional, even if the language allows null. Checks for it are defensive noise.
- An upper bound on a many-side (the book allows capping the number of children the system handles, p. 189) is a design decision, not a defect. Where the model does fix one, a bound taken from hardware or configuration is better checked against a value supplied at run time than fixed in the type.
- A count the model has not settled, as in the two-divisions case (p. 205), is a modelling question; the page fires only on a count the model has fixed.
- An object built in several steps (a builder, a form being filled in) may hold fewer parts for a while; the check belongs where it becomes usable.

## Repair

1. Write down each association's cardinality (1, 0..1, 1..n, 0..n) from the book's three questions.
2. Optional (0..1): give it a type or accessor that makes absence explicit, and handle the absent case at every use as a valid path, not an error.
3. Many-sides: initialise the collection empty and never assign null; for 1..n require at least one element at construction, and let the remove operation refuse to take the last one.
4. A fixed upper bound: check it where elements are added.

## Before and after

```
class Employee
  field spouse          // optional, may be unset
  field children        // may be null

  hasSpouse()
    return spouse != null                    // one site checks

  anniversaryReminder()
    return "Anniversary: " + spouse.anniversaryDate()   // another does not

  hasChildren()
    if children == null or children.isEmpty()   // two kinds of 'none'
      return false
    return true
```

```
class Employee
  field spouse = NONE   // 0..1: explicit absence
  field children = []   // 0..n: empty, never null

  hasSpouse()
    return spouse is not NONE

  anniversaryReminder()
    if spouse is NONE
      return NO_REMINDER
    return "Anniversary: " + spouse.anniversaryDate()

  hasChildren()
    return not children.isEmpty()
```

A 1..n association that a remove can empty:

```
class Employee
  field jobDescriptions = []

  constructor(name)
  removeJob(job)
    jobDescriptions.remove(job)
```

```
class Employee
  field jobDescriptions

  constructor(name, firstJob)
    jobDescriptions = [firstJob]
  removeJob(job)
    if jobDescriptions.size == 1
      fail "an employee keeps at least one job description"
    jobDescriptions.remove(job)
```

## Source

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), ch. 9, via [[object-oriented-thought-process]]: cardinality and the three questions after Gilbert and McCarthy (p. 188), the `Employee` example and table 9.1 (pp. 188-189), to-many associations as arrays and the null check for optional ones (p. 191). Ch. 10, pp. 204-205: the counts in notation, 1..n against 0..n, the 1..6 memory slots, the importance of the indicator, the two-divisions caveat. The quotations were checked against `raw/`. This wiki's own: the extension to many-sides, both signs, the owner assignments, the limits, the settlement with the no-null convention, the 1..n and upper-bound signs, the limits on run-time bounds, unsettled counts and objects under construction, the repair and the pseudocode.

Related: [[aggregation-vs-association]].
