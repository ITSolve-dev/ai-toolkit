---
title: Names in one scope differ by more than one character
category: naming
summary: "Two names in the same code for different things differ by a single inner letter, a transposed, doubled or dropped letter, only by case, by a look-alike character (1/l/I, 0/O, 2/Z, 5/S, 6/G) or only by sound (clientRecs/clientReps, shiftrn/shiftrm, SYSTSTS/SYSSTSTS, frd/FRD/Frd, wrap/rap)."
tags: [rule, naming, readability, confusable-names, psychological-distance]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Two names that look alike invite a reader to take one for the other. The compiler accepts either name, so the slip shows up as a wrong value at run time and never as an error. McConnell lists four forms of the hazard: names a single letter apart, names apart only in case, names apart only in characters that look alike, and names that sound alike.

His debugging chapter gives the measure behind them, *psychological distance*: how easily two items are told apart (p. 544). Given a list of words all about ducks, a reader easily confuses «Queck» with «Quack»; «Tuack» is harder to confuse though it also differs by one letter, because a first letter stands out more than a middle one (p. 544). His table of pairs (Table 23-1, p. 545) ranks `stoppt` / `stcppt` as almost invisible, `shiftrn` / `shiftrm` as almost none, `dcount` / `bcount` and `claims1` / `claims2` as small, and `product` / `sum` as large. His case from Weinberg: a programmer used `SYSTSTS` and `SYSSTSTS` as one variable until hundreds of runs had produced a book of wrong results (p. 543). The why is on [[mental-set-in-debugging]].

## Rule

McConnell's rule is to rename one of two names that have different meanings but are spelled almost alike. Of `clientRecs` and `clientReps` he says: «Они различаются только одной буквой, и это трудно заметить.» (p. 277). His repair rule is: «Выбирайте имена, различающиеся хотя бы двумя буквами или первой/последней буквой.» (p. 277).

The debugging chapter states the same rule for construction, «Выбирайте во время конструирования имена, ясно отличающиеся от других имен» (p. 545), and asks a debugger to be ready for defects caused by too little distance between similar names of variables and routines (p. 545).

He treats the related forms the same way (pp. 277-279):

- **Case only.** He rejects `frd`, `FRD` and `Frd` for three different concepts. The names are unique, but «их связь с конкретными значениями произвольна и непонятна» (p. 278).
- **Look-alike characters.** The pairs he names are (1, l), (1, I), (., ,), (0, O), (2, Z), (;, :), (S, 5) and (G, 6). Names that differ only in one of these cause trouble (p. 279). He adds Weinberg's story of a space probe lost because a comma stood where a period belonged in a Fortran FORMAT statement (p. 279).
- **Sound only.** Homophones such as *wrap* and *rap*, or *Goal Donor* and *Gold Owner*, break spoken discussion of the code. His check is the telephone test (pp. 277-278).

## Sign in code

Two identifiers for different things that appear in the same routine or class and meet any of these conditions:

- their edit distance is 1, or they differ by a transposed pair of letters, as in `clientRecs` / `clientReps`, `shiftrn` / `shiftrm`, `SYSTSTS` / `SYSSTSTS` or `total` / `totals` used for unrelated things;
- they are equal when case is ignored (`frd`, `Frd`, `FRD`);
- they are equal once look-alike characters are swapped (`ttl5` / `ttlS`, `eyeChart1` / `eyeChartl`, `GRANDTOTAL` / `6RANDTOTAL`);
- read aloud, they sound the same.

This wiki assigns the neighbouring case as follows. This page owns two names that **look or sound** alike and stand for different things. Two names that **mean** nearly the same thing are [[similar-meaning-names]]. Siblings told apart only by a trailing digit (`claims1` / `claims2`) are [[numbered-names]], even though McConnell's table also ranks that pair. One name bound at two scopes in one method, a local shadowing a field, is [[shadowed-field-names]].

## When not to apply

- This wiki's own limit: a one-letter difference that comes from a systematic, well-known pair is not this sign, provided the two cannot be swapped without a visible type mismatch. Examples are `x` / `y` as coordinates, or the singular `item` and the plural `items` for an element and its collection. The source does not discuss such pairs.
- A type and a variable of that type that differ only in the case of the first letter (`Widget widget`) are a convention question. McConnell counts names differing only in the first letter's case as too little psychological and visual distance, yet lists the form among trade-offs and does not ban it (p. 265); the project's convention decides it ([[naming-conventions]], [[follow-local-naming-culture]]).

## Repair

Rename one name, or both, until they differ in at least two characters or in the first or last character. McConnell's example is `clientRecords` / `clientReports` (p. 277). Prefer the full word to an abbreviation; this wiki's reading is that most collisions come from shortening (see [[abbreviation-discipline]]). Where an abbreviation is still needed, a synonym can break the collision: *fired* becomes *dismissed* and *full revenue disbursal* becomes *complete revenue disbursal*, giving `dsm` and `crd` instead of two `frd` (p. 275).

## Before and after

```
clientRecs = loadRecords(client)
clientReps = loadRepresentatives(client)
for r in clientReps:          // meant clientRecs; nothing complains
    archive(r)
```

```
clientRecords = loadRecords(client)
clientRepresentatives = loadRepresentatives(client)
for record in clientRecords:
    archive(record)
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, pp. 265, 275, 277-279 ([[code-complete]]). The rule, the two-letter / first-last-letter repair, the case-only, look-alike-character and homophone cases, and the telephone test come from the book. From its chapter 23 (pp. 543-545) come psychological distance, the duck example, Table 23-1, the `SYSTSTS` case and the construction and debugging rule. The edit-distance phrasing of the sign, the transposition case, the assignments against [[similar-meaning-names]] and [[numbered-names]] the limit for systematic pairs (`x`/`y`, `item`/`items`) and the reading that most collisions come from shortening are this wiki's own. The synonym repair (p. 275) is the book's.
