---
title: Design heuristics for construction
category: structure
summary: "Checklist to run while designing a class, and against an existing one: find the objects, form consistent abstractions, hide secrets (one sentence names the class's secret), isolate likely change, keep coupling loose; for review, decomposition into classes and methods, minimal interaction, complete but minimal, standard techniques."
tags: [method, design, heuristics, checklist, information-hiding, coupling]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell's premise is that design is not deterministic, so good design comes from skilful use of heuristics, which he likens to rules for the trials of trial and error; each is judged against managing complexity, which he calls the primary technical imperative of software (p. 84; see [[managing-complexity]]). This page is the procedure his section adds up to; the pages it links hold the rules.

## The core heuristics, in the book's order

1. **Find real-world objects.** For each: its attributes, the operations on it, what it does to other objects (containment and inheritance), which of its parts are public and private, and its public interface; iterate rather than follow the order strictly (pp. 84-86). The book warns that a one-to-one match with real-world objects may not be the best final choice, but is a good start (p. 85). For inherited classes also design the *protected* interface (p. 86).
2. **Form consistent abstractions** at routine and class level: [[abstraction]], [[abstract-data-type]].
3. **Encapsulate implementation details**: [[abstraction]].
4. **Inherit when it simplifies the design**: [[choose-an-alternative-to-inheritance]].
5. **Hide secrets** — ask «Что мне скрыть?» (p. 94): [[information-hiding]], [[hide-secrets-behind-one-access-point]].
6. **Identify areas likely to change**: [[anticipate-likely-changes]].
7. **Keep coupling loose**: [[coupling]], [[semantic-coupling]].
8. **Look for a common design pattern**: [[do-not-force-a-design-pattern]].

## The minor heuristics

The book lists these as less useful but worth mentioning (pp. 102-105):

- aim for strong [[cohesion]];
- build hierarchies, which do not remove details but push them to another level (p. 103);
- formalise class contracts as preconditions and postconditions: [[design-by-contract]];
- assign responsibilities, which the book says is close to asking what to hide but may give more general answers (p. 103);
- design for test: ask how the system would look if built to be easy to test (p. 103). The book's examples there are architectural, separating the user interface and limiting dependencies between subsystems, which this wiki takes as given; it keeps the class-level consequence the book names, more formal class interfaces (p. 103);
- avoid failure: consider how the design could fail rather than only copying past successes (p. 103);
- choose [[binding-time]] consciously;
- make central points of control, Plauger's One Right Place (p. 104): [[hide-secrets-behind-one-access-point]];
- consider brute force: «Работоспособное решение проблемы методом грубой силы лучше, чем элегантное, но не работающее решение.» (p. 104) The book's example is binary search, first published in 1946 and correct for lists of every size only 16 years later, while sequential search is often acceptable (p. 104); see [[fastest-algorithm-is-not-always-best]];
- draw diagrams;
- keep the design modular, each routine or class a black box whose output is predictable from its input (p. 104).

## When a design will not settle

If an acceptable class interface does not come at first, try again until it stabilises, and if it does not, try a different approach (p. 90; more approaches on p. 106). For decomposition see [[top-down-and-bottom-up-design]].

## Running it against existing code

This wiki's use in review: for a class under review, state its secret in one sentence; if no sentence fits, or two do, the class fails step 5 before any finer rule applies.

The chapter's checklist of design goals (p. 119) can also be run against code that exists. This wiki keeps the questions that concern code inside a module; those about architecture (problems deferred from it, layering, decomposition into subsystems and packages, subsystems reused in other systems) are out of its scope and taken as given. A "no" points to the page that owns the sign:

1. **Is the decomposition into classes satisfactory?** Look for one purpose per class: [[cohesion]], [[class-interface-coherent-abstraction]].
2. **Is the decomposition of classes into methods satisfactory?** Look at method size and single purpose: [[routine-length]], [[routine-cohesion]].
3. **Is interaction between classes minimal?** Count collaborators and how wide the calls between them are: [[coupling]], [[limit-fan-out]]. Whether a class depends on its application's context where it need not: [[do-not-rely-on-unguaranteed-context]], which this wiki does not read as a demand for speculative generality ([[replaceable-code-over-forecast]]).
4. **Is it complete but minimal? Is every part needed?** Look for unused parameters, unused classes and wrappers that only forward calls: [[minimal-but-complete-functionality]], [[know-when-to-stop]].
5. **Does it use only standard techniques, avoiding exotic, hard-to-understand elements?**
6. **Does it reduce both essential and accidental complexity?** The key points name two ways to simplicity: minimise how much essential complexity anyone faces at once, and stop accidental complexity growing needlessly (p. 120): [[managing-complexity]].

The practices part of the checklist adds one question that can be checked on code: has the design been taken to the point where implementing it seems obvious (p. 119)?

The book calls design heuristic: blind adherence to one methodology suppresses creative thinking and lowers the quality of programs (p. 120), and it quotes Plauger: «чем догматичнее вы будете в отношении методики проектирования, тем меньше реальных проблем решите» (p. 116). This wiki reads that as a limit on the checklist itself: a "no" is a prompt to open the owning page, not a finding, and a design may be judged fine as it is.

## Source

[[code-complete]], section 5.3, Russian edition, pp. 84-106; the chapter checklist and key points, pp. 116, 119-120. The ordering, lists and checklist questions are the book's. This wiki's own: the one-sentence secret test, the selection of in-module checklist questions, what to look at for each and the links to owning pages, and the reading of p. 120 as a limit on the checklist.
