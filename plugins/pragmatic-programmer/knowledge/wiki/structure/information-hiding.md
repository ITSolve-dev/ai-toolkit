---
title: Information hiding
category: structure
summary: "Concept: each class, routine or package is defined by the design decision (secret) it keeps from the rest; its absence shows as a representation detail (how a value is made, its type, a size, a file format) visible where the value is used."
tags: [concept, information-hiding, encapsulation, secrets, interfaces, change]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Information hiding is the design heuristic of deciding, for each class, package or routine, which design or construction decisions it keeps from the rest of the program. McConnell traces it to Parnas's 1972 paper on decomposing systems into modules and treats it as a foundation of both structured and object-oriented design (p. 89). The decisions kept are called *secrets*.

## What a secret is

The book lists as candidate secrets a likely source of change, a file format, the implementation of a data type, and an area to be isolated so that an error in it does limited damage (p. 89). Its test for the boundary: «Небольшие изменения системы могут влиять на несколько методов класса, но не должны распространяться за его интерфейс.» (p. 89) And for the interface: «Интерфейс класса должен сообщать как можно меньше о внутренней работе класса.» (p. 89)

The book sorts secrets into two categories (p. 91):

- secrets that hide **complexity**, so a programmer can forget it while working elsewhere: complicated data types, file structures, boolean tests, intricate algorithms;
- secrets that hide **sources of change**, so the effect of a change stays local. The common ones are on [[anticipate-likely-changes]].

## The question it asks

The book's working form of the heuristic is a question: «Что этот класс должен скрывать?» (p. 94). If a function or a piece of data can go into the public interface without exposing the class's secrets, put it there; otherwise do not (p. 94). The book claims this question reaches decisions object-oriented modelling misses: asked "should the identifier be an object?", a developer says no and uses a bare integer, while asked "should the identifier's type be hidden?", the same developer may declare a named type for it (p. 93). The worked rule is [[hide-secrets-behind-one-access-point]]; the same rule applied to stored data is [[single-owner-of-data-access]].

The book applies the heuristic at every scale, from named constants instead of literals, through data types, to routines, classes and subsystems (p. 91), and notes that «Сокрытие информации не всегда требует создания целого класса.» (p. 96) A named constant can be enough.

## Barriers the book names

Most barriers are habits of mind, the book says, not real impossibilities (p. 91):

- **Excessive distribution of information.** A literal repeated across the program, user-interaction code spread through the system, direct access to a global array whose size and shape then become known everywhere (pp. 91-92). See [[hide-secrets-behind-one-access-point]] and [[global-data]].
- **Circular dependency**, as when a method of class A calls one of B and a method of B calls one of A: neither class can be tested until at least part of the other is written (p. 92). The rule is [[circular-dependency]].
- **Treating class data as global data.** A careful programmer may avoid class fields for fear of the problems of globals; the book answers that class data is far safer, since direct access is limited to a few methods of the class, which know of each other. Its condition: the classes are small and well designed; in huge classes with dozens of methods the difference fades and class data takes on many faults of global data (p. 92). The test is [[class-data-versus-global-data]].
- **Perceived performance cost.** At the architecture level hiding and performance do not conflict; at the code level the worry that indirection costs time is premature: «Эти волнения преждевременны.» (p. 93) Until the system is measured and the bottlenecks found, modular design is the best preparation for optimising, because a hot spot can then be tuned inside one class (p. 93).

## Evidence the book cites

The book reports a study finding large programs that use information hiding four times easier to modify than those that do not (Korson and Vaishnavi, 1986; p. 93). This wiki records the figure as the book's citation and has not checked the study.

## Neighbours

This wiki reads information hiding as the reason behind encapsulation, and places it close to [[coupling]], since a module that hides more leaks less into its callers. The book also says thinking in *responsibilities* is close to asking what to hide but may yield more general answers (p. 103). This wiki reads [[dry]] as overlapping and distinct: DRY asks whether the same knowledge is stated twice, information hiding asks whether a decision is visible where it need not be, which can be true with no repetition at all (a primitive type compared with `<` at every site). [[logic-testable-without-ui]] applies it between logic and presentation.

## Source

[[code-complete]], ch. 5, section 5.3, Russian edition, pp. 89-94, 96, 103. This wiki's own: the reading of information hiding as the reason behind encapsulation and its closeness to coupling, the distinction from DRY, and the links to rule pages.
