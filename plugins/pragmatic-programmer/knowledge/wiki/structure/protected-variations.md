---
title: Protected Variations
category: structure
summary: "Concept: find the points of predicted variation or instability and put a stable interface around them; information hiding, the open-closed principle, polymorphism, indirection and the Law of Demeter are forms of it; at a speculative evolution point protection can cost more than reworking a simple design, and this wiki routes that call to replaceable-code-over-forecast."
tags: [concept, grasp, protected-variations, information-hiding, open-closed, indirection]
paradigm: any
sources: [larman-applying-uml-and-patterns]
created: 2026-11-07
updated: 2026-11-07
---

**Protected Variations (PV)** is the GRASP principle under most of the others: "Identify points of predicted variation or instability; assign responsibilities to create a stable interface around them" (25.4, p. 592). "Interface" here means an access view in the broadest sense, not only a language's `interface` construct (p. 592). Larman calls it "a very important, fundamental principle of software design" and says data encapsulation, polymorphism, interfaces, configuration files and much more are specializations of it (p. 592).

## What it says

Code that depends on something likely to change should depend on a stable surface in front of it, not on the changing thing. In Larman's tax example the variation is the differing APIs of external tax calculators. Internal code talks to one `ITaxCalculatorAdapter`, and each adapter hides one API: "Internal objects collaborate with a stable interface; the various adapter implementations hide the variations to the external systems" (p. 592). That case is worked on [[hide-third-party-apis]].

## Mechanisms inside a module

Larman lists many mechanisms. These are the ones that work at the level of classes and functions:

- **Data encapsulation**: private fields behind methods.
- **Polymorphism and interfaces**: see [[polymorphism-or-type-switch]].
- **Indirection**: GRASP **Indirection** says to "Assign the responsibility to an intermediate object to mediate between other components or services so that they are not directly coupled" (25.3, p. 590). Adapter, Facade and Observer are examples ([[hide-third-party-apis]], [[facade-single-entry-point]], [[observer-publisher-knows-only-interface]]). Larman quotes Wheeler's adage and its counter-adage: "Most problems in performance can be solved by removing another layer of indirection!" (p. 591, fn. 3). This wiki reads the counter-adage as the cost side: each intermediary is a hop a reader has to follow, and it earns its place only by hiding a real variation.
- **Substitutability**: see [[liskov-substitution-principle]].
- **Structure hiding**: the Law of Demeter, see [[train-wreck]] and [[hide-delegate-or-remove-middle-man]].
- **Uniform access**: in languages where a field read and a method call look the same, a field can become a method without touching clients (p. 593). See [[uniform-access]].

Larman also lists data-driven designs, service lookup, interpreters, reflection, virtual machines and standard languages (pp. 593-594). This wiki leaves those out: they are mostly system or architecture-level choices, which the charter puts outside its scope.

## Information hiding and the open-closed principle

Larman treats PV as "essentially the same as the information hiding and open-closed principles" (p. 597).

- **Information hiding** in Parnas's original sense means hiding *design decisions* that are difficult or likely to change, not just data. Larman quotes Parnas: "that one begins with a list of difficult design decisions or design decisions which are likely to change. Each module is then designed to hide such a decision from the others" (p. 598). Larman says that reading it as a synonym for data encapsulation is a misreading, and that data encapsulation "is but one of many techniques to hide information about the design" (p. 598). This wiki draws the consequence: getters and setters around every field do not by themselves hide anything, because callers may still depend on the representation the accessors expose. The concept page is [[information-hiding]]; the method for listing the likely changes is [[anticipate-likely-changes]].
- **Open-Closed (Meyer)**: "Modules should be both open (for extension; adaptable) and closed (the module is closed to modification in ways that affect clients)" (p. 598). Larman's reading is that "closed with respect to X" means clients are not affected if X changes. A class with private fields is closed with respect to its field definitions and open to changing them (p. 598). In OCP, "module" covers methods and classes as well.

## Limits

Larman applies PV to both *variation points* (variation present in today's requirements) and *evolution points* (speculative future variation), and warns that at the second "the cost of engineering protection at evolution points can be higher than reworking a simple design" (p. 597). This wiki gives that decision to [[replaceable-code-over-forecast]], with pattern scaffolding that has one occupant on [[do-not-force-a-design-pattern]] and a single-subclass base on [[base-class-with-one-subclass]]. How the GoF patterns of chapter 26 specialize PV is [[patterns-as-specializations-of-grasp]].

## Source

- Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]]: 25.3 Indirection (PDF pp. 590-591) and 25.4 Protected Variations (PDF pp. 592-598).
- This wiki's own: the selection of mechanisms that work at module level, the cost reading of the counter-adage, the remark about accessors on every field, and the routing of the evolution-point limit to neighbouring pages.
