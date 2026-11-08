---
title: Control states and computational states
category: types-and-state
summary: "Telling a variable that selects which action runs (a few named, qualitatively different values, a mode) from one that only holds the result of actions (counters, positions, times): only the first kind becomes explicit states; a mode or phase field mixed among the data fields and tested ad hoc in every routine is the first kind hidden in the second, owned by state-machine-as-switch-on-state (one mode variable) or replace-flags-with-explicit-states (flags)."
tags: [concept, state-machine, control-state, computational-state, automata-based-programming]
paradigm: any
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

In automata-based programming the state of an entity is split into two kinds. **Control states** (управляющие) are few. Each is named and decides what the entity does. **Computational states** (вычислительные) are the large or unbounded remainder of the data, which only records the results of what was done. The split decides which variables belong in an explicit state machine and which stay ordinary data. It is the discriminating criterion behind [[replace-flags-with-explicit-states]] and the line that [[logic-vs-semantics-split]] places.

## What a state is

The book's definition of state is the one from Turing and control theory: the current state «несет в себе всю информацию о прошлом системы, необходимую для определения ее реакции на любое входное воздействие» (p. 11). With a state in hand, the history is no longer needed, and the reaction depends only on the input and the current state (p. 11). The traditional view of a program's state as the values of all its variables gives a state space that is unmanageably large (p. 15). That is why the book does not stop there.

## Where the split comes from

The authors build the distinction on a Turing machine that increments a binary number (pp. 13-14). Its control automaton has three named states. The machine as a whole, counting every tape content and head position, has infinitely many. Even so, it was enough to describe its behaviour in each of the three control states, and no reaction to each possible tape had to be specified. In the book's words, «состояния управляющего автомата определяют действия машины, а состояние ленты – лишь результат этих действий» (p. 14). The authors compare this to a class: it has only a few methods but endlessly many argument values, and the method name picks the algorithm while the arguments decide only the result (p. 14).

The conclusion they draw is that the two kinds must not be mixed. Control states are listed explicitly, drawn on the transition graph and given a behaviour each. Computational states do not appear in the program explicitly, and even if a graph of them could be built, it would be useless for understanding the program (p. 15).

## Discriminating criteria

Table 1.1 (p. 16), paraphrased:

| Control states | Computational states |
|---|---|
| «Их число не очень велико» | Infinitely many, or finite but very many |
| Each has a definite meaning and differs from the others *qualitatively* | Most have no meaning of their own and differ only *quantitatively* |
| They determine the actions the entity performs | They directly determine only the results of actions |

The book states that the difference is hard to formalise in general. For a Turing machine it is given by construction, but for an arbitrary entity, explicitly identifying the control states is a hard task (p. 15). Unless stated otherwise, "state" in the book means control state (p. 15, footnote 2).

The book's practical tip, from chapter 2, is to search the description of the behaviour for "situations" in which it is qualitatively different. It treats the word *mode* as a synonym of control state: «Если в описании поведения системы упоминаются несколько режимов, то каждому из них наверняка будет соответствовать отдельное состояние» (p. 44). In the alarm-clock example the three control states are "alarm off", "setting alarm time" and "alarm on"; the four integers for hours and minutes (current and alarm) are computational state (pp. 44-46).

This wiki applies the table to code with three tests:
- Can you name each value after what the entity *does* in it ("setting alarm")? If the name only states an amount ("minutes = 37"), the variable is computational.
- Do handlers branch on the variable to choose *which* action runs, or do they only pass it into a calculation?
- Would a transition diagram over its values be readable? If it would need a node per number, the variable is computational.

## Design order

The book's procedure for designing one automaton puts the control states first and the data last (pp. 43-44):

1. Derive the set of control states from the verbal description of the behaviour.
2. Connect the states with transitions and add the input and output variables (and the events, if the system is event-driven).
3. Map each input variable to a query and each output variable to a command of the controlled object ([[automated-object]]). A command that is not simple enough is refined by ordinary top-down decomposition.
4. Only then introduce the variables those queries and commands need. Their combined values are the computational state.

The book's argument for this order is design stability: the question "what states can the system be in?" has a steadier answer than "what does the system do?", so a structure built on control states extends better (p. 46).

## Failure modes

- **Control state hidden in data.** The book's thought experiment (p. 16) is a Turing machine with no control automaton, its algorithm coded on the tape. It would still behave differently at different steps, but its description would no longer show that, and the logic would be lost among details. The book says Listing 1.1 has the same defect (p. 16). This wiki reads the code-level form as a mode field sitting among the data fields and tested ad hoc inside every routine, or as flags. Code that already holds the mode in one state variable but does not mirror the transition graph is [[state-machine-as-switch-on-state]]. Flags held as fields of one entity and tested in combination by several of its own input handlers to choose a reaction are [[replace-flags-with-explicit-states]].
- **Control information in shared data.** The book advises against abusing a shared controlled object: adding variables to it that concern control rather than computational state (pp. 54-55, footnote 7). See [[state-machines-communicate-through-an-explicit-interface]].
- **Computational state forced into a machine.** This wiki adds the opposite failure, which the book only implies: turning counters, positions or similar values into enumerated states produces a graph that the book calls useless for understanding (p. 15). [[logic-vs-semantics-split]] owns that shape as "logic overloaded".

## Limits

This wiki's own reading: the split pays where behaviour differs qualitatively between situations. If a component has one mode, a state machine is accidental complexity ([[complex-behavior]]). The book itself warns that a single automaton suits only very small systems, and that a growing automaton needs decomposition (p. 51). See [[decompose-state-machine-by-modes-or-by-controlled-objects]].

## Source

- Polikarpova, Shalyto, *Automata-Based Programming* ([[automata-based-programming]]). Ch. 1: the definition of state, p. 11; the Turing-machine argument and the class analogy, pp. 13-14; the split and its terms, p. 15; Table 1.1 and the tape-only thought experiment, p. 16. Ch. 2: the design procedure, pp. 43-44; modes as control states and the alarm-clock states, pp. 44-46; design stability, p. 46; a single automaton for small systems, p. 51; control information kept out of a shared object, pp. 54-55.
- This wiki's own parts: the three tests for code, the code-level reading of "control state hidden in data" and its assignment to owners, the "computational state forced into a machine" failure mode, and the limit on single-mode components.
