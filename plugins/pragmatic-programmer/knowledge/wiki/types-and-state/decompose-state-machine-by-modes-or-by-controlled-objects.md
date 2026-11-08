---
title: Decompose a state machine by modes or by controlled objects
category: types-and-state
summary: "One state enum whose values are products of several independent parts (V1_OPEN_V2_CLOSING, LOCKED_RUNNING_GRILL ...) or copies one part's states per part (V1_OPENING ... V5_OPENING), a state handler carrying a long block of its own sub-phase logic, several state machines identical up to names, or in object-oriented code automata reaching each other through a special nesting mechanism: split by controlled object into classes or instances, or by mode into sub-machines."
tags: [decision-rule, state-machine, automata-based-programming, decomposition]
paradigm: any
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

One automaton driving everything suits only very simple systems. As a system grows, both the controlled object and the automaton grow, and the automaton needs its own decomposition (p. 51). The book's procedure (pp. 55-56) runs as follows. Build a head automaton on the most abstract control states. If its outputs are only commands, stop. Otherwise each *abstract action* in it (for example "cook food without harming the user" in the "On" state of a microwave) is replaced by a call to one or more nested or called automata. Repeat until only commands and calls to automata already defined remain. The book holds that no decomposition algorithm fits every problem, but that two criteria usually give a sound structure (p. 56).

## Rule

- **By modes.** Use it when the behaviour has several qualitatively different modes. Give each complex mode, that is each abstract action, its own automaton, for example a cooking automaton with states "Microwave" and "Grill", each refined further (pp. 56-57).
- **By controlled objects.** Use it when several controlled objects are present. Give each object its own automaton or subtree (p. 57). According to the book it usually gives more modularity and extensibility than decomposition by modes. Decomposition by modes stays indispensable where there is one controlled object that cannot, at the current level, be seen as several: the microwave's top two levels concern the whole oven, not its screen or its door lock (p. 58, footnote 8).

The deciding payoff of decomposition by objects appears once the machines talk by events instead of state numbers. The two valve machines turn out to be identical up to the names of events and variables. If names only need to be unique inside each machine, they are fully identical: «они являются экземплярами одного и того же класса» (p. 62). One description then yields any number of instances, so moving from two valves to five adds no new machines (p. 63). The book adds that the head automaton coordinating per-object machines often matters little and can be dropped with small changes to the subordinates, which leaves machines running in parallel (p. 63).

**In object-oriented code: by objects only.** Chapter 3 narrows the choice. When the automaton inside an [[automated-class]] grows too large, the book splits it the way any class is split: «если автоматизированный класс слишком сложен, его необходимо разбить на несколько классов, обыкновенных или автоматизированных» (p. 104). Levels of abstraction come from the ordinary client relation: the interface of an automated class is like any other, so the class of a control object may itself be automated, and one automated class serves as the control object of another (p. 105). Nested and called automata, superstates and orthogonal regions are not used to manage size. Once object decomposition replaces decomposition into automata, the book says, a notation needs only states and transitions with conditions and actions, and grouping states stays a cosmetic device for diagrams (p. 110). The reasoning: nesting between automata «обладает специфической семантикой и не имеет аналогов среди межмодульных отношений в объектно-ориентированном мире» (p. 101). In the procedural form automata and control objects are different kinds of thing reached in different ways, which the book says makes the model more complicated; with classes every level is reached through a method call (p. 105).

The book answers two objections (pp. 104-105). A control object that is given and cannot be split (bought, or built in hardware) stays indivisible in the implementation and can still be modelled as composite: a ready-made microwave emulator with both "unlock door" and "start timer" is treated as a door lock plus a timer, one automaton each, mapped back onto it by adapters or by different methods of the one class. And where every state touches every part of the control object, which the book calls rare, the control object itself becomes an automated class one level down.

This wiki resolves the two chapters per setting. In procedural code, decomposition by modes into nested or called automata stands as chapter 2 gives it ([[called-vs-nested-state-machines]]). In object-oriented code a mode's logic goes into an automated class that the higher one calls as a supplier, not into a nested automaton reached through a special mechanism.

## Sign in code

This wiki's own reading:
- One state enum whose values combine the status of several independent parts (`V1_OPEN_V2_CLOSING`, `V1_OPEN_V2_OPEN` ...), or repeat one part's states once per part (`V1_OPENING` ... `V5_OPENING`), so the number of states grows with the product or the number of the parts. This calls for decomposition by object. (An existing state variable with extra flags beside it that change what a state does is [[replace-flags-with-explicit-states]]; this page owns the product of *independent* parts.)
- A state whose handler holds a long block of its own sequencing logic (nested ifs over sub-phases) under one abstract action. This calls for decomposition by mode.
- Two or more state machines whose transition tables are identical except for the names of their inputs and outputs. They call for one parametrised machine class instantiated per object.
- In object-oriented code, an automaton reaching another through a special mechanism (`run_nested(B, event)`, a shared event queue between them) instead of calling a method on an object (one state machine's guard reading another machine's state is [[state-machines-communicate-through-an-explicit-interface]]); or hierarchical or orthogonal states used to keep one class manageable where the regions touch disjoint data.

## When not to apply

