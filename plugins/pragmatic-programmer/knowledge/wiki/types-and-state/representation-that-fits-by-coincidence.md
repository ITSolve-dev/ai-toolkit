---
title: A representation that fits only by coincidence
category: types-and-state
summary: "A phone number or identifier in a numeric field, key-value pairs in an array searched by first match, a fixed conversion between units whose size depends on place, or a bare quantity with no unit."
tags: [rule, data-representation, assumptions, duplicate-keys, units]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

A data shape can work on every value seen so far and still be wrong for the data's real domain. The book's answers show this in three unrelated places, and in the phone case it uses the word itself: fitting local numbers in a numeric field is «простым совпадением» (p. 360). This wiki reads that as [[programming-by-coincidence]] applied to data.

## Rule

Choose a representation from what the data's domain allows, not from the values in hand. The book's cases are these.

- **Numeric field for phone numbers.** It suffices for the USA, Canada and the Caribbean, but the international format begins with `+`, some local networks use `*`, and numbers can have leading zeros. The answer concludes: «Поэтому номера телефонов ни в коем случае нельзя хранить в числовом поле.» (p. 360).
- **Key-value pairs in an array.** Hash libraries usually guarantee unique keys, either through their own behaviour or by reporting duplicates, and an array imposes nothing of the kind. Where a lookup scans the array, «одерживает верх первая же запись» and the others are ignored. Because the order is not guaranteed, the structure works in some runs and fails in others (p. 360).
- **A named unit whose size depends on place.** The exercise's code converts with a fixed 16 cups to the gallon. The answer says that depends on where you are: in Canada one cup can mean 227, 236, 240 or 250 ml, and on a rice cooker it means 180 ml (p. 360).

This wiki reads the third answer as a warning about a number whose meaning comes from local practice, and extends it to a quantity with no unit at all, which leaves the same question open.

A neighbouring case is on [[externally-controlled-identifier]]: there the problem is using such a value as a key, and here it is the type chosen to hold it.

## Sign in code

- A field for a phone number, postal code or similar identifier declared with a numeric type.
- A list of key-value pairs read by linear search for the first match, with no check for duplicates at construction.
- A constant converting between units whose size depends on place, such as cups per gallon.
- A numeric field or constant for a measure with no unit in its name or type. A measure with no unit is judged by where it is declared: a parameter is [[name-by-role]], a stored field or constant is [[representation-that-fits-by-coincidence]], a local is [[comment-data-declarations]]; a line joining two of them goes to the page owning the left-hand side.

This wiki assigns the neighbouring case as follows. This page owns an assumption built into a data shape. An assumption about the surroundings, such as the environment, the current directory, the network or the clock, is [[do-not-rely-on-unguaranteed-context]].

## When not to apply

The book states no limits here. The limits below are this wiki's own.

- The value is really a number: the code does arithmetic on it or compares it by magnitude. This is the test separating a quantity from an identifier made of digits.
- First-match order is the intended behaviour, as in a list of rules where the order is defined and documented. The book's failure needs an order nobody guarantees.
- Uniqueness is enforced where the list is built, so the array is only a storage choice.
- The whole program uses one unit and values never cross a boundary. A named constant for the unit may be enough.

## Repair

1. Ask what values the domain allows, beyond those seen so far.
2. Keep identifiers made of digits as text, with format validation at the boundary.
3. Load key-value data into a structure that rejects or reports duplicate keys.
4. Put the unit in the type, or at least in the name. Where the unit's size depends on place, state the place too.

## Before and after

Before: each line works on current data.

```
record Customer
  phone: integer

settings = [("host", "a"), ("port", 80), ("host", "b")]
value = firstMatch(settings, "host")

CUPS_PER_GALLON = 16
```

After: each line states what the domain allows.

```
record Customer
  phone: text   // validated, keeps "+", "*" and leading zeros

settings = mapRejectingDuplicates([("host", "a"), ("port", 80), ("host", "b")])   // stops here, naming "host"
value = settings["host"]

cups_per_gallon = measures_for(locale).cups_per_gallon   // the cup's size is stated per place
```

## Source

[[pragmatic-programmer]], Thomas and Hunt, 20th Anniversary Edition, Russian translation (Dialektika, 2020), answers to exercises 25, 26 and 27, p. 360. The cases and reasoning are the book's, apart from the extension of exercise 27 to quantities with no unit, which is this wiki's own. The unifying rule, the signs, the assignment of the neighbouring cases, the limits, the repair and the pseudocode are this wiki's own. Related: [[do-not-rely-on-unguaranteed-context]].
