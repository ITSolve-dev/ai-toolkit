---
title: "Creator: the class that contains, records or initializes A creates A"
category: objects
summary: "A class runs `new A(...)` and hands the result straight to another object that stores it, using A for nothing else, so it depends on A only to build it; the part belongs to the object that contains, records or holds the initializing data for it."
tags: [rule, responsibilities, grasp, object-creation, coupling]
paradigm: oop
sources: [larman-applying-uml-and-patterns]
created: 2026-11-07
updated: 2026-11-07
---

**Creator** is the GRASP principle that answers "Who creates an A?" (17.8, p. 425). Creating an object is a doing responsibility (see [[responsibility-driven-design]]), and any class could hold it. Creator says which class should, so that creating the object adds no dependency the design did not already have. Larman counts one of its cases as an application of [[information-expert]], and [[low-coupling]] is the reason under it.

## Rule

Assign class B the responsibility to create instances of A if one or more of these is true, "the more the better" (17.8, p. 425; 17.10, p. 436):

- B "contains" or compositely aggregates A;
- B records A;
- B closely uses A;
- B has the initializing data for A: "B has the initializing data for A that will be passed to A when it is created" (p. 436). Larman says B is then the expert on creating A.

Where several apply, "usually prefer a class B which aggregates or contains class A" (p. 436), and "A composite object is an excellent candidate to make its parts" (p. 438). His examples: a `Board` contains its `Square`s, so it creates them (p. 425); a `Sale` aggregates its line items, so it gets `makeLineItem`, whose parameters carry the quantity and the product so the line is fully initialised at construction (p. 437; 18.4, p. 480). He ties the rule to mental fit: virtually every developer he asked would "Make the Board object create the Squares" (17.8, p. 424).

The reason is coupling. The creator chosen this way is one that needs to be connected to the created object in any event, so the created class is probably already visible to it and the choice adds no coupling (17.10, pp. 437-438).

Larman also gives a rule of order for start-up: "Do the initialization design last" (18.4, p. 494), because what needs creating and wiring is known only once the other operations are designed. The root object is "a class at or near the root of the containment or aggregation hierarchy" (p. 495); it creates its direct parts, which create theirs (pp. 495-496).

## Sign in code

The book states the rule in terms of diagrams. This wiki derives the sign from Larman's Register/Payment case (17.12, pp. 444-445; 18.4, p. 489): one class runs `new A(...)` and immediately hands the result to a second object, which stores it or adds it to a collection. Apart from that handover the first class never touches A, while the second class keeps A's instances or holds the data A is built from. The constructing class names A's type only to construct it.

This wiki assigns the neighbouring cases as follows. Whether the class constructed is a collaborator whose behaviour the constructing object calls, or a part it keeps as its own state, decides between [[creator]] and [[new-only-in-secondary-constructors]]: a collaborator built with `new` inside the class that uses it is [[new-only-in-secondary-constructors]]; where a part or record is constructed, and in which class, is [[creator]]. A plain `new` of one fixed class, with no choice and no setup, is [[creator]] where a part or record is constructed and [[new-only-in-secondary-constructors]] where a collaborator is. A choice among concrete classes, or many lines of construction logic, made in a domain class is [[factory-object-for-creation]]. A dependency added for any other single operation is compared on [[low-coupling]].

## When not to apply

- **Complex creation.** Larman says to delegate creation to a Concrete Factory or an Abstract Factory, not to the class Creator suggests, when creation requires significant complexity: recycling instances for performance, or choosing one class of a family by some external property value (17.10, p. 438).
- **Coupling decides against the Creator candidate.** In Larman's example Creator points at Register, because in the domain a register records payments, while Low Coupling prefers Sale, because Sale must know Payment in any case and Register then needs no knowledge of it (17.12, pp. 444-445). Larman's conclusion is that the two patterns "may suggest different solutions" (p. 445). This wiki reads that as an ordering: among the candidates, the one already coupled to A wins.
- **The constructing class is the one that holds the initializing data**, such as a parser or mapper building objects from input it reads. By the rule's own fourth case it is Creator's candidate; the sign holds only where the receiving class could build A from data passed to it. This limit is this wiki's own.
- **Creation through injection, a factory or a persistence layer.** Larman calls Creator "only a guideline" (p. 437) and notes that product descriptions will later be materialised from a database (18.4, p. 497). This wiki reads that as a limit: where the project creates objects through injection, a factory or a persistence layer, that mechanism decides who instantiates, and Creator speaks only to who requests the creation and keeps the reference. The same holds for parts the caller must choose, such as substitutes injected for tests.

## Repair

Move the `new` into the class that contains A or holds its initializing data, and give that class a method named for the act (`makeLineItem`, `makePayment`) that takes only the raw data. The former constructing class calls this method and drops its dependency on A. If building A needs a choice among classes or pooling, move it into a factory instead.

## Before and after

```
class Register
    makePayment(cashTendered)
        p = new Payment(cashTendered)   // Register keeps no Payment
        currentSale.addPayment(p)
```

```
class Register
    makePayment(cashTendered)
        currentSale.makePayment(cashTendered)

class Sale
    makePayment(cashTendered)
        payment = new Payment(cashTendered)
```

After the change Register no longer names Payment, and Sale, which keeps the payment anyway, builds it. `Payment` is a part Sale keeps, not a collaborator reaching a resource, so the `new` inside `Sale.makePayment` is not a sign of [[new-only-in-secondary-constructors]].

## Source

- Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]]: 17.8, PDF pp. 424-426 (the question, the Board/Square case, mental fit); 17.10, PDF pp. 436-438 (the rule, the preference for the container, the initializing-data case, the factory contraindication, the coupling benefit); 17.12, PDF pp. 444-445 (the Creator/Low Coupling conflict); 18.4, PDF pp. 480, 489, 494-497 (`makeLineItem`, the Payment tie-break, initialisation last, the root object, descriptions from a database).
- This wiki's own: the sign in code, the reading of the conflict as an ordering, the injection limit, the initializing-data limit, the owner split with [[new-only-in-secondary-constructors]], and the pseudocode, which follows Larman's Figures 17.18 and 17.19.
