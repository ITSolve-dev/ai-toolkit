---
title: Digits in names stand in for a collection or a missing distinction
category: naming
summary: "Sibling variables told apart only by a trailing digit (file1, file2, total1, total2, x1, x2) instead of a collection or names that say how they differ."
tags: [rule, naming, collections]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

A digit suffix tells the reader that two variables differ, but not how. McConnell's examples are `file1` / `file2` and `total1` / `total2` (p. 278), and earlier in the chapter he notes that even once you know what `x` means, `x1` and `x2` say nothing about how the two relate (p. 255).

## Rule

McConnell's rule is that if digits in the names genuinely mean something, «используйте вместо отдельных переменных массив» (p. 278). If an array does not fit, the digits fit even less, and some better way to tell the two variables apart can almost always be found (p. 278).

## Sign in code

Two or more variables declared side by side whose names share a stem and end in different digits (`total1`, `total2`, `addr1`, `addr2`), especially when they are handled by repeated, near-identical statements.

This wiki assigns the neighbouring case as follows. This page owns siblings told apart by a digit. A single name too general for its value is [[name-describes-what-the-variable-represents]]. A digit appended to the type-named variable (`account`, `account2`) is [[numbered-names]]; a variable whose name is its type's name is [[type-name-vs-variable-name]].

## When not to apply

- McConnell's own limit: some real-world entities include a number in their name, such as Route 66. A digit that is part of the domain term (`route66`, `ipv4Address`, `sha256Digest`, `level2Cache`) is not this sign (p. 278).
- This wiki's own limit: a digit that names a position in a fixed, well-known structure, such as `x1, y1, x2, y2` for the two ends of a segment, is acceptable when a small record type would be heavier than the code using it. It still reads better as `start` / `end`.

## Repair

- If the variables are instances of one thing processed alike, replace them with a collection and a loop.
- If they play different roles, name each by its role: `sourceFile` / `targetFile`, `subtotal` / `grandTotal`.

## Before and after

```
total1 = sum(ordersOf(region1))
total2 = sum(ordersOf(region2))
report(total1)
report(total2)
```

```
for region in regions:
    report(sum(ordersOf(region)))
```

```
file1 = open(sourcePath)
file2 = open(targetPath)
```

```
sourceFile = open(sourcePath)
targetFile = open(targetPath)
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, pp. 255, 278 ([[code-complete]]). The rule, the array-or-better-distinction repair and the Route 66 exception come from the book. The sign's 'repeated near-identical statements' clause, the assignments against the neighbouring pages and the fixed-structure limit are this wiki's own.
