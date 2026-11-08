---
title: Group related data into a structure
category: types-and-state
summary: "The same run of three or more loose variables or parameters (name, address, phone, ssn...), or a pair that is one domain value (min and max, start and end), is copied, swapped or passed field by field at several sites, with no structure holding them, so adding a field means finding every site and nothing shows which variables belong to which entity."
tags: [rule, data-clump, parameter-list, records, maintenance]
paradigm: any
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

*Code Complete* (section 13.1) argues for gathering data that belongs together into one structure, meaning a record with public fields. It says that a class is usually the better choice, because a class adds hiding and behaviour to the data, and that directly handling blocks of data is still sometimes useful (Russian edition, pp. 310-311).

## Rule

When several variables describe one thing, declare them as one structure and handle the structure as a whole. The book gives four gains (pp. 311-314):

- **It shows which data belongs together.** Six assignments `name = ...` through `bonus = ...` look like one group. In fact the first three describe an employee and the last three a supervisor; `employee.name` and `supervisor.title` make that visible.
- **It simplifies block operations.** Copying an employee field by field takes six statements, and swapping two takes eighteen. With a structure, swapping takes three statements. «Это надежней и требует меньше строк кода.» (p. 311)
- **It shortens parameter lists.** `EasyWayRoutine(employee)` in place of `HardWayRoutine(name, address, phone, ssn, gender, salary)`.
- **It eases change.** Adding `numWithholdings` touches only the declaration, not every copy, swap and call. The book's point is that code which handles the set as a whole mentions each field only because it is part of the set, so a change to one field is easily missed there. That is exactly the code a structure spares from editing.

Fowler's **Data Clumps** smell is the same shape: the same three or four data items turn up together as fields in a couple of classes and as parameters in many method signatures, and "Bunches of data that hang around together really ought to find a home together" (*Refactoring*, 2nd ed., ch. 3, Data Clumps, PDF p. 92). He sets a low bar for acting: clumps that use only some of the new object's fields are no reason to hold back, and as long as two or more fields are replaced with the new object, the code comes out ahead (PDF p. 92). He also counts groups of primitives that appear together as data clumps (Primitive Obsession, PDF p. 93).

The catalogue entry **Introduce Parameter Object** (ch. 6, PDF pp. 158-164) treats the repair less as a way to shorten parameter lists than as the start of a new abstraction. Replacing "groups of data items that regularly travel together, appearing in function after function" with one structure makes their relationship explicit, shortens the lists, and gives every function the same names for the elements (PDF p. 159). The larger gain comes after: behaviour over the data moves into the new structure, which "can change the conceptual picture of the code, raising these structures as new abstractions" (PDF p. 159). His example ends with a `NumberRange` that owns a `contains` test, so the filter no longer spells out the comparison against a loose minimum and maximum (PDF p. 163). He prefers a class to a record, and usually a value object: no setters and, eventually, equality by value (PDF pp. 159, 161, 164).

## Sign in code

- The same run of three or more variables, with a shared prefix or one per entity, is assigned, copied or swapped field by field at more than one site.
- Several routines take the same run of parameters in the same order, and no structure holding them exists. Two suffice when the pair is one value of the domain (a range, a period, a coordinate) and passes the deletion test below; that threshold is this wiki's reading of Fowler's min/max example (PDF p. 159).
- The same pair is passed under different names at the two ends of a call (`floor`, `ceiling` at the caller, `min`, `max` in the callee), which Fowler notes in his example (PDF p. 161).
- Adjacent assignments mix fields of two different entities with nothing in the names to tell them apart.

Fowler's discriminating test separates a clump from values that merely sit side by side: "consider deleting one of the data values. If you did this, would the others make any sense?" If they would not, "you have an object that’s dying to be born" (PDF p. 92). This wiki applies that test to every sign above before reporting it.

This wiki assigns neighbouring cases as follows. Where callers read several fields of one existing object and the routine's job is about that object, [[pass-what-the-routine-uses]] owns the signature; where those fields form a value the source object does not model on its own (a range or a period held as two fields of a plan), [[group-related-data-into-a-structure]] owns it. A routine that takes the whole object but reads one field is [[pass-what-the-routine-uses]]. A parameter list too long whatever its contents is [[limit-parameter-count]]. One large structure passed to every routine, each using a different subset, is [[global-data]]. A shared name prefix as the only sign of the relation is discussed on [[naming-conventions]]. The same run of loose variables or parameters passed field by field at several sites, with no structure holding them, is [[group-related-data-into-a-structure]]; a group inside one class, shown by a shared prefix or by being passed together, is [[keep-objects-small]]. A field that already lives in an existing record but always travels with one other record is [[move-field]].

