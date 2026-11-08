---
title: "Interacting state machines: nested, called and pseudo-parallel automata in code"
category: types-and-state
summary: "Reference for reading code with several state machines: one step function each, a nested machine stepped once from a parent's action, a called machine looped to its final state, parallel machines stepped in turn from one loop (call order is semantics), active versus passive stepping."
tags: [concept, state-machine, decomposition, concurrency]
paradigm: any
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

When a system's logic is decomposed into several automata ([[decompose-state-machine-by-modes-or-by-controlled-objects]]), Polikarpova and Shalyto implement each automaton's step as its own function and wire them in a small number of fixed ways (pp. 82-85). This page records those ways as a map for reading and reviewing such code. The signs and repairs belong to the pages named below; the shape of one step function is [[state-machine-as-switch-on-state]].

## The forms

- **One step function per automaton.** The book: «такт работы каждого из автоматов удобно реализовать в виде отдельной функции» (p. 82).
- **Interaction by state numbers.** In logic control, guards may test another automaton's state variable alongside inputs (p. 82). In the two-valve example the second valve starts opening when the first one's state is "open" (p. 84). The book's own later chapters replace this with events, and the rule against it is [[state-machines-communicate-through-an-explicit-interface]].
- **Nested automaton.** Called from an action by calling its step function, one step per step of the enclosing machine (p. 82).
- **Called automaton.** Run to completion: a wrapper sets it to its initial state and loops (read inputs, step, write outputs) until it reaches its final state (listing 2.4, p. 83). The caller blocks for the whole run, which is the difference from a nested one. Mixing run-to-completion and one-step access to sub-machines in one system, with no stated rule on kept state, is [[called-vs-nested-state-machines]].
- **Parallel decomposition on one processor.** Pseudo-parallel execution needs no multitasking: the main loop calls each automaton's step in turn (p. 83, fig. 2.31; listing 2.5). On separate processors each automaton gets its own loop, and data consistency and synchronisation come to the fore, with the solution depending on the system (p. 84).
- **Active and passive.** An active automaton (logic control) is stepped in an endless loop owned by its implementation; a passive one (event-driven software) is stepped by its environment, so the main program is no longer part of the automaton's implementation (p. 87). How a passive machine receives its event is [[passing-events-to-a-state-machine]].

## Reading it in code

This wiki's own reading, as review checks:

- A called automaton's loop blocks the caller until the final state. If its final state is unreachable from some state, the caller hangs, so a review checks that the final state is reachable from every state of the called machine (the reachability check of [[transition-conditions-consistent-and-complete]], run backwards from the final state).
- Pseudo-parallel stepping makes the order of the calls in the loop part of the semantics: a machine stepped later sees the others' new states in the same cycle. A reordering of those calls is a behaviour change, not a tidy-up.
- In object-oriented code the book replaces nesting and calling with ordinary method calls between automated classes ([[automated-class]], [[decompose-state-machine-by-modes-or-by-controlled-objects]]).

## Source

Polikarpova, Shalyto, *Automata-Based Programming* ([[automata-based-programming]]): one function per automaton and interaction by state numbers, p. 82; nested and called automata, pp. 82-83; pseudo-parallel and multiprocessor execution, pp. 83-84; the two-valve example, pp. 84-85; passive automata and the main program, p. 87. The "Reading it in code" checks are this wiki's own.
