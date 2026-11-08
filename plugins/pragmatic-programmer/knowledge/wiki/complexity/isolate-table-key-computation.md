---
title: Isolate table key computation
category: complexity
summary: "A table index computed inline (clamping with min/max, dividing into buckets, index-array lookups) at a lookup site, especially the same expression at two or more sites: move it into one named key function."
tags: [rule, table-driven, encapsulation, duplication]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Data does not always fit as a table key. McConnell's insurance rates have one rate for under-18s, one per age from 18 to 65, and one over 65, so `age` cannot index the table directly (p. 417). The book names two ways to fit the key, and one rule about where the fitting code lives.

## Rule

Put the operations that turn data into a table key in their own routine. The book's reason is that one routine «исключает возможность применения разных преобразований в разных местах» (pp. 417-418). It also makes the transformation easy to change, and a name such as `KeyFromAge()` documents what the arithmetic is for (p. 418). The same applies to index-access code: the book wants it in a separate routine so that the access scheme can be changed later (p. 419), and to stair-step lookups (p. 422). Where the environment offers a ready key mapping such as a hash map, the book says to use it (p. 418).

The two ways of fitting the key trade against each other (p. 417):

- **Duplicate entries** so the raw value is the key: copy the under-18 rate into every age from 0 to 17. The table stays simple and one age can later get its own rate by editing a value. The cost is storage and a higher chance of error, because the table holds redundant data.
- **Transform the key**: `max(min(66, age), 17)` maps every age into 17-66. This needs a good grasp of the key's structure and is not always that easy. If rates changed every five years, the function would also have to divide by 5.

## Sign in code

- A lookup whose index is an inline expression (clamping with `min`/`max`, integer division into buckets, offset arithmetic, or a lookup in an index array) rather than a call or a plain variable.
- The same index expression, or an index-array access, written at two or more lookup sites into the same table.

This wiki assigns the neighbouring cases as follows. A table padded with identical rows for ranges is [[choose-table-access-scheme]]; once it chooses a key transformation, the transformation lives in one routine in [[isolate-table-key-computation]]. An expression computing an index into a lookup table is [[isolate-table-key-computation]]'s, wherever it repeats; [[dry]] and [[name-repeated-subexpression]] defer to it.

## When not to apply

- The data is already a valid key: a month from 1 to 12, or an enum numbered from 0. The book's direct examples need no transformation (p. 417).
- The language's map type already does the mapping, as the book itself notes (p. 418).

## Repair

1. Find every site that computes an index into the table.
2. Move the computation into one function named for the key it produces (`keyFromAge`, `indexOfPart`).
3. Make each lookup call it.

## Before and after

Before: two sites clamp the age, and they disagree.

```
quote  = rates[max(min(66, age), 17)]
...
renew  = rates[max(min(65, age), 18)]
```

After: one routine fits the key.

```
function keyFromAge(age):
    return max(min(66, age), 17)

quote = rates[keyFromAge(age)]
renew = rates[keyFromAge(age)]
```

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, section 18.2 ("Подгонка значений ключа"), pp. 417-418; section 18.3, p. 419; section 18.4, p. 422; checklist, p. 423. The two fitting methods and their trade-offs, the rule to isolate the key computation, and the reasons for it are the book's. The signs, the assignment against [[choose-table-access-scheme]], [[dry]] and [[name-repeated-subexpression]], and the pseudocode are this wiki's own. Related: [[drive-repeated-dispatch-from-a-table]], [[choose-table-access-scheme]], [[dry]].
