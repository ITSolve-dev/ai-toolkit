---
title: "Moore, Mealy and mixed machines: where a state machine's outputs live"
category: types-and-state
summary: "Reference for where a state machine's actions live: on a state (Moore), on a transition (Mealy) or both (mixed), and whether a transition's action sees the old or the new state."
tags: [concept, state-machine, automata-based-programming, outputs]
paradigm: any
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

In structural automata theory, which Polikarpova and Shalyto present as the logic-control half of automata-based programming, a machine with memory is classified by **where its outputs come from** (pp. 27-33). This wiki reads the classification as answering, for code, where an action should be written: on a state or on a transition.

## Classes

- **Combinational circuit (no memory).** The output depends only on the current input: z = f(x). The book says that strictly this is not an automaton at all, and calls it the model of an entity with **simple behaviour**, because the output does not depend on state (pp. 26-27; [[complex-behavior]]). In code, this wiki reads it as a pure function or a decision table, which needs no state machine.
- **Automaton without an output converter.** The output variables are the state, a form the book calls forced encoding. It fits only when control states do not outnumber distinct outputs (p. 28). See [[replace-flags-with-explicit-states]].
- **Moore machine.** The output depends only on the state, through an output function separate from the transition function (p. 31). In code, this wiki reads it as an action that belongs to a state: it runs whenever the machine is in that state, or on entering it.
- **Mealy machine.** The output depends on the state and the input (p. 32). In code, this wiki reads it as an action that belongs to a transition. The book's example is a serial one-bit adder: the states are the carry values, and the sum bit is produced on each transition (p. 33).
- **Mixed (Moore-Mealy, C-automaton).** Some outputs depend only on the state and others also on the input, so the output function splits into two parts (p. 33). The [[automated-object]] model uses this general form.

## First and second kind

A machine of the first kind computes its output from the state before the update. One of the second kind updates the state first and then computes the output from the new value (p. 31). This wiki reads that as a question code has to answer explicitly: does a transition's action see the old state or the new one?

## Trade-off

For any Mealy machine there is an equivalent Moore machine, and it has at least as many states as the original (p. 32). This wiki reads the trade-off as follows: moving transition actions onto states keeps actions in one place per state, but can multiply the states. Keeping them on transitions keeps the graph small, but puts actions on many edges.

How each class maps onto the switch template is on [[state-machine-as-switch-on-state]].

## Source

Polikarpova, Shalyto, *Automata-Based Programming*, [[automata-based-programming]], section 1.4.2 (pp. 25-33). The book gives schematics and equations, not code. The mapping of each class to where code puts an action, and the reading of first and second kind and of the Moore/Mealy trade-off, are this wiki's own.
