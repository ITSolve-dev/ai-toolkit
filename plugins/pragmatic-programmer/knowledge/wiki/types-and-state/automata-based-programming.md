---
title: Automata-Based Programming (Polikarpova, Shalyto)
category: types-and-state
summary: "Source page, no rules of its own: a textbook on programming with explicitly separated states, whose pages here own the state-machine shapes in code (history held in flags, a switch that does not mirror the graph, overlapping or missing transitions, control logic mixed with the data it controls, how events reach a machine, how a machine is packaged as a class)."
tags: [summary, state-machine, automata-based-programming]
sources: [automata-based-programming]
created: 2026-11-06
updated: 2026-11-06
---

Polikarpova and Shalyto's *Automata-Based Programming* (автоматное программирование, also called "programming with explicit separation of states") presents a method for building programs whose complex behaviour is described by automata. The authors stress that it is not mainly about using finite automata inside programs but about a way of building such programs as a whole (p. 4). This summary covers the preface, chapter 1 (concepts and automaton models), chapter 2 (procedural programming with explicit states), chapter 3 (the object-oriented form), chapter 4 (new problems: verification, parallelism, genetic programming) and the conclusion.

## Edition and authority

Edition read: Russian, ITMO University, 2008, 168 pages; the raw file was extracted with the `--fast` mode of `read-book`, which gives a clean text layer, so quotations were checked against `raw/`. One of the authors proposed the technology behind the method in 1991, and the book presents itself as the first attempt at a complete account of it as a paradigm (p. 4). It is therefore the method's own advocate, not an outside assessment. It argues from worked examples (an alarm clock, valves and a microwave from logic control, a flight-booking client) and from automata theory, not from measurement. Its conclusion admits the account is incomplete, because the technology is still developing (p. 151).

## Thesis

- An entity has **complex behaviour** when the same input can produce different reactions depending on its history ([[complex-behavior]]). Such an entity is best modelled as an [[automated-object]]: a small, surveyable control automaton that holds every decision of "which action now", and a controlled object with simple behaviour reached only through queries and commands.
- The state that selects actions (control state) is kept apart from the state that only stores results (computational state), and only the first becomes explicit states ([[control-and-computational-states]]).
- Code mirrors the transition graph one to one, so the graph can be read, checked and regenerated from it ([[state-machine-as-switch-on-state]]); the graph is then open to checks that are hard without it ([[transition-conditions-consistent-and-complete]], [[state-machine-execution-log]]).
- In object-oriented code the entity with complex behaviour becomes one [[automated-class]], and decomposition is by objects, not by nesting automata ([[decompose-state-machine-by-modes-or-by-controlled-objects]]).

## Scope and limitations

