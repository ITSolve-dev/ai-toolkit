---
title: "Table or switch: choose a state machine's representation by whether it changes at run time"
category: types-and-state
summary: "A transition table assembled at start-up for a state machine that never changes afterwards, a state machine hard-coded as a switch although its states or transitions are loaded or edited while the program runs, or a transition table indexed by the full vector of boolean inputs."
tags: [decision-rule, state-machine, transition-table, switch]
paradigm: any
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

A state machine can be represented in code in two ways: as data (tables of outputs and transitions held in memory) or as code (a selection on the state, with guarded branches). Polikarpova and Shalyto decide between them by one question: must the automaton be modified while the program runs (pp. 79-80, 87).

## Rule

- **Table** when the automaton is created or modified at run time. The source says tables are built dynamically, so this representation «является более гибким по сравнению с использованием инструкции выбора: автомат можно изменять в ходе выполнения программы» (p. 79), at the price of some performance. The book's example need is run-time optimisation of automata (section 4.4, p. 80).
- **Selection with guarded branches** otherwise. It is static, faster, and makes the isomorphic conversion from the graph simpler. Tasks needing run-time modification «встречаются довольно редко» (p. 87), so this remains the most used template. The shape of that selection is owned by [[state-machine-as-switch-on-state]].
- **Do not index by the full input vector.** A transition table with s rows and 2^n columns grows exponentially with the number of inputs (p. 79). Each state depends on only a few significant inputs, so a compact table stores only those (pp. 79-80).

This wiki assigns the neighbouring cases as follows. Whether a state machine's transitions are held as a table or as a switch is [[state-machine-table-or-switch]]; a table for repeated dispatch outside a state machine is [[drive-repeated-dispatch-from-a-table]]. The shape of the switch itself (state first, one guarded branch per arc, no nested selection over every input combination) is [[state-machine-as-switch-on-state]].

## Sign in code

This wiki's own reading:

- A transition table is assembled at start-up from constants that never change afterwards, and its cells hold guards over several inputs or priorities.
- A machine whose states or transitions are edited at run time (loaded from configuration, rewritten by an optimiser) is nonetheless hard-coded as a selection, so every change requires editing and redeploying code.
- A table indexed per state by an encoding of all n boolean inputs, most of whose cells lead to the same next state.

## When not to apply

- **This source and *The Pragmatic Programmer* disagree on the form.** This wiki resolves it per setting, in the words of [[state-machine-as-switch-on-state]]: where every transition is keyed by the state and an event type alone and its action is a name, the table of [[finite-state-machine]] is the shorter form; where transitions are guarded by conditions over several inputs, or carry priorities, or where each event reaches the machine through its own handler or event method (*Automata-Based Programming*, pp. 88-89), the switch with one guarded branch per arc of [[state-machine-as-switch-on-state]] is the form. A project convention on state-machine form overrides both. The first sign above therefore does not fire on a state-by-event table.
- Where the source's efficiency argument does not hold (desktop event-driven systems, p. 87), the choice may be decided by flexibility and readability instead. The source says flexibility gains weight there, while keeping isomorphism first (p. 87).
- This wiki adds: a table generated from the graph by a tool and never read by people is not bound by the readability argument for a switch.
- In object-oriented code other patterns exist (section 3.3, p. 87). The choice among them is [[switch-on-state-vs-state-pattern]].

## Repair

- Static machine held as a run-time table over guarded inputs: replace the table with one selection on the state, a guarded branch per arc.
- Machine that must change at run time held as code: move states and transitions into data (per state, a list of guard, actions and target) and keep one generic step function that walks it.
- Table over the full input vector: per state, store only the transitions, with their guards over the significant inputs.

## Before and after

```
// before: a fixed machine held as a table over all input combinations
transitions = new Table(rows = stateCount, cols = 2^inputCount)
for each state s, for each input vector v:
    transitions[s][v] = s             // default: stay
transitions[CLOSED][vectorWith(openRequested)] = OPENING
...
function step(inputs):
    state = transitions[state][encode(inputs)]
```

```
// after: the machine is fixed, so it is code with one branch per arc
function step():
    switch state:
        case CLOSED:
            if openRequested(): state = OPENING
        case OPENING:
            if reachedOpen(): state = OPEN
        ...
```

## Source

Polikarpova, Shalyto, *Automata-Based Programming* ([[automata-based-programming]]): the two ways of implementation and the flexibility and cost of tables, p. 79; exponential growth and compact tables, pp. 79-80; static selection where no run-time modification is needed, p. 80; rarity of run-time modification and the most used template, p. 87. The signs in code, the assignment of neighbouring cases, the limit about generated tables and the repairs are this wiki's own; the resolution against *The Pragmatic Programmer* is copied from [[state-machine-as-switch-on-state]].
