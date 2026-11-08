---
title: Split behaviour between the state machine and the operations it calls
category: types-and-state
summary: "A state machine whose states stand for steps of a computation (SENDING_BYTE_0, SENDING_BYTE_1 ..., one state per digit or index) has primitive operations too low; an operation it calls that itself re-decides control from remembered flags has them too high: move the computation down into a command, or the remembered mode up into a state."
tags: [decision-rule, state-machine, abstraction-level, complexity, automata-based-programming]
paradigm: any
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

Automata-based programming splits an entity's behaviour into **logic**, meaning the control automaton with its states and transitions, and **semantics**, meaning the queries and commands of the controlled object (see [[automated-object]]). Polikarpova and Shalyto call the choice of how primitive those operations are «наиболее творческий и нетривиальный шаг в автоматном подходе» (p. 40). That choice decides where the line between control states and computational states falls ([[control-and-computational-states]]).

## Rule

Pick the level of the primitive operations (queries and commands) so that neither side gets overloaded. The authors name two failure directions (p. 40):

- **Operations too primitive.** The automaton grows and gets more complicated, and the logic fills with detail that the controlled object would handle better. The Turing machine is the extreme case of this «злоупотребления логикой». Its automaton has to compute as well as control: a Turing machine that multiplies two numbers already needs 12 states (p. 39).
- **Operations too abstract.** The queries and commands become hard to implement, with «перегруженности флагами и условными конструкциями» (p. 40). The degenerate case of this «злоупотребления семантикой» is the traditional, non-automaton style, in which all behaviour is treated as simple.

The level is not fixed. It depends on the task (p. 40). Multiplying two numbers can be complex behaviour if the point is to emulate an abacus. Building a balanced search tree can be one elementary operation if a library provides it.

## Sign in code

This wiki's reading of the two directions as shapes a reader can point at:

- **Logic overloaded.** The states or transitions of a state machine stand for steps of a computation, such as a loop counter, a position in a buffer or a digit being carried, rather than for modes the entity is in. Another sign is several states that differ only in which piece of data is being processed.
- **Semantics overloaded.** A method called by the state machine branches on boolean fields or mode fields that remember what happened before, and decides from them what to do next. That is control logic hidden in an operation.

This wiki assigns the second direction as follows. Flags held as fields of one entity and tested in combination by several of its own input handlers to choose a reaction are [[replace-flags-with-explicit-states]]. This page owns the shape only where an explicit state machine exists and the flag-driven branching sits inside an operation it calls, and its "logic overloaded" shape: states that count. Flags beside a state variable tested in the machine's own handlers are [[replace-flags-with-explicit-states]]; flags tested inside an operation the machine calls are [[logic-vs-semantics-split]].

## When not to apply

- If the behaviour is simple, meaning the output does not depend on history (the book's combinational case, p. 27), there is no logic to separate, and an explicit automaton adds nothing.
- The balance is set per task. A state machine that steps through data is right when stepping through data is what the program models (the abacus example, p. 40). This wiki treats the sign as evidence only where the steps are incidental to the modes.
- Within this source's frame, decomposition into functions or objects is not a substitute. The authors argue that decomposition «лишь распределяет» complex logic across components without making it explicit (pp. 40-41). This wiki does not read that as a rule against decomposing. It is a claim that splitting code up does not by itself give the reader a picture of the behaviour.

## Repair

- Logic overloaded: move the computation into a command or query of the controlled object, so that the transitions reference it by name. The automaton keeps only the states that change what the entity responds to.
- Semantics overloaded: lift the remembered mode out of the flags into an explicit control state. Let the operations become plain queries and commands that do not decide control.

## Before and after

Logic overloaded: the automaton counts.

```
state machine Sender:
  SENDING_BYTE_0 -> on tick: write(buf[0]); go SENDING_BYTE_1
  SENDING_BYTE_1 -> on tick: write(buf[1]); go SENDING_BYTE_2
  ...
  SENDING_BYTE_N -> on tick: write(buf[n]); go IDLE
```

```
state machine Sender:
  IDLE    -> on send(msg): channel.start(msg); go SENDING
  SENDING -> on tick: channel.writeNext()
             if channel.done(): go IDLE
```

Semantics overloaded: an operation the machine calls re-decides control from flags.

```
state machine Player:
  ACTIVE -> on button: controls.press()

controls.press():
  if not started and not paused: start(); started = true
  else if started and not paused: pause(); paused = true
  else if paused: resume(); paused = false
```

```
state machine Player:
  IDLE    -> on button: controls.start();  go RUNNING
  RUNNING -> on button: controls.pause();  go PAUSED
  PAUSED  -> on button: controls.resume(); go RUNNING
```

## Source

Polikarpova, Shalyto, *Automata-Based Programming*, [[automata-based-programming]]: the logic/semantics split, the two kinds of abuse, and the task-dependent level (p. 40); the 12-state multiplying Turing machine (p. 39); the combinational case (p. 27); the remark that decomposition distributes logic without making it explicit (pp. 40-41). The signs, the assignment against [[replace-flags-with-explicit-states]], the limits beyond the combinational case, and both pseudocode pairs are this wiki's own. The book gives the trade-off only as a principle and a diagram (fig. 1.24).
