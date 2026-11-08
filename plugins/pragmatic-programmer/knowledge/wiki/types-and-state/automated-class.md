---
title: Model an entity with complex behaviour as an automated class
category: types-and-state
summary: "Clients drive a state machine directly (handle(EVENT), step(e), reading or writing its state field), its control state lives in globals, or a class only wraps one transition routine; repair: one class whose public methods are the events and whose method bodies pick the action by a private control state."
tags: [rule, state-machine, encapsulation, oop, class-interface]
paradigm: oop
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

An **automated class** (автоматизированный класс) is Polikarpova and Shalyto's object-oriented model of an entity with complex behaviour ([[complex-behavior]]): an entity that answers the same input differently depending on its history. To its clients it looks like an ordinary class. Inside, each public method chooses what it does from a hidden control state. It is the object-oriented form of [[automated-object]].

The argument starts from a diagnosis. Leaving polymorphism aside, a class answers a given call by running the same algorithm every time, which is the book's definition of simple behaviour: «Класс является моделью сущности с простым поведением» (p. 98). The book calls this the deep reason why object technology in its original form does not fit complex behaviour. Its repair: «Моделью сущности со сложным поведением должна быть специальная разновидность класса» (p. 101). On a call, «выбор выполняемого действия (тела компонента) должен осуществляться в зависимости от управляющего состояния» (p. 101).

## Rule

An entity whose reaction to a call depends on its control state becomes one class:

- its interface is that of an ordinary class, with one method per event the automaton handles. The book: «Интерфейс автоматизированного класса ничем не отличается от любого другого» (p. 105);
- the control state is private, and each method body is the transition and output function for its event;
- the queries and commands of the control object become the automaton's inputs and outputs. They go in a separate supplier class when the control object is an abstraction in its own right; when it is not, they go in the automated class itself or spread over several suppliers (pp. 102-103). See [[separate-control-object-from-state-logic]];
- entities whose behaviour is simple stay ordinary classes (p. 102).

The book rejects two earlier models, and their shapes are the signs below.

- **The automaton as a subroutine.** Wrapping the transition routine in a class, even with the state number encapsulated, «сути дела такая «обертка» не меняет» (p. 99). The book draws a parallel with active objects, where a class owns a main routine, and states the principle: «Класс должен описывать сущность, предоставляющую набор сервисов, а не программу» (p. 100).
- **The automaton and its control object as separate classes**, with automata nested in each other. According to the book an automaton is not an abstraction in its own right: «самостоятельной абстракцией в автоматной архитектуре является не отдельно взятый автомат, а вся сущность со сложным поведением в целом» (p. 101). It asks whether a valve-control automaton could start running a coffee maker in another system.

The reasoning is encapsulation. In the procedural form of the method, the computational state of every control object and the control state of every automaton are global (p. 98), and the book says «Такие избыточные зависимости делают систему неспособной к эволюции» (p. 98). A second reason is practical: most existing systems are object-oriented, and a new entity with complex behaviour has to fit into one as a single new class; otherwise, the book warns, «придется перепроектировать всю систему с нуля в автоматном стиле» (p. 99).

## Sign in code

This wiki's own reading:

- Clients call a generic dispatcher such as `machine.handle(EVENT_BACK)` or `step(e)`, pass event codes, or read or write the state variable, instead of calling named methods.
- The control state, or the data it decides on, sits in globals or module-level variables that other routines also touch.
- A class has a single public `run`/`process`/`step` method holding the whole transition switch, and its other members are only the state number. This is the subroutine in a wrapper.
- A separate automaton class and its control-object class are both visible to clients, and clients must coordinate the two.

The book's example (pp. 112-114): in an online flight-booking client the `Application` entity is complex because «в зависимости от этапа нажатие одних и тех же кнопок («Вперед» и «Назад») производит разный эффект» (p. 114). On the `Reservation` screen, whether saving or reloading personal data is available «зависит от предыстории» (p. 114). Both become automated classes, and every other entity stays an ordinary class.

