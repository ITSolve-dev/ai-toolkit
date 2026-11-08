---
title: Logging execution in terms of states
category: debugging
summary: "Logic with complex behaviour debugged from print statements scattered through branch and action bodies, when a trace of the state machine's own steps (state before, event, inputs the guards read, transition taken, outputs, state after, nested machines indented) could be written at the one transition function."
tags: [method, state-machine, logging, tracing]
paradigm: any
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

When control logic is written as explicit state machines, the run can be logged in the machines' own terms rather than in lines of code. Polikarpova and Shalyto say that most libraries and tools for automata-based programming can keep such a protocol of execution (p. 138). Static checks on the same graph are [[transition-conditions-consistent-and-complete]]; the general rules for trace output are [[trace-statements]].

## What the protocol records

The source lists what the protocol holds (p. 138):

- the sequence of states the machine passed through;
- the events it processed;
- the values of input and output variables;
- the nesting and calling relations between machines, shown «при помощи специального форматирования (например, отступов)».

The authors add that UniMod allows step-by-step debugging in terms of automata, and claim that with such high-level means «гораздо проще находить ошибки в логике сложного поведения, чем с использованием традиционных методов» (p. 138).

## Procedure

This procedure is this wiki's own reading of the source's list:

1. Log in one place, the dispatch or transition function, not in the bodies of actions. Each step writes one line: machine, state before, event, the inputs the guards read, the transition taken, the outputs fired, and the state after.
2. Indent a nested or called machine's lines under the line of the step that called it ([[interacting-state-machines]]).
3. Reproduce the failure and read the trace for the first step whose transition differs from the transition graph. A wrong guard value points to the inputs, that is to the control object ([[separate-control-object-from-state-logic]]). A right guard value but the wrong transition points to the machine.

## Limits

This limit is this wiki's own. The method needs the state to be explicit and transitions to go through one function. If state is spread across flags, the trace cannot be written at one point; that shape is a sign for [[replace-flags-with-explicit-states]] first, and a state assigned outside the step function is [[state-machine-as-switch-on-state]].

Where the state-machine library or tool already keeps such a protocol (the book says most do, p. 138), read its trace instead of writing one. A polled machine stepped every tick writes a line per tick, so its trace needs a switch or a filter on steps that change state. These two limits are this wiki's own.

## Source

Polikarpova, Shalyto, *Automata-Based Programming*, ch. 4.2, p. 138 ([[automata-based-programming]]): the contents of the protocol and the claim that debugging is easier. The three-step procedure and the limits are this wiki's own.
