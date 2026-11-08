---
title: "Pure Fabrication: when the information expert is the wrong home"
category: objects
summary: "Deciding whether a responsibility stays with the class that owns the data or moves to a made-up class: move it when it brings in operations unrelated to the concept, a technical interface or a task many classes repeat; own sign: a domain method acts on a group it holds and keeps the computed value only in a local (Player rolls and sums the dice inside takeTurn), so the value cannot be had without repeating the action."
tags: [decision-rule, grasp, pure-fabrication, cohesion, coupling, information-expert]
paradigm: oop
sources: [larman-applying-uml-and-patterns]
created: 2026-11-07
updated: 2026-11-07
---

GRASP **Pure Fabrication** answers the case where [[information-expert]], which gives a responsibility to the class holding the data, would make that class incohesive or tightly coupled. The answer: "Assign a highly cohesive set of responsibilities to an artificial or convenience class that does not represent a problem domain concept" (25.2, p. 585). Larman calls this splitting by *behavioral decomposition*, as opposed to *representational decomposition*, where classes mirror domain things (p. 587). He notes that most GoF patterns (Adapter, Strategy, Command) are pure fabrications (p. 588), as is a use-case [[controller]] (17.13, p. 452).

## Rule

This page decides between leaving a responsibility with the data's owner and moving it to a fabricated class. Larman's Sale-in-a-database case gives three reasons to move it (25.2, p. 585):

- **Operations unrelated to the concept.** Saving a Sale "requires a relatively large number of supporting database-oriented operations, none related to the concept of sale-ness".
- **Coupling to a technical interface** rather than to another domain object: the Sale becomes coupled to a particular kind of database interface.
- **A general task many classes need.** Leaving it in one class "suggests there is going to be poor reuse or lots of duplication in other classes that do the same thing".

Leave it with the expert when none of these holds. Larman's contraindication is overuse: Expert "supports the goal of co-locating responsibilities with the objects that know the information needed for those responsibilities, which tends to support lower coupling", and with too many fabrications "functions just become objects" (p. 588). The usual symptom "is that most of the data inside the objects is being passed to other objects to reason with it" (p. 588).

Larman says that labelling a class a Pure Fabrication "is not critical" (p. 588). This wiki reads that as: the page decides where a responsibility goes; it is not a vocabulary to enforce in review.

## Sign in code

The shapes Larman's three reasons produce in code are mostly owned by other pages, and this page supplies the decision behind them:

- Save, load or query methods on a domain class, where the project's convention keeps persistence out of domain classes, are [[delegate-to-services]].
- A vendor's client or query dialect next to business logic is [[hide-third-party-apis]].
- Presentation built inside a class holding business decisions is [[logic-testable-without-ui]].
- The overuse symptom, a field-less `*Service` or `*Calculator`: A field-less class whose methods all take the same one record and read or write only its fields, while the record has only fields or accessors, is [[class-with-only-data-or-only-behaviour]]; where its methods each read and write several data-only classes, [[god-class]] owns it.

This page owns one shape, from Larman's dice example (25.2, pp. 586-587): a method of a domain class acts on a group of objects it holds and computes a value over them in the same loop, keeping the value only in a local, inside a method whose purpose is wider. In Larman's case Player rolls each die and sums the faces inside `takeTurn`, so the summing cannot be reused, and "It is not possible to simply ask for the current dice total without rolling the dice again" (p. 586). The pointable form is the loop that both commands each element and accumulates a result that no field or query exposes afterwards. A loop that commands each element of a group the class holds and accumulates a value kept only in a local is [[pure-fabrication]]; a read-only computation of a derived value from another class's data is [[information-expert]].

## When not to apply

- **The behaviour needs only the domain object's own data and touches no technical API.** Expert then holds, and a fabricated class would only pull data out of its owner, which is the overuse symptom above.
- **The project's architecture already fixes where persistence or I/O lives.** That convention decides, and this wiki only reports a class that contradicts it. The architecture itself is outside this wiki's scope.
- **The group and its total belong to one small class with no other caller of the total.** This limit is this wiki's own: a loop over two fields inside a short method gains nothing from a new class until the total is needed apart from the action.

## Repair

- Where the expert placement is wrong, create a class named after the service it gives (`PersistentStorage`, `Cup`), move the cohesive set of responsibilities into it, and let the domain class drop the technical dependency. Larman still prefers vocabulary close to the domain where one exists, like `Cup` for the dice (p. 587).
- Where fabrication is overused, move each method that reads mostly one object's data back onto that object (see [[information-expert]]), and keep in the fabricated class only what spans objects or touches technical APIs.

## Before and after

```
class Player
    dice: list of Die
    takeTurn()
        total = 0
        for die in dice
            die.roll()
            total = total + die.faceValue()
        move(total)
```

```
class Cup
    dice: list of Die
    roll()
        for die in dice
            die.roll()
    total()
        return sum of die.faceValue() for die in dice

class Player
    cup: Cup
    takeTurn()
        cup.roll()
        move(cup.total())
```

In the "after" the total can be read without rolling again, and `Cup.roll` is a command that returns nothing, so the pair also keeps [[command-query-separation]].

## Source

- Larman, *Applying UML and Patterns*, 3rd ed., 25.2 Pure Fabrication, PDF pp. 585-589, via [[larman-applying-uml-and-patterns]]: the problem, the solution, the Sale persistence and dice Cup examples, representational and behavioral decomposition, GoF patterns as fabrications, the contraindication with its symptom, the remark that the label is not critical.
- This wiki's own: the assignment of the code shapes to owner pages, the wording of the owned sign and its selecting sentence against [[information-expert]], the architecture limit as worded, the small-class limit, and the pseudocode.
