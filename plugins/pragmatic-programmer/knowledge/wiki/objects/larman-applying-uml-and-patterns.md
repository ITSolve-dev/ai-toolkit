---
title: Applying UML and Patterns (Larman), GRASP and GoF chapters
category: objects
summary: "Source page, no rules of its own: the GRASP and GoF chapters of Larman's textbook (17, 18, 25, 26, 35), which teach assigning responsibilities to objects by nine named principles (Expert, Creator, Controller, Low Coupling, High Cohesion, Polymorphism, Pure Fabrication, Indirection, Protected Variations) and then read the GoF patterns as their specializations, on the NextGen POS and Monopoly case studies."
tags: [summary, objects, larman-applying-uml-and-patterns]
sources: [larman-applying-uml-and-patterns]
created: 2026-11-07
updated: 2026-11-07
---

Craig Larman's *Applying UML and Patterns* is a textbook on object-oriented analysis and design taught through iterative development. This base holds only the chapters on object design: 17 (GRASP), 18 (object design examples with GRASP), 25 (the remaining GRASP principles), 26 (GoF patterns) and 35 (more object design with GoF patterns).

## Edition and authority

Edition read: the English e-book of the 3rd edition, 2004. The extracted chapters carry no imprint, so the publisher named in `SCHEMA.md` (Addison-Wesley) is not confirmed from `raw/`. The e-book has no printed page numbers: pages cite the section number and the PDF page from the `<!-- p. N -->` markers. Quotations are in English and were checked against `raw/`.

The book argues from worked design of two case studies (the NextGen point-of-sale system and a Monopoly game) and from the literature it cites (the GoF, Parnas, Meyer, Liskov, Coad, Wirfs-Brock), not from measurement. It is an introductory textbook, and Larman says so of its own vocabulary: GRASP is "a learning aid to help you understand essential object design and apply design reasoning in a methodical, rational, explainable way" (17.4, PDF p. 418), and once the fundamentals are grasped "the specific GRASP terms (Information Expert, Creator, …) aren't important" (p. 418).

## Thesis

- Object design is the assignment of responsibilities, knowing and doing, to classes, and it can be reasoned about rather than guessed ([[responsibility-driven-design]]).
- "There are nine GRASP patterns" (17.9, PDF p. 435): [[creator]], [[information-expert]], [[low-coupling]], [[controller]], High Cohesion ([[cohesion]]), Polymorphism ([[polymorphism-or-type-switch]]), [[pure-fabrication]], Indirection and [[protected-variations]] (Indirection is treated on [[protected-variations]]).
- The GoF patterns are specializations of these principles: each pays for an indirection with protection from one named variation, Adapter for instance resting on Indirection and Polymorphism against varying external interfaces ([[patterns-as-specializations-of-grasp]]).
- There is no single best design; the case studies show that design "can be reasoned through by core principles such as low coupling and the application of patterns", and he warns against "pattern-itis" (35.10, PDF p. 818; [[do-not-force-a-design-pattern]]).

## Scope and limitations

- Only five chapters were extracted. The rest of the book (requirements, domain modelling, UML notation, the Unified Process, architecture and layers) is outside this charter: analysis and domain modelling belong to `domain-driven-guide`, architecture is taken as given.
- The case studies sit inside a layered architecture with a UI layer, a domain layer and technical services. The pages name that as a setting and do not prescribe it ([[controller]], [[hide-third-party-apis]]).
- Several GoF solutions use a Singleton plus reflection for factories and services. This wiki keeps the pattern and records that refinement as the source's choice against [[no-singletons]] and [[global-data]] ([[abstract-factory]], [[factory-object-for-creation]]).
- Many of the book's examples are UML diagrams that `raw/` does not reproduce. The pages' pseudocode is this wiki's own, and where a figure carried a detail (a formula, a message order) the page says it was invented or inferred.
- The book states almost no signs in code and few limits. Its contraindications, such as Do It Myself being "often contraindicated due to problems in coupling and cohesion" (35.8, PDF p. 808), are kept as limits on the owning pages.

## Key takeaways

This wiki reads the chapters as making five claims that change code:

1. **Give a responsibility to the class that holds the information, unless that couples it to something unstable or breaks its cohesion.** [[information-expert]], [[creator]], [[tell-dont-ask]], [[keep-objects-small]], [[class-with-only-data-or-only-behaviour]], [[responsibility-driven-design]].
2. **A system operation enters through a controller that coordinates and delegates.** [[controller]], [[god-class]], [[command-query-separation]].
3. **Coupling and cohesion decide between placements, and a made-up class takes what no domain class should own.** [[low-coupling]], [[coupling]], [[cohesion]], [[pure-fabrication]], [[hide-delegate-or-remove-middle-man]], [[train-wreck]].
4. **Variation is handled by polymorphism behind a stable interface, at the points where it actually varies.** [[polymorphism-or-type-switch]], [[protected-variations]], [[liskov-substitution-principle]], [[replaceable-code-over-forecast]], [[shared-behavior-in-superclass-varying-step-polymorphic]].
5. **The GoF patterns are those principles applied to recurring problems.** [[patterns-as-specializations-of-grasp]], [[hide-third-party-apis]] (Adapter), [[factory-object-for-creation]], [[abstract-factory]], [[strategy-for-varying-algorithms]], [[composite-same-interface-as-part]], [[facade-single-entry-point]], [[observer-publisher-knows-only-interface]], [[proxy]], [[no-singletons]] (Singleton), [[do-not-force-a-design-pattern]].

## Pages by chapter

- Ch. 17 (GRASP): [[responsibility-driven-design]], [[creator]], [[information-expert]], [[low-coupling]], [[coupling]], [[controller]], [[cohesion]], [[god-class]].
- Ch. 18 (examples with GRASP): [[controller]], [[creator]], [[information-expert]], [[low-coupling]], [[command-query-separation]], [[responsibility-driven-design]], [[god-class]].
- Ch. 25 (more GRASP): [[polymorphism-or-type-switch]], [[tell-dont-ask]], [[liskov-substitution-principle]], [[pure-fabrication]], [[class-with-only-data-or-only-behaviour]], [[protected-variations]], [[replaceable-code-over-forecast]], [[hide-delegate-or-remove-middle-man]], [[train-wreck]].
- Ch. 26 (GoF): [[patterns-as-specializations-of-grasp]], [[hide-third-party-apis]], [[factory-object-for-creation]], [[no-singletons]], [[strategy-for-varying-algorithms]], [[composite-same-interface-as-part]], [[pass-what-the-routine-uses]], [[ids-to-objects]], [[facade-single-entry-point]], [[observer-publisher-knows-only-interface]].
- Ch. 35 (more GoF): [[proxy]], [[fault-error-failure]], [[exception-at-the-interface-abstraction]], [[name-exceptions-after-the-problem-not-the-thrower]], [[abstract-factory]], [[information-expert]] (Do It Myself), [[keep-objects-small]], [[polymorphism-or-type-switch]], [[shared-behavior-in-superclass-varying-step-polymorphic]], [[do-not-force-a-design-pattern]].

## Where it disagrees with the other sources

The owning page resolves the disagreement per setting.

- **Singleton.** Larman uses it for factories and service access; *Elegant Objects* bans it. [[no-singletons]].

## Source

Larman, *Applying UML and Patterns*, 3rd ed., English e-book, 2004, chapters 17, 18, 25, 26 and 35, cited by section and PDF page. The reading of the chapters as five claims, the grouping of pages under them and the summary of the disagreement are this wiki's own.
