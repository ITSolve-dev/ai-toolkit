---
title: Called vs nested state machines
category: types-and-state
summary: "A parent state machine both runs a sub-machine to completion (loop until done, reset first) and steps another or the same one once per tick, or resets a sub-machine on some paths and resumes it on others, with no stated rule on whether it keeps its state across calls."
tags: [decision-rule, state-machine, automata-based-programming, composition]
paradigm: any
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

When the logic is split across several automata ([[decompose-state-machine-by-modes-or-by-controlled-objects]]), a subordinate automaton relates to its parent in one of two ways (p. 53):

- **Called.** Like a synchronous subroutine call, control passes to the sub-automaton. It starts in its initial state on every call and returns control only after it reaches a final state. How many steps it takes is not known in advance, and it may never return. It can be called with an event, which it handles first. While it runs, every later event goes to it alone.
- **Nested.** Each access performs **one step**, and the state is kept between accesses (the book compares this to coroutines, though only loosely). It handles whatever event exists at the moment of access, so one event can be handled by the parent and by several nested automata. If the parent loops in the same state, the nested automaton is stepped again. It stops when the parent leaves the state, not on its own initiative. Several automata nested in one state step in turn, pseudo-parallel (p. 54).

## Rule

In most cases use only nested or only called automata in one system, because «это делает логику системы более понятной» (p. 54). The two are formally interchangeable: each can be emulated by the other, though emulating the kept state of a nested automaton may need an extra variable in the controlled object. If a system mixes the two, state the semantics of the combination explicitly. Example: does A3, nested in A2, keep its state between calls of A2 from A1? The book says automata-based programming gives no universal answer (p. 54).

As a selecting criterion, the book makes a sub-automaton *called* when its job is a fixed sequence that must not be interrupted before it completes. The parent's transition out of that state can then be unconditional (p. 60).

## Sign in code

This wiki's own reading: one parent machine invokes a sub-machine both as "run until done" (a loop until it reaches its final state, or a reset to the initial state before the run) and as "one step" (a single `step()` per parent tick). Or a sub-machine is reset in some paths and resumed in others, and no comment or type says which semantics applies.

This wiki assigns the shape as follows. Mixing run-to-completion and one-step access to sub-machines in one system, with no stated rule on kept state, is [[called-vs-nested-state-machines]]; the map of the wiring styles themselves is [[interacting-state-machines]].

## When not to apply

- One composition style really cannot express the problem, and the combined semantics is written down. The book allows this.
- A single machine with no sub-machines has nothing to choose.
- Object-oriented code. The book drops nested and called automata there in favour of ordinary method calls between automated classes (pp. 105, 110); see [[decompose-state-machine-by-modes-or-by-controlled-objects]].
- A statechart library or framework that fixes the semantics (history states, reset on entry) has already stated it. This limit is this wiki's own.

## Repair

Pick one style per system. Otherwise document, at the composition point, whether the sub-machine resets on entry and who decides when it ends. In code, this wiki's suggestion is to make the call style visible in the name or signature (`runToCompletion(event)` vs `step()`). The book's diagram convention does the same: a nested automaton is written by its identifier, and a called one with parentheses, optionally holding an event, like a C call (p. 61).

## Before and after

```
// before: mixed, semantics implicit
in state OPENING: opener.step()          // nested
in state CLOSING: closer.reset(); while not closer.done: closer.step()   // called
// does opener keep its state if OPENING is re-entered?
```

```
// after: one style, stated
// all sub-machines are called: start in their initial state, return on final state
in state OPENING: opener.run(OPEN); state = OPEN
in state CLOSING: closer.run(CLOSE); state = CLOSED
```

## Source

Polikarpova, Shalyto, *Automata-Based Programming*, ch. 2, pp. 53-54, 60-61, and ch. 3, pp. 105, 110 ([[automata-based-programming]]). The quotation is verbatim. The sign, the assignment of the shape, the library limit, the naming repair in code, and the pseudocode are this wiki's own.
