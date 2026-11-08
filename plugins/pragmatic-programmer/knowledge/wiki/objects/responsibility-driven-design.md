---
title: Responsibility-driven design
category: objects
summary: "Concept: deciding which class a method belongs to by first naming the responsibility it carries out (a doing or a knowing) and then giving that responsibility to a class; a method is judged by the responsibility it fulfils, not by its name; a class named after a human role is judged by whose data its steps use, not by what the person does. The frame under the GRASP pages."
tags: [concept, responsibilities, grasp, rdd]
paradigm: oop
sources: [larman-applying-uml-and-patterns]
created: 2026-11-07
updated: 2026-11-07
---

**Responsibility-driven design (RDD)** treats object design as assigning *responsibilities* to collaborating objects. A responsibility is an abstraction of what an object does or knows, and methods carry it out. Larman takes the frame from Wirfs-Brock and McKean and uses it as the backbone of GRASP, a set of named principles for deciding which class gets which responsibility (17.3-17.4, pp. 416-418).

## Two kinds of responsibility

Larman, following the UML, defines a responsibility as "a contract or obligation of a classifier" (17.3, p. 416). He splits responsibilities into two kinds:

- **Doing:** doing something itself (creating an object, calculating), starting action in other objects, and controlling and coordinating other objects.
- **Knowing:** knowing its private encapsulated data, knowing related objects, and knowing what it can derive or calculate.

His examples: a Sale being responsible for creating its SalesLineItems is a doing, and a Sale being responsible for knowing its total is a knowing (p. 416).

## A responsibility is not a method

Larman says a responsibility is not the same thing as a method but an abstraction, and that "methods fulfill responsibilities" (17.3, p. 417). Granularity varies widely: providing access to relational databases may take hundreds of classes, while creating a Sale may take one method (pp. 416-417). A responsibility is usually met through **collaboration**: `Sale.getTotal` asks each line item for its subtotal (p. 417).

This wiki reads the consequence for code this way: a method is judged by the responsibility it carries out, not by its name. A method named `getTotal` on `Sale` that pulls the line items' fields and multiplies them itself has taken the line items' knowing responsibility. That shape is [[information-expert]].

## The domain model as a hint for knowing responsibilities

Larman's guideline is that the attributes and associations of the domain model often suggest the knowing responsibilities: if the domain concept `Sale` has a time, the software `Sale` knows its time. This keeps a "low representational gap" between how people think of the domain and the classes (p. 416). He gives the same reason for naming classes `Square` and `Board` rather than opaque codes (17.8, p. 424).

Modelling the business domain itself is out of this wiki's scope and belongs to `domain-driven-guide`. This page keeps only the role the hint plays in placing a method. The hint has a limit Larman states himself, set out in the next section.

## Software objects are not people

An object design is not a one-to-one simulation of how people in the domain act. Larman's warning is that a guideline to put responsibilities in software objects as they are assigned to people would, in the point-of-sale domain, leave a Cashier software object doing almost everything, which violates High Cohesion and Low Coupling: "Big fat objects" (18.5, p. 501). Responsibilities are instead distributed among many objects by [[information-expert]] (p. 501).

The person-named class can still win, for a different reason. In Monopoly, Player ends up taking the turn, and Larman stresses that the choice "will be by Expert, not inspiration from how humans behave" (18.5, p. 501): Player holds the cash and the strategy data the turn needs (pp. 501-502). The same goes for counts: a real store has many registers, while the software Store creates one because the requirements need one (18.4, p. 497).

This wiki reads the point as a check on reasoning, not a ban on names. A class for a human role is right when the data its behaviour needs really is that person's (a balance, permissions, preferences); it is wrong when it took a step only because a person performs that step. The domain model hints at *knowing* responsibilities; the limit is on *doing* responsibilities copied from human activity.

The shape the copying produces is a class named after a human actor or role whose methods cover most of a use case's steps (scan item, compute total, take payment, print receipt), while the objects it works on (`Sale`, `LineItem`, `Payment`) are plain data holders with getters. That shape is not owned here:

- a class that reads and decides for several data-only classes is [[god-class]];
- where the role class is the one that receives the program's incoming requests or system operations, [[controller]] owns it;
- a single computation pulled out of another class's data is [[information-expert]].

The repair on each of those pages is the same move: give each computation to the class whose data it uses, and leave the role class with its own data and with coordination.

## GRASP as a learning aid

Larman calls GRASP "a learning aid" for applying design reasoning in a methodical, rational, explainable way; once the fundamentals are grasped, the specific names "aren't important" (17.4, p. 418). In his usage a pattern is a named problem/solution pair with advice on applying it and its trade-offs (17.6, p. 420). The GRASP patterns "don't state new ideas; they name and codify widely used basic principles" (p. 421).

This wiki reads the practical use as follows: the name lets a review finding say *why* a method belongs elsewhere, and the reason (coupling, cohesion) carries more weight than the label.

The GRASP pages in this wiki:

- [[information-expert]]: who computes or knows something
- [[creator]]: who calls `new`
- [[controller]]: who receives a system operation behind the UI
- [[low-coupling]]: comparing two placements by what they make depend on what
- [[cohesion]]: Larman's High Cohesion scale and its contraindications
- [[pure-fabrication]]: when the information expert is the wrong home
- [[polymorphism-or-type-switch]]: behaviour that varies by type
- [[protected-variations]]: a stable interface around a point of variation

## Source

- Larman, *Applying UML and Patterns*, 3rd ed., 17.3-17.6 and 17.8, PDF pp. 416-424, via [[larman-applying-uml-and-patterns]].
- Larman, 18.4, PDF p. 497, and 18.5 "Who Takes a Turn?", PDF pp. 501-502: the Cashier case (given in prose only), Player chosen by Expert, one software Register.
- This wiki's own: the reading of a misplaced `getTotal` as a misplaced knowing responsibility, the reading of what the GRASP names are for in review, the reading of the person-named class as a check on reasoning rather than on names, the split between knowing and doing responsibilities, the code shape of copied human duties and its assignment to owner pages.
