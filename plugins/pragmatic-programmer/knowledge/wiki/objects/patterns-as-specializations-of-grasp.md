---
title: Design patterns as specializations of GRASP principles
category: objects
summary: "Concept: each GoF pattern pays for an indirection with protection from one named variation (Adapter from varying interfaces, Strategy from changing algorithms, Observer from the number and class of listeners); judging a pattern in code means asking whether that variation is present."
tags: [concept, grasp, gof, design-patterns, protected-variations, indirection, polymorphism]
paradigm: oop
sources: [larman-applying-uml-and-patterns]
created: 2026-11-07
updated: 2026-11-07
---

Larman's claim in chapter 26 is that "Most design patterns can be seen as specializations of a few basic GRASP principles". Studying the underlying themes ("Protected Variations, Polymorphism, Indirection, …") helps "cut through the myriad details and see the essential 'alphabet' of design techniques being applied" (26.2, p. 603). He gives the motivation as pattern overload: the Pattern Almanac 2000 lists around 500 patterns, and few people can learn or remember that many (p. 603). The general idea of a pattern is [[design-pattern]].

## The mapping in this chapter

Larman states each pattern's GRASP basis, mostly in its "Related Patterns" note (Factory's in its solution, p. 606; Adapter's in 26.2, p. 603):

| Pattern | Builds on | Protects against |
|---|---|---|
| Adapter, see [[hide-third-party-apis]] | Indirection, Polymorphism, interfaces | varying external interfaces |
| [[factory-object-for-creation]] | Pure Fabrication, High Cohesion | a changing implementation class (when data-driven) |
| [[strategy-for-varying-algorithms]] | Polymorphism, interfaces | changing algorithms |
| [[composite-same-interface-as-part]] | Polymorphism | whether related objects are atomic or composite |
| [[facade-single-entry-point]] | Indirection, Low Coupling | changes in a subsystem's implementation |
| [[observer-publisher-knows-only-interface]] | Polymorphism, interfaces | the class and number of the notified objects |

He also shows patterns combining, for example "Adapters generated from a Singleton Factory" (26.6, p. 612), strategies created by a factory, and composites of strategies. He presents the whole external-services design as reasoning from "Controller, Creator, Protected Variations, Low Coupling, High Cohesion, Indirection, Polymorphism, Adapter, Factory, and Singleton" (p. 612), and admits that "This design may not be ideal" (p. 612). The GRASP principles themselves are on [[protected-variations]], [[pure-fabrication]], [[low-coupling]], [[cohesion]], [[polymorphism-or-type-switch]], [[controller]] and [[creator]].

## Why it matters for judging code

This wiki reads the mapping as a test. Each pattern in the table is a form of [[protected-variations]]: it pays for an indirection with protection from one named variation. When the code in front of the reader shows no such variation (one vendor, one algorithm, one listener, a group with one class), the pattern's cost remains and its benefit does not. This is the shared root of the "When not to apply" sections on the pattern pages; the sign itself, pattern roles with one occupant, is owned by [[do-not-force-a-design-pattern]]. The reading is this wiki's extension of Larman, who argues the mapping for learning and communication, not as a criterion against use.

Larman makes the communication point too: shared pattern names let a designer be succinct, "raising the level of abstraction in design communication" (26.6, p. 612). The guideline to put the pattern name in a type name, as in `TaxMasterAdapter` (26.1, p. 602), follows from it.

## Source

Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 26.2, 26.4 (Factory's solution, p. 606), 26.6 and the Related Patterns notes of 26.1-26.10, PDF pp. 602-637. The specialization claim, the motivation, the per-pattern relations, the combinations and the communication point are Larman's. Reading the mapping as a criterion against unneeded patterns, and the routing of its sign to [[do-not-force-a-design-pattern]], are this wiki's own.
