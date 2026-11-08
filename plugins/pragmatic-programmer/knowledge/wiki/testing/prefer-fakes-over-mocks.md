---
title: Prefer fakes shipped with the interface over mocks
category: testing
summary: "A test stubs or verifies calls on a collaborator through a mocking framework (when(x).rate(..).thenReturn, verify(x, times(n))), so it fails when the class under test changes how it uses that collaborator while its visible behaviour stays the same."
tags: [rule, mocking, test-doubles, brittle-tests, interfaces]
paradigm: oop
sources: [elegant-objects]
created: 2026-11-03
updated: 2026-11-03
---

Bugayenko's *Elegant Objects* calls mocking a bad practice that is acceptable only in the most extreme cases, and prescribes fake objects instead: a working, simplified implementation of an interface, written once and shipped as a nested class inside that interface (pp. 99, 103). The book's argument is about [[brittle-tests]]: a mock writes down an assumption about how the object under test uses its dependency, and the test then breaks when that private decision changes.

## Rule

Do not build a test double by scripting the expected calls on a collaborator. Give each interface you write a fake implementation, ship it with the interface (the book nests it: `Exchange.Fake`), and let tests pass that fake to the object under test, asserting only on what that object returns or exposes (pp. 99, 103-104). The book's verdict: «мокинг — плохая практика, применять его можно только в самых крайних случаях» (p. 99).

The reasoning, per the book (pp. 100-103):

- A stub such as "when `rate("USD","EUR")` is called, return 1.15" says: *assume* the class under test calls `rate()` with those arguments. From a unit test's point of view the class is a black box, and it may not call the dependency at all. The test «превращает предположения в факты» (p. 100).
- The purpose of a unit test is to protect refactoring: it must fail when visible behaviour changed and must not fail when it did not (p. 101). The book's example: the collaborator interface gains a one-argument overload, the class under test switches to it, behaviour is unchanged, and the mocked test fails because the scripted two-argument call no longer happens. The fake absorbs the change, since its new method delegates to the old one, and the test is untouched (pp. 101-103).
- Call verification ("was this called, how many times") is worse for the same reason: how an object works with its dependencies is encapsulated, and a test that checks it makes refactoring painful or impossible (p. 103).
- Mock setup grows verbose: with five collaborators of several methods each, a pile of mock calls is unreadable to its own author a couple of months later (p. 100).
- Writing a fake forces the interface's author to think as its user, and the questions that come up (where a fake web page stores its content, thread safety of read and update, encodings) improve the interface itself (p. 104).

The book reports two large fakes in its author's projects: a fake of a ~150-endpoint GitHub API backed by an XML file, and a fake persistence layer over text files nested in each model interface, both making unit tests shorter (pp. 104-105). It also warns: do not fit tests to a fake's behaviour; a fake may be more capable than the real class and may work differently, which is fine as long as tests do not depend too much on its particulars (p. 100).

## Sign in code

- A test creates a double through a mocking library and scripts a return value for a specific call with specific arguments on a collaborator of the class under test (`mock(Exchange)`, `when(...).rate("USD","EUR")`, `doReturn`).
- A test asserts on interactions with a collaborator (called / not called / called N times / called with these arguments) through a mocking library's verification API (`verify`, `times(n)`); asserting on state a fake exposes is not this sign.
- The same collaborator interface is mocked, with near-identical setup lines, in several test files.

This wiki assigns the neighbouring cases as follows. This page owns a test double that scripts or verifies calls on a collaborator. A test that pins incidental output (error text, timestamps, positions) is [[brittle-tests]]. A test that patches a member to substitute a collaborator belongs to the page that owns the patched shape: a static method is [[no-static-methods]], new inside a method is [[new-only-in-secondary-constructors]], a static field or singleton is [[global-data]], and a final or non-overridable method of a collaborator typed by a concrete class is [[public-methods-implement-interfaces]]. A test double that scripts or verifies calls on a collaborator through a mocking library, with no member patched, is [[prefer-fakes-over-mocks]]. A test whose setup reaches global state is [[global-data]].

## When not to apply

- **A large third-party interface used once.** The author's own concession, answering a reader about a 30-plus-method servlet context: if you need a stand-in in many places, write a fake; if only once, use the mocking library (p. 108). The fake for such a «монстрообразный интерфейс» should come from the library's authors (pp. 107-108).
- **When the interaction is the visible behaviour.** This limit is this wiki's own, not the book's: where the unit's only observable effect is a call on a port (sending a message, writing an audit record) and there is no state to read back, asserting on the call is asserting on behaviour. Even then a recording fake that exposes what it received keeps the test off the call's exact shape.
- **The project's convention is mocking.** Readers quoted in the book disagree: one calls home-made test doubles an anti-pattern that becomes a poor, undocumented mocking framework, another says mocking frameworks give controllable stubs for many scenarios (e.g. exception paths) at minimal cost (pp. 105-107). This wiki resolves it per setting: where the team already standardises on a mocking library and has no fakes, the rule applies to interfaces you own and to new code first, as the book itself suggests («Начните со своих интерфейсов», p. 104), not as a reason to rewrite passing tests.
- **Fakes shipped next to production code can be used in production by mistake.** A reader raised this; the author agreed and said he had no answer (p. 107). Where that risk matters, put fakes in a test-scope module, which the author did earlier and found more complicated (p. 107).

## Repair

1. Add a fake implementation of the collaborator interface, simple but functional; nest it in the interface or place it where every user's tests can reach it.
2. Make the fake configurable through its constructor where tests need control (the book: a fake can return an encapsulated rate instead of a constant, p. 100), so the expected value in the test is not a magic number.
3. Replace the mock setup with constructing the fake; delete interaction verifications; assert on what the object under test returns.
4. When the interface changes, change the fake in the same commit, so every test using it keeps compiling and passing.

## Before and after

```
// before: the test scripts how Price must use Rates
rates = mock(Rates)
when(rates.rate("USD", "EUR")).thenReturn(1.5)
price = Price(rates, 200)
assert price.in("EUR").text() == "3.00"
verify(rates, times(1)).rate("USD", "EUR")
```

```
// after: a fake shipped with the interface; only visible behaviour is asserted
interface Rates
  rate(from, to)
  class Fake implements Rates
    Fake(fixed)            // the test states the rate it needs
    rate(from, to) = fixed

price = Price(Rates.Fake(1.5), 200)
assert price.in("EUR").text() == "3.00"
```

If `Rates` later gains `rate(to)` and `Price` starts using it, the fake gets `rate(to) = rate("USD", to)` and the test stays as it is.

McConnell's neutral list of stand-ins, and this wiki's resolution of it against this page, is [[test-scaffolding]].

## Source

- [[elegant-objects]], section 2.8, pp. 97-108: the rule, the false-failure argument with the overload example, call verification, test verbosity, fakes improving the interface, the GitHub and persistence examples, the servlet-context concession, the production-misuse risk the author leaves unanswered, and the readers' objections. The quotations on pp. 99 and 100 were checked against the page images.
- This wiki's own: the third sign, the assignment of neighbouring cases, the limit for interactions that are the behaviour, the per-setting resolution of the readers' disagreement, repair step 1's alternative placement outside the interface, repair steps 3 and 4, and the pseudocode.
