---
title: "Declare a named type for each kind of data that may change"
category: types-and-state
summary: "Many declarations of one kind of value (coordinates, employee names, ages) spelled with a built-in type (float, char[30]), a type alias named after its representation (BigInteger, LongString), or an alias that redefines a built-in name."
tags: [rule, types, typedef, information-hiding, naming]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

*Code Complete* calls programmer-defined types one of the most powerful ways to state your understanding of a program: they protect it from unforeseen change and make it easier to read, without designing, building or testing a new class (Russian edition, p. 303). Its example: coordinates declared as `Coordinate` rather than `float` change from single to double precision by editing one alias (pp. 303-304).

## Rule

Where a kind of data may change representation, declare a type for it and use that type at every declaration. The book's reasons (p. 306): modification is easier; information about the type is centralised instead of spread through the program, which it presents as [[information-hiding]]; in languages with range types the compiler can check values (Ada's `type Age is range 0..99`); and a missing built-in type can be supplied.

Its guidelines (pp. 307-308):

- **Name types after the problem, not the representation.** Coordinates, employee names, currency, payment codes, ages are real entities. «Такие имена, как BigInteger или LongString, описывают компьютерные данные, а не конкретную задачу.» (p. 307). Such names break the insulation from the language that the type was meant to provide.
- **Avoid built-in types outside type definitions** wherever the type may change. A named type also documents the variable: «Coordinate x сообщит вам об x гораздо больше, чем объявление float x» (p. 307).
- **Do not redefine built-in types.** An alias named `Integer` that is not the language's integer misleads readers who forget it was redefined.
- **Define substitutes for portability**, such as `INT32` instead of `int`, so the definition can change per platform; but do not choose names easily mistaken for built-ins (`INT` rather than `INT32`).
- **Consider a class instead of an alias.** An alias hides the underlying type only figuratively: users must not look at the definition. Where more flexibility and control are needed, a class does more (pp. 305-306, 308).

The book's aside on Pascal and Ada makes the gap explicit: a declaration with a range carries semantic information that `int temperature` does not, and a distinct `Temperature` type lets the compiler stop it being mixed with other integers. A class can enforce the same, but the distance between a one-line type and a class means a programmer often will not make the effort (p. 306).

## Sign in code

- The same kind of value (coordinates, identifiers, names, amounts) declared with a built-in type in many places, so changing its representation means editing each declaration.
- A fixed size for a kind of data repeated at its declarations: `char name[30]` in several structures.
- A type alias named after its representation (`BigInteger`, `LongString`, `Float64Value`) rather than after what it holds.
- An alias that reuses the name of a built-in type for something else, or a portability alias easily mistaken for a built-in.

This wiki assigns neighbouring cases as follows. This page owns declaring and naming a type for a kind of value. Two different kinds of value that share one primitive type, so that one can be assigned to, added to or compared with the other without complaint, are [[replace-primitive-with-class]]; one kind of value spelled with a built-in type at many declarations, so that a change of representation means editing each one, is [[define-domain-types]]. One quantity's primitive representation declared and compared across modules, so a change of representation spreads, is [[hide-secrets-behind-one-access-point]]. A numeric field for a phone number or a quantity with no unit is [[representation-that-fits-by-coincidence]]. Money in a floating type is [[exact-representation-for-money]]. A value whose rules (range, format, operations) must hold everywhere it is used belongs in a class or value type with its own invariant, [[class-invariant]]. A variable named after its type is [[type-name-vs-variable-name]].

## When not to apply

The book's own limit is to decide case by case whether a class would serve better than an alias (pp. 307-308). The limits below are this wiki's own:

- **A value used in one place** gains nothing from a type of its own.
- **A language where an alias is structurally identical to its base** gives readability and one place to change, but no checking: two aliases of `double` still mix. Where mixing is the risk, see [[replace-primitive-with-class]].
- **A language without type declarations** leaves only naming and, where available, type hints; the representation-change benefit then needs a class or a constructor function.
- **Cost when followed:** more types to learn, and conversions at boundaries with code that uses the built-in type.

## Repair

1. Identify each kind of value that is declared in several places and may change representation or range.
2. Declare a type for it, named for what it holds in the problem; derive any size from a named constant ([[named-constants-over-literals]]).
3. Replace the built-in type at every declaration of that kind of value.
4. Where a range must be enforced, make the type distinct or a small class rather than a transparent alias; where values of two kinds must not mix, see [[replace-primitive-with-class]].

## Before and after

```
function to_geo(x: float, y: float, z: float)
  latitude: float
  longitude: float
  elevation: float
  ...

record Employee
  name: char[30]
```

```
type Coordinate = float
const NAME_LENGTH = 30
type EmployeeName = char[NAME_LENGTH]

function to_geo(x: Coordinate, y: Coordinate, z: Coordinate)
  latitude: Coordinate
  longitude: Coordinate
  elevation: Coordinate
  ...

record Employee
  name: EmployeeName
```

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, chapter 12: the case for programmer-defined types and the `Coordinate` example, pp. 303-304; employee names and the length constant, pp. 304-305; information hiding with C++ aliases versus Ada private types, pp. 305-306; reasons for creating types and the Pascal/Ada aside, p. 306; guidelines on naming, avoiding and not redefining built-ins, and portability substitutes, p. 307; class instead of alias, p. 308. The quotations of p. 307 are transcribed from `raw/` and need the page-image check. This wiki's own: the signs as worded, all limits except the book's class-or-alias limit, the split with neighbouring pages, and the pseudocode.
