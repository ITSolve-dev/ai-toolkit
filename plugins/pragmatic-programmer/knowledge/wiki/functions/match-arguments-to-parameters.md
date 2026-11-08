---
title: Make argument-to-parameter matching checkable
category: functions
summary: "A call passes several adjacent arguments of the same quantity positionally (Transfer(from, to, amount) with two account ids, Move(srcId, dstId)), so swapping two compiles and runs."
tags: [rule, parameters, named-arguments, interfaces]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell's last two parameter guidelines concern the match between what a call passes (actual parameters) and what the routine declares (formal parameters) (*Code Complete*, pp. 175-177).

## Rule

- **Use named parameters where the language allows.** Matching actual to formal parameters explicitly makes their use clearer and prevents mismatches. The book says this matters most for long lists of parameters of the same type: mismatches are more likely there, and the compiler cannot catch them. It concedes that explicit matching can be overkill in many settings, and says the extra guarantee does no harm in safety-critical and other high-reliability settings (pp. 175-176).
- **Check that actuals match formals.** Passing a variable of the wrong type is a common slip. Usually the compiler converts input-only arguments and warns when that causes trouble, but a wrong type for an in-out argument can do serious damage. The book asks that argument types always be checked and compiler warnings about parameter type mismatches be read (pp. 176-177).

## Sign in code

- A call with two or more adjacent positional arguments of the same type whose roles differ (`Move(srcId, dstId)`, `Box(w, h, d)`), where the language offers named arguments and the call does not use them.
- A call whose argument names match a different parameter's name at that position (`Distance(y, x)` against `Distance(x, y)`).
- An explicit suppression or cast at a call's argument that silences a parameter type conversion warning.

This wiki assigns the neighbouring cases as follows. This page owns the call site. The order of the declared list is [[parameter-order]], and its length is [[limit-parameter-count]]. Two arguments of the *same* quantity that can be swapped at a call site (two account ids) are [[match-arguments-to-parameters]], while arguments of *different* quantities sharing one primitive are [[replace-primitive-with-class]]. Bare boolean or integer-code arguments are [[enum-instead-of-codes-and-flags]]; same-type arguments of one quantity whose roles differ are [[match-arguments-to-parameters]].

## When not to apply

- **The book's own concession:** in ordinary code, explicit matching for every call is overkill. This wiki reads the rule as applying to the same-type adjacent case, and wherever reliability requirements are raised.
- **Distinct types already guard the call.** This wiki adds a limit. Where each argument has its own type (`Latitude`, `Longitude`) or is a field of a record, a swap fails to compile, and named arguments add nothing to the check.
- **The wrong-type half** is largely what a type checker catches in a strongly typed language, and so is out of this wiki's scope there. The book itself limits that problem to weakly typed languages compiled without the full set of warnings (p. 176).

## Repair

Name the arguments at the call site, or give the parameters distinct types so that a swap cannot compile. If neither is available, this wiki suggests reducing the number of same-type parameters by grouping them into a record ([[limit-parameter-count]]).

## Before and after

```
Transfer(account1, account2, 100)
```

```
Transfer(from: account1, to: account2, amount: 100)
```

## Source

- McConnell, *Code Complete*, 2nd edition, Russian edition, section 7.5, pp. 175-177 ([[code-complete]]). The two guidelines, the same-type reasoning and the overkill concession are the book's.
- The signs, the split with neighbouring pages, the distinct-type limit, the scope note and the pseudocode are this wiki's own.

Related: [[parameter-order]].
