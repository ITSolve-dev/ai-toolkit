---
title: Choose test values whose expected result can be checked by hand
category: testing
summary: "Test inputs like 90783.82 or 1239078382346 next to an expected value nobody can compute in their head, with no derivation shown; pick round values from the same equivalence class."
tags: [rule, test-design, test-data, equivalence-classes]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

A test is only as good as the reader's ability to tell whether its result is right. McConnell's payroll example: a programmer types a random-looking salary, trims it to something realistic like 90 783,82, and the test fails. Now the expected value has to be computed by hand, and with numbers like that the chance of a mistake in the hand calculation is as high as the chance of the defect in the program (p. 507). Round numbers such as 20 000 make the calculation trivial.

The reasoning that keeps this from costing coverage: an awkward number is not a better probe. Every value from the same equivalence class finds the error with the same probability: «при использовании любого числа из одного и того же класса эквивалентности вероятность нахождения ошибки одинакова» (p. 507). See [[equivalence-partitioning]] and [[boundary-value-analysis]].

## Rule

Within an equivalence class, choose the input whose correct output can be verified mentally: round numbers, zeros, small multiples. The chapter checklist asks it directly: do the tests make it easy to check results by hand (p. 523)?

## Sign in code

- A test's input literal has many significant digits (`90783.82`, `1239078382346`) and the expected literal beside it is a number of similar shape with no derivation shown.
- An expected literal of many significant digits with no derivation shown, even beside round inputs. This sign is this wiki's own.

This wiki assigns the neighbouring case as follows. An expected value computed in the test by logic that repeats the code under test is [[test-code-is-defect-prone]]; an expected literal whose derivation cannot be checked mentally is [[test-values-checkable-by-hand]].

## When not to apply

- When the value itself places the input in its class: a test of rounding, overflow or precision needs the awkward digits. This wiki reads the round-value rule as applying only among values of one class.
- When the expected output comes from an independent oracle, such as a round trip, a reference implementation or a property, not from a hand calculation; see [[property-based-testing]]. This limit is this wiki's own.

## Repair

Replace the value with a round one from the same class, and write the expected result so its derivation is visible (`800 + 210`). Keep a separate, named test for any boundary or precision case that genuinely needs odd digits.

## Before and after

```
test pay_for_overtime:
    emp = employee(hourly_rate = 43.646)
    assert pay(emp, hours = 47) == 2204.12
```

```
test pay_for_overtime:
    emp = employee(hourly_rate = 20)
    // 40 h * 20 + 7 h * 20 * 1.5
    assert pay(emp, hours = 47) == 800 + 210
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]]: p. 507 (the payroll example and the equivalence-class argument) and p. 523 (the checklist item). This wiki's own: the second sign, the assignment against [[test-code-is-defect-prone]], both limits and the pseudocode.
