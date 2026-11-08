---
title: Computed-value qualifiers go at the end of the name; Count and Index instead of Num
category: naming
summary: "One module puts a qualifier in both orders across different quantities (totalRevenue beside expenseTotal, averageExpense beside revenueAverage); a count or position named with Num (numCustomers, customerNum); opposites paired unconventionally (begin/last, first/end)."
tags: [rule, naming, variables, consistency]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Many variables hold computed values such as totals, averages and maxima. McConnell advises putting the qualifier (`Total`, `Sum`, `Average`, `Max`, `Min`, `Record`, `String`, `Pointer`) at the end of the name (*Code Complete*, Russian edition, p. 256). He gives four reasons. The part that carries most of the meaning comes first and is read first. With one fixed order, `totalRevenue` and `revenueTotal` cannot both exist as different variables. A family such as `revenueTotal`, `expenseTotal`, `revenueAverage`, `expenseAverage` is symmetric. Consistent names are easier to read and maintain (pp. 256–257).

## Rule

- Put the computed-value qualifier last, and use the same order in every name of a module.
- Do not use `Num`. At the start of a name it means a total (`numCustomers`), and at the end it means an index (`customerNum`). McConnell says this still confuses readers often, and recommends `Count` or `Total` for the total and `Index` for a particular item: `customerCount`, `customerIndex` (p. 257).
- Use opposites in their conventional pairs: begin/end, first/last, locked/unlocked, min/max, next/previous, old/new, opened/closed, visible/invisible, source/target, source/destination, up/down. McConnell says pairs that are not common antonyms are harder to remember and confuse readers (p. 257).

## Sign in code

- Two orders of the same qualifier across different quantities in one scope (`totalPoints` beside `heightMax`, `maxSpeed` beside `pointTotal`).
- `num` as a qualifier, alone (`numCustomers`) or as a pair (`numX` beside `xNum`), where it stands for a count or a position.
- Mismatched pairs of opposites in one scope: `begin` with `last`, `first` with `end`, `start` with `stop` beside `begin` with `end`.

This wiki assigns the neighbouring cases as follows. This page owns qualifier order across different quantities, the `Num` qualifier and unconventional antonym pairs. Unconventional antonyms in routine names are [[routine-names]]; in variable names, [[computed-value-qualifier-at-end]]. The same words in both orders on two different values (`totalPoints` / `pointsTotal`) are [[similar-meaning-names]]; one qualifier in both orders on different stems (`totalRevenue` beside `expenseTotal`) is [[computed-value-qualifier-at-end]]. Two names for one and the same quantity (`pointTotal` and `totalPoints` holding one value) are [[one-name-per-concept]]. Two names for different values whose words mean nearly the same thing, where the differing word is not `Num`, are [[similar-meaning-names]].

## When not to apply

- A project or language convention that fixes the other order (for example `maxValue` everywhere) overrides this one. What matters is a single order, not which order. This wiki's reading of the book's reasons, three of which concern consistency.
- Names taken unchanged from a domain or an external API (`totalAmount` in a payment provider's schema) keep their form at that boundary.

## Repair

Pick one order (qualifier last, unless the project has decided otherwise) and rename the outliers. Replace `num` with `Count` or `Index` by meaning. Replace a mismatched opposite with its conventional partner.

## Before and after

```
totalRevenue = sum(revenues)
expenseTotal = sum(expenses)
averageExpense = expenseTotal / months
for customerNum from 0 to numCustomers - 1
    ...
```

```
revenueTotal = sum(revenues)
expenseTotal = sum(expenses)
expenseAverage = expenseTotal / months
for customerIndex from 0 to customerCount - 1
    ...
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 11.1, pp. 256–257 ([[code-complete]]): qualifier position and its four reasons, the `Num` exception and the `Count`/`Index` replacement, and the list of antonym pairs. The signs as worded, the assignment against the neighbouring pages, and the limit for a project convention and API boundaries are this wiki's own. The pseudocode is this wiki's own.
