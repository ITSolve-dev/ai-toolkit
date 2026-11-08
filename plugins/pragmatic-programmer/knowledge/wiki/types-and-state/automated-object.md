---
title: "Automated object: control automaton plus controlled object"
category: types-and-state
summary: "Model behind state-machine code: a small automaton holds every 'which action now' decision and the transitions; a controlled object holds the data, is reached only through finite-valued queries and commands, and each command always does the same thing. The shapes that break the split are owned by separate-control-object-from-state-logic (a transition computing inline over the data) and logic-vs-semantics-split (an operation of the controlled object that reads the mode)."
tags: [concept, state-machine, separation-of-logic, controlled-object, queries-and-commands, automata-based-programming]
paradigm: any
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

An **automated object** (автоматизированный объект управления, АО) is the central model of Polikarpova and Shalyto's automata-based programming. An entity with complex behaviour ([[complex-behavior]]) is built as a pair of a **control automaton** and a **controlled object** (p. 38). The automaton chooses actions from the current control state and the input, and moves to the next state. The controlled object performs those actions. The book puts the paradigm in one line: «Парадигма автоматного программирования состоит в представлении сущностей со сложным поведением в виде автоматизированных объектов управления» (p. 17). How the two halves are balanced is [[logic-vs-semantics-split]].

## The two parts

The book takes this split from automation, where a controlling device and a controlled plant are always kept apart (p. 16). It defines the two parts as follows (p. 16):
- The **control part** is responsible for the logic of behaviour: choosing the actions to perform, which depends on the current state and the input, and moving to a new state.
- The **controlled part** carries out the actions the control part chose. It may also produce some of the control part's inputs, which the book calls feedback.

The controlled object has simple behaviour. It does not handle input from the environment directly. It only receives commands from the automaton, and «каждая команда всегда вызывает одно и то же действие» (p. 17), which the book notes is the very definition of simple behaviour. So the controlled object can be written by ordinary non-automata methods, and «Вся логика поведения сущности сосредоточена в управляющем автомате» (p. 17).

This is one form of an idea the book calls central (p. 11): separating the description of the logic of behaviour («при каких условиях необходимо выполнить те или иные действия») from its semantics («собственно смысла каждого из действий»). The logic part is also rigidly structured, which the authors say makes the description clear (p. 11).

## The formal model

The book generalises the abstract machines into this model: it replaces the fixed data store of a pushdown automaton or a Turing machine with a controlled object whose set of computational states can be anything the task needs, reached through arbitrary queries and commands (p. 34).

- **Control automaton.** A finite set of inputs, each made of a part from the environment and a part from the controlled object; a finite set of control states and an initial state; a finite set of outputs; a transition function; and an output function made of two parts, outputs in states and outputs on transitions (p. 38). In general it is therefore a mixed Moore-Mealy machine ([[moore-and-mealy-machines]]).
- **Controlled object.** A possibly infinite set of computational states, a query function from computational state to the automaton's input, and a command function that changes the computational state according to the automaton's output (p. 38). The book notes that these queries and commands are what object-oriented code calls queries (value-returning) and commands (state-changing) (p. 34, footnote 3).

## Properties the model asks for

- **Finite and surveyable control.** The automaton must be finite, and in addition its states, inputs and outputs should be «небольшим (обозримым)» (p. 34). An automaton with a thousand states is finite, but its graph cannot be drawn, which «сводит на нет» the benefit of separating control states (pp. 34-35). Computational states may be as many as needed (p. 35).
- **Indirect access to data.** Because it is finite, the automaton cannot read or write the computational state directly. It sees that state only through a small number of queries with finite-valued results, and changes it only through a small number of commands (p. 35).
- **Acts only on its own controlled object.** The automaton could in principle act on the environment directly. The authors advise decomposing so that each automaton acts only on its own controlled object, to minimise links between modules, and note that such links can usually be removed by bringing the controlled entities into the controlled object (p. 37).
- **Nesting.** A low-level automated object can be wrapped inside the controlled object of a higher-level one. That is how the approach supports levels of abstraction (p. 40).

## Active and passive, polled and event-driven; open and closed

In a **passive** model the environment starts each step and gets control back when it ends; that suits event-driven interaction, where the environment signals a change by calling the automaton with an event. An **active** model starts the next step as soon as one ends and polls the environment's state (pp. 35-36). In a passive model, in general, only some inputs are events; the rest are ordinary variables that the automaton polls, and a change in them does not start a step (p. 36). The choice changes the automaton: the counting trigger needs four states when it polls a boolean button and two with separate press and release events (p. 29). The decision is [[event-driven-vs-polled-state-machine]].

Without input from the controlled object, so with no queries, the model is **open** (no feedback). With that input it is **closed** (pp. 36, 39).

## Outputs as commands

In programming each output variable usually stands for one command: 1 means do it, 0 means skip it. If the result depends on the order in which commands run, an output given as a *set* of commands is nondeterministic, so the output is often a *sequence* of commands instead (p. 37).

## Reading it in code

This wiki reads the model as a check on any state-machine implementation. These readings are this wiki's own:
- The automaton's handlers should contain only state switches, transitions and calls to the controlled object, with no arithmetic or I/O inline.
- The controlled object's operations should take no mode argument and read no mode field. If an operation branches on the automaton's state, part of the logic has leaked into the controlled part. An operation of the controlled object that itself reads the mode is the 'semantics overloaded' shape of [[logic-vs-semantics-split]].
- Transition conditions call named boolean or enum queries of the controlled object ("is it one minute before the alarm?"), not inline expressions over its data ([[control-and-computational-states]]).
- A transition whose actions are kept in an unordered collection, or fired from flags in an order nobody stated, while the commands touch shared state, is the nondeterminism of p. 37 in code.

The rule that enforces the split, with its sign and repair, is [[separate-control-object-from-state-logic]]; the object-oriented packaging is [[automated-class]]. The procedure for refactoring flag code into this shape is [[replace-flags-with-explicit-states]]. The preface says the automated controlled object is «по своей природе глубоко объектно-ориентированной» (p. 5); the book's object-oriented implementation comes in later chapters.

## What it buys, what it costs, and its limits

- **Gain (the book's claim):** once the split is made, the entity is easy to implement, and its implementation becomes understandable and easy to modify (p. 17).
- **Cost (the book's claim):** finding which entities have complex behaviour, and pulling out their logic, are «сложные творческие задачи» (p. 11) that the developer settles for each entity individually. The method does not say where the boundary lies.
- **Limit (the book's own):** apply it only to the components that have complex behaviour. Elsewhere it overloads specifications and code with logic that is not needed (p. 11). Where the output does not depend on history, the combinational case, there are no control states to model (p. 27).
- The authors say no single automaton model fits every task: active and passive, open and closed models, and different forms of input and output all have uses, which is why the definition is kept abstract (p. 37).

## Source

- Polikarpova, Shalyto, *Automata-Based Programming* ([[automata-based-programming]]). Preface, p. 5. Ch. 1: logic versus semantics and the cost of identification, p. 11; control and controlled parts, p. 16; simple behaviour of the controlled object and the statement of the paradigm, p. 17; the counting trigger, p. 29; section 1.4.3, pp. 33-41, for the formal model, its properties, active and passive and open and closed models, outputs as commands, and nesting.
- This wiki's own parts: the "Reading it in code" checks.
