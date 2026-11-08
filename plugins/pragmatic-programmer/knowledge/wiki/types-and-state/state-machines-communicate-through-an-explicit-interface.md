---
title: State machines communicate through an explicit interface
category: types-and-state
summary: "One state machine's guard reads another machine's raw state number or enum (`if valveA.state == 3`, `a2.y != 1`), or a flag field sits in shared data only to signal between machines: name each dependence as a predicate the owner exposes, then replace it with an event."
tags: [rule, state-machine, automata-based-programming, coupling, interface]
paradigm: any
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

Polikarpova and Shalyto list four ways automata exchange information and rank them (pp. 54-55):

1. **A shared controlled object.** The book calls this powerful, but it has the defects of global variables: «отсутствие явного интерфейса межмодульного взаимодействия и, как следствие, чрезмерная зависимость между модулями» (p. 54). It also has an automata-specific defect: the exchanged information is control information, which should not be mixed with the computational state of the object ([[control-and-computational-states]]). "Abuse" here means adding to the controlled object variables that belong to control rather than to computation (p. 55, footnote 7).
2. **Exchanging state numbers.** A guard contains a predicate of the form "automaton i is (not) in state j". It is simple and keeps control and computational information apart. It is ideal for logical control, but it is not recommended in large software systems, because it needs access to the automaton's internals and so strengthens coupling (p. 55).
3. **Events raised by automata.** In an event-driven system an automaton may raise an event, which the automaton executed next handles. This generalises calling an automaton with an event (p. 55).
4. **Messages.** These are events carrying data of any size and structure, sent to one automaton, a group, or the whole system. It is the most powerful option, paid for with a more complex implementation (p. 55).

The two-valve example shows the cost. The version decomposed by valves and wired by state numbers came out «больше и сложнее для понимания», and the authors trace the extra complexity largely to the state-number mechanism. They propose instead to give each valve machine two events (open, close) and make it called (p. 62).

Where the book does keep state numbers, in the parallel and nested valve designs (pp. 64, 67-68), its notation gives each predicate its own link on the link scheme and its own verbal meaning, and the authors call that «шагом на пути к четко определенному интерфейсу взаимодействия между автоматами» (p. 68). Because every predicate already carries a distinct meaning, they note, moving to event-based interaction then only needs each predicate replaced by a separate event (p. 68).

## Rule

In a software system that is more than trivial, pass control information between state machines as events or messages, through a small declared interface. Do not let one machine read another's raw state, and do not route control through flags in shared data. Where a state test stays for now, give it a name with a stated meaning, so that it can later become an event.

## Sign in code

This wiki's own translation:

- A transition guard in machine A compares machine B's state field with a numeric or enum literal: `if pump.state == RUNNING`, `if a5.y != 3`. The same comparison may be repeated in several places, or appear in both its positive and its negated form, with no name saying what that state of B means to A. Renumbering or splitting a state in B then silently changes A's conditions.
- A boolean or enum field in a shared data structure is written by one machine and read by another only to coordinate them (`openingDone`, `phase2Started`), and plays no part in the domain computation.

This wiki assigns the neighbouring cases as follows. Client code that reads or writes a machine's state field is [[automated-class]]; one state machine's guard reading another machine's state is [[state-machines-communicate-through-an-explicit-interface]]. A flag in shared data written by one state machine and read by another only to coordinate them is [[state-machines-communicate-through-an-explicit-interface]]; a status read by other functions outside its owner is [[status-variable-as-enumeration]]. This page covers machines inside one module; how separate modules or services exchange events or messages is architecture, taken as given.

## When not to apply

- Logical control on controllers, where the book calls state-number exchange traditional and ideal (p. 55).
- Small systems in which the authors themselves use state-number exchange throughout; their own decentralised two-valve design keeps it and stays simple (p. 64). This wiki's threshold: a single test in one place, in a machine whose author also owns the other machine, may not justify an interface.
- Data that really is computational state shared by several machines. The book notes that this channel always exists while machines share a controlled object. Only the *extra* control variables are abuse (p. 55, footnote 7).
- Code that is already event-driven, where the other machine emits events and the reader consumes them, has nothing to repair.
- This wiki adds: a tiny system where a single machine would do. Then merge the machines instead of adding an interface.

## Repair

1. Give each state test a name that says what it means to the reader, and put it in the owning machine (`valve2.isClosed()` rather than `valve2.state == 1`), so that the numbering stays private. The book treats named predicates as the step towards an interface (p. 68).
2. Where the reader is really reacting to a change of state, replace the predicate with an event the owner raises on that transition, or with a call carrying an event ([[called-vs-nested-state-machines]]). Where a coordinator needs to know about completion, a called sub-machine returning on its final state expresses it directly.
3. Move coordination flags out of the shared data. The general rule on shared global data is [[global-data]].
4. While reviewing the dependencies, check the graph of which machine calls or nests which. The source notes that cycles in it «могут приводить к зацикливанию» (p. 68).

## Before and after

```
// before: valve2's machine peeks at valve1's internals
valve2.step():
  if state == IDLE and valve1.state == 3: state = OPENING; open2()
```

```
// after: valve1 raises a named event; valve2 reacts to it
valve1.step():
  if state == OPENING and isOpen1(): stop1(); state = OPEN; raise(VALVE1_OPENED)
valve2.handle(event):
  if state == IDLE and event == VALVE1_OPENED: state = OPENING; open2()
```

An intermediate step, where events are not yet available, is a query on the owner: `valve1.isOpen()` in place of `valve1.state == 3`.

## Source

- Polikarpova, Shalyto, *Automata-Based Programming*, ch. 2 ([[automata-based-programming]]). The four mechanisms and their ranking, pp. 54-55, with footnote 7; the two-valve cost and the switch to events, p. 62; state-number exchange in the parallel and nested designs, pp. 64, 67-68; named predicates as a step towards an interface, the predicate-to-event replacement, and cycles in the call graph, p. 68. The quotations are verbatim. The analogy with global variables is the book's.
- This wiki's own parts: the signs in code, the assignment of neighbouring cases, the note that architecture between modules is out of scope, the small-system threshold and the last two limits, the repair through a query owned by the other machine, the step list, and the pseudocode. The source states these points for link schemes and diagrams, not for code.