- A small problem that one automaton handles readably. The book says the two-valve task is easy with one automaton and serves only to demonstrate (p. 58).
- Decomposition by object when the behaviour at this level belongs to the whole and not to any part (the microwave's On/Off and Microwave/Grill levels).
- Splitting by object while keeping state-number exchange. In the book's own example this made the system larger and harder to understand (p. 62). Split only together with an explicit interface: [[state-machines-communicate-through-an-explicit-interface]].
- Grouping states on a diagram, or a helper that factors out shared transitions, is not nesting: the book keeps grouping as a cosmetic device (p. 110), and the shape is [[state-grouping-for-shared-transitions]].
- Where every control state reaches every part of the control object, which the book admits occurs, though rarely (p. 105), a flat split into peers does not apply. The repair there is a layer of abstraction, an automated control object one level down.
- This wiki's own limit: if the combined states are few and the concerns really interact in each one, a split adds a class and a protocol between two objects without removing any transition. The book gives no size threshold, so "too complex" is a judgement and not a count.

## Repair

List the controlled objects. If there are several and they behave alike, write one machine parametrised by its object, give it a small set of events, and create one instance per object. Keep a coordinator only if it carries real logic. If there is one object with qualitatively different modes, move each complex mode's logic into its own sub-machine, either called (for an uninterruptible sequence) or nested: see [[called-vs-nested-state-machines]].

In object-oriented code, give each independent part a class with its own control state and event methods. Where one part drives another, make the driven part a supplier whose methods the higher automaton calls as its outputs. If the parts are fused in a given component, put an adapter per abstraction in front of it, or map each abstraction to the component's own methods.

## Before and after

```
// before: one machine over five valves, each valve's states copied in
states: CLOSED, V1_OPENING, V2_OPENING, ..., V5_OPENING, OPEN,
        V5_CLOSING, ..., V1_CLOSING          // 12 states, 2 more per valve
step():
  CLOSED:     if openBtn: open1(); state = V1_OPENING
  V1_OPENING: if isOpen1(): stop1(); open2(); state = V2_OPENING
  V2_OPENING: if isOpen2(): stop2(); open3(); state = V3_OPENING
  ...  // the same two lines again for every valve, both directions
```

```
// after: one valve class, instances per valve, coordinator calls them
class ValveMachine(valve):
  run(OPEN):  valve.open();  wait until valve.isOpen();   valve.stop()
  run(CLOSE): valve.close(); wait until valve.isClosed(); valve.stop()

head.step():
  CLOSED:  if openBtn:  state = OPENING
  OPENING: for v in valves:           v.run(OPEN);  state = OPEN
  OPEN:    if closeBtn: state = CLOSING
  CLOSING: for v in reversed(valves): v.run(CLOSE); state = CLOSED
```

The book moves from two valves to five in the same terms (p. 63); with two, its own limit above applies.

The object-oriented form, on the book's microwave case:

```
// before: one automated class over the product of three concerns
class Microwave:
    private state = UNLOCKED_IDLE_MW
    // {LOCKED, UNLOCKED} x {IDLE, RUNNING, PAUSED} x {MW, GRILL}, 8 reachable
    open_door():
        switch state:
            case LOCKED_IDLE_MW:      device.unlock(); state = UNLOCKED_IDLE_MW
            case LOCKED_IDLE_GRILL:   device.unlock(); state = UNLOCKED_IDLE_GRILL
            case LOCKED_PAUSED_MW:    device.unlock(); state = UNLOCKED_IDLE_MW
            case LOCKED_PAUSED_GRILL: device.unlock(); state = UNLOCKED_IDLE_GRILL
            // RUNNING cases: ignored
    toggle_heater():
        switch state:
            case UNLOCKED_IDLE_MW:    device.grill(); state = UNLOCKED_IDLE_GRILL
            case UNLOCKED_IDLE_GRILL: device.mw();    state = UNLOCKED_IDLE_MW
            ...  // the same pair again for every lock and timer state
    start(), pause(), close_door(), timer_done(): ...  // one case per product state
```

```
// after: three automated classes, the oven is their client
class DoorLock:                   // automated: LOCKED, UNLOCKED
    open():   if state == LOCKED:   device.unlock(); state = UNLOCKED
    close():  if state == UNLOCKED: device.lock();   state = LOCKED
    locked(): return state == LOCKED

class Timer:                      // automated: IDLE, RUNNING, PAUSED
    start():   if state != RUNNING: device.start_timer(); state = RUNNING
    pause():   if state == RUNNING: device.stop_timer();  state = PAUSED
    done():    if state == RUNNING: state = IDLE
    running(): return state == RUNNING

class Heater:                     // automated: MW, GRILL
    toggle(): switch state: case MW: device.grill(); state = GRILL
                            case GRILL: device.mw(); state = MW

class Microwave:
    open_door():     if not timer.running(): door.open()
    close_door():    door.close()
    start():         if door.locked(): timer.start()
    pause():         timer.pause()
    toggle_heater(): if not timer.running(): heater.toggle()
    timer_done():    timer.done()
```

The one emulator `device` still serves all three classes: the book's case of a component indivisible in the implementation and composite in the model. Only `Microwave` combines the parts, through the named queries `door.locked()` and `timer.running()`, so no class reads another's state field and the parts do not depend on each other ([[state-machines-communicate-through-an-explicit-interface]]).

## Source

Polikarpova, Shalyto, *Automata-Based Programming* ([[automata-based-programming]]): ch. 2, pp. 51, 55-63; ch. 3, the rule of splitting into classes, p. 104; the critique of nesting, pp. 101 and 105; the two objections and the microwave case, pp. 104-105; the flat notation and cosmetic grouping, p. 110. The quotations are verbatim. The signs, the split against [[replace-flags-with-explicit-states]] and [[state-machines-communicate-through-an-explicit-interface]], the per-setting resolution of chapters 2 and 3, the size-judgement limit, the repairs as code, and the pseudocode are this wiki's own; the book gives the microwave case in prose, without code. The deployment discussion (parallel automata on separate controllers) is left out as architecture.
