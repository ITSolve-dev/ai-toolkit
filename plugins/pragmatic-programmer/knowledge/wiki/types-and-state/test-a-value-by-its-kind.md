---
title: Test a value by its kind
category: types-and-state
summary: "A boolean held as an integer 0/1 or compared to true/false (flag = 1, done == false), or a number or reference used bare as a condition (while balance, if ptr): use a boolean or an enum, test booleans directly, compare numbers and references explicitly."
tags: [rule, boolean, flags, magic-numbers, conditions]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

A condition should show what kind of value it tests. McConnell makes three moves on this: use `true` and `false`, not `0` and `1`, for logical values; compare booleans implicitly; compare numbers, characters and pointers explicitly (*Code Complete*, section 19.1, pp. 425-426 and 434-435). This wiki reads a common thread in the three: `0` and `1` stand for too many things.

## Rule

- Hold a logical value in a boolean, not an integer used as a flag. Of integer flags tested against 0 and 1 the book says «Ничего в этом фрагменте не говорит о том, представляет ли 1 «истину», а 0 — «ложь» или же все наоборот» (p. 425), and that 0 is easily typed for 1 (p. 425).
- Rewriting with booleans exposed that one of the flags was not logical at all: `reportSelected = 1` tested whether the first report was chosen, and became an enumerated type, `reportSelected = ReportType_First` (pp. 425-426).
- Compare booleans implicitly: `while ( not done )`, not `while ( done = false )`; `while ( a > b )`, not `while ( (a > b) = true )`. This cuts what the reader must keep in mind and reads closer to spoken English (p. 426).
- Compare non-logical values explicitly, because 0 is a number, a string terminator, a null pointer, the first element of an enumeration and false (p. 434): `while ( balance != 0 )`, not `while ( balance )` (p. 434); a character against the terminator explicitly; a pointer against `NULL` (p. 435). McConnell admits the last two run against established C convention and holds that the readability gain justifies it (p. 435).

## Sign in code

- A variable of integer type assigned only 0 and 1 and tested with `= 0` / `= 1` or `== 1`.
- A boolean compared to a literal `true` or `false`.
- A number, character or reference used bare as a condition, where the language allows it (`while balance`, `if ptr`, `if count`).

This wiki assigns the neighbouring cases as follows. An integer assigned and tested only as 0 and 1, standing for true and false, is [[test-a-value-by-its-kind]]; an integer compared against a closed set of codes with three or more members is [[enum-instead-of-codes-and-flags]]. An integer "flag" compared to 1 whose other values would select among options (a selection, a mode) is an enumeration in disguise, owned by [[enum-instead-of-codes-and-flags]]. A boolean compared to a literal `true` or `false` is [[test-a-value-by-its-kind]]; a negated condition or a double negative is [[prefer-positive-conditions]]; a boolean's name is [[boolean-variable-names]].

## When not to apply

The book gives one limit: where a language has no boolean type and booleans are emulated, implicit comparison may not work, since emulated true and false cannot always be tested in forms like `while ( not done )` (p. 426). Further limits are this wiki's own:

- Truthiness of references, collections, optional values and numbers is a language idiom, and the charter leaves idioms to the project's conventions and tooling. Where the project's idiom is `if items:`, `if count:` or `if (ptr)`, follow it; this page then fires only on integer-encoded booleans and on booleans compared to literals.
- Comparison to a literal `true` is right where the value can be something other than a boolean (a nullable boolean, a dynamically typed value); `== true` then states that only `true` passes.
- Most linters already flag `== true`; a review that finds only that has found style, not this rule.

## Repair

1. For an integer flag with only two meanings, change its type to boolean and name it for the true case.
2. For an integer "flag" whose values select among options, introduce an enumeration and compare against its named members, as [[enum-instead-of-codes-and-flags]] describes.
3. Replace `x == true` with `x` and `x == false` with `not x`, where `x` is a plain boolean.
4. Where project convention allows, write numeric and reference tests as explicit comparisons (`count != 0`, `ref != null`).

## Before and after

Before: nothing says which of these are logical, or which value means yes.

```
printerError = 0
reportSelected = 1
if printerError == 0: initPrinter()
if printerError == 1: notifyUser()
if reportSelected == 1: printReport()
while balance: pay()
```

After: a boolean, an enumeration and an explicit numeric test.

```
printerError = false
reportSelected = Report.FIRST
if not printerError: initPrinter()
if printerError: notifyUser()
if reportSelected == Report.FIRST: printReport()
while balance != 0: pay()
```

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, section 19.1, pp. 425-426 and 434-435. The three moves, the ambiguity of 0 and 1, the `reportSelected` flag that turned out to be an enumeration, the many meanings of 0, the conflict with C convention and the limit for emulated booleans are the book's. The book's C-specific advice on the terminator and `NULL` is reduced here to its general point. The signs, the common thread read into the three moves, the assignment of neighbouring cases, the limits other than emulated booleans, and the pseudocode are this wiki's own. Related: [[name-by-role]], [[self-describing-field-names]], [[prefer-positive-conditions]].
