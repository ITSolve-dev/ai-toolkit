---
title: Separate the control object from the state logic
category: types-and-state
summary: "A state machine's step function or state classes compute over the controlled data inline (time arithmetic, compound comparisons of several fields, device fiddling) instead of calling named queries and commands, the same compound guard repeated across states, or control-object members named after automaton ids such as x1 or z5."
tags: [rule, state-machine, cohesion, queries-and-commands, naming, reuse]
paradigm: any
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

In automata-based programming an entity with complex behaviour splits into a **control automaton**, which holds the control state and decides what to do next, and a **controlled object** (control object), which offers queries (input conditions, named x in the book) and commands (actions, named z) and holds the rest of the data. The model is [[automated-object]]; this page is the rule that makes code keep the split, with its sign.

The book keeps the split in both its procedural and its object-oriented code. In the procedural alarm clock the queries and commands are separate functions, outside the automaton, «в целях повышения модульности» (listing 2.7, p. 90), and three later implementations that feed events to the automaton differently reuse the same controlled object unchanged (p. 92). In the object-oriented version `Clock_Control_Object` owns current time, alarm time and the bell and exposes operations such as `increase_hours`, `bell_on`, `minute_less` and `times_equal` (listing 3.1, p. 118), while the automated class holds only the state and a reference to it. When that implementation moves from a switch to the State pattern, the book notes «Реализация объекта управления остается прежней» (p. 121). The payoff once logic is generated from the graph: the programmer «останется только реализовать объект управления – его запросы, команды и множество вычислительных состояний» (p. 94).

The same chapter supplies the naming half. Criticising the UniMod tool, the authors object that its control objects' members carry the automaton's short ids: «имена компонентов объектов управления совпадают с краткими идентификаторами входных и выходных переменных автомата» (p. 132), which is odd if the class was written separately and may be reused in another system. They also object that an automaton whose clients are fixed in advance to given event sources cannot be reused in another context (p. 132).

## Rule

Keep the state-dependent decision (which action, which next state) in the state machine, and the data plus the elementary queries and commands on it in a control object. The step function, or each state class, contains only the state selection, guards that call queries, calls of commands, and state assignments. Name the control object's members after what they do in its own domain, not after the machine that happens to drive it.

## Sign in code

This wiki's own reading:

- A case of the state selection, or a method of a state class, holds multi-line arithmetic or data updates (time-carry logic, compound comparisons of several fields, toggling a device) written inline.
- The same compound condition, or the same low-level fragment, repeated in the branches of several states instead of being one named query or command.
- Members of a data or device class named `x1`, `x2`, `z5`, `e3`, or after an automaton's labels, rather than `firstNameNotEmpty`, `enableSaveButton`.
- A state machine class that takes one concrete event-source class in its constructor and is called only from it, where event methods any caller can call would do.

This wiki assigns the neighbouring cases as follows. In a state machine's step function, a case arm that computes over the controlled data inline is [[separate-control-object-from-state-logic]]; a long arm elsewhere is [[keep-case-arms-short]]. A state machine whose primitive operations are pitched too low (one state per byte or digit) is [[logic-vs-semantics-split]]. An operation of the controlled object that itself reads the mode is the 'semantics overloaded' shape of [[logic-vs-semantics-split]].

## When not to apply

- An action that is a single assignment to an output, as in the book's logic-control examples (p. 82), needs no function of its own; the book assigns such outputs inline.
- A machine whose actions are one line each on one or two fields: a separate control class only adds a hop. The book itself does not split out a control object for the counting trigger, using a button and a lamp directly (p. 125).
- The book's own model lets the queries and commands be implemented fully or partly inside the automated class (p. 132). Then the separation is a split into private methods inside one class, not a new class, and a missing separate class is not a sign.
- Short ids like `x1` and `z5` on a transition diagram or in a generated table are notation for the diagram; the naming part of the rule concerns names in hand-written classes.

## Repair

1. List every condition the machine tests and every effect it performs; each becomes a query or a command of the control object, named for what it tests or does.
2. Move the fields those operations touch into the control object.
3. Replace inline code in switch cases or state classes with calls to those operations, leaving `switch state`, `if query()`, `command()`, `state = ...`.
4. Rename members coded after automaton labels to names from the control object's own vocabulary; keep the label map, if needed, in a comment or on the diagram.
5. Give the machine its events as its own entry points, so any caller, not one fixed source, can drive it ([[passing-events-to-a-state-machine]], [[automated-class]]).

## Before and after

```
// before: the clock's arithmetic and comparisons inside the machine
function onTimer():
    switch state:
        case ALARM_ON:
            minutes = (minutes + 1) mod 60
            if minutes == 0: hours = (hours + 1) mod 24
            if (minutes == alarmMinutes - 1 and hours == alarmHours)
               or (alarmMinutes == 0 and minutes == 59 and hours == alarmHours - 1):
                bell.z1()
        case ALARM_OFF:
            minutes = (minutes + 1) mod 60
            if minutes == 0: hours = (hours + 1) mod 24
        ...
```

```
// after: the machine names queries and commands; the control object implements them
function onTimer():
    switch state:
        case ALARM_ON:
            if clock.minuteBeforeAlarm(): clock.ringBell()
            clock.tick()
        case ALARM_OFF:
            clock.tick()
        ...

class Clock:
    tick():              minutes = (minutes + 1) mod 60
                         if minutes == 0: hours = (hours + 1) mod 24
    minuteBeforeAlarm(): return currentTime().plusMinute() == alarmTime()
    ringBell():          bell.on()
```

The after keeps only decisions in the machine; time arithmetic lives once, in `Clock`, under names of its own.

## Trade-offs

The control object can be reused and tested without the machine, and the machine can be reimplemented (event passing changed, or switch moved to the State pattern, see [[switch-on-state-vs-state-pattern]]) without touching it. The cost is one more class or set of functions, and an interface that has to be kept in step with what the machine needs.

## Source

Polikarpova, Shalyto, *Automata-Based Programming* ([[automata-based-programming]]): outputs assigned inline in logic control, p. 82; queries and commands as separate functions for modularity, p. 90; the controlled object reused across three implementations, p. 92; the programmer implements only the controlled object once logic is generated, p. 94; the control object as a class, p. 118 (listing 3.1); unchanged across implementations, p. 121; the trigger without a separate control object, p. 125; the criticism of naming members after automaton ids and of fixed event sources, and queries and commands possibly inside the automated class, p. 132. The signs in code, the assignment of neighbouring cases, the second limit as a size judgement, the repair steps and the pseudocode are this wiki's own; the time arithmetic and alarm comparison in the before are adapted from Listing 1.1 (p. 10).
