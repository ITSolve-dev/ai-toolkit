---
title: Comment what a declaration's name cannot carry
category: documentation
summary: "A local variable for a length, time, angle or amount carries no unit in its name, type or comment, so an assignment can join two quantities in different units unseen; a bit-flag word has no documented layout; a global has no stated role."
tags: [rule, comments, data, naming, documentation]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

**Commenting data declarations** is *Code Complete*'s rule that a declaration states what its name cannot: units, the valid range, the meaning of coded values, the layout of bits, and the role of global data. The book cites one company's finding that commenting data matters more than commenting the processes that use it (p. 784).

## Rule

- **Units of numeric quantities** (p. 784): inches or metres, seconds since a given epoch or milliseconds since start-up, degrees or radians, and which coordinate system. «Не предполагайте, что единицы измерения очевидны» (p. 784). They will not be obvious to a new programmer, to someone working on another part of the system, or to anyone after a major change. The book says the unit should often go in the name rather than a comment. `distanceToSurface = marsLanderAltitude` looks correct, while `distanceToSurfaceInMeters = marsLanderAltitudeInFeet` shows the error (p. 784).
- **Ranges of numeric values** (p. 784), for example a dollar amount between 1 and 100. In its cross-reference the book calls assertions at the start and end of a routine the more effective way to document ranges (p. 784, margin).
- **Meaning of coded values** (p. 784). Use an enumeration where the language has one. Otherwise comment each value and give it a named constant rather than a literal.
- **Limits on input data** (p. 785), expected and unexpected values alike, with assertions as the stronger option.
- **Flags down to the bit** (p. 785). Where the language has bit-field syntax, the fields document themselves.
- **The variable's name inside comments about it** (p. 785), so that a search for the variable also finds its comments.
- **Global data** (p. 786). At the declaration, state its role and why it must be global. At each use, make its global status visible, preferably by a naming convention, otherwise by a comment.

## Sign in code

- A local variable for a physical quantity, a duration, a timestamp, an angle or money has a plain numeric type and no unit in its name, its type or a comment.
- An assignment or comparison joins two such quantities whose units are visible on neither side of the line.
- Masks or shifts with numeric literals act on a flags word whose bit layout is stated nowhere.
- A mutable global or module-level variable is declared with no word on its role.

This wiki assigns the neighbouring cases as follows. A measure with no unit is judged by where it is declared: a parameter is [[name-by-role]], a stored field or constant is [[representation-that-fits-by-coincidence]], a local is [[comment-data-declarations]]; a line joining two of them goes to the page owning the left-hand side. A coded integer compared against bare literals (`style == 2`) is [[enum-instead-of-codes-and-flags]]. A bare mask literal is [[named-constants-over-literals]]; this page owns only the missing statement of the bit layout. Where [[global-data]]'s repair (pass it in) is taken, nothing is left to document; this page applies to a global that stays.

## When not to apply

- A type carries the unit or range, such as a `Duration`, a `Meters` value type or an enumeration. This wiki's reading of the book's preference for self-documenting forms (pp. 784-785) is that a comment is then redundant.
- The name already says it all. The book says well-named variables need no comment (p. 789).
- Loop counters and other locals that are not quantities.

## Repair

Use the strongest means the language offers, in this order. The ranking is this wiki's own arrangement of the book's preferences.

1. A type that carries the unit or the set of values: an enumeration, a value type, bit-field syntax.
2. The unit in the name (`altitude_in_feet`).
3. An assertion on the range at the routine's boundary; see [[state-the-contract]].
4. A declaration comment that names the unit, range or encoding.

Global data is better reduced than documented; see [[global-data]].

## Before and after

```
// before
distance_to_surface = lander_altitude
flags = read_status()
if flags & 0x04: ...
```

```
// after
distance_to_surface_in_meters = feet_to_meters(lander_altitude_in_feet)
flags = read_status()   // bit 0 ready, bit 1 error, bit 2 low fuel; rest unused
if flags & LOW_FUEL_BIT: ...
```

## Source

[[code-complete]], ch. 32.5, pp. 784-786 and p. 789. The book's parts: the list of what to comment, the Mars lander naming example, the preference for enumerations, named constants, bit-field syntax and assertions, and the treatment of global data. This wiki's own parts: the signs, the assignments against neighbouring pages, the limit for types that carry the unit, the ranking in the repair, and the pseudocode. The quotation was transcribed from the extracted text and should be checked against the page image.
