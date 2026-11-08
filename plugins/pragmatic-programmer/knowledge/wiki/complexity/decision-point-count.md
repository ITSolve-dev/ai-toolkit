---
title: Decision point count
category: complexity
summary: "A routine with more than 10 decision points (each if, while, repeat, for, and, or, and each case label), counted from 1: McCabe's cyclomatic measure."
tags: [rule, cyclomatic-complexity, metrics, routine-size]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell presents Tom McCabe's measure, the number of decision points in a routine, as perhaps the most important way of measuring complexity and the most useful for control flow (pp. 452-453). The reasoning: one unit of complexity is the number of things a reader must hold in mind at once; people struggle beyond five to nine such items (Miller, 1956), so the room to train that ability is small and the code must change instead (pp. 451-452). Control-flow complexity correlates with low reliability and frequent errors (p. 451); the book reports that at Hewlett-Packard McCabe's measure was used to find problem areas in a 77,000-line program that shipped at 0.31 defects per 1,000 lines (p. 451).

This wiki assigns the neighbouring cases as follows. This page owns the **count of branches in one routine**, whatever their depth. Depth belongs to [[tame-deep-nesting]], line count to [[routine-length]], and a single condition with many operands to [[name-complex-conditions]]. The same count sets the minimum number of tests in [[structured-basis-testing]]. The threshold of 10 decision points is [[decision-point-count]]; ranking units by their counts to pick what to read is [[metric-outlier-review]]; a first scan routing a mark to its owner is [[design-warning-signs]].

## Rule

Count decision points (Table 19-2, p. 452):

1. Start at 1.
2. Add 1 for each `if`, `while`, `repeat`, `for`, `and`, `or` or their equivalent.
3. Add 1 for each case in a `case` statement.

Read the count (p. 452): 0-5, the routine is probably fine; 6-10, start thinking about simplifying it; more than 10, move part of the routine into another routine and call it. The checklist asks of a routine above 10 whether there is a good reason not to redesign it (p. 453).

## Sign in code

The count above, run on one routine, exceeds 10. The book's own counting example: `if (((status = Success) and done) or (not done and (numLines >= maxLines)))` scores 5: 1, plus `if`, `and`, `or`, `and` (p. 452).

## When not to apply

- Ten is not an absolute limit; the book calls it a warning that the routine may need redesign: «Не считайте его неколебимым правилом» (p. 453).
- A `case` with many branches can exceed 10, and depending on its purpose splitting it «может быть глупо» (p. 453).
- Extraction does not make the program simpler; it only moves decision points (p. 452). It pays because the reader handles less at a time. This wiki reads that as: extracting a piece that the reader must still trace into to understand the caller gains nothing.
- The book names other measures: amount of data used, nesting levels, lines of code, variable span and live time, input/output volume (p. 453). A low decision count does not clear a routine of those.

## Repair

Move a coherent part of the routine into its own routine and call it (p. 452); simplify boolean expressions with named booleans, boolean functions or decision tables, and for depth use the repairs in [[tame-deep-nesting]] (checklist, p. 453). See [[extract-routine-to-name-a-step]] for choosing what to extract.

## Before and after

```
report(items)                                  // count: 1
    for item in items                          // 2
        if item.active and item.visible        // 3, 4
            if item.total > limit or item.flagged   // 5, 6
                warn(item)
            else if item.total == 0            // 7
                skip(item)
        if item.dirty                          // 8
            save(item)
            if item.remote and online          // 9, 10
                push(item)
            if item.audit                      // 11
                log(item)
```

```
report(items)                                  // 1
    for item in items                          // 2
        if isShown(item)                       // 3
            review(item)
        if item.dirty                          // 4
            persist(item)

isShown(item)                                  // 2
    return item.active and item.visible

review(item)                                   // 4
    if item.total > limit or item.flagged  warn(item)
    else if item.total == 0                skip(item)

persist(item)                                  // 4
    save(item)
    if item.remote and online  push(item)
    if item.audit              log(item)
```

Each routine now scores 4 or less. The total did not fall, which is the book's point about extraction moving decision points.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, section 19.6, pp. 450-453: see [[code-complete]]. The counting procedure, the thresholds, the case-statement limit, the remark that extraction moves decision points, the Miller and HP figures and the list of other measures are the book's. The reading that an extraction a reader must trace into gains nothing, the owner assignments and the pseudocode are this wiki's own. Related: [[structured-programming]], [[managing-complexity]].
