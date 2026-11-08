---
title: Choose a table access scheme
category: complexity
summary: "A lookup table of large entries mostly empty because the key's range is far wider than the entries, a table padded with duplicate rows for ranges, or a range if-chain over irregular thresholds: pick direct, indexed or stair-step access by key shape, memory and speed."
tags: [decision-rule, table-driven, lookup-table, performance]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

The first question for any table, in McConnell's terms, is how an entry is found. Some data indexes the table directly, as months 1 to 12 do. Other data cannot: a social security number cannot be a key unless you store 999-99-9999 entries (p. 405). The book gives three schemes: direct, indexed and stair-step (p. 406).

## Rule

Pick the scheme from the shape of the key.

- **Direct access** where the key, as is or through a simple transformation, is a dense index. It is simple and fast (p. 417). For fitting a key see [[isolate-table-key-computation]].
- **Indexed access** where the key's range is wide and the entries few. The raw data looks up a key in an index table, and that key finds the entry in the main table (p. 418). The book's warehouse has about 100 parts numbered 0000-9999. An index array of 10,000 small entries points into a main table of 100 (p. 418). With 100-byte main entries and 2-byte index entries, the index costs 30,000 bytes against 1,000,000 for a sparse main table (p. 419). The book adds that several indexes can order one table (by name, hire date, salary), and that index entries are cheaper to manipulate than main entries (p. 419).
- **Stair-step access** where each entry covers a range and the boundaries are irregular. The table holds the upper bound of each range, and a loop compares the value against them (pp. 419-420). It works well «с нестандартными данными», such as grade cut-offs or a probability distribution with values like 0,458747, for which no transformation into keys exists (pp. 420-421). It costs less memory than an index but is less direct (p. 419). Its boundary handling is [[stair-step-lookup-boundaries]].

Between stair-step and indexed: a stair-step search adds run-time overhead. Where speed matters, an index can trade memory for speed, as with 100 discrete percentages for grades. It is impossible where the keys are arbitrary reals (p. 422). For a long stair-step list, the book suggests a "quasi-binary" search that finds the category, not the value (pp. 421-422).

Where several schemes fit, the book, citing Butler Lampson, advises aiming for a good solution that avoids failure rather than hunting for the best one (p. 422).

## Sign in code

- A direct table of large entries (records, objects) sized to the key's whole range, in which most entries are empty or a sentinel: the 10,000-slot table of parts with 100 used. Indexed access is the case. An index array of small entries over that range is the repair, not the sign.
- A direct table with long runs of identical rows standing for ranges. Transform the key, or use stair-step if no simple transformation exists.
- An `if`/`else if` chain comparing one numeric value against a descending or ascending list of irregular thresholds and assigning a category; once a table is chosen, stair-step is the case.
- A linear stair-step scan over a long bounds list inside a loop. Binary search or an index is the case.

Whether a chain becomes a table is [[drive-repeated-dispatch-from-a-table]]; which access scheme the table uses is [[choose-table-access-scheme]]. A table padded with identical rows for ranges is [[choose-table-access-scheme]]; once it chooses a key transformation, the transformation lives in one routine in [[isolate-table-key-computation]].

## When not to apply

- The value is not chosen by lookup at all. [[drive-repeated-dispatch-from-a-table]] decides whether to use a table in the first place.
- This wiki adds that the memory argument for an index is the book's, made with 100-byte records. Where both tables are small, it decides nothing, and the simpler direct table wins.
- This wiki adds that duplicated rows are acceptable where the book's benefit of duplication applies (p. 417): one value in the range may later need its own entry, and the range is small enough that the copies can be checked by eye.
- This wiki adds that the speed argument for replacing stair-step applies only where the lookup has been measured as costly, so the fourth sign is reported only with such a measurement; see [[estimate-algorithm-order]].

## Repair

- Sparse direct table: replace it with an index array (or the language's map) from key to a slot in a dense main table, behind one access routine.
- Duplicated range rows or a threshold chain: keep a bounds array and a parallel result array, and write one stair-step lookup in its own routine.
- Slow stair-step: switch to a binary search for the category, or precompute an index if the value domain is small and discrete.

## Before and after

Before: a part table sized to every possible part number.

```
parts = array(10000)          // 100 used
parts[4711] = Part(...)
info = parts[partNumber]
```

After: a small index into a dense table, behind one routine.

```
partSlot = array(10000, fill = NONE)   // small entries
parts = [ Part(...), ... ]              // 100 entries

function partFor(number):
    slot = partSlot[number]
    if slot == NONE: fail("unknown part", number)
    return parts[slot]
```

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, sections 18.1-18.4, pp. 405-422; Lampson (1984) as cited there. The three schemes, the memory figures, the speed trade-off and the binary search suggestion are the book's. The signs (including the large-entry condition of the first, this wiki's reading of the book's 100-byte figures), the assignments against [[drive-repeated-dispatch-from-a-table]] and [[isolate-table-key-computation]], the limits and the pseudocode, including the missing-part handling, are this wiki's own.
