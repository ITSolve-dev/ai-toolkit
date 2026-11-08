---
title: Remove calls you cannot justify
category: complexity
summary: "A run of near-synonymous calls on one object with nothing between them (refresh, redraw, flush, sync), left in because the result finally looked right."
tags: [rule, accidental-complexity, superstitious-code, coincidence]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

Calls added one after another until the output looks right are a form of [[programming-by-coincidence]]: the sequence works, nobody knows which part does the work, and the rest stays out of fear. The book's example is a programmer trying to get something drawn with a GUI framework by calling six overlapping repaint routines in a row (p. 247).

## Rule

Every call stays only because someone can say what it contributes to the result. Working output is not a reason to leave the code alone. The book names that reasoning, that it is better «не трогать то, что и так работает» (p. 247), as the trap.

The book gives five reasons to go back (p. 247):

- The program may only look as if it works.
- The boundary condition it depends on may be chance, so behaviour differs with screen resolution or processor core count.
- Undocumented behaviour may change in the next library release.
- Extra calls can slow the program.
- Extra calls raise the risk of new bugs.

## Sign in code

- Two or more calls with overlapping names or purposes on the same object, with no state change between them.
- The same call with the same arguments made twice on one object on one path, with no state change between them and no comment giving a reason.
- A delay or a retry added next to such a call, with no stated cause. This page owns that shape. Where a comment blames a dependency, [[select-isnt-broken]] owns it.

## When not to apply

- The sequence is a protocol that the API documentation requires, and each step is named there, such as begin, write, commit. The sequence is then a contract, not superstition.
- A repeated call is deliberate and carries its reason in a comment, such as a documented workaround for a known defect with a reference.
- There is no way to observe the result. Do not delete blindly: first make the effect checkable, because removal without observation is the same coincidence in reverse.

## Repair

1. Read the documentation of each call and state what it does.
2. Remove the calls one at a time, checking the result after each.
3. Keep the minimum. If a call turns out to be needed and the reason is not obvious, record the reason next to it.

## Before and after

```
// before
connection.send(frame)
connection.flush()
connection.sync()
connection.flush()
connection.commitBuffer()
sleep(50)
```

```
// after: flush is documented to deliver everything buffered
connection.send(frame)
connection.flush()
```

## Source

[[pragmatic-programmer]], Topic 38, p. 247, for the case and the five reasons. The signs, the limits, the repair and the example are this wiki's own. The rule's wording is this wiki's reading of the book's example.
