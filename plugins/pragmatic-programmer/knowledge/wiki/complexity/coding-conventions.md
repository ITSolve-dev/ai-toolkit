---
title: Coding conventions as complexity control
category: complexity
summary: "Concept: code where the same kind of arbitrary decision (error reporting, resource handling, interface shape, constant marking) is made differently in each place, such as units of one kind each exposing their own ad-hoc public methods or one invariant checked in several ad-hoc forms where the language lacks an assertion helper, or a review proposing a new convention for a question the code already answers one way; a convention earns its place only by settling a question that is arbitrary but answered inconsistently."
tags: [concept, conventions, consistency, complexity, predictability]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell treats a set of conventions as one of the intellectual tools for managing complexity (p. 824; see [[managing-complexity]]). Many programming questions are arbitrary and have no single right answer: «Конкретный ответ на такой вопрос менее важен, чем его согласованность.» (p. 824). Conventions spare programmers from answering the same questions again and again, and in a team they prevent the confusion that comes when different programmers decide differently (p. 824).

Formatting conventions are mechanical style and out of this wiki's scope, because tooling catches them. This page keeps what conventions do for the design-level reading of code. Naming conventions have their own page, [[naming-conventions]].

## What a convention buys, per the source

- **It frees attention.** Standardising decisions on formatting, loops, variable names and modelling notation frees mental resources for the harder parts of programming (p. 819). People argue most fiercely about the smallest differences, the book observes; conventions are most useful when they free you from making and defending unimportant decisions, and least useful when they constrain more important areas (p. 819).
- **It carries information concisely.** One naming character can separate local, class and global variables, and letter case can mark types and constants (p. 824).
- **It guards against known hazards.** «Соглашения защищают от известных опасностей.» (p. 824). A convention can forbid a dangerous technique, restrict it to the cases that need it, or compensate for its known weaknesses. The book's examples are banning global variables, parenthesising complex expressions, and nulling pointers after release (p. 824).
- **It makes low-level tasks predictable.** Conventions for memory requests, error handling, input/output and class interfaces add expressive structure and make code easier to follow for anyone who knows them (p. 824). Good conventions let a reader take more for granted, so there are fewer details to hold (p. 824). The error-handling case is [[consistent-error-handling-strategy]]. Chapter 4 shows the interface case: in McConnell's Visual Basic project every form had one public method, `IsFormCompleted()`, so a call to it always meant the same thing (p. 66). This wiki reads the opposite as the sign: units of one kind (forms, views, handlers) each exposing their own ad-hoc public methods, so a caller has to know the particular unit.
- **It compensates for the language.** In a language without named constants, a convention can separate read-write variables from variables that emulate read-only constants (p. 825; see [[program-into-the-language]]). Where the language has no assertions, McConnell's advice is to write your own `assert()` routine (p. 823). This wiki reads the missed case as the sign: the same kind of invariant checked in several ad-hoc forms (print and continue here, exit there, a thrown string in a third) instead of through one helper. Whether an invariant should be an assertion at all is [[assertion-or-error-handling]].

## Cost and failure modes

- **Too many.** On large projects programmers sometimes create so many standards that memorising them becomes a job in itself (p. 825).
- **Too few.** On small projects programmers usually go to the other extreme, because they do not understand what sensible conventions are worth (p. 825).
- **Misused.** In the chapter's key points, a convention used inappropriately is a cure worse than the disease, while one used well adds valuable structure, helps manage complexity and eases communication (p. 833).

The book's guidance is to understand the real value of conventions and use them to structure the areas that lack structure (p. 825). This wiki reads that as a test to run before proposing a convention in a review: does it settle a question that is arbitrary but is currently answered inconsistently in the code in front of you, or does it constrain a decision that should be made case by case? Only the first earns a convention. A codebase that already answers the question one way needs no new convention, and saying so is a valid outcome.

## Source

[[code-complete]], ch. 34.1-34.5, pp. 818-819 and 823-825, with the key points on p. 833; ch. 4.3, p. 66 (the form convention). The benefits, the hazard examples, the too-many and too-few observations, the uniform form interface and the hand-written `assert()` are the book's. The test for whether a convention earns its place, the note that a consistent codebase needs none, the review-proposal sign in the summary, and the two signs read from the form and `assert()` cases (moved here from [[program-into-the-language]]) are this wiki's own.
