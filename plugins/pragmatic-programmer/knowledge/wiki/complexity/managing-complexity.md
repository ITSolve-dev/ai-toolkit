---
title: Managing complexity
category: complexity
summary: "Concept: the primary technical goal of design is that a reader can change one part while safely ignoring most others; code that forces many parts into mind at once fails it, whatever the local code looks like."
tags: [concept, complexity, essential-complexity, accidental-complexity, abstraction]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

**Managing complexity** is, in McConnell's *Code Complete*, the primary technical imperative of software development: every other technical goal of design is subordinate to it. He grounds it in Brooks's split between **essential** complexity (the properties a problem must have to be that problem) and **accidental** complexity (properties it happens to carry: awkward syntax, batch-only machines, poorly integrated tools) (pp. 74-75).

## The claim

McConnell writes: «Управление сложностью — самый важный технический аспект разработки ПО» (p. 75). When projects fail for a technical reason, the reason is usually complexity nobody controls: no one can fully predict how a change in one fragment will affect the others, and progress stops (p. 75, paraphrase).

The reasoning, after Dijkstra, is that no human mind holds all the details of a modern program, so programs must be organised so that one can work safely on one fragment at a time. The goal is «минимизация объема программы, о котором нужно думать в конкретный момент времени» (p. 76). McConnell likens it to mental juggling: the more balls the program keeps in the air, the likelier a dropped one becomes a defect (p. 76, paraphrase).

## A two-part approach

McConnell proposes two moves (p. 77):

- minimise the amount of **essential** complexity anyone has to deal with at a given time;
- «сдерживайте необязательный рост несущественной сложности» (p. 77), that is, keep **accidental** complexity from proliferating.

He names three typical failures: a complex solution to a simple problem, a simple but wrong solution to a complex problem, and an inappropriate complex solution to a complex problem (p. 76, paraphrase).

## The test it gives for a design

Under the characteristic "minimal complexity", McConnell gives a test that can be put to code: «Если при работе над отдельным фрагментом программы проект не позволяет безопасно игнорировать большинство остальных фрагментов, он неудачен» (p. 77). He also warns against "clever" designs, which are usually hard to understand (p. 77).

This wiki reads that test as the operational core of the concept: to edit one routine or class, does the reader have to open and understand most of its neighbours? If so, the design is leaking complexity, whatever the local code looks like. The rule pages that turn the test into countable signs are listed below.

## Tools the source names

- The book also names splitting a system into subsystems at the architecture level (p. 76). This wiki takes the architecture as given by the project and has no page prescribing it; the tools below act inside a module.
- Well-defined objects separate concerns so they can be solved one at a time; packages do the same at a higher level (p. 76). See [[information-hiding]].
- Keep routines short; write in terms of the problem domain rather than low-level implementation details; work at the highest level of abstraction available (p. 76). See [[program-close-to-the-domain]].
- Limit how many others a class or routine uses: [[limit-fan-out]].
- Leave out what is not needed: [[minimal-but-complete-functionality]], and reuse what exists: [[use-existing-components-before-writing-your-own]].

The sidebar quotation from Hoare frames the same choice: a design can be so simple that it obviously has no deficiencies, or so complex that it has no obvious deficiencies (p. 75, paraphrase).

## The closing chapter's restatement

Chapter 34 returns to the imperative as the main goal of design and construction, and probably the most important condition of effective programming (pp. 817-819). Its reasoning is cognitive: nobody's mind can span nine orders of magnitude of detail, so the job is to arrange code so that a person works on a small part at a time (p. 818). It lists the tools, each named by what it saves the reader from holding in mind (p. 818):

- subsystems at the architecture level, to focus on a smaller part at a time (a setting here, not a rule of this wiki);
- carefully defined class interfaces, so internals can be ignored, and keeping the abstraction the interface forms ([[class-interface-coherent-abstraction]]);
- avoiding global data, which sharply raises how much code must be kept in mind at once ([[global-data]]);
- avoiding deep inheritance ([[deep-inheritance-hierarchy]]), deep nesting of loops and conditionals ([[tame-deep-nesting]], [[loop-length-and-nesting]]) and `goto` ([[goto-as-last-resort]]);
- one deliberately chosen approach to error handling instead of an arbitrary mix, with exceptions used systematically ([[consistent-error-handling-strategy]]);
- classes that do not grow into monsters the size of whole programs ([[class-size]]), and short methods ([[routine-length]]);
- clear names, so the reader does not ask whether `i` is the account index and `j` the client index or the reverse;
- few parameters, or more importantly only those the method's abstraction needs ([[limit-parameter-count]], [[pass-what-the-routine-uses]]);
- conventions, so arbitrary differences between fragments need not be remembered ([[coding-conventions]]).

All of this, in the book's words, fights accidental complexity (p. 818).

On p. 818 the book gives three examples of simplification: a boolean function naming the essence of a complex test ([[name-complex-conditions]]), a table lookup in place of a chain of logic ([[drive-repeated-dispatch-from-a-table]]), and a consistent class interface. On p. 819 it names abstraction as an especially powerful means and gives two ways to raise it: names that answer the problem-level "what" rather than the implementation-level "how", and named constants in place of literals ([[named-constants-over-literals]]). Of the naming example the book admits the gain is small, but against a range of 1 to 10^9 every step counts (p. 819). The structural form of the same idea is [[high-level-code-in-problem-terms]]; the scan for where complexity has already got out of hand is [[design-warning-signs]]; readability as the reader's side of it is [[code-for-the-reader]].

The book also claims object-oriented programming gives a level of abstraction covering algorithms and data together, which functional decomposition alone cannot (p. 819). This wiki reads that comparison as against decomposition into procedures, not against functional programming as a paradigm.

## Limits

This wiki's own note: the concept does not license removing **essential** complexity. A domain with many genuine rules and exceptions produces code with many branches, and hiding them in a framework or configuration does not reduce them; it moves them (see [[over-configuration]]). The question is whether the reader must hold them **all at once**.

## Source

[[code-complete]], ch. 5, section 5.2, Russian edition, pp. 74-77, and ch. 34.1, pp. 817-819, with the key points on p. 833. The Brooks and Dijkstra arguments are McConnell's retelling. The reading of the test as the concept's operational core, the scoping of the OOP claim to procedural decomposition, the links to rule pages, the treatment of the book's subsystem advice as a setting outside this wiki's scope, and the note on essential complexity under *Limits* are this wiki's own.
