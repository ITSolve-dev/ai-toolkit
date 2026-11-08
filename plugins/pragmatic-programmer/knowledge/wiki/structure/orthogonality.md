---
title: Orthogonality
category: structure
summary: "One change forces edits in unrelated modules, or a fix here breaks something elsewhere: components are not independent."
tags: [concept, coupling, cohesion, modularity]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

Orthogonality is the book's name for independence between components. The authors borrow the word from geometry, and in computing it has come to mean independence or decoupling: «Два или более компонента считаются ортогональными (не связанными), если изменения в одном из них не оказывают никакого влияния на остальные компоненты системы» (p. 70). Their example is database code orthogonal to the user interface, where each can change or be replaced without touching the other (p. 70).

The book's tip is «Исключайте взаимное влияние несвязанных компонентов системы» (p. 71). The means is a component that is self-contained, independent and has one well-defined purpose (p. 71).

A terminology trap: the Russian edition renders Yourdon and Constantine's *cohesion* as «сцеплением (cohesion)» (p. 71), a word often used for coupling. Here it means cohesion.

## What non-orthogonality looks like

The book's picture is a helicopter, where every control input has side effects on all the others and the pilot must keep compensating (pp. 70-71). Its description of the same thing in a project is a team fighting to make changes, where each change can make things go wrong in four other places (p. 77). If components are highly interdependent, the authors write, a local fix does not exist (p. 71).

## What it gives

Productivity (pp. 71-72):

- Changes are localised, so development and testing time fall. Small self-contained components can be designed, coded, tested and then forgotten.
- Components with well-defined duties can be combined in ways their authors did not foresee.
- Combination multiplies: a component with M distinct operations and one with N give M×N when orthogonal, and fewer when they overlap.

Reduced risk (p. 72):

- Faulty code is isolated, and a bad module is easier to cut out and replace.
- Small changes and fixes stay inside one area.
- The system is easier to test, see [[orthogonality-tests]].
- Interfaces to vendors, products and platforms stay confined to small parts of the system, see [[framework-intrusion]] and [[hide-third-party-apis]].

## How it is kept

The book's coding practices are [[coupling|decoupled]] code that exposes little and does not rely on others' implementations (p. 75), [[global-data]] (p. 75), [[similar-functions-varying-middle]] (p. 75), and continual review of the code's structure, which it calls refactoring (p. 76). Structurally it names layering (pp. 72-73), an architecture this wiki takes as given rather than prescribes, and independence from outside facts, see [[externally-controlled-identifier]] (p. 74).

## Relation to DRY

The authors treat the two as closely related: [[dry]] minimises duplication, and orthogonality reduces interdependence (p. 77). Their chapter opening puts the pair as not duplicating knowledge across systems and not spreading one piece of knowledge across many components (p. 57). This wiki reads them as the same fault seen from two sides, since a fact held in several modules ties those modules together. Both fall under [[easier-to-change]], of which the book calls every design principle a special case (p. 58).

## Limits

A footnote concedes that real requirement changes usually touch several functions. The claim of one module holds per function, as an ideal (p. 73). This wiki therefore reads orthogonality as a direction and not a state that a system reaches.

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation (Dialektika, 2020), chapter opening p. 57 and Topic 10, pp. 69-77, via [[pragmatic-programmer]]. The authors cite Yourdon and Constantine, *Structured Design*. This wiki's own: the reading of DRY and orthogonality as one fault, the final sentence under *Limits*, and the arrangement of the page.
