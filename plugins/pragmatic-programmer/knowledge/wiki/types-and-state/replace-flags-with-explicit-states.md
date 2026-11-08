---
title: Replace behaviour flags with one explicit control-state variable
category: types-and-state
summary: "Two or more boolean or small-range fields of one entity, tested in combination by several of its own input handlers to pick a different reaction to the same input (alarm_on and setting_alarm, lampOn and wasPressed): an implicit state machine; name the modes, hold them in one state variable, give each handler one case per state."
tags: [rule, state-machine, flags, branching, state-encoding, complex-behavior]
paradigm: any
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

An entity has **complex behaviour** when the same input can produce different reactions depending on what happened before (see [[complex-behavior]]). Polikarpova and Shalyto describe how such an entity usually looks when it is coded without a model: the history is held in boolean flags, and each input handler works out which reaction applies from tangled conditions over those flags. Their repair is to name the **control states** the flags encode, keep them in one variable, and describe the entity's behaviour in each state separately (see [[control-and-computational-states]], [[automated-object]]).

## Rule

The book names the sign directly: in the traditional implementation of such an entity, «используются логические переменные, называемые флагами, и многочисленные запутанные конструкции ветвления, условиями в которых выступают различные комбинации значений флагов» (p. 9). Such a description of the logic, it says, is «плохо структурирован, труден для понимания и модификации, подвержен ошибкам» (p. 9), and even its alarm-clock example comes out cumbersome and unclear (Listing 1.1, pp. 9-10).

The prescription, drawn from the Turing-machine analogy, is to «явно выделить управляющие состояния (идентифицировать их, дать им имена) и описать поведение сущности в каждом из них» (p. 16). For the alarm clock the book names three: «Будильник выключен», «Установка времени будильника» and «Будильник включен». In each of them the reaction to any button is unambiguous and specific to that state (p. 16).

**How to hold the state: one multi-valued variable.** The book compares three ways to encode an automaton's states (pp. 28-31). *Forced* encoding uses the output values as the state code. *Forced-free* encoding adds extra bits to tell states apart. *Free* encoding uses one multi-valued variable whose codes are chosen arbitrarily: integers, characters or mnemonic strings. The authors recommend free encoding as the default for programming (pp. 30-31). Their reasons:

- **Forced encoding breaks when states outnumber outputs.** A counting trigger toggles a lamp each time a button is pressed. It needs four control states, but the lamp has only two values, so a graph coded by the lamp's value has pairs of vertices that cannot be told apart and cannot be implemented (p. 29).
- **With free encoding, outputs and internal variables are independent,** and states can carry mnemonic names, for example «Кнопка нажата, лампа включена» (p. 30).
- **Observability.** One variable holding the state number, whatever the number of states, makes the automaton's work observable (p. 32): the current mode can be read, logged and checked at any moment.
- **Interaction.** Other automata can read the state variable after each step (p. 32). How they should read it is [[state-machines-communicate-through-an-explicit-interface]].

The cost, which the book states: free encoding needs an output converter, a separate function from state to outputs (p. 30). With forced encoding the state is the output.

## Sign in code

- Two or more boolean fields (or small mode enums kept in parallel) of one entity that are not data shown to the user. Their only job is to choose between reactions.
- Several input handlers (`on_x`, `on_y`, `tick`) each open with an `if` over the same flags, so one mode decision is repeated in every handler.
- Nested `if`s over flag *combinations*, in which a handler assigns two or more flags together to move to the next mode (in Listing 1.1, the A-button handler sets the alarm-on flag and the alarm-setting flag together).
- A mode inferred from output-like fields (running read off whether `motorOn` is true) while the code also needs to tell apart modes in which those fields look the same. This is the book's forced-encoding failure, as this wiki reads it in code.
- This wiki adds: a combination of flag values that no code path can produce, yet the type allows (in Listing 1.1, alarm off while in alarm-setting mode), and no single place where a reader or a log can see which mode the entity is in.

This wiki assigns the neighbouring cases as follows. Flags held as fields of one entity and tested in combination by several of its own input handlers to choose a reaction are [[replace-flags-with-explicit-states]]; flags that one loop over a sequence of events sets and tests to track its place in that sequence are [[finite-state-machine]]; a status read by functions outside its owner is [[status-variable-as-enumeration]]. An existing state variable with extra flags beside it that change what a state does is this page too: the reasoning is on [[finite-memory-folds-into-states]]. Flags beside a state variable tested in the machine's own handlers are [[replace-flags-with-explicit-states]]; flags tested inside an operation the machine calls are [[logic-vs-semantics-split]]. Code that already holds the mode in one state variable but does not mirror the transition graph is [[state-machine-as-switch-on-state]]. Integer codes for a closed set of values are [[enum-instead-of-codes-and-flags]]. When one fragment shows both flags standing for history and a state machine reached through a generic dispatcher or a global state, this page decides whether there is a state machine at all, and [[automated-class]] decides how it is exposed.

