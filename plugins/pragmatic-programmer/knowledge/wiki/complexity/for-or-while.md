---
title: For or while
category: complexity
summary: "A for loop whose index is assigned inside the body to force an exit, a for over a huge literal bound used as an endless loop, a while whose counter init, test and update could sit in a for header, or an index walked only to read items[i]: pick for, while or foreach by who controls the loop."
tags: [decision-rule, loops, control-flow, loop-index]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell separates loops by two properties: whether the number of iterations is fixed in advance, and where the termination test sits (pp. 359-360). The `for` loop is for the fixed, set-and-forget case. The `while` loop is for a count that is not known in advance. A foreach-style loop over a container removes index arithmetic altogether (p. 364). This wiki reads the choice as mattering because each form tells the reader where control lives, and a `for` whose control is changed from inside its body tells the reader something false.

## Rule

- Use `for` for simple cases that need no control from inside the body, where the control is a plain increment or decrement (p. 364). In the book's words, set it up at the start and forget it.
- «Не изменяйте значение индекса цикла for явно, чтобы принудительно его завершить.» Use `while` instead (p. 364). On pp. 369-370 McConnell calls tampering with the index to leave early the mark of an amateur.
- «Предпочитайте циклы for, если они применимы» (p. 366). In a `for` the control code sits in one place. In a `while` a maintainer can change the initialization at the top and forget the matching update at the bottom.
- For a loop that never ends, write `while (true)` (or `for (;;)`). Do not fake it with `for i = 1 to 99999`. The literal bound hides the meaning, may itself be a legal value, and is hard to maintain (p. 366).
- Where the language has a loop over each element of a container, use it. It removes the auxiliary index arithmetic and the errors that come with it (p. 364).

## Sign in code

- An assignment to a `for` loop's index inside its body, typically to its upper bound or beyond, to stop the loop.
- A `for` with a large literal bound and a body that is expected to run until something external happens.
- A `while` that walks a counter: initialized just before the loop, compared in the condition, incremented as the body's last statement, with nothing else affecting termination.
- A loop that walks an index only to read `items[i]`, where the index is used for nothing else.

This wiki assigns the neighbouring cases as follows. This page owns the choice of loop form, including an index walked only to read each element in order. An index expression that can leave the array or cross another index is [[array-index-discipline]]. A `for` header holding expressions that do not control the loop is [[loop-header-holds-only-control]]. Exits by `break` and `continue` are [[break-and-continue]].

## When not to apply

- A single `break` out of a search `for`. The book pulls two ways here. On p. 364 it says to switch to `while` when a loop is interrupted from inside, yet its recommended rewrite on pp. 370-371 keeps a `for` with one `break` and a `found` flag. This wiki resolves it per setting. Assigning to the index is always a violation. One `break` from a short `for` that searches a bounded range is accepted; [[break-and-continue]] owns it and does not report it. A search loop with *no* exit at the hit is [[stop-loop-once-answer-known]]. Several exits move the loop to `while`.
- Termination depends on data produced inside the body (reading until end of input, convergence). That is a `while` by definition. A `for` whose header holds only control but whose termination depends on data read in the body is accepted by the book (p. 367): [[for-or-while]] may prefer a `while`, and [[loop-header-holds-only-control]] does not report it.
- Code with no explicit loop (a map, a fold, or a whole-collection operation) is outside this page.

## Repair

1. Where the index is assigned to force an exit, turn the loop into a `while` whose condition states both the bound and the early-exit condition.
2. Where a `for` fakes an infinite loop, replace it with `while (true)` and a comment saying what ends it.
3. Where a `while` merely counts, move its initialization, test and update into a `for` header.
4. Where the index serves only to fetch elements, iterate the elements.

## Before and after

```
for i = 0; i < 100; i++:
    process(i)
    if done(i):
        i = 100          // forced exit
```

```
i = 0
finished = false
while i < 100 and not finished:
    process(i)
    finished = done(i)
    i = i + 1
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]], sections 16.1-16.2: loop kinds, pp. 359-360; `for` and foreach, p. 364; `while (true)` and "prefer for", p. 366; index tampering, pp. 369-370; the `found` rewrite, pp. 370-371. The reading of why the form matters, the resolution of the book's two positions on a single `break`, the third and fourth signs, the assignment against the neighbouring pages and the pseudocode are this wiki's own.
