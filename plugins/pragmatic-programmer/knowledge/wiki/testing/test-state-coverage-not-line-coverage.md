---
title: Test state coverage, not line coverage
category: testing
summary: "A function has a divisor, index or length derived from its arguments, its tests reach every line, yet no test input makes that value zero, empty or out of range."
tags: [rule, testing, coverage, test-design, boundaries]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

Line coverage records which lines ran, while correctness depends on which program states were reached. A function can be fully covered and still fail in a state no test ever visited.

## Rule

The book's prescription: «Проверяйте покрытие тестами состояний, а не исходного кода» (p. 336). Thomas and Hunt accept coverage tools as a general gauge of how broad testing is, and they say not to expect full coverage from them (p. 335).

The reasoning: «Ведь реально важно число состояний, в котором может находиться программа, но состояния не равнозначны строкам кода.» (p. 335). Their example is a three-line function taking two integers from 0 to 999 and dividing by their sum. It has a million logical states, of which 999,999 are correct and one fails, when the sum is zero (pp. 335-336). Knowing the line ran says nothing about that state. They add that covering all states is in general out of reach (p. 336), and that the short answer to how you know you have tested enough is that you do not (p. 335).

The same section observes that many developers test softly, unconsciously steering around the places they know are weak (p. 332). This wiki reads soft testing as the mechanism behind the gap: the author picks inputs the code was already written to handle.

## Sign in code

- A function divides by, indexes with, or takes a length from a value derived from its arguments, and no test passes arguments that make that value zero, negative or out of range.

The sign is a relation between a distinguished value in the code and the inputs in the tests, so it can be checked by reading both.

This wiki assigns the neighbouring shapes by where the missing case comes from. This page owns a value derived from the arguments, which no signature declares. A limit the code declares belongs to [[test-the-contract]]. A direction, order or sign that every test takes the same way belongs to [[test-boundaries-and-realistic-use]]. A comparison in the routine's own logic, which declares no limit of the input, belongs to [[boundary-value-analysis]].

## When not to apply

- Code with no distinguished values: pure delegation or field mapping, where every input takes the same path and no operation has a partial domain. One example is enough there.
- Line coverage is not worthless. A line that never ran is a definite gap, and the book keeps the tool as a gauge (p. 335). The rule is against treating the figure as proof, not against measuring it.
- The rule does not ask for every state. The book itself says that is out of reach (p. 336). Demanding every combination of inputs misreads it. This wiki aims the effort at states where behaviour changes.

## Repair

1. List the operations in the function with a partial domain, such as division, indexing and parsing, and the limits of each parameter.
2. Add one test for each state that changes behaviour: zero, empty, the minimum, the maximum, just past a limit.
3. Where the state space is too large to list, state the contract or invariant and let the machine generate inputs, which is the book's recommendation (p. 336). See [[property-based-testing]]. This wiki prefers listed boundary examples where no invariant can be stated.
4. If the function has no defined answer in a state, the gap is in the contract. Decide the behaviour first, then test it. See [[design-by-contract]].

## Before and after

Before. Every line runs, and the state that fails is never visited:

```
function average_price(total, count):
    return total / count

test "average price":
    assert average_price(100, 4) == 25

# line coverage of average_price: 100%
```

After:

```
function average_price(total, count):
    require count > 0
    return total / count

test "average price":
    assert average_price(100, 4) == 25

test "average price rejects an empty order":
    assert_fails average_price(100, 0)

property "average lies between zero and the total":
    for any total >= 0, count >= 1:
        assert 0 <= average_price(total, count) <= total
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation (Dialektika, 2020), see [[pragmatic-programmer]]. The rule is on p. 336, coverage tools and the limits of knowing on p. 335, the million-state example on pp. 335-336, soft testing on p. 332, and the pointer to property-based testing on p. 336. The book footnotes a study of coverage and defects, [ADSS18] (p. 335), which was not read for this page.

This wiki's own: all of `## Sign in code` and the assignment against the neighbouring pages, the limits in `## When not to apply` other than the two attributed to the book, repair steps 1, 2 and 4, the preference in step 3, and the pseudocode.
