---
title: Design by contract
category: errors
summary: "A routine's rights and duties stated as preconditions, postconditions and invariants; relevant when a body assumes what no signature, comment, test or check states, or when a mutator's conditions still let a class invariant break."
tags: [concept, contracts, correctness, invariant, precondition, postcondition]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

Design by contract (DBC) treats a call as an agreement: if the caller meets every precondition, the routine guarantees every postcondition and invariant when it finishes (p. 142). Thomas and Hunt take the idea from Bertrand Meyer's work on Eiffel and define a correct program as one that does what is required of it, «ни больше и ни меньше» (p. 141). The book's tip is «Проектируйте по контракту» (p. 143).

## The three terms

- **Precondition:** what must be true for the routine to be called. The caller is responsible for supplying good data. «Подпрограмма вообще не должна вызываться, если ее предусловия будут нарушены.» (p. 141). See [[caller-owns-the-precondition]].
- **Postcondition:** the state of the world when the routine finishes, which is what it guarantees. Having one implies that the routine terminates, so infinite loops are excluded (p. 141).
- **Invariant:** a condition the class guarantees to callers. It may lapse during internal processing and must hold again on return (p. 141). See [[class-invariant]]. The book widens the term beyond classes: in functional code, state is passed in and handed back updated, and invariants are just as useful there (p. 144). A requirement fixed for a whole system is a [[semantic-invariant]].

## What a breach means

A breach is a bug: «несоблюдение условий контракта считается программной ошибкой» (p. 142). The remedy is agreed in advance, typically an exception or termination (p. 142). This is why preconditions must not carry validation of user input; [[assertion-or-error-handling]] gives the test.

Contracts fit [[crash-early]]: checking conditions at the contract stops the program sooner and reports the problem more precisely. The book contrasts a square root that rejects a negative argument at once with one that returns NaN, which later arithmetic turns into baffling results (p. 146).

## Against tests and defensive code

The authors do not offer contracts as a replacement for testing. They call the two different approaches to correctness, each useful in its own situations, and list what contracts add (p. 144):

- They need no setup or mocking.
- They define success and failure for all cases, while a test targets one case at a time.
- Tests run only in the test stage of the build; contracts and assertions apply throughout design, development, deployment and maintenance.
- Test-driven work leans towards black-box checks of a public interface rather than internal invariants.
- They are more efficient and closer to DRY than defensive programming, where everyone validates data in case nobody else did.

This wiki reads the comparison as a division of labour: a contract states a routine's domain, and a test pins chosen examples inside it.

## How far a language takes it

This wiki arranges the book's remarks on enforcement as a ladder:

1. List the input domain, the boundary conditions, what the routine promises and what it does not, before writing the code. See [[state-the-contract]].
2. Put the contract in comments or unit tests. Even with no automatic checking this yields real benefit (p. 145).
3. Emulate it with assertions, which only partly succeeds (pp. 145-146): assertions may not propagate down an inheritance hierarchy, so an override must duplicate them by hand; invariants must be called by hand before each exit; such checks can be switched off globally; there is no built-in notion of old values, so a precondition must save what a postcondition needs; and ordinary runtimes and libraries are not contract-checked, although the boundary with a library is where most trouble shows up.

The breadth of a contract has its own cost: see [[strict-accept-narrow-promise]].

## Stating a class's contract so that it closes

The book's answer to exercise 14 writes the contract of a kitchen blender, in Java signatures with the conditions in comments (pp. 354-355). It shows what each kind of condition is for:

- An invariant can bound one value, or tie two together: speed lies in a fixed range, and speed above zero implies the container is full (p. 355).
- A precondition can depend on current state as well as on the argument: a new speed must differ from the current one by at most one (p. 355).
- A postcondition pins the visible effect: after setting the speed, the getter returns that value. A paired operation mirrors it: filling requires not full and ensures full, and emptying the reverse (p. 355).

This wiki adds a requirement the answer does not state: a contract must close, meaning that every mutator's precondition and postcondition together preserve every invariant. The published answer does not close. Nothing there stops the speed being raised from zero on an empty object, and nothing stops emptying while running, and either one breaks the implication between speed and fullness.

[[class-invariant]] asks whether code outside the class can break an invariant. This wiki's closing check asks whether the class's own mutators can.

### Sign in code

- A field with a restricted range, or valid only in combination with another field, and a mutator that assigns to it with no check and no stated precondition.
- A pair of operations that must alternate, such as open and close, with nothing rejecting a repeated call.
- An invariant written down, and a mutator that can change one of its fields without a precondition mentioning the other. Read each mutator against each invariant.

### When not to apply

The book states no limit here. The limits below are this wiki's own.

- A plain data holder with no constraint among its fields has no invariant worth stating.
- A precondition is the caller's duty, so it does not replace validation of data arriving from outside the program.
- A contract kept only in comments is not checked by anything, and it can go stale without any failure. Where the language has no contract support, enforce the conditions with assertions at method entry and exit, or treat the comments as documentation only.

### Repair

1. List the fields and write what must always hold among them.
2. For each mutator, write what must hold before the call, including conditions on other fields.
3. Write what the call guarantees afterwards.
4. Walk each mutator against each invariant. If an invariant can be broken, add the missing precondition.
5. Turn the conditions into checks where the language allows it. See [[assert-the-impossible]].

### Before and after

Before: nothing states that a running pump must be primed.

```
class Pump
  rate = 0
  primed = false
  prime():     primed = true
  setRate(x):  rate = x
  drain():     primed = false
```

After: the contract closes, because `setRate` and `drain` are barred from breaking the second invariant, and `prime` cannot break it.

```
class Pump
  invariant 0 <= rate < 10
  invariant rate > 0 implies primed

  prime()
    pre  not primed
    post primed

  setRate(x)
    pre  0 <= x < 10
    pre  x == 0 or primed
    post rate == x

  drain()
    pre  primed
    pre  rate == 0
    post not primed
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, [[pragmatic-programmer]]: pp. 140-148, and pp. 354-355 for the answer to exercise 14. The division of labour between a contract and a test and the arrangement as a ladder are this wiki's own. In the closing section, the three condition kinds and their uses are the book's; the closing requirement, the observation about the published answer, the signs, the limits, the repair and the pseudocode are this wiki's own. Extraction scrambled the order of the comments in the book's listing for exercise 14, so its text was read for meaning and is not quoted.
