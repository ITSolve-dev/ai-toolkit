---
title: Switch on state vs the State pattern
category: types-and-state
summary: "Every event method of a class opens with a switch over the same control-state field, one case per state, so one state's behaviour is scattered across methods; or a class per state, per event and per transition for a machine never changed at run time: choose between the switch, the State pattern, and tables."
tags: [decision-rule, state-machine, state-pattern, polymorphism]
paradigm: oop
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-07
---

An object whose behaviour depends on a control state (an [[automated-class]]) can be written in several ways. Polikarpova and Shalyto set the options on one axis (p. 117). At one end the automaton function is wrapped in a class and states and events are integer constants, with «высоким быстродействием, но крайне низкой гибкостью» (p. 117). At the other end is the FSM Framework pattern, with one class per element of the model: a state holds a table from events to transitions, and a transition holds its target state and its action. That end is the most flexible, but the program is bulky and costs time and memory (p. 117). Mixtures of constants, subroutines and classes lie between.

The authors narrow the choice to two templates for an automated class, whose public methods are the events (p. 117). Because events are the methods, how to represent them is no longer a question. They also hold that «для большинства задач не требуется обеспечивать возможность динамической конфигурации автомата» (p. 117), so they prefer a static description of transitions and actions over tables ([[state-machine-table-or-switch]]). The two templates are:

1. **Switch per event method** (listing 3.2, pp. 118-120): a private `state` field of an enum type; each event method is a `switch (state)` whose cases call the control object and assign the next state. The authors present it as the way to turn a procedural implementation into an object-oriented one, «сделав минимум изменений» (p. 117).
2. **The State pattern** (listing 3.3, pp. 120-123): an abstract state class whose methods are the same events, and one subclass per control state. The owning class delegates each event to the current state object and then replaces it with the state that object chose. Variation by state comes from subtype polymorphism. The authors note that the language's own dispatch table then stands in for the transition table, which is much more convenient for the developer than building a table by hand (p. 117).

## Rule

Keep the switch while the machine is small and stays closed; move to the State pattern when the states' behaviour grows. Use tables (FSM Framework style) only when the machine must be configured at run time. The book states the two ends of the axis and the preference for static description; the threshold between switch and State pattern is this wiki's own reading, since the book shows both templates without saying when to change from one to the other.

This wiki assigns the neighbouring cases as follows. A switch over a control state that the object's own methods reassign is [[switch-on-state-vs-state-pattern]]; a switch over a type code fixed for the object's life is [[polymorphism-or-type-switch]]. A branch whose key names what kind of thing the switched-on object is (a shape, a square, a transaction) is [[polymorphism-or-type-switch]]; a branch whose key names a policy the object applies to compute one result, with that policy's parameters stored as fields of the object, is [[strategy-for-varying-algorithms]]. Whether the transitions are data or code at all is [[state-machine-table-or-switch]]; the shape of each case (state first, one guarded branch per arc) is [[state-machine-as-switch-on-state]].

## Sign in code

This wiki's own reading:

- In a machine of more than three states, or where a switch no longer fits on a screen, several public methods of one class each consist of a `switch` (or `if/else` chain) over the same state field, with one branch per state, and adding one state means editing every such method.
- Branches of different methods for the same state repeat the same call (in listing 3.2 the cases for "alarm off" and "alarm on" of the hours button both call `increase_hours`).
- The opposite sign, for the other end: a class per state, per event and per transition, plus an event-to-transition map, in a machine that is never changed while running.

## When not to apply

- A machine with two or three states and a few events, where every switch fits on a screen: the State pattern adds a class hierarchy and an object swap on every event for little gain. This limit is this wiki's own; the book's own State examples (adder, counting trigger, pp. 123-128) are offered for understanding, and the authors say they have little practical value.
- Where the machine has to be verified as a whole: the book says programs built with the approach of its chapter 3 are substantially harder to verify than those whose logic is centralised (p. 133); this wiki reads the State pattern, which spreads the transition function further, as the stronger case. A single switch or table that a checker or a reviewer reads in one place is the better choice there.
- Where transitions are configured at run time (loaded, edited by users): neither static template fits, and a table is required.
- Where a generator builds the code from diagrams: the authors call generation the best approach for complex behaviour where a tool exists (p. 116), and the hand templates are then moot.