- Large parts of the book are outside this wiki's charter and yielded no pages: automata theory beyond what changes code, the specification notations of sections 2.2 and 3.2 as notations, chapter 4.1 (automata in discrete-mathematics algorithms), formal verification by model checking in 4.2, 4.3 (parallel computing) and 4.4 (genetic programming of automata). Deployment of automata on separate controllers was left out as architecture.
- The book judges that applying automata concepts in functional or logic programming would most likely be of purely theoretical value (p. 95). Its pages carry `paradigm: any` where the rule is about the shape of a state machine in any code, and `paradigm: oop` for chapter 3, except where one page resolves both chapters ([[decompose-state-machine-by-modes-or-by-controlled-objects]]).
- The listings contain typos (in the two-valve listing one transition writes `y = 4` for `y1`, p. 84; chapter 3's listings use an undeclared variable and a field private in the base). The pages do not reproduce the listings; their pseudocode is this wiki's own.
- The book states rules for diagrams and templates, and rarely a sign in code or a limit; as elsewhere, most signs and limits on its pages are this wiki's own, marked in each `## Source`.
- The authors criticise their own tool, UniMod, on naming and reuse (p. 132), and call logic distributed over classes harder to verify (p. 133); the pages carry those costs.

## Key takeaways

This wiki reads the book as making five claims that change code:

1. **History spread over flags is a hidden state machine.** Name its states: [[replace-flags-with-explicit-states]], [[finite-memory-folds-into-states]], with the limit of finite control on [[finite-automaton-limits]].
2. **The code has the shape of the graph.** One selection on the state, one guarded branch per arc: [[state-machine-as-switch-on-state]], with tables only for machines changed at run time ([[state-machine-table-or-switch]]) and the State pattern as the object alternative ([[switch-on-state-vs-state-pattern]]).
3. **The graph is checked as a whole.** Every state reachable, guards from one state consistent and complete: [[transition-conditions-consistent-and-complete]], [[spontaneous-and-guarded-transitions]], [[state-grouping-for-shared-transitions]].
4. **Decisions and data live apart.** [[separate-control-object-from-state-logic]], at the right level of primitive operations ([[logic-vs-semantics-split]]), with actions placed by [[moore-and-mealy-machines]].
5. **Several machines talk through named interfaces, not state numbers.** [[state-machines-communicate-through-an-explicit-interface]], [[called-vs-nested-state-machines]], [[interacting-state-machines]], [[event-driven-vs-polled-state-machine]], [[passing-events-to-a-state-machine]].

## Pages by chapter

- **Chapter 1** (concepts, models, pp. 7-41): [[complex-behavior]], [[control-and-computational-states]], [[replace-flags-with-explicit-states]], [[automated-object]], [[logic-vs-semantics-split]], [[finite-automaton-limits]], [[finite-memory-folds-into-states]], [[spontaneous-and-guarded-transitions]], [[moore-and-mealy-machines]].
- **Chapter 2** (procedural, pp. 42-94): [[event-driven-vs-polled-state-machine]], [[decompose-state-machine-by-modes-or-by-controlled-objects]], [[called-vs-nested-state-machines]], [[state-machines-communicate-through-an-explicit-interface]], [[state-grouping-for-shared-transitions]], [[transition-conditions-consistent-and-complete]], [[state-machine-as-switch-on-state]], [[state-machine-table-or-switch]], [[interacting-state-machines]], [[passing-events-to-a-state-machine]], [[separate-control-object-from-state-logic]]; it also joins [[finite-state-machine]] from *The Pragmatic Programmer*.
- **Chapter 3** (object-oriented, pp. 95-133): [[automated-class]], the object-oriented half of [[decompose-state-machine-by-modes-or-by-controlled-objects]], [[contract-of-state-dependent-method]], [[switch-on-state-vs-state-pattern]], and the class form of [[separate-control-object-from-state-logic]].
- **Chapter 4** (new problems, pp. 133-150): reachability on [[transition-conditions-consistent-and-complete]], and [[state-machine-execution-log]].

## Where it disagrees

- **With *The Pragmatic Programmer* on the form of a state machine.** That book recommends a transition table driven by a loop ([[finite-state-machine]]); this one a switch with guarded branches. [[state-machine-as-switch-on-state]] resolves it per setting: a table keyed by state and event type where every transition is keyed so and its action is a name, the switch where guards span several inputs or carry priorities.
- **With itself, chapter 2 against chapter 3, on nesting.** Chapter 2 decomposes by modes into nested and called automata; chapter 3 rejects nesting in object-oriented code. [[decompose-state-machine-by-modes-or-by-controlled-objects]] resolves it by paradigm.
- **With itself on interaction by state numbers.** Chapter 2's logic-control examples let one machine read another's state number; its own later examples replace that with events, and [[state-machines-communicate-through-an-explicit-interface]] takes the later view.
- **With *Code Complete* and *The Object-Oriented Thought Process* on switches.** Those books push switches over a type code towards polymorphism ([[polymorphism-or-type-switch]]); this book keeps a switch over a control state as a legitimate template. The two shapes are told apart on [[switch-on-state-vs-state-pattern]]: whether the object's own methods reassign the value switched on.
