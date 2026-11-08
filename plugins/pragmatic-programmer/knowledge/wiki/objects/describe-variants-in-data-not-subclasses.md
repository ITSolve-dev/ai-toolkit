---
title: Describe variants in data, not subclasses
category: objects
summary: "N methods or N subclasses, one per record/message type, each a straight-line sequence of the same read/print/convert steps over a different field list, plus an if/factory chain on the type id: replace with one description table per type and one interpreter."
tags: [rule, table-driven, inheritance, polymorphism, interpreter]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

When variants differ only in *which* fields they hold and in what order, a subclass or a method per variant hard-codes data as control flow. McConnell's flexible message format example shows the function-per-type design and the class-per-type design costing the same, and a table of message descriptions beating both: «Сам факт, что проект использует наследование и полиморфизм, не делает его хорошим проектом.» (p. 416).

## Rule

Describe each variant's layout in a table, and write one routine that interprets any description. Keep polymorphism, if any, at the level of the few primitive kinds the descriptions are built from.

The book's case is about 20 kinds of buoy messages whose formats the customer keeps changing (pp. 410-411). The logical approach writes 20 print routines. The "mechanical" object-oriented approach writes an abstract message and 20 subclasses, and the top loop is still a 20-way choice that now creates objects (pp. 411-412). Each per-type body is a straight list: read a float, print "Average temperature", print the float, and so on. A 21st type needs a 21st routine or subclass, so any new type changes existing code (pp. 412-413).

The table approach lists the field types (float, integer, string, time of day, boolean, bit field) and describes each message as a list of (field type, label) entries (p. 413). The descriptions come in from outside, and «Данные обычно гибче программной логики» (p. 414). One routine walks a description and handles six field types; it is longer than one print routine, but it replaces all 20 (pp. 414-415). The book then removes the field-type `case` too: an `AbstractField` with `ReadAndPrint`, one subclass per field type, and an array of field objects indexed by field type, so the per-field code is `field[fieldType].ReadAndPrint(fieldName, fileStatus)` (pp. 415-416). If descriptions are read from a file, new message types need no code change unless they bring a new field type (p. 416); a new field type still needs code. The book's verdict: the design's substance is «не в объектной и не в функциональной ориентации, а в использовании хорошо продуманной таблицы поиска» (p. 416).

## Sign in code

- Several methods or subclasses, one per record or message type, whose bodies are straight-line runs of the same few primitive steps (read a value of type T, emit a label, emit the value) and differ only in the sequence of types and labels.
- An `if`/`switch` or factory chain on a type id whose every arm constructs or calls one of those per-type units.
- Adding a type is done by copying a subclass or method and editing its field list.

This wiki assigns ownership as follows. This page owns the per-type units and the chain that selects them. [[drive-repeated-dispatch-from-a-table]] owns a branch over a data value chosen at run time, whose arms hold the varying values or calls themselves. Where each arm instead constructs or calls a per-variant unit whose body is a fixed list of fields, [[describe-variants-in-data-not-subclasses]] owns it. A switch on a type tag of an object whose arms call per-kind behaviour of one operation is [[polymorphism-or-type-switch]]. Subclasses whose overrides only return constants are [[subclass-that-differs-only-in-data]]; subclasses each holding a sequence of steps over a different field list are [[describe-variants-in-data-not-subclasses]].

## When not to apply

- The variants differ in behaviour, not just layout: different validation, different algorithms, different collaborators. This wiki's view is that a description table would then need flags that recreate that behaviour, and subclasses (see [[prefer-interfaces-for-polymorphism]]) are the honest form.
- There are only a few variants and they are stable. This wiki's view is that the interpreter and description format then cost more than the copies.
- This wiki adds a trade-off the book does not state. A description read from a file moves layout errors from compile time to run time. Where that matters, validate descriptions on load or keep the table in code.

## Repair

1. List the primitive kinds the per-type bodies are made of. These become a closed enumeration.
2. Write each variant as a description: an ordered list of (kind, label) entries, keyed by type id.
3. Write one interpreter that looks up the description by id and walks it.
4. Dispatch on primitive kind through a small `case` or a table of handler objects or functions indexed by kind.
5. Delete the per-type units and the chain on type id.

## Before and after

Before: one class per message type, and a chain to pick it.

```
class BuoyTemperature extends Message:
    printFrom(input):
        print("Average temperature", input.readFloat())
        print("Temperature range",   input.readFloat())
        print("Number of samples",   input.readInt())
        print("Location",            input.readString())
// ... nineteen more like it

if id == 1: m = new BuoyTemperature()
else if id == 2: m = new BuoyDrift()
...
m.printFrom(input)
```

After: one description per type, one interpreter, a handler per field kind.

```
descriptions[BUOY_TEMPERATURE] = [
    (FLOAT, "Average temperature"), (FLOAT, "Temperature range"),
    (INT, "Number of samples"), (STRING, "Location") ]

handlers = { FLOAT: readPrintFloat, INT: readPrintInt, STRING: readPrintString }

for (kind, label) in descriptions[id]:
    handlers[kind](label, input)
```

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, section 18.2, pp. 410-416, and the checklist on p. 423 ("tables as an alternative to complex inheritance structures"). The example, the three designs compared and the claim that a new message type needs no code change are the book's. The signs, the splits with [[drive-repeated-dispatch-from-a-table]] and [[polymorphism-or-type-switch]], the behaviour-versus-layout limit, the run-time error trade-off and the pseudocode are this wiki's own.