## Repair

To move from switch to State pattern:

1. Declare an abstract state type with one method per event of the owning class.
2. For each enum value, create a subclass, and move into each method the body of that state's case from the corresponding switch.
3. In each branch, replace `state = X` with returning, or choosing, the next state object.
4. In the owning class, make each event method delegate to the current state and then install the chosen next state (one private update step, as in listing 3.3).
5. Give the states the control object they act on, not the owning class, so states do not reach back into their owner ([[separate-control-object-from-state-logic]]).

The State pattern implements a Mealy machine, where actions sit on transitions ([[moore-and-mealy-machines]]). A Moore machine, with actions in states, must first be rewritten «переместив действия из каждого состояния на все переходы, которые ведут в это состояние» (p. 126). This wiki reads the cost of skipping that step as a state action left unexecuted on entry, or duplicated in an entry hook the pattern does not have.

## Before and after

```
// before: one switch over the same state in every event method
class AlarmClock
  state: enum { OFF, SETTING, ON }

  hourButton():
    switch state
      OFF:     clock.increaseHours()
      SETTING: clock.increaseAlarmHours()
      ON:      clock.increaseHours()

  alarmButton():
    switch state
      OFF:     state = SETTING
      SETTING: state = ON
      ON:      clock.bellOff(); state = OFF

  tick():
    switch state
      OFF, SETTING: clock.increaseTime()
      ON: if clock.minuteBeforeAlarm() then clock.bellOn()
          else if clock.atAlarm() then clock.bellOff()
          clock.increaseTime()
```

```
// after: each state's behaviour in one class
class AlarmClock
  state: ClockState
  hourButton():  state = state.hourButton()
  alarmButton(): state = state.alarmButton()
  tick():        state = state.tick()

abstract class ClockState(clock)
  hourButton():  clock.increaseHours(); return this   // shared default
  alarmButton(): ClockState
  tick():        clock.increaseTime(); return this    // shared default

class AlarmOff extends ClockState
  alarmButton(): return AlarmSetting(clock)

class AlarmSetting extends ClockState
  hourButton():  clock.increaseAlarmHours(); return this
  alarmButton(): return AlarmOn(clock)

class AlarmOn extends ClockState
  alarmButton(): clock.bellOff(); return AlarmOff(clock)
  tick():
    if clock.minuteBeforeAlarm() then clock.bellOn()
    else if clock.atAlarm() then clock.bellOff()
    return super.tick()
```

The after has no switch over a state field; each state's behaviour sits in one class, and a call shared by several states is written once, as the base class's default. Returning the next state (and `this` for a self-loop) instead of the book's mutable next-state field, with a new state object allocated even on self-loops, is this wiki's simplification.

## Trade-offs

- The switch keeps the whole machine in one class and readable as a table, at the cost of scattering each state across methods.
- The State pattern gathers each state, at the cost of scattering the transition function across classes: no single place shows the whole graph. The book names a verification cost for its chapter-3 approach as a whole (p. 133); applying it to the State pattern is this wiki's reading.
- Tables give run-time flexibility, at the cost of bulk and speed (p. 117).

## Source

Polikarpova, Shalyto, *Automata-Based Programming* ([[automata-based-programming]]): generation as the best option, p. 116; the axis from constants to FSM Framework and the preference for static description, p. 117; the switch template, pp. 117-120; the State pattern template, pp. 120-123; the State examples, pp. 123-128; Moore to Mealy for the State pattern, p. 126; the verification cost of the chapter-3 approach against centralised logic, p. 133. The threshold in `## Rule`, the assignment of neighbouring cases, the signs, the first limit, the repair steps, the reading of the Moore-to-Mealy cost, the application of the p. 133 cost to the State pattern and the pseudocode are this wiki's own. The listings in the book contain typos (an undeclared variable, a field private in the base but used in subclasses); the pair here does not reproduce them.
