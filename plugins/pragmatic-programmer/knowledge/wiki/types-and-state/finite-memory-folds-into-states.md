---
title: Finite memory folds into the state set
category: types-and-state
summary: "A state variable alongside boolean flags or small enums that change what a state does (state = RUNNING plus paused): the real state space is their product, and the flags are unnamed states; only unbounded memory (a count, a stack) cannot be folded in."
tags: [concept, state-machine, flags, hidden-state]
paradigm: any
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

An abstract machine is a finite control (a deterministic finite automaton) plus some kind of extra memory. Polikarpova and Shalyto note that the extra memory adds computational power only when it can hold infinitely many values, as the stack of a pushdown automaton or the tape of a Turing machine can: «только бесконечная дополнительная память (которая может хранить бесконечное множество значений) увеличивает вычислительную мощность абстрактной машины» (p. 25). If the set of memory values V is finite, then «вычислитель всегда может быть преобразован в эквивалентный ДКА» (p. 25). The equivalent DFA's state set is the Cartesian product Y × V of the original states and the memory values (p. 25).

## What this means for code

The transfer to code here is this wiki's own. Code often keeps an explicit `state` variable together with booleans or small enums (`isRetrying`, `wasPaused`, `mode`) that the handlers consult to decide what to do. By the theorem above, such a component is still a finite automaton, but one whose real states are the pairs (state, flags). A state variable with 4 values and 2 independent booleans has up to 16 real states, and most of them have no name, no diagram and no test.

This wiki draws two consequences from that.

- **The diagram lies.** A transition diagram drawn over `state` alone leaves out the behaviour that the flags select. A reader who checks the code against it misses whole states.
- **Some combinations are unreachable or invalid,** but nothing in the code says so.

The repair this wiki proposes is to fold each flag that changes a state's behaviour into the state set, giving each meaningful pair its own named state. A flag that never changes which transition fires (a counter used only for logging, say) stays outside. The criterion is whether the handler for a state branches on the flag. The rule that owns this shape in code, with its limits: an existing state variable with extra flags beside it that change what a state does is [[replace-flags-with-explicit-states]].

## Limits

- Data that is legitimately unbounded (a count, a buffer, a stack of nested scopes) cannot be folded. This is exactly the case where the source says memory adds power. It stays as data next to the control states, as in a pushdown automaton; see [[finite-automaton-limits]].
- When flags really are independent, so the product would explode into many states that each behave the same way along one dimension, folding them in makes the diagram worse. Separate machines are the better shape there ([[decompose-state-machine-by-modes-or-by-controlled-objects]]). This limit is this wiki's own reasoning, since the source states only the equivalence.

## Example

```
// before: 3 states x 1 flag, behaviour depends on both
state = IDLE | RUNNING | DONE
paused = false
on tick:
  if state == RUNNING and not paused: step()
on pause:  if state == RUNNING: paused = true
on resume: paused = false
on stop:
  if state == RUNNING and paused: discard(); state = DONE
  else if state == RUNNING: finish(); state = DONE

// after: the flag folded into the state set
state = IDLE | RUNNING | PAUSED | DONE
on tick:   if state == RUNNING: step()
on pause:  if state == RUNNING: state = PAUSED
on resume: if state == PAUSED:  state = RUNNING
on stop:
  if state == PAUSED:  discard(); state = DONE
  if state == RUNNING: finish();  state = DONE
```

In the before version, the combinations `IDLE + paused` and `DONE + paused` exist and nothing defines them. In the after version they do not exist.

Related: [[finite-state-machine]], [[spontaneous-and-guarded-transitions]], [[control-and-computational-states]].

## Source

Polikarpova, Shalyto, *Automata-Based Programming*, p. 25 ([[automata-based-programming]]): only infinite memory increases power, and finite memory gives an equivalent DFA over Y × V. Reading flags as hidden states, the criterion for folding, both limits and the pseudocode are this wiki's own.
