---
title: No two names with nearly the same meaning in one fragment
category: naming
summary: "One fragment holds two names for different values whose words mean nearly the same thing (input/inputValue, fileNumber/fileIndex, count/total for two counts), so swapping them compiles and is wrong."
tags: [rule, naming, semantics, confusable-names]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Some pairs of names are spelled differently but say nearly the same thing. A reader cannot tell from the words which variable holds which value. McConnell's examples are `input` / `inputValue`, `recordNum` / `numRecords` and `fileNumber` / `fileIndex` (p. 277).

## Rule

McConnell's rule is that if two names can be confused and the confusion will not cause a compile error, «переименуйте обе переменных» (p. 277). Renaming only one leaves the other just as vague. His reason is that names this close in meaning, used in one fragment, are easy to mix up, and the mix-up plants subtle errors (p. 277).

The checklist on the same chapter's last pages adds a related prescription: use `Count` or `Index` as the qualifier instead of `Num` (p. 280). This wiki reads that as the usual repair for the `recordNum` / `numRecords` case, since `Num` can mean either a count or a position.

## Sign in code

In one routine or class, two variables of compatible types holding different values, whose names:

- differ only by a filler word such as `Value`, `Data`, `Info` or `Obj` (`input` / `inputValue`);
- are the same words in a different order;
- use near-synonyms for the role (`fileNumber` / `fileIndex`, `count` / `total` for two different counts).

This wiki assigns the neighbouring cases as follows. This page owns two names that **mean** nearly the same thing and hold different values. Two names that **look or sound** alike are [[names-differ-by-more-than-a-character]]. Where the differing word is `Num` (`recordNum` / `numRecords`), [[computed-value-qualifier-at-end]] owns it. Two names holding one and the same value are [[one-name-per-concept]]. The same words in both orders on two different values (`totalPoints` / `pointsTotal`) are [[similar-meaning-names]]; one qualifier in both orders on different stems (`totalRevenue` beside `expenseTotal`) is [[computed-value-qualifier-at-end]].

## When not to apply

- This wiki's own limit: if the two variables have types the language will not let you swap, a mix-up fails to compile, so the source's stated condition (no compile error) is not met. That holds, for example, when one is a count and the other a record object, or a raw string and a parsed value of a distinct type. Renaming is still optional there.
- A pair that is genuinely the same value under two names is a duplication problem, not a naming one. Remove one variable instead of renaming both.

## Repair

Rename both names so that each states its own role: a count against a position, the raw form against the parsed form, the one being built against the one being read. In practice that means `recordCount` / `recordIndex`, `rawInput` / `parsedAmount`, or `fileCount` / `currentFileIndex`.

## Before and after

```
input = readLine()
inputValue = parse(input)
if input > limit:            // meant inputValue
    reject()
```

```
rawLine = readLine()
requestedAmount = parse(rawLine)
if requestedAmount > limit:
    reject()
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, pp. 277, 280 ([[code-complete]]). The rule, the three example pairs, the 'rename both' repair and the Count/Index-over-Num checklist item come from the book. The filler-word and word-order forms of the sign, the `count` / `total` example, the assignment against the neighbouring pages, the type-safety limit and the duplication limit are this wiki's own.
