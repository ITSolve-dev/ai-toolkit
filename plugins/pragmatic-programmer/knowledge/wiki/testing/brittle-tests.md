---
title: Brittle tests
category: testing
summary: "An assertion compares exact error text, a log timestamp, an absolute screen position or a private field read by reflection, so the test fails after a change that kept every return value and visible effect the same."
tags: [rule, testing, brittleness, refactoring, false-failure]
paradigm: any
sources: [pragmatic-programmer, elegant-objects]
created: 2026-11-01
updated: 2026-11-06
---

A test becomes brittle when it pins something incidental rather than the behaviour it exists to protect. It then fails on harmless changes, and *Elegant Objects* says such false alarms undermine faith in one's own unit tests (p. 102).

*Elegant Objects* gives the definition this page tests against. A unit test is a safety net for refactoring with two halves: it must fail when the class's behaviour changed (a true alarm), and it must not fail when the visible behaviour did not change (a false alarm). The book calls the second half extremely important: «тест не должен давать отрицательный результат, если видимое поведение класса не изменилось» (p. 101; checked against the page image). Per that book, false alarms are maddening, undermine faith in one's own tests and are a key reason many programmers dislike unit tests; when refactoring comes, tests coupled to implementation details that no longer exist have to be deleted (pp. 102-103). The test may care only how the object interacts with *us*, not how it interacts with other classes (p. 103).

## Rule

«Уделяйте тестовому коду такое же внимание, как и любому рабочему коду.» (p. 274). Keep it decoupled, clean and reliable. *The Pragmatic Programmer* names what not to lean on: the absolute position of widgets in a GUI, the precision of timestamps in a server log, and the exact wording of error messages. Testing such things makes tests brittle (p. 274). The book's cross-reference here is to [[programming-by-coincidence]], and this wiki reads the link this way: such a test relies on something that happens to be true.

*Elegant Objects* adds the same care in its own terms: a well-made unit test documents the class better than prose, and tests deserve the same attention as the main code (p. 96; see [[tests-instead-of-documentation]]). This wiki reads the two books as one rule: a test pins only what a user of the code can observe.

A procedure to apply, which is this wiki's own and derived from the *Elegant Objects* definition: imagine a refactoring that keeps every return value and visible effect but changes the wording of internal text, the representation of fields, or how the object uses its dependencies. If the test would fail, it is brittle.

## Sign in code

- An assertion compares the full text of an error or exception message.
- An assertion compares a timestamp or a formatted log line for equality.
- A UI test locates an element by pixel coordinates or by its position among siblings.
- An assertion reads a private field through reflection or a test-only accessor, rather than a value the object returns.

This wiki assigns the neighbouring cases as follows. This page owns an assertion on incidental output or internal state. A test double that scripts or verifies calls on a collaborator is [[prefer-fakes-over-mocks]], the source *Elegant Objects* names as the main cause of false alarms (p. 102). A client-facing contract or docstring stated in terms of a class's control state is [[contract-of-state-dependent-method]].

## When not to apply

- This wiki's reading is that an exact text is fair to pin when the text is the contract: a message format that other programs parse, or wording under a regulatory or product requirement.
- This wiki's reading is that a time value is fair to compare exactly when the test injected the clock, because it is then an input and not an accident. See [[test-is-first-client]].
- This wiki's reading is that a field is fair to assert on when the object exposes it as part of its contract; then it is a returned value, not internal state.

## Repair

Assert on the stable thing beneath the incidental one: an error's type or code rather than its text, the ordering of events rather than their timestamps, an element's role or stable identifier rather than its coordinates, a returned value rather than a private field.

## Before and after

Before: rewording the message breaks the test.

```
test rejects_expired_card:
    error = capture_error(pay(expired_card))
    assert error.message == "Card expired on 01/24, please update it"
```

After: the test pins the behaviour.

```
test rejects_expired_card:
    error = capture_error(pay(expired_card))
    assert error.code == CARD_EXPIRED
```

## Source

- *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020 ([[pragmatic-programmer]]): p. 274.
- Bugayenko, *Elegant Objects*, Russian translation, Piter, 2018 ([[elegant-objects]]): section 2.8, pp. 101-103 (the two halves of a unit test's job, the consequences of false alarms, coupling to how an object uses its dependencies); end of section 2.7, p. 96 (tests as documentation and deserving care).
- This wiki's own: the reading of the cross-reference, the reading of the two books as one rule, the imagined-refactoring procedure, the signs (the reflection sign included), the assignment of neighbouring cases, the limits, the repair and the pseudocode.
