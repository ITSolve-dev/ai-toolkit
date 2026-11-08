---
title: Give each routine functional cohesion
category: functions
summary: "A routine whose operations share only an execution order, the same data, the moment they run, or a control flag that picks one of several unrelated actions (InputAll(kind), Startup doing the work itself); split it into routines that each do one thing."
tags: [rule, cohesion, routine-design, control-flag]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-07
---

Cohesion of a routine is how closely the operations inside it serve one purpose (the concept is on [[cohesion]]). McConnell takes the idea from Stevens, Myers and Constantine (1974). He says that at class level it has largely given way to abstraction and encapsulation, but that it remains a useful heuristic for designing a single routine (*Code Complete*, p. 163). His example pair is `Cosine()`, which has one purpose, and `CosineAndTan()`, which does two things and is less cohesive (pp. 163-164).

## Rule

Aim for **functional cohesion**: the routine performs one and only one operation, as `sin()`, `GetCustomerName()`, `EraseFile()` or `AgeFromBirthdate()` do. The author adds that this judgement assumes the routine does what its name says. Otherwise the name is bad and nothing definite can be said about its cohesion (p. 164). He holds that functional cohesion can almost always be reached, and asks the reader to learn the ideas rather than the labels: «Изучайте идеи, а не терминологию.» (p. 166).

The reasoning is reliability. In one study of 450 routines, 50% of the highly cohesive routines were defect-free, against 18% of the routines with low cohesion (Card, Church and Agresti, 1986). In another, the routines with the highest coupling-to-cohesion ratio had 7 times as many errors as those with the lowest, and were 20 times as costly to fix (Selby and Basili, 1991) (p. 164).

The weaker kinds the book names, with its repair for each (pp. 164-166):

| Kind | What holds the operations together | Book's repair |
|---|---|---|
| Sequential | They must run in a given order, and each uses the previous step's data, yet together they do not form one function (age, then time to retirement, both from a birth date) | Two routines, each functionally cohesive. The second may call the first |
| Communicational | Only that they use the same data (print a report, then reinitialise the data passed in) | Split them, and move the reinitialisation next to the code that creates or changes the data |
| Temporal | They run at the same time (`Startup()`, `Shutdown()`, `CompleteNewEmployee()`) | The routine does none of the work itself. It calls other routines, so its job is coordinating them |
| Procedural | Only the order, here the order a user is asked for input (name, then address, then phone) | Separate routines, with the caller doing one whole job: `GetEmployee()`, not `GetFirstPartOfEmployeeData()`. This often means changing two or more of the original routines |
| Logical | A control flag passed in picks which of several unrelated operations runs, through a large `if` or `case` (`InputAll()`, `ComputeAll()`, `PrintAll()`) | One routine per operation. Shared code moves to a lower-level routine, and the routines go into a class |
| Coincidental | Nothing | Redesign and rewrite. The book's opening `HandleStuff()` example is its instance |

The author calls the kinds below temporal "usually unacceptable" and advises rewriting a poorly cohesive routine rather than debugging it: «Метод с плохой связностью лучше переписать, чем тратить время и средства на поиск проблем.» (p. 165). He suggests that logical cohesion might better be called "illogical", because the only tie between its operations is the routine's control logic (p. 166).

## Sign in code

- A parameter whose only use is to choose a branch, where each branch does a different job and the branches share nothing but the routine's frame: `Process(kind)` with `if kind == CUSTOMERS ... else if kind == TIMECARDS ...`. This is logical cohesion.
- A routine named after a moment (`Startup`, `OnSave`, `Init`) whose body performs the steps inline: it opens files, parses, allocates and draws, rather than calling a named routine for each step. This is temporal cohesion done badly.
- A routine whose honest name needs "And" between two results (`AgeAndRetirement`, `PrintAndReset`), or whose name names only part of a whole (`GetFirstPartOf...`). These are sequential, communicational or procedural cohesion.
- A routine whose statements fall into groups that share no variable with each other. This is coincidental cohesion.

This wiki assigns the neighbouring cases as follows. This page owns the shape "one routine, several unrelated jobs". A flag or mode parameter choosing which of one class's validations run is [[mixins-share-functionality]]; a control flag choosing among unrelated actions is [[routine-cohesion]]. A control flag passed as a bare literal at the call site is [[semantic-coupling]], which owns the call site. Where an integer or boolean code selects which of several unrelated jobs a routine body does, [[routine-cohesion]] owns the body and the repair is one routine per job; where the code names a value the routine handles in one way, [[enum-instead-of-codes-and-flags]] owns it. A routine that mutates state and returns a value describing the mutation belongs to [[command-query-separation]]. A requirement that callers invoke separate routines in a fixed order belongs to [[temporal-coupling]]. A switch on an object's type calling a type-specific method in each arm is [[polymorphism-or-type-switch]]. A flag parameter that selects between unrelated jobs the routine performs inline is [[routine-cohesion]]; a flag that only switches off a trailing or leading line for one caller is [[move-statements-across-call-boundary]]. A routine whose later part reads a different set of inputs and only a few results of its earlier part has sequential cohesion, which [[routine-cohesion]] owns; [[split-phase]] is the procedure that separates its parts.

## When not to apply

- **Dispatch only.** The book accepts a logically cohesive routine whose code consists only of `if` or `case` statements and calls to other routines. When its sole role is to coordinate commands and it does no work itself, «это обычно удачное проектное решение» (p. 166). It calls such routines event handlers. The book's sidebar says such a routine's cohesion may be satisfactory and raises whether the `case` should become a polymorphic call (p. 166); this wiki routes that question to [[polymorphism-or-type-switch]].
- **Temporal routine that only orchestrates.** Named for its moment (`Startup`) and made of calls, it counts as functionally cohesive. The book notes that the name decides how it reads: `ReadConfigFileInitScratchFileEtc()` would admit coincidental cohesion, while `Startup()` states one purpose (p. 165).
- **A sequence that is one function.** This wiki adds a limit the book does not state. When the steps together compute one named result (parse, then validate, then build one value), and no caller needs any intermediate step on its own, the sequence is the function. Splitting it then adds names nobody calls.

## Repair

1. Name what each group of statements produces.
2. Give each product its own routine.
3. Leave behind a caller that either composes them (it stays functionally cohesive under its own name) or disappears, its callers calling the parts directly.
4. For a flag-selected routine, replace each flag value with its own routine. Callers that passed a constant flag now call the matching routine by name.

## Before and after

```
routine Input(kind)
    if kind == 1
        read customer names from file
        store them in customers
    else if kind == 2
        read time cards
    else if kind == 3
        read inventory rows

Input(2)
```

```
routine InputCustomerNames()
    read customer names from file
    store them in customers

routine InputTimeCards()
    read time cards

routine InputInventory()
    read inventory rows

InputTimeCards()
```

The "after" has no flag, and each routine's name states its single result. The "before" is not a dispatcher in the sense of the first limit, because its branches do the work inline rather than call routines.

## Source

- McConnell, *Code Complete*, 2nd edition, Russian edition, section 7.2, pp. 163-166 ([[code-complete]]). The rule, the kinds of cohesion with their repairs, the studies, and the dispatch and orchestrating-temporal limits are the book's.
- The signs, the third limit (a sequence that is one function), the reading of the polymorphism sidebar, the owner split with [[semantic-coupling]], [[enum-instead-of-codes-and-flags]], [[command-query-separation]], [[temporal-coupling]] and [[polymorphism-or-type-switch]], and the pseudocode are this wiki's own.

Related: [[routine-names]], [[extract-routine-to-name-a-step]], [[coupling]], [[routine-review-checklist]].