## When not to apply

- **Simple behaviour.** The reaction to each input depends only on that input (the clock with only H and M buttons, p. 8). There is no history to encode, and the book's own scoping rule applies: «используйте автоматный подход при создании только тех компонентов системы, которые являются сущностями со сложным поведением» (p. 11), so as «не перегружать спецификации и код описанием логики там, где в этом нет необходимости» (p. 11).
- **The variable is computational state, not control state.** Counters, accumulated values, positions and times being compared have a huge or unbounded range of values, most of which mean nothing on their own, and they hold the *results* of actions rather than selecting them (Table 1.1, p. 16). Turning them into named states is the misuse that [[control-and-computational-states]] warns about. In the alarm clock, the hours, minutes and alarm time stay ordinary fields.
- **Independent flags.** This wiki's own limit: if every combination is valid and none of them selects behaviour on its own, the flags are data, not a control state, and one variable would multiply the states. Where several independent parts each have modes, see [[decompose-state-machine-by-modes-or-by-controlled-objects]].
- **States map one-to-one onto outputs.** If the number of control states does not exceed the number of distinct outputs and every state maps onto one output value, forced encoding with no output converter is valid (p. 28), and the extra function adds nothing. This wiki reads the counting trigger as the case where that condition fails.
- **Event-driven input.** With separate press and release events the counting trigger needs only two states (p. 29). This wiki's reading: check the input model before counting states ([[event-driven-vs-polled-state-machine]]).
- This wiki's own reading: a single flag tested in a single place is a plain conditional, not a hidden machine. The sign needs the same mode decision to recur across handlers, or flags to be tested in combination. A flag beside an existing state variable that two or more handlers test together with the state counts as tested in combination ([[finite-memory-folds-into-states]]).

## Repair

1. List the flag combinations that are actually reachable, and give each a name that says what the entity does in it (the book stresses that state names describe behaviour in that state, p. 14).
2. Replace the flags with one state variable of an enumerated type holding exactly those names.
3. In each handler, switch on the state: one branch per state that reacts to this input, with the transition written as one assignment of the new state ([[state-machine-as-switch-on-state]]).
4. Derive any output fields from the state in one output function, rather than storing them alongside it (the output converter, p. 30).
5. Move the actions themselves (incrementing a counter, ringing a bell) into operations that always do the same thing when called, so the switch holds only the choice of action ([[automated-object]]). Leave computational data (times, counts) as fields, and expose the conditions over it as named predicates.

## Before and after

```
class AlarmClock
  alarm_on: bool
  setting_alarm: bool
  hours, minutes, alarm_hours, alarm_minutes: int

  on_h()
    if setting_alarm: alarm_hours = (alarm_hours + 1) mod 24
    else: hours = (hours + 1) mod 24

  on_a()
    if alarm_on
      if setting_alarm: setting_alarm = false
      else: bell_off(); alarm_on = false
    else
      alarm_on = true
      setting_alarm = true

  on_tick()
    if alarm_on and not setting_alarm
      if one_minute_before_alarm(): bell_on()
      else if at_alarm(): bell_off()
    advance_time()
```

```
enum Mode { ALARM_OFF, SETTING_ALARM, ALARM_ON }

class AlarmClock
  mode: Mode = ALARM_OFF
  time: ClockFace          -- controlled object: simple behaviour only

  on_h()
    switch mode
      SETTING_ALARM: time.increment_alarm_hours()
      ALARM_OFF, ALARM_ON: time.increment_hours()

  on_a()
    switch mode
      ALARM_OFF:     mode = SETTING_ALARM
      SETTING_ALARM: mode = ALARM_ON
      ALARM_ON:      time.bell_off(); mode = ALARM_OFF

  on_tick()
    switch mode
      ALARM_ON:
        if time.one_minute_before_alarm(): time.bell_on()
        else if time.at_alarm(): time.bell_off()
    time.advance()
```

The after-version has no flags and no combination conditions, and the unreachable combination is gone. The time comparisons stay, because they are tests on computational state; they now live in the controlled object as named predicates, so this page's limit holds for them.

## Source

- Polikarpova, Shalyto, *Automata-Based Programming*, ch. 1 ([[automata-based-programming]]). Complex behaviour, pp. 7-8; the sign and Listing 1.1, pp. 9-10; the scoping rule, p. 11; the prescription with the three alarm-clock states, p. 16; state names describing behaviour, p. 14. Forced, forced-free and free encoding and the counting trigger, pp. 28-31; free encoding as the default and its output converter, pp. 30-31; observability and interaction through the state variable, p. 32.
- This wiki's own parts: the signs about output-like fields, unreachable flag combinations and the missing single view of the mode; the limits on independent flags, event-driven input and a single flag; the assignment of neighbouring cases; steps 1-5 of the repair as a procedure; the after block. The before block is adapted from Listing 1.1 (pp. 9-10). The book's own automaton version of the clock is given in later chapters and is not reproduced here.
