---
title: Name length matches the variable's scope and how often it is used
category: naming
summary: "One-to-three-letter names (n, ns, lpp) on variables that live past a few lines, are fields or globals, or are rarely referenced; or the opposite, sentence-long names with articles and prepositions that drown statement structure."
tags: [rule, naming, variables, scope]
paradigm: any
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

McConnell places the best name length somewhere between `x` and `maximumNumberOfPointsInModernOlympics`. Names that are too short lack meaning. Names that are too long are tiresome to type and blur the program's visual structure (*Code Complete*, Russian edition, p. 255). He cites Gorla, Benander and Benander (1990): debugging took least effort when variable names averaged 10–16 characters, and almost as little at 8–20. He warns that this is no quota for every name. It is a prompt: code with many names well below that length should have them checked for clarity (p. 255).

## Rule

Choose the length by scope and use. A short name such as `i` tells the reader that the variable is minor and lives for a few lines. Citing W. J. Hansen (via Shneiderman, 1980), McConnell says longer names suit rarely used or global variables, and shorter names suit locals and loop variables (p. 255). He adds that short names cause many problems, and that some cautious, defensive programmers avoid them entirely (pp. 255–256). Many short names in one module are, by the book's rule of thumb, a prompt to check their clarity rather than a violation in themselves (p. 255).

Fowler's catalogue entry for Rename Variable states the same proportion (*Refactoring*, 2nd ed., ch. 6, PDF p. 156): "Naming things well is the heart of clear programming", and "the importance of a name depends on how widely it’s used". A variable in a one-line lambda can be a single letter because its context makes the purpose clear; parameters of short functions can be terse; "Persistent fields that last beyond a single function invocation require more careful naming" (PDF p. 156). He gives three reasons names go wrong: too little thought, a better understanding of the problem gained later, and a change in the program's purpose (PDF p. 156). This wiki reads that as: renaming is a normal, repeated act, not the correction of a one-off mistake.

The book's table of corrected names keeps the distinguishing words and drops the filler. `numberOfSeatsInTheStadium` becomes `numSeatsInStadium` or `seatCount`, and `maximumNumberOfPointsInModernOlympics` becomes `teamPointsMax` or `pointsRecord` (p. 255).

## Sign in code

- Names of one to three letters (`n`, `np`, `ns`, `lpp`) on a field, a global, a parameter of a public function, or a local whose uses are spread over more lines than fit on one screen.
- A short name used again far from its definition, so the reader has to scroll back to learn what it is.
- At the other extreme, names that read as full sentences with articles and prepositions (`numberOfPeopleOnTheUsOlympicTeam`), so that one statement wraps or its operators are hard to find.

This wiki assigns the neighbouring cases as follows. This page owns a name too short or too long for its scope, whatever its form. A shortened word whose form breaks the abbreviation rules (spelled two ways, one letter dropped, unpronounceable, phonetic) is [[abbreviation-discipline]]. `i`, `j`, `k` are [[loop-index-names]]. A short name used far from its binding is [[name-length-matches-scope]]; a conventional short name bound against its convention is [[follow-local-naming-culture]]. `temp`, `tmp`, `x` for an intermediate value are [[temporary-variable-names]].

## When not to apply

- A plain loop counter or array index used within a few lines, including the short body of a lambda: the short name is the signal the book describes. See [[loop-index-names]].
- **A published variable.** If code in another code base references it, Fowler says the variable is a published variable and the rename cannot be done as this refactoring (ch. 6, PDF pp. 156-157). This wiki reads that as: rename it only along a deprecation path its consumers can see ([[parallel-change]]).
- The 10–16 figure is an average across a program. It does not apply to any single name (p. 255).
- Where a scope is wide but the name is the established term of the domain or the formula, a short name can be complete. This wiki's reading; the book does not say it.

## Repair

- Too short and too wide in scope: expand the name to the phrase from [[name-describes-what-the-variable-represents]], then trim filler words.
- Too long: drop articles and prepositions, keep the words that tell it apart from neighbouring names, and move a qualifier to the end ([[computed-value-qualifier-at-end]]).
- Fowler's mechanics for the rename itself (ch. 6, PDF pp. 156-158). A local or parameter: change every reference and test. A widely used variable: encapsulate it first ([[encapsulate-variable]]), then rename the underlying variable inside its module; he then keeps the accessors, because a variable wide enough to need that for a rename makes it "worth keeping it encapsulated behind functions for the future" (PDF p. 158). A constant, or a variable read-only to clients: declare the new name, assign the old name from it, move references over one at a time with tests, then delete the old name; declaring the new and copying into the old makes it easy to put the old one back if a test fails (PDF p. 158).
- If a short name has to stay short but its scope is wide, narrowing the scope (extracting the block that uses it) is the alternative repair. This is this wiki's addition; see [[smallest-scope-first]].

## Before and after

```
class Stadium
    field ns

function report(stadium)
    ... forty lines ...
    print(stadium.ns)
```

```
class Stadium
    field seatCount

function report(stadium)
    ... forty lines ...
    print(stadium.seatCount)
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 11.1, pp. 255–256 ([[code-complete]]): optimal length, the Gorla–Benander study, the table of too-long, too-short and right names, and the Hansen finding on scope. The signs, the assignment against the neighbouring pages, the scope-narrowing repair and the limit for domain terms are this wiki's own.

Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 6, "Rename Variable", PDF pp. 156-158: naming as the heart of clear programming, importance in proportion to use, the lambda, short-function and persistent-field cases, the three reasons names go wrong, the published-variable limit, encapsulate-then-rename and copy-to-rename. This wiki's own for that part: reading renaming as a repeated act and the deprecation path for a published variable. A field whose name no longer matches what it stores is [[rename-when-meaning-drifts]]. The pseudocode is this wiki's own.
