---
title: What a finite automaton cannot do
category: types-and-state
summary: "A state machine, a set of flags or a regular expression used to track nested or arbitrarily deep structure (brackets, nested blocks, tags closing in reverse order), with depth-limited states such as IN_ONE, IN_TWO: finite control cannot hold unbounded memory or look ahead, so the nesting needs a stack."
tags: [concept, state-machine, computational-power, pushdown, parsing]
paradigm: any
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

Polikarpova and Shalyto describe abstract automata by the languages they recognise. A model's computational power is greater the wider the class of languages it recognises (p. 20). The source sets out a ladder of models.

- **Deterministic finite automaton (DFA):** it recognises exactly the regular languages, the same class that regular expressions and automaton grammars describe (p. 20). A Mealy machine adds an output that depends on the state and the input, and a Moore machine adds one that depends on the state only (p. 20; [[moore-and-mealy-machines]]). Neither changes what can be recognised.
- **Non-determinism and ε-transitions** add no power, so every NFA has an equivalent DFA: «недетерминизм не увеличивает вычислительной мощности модели» (p. 21). See [[spontaneous-and-guarded-transitions]].
- **Pushdown automaton:** a stack added to the finite control is enough for context-free languages, which hold most constructs of modern programming languages (p. 23). The deterministic variant without spontaneous transitions covers the languages that an unambiguous grammar describes, which the source calls the class most in demand in practice (p. 23).
- **Turing machine:** a finite control with tape memory, the most powerful of these models (pp. 24-25).

Two limits of the finite model are stated outright. Automaton mappings work without prediction: «перерабатывая цепочку слева направо, они «не заглядывают вперед»» (p. 21). The source's example is that reversing a string is not an automaton mapping (p. 21). And only infinite extra memory raises power; see [[finite-memory-folds-into-states]].

## Sign in code

The transfer to code here is this wiki's own. The symptom is a state machine, a set of flags or a regular expression asked to track structure of unbounded depth: matching brackets, nested comments or blocks, or tags that must close in reverse order. A finite control can count only up to a fixed depth. The sign is depth-limited states (`IN_ONE`, `IN_TWO`, ...), or flags standing for depth. A counter or a stack is the repair, not the sign: it is unbounded memory, which places the code outside the finite model whether or not anyone says so.

## Repair

This repair is the wiki's reading of the ladder above. Keep the finite control for what is regular, and add an explicit stack for the nesting, which turns the component into a pushdown automaton. The source also notes that a pushdown automaton can accept either by final state or by an empty stack, the two are equivalent, and an implementation may use whichever is more convenient (p. 24). For a full language, this wiki's advice is a parser of the matching class rather than a growing state machine.

## Limits

- If the input format bounds the depth (at most two levels by specification), a finite machine is correct and simpler than a stack. This limit is this wiki's own.
- A single integer counter is enough for one kind of bracket. This wiki holds that whether that counts as "a stack" does not matter in practice; what matters is admitting that the memory is unbounded instead of modelling it as states.

## Example

```
// before: nesting encoded as states, breaks at depth 3
state = OUTSIDE | IN_ONE | IN_TWO
on '(' : state = next_deeper(state)   // no state beyond IN_TWO
on ')' : state = next_shallower(state)

// after: finite control for the regular part, a stack for the nesting
stack = []
on open(kind):  stack.push(kind)
on close(kind): if stack.empty or stack.pop() != kind: error
on end:         if not stack.empty: error
```

Related: [[finite-state-machine]], [[control-and-computational-states]].

## Source

Polikarpova, Shalyto, *Automata-Based Programming*, pp. 19-25 ([[automata-based-programming]]): recognition and computational power, DFA and regular languages, Mealy and Moore machines, NFA and ε-transition equivalence, no lookahead and the reversal example, pushdown automata and context-free languages, the two equivalent acceptance conditions, and the Turing machine. The sign in code, the repair as applied to code, the limits and the pseudocode are this wiki's own.
