---
title: Test a module against its contract
category: testing
summary: "A guard clause or documented precondition has no test that it rejects, a declared limit of the input domain appears in no test input, every test of a unit feeds valid nominal input only, or a module is exercised only through its dependents."
tags: [rule, testing, contracts, unit-testing]
paradigm: any
sources: [pragmatic-programmer, code-complete]
created: 2026-11-01
updated: 2026-11-06
---

A unit test is most useful when it is read as a check that a module keeps its contract, rather than as a few arbitrary calls. The contract then says which cases to write, and testing dependencies first tells a failure where to look.

## Rule

The book prefers to treat unit testing as testing for conformance to the contract (see [[design-by-contract]]). Such a test shows both whether the code meets the contract and whether the contract means what it was meant to mean, across a wide range of test cases and boundary conditions (p. 271).

Its example is a square root with a precondition on the argument and a postcondition bounding the error. The contract directly yields the test plan: pass a negative argument and see it rejected, pass zero and see it accepted as the boundary, pass values across the range and check the postcondition (pp. 271-272).

For a module that depends on others, the order matters. Test each dependency's contract in full first, then the module that relies on them. If the dependencies pass and the module fails, the fault lies in the module or in its use of a dependency, and no time goes on rechecking the rest (p. 272). The book's motive is to avoid a time bomb that sits unnoticed and goes off late in the project (p. 272).

*Code Complete* names the habit this page counters. Developers lean toward clean tests, which check that code works, over dirty tests, which try to break it: immature organisations write about five clean tests per dirty one, mature ones about five dirty per clean, and the shift comes from writing 25 times more dirty tests, not fewer clean ones (Beizer, in Johnson 1994; p. 495). The attitude underneath: «Успешным считается тест, нарушающий работу ПО» (p. 492), and a programmer who runs code hoping it is correct overlooks errors in plain view (Myers 1978, pp. 492-493). Its classes of bad data supply the rejected inputs: too little or no data, too much, the wrong kind, the wrong size, uninitialized data (p. 506); see [[test-data-classes]] and [[developer-testing]].

## Sign in code

- A guard clause, a raised error or a documented precondition has no test that feeds it an invalid value.
- A limit of the input domain declared in a signature, contract or validation (zero, empty, maximum) appears in no test input.
- A test file contains one or two happy-path examples for a function with a stated postcondition.
- Every test of a unit passes valid, nominal input and asserts success, although the unit's signature admits empty, negative, wrong-kind or absent values.
- A lower-level module with its own contract has no tests of its own and is exercised only through the module above it.

This wiki assigns the neighbouring shapes by where the missing case comes from. This page owns a limit the code declares. A divisor, index or length derived from the arguments belongs to [[test-state-coverage-not-line-coverage]]. A direction, order or sign that every test takes the same way belongs to [[test-boundaries-and-realistic-use]]. A comparison in the routine's own logic, which declares no limit of the input, belongs to [[boundary-value-analysis]].

## When not to apply

- This wiki's reading is that a thin delegating function with no logic has no contract of its own worth a separate test.
- The dependency-first order covers modules the project owns. Retesting a third-party library is not what the book's example describes, and this wiki does not extend it there.
- Validation is owned by one boundary layer and the inner unit is documented to receive only checked data. This wiki's reading is that the rejection tests then belong to the validating layer, not duplicated on every inner unit; see [[barricade]].
- The clean/dirty ratio describes organisations, not a quota per unit. This wiki reads a unit with one invalid input class as needing one rejection test, not five.
- The book's order assumes contracts can be stated. Where nobody can say what a module promises, this wiki reads the missing contract as the problem to solve first, because a test written without one only pins current behaviour.

## Repair

1. Write the module's preconditions and postconditions down.
2. Add one test per rejected input class (the bad-data classes of p. 506 in *Code Complete*), asserting the specific failure rather than "does not crash", one per boundary, and a set across the valid range that checks the postcondition rather than one remembered value.
3. Give each lower-level module its own contract tests, so that a failure above can be located.

## Before and after

Before: one example, with the contract untested.

```
test withdraw:
    assert withdraw(balance = 100, amount = 30) == 70
```

After: each case comes from the contract `0 < amount <= balance`, result `balance - amount`.

```
test rejects_non_positive:
    assert raises withdraw(100, 0)

test rejects_above_balance:
    assert raises withdraw(100, 101)

test accepts_full_balance:
    assert withdraw(100, 100) == 0

test keeps_postcondition_across_range:
    for amount in [1, 37, 99]:
        assert withdraw(100, amount) == 100 - amount
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020 ([[pragmatic-programmer]]): pp. 271-273. This wiki's own: the signs and their assignment against the neighbouring pages, the limits, the repair and the pseudocode. McConnell, *Code Complete*, 2nd ed., Russian edition ([[code-complete]]): p. 492 (a successful test breaks the software), pp. 492-493 (the Myers study), p. 495 (the clean/dirty ratio and the Beizer data), p. 506 (the bad-data classes). This wiki's own: the nominal-input-only sign, the barricade and ratio limits, and the use of the bad-data classes in the repair.

Related: [[property-based-testing]], [[test-is-first-client]], [[test-boundaries-and-realistic-use]], [[test-state-coverage-not-line-coverage]].
