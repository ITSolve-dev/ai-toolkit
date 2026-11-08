---
title: Complex (state-dependent) behaviour
category: types-and-state
summary: "A handler that does something different for the same input depending on a field earlier inputs set (the same button acts differently by mode) marks complex behaviour, the precondition for replace-flags-with-explicit-states, which decides whether explicit states pay; a handler that does the same thing every call, only on different values, is simple behaviour."
tags: [concept, state-machine, state-dependent-behavior, applicability]
paradigm: any
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

**Complex behaviour** is Polikarpova and Shalyto's test for when automata-based programming applies. Informally, an entity (an object or subsystem) has complex behaviour if it can respond to an input with one of several outputs, and the choice may depend «не только от входного воздействия, но и от предыстории» (p. 8). For an entity with **simple behaviour**, the reaction to any input depends only on that input (p. 8). The book notes that complex behaviour is also called *state-dependent behaviour*, and simple behaviour *state-independent* (p. 8, footnote 1).

## The book's example

A clock with two buttons, H and M, that add one to the hours and the minutes (modulo 24 and 60) has simple behaviour: each press always produces the same predetermined reaction (p. 8). Add an A button that switches the alarm on and off and puts H and M into alarm-setting mode, and the behaviour becomes complex. The same presses now trigger different actions depending on the mode (pp. 8-9). The book lists devices, network protocols, dialog boxes and game characters as common entities with complex behaviour (p. 9).

## Why it is the criterion

Once the concept of state is introduced, knowing the history is no longer needed. The state implicitly sums up every past input that affects the present reaction, so the reaction depends only on the input and the current state (p. 11). This wiki reads complex behaviour therefore as marking an entity whose history has to be kept somewhere. The question that follows is whether it is kept as named control states or scattered across flags ([[replace-flags-with-explicit-states]], [[control-and-computational-states]]).

The book gives two recommendations. The first is to use the automata approach in any system that has entities with complex behaviour, which in the authors' experience means almost every serious system. The second is to use it only for those components that do have complex behaviour (p. 11). In the structural theory the simple case is the combinational circuit, whose output depends only on the current input (pp. 26-27; [[moore-and-mealy-machines]]).

## Discriminating test in code

This wiki turns the definition into a check on a handler. Take one input (one method or one event) and ask whether its body chooses a different action depending on a field that earlier inputs set. If it does, the behaviour is state-dependent. Whether explicit states pay for it is decided on [[replace-flags-with-explicit-states]], whose limit holds that a single flag tested in a single place is a plain conditional, not a hidden machine. If the body does the same thing every call, and only the *values* it reads differ (for example, adding 1 to whatever the counter holds), the behaviour is simple, and an explicit state machine would add no clarity. That second case is the first limit stated on [[replace-flags-with-explicit-states]].

## Source

- Polikarpova, Shalyto, *Automata-Based Programming*, ch. 1 ([[automata-based-programming]]). The definition, pp. 7-8 with footnote 1; the clock examples, pp. 8-9; state as a summary of history and the two recommendations, p. 11; the combinational case, pp. 26-27.
- This wiki's own parts: the discriminating test in code.
