---
title: "How events reach a state machine: global variable, argument, or one function per event"
category: types-and-state
summary: "An event-driven state machine reads the current event from a global or shared variable that callers must set before calling the step function, or one event is decoded twice, once by the dispatcher choosing the machine and again inside the machine's step function."
tags: [decision-rule, state-machine, events, side-effects, function-arguments]
paradigm: any
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

An event-driven (passive) state machine runs one step when its environment calls it, so the design question is how that call tells the machine which event happened. Polikarpova and Shalyto list three options and give each its reason (pp. 87-88), illustrating all three on an alarm clock (listings 2.7-2.9, pp. 90-93). Whether to drive the machine by events at all is [[event-driven-vs-polled-state-machine]].

## Rule

1. **Event in a global variable**, or a bit vector if events are not exclusive. The step function keeps the shape it has for inputs (pp. 87-88). The source notes the cost: a programmer may forget to set the variable before calling the step (p. 88).
2. **Event as an argument of the step function**, for example `step(event)` for exclusive events or `step(eventSet)` for non-exclusive ones. This reflects that the machine *processes* an event, while it only *polls* inputs on its own initiative, and it «предотвращает программные ошибки, возможные при первом подходе: когда программист забывает установить переменную для хранения события перед вызовом такта автомата» (p. 88).
3. **One function per event**, each containing a selection on the state and guards over inputs (listing 2.6, p. 89). It suits only exclusive events, the most common model (p. 88). It matches how event-driven modules are usually written, as a set of handlers of related events, and it avoids decoding the event twice: the environment already decodes it to find which machine to send it to, and with the other options «дешифрация событий на каждом такте без всякой необходимости происходит два раза» (p. 88).

Resolution per setting. The book states the reasons; this selection among them is this wiki's:

- Events can co-occur: option 2 with a set argument (option 3 does not apply).
- Events are exclusive and the dispatcher already branches on the event: option 3.
- Events are exclusive and arrive through one generic entry point: option 2 with a single event argument.
- Option 1 only where the event really is shared state of the program. The book notes that, of the two places for such a global, the automaton's own module is the less likely, since events usually serve communication between modules (p. 87).

This wiki assigns the neighbouring cases as follows. How the event is handed to the machine is this page; boolean "is pressed" flags standing in for events are [[event-driven-vs-polled-state-machine]]. In procedural code, how an event reaches a step function is [[passing-events-to-a-state-machine]]; in object-oriented code, where each event is a public method, it is [[automated-class]]. Whether the transitions are held as a table or as a switch is [[state-machine-table-or-switch]]; the switches below show only how the event arrives.

## Sign in code

This wiki's own reading:

- Callers write `currentEvent = X` and then call `step()`; the step function reads `currentEvent` from outside its parameters.
- A dispatcher switches on the event to pick a target machine, then calls a generic `step(event)` that switches on the same event again.

## When not to apply

- Option 3 is wrong for non-exclusive events: the book says it suits only the exclusive model (p. 88). The reason, that two simultaneous events would run two steps instead of one, is this wiki's reading.
- With option 3 the code is no longer quite isomorphic to the state-first scheme of the algorithm: it branches on the event first, then the state, then the inputs (p. 88). Where a reviewer compares code to a state-first diagram, that cost is real; the book judges it justified in most event-driven systems.
- When the machine is generated from a graph by a tool that expects one template, the template decides; the book treats generation separately (p. 94).

## Repair

- From option 1 to option 2: add the event as a parameter of the step function, remove the global, and change each call site from "set, then call" to one call with the event.
- From option 2 to option 3 (exclusive events, dispatcher already decodes): split the step function into one handler per event, and in each keep only that event's guarded branches per state.

## Before and after

```
// before: global event, callers must remember to set it
currentEvent: Event

function step():
    switch state:
        case ALARM_OFF:
            if currentEvent == HOUR: incrementHours()
            else if currentEvent == ALARM: state = SETTING_ALARM
        ...

// caller
currentEvent = HOUR
step()
```

```
// after (option 2): the event is an argument
function step(event):
    switch state:
        case ALARM_OFF:
            if event == HOUR: incrementHours()
            else if event == ALARM: state = SETTING_ALARM
        ...

// caller
step(HOUR)
```

```
// after (option 3): one handler per exclusive event, no second decoding
function onHour():
    switch state:
        case ALARM_OFF:     incrementHours()
        case SETTING_ALARM: incrementAlarmHours()
        case ALARM_ON:      incrementHours()

function onAlarmButton():
    switch state:
        case ALARM_OFF:     state = SETTING_ALARM
        case SETTING_ALARM: state = ALARM_ON
        case ALARM_ON:      stopBell(); state = ALARM_OFF
```

## Source

Polikarpova, Shalyto, *Automata-Based Programming* ([[automata-based-programming]]): the three options of interaction, pp. 87-88; the template of one function per event, p. 89; the alarm-clock implementations, pp. 90-93; generation, p. 94. The per-setting selection, the reason option 3 fails for simultaneous events, the assignment of neighbouring cases, the signs in code, the repair steps and the pseudocode are this wiki's own.
