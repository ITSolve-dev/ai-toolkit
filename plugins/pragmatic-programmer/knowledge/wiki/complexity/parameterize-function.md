---
title: Functions that differ only in literal values
category: complexity
summary: "Two or more functions with the same body except for the literal numbers or strings in it (tenPercentRaise / fivePercentRaise; bottomBand / middleBand / topBand over hard-coded boundaries); merge them into one function taking the literals as parameters."
tags: [rule, duplication, parameters, parameterize-function]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

**Parameterize Function**, formerly Parameterize Method, removes the duplication of functions that carry out very similar logic with different literal values, by one function with a parameter for each value (*Refactoring*, 2nd ed., ch. 11, PDF p. 347). It is a specific shape of [[dry]].

This wiki assigns the neighbouring cases as follows. Functions whose bodies differ only in literal values are [[parameterize-function]]; functions that share opening and closing lines and differ in the algorithm between them are [[similar-functions-varying-middle]]. Sibling subclass methods that differ only in values are parameterized here first and then pulled up as a separate step ([[pull-up-method]]). A method whose whole body returns a constant, overridden per subclass, is [[subclass-that-differs-only-in-data]]; sibling methods with a computing body that differs only in literals are [[parameterize-function]].

## Rule

Replace the family with one function whose parameters are the values that varied. Fowler adds that this also increases the function's usefulness, because it can now be applied elsewhere with other values (PDF p. 347).

## Sign in code

- Two functions, often named after a value (`tenPercentRaise`, `fivePercentRaise`), whose bodies are identical except for one or more literals (PDF p. 348).
- A set of functions over adjacent ranges whose boundaries are hard-coded (`bottomBand`, `middleBand`, `topBand` over 100 and 200, PDF p. 348). Fowler notes the likeness here is "a touch less obvious" than the trivial case (PDF p. 348), yet still enough.

## When not to apply

- The source states no limit. This wiki adds: when the literals mean different things in the domain and are expected to diverge in logic, not just in value, the likeness is chance and merging them couples two rules ([[coincidental-duplication]]).
- This wiki adds: when callers would only ever pass the same literal at every site, the parameter adds a point of variation nobody uses ([[minimal-but-complete-functionality]]).

## Repair

Fowler's mechanics (PDF p. 347):

1. Pick one of the similar functions; with ranges, start with the middle one, as it shows both boundaries (PDF p. 349).
2. Use [[change-function-declaration]] to add the literals as parameters, renaming the function to fit (`middleBand` becomes `withinBand(usage, bottom, top)`); make each caller pass the literal. Test.
3. Replace each literal in the body with its parameter, testing after each.
4. Replace each similar function's calls with calls to the parameterized one, adjusting it if it does not yet fit. The top band needs an infinite upper bound (PDF p. 350).

Fowler keeps a guard clause for negative usage that became logically unnecessary, because it "documents how to handle that case" (PDF p. 350).

## Before and after

```
function lowTier(usage)
    return min(usage, 100)
function midTier(usage)
    return usage > 100 ? min(usage, 200) - 100 : 0
function highTier(usage)
    return usage > 200 ? usage - 200 : 0

charge = lowTier(u) * 0.03 + midTier(u) * 0.05 + highTier(u) * 0.07
```

```
function withinTier(usage, bottom, top)
    return usage > bottom ? min(usage, top) - bottom : 0

charge = withinTier(u, 0, 100) * 0.03
       + withinTier(u, 100, 200) * 0.05
       + withinTier(u, 200, infinity) * 0.07
```

## Source

- [[fowler-refactoring]], ch. 11, Parameterize Function, PDF pp. 346-350: the rule, the raise and band examples, the mechanics, starting from the middle range, infinity for the top band, the kept guard clause. The pull-up ordering is from ch. 12, Pull Up Method, PDF p. 390.
- This wiki's own: both limits (the source gives none), the owner assignments, and the pseudocode pair, after the book's band example.
