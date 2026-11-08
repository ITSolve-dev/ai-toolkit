---
title: Event-driven vs polled state machine
category: types-and-state
summary: "A state machine whose guards test one boolean 'is pressed' flag per button or signal, set and cleared around it, with the same flag guard repeated across states: choose events for discrete happenings and polled inputs for levels."
tags: [decision-rule, state-machine, automata-based-programming, events]
paradigm: any
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

A state machine either reacts to **events**, taking one step per event (the book calls this a *passive* automated object), or runs **continuously, step after step**, and reads boolean input variables on each step (an *active* one) (p. 50; see [[automated-object]]).

## Rule

Where the stimuli are discrete happenings (a button press, a timer tick), model them as events rather than as boolean inputs. This criterion is this wiki's generalisation of one example: in the alarm-clock example the authors chose events because three boolean "button pressed" inputs «усложнило бы автомат». Only two real inputs remained, both comparing the current time with the alarm time (p. 45). The choice also changes the number of states: the counting trigger needs four states when it polls a boolean button and two with separate press and release events (p. 29).

Where the machine polls a continuous process (logical control of a valve), use input variables. The book's valve graph gives every state a self-loop: the machine stays in the state until some outgoing condition holds, and «Условие на петле строится как отрицание дизъюнкции условий на всех остальных исходящих дугах» (pp. 50-51). Later in the same chapter the book replaces that hand-written negation with an «иначе» (else) arc, because the negation is bulky and must be rewritten whenever an arc is added (p. 70; [[transition-conditions-consistent-and-complete]]).

## Sign in code

This wiki's own reading:
- In an event-driven setting, the guards of the transitions test several `isXPressed` flags that are set and cleared around the machine, and the same guard repeats in many states.

This wiki assigns a related shape elsewhere: a missing or hand-negated stay case, or exit guards that overlap, belong to [[transition-conditions-consistent-and-complete]]; input flags here are distinct from the mode flags of [[replace-flags-with-explicit-states]], which remember what the entity is doing rather than what just happened. An identical transition (condition, action, target) in several states is [[state-grouping-for-shared-transitions]]; a guard on an 'is pressed' flag set and cleared around the machine is [[event-driven-vs-polled-state-machine]].

## When not to apply

- The domain fixes the choice: the book follows the logical-control tradition and uses no events and Moore machines there (p. 48).
- The stimulus is a level that must be checked on every step, not a discrete happening. Then it is an input variable.
- In a purely event-driven machine there is nothing to poll, so self-loops are not needed.

## Repair

Turn each discrete stimulus into an event the machine dispatches on, and keep as input variables only the genuine conditions (comparisons, sensor levels). How a polled machine's stay case is written is [[transition-conditions-consistent-and-complete]].

## Before and after

```
// before: buttons as polled flags
step():
  if state == OFF and btnA and not btnH and not btnM: state = SETTING
  if state == OFF and btnH and not btnA: incHours()
  ...
```

```
// after: buttons as events
handle(event):
  switch state:
    OFF:
      on A -> state = SETTING
      on H -> incHours()
      on M -> incMinutes()
      on T -> tickMinute()
```

In object-oriented code the events become the public methods of the class instead of a `handle(event)` dispatcher ([[automated-class]]).

## Source

Polikarpova, Shalyto, *Automata-Based Programming*, ch. 1, p. 29, and ch. 2, pp. 45, 48, 50-51, 70 ([[automata-based-programming]]). The quotations are verbatim. The rule's criterion (discrete happenings as events, levels as input variables), the signs, the assignment of neighbouring shapes, the limits beyond the logical-control tradition, and the pseudocode are this wiki's own.
