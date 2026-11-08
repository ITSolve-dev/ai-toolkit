---
title: "Use an enumerated type instead of integer codes and boolean flags"
category: types-and-state
summary: "Integer codes for a closed set of values (kind == 3, 1 = red, 2 = green), a call with several bare true/false arguments, a boolean return value that already needs a third outcome, or two closed sets held in one integer type and mixable."
tags: [rule, enums, booleans, flag-arguments, type-safety]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-07
---

An enumerated type lists, in words, every value a variable may take. *Code Complete* recommends it whenever all values are known, as a replacement for schemes such as "1 is red, 2 is green, 3 is blue" (Russian edition, pp. 294-295), and gives four reasons: readability, reliability, modifiability, and room beyond true and false (pp. 295-296).

## Rule

- **Readability.** `if chosenColor = Color_Red` instead of `if chosenColor = 1`. «Каждый раз, когда вы видите числовую константу, подумайте: не заменить ли ее перечислимым типом.» (p. 295). The book's strongest case is a parameter list: `RetrievePayrollData(data, true, false, false, true)` tells the reader nothing, while the same call with `EmploymentStatus_CurrentEmployee`, `PayrollType_Salaried` and so on reads on its own (p. 295).
- **Reliability.** With named integer constants the compiler cannot know that a colour variable takes only colours, and accepts `color = Country_England`. A distinct enumerated type lets it reject that (p. 295). The book notes this depends on the language.
- **Modifiability.** A gap in a numeric scheme forces a search for every 1, 2, 3; an enumeration grows by adding a member (pp. 295-296).
- **An alternative to booleans.** A routine that returns true on success may later turn out to have two kinds of failure: one local, one fatal and to be propagated. `Status_Success`, `Status_Warning`, `Status_FatalError` fits better than true and false and extends easily (p. 296).

Where a language lacks enumerations, the book emulates them with a class that has a private constructor and one static instance per value, which also gives type safety (pp. 298-299).

## Sign in code

- An integer variable or field compared against literals or plain integer constants that form a closed set (`status == 3`, `kind == KIND_FILE` where `KIND_FILE = 2`).
- A call with two or more bare boolean arguments, or a boolean argument whose meaning cannot be read at the call site.
- A boolean return value accompanied by an out-parameter, a global error flag or a second call to find out which kind of false it was.
- Values of two different closed sets held in the same integer type, so that one can be assigned to the other without complaint.

This wiki assigns neighbouring cases as follows. This page owns replacing codes and flags with a named closed set, at call sites, in return values and in comparisons. A control flag passed as a bare literal at the call site is [[semantic-coupling]], which owns the call site. Where an integer or boolean code selects which of several unrelated jobs a routine body does, [[routine-cohesion]] owns the body and the repair is one routine per job; where the code names a value the routine handles in one way, [[enum-instead-of-codes-and-flags]] owns it. An argument the callee branches on is [[no-public-constants]] when it is a public enum or constant shared across classes, whatever the call site writes; otherwise, written as a literal at the call site it is [[semantic-coupling]], and flowing in as data its type is [[enum-instead-of-codes-and-flags]]. An argument the callee stores, filters on or passes on is [[enum-instead-of-codes-and-flags]]. Same-type arguments of one quantity whose roles differ are [[match-arguments-to-parameters]]. A status held in a boolean field and read by several functions outside the code that sets it is [[status-variable-as-enumeration]], which adds the accessor. A status variable whose name contains `flag` is [[status-variable-not-flag]] for its name. Where each user of a public enum wraps it in its own code, [[no-public-constants]] owns the shape and its repair is a class per behaviour. A chain of branches over the enum, all of one shape, is [[drive-repeated-dispatch-from-a-table]]. A multi-way branch over the enum with no default arm is [[default-branch-catches-the-unexpected]]. A single bare literal that is not part of a closed set is [[named-constants-over-literals]]. Different open quantities mixable because they share a primitive are [[replace-primitive-with-class]]. A closed set held as strings is [[replace-primitive-with-class]] where call sites validate it or compare its values by order or by membership in a subset (`== "high" or == "rush"`), and [[enum-instead-of-codes-and-flags]] where they only test equality with single alternatives. Ordering, sentinel and gap problems inside an enum are [[enum-sentinels-and-gaps]]. A raw input string compared far from where it was read is [[convert-input-at-entry]]. An integer assigned and tested only as 0 and 1, standing for true and false, is [[test-a-value-by-its-kind]]; an integer compared against a closed set of codes with three or more members is [[enum-instead-of-codes-and-flags]].

## When not to apply

The book's one limit is that the reliability gain depends on the language (p. 295). The limits below are this wiki's own:

- **One boolean whose meaning is plain at the call site**, such as `setVisible(true)`, gains little from an enum.
- **An open set**, where new values come from data or configuration at run time, is not an enumeration; a closed type would have to be recompiled for each new value.
- **Codes fixed by an outside format** (protocol status codes, database values) still need their numbers; an enum then maps names to those numbers at the boundary rather than replacing them.
- **The book and *Elegant Objects* disagree on enums.** *Code Complete* recommends them; [[no-public-constants]] treats them as public constants. This wiki resolves it per setting: an enum that names a closed set of values and is read, stored or compared is this page's repair; a public enum passed in to select behaviour that callers would otherwise need to know about is [[no-public-constants]]'s sign, and its repair is a class per behaviour. An argument the callee branches on is [[no-public-constants]] when it is a public enum or constant shared across classes, whatever the call site writes; otherwise, written as a literal at the call site it is [[semantic-coupling]], and flowing in as data its type is [[enum-instead-of-codes-and-flags]]. An argument the callee stores, filters on or passes on is [[enum-instead-of-codes-and-flags]]. A project convention on enums overrides both.

## Repair

1. Collect the values of the closed set and give each a name in the problem's terms.
2. Declare a distinct type for them, so values of different sets cannot be mixed.
3. Replace literal codes and constants with the members; replace each bare boolean argument with a member of a two-valued type named for what it chooses.
4. Where a boolean result has grown a third meaning, change the return type to an enumeration of the outcomes, and update callers to handle each.

## Before and after

```
result = retrieve_payroll(data, true, false, false, true)

function save(record) returns boolean
  ...
  if disk_full
    last_error = FATAL
    return false
```

```
result = retrieve_payroll(data,
  Employment.CURRENT, Payroll.SALARIED,
  Savings.NO_DEDUCTION, Medical.INCLUDE_DEPENDENTS)

enum SaveStatus { SUCCESS, WARNING, FATAL_ERROR }
function save(record) returns SaveStatus
  ...
  if disk_full
    return FATAL_ERROR
```

Here the payroll members are filter values the routine passes to its query, not selectors of different code, so [[no-public-constants]] does not fire.

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, chapter 12: definition and examples, pp. 294-295; readability, the payroll call and reliability, p. 295; modifiability, pp. 295-296; enums instead of booleans, p. 296; emulation by a class, pp. 298-299. The quotation of p. 295 is transcribed from `raw/` and needs the page-image check. This wiki's own: the signs, the listed limits (the language dependence is the book's, p. 295), the resolution against [[no-public-constants]] and the note under the pair, the splits with neighbouring pages, and the pseudocode.
