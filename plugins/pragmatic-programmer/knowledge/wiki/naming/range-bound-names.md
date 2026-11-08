---
title: Name range bounds as first, last, lim, min or max, not as end
category: naming
summary: "A loop or range bound held in a variable named end, top, upper, bound or n, where the reader cannot tell whether it is inclusive or exclusive, or whether it belongs to the array or to the current pass, and it is compared with < at one site and <= at another."
tags: [rule, naming, off-by-one, loops]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell credits standardized prefixes with making names precise where they would otherwise be vague, and picks out the exact distinctions between `min`, `first`, `last` and `max` as especially useful (*Code Complete*, Russian edition, p. 273). These names answer the two questions an off-by-one error turns on: is the bound inclusive, and is it a property of the data or of the current operation?

## Rule

McConnell's table of semantic prefixes defines these meanings (Table 11-7, p. 273):

- `first` is the first element the current operation processes, and `last` is the last one. Both belong to the operation, not to the array.
- `min` and `max` are the indices of the array's first and last elements. They belong to the array itself: «Префикс max связан с самим массивом, а не с выполняемыми над массивом операциями» (p. 273).
- `lim` is the upper limit of the range being processed and is no longer a valid index. Unlike `last`, which is the last valid element, a `lim` value lies outside the range. «В общем, lim равняется last + 1.» (p. 273).

This wiki reads the rule as follows: a name for a bound should say which of these it is, so that `<` against `<=` can be checked by reading the name.

## Sign in code

- A bound held in a variable named `end`, `top`, `upper`, `bound` or `n`, compared with `<` in one place and `<=` in another.
- A variable named `max` or `last` that holds one past the last valid index, or a `size` used as if it were the last index.
- A sub-range loop (`for i from start to stop`) where nothing in the names tells whether `stop` is processed.

This wiki assigns the neighbouring cases as follows. Where the bound is a variable whose name hides whether it is inclusive, this page owns the sign. Where the loop compares directly against the array's length or a hard-coded number, with no named bound, [[array-index-discipline]] owns it. The name of the index itself (`i`, `j`) is [[loop-index-names]], and opposites paired unconventionally (`first`/`end`, `begin`/`last`) are [[computed-value-qualifier-at-end]].

## When not to apply

- This wiki's own limit: in a language or codebase where half-open ranges are the single, universal convention (every range written as `[begin, end)`, as standard library ranges often are), `end` is unambiguous by convention. Follow the project's idiom there. The source does not discuss such conventions.
- Iteration over a collection without explicit indices (`for each item in items`) has no bound to name.

## Repair

Rename the bound to say whether it is inclusive and what it belongs to: `lastProcessed` for an inclusive end of the current pass, `limit` or `lim` for one past it, `maxIndex` for the array's last valid slot. Then make each comparison agree with the name: `<= last`, `< lim`.

## Before and after

```
end = count(lines)                        // sign 2: a count used as the last index
for i from firstLine while i <= end:      // reads one past the data
    print(lines[i])
```

```
limLine = count(lines)                    // one past the last valid index
for i from firstLine while i < limLine:
    print(lines[i])
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, p. 273 ([[code-complete]]). The definitions of first, last, lim, min and max, the `lim = last + 1` relation, the operation-against-array distinction and the claim that these prefixes make names precise come from the book. Applying them as a guard against off-by-one comparisons, the sign list, the split with [[array-index-discipline]] and the half-open-range limit are this wiki's own.