This wiki assigns the neighbouring cases as follows. This page owns the packaging of a state machine in object-oriented code: how clients reach it and where its state lives. Whether history spread over boolean flags should become one explicit control state is [[replace-flags-with-explicit-states]]; when one fragment shows both, that page decides whether there is a state machine at all, and this page decides how it is exposed. How the private body selects by state (switch or State pattern) is [[switch-on-state-vs-state-pattern]]. In procedural code, how an event reaches a step function is [[passing-events-to-a-state-machine]]; in object-oriented code, where each event is a public method, it is [[automated-class]]. Client code that reads or writes a machine's state field is [[automated-class]]; one state machine's guard reading another machine's state is [[state-machines-communicate-through-an-explicit-interface]].

## When not to apply

- The entity's behaviour is simple: every call runs the same algorithm whatever came before. The book keeps such entities as ordinary classes (p. 102). This wiki adds that an automated class for them is ceremony with nothing to hide.
- The control object is not an abstraction in its own right. Then the rule does not demand a separate control-object class, and its operations may live in the automated class or in several suppliers (p. 103). Splitting one off anyway departs from the book's version of this rule.
- Where the code is generated from a transition diagram by a tool, the generated body is the tool's (p. 106). This wiki reads that as: review the interface the clients see, not the generated body.
- The rule assumes object-oriented code. The book judges that applying automata concepts in functional or logic programming would most likely be of purely theoretical value (p. 95), and this page says nothing about them.
- A dispatcher that receives events from outside the process (a message loop, a UI toolkit callback taking an event code) is the environment, not a client; the sign concerns code in the project that could call a named method and calls `handle(code)` instead. This limit is this wiki's own.

## Repair

1. Name one public method per event clients send, and remove the generic dispatcher from the public interface.
2. Move the control state into a private field of that class, and remove every global copy.
3. In each method, select the action by the current state, by a switch on the private state or by the State pattern ([[switch-on-state-vs-state-pattern]]).
4. Make the control object's queries and commands calls to a supplier or to private methods, so the automaton's inputs and outputs are named operations, not shared variables.
5. If one class ends up with too many states, split it by objects as in [[decompose-state-machine-by-modes-or-by-controlled-objects]], not by nesting automata.

## Before and after

```
// before: the automaton is a subroutine, its state is global
global stage = SEARCH

function app_step(event):
    switch stage:
        case SEARCH:  if event == NEXT: stage = CHOICE;  show(choice_screen)
        case CHOICE:  if event == NEXT: stage = BOOKING; show(booking_screen)
                      if event == BACK: stage = SEARCH;  show(search_screen)
        case BOOKING: if event == BACK: stage = CHOICE;  show(choice_screen)

// client
app_step(NEXT)
if stage == BOOKING: ...
```

```
// after: an automated class; clients see ordinary methods
class Application:
    private stage = SEARCH
    private screens            // supplier: the control object's commands

    next():
        switch stage:
            case SEARCH:  stage = CHOICE;  screens.show_choice()
            case CHOICE:  stage = BOOKING; screens.show_booking()
            case BOOKING: screens.confirm_booking()

    back():
        switch stage:
            case SEARCH:  // no effect
            case CHOICE:  stage = SEARCH;  screens.show_search()
            case BOOKING: stage = CHOICE;  screens.show_choice()

// client
app.next()
```

The after keeps a switch on state, and that is the intended shape: the switch is private and sits in the body of a method named for its event. Every event method opening with a switch over `stage` is the sign of [[switch-on-state-vs-state-pattern]]; this wiki reads the after as inside that page's limit for a machine with two or three states and a few events, where every switch fits on a screen. The before shows behaviour that depends on history, so it is not covered by the limit on simple behaviour.

## Source

Polikarpova, Shalyto, *Automata-Based Programming*, ch. 3 ([[automata-based-programming]]): the diagnosis and the rule, pp. 98 and 101; the rejected models, pp. 99-101; the control object in a separate class or not, pp. 102-103; the encapsulation argument, p. 98; the interface, p. 105; generation, p. 106; functional and logic programming set aside, p. 95; the booking example, pp. 112-114. The signs in code, the assignment of neighbouring cases, the ceremony remark in the first limit, the generated-code limit as a review instruction, the external-dispatcher limit, the pseudocode and the reading of the after against [[switch-on-state-vs-state-pattern]] are this wiki's own. The book describes the shapes as architectures in diagrams, not as client code.
