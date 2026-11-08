---
title: Property-based testing
category: testing
summary: "A function whose tests are only hand-picked examples while it has a statable contract, invariant or inverse (round trip, length kept, sorted output): state it as a property over generated inputs and pin each falsifying input as a unit test."
tags: [method, testing, properties, invariants, test-design, oracle]
paradigm: any
sources: [pragmatic-programmer, code-complete]
created: 2026-11-01
updated: 2026-11-06
---

Property-based testing states what must hold for all inputs and lets a generator choose the inputs. It answers a specific weakness of hand-written tests: the same head wrote the code and the test.

## The problem it addresses

Code and its tests can express the same wrong assumption, and the code then passes because it does what its author understood (p. 276). Having different people write each would resolve that, but the book rejects this because thinking about tests gives feedback on the code, and splitting the work loses it (p. 276; see [[test-is-first-client]]). It prefers to have a computer do the testing, since a computer brings no preconceptions.

## What a property is

Contracts are the conditions code requires of its inputs and the guarantees it gives about its outputs. Invariants are things about some part of state that stay true as it passes through a function: sorting leaves a list's length unchanged. The book calls both together properties (p. 276; see [[design-by-contract]]). Its tip: «Пользуйтесь тестами на основе свойств для проверки правильности ваших предположений» (p. 276).

## Procedure

1. State a property of the function under test: a contract clause, or something that must not change.
2. Describe the inputs through the tool's generator language, which most languages have a library for (pp. 277-278).
3. Assert the property inside a test that the framework runs many times with different data. In the book's sort example, two tests run a hundred times each, which it likens to 200 separate tests (p. 277).
4. When a test fails, read which arguments the framework passed.
5. Copy those arguments into an ordinary unit test. The book gives two reasons (p. 282): it focuses on the failure without further calls through the framework, and it acts as a regression test, since generated values are not guaranteed to recur on the next run.

## Worked example

The book's warehouse has a stock check and a removal operation, an order function built on both, and passing example tests (pp. 278-280). The added property is that nothing appears or vanishes in a transaction: units taken plus units left equal the original level. The run fails with a request for three of an item of which two are held: the stock check asks only whether at least one unit exists, not whether the requested quantity does (pp. 280-281). The repair gives the check the quantity. The failure had nothing to do with the arithmetic the property was written to check, and the book calls that both the strength and the weakness: «В этом состоит сила и слабость тестирования на основе свойств.» (p. 281). Inputs and assertions are set up and the tool then runs freely, so the outcome cannot be known in advance, while «выяснение причины сбоя может оказаться нелегким делом» (p. 282).

A minimal shape, in this wiki's pseudocode:

```
for any list of integers xs:
    ys = deduplicate(xs)
    assert set(ys) == set(xs)
    assert ys has no repeated element

// generated failure: xs = [1, 1, 2, 2], pinned as:
test deduplicate_removes_every_repeat:
    assert deduplicate([1, 1, 2, 2]) has no repeated element
```

## Choosing what to assert

The book's answers to exercises 31 and 32 show how to find properties and how they share the work with example tests.

1. **Divide the work.** Point example-based unit tests at individual cases whose result was obtained by other means, and let property tests carry the general questions. The book calls packing boxes in a truck «удобный случай для тестирования на основе свойств» (p. 362).
2. **Ask what no result may ever do.** The book's list for packing asks whether any two boxes overlap, and whether any part of a box sticks out past the truck's width or height (p. 362).
3. **Bound a derived figure.** Packing density, the area taken by boxes divided by the truck's area, must be at most 1 (p. 362).
4. **Add requirements only as requirements.** A minimum density belongs in the test only if it is part of the requirement (p. 362).
5. **Condition a property on its input.** For an order, the book generates arbitrary quantities and checks that an OK tuple comes back whenever stock suffices (p. 362).

## A random generator with a round-trip oracle (McConnell)

McConnell's account of testing his own file encryption program (*Code Complete*, pp. 515-516) is the same method without a library, and it shows the parts a property test stands on.

1. **An oracle that needs no hand calculation.** Decrypting an encrypted file must give the original back. His generator made two copies of a random file, encrypted one, reinitialised, decrypted it, and compared the result with the copy (p. 515).
2. **Every dimension of the input randomised.** Random content, a random size from 0 to 500 KB, random passwords 1 to 255 characters long (p. 515).
3. **A biased distribution.** He set the mean file size to 30 KB instead of the uniform 250 KB, so runs were faster and more of them hit passwords, end-of-file markers and unusual sizes (p. 515). He adds that over time the distribution can be shifted toward the realistic input range to harden the parts used most (p. 516).
4. **Everything needed to reproduce a failure printed with it** (p. 515).
5. **The driver reused after a fix**, so retesting began at once (p. 516).

The result: two defects after only about 100 tests, both in situations that might never arise in practice; then about 100 000 files over several weeks with no errors (pp. 515-516). His lessons: well-designed random generators produce combinations a person would not think of and test more thoroughly than a person does, and modular design paid for itself because the crypto code could be driven apart from the UI (p. 516; see [[test-scaffolding]]).

This wiki reads step 1 as what the method rests on: without an oracle independent of the code under test, random inputs only show that the program does not crash. Where no inverse or reference exists, a weaker property such as "output sorted", "length preserved" or "invariant held" is the oracle. This wiki also reads step 4 as the book's form of step 5 of the procedure above: a failing input or seed that is not recorded turns a found defect into a lost one.

```
test encrypt_roundtrip_random:
    repeat 1000 times:
        seed = new_seed()
        data = random_bytes(size = skewed_size(mean = 30KB, max = 500KB), seed)
        pw   = random_string(length = 1..255, seed)
        if decrypt(encrypt(data, pw), pw) != data:
            fail("seed", seed, "size", len(data), "pw length", len(pw))
```

## Design effect

Just as a unit test makes the author see the API as its first client, a property makes the author see the code in terms of invariants and contracts: what must not change and what must stay true. The book says this removes edge cases and exposes functions that leave data inconsistent (p. 282).

## Limits and trade-offs

- It complements unit testing rather than replacing it. The two solve different tasks (p. 282).
- Diagnosis costs more, for the reason given above.
- A property comes from an author too. This wiki's reading is that a wrong property shares the blind spot the method exists to escape, although a property states the assumption more explicitly than an example does.
- This wiki's reading is that a property which merely restates the implementation proves nothing, and that randomised runs in a shared build can fail on unrelated changes unless the tool's seed can be fixed. The book's packing properties avoid the first trap, in this wiki's reading, since each one checks the output without needing to know the best packing.
- This wiki adds that a conditional property covers one branch. Step 5 under *Choosing what to assert* says nothing about a refused order, so the opposite condition needs a property of its own.
- This wiki adds that if the guard is rarely true, most generated inputs test nothing. Generate inputs that meet it instead of filtering for them.
- This wiki adds that properties alone are weak on correctness. An output that passes every packing property can still be a poor packing, which is why step 1 keeps example tests.

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020 ([[pragmatic-programmer]]): pp. 276-282, and p. 362 for the answers to exercises 31 and 32. This wiki's own: every limit marked as such, the arrangement of the two answers as steps, and the pseudocode. The book's example uses Hypothesis and pytest; tool syntax is not recorded here. McConnell, *Code Complete*, 2nd ed., Russian edition ([[code-complete]]): pp. 515-516 for the random generator with a round-trip oracle; the oracle reading, the link between his printed failure data and pinning a falsifying input, and the second pseudocode block are this wiki's own. Related: [[test-the-contract]], [[find-bugs-once]], [[test-state-coverage-not-line-coverage]].
