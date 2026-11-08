---
title: Implement a state machine as a switch on the state with one guarded branch per transition
category: types-and-state
summary: "Code that holds a mode in a state variable but does not mirror the transition graph: inputs tested first and the state inside, the state assigned in several places or outside the step function, or a selection over every combination of inputs where one or two decide; no block of code corresponds to one state or one transition."
tags: [rule, state-machine, isomorphism, switch, transition-graph]
paradigm: any
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

Once behaviour has been designed as a state machine (a transition graph), Polikarpova and Shalyto have the code that runs it mirror the graph one to one: an outer selection on the current state, and inside each state's branch one guarded branch per outgoing transition, whose condition is the transition's label and whose body updates the state. They call this one-to-one correspondence isomorphism and rank it among the criteria for implementing automata (pp. 77-78, 87).

## Rule

The source states three criteria for implementing an automaton (pp. 77-78): the graph must be convertible into code formally («Это преобразование должно быть формальным и однозначным»), the code must be isomorphic to the graph, and, for control systems, it must be time- and memory-efficient. On isomorphism: «каждому структурному элементу графа переходов (состоянию, переходу) должна соответствовать отдельная конструкция языка программирования».

The template that meets them (pp. 80-81, listing 2.2):

- the step function opens with a **state decoder**: a selection on the state variable, one case per state;
- in a Moore machine each case first sets the outputs of that state, then has **one `if / else if` per outgoing arc**, the arc's boolean label as the condition and the assignment of the target state as the body;
- a self-loop needs no branch in a Moore machine (p. 81);
- in a Mealy machine the output actions move inside the transition branch, and in event-driven software they become calls of the controlled object's commands rather than assignments to output variables (pp. 85, 87; listing 2.6). Where actions live is [[moore-and-mealy-machines]].

The book first shows a nested selection on the whole input vector (listing 2.1) and rejects it: the number of input cases grows as 2^n with the number of inputs (p. 80). Guarded branches fix this, because in a real state only a few inputs matter and the arc labels stay small as inputs grow (pp. 80-81). The source notes the fix also made the formal conversion simpler (p. 81).

**Order of branches.** A chain of `if / else if` is tested in text order, while arcs on a graph have no order. The source resolves it: in a consistent graph the order does not matter; if arcs carry priorities, the branches must appear in priority order (p. 81). The `else` in the valve example is there only for speed, since its guards are mutually exclusive (p. 82). Overlapping guards and a missing fallback are owned by [[transition-conditions-consistent-and-complete]].

## Sign in code

This wiki's own translation:

- The same handler tests inputs first and the state inside, or mixes the two, so the branches of one state are scattered among several input checks.
- A state assignment (`state = ...`) appears outside the step function, or in more than one place per transition. Client code that reads or writes a machine's state field is [[automated-class]].
- A selection enumerates every combination of inputs in a state where only one or two inputs decide the next state.

This wiki assigns the neighbouring cases as follows. Code that already holds the mode in one state variable but does not mirror the transition graph is [[state-machine-as-switch-on-state]]. Flags held as fields of one entity and tested in combination by several of its own input handlers to choose a reaction are [[replace-flags-with-explicit-states]]; flags that one loop over a sequence of events sets and tests to track its place in that sequence are [[finite-state-machine]].

## When not to apply

- The behaviour has not been designed as a state machine and has two or three trivially distinct modes; introducing a state variable and a transition graph then is this wiki's judgement call, not the source's prescription ([[complex-behavior]]).
- The automaton must be **changed while the program runs** (built, optimised or edited at run time): the source sends this case to a table representation, which it calls more flexible at some cost in performance, and notes such tasks are rare (pp. 79-80). See [[state-machine-table-or-switch]].
- **This source and *The Pragmatic Programmer* disagree on the form.** *The Pragmatic Programmer* recommends a transition table driven by a loop ([[finite-state-machine]]); this source recommends the switch. The tables differ: this source's table is indexed by the full input vector and grows exponentially with the inputs (p. 79), while the other book's table is indexed by state and event type. This wiki resolves it per setting: where every transition is keyed by the state and an event type alone and its action is a name, the table of [[finite-state-machine]] is the shorter form; where transitions are guarded by conditions over several inputs, or carry priorities, or where each event reaches the machine through its own handler or event method (*Automata-Based Programming*, pp. 88-89), the switch with one guarded branch per arc of [[state-machine-as-switch-on-state]] is the form. A project convention on state-machine form overrides both.
- In object-oriented code the source points to a wider set of patterns (section 3.3, p. 87); this page records the procedural template, and the choice between a switch and the State pattern is [[switch-on-state-vs-state-pattern]].
- When an event-per-function structure is chosen, the outer branch is on the event, not on the state; see [[passing-events-to-a-state-machine]].

## Repair

1. Name the states and give the machine one state variable.
2. Write one step function whose body is a selection on that variable, one case per state, each case commented with the state's name.
3. In each case write one guarded branch per outgoing transition: condition = the arc label over inputs (or events), body = outputs or actions of the transition, then the new state.
4. If arcs have priorities, order the branches by them; otherwise make the guards mutually exclusive so order does not matter.
5. Move the reading of inputs and the performing of actions into named queries and commands of the controlled object ([[separate-control-object-from-state-logic]]).

## Before and after

```
// before: a state variable exists, but inputs are tested first
function onTick():
    if reachedOpen():
        if state == OPENING: state = OPEN
    if state == OPEN and closeRequested():
        state = CLOSING
    if reachedClosed() and state == CLOSING:
        state = CLOSED
    if state == CLOSED and openRequested():
        state = OPENING
    if state == OPENING: driveForward()
    else if state == CLOSING: driveBack()
    else: stopMotor()
```

```
// after: one case per state, one guarded branch per arc
function step():
    switch state:
        case CLOSED:
            stopMotor()
            if openRequested(): state = OPENING
        case OPENING:
            driveForward()
            if reachedOpen(): state = OPEN
        case OPEN:
            stopMotor()
            if closeRequested(): state = CLOSING
        case CLOSING:
            driveBack()
            if reachedClosed(): state = CLOSED
```

In the before, one tick can run several transitions in a row (CLOSING to CLOSED to OPENING when the valve closes while an open is requested), and the reader cannot see from any one block what CLOSED does. In the after, each step takes at most one arc, and each arc is one branch of its state.

**Failure mode, this wiki's reading.** In the book's own two-valve listing (p. 84) one transition writes `y = 4` where the machine's state variable is `y1`. With numbered global state variables per automaton, a wrong name compiles and silently breaks the transition. This wiki reads that as an argument for giving each machine's state a distinct, named type or an owner that only its own step function can assign.

## Source

Polikarpova, Shalyto, *Automata-Based Programming* ([[automata-based-programming]]): criteria of implementation, pp. 77-78; table versus selection, pp. 79-80; templates 2.1 and 2.2, pp. 80-81; branch order and priorities, p. 81; valve example, p. 82; the two-valve listing, p. 84; Mealy and event-driven changes, pp. 85-87. The signs in code and their assignment, the resolution against *The Pragmatic Programmer*, the item about trivial modes, the repair steps as a list, the pseudocode and the failure-mode reading of the two-valve listing are this wiki's own.