## When not to apply

The book sets the limit itself: «Аккуратные программисты избегают объединения большего количества данных, чем это необходимо логически.» (p. 313). A routine that needs one or two fields of a structure receives those fields and not the whole structure, because only what a routine needs to know should pass between routines; the book frames this as information hiding (p. 313).

Further limits, this wiki's own:

- Variables that merely sit side by side, but do not describe one thing and do not change together, are not a structure. Grouping them is a likeness by chance.
- If the group carries a rule (a range that must be valid, fields that must agree), the book's checklist question applies: should it be a class instead (p. 335)? The invariant then belongs to [[class-invariant]].
- The book's "fat structure" taken to the extreme, one structure holding everything and passed everywhere, is not this page's repair; it is a sign of [[global-data]].
- A project convention on how related values travel (positional tuples, keyword arguments, records generated from a schema) decides the form of the grouping.

## Repair

Declare a structure (or a class, where the data carries rules) holding the fields, replace the loose variables with fields of it, replace field-by-field copies and swaps with whole-value assignment, and pass the structure to the routines that use all or most of it. Pass the individual fields to routines that use only one or two of them. Fowler's mechanics for Introduce Parameter Object (PDF pp. 159-160): create the structure if none fits; add a parameter for it with [[change-function-declaration]] and test; make each caller pass an instance and test; for each element, switch uses of the old parameter to the structure's element, remove the parameter and test. Then look for behaviour over the data (a range test, equality, formatting) to move into the new type, and for other places where the same loose values appear (PDF p. 163). Fowler's order for a clump (PDF p. 92): look first where the clump appears as fields and use Extract Class on them, then slim the signatures with Introduce Parameter Object or Preserve Whole Object ([[limit-parameter-count]]). He prefers a class to a plain record, because a class opens the next step: behaviour elsewhere that envies the new class's data moves into it ([[information-expert]]), which he reports as a powerful way to remove duplication.

## Before and after

```
function save(name, address, phone, ssn, salary)
function print_badge(name, address, phone)

prev_name = old_name;  prev_address = old_address;  prev_phone = old_phone
old_name  = new_name;  old_address  = new_address;  old_phone  = new_phone
new_name  = prev_name; new_address  = prev_address; new_phone  = prev_phone
```

```
record Employee { name, address, phone, ssn, salary }

function save(employee)
function print_badge(employee)
function format_phone(phone)        // needs one field: gets one field

previous = old_employee
old_employee = new_employee
new_employee = previous
```

A pair that is one domain value, after Fowler's temperature-range example:

```
function readingsOutsideRange(station, min, max)
    return station.readings.filter(r -> r.temp < min or r.temp > max)

alerts = readingsOutsideRange(station, plan.temperatureFloor, plan.temperatureCeiling)
```

```
class NumberRange
    constructor(min, max)          // no setters
    contains(v): return v >= min and v <= max

function readingsOutsideRange(station, range)
    return station.readings.filter(r -> not range.contains(r.temp))

alerts = readingsOutsideRange(station, NumberRange(plan.temperatureFloor, plan.temperatureCeiling))
```

## Source

McConnell, *Code Complete*, 2nd edition, Russian edition, via [[code-complete]], section 13.1, pp. 310-314, and the chapter checklist, p. 335: the preference for classes, the four uses with their examples, and the limit against bundling more than is logically needed. The quotations of pp. 311 and 313 are transcribed from `raw/` and need the page-image check. This wiki's own: the signs and their threshold of three, the chance-likeness and project-convention limits, the splits with neighbouring pages, and the pseudocode. Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 3, "Data Clumps", PDF p. 92, and "Primitive Obsession", PDF p. 93: the smell, the low bar, the deletion test, the order of repairs and the preference for a class. This wiki's own for that part: applying the deletion test to every sign. Ch. 6, "Introduce Parameter Object", PDF pp. 158-164: the rule and its gains, behaviour moving in, the value-object class, the names differing at the two ends, the mechanics and the `NumberRange` example. This wiki's own for that part: the threshold of two for a domain pair, and the second pair of pseudocode.
