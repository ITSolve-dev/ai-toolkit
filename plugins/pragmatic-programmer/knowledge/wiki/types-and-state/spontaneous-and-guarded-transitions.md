---
title: Spontaneous and guarded transitions
category: types-and-state
summary: "A state machine whose transitions fire on the machine's own initiative after checking a condition, or a flowchart turned into states: guards on a diagram are checked at once, while an if/else-if chain checks them in order and silently resolves overlaps by line order."
tags: [concept, state-machine, transitions, guards, flowchart]
paradigm: any
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

In abstract automata, a change of state that no input symbol causes is called an ε-transition. The source also uses the terms «спонтанный переход», «немотивированный переход» and «переход по завершении» for it (p. 21). Formal language theory shows that ε-transitions, like non-determinism, do not widen the class of recognised languages, so any automaton that has them reduces to an equivalent DFA (p. 22).

The source stresses the programming side. Many software automata have only spontaneous transitions, which the book calls *active* models (p. 22). Spontaneous does not mean unconditional: «Спонтанность выражается в том, что переход совершается по инициативе самого автомата» (p. 22). The automaton may first check a condition and then decide whether to take the transition, and such a transition is said to be guarded by that condition (p. 22).

## Flowcharts are transition diagrams

Spontaneous transitions make a traditional flowchart a special case of a transition diagram, according to the source. Each step that is not final has either one unconditional ε-transition or several ε-transitions labelled with independent conditions (p. 22). For flowcharts the source uses the term «переход по завершении»: the transition happens because the actions prescribed to the current state have finished (p. 23).

The difference that matters for code is how the conditions are checked. In a flowchart, a set of conditional exits is drawn as a segmented transition, and «условия проверяются не одновременно, а одно за другим» (p. 22). On a transition diagram, all the conditions leaving a state are checked at once (p. 22).

## What this means for code

The reading for code here is this wiki's own. An `if / else if` chain inside a state handler is a segmented transition: when two conditions overlap, the first one wins, and that priority is written only in the line order. On a transition diagram drawn from that code the same two arrows look equal, so the diagram and the code disagree whenever both guards are true.

- If the guards leaving a state are mutually exclusive, order does not matter, and the code matches its diagram.
- If they can overlap, the priority has to be made explicit or the guards made exclusive. The rule that owns this shape, with its repair and limits, is [[transition-conditions-consistent-and-complete]]: overlapping guards, or a missing fallback, among the transitions leaving one state are [[transition-conditions-consistent-and-complete]].

This wiki also notes a limit: a plain sequential algorithm whose exits really are priority-ordered (try the cache, then the replica, then the primary) is a flowchart, and its order is its meaning. Restating it as a diagram with exclusive guards adds no information.

## Example

```
// before: overlapping guards, priority hidden in line order
in state WAITING:
  if timeout_elapsed: go FAILED
  else if reply_received: go DONE
// a reply arriving exactly at timeout -> FAILED, though a diagram shows two equal arrows

// after: guards exclusive, the diagram can be read as the code
in state WAITING:
  if reply_received: go DONE
  else if timeout_elapsed and not reply_received: go FAILED
  else: stay WAITING
```

Related: [[finite-state-machine]], [[finite-memory-folds-into-states]], [[finite-automaton-limits]].

## Source

Polikarpova, Shalyto, *Automata-Based Programming*, pp. 21-23 ([[automata-based-programming]]): ε-transitions and their other names, their equivalence to a DFA, active models, guarded spontaneous transitions, flowcharts as transition diagrams, segmented transitions checked in order against simultaneous checks on a diagram, and the meaning of «переход по завершении». The reading for code, its limit and the pseudocode are this wiki's own.
