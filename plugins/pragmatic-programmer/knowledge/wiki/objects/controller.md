---
title: "Controller: the class that receives system operations coordinates, it does not do the work"
category: objects
summary: "The class that receives the program's incoming requests or system operations computes the results itself (loops and arithmetic over domain data, line items and totals in its own fields) instead of delegating, or one such class takes every operation of many unrelated use cases; split per use case or delegate. A UI handler computing business results is logic-testable-without-ui."
tags: [rule, grasp, responsibilities, cohesion, delegation]
paradigm: oop
sources: [larman-applying-uml-and-patterns]
created: 2026-11-07
updated: 2026-11-07
---

**Controller** is the GRASP principle that answers "What first object beyond the UI layer receives and coordinates ('controls') a system operation?" (17.8, p. 431). A *system operation* is an incoming event such as `enterItem`, `endSale` or `playGame` (17.13, p. 448). Larman assumes a separation between UI and domain objects, from Model-View Separation: UI objects "should not contain application or 'business' logic" (17.8, p. 429). Which layer the controller lives in and how the UI reaches it belong to the project's architecture, which this wiki takes as given. This page covers what happens inside the receiving class once that separation exists.

## Rule

Larman's guideline: "Normally, a controller should delegate to other objects the work that needs to be done; it coordinates or controls the activity. It does not do much work itself" (17.13, p. 452). The UI object only adapts the raw event into a meaningful message: the window receiving `actionPerformed` must turn it into something such as `playGame` and delegate it (17.8, p. 430).

He names two kinds of controller (17.8, p. 431; 17.13, p. 448):

- **Facade controller.** One class represents the overall system, a root object, the device the software runs in, or a major subsystem: `Register`, `Store`, `MonopolyGame`.
- **Use-case or session controller.** One class per use case, named `<UseCase>Handler` or `<UseCase>Session`, such as `ProcessSaleHandler`. It handles every event of one scenario, so it can hold the scenario's state and reject out-of-order events, such as `makePayment` before `endSale` (pp. 451, 453). Larman notes that such a class is not a domain object but a [[pure-fabrication]] (p. 452).

The choice between them, in Larman's words: "Choosing a device-object facade controller like Register is satisfactory if there are only a few system operations and if the facade controller is not taking on too many responsibilities (in other words, if it is not becoming incohesive). Choosing a use case controller is suitable when we have many system operations and we wish to distribute responsibilities in order to keep each controller class lightweight and focused" (18.4, p. 477). With the few POS operations (four in Process Sale, by this wiki's count) and the two Monopoly operations, the facade suffices (18.4, p. 477; 18.5, p. 499).

The defect this rule guards against is what Larman calls a bloated controller: over-assignment of responsibility, which leaves the controller with low [[cohesion]] (17.13, pp. 451-452, 456).

## Sign in code

Larman lists the signs of a bloated controller (17.13, pp. 456-457):

- There is only one controller class, it receives every system event, and there are many of them. This sometimes happens if a facade controller is chosen.
- The controller performs much of each operation itself instead of delegating. Larman says this usually also breaks [[information-expert]] and High Cohesion.
- The controller has many attributes and keeps significant information about the system or domain that should live in other objects, or duplicates information found elsewhere.

This wiki reads them in code as: a method of the receiving class whose body loops over domain data, does the arithmetic, and keeps the results (line items, running totals) in its own fields; or one receiving class whose public methods are the operations of several unrelated use cases, counted in the dozens rather than a handful.

This wiki assigns the neighbouring cases as follows. This page applies to the class that receives the program's incoming requests or system operations. Where the class reads widget fields or builds presentation output (a UI event handler, code-behind, a template), [[logic-testable-without-ui]] owns the sign; where it receives requests or system operations and holds no widgets (a web or command handler, a use-case controller), [[controller]] owns it. Where any other class reads and decides for several data-only classes, [[god-class]] owns it. Where a class whose public methods serve unrelated purposes is the one that receives the program's incoming requests or system operations, [[controller]] owns it; any other such class is [[class-interface-coherent-abstraction]].

## When not to apply

- **Few operations.** A single facade controller is satisfactory when there are only a few system operations (17.8, p. 432; 18.4, p. 477). One entry class with a handful of thin, delegating methods is not bloated, and splitting it into per-use-case handlers adds classes for nothing.
- **The incoming side cannot route.** Where input cannot be sent to different controllers, as in a message-handling system, Larman notes that a facade controller suits a UI that cannot redirect system event messages to alternating controllers (17.13, p. 452), and points to the Command pattern, where each message is represented and handled by its own Command object (pp. 459-460). Splitting by use case does not apply there.
- **Holding the scenario's state is the controller's job.** Larman gives knowing the state of the current use case, for legal ordering of operations, as a benefit of a session controller (p. 453). This wiki reads that as an exception to the many-attributes sign: fields that track where the scenario stands are not bloat; fields that copy domain data are.
- **The Web-MVC controller.** Larman says the controller in Web-MVC frameworks is part of the UI layer and controls page flow, and differs from the GRASP controller (p. 453). This page does not judge framework controller classes by these signs; their shape comes from the framework.
- **No UI/domain separation by design**, as in a small script or a throwaway tool. There is no boundary for a controller to sit behind, and that layering is the project's call. This limit is this wiki's own.
- **The project prescribes the shape of entry points** (one handler per command, one controller per resource). That convention decides which receiving classes exist; this page judges only whether each delegates. This limit is this wiki's own.

## Repair

Larman gives two cures (17.13, p. 457):

1. Add more controllers: replace a facade controller with use-case controllers. His airline example has `MakeReservationHandler`, `ManageSchedulesHandler` and `ManageFaresHandler`.
2. Design the controller so that it mainly delegates each system operation to other objects.

This wiki puts the second cure into practice with [[information-expert]]: move each computation to the object that holds its data, and leave in the controller only the call sequence and the scenario-state checks.

A trade-off Larman works through on the running total (18.4, p. 493): adding `getTotal` to Register keeps the UI coupled only to Register, "But it starts to expand the interface of the Register object, making it less cohesive". Letting the UI hold the Sale raises coupling, which he accepts because "coupling to unstable things is a real problem" and Sale is stable. This wiki reads that as: a pass-through query on a controller is justified only when the object behind it is unstable or must stay hidden from the caller; otherwise hand the caller the stable domain object. See [[low-coupling]] and [[hide-delegate-or-remove-middle-man]].

## Before and after

```
class Register                          // receives all system operations
    enterItem(id, qty)
        desc = catalog.find(id)
        line = { product: desc, qty: qty, subtotal: desc.price * qty }
        lines.add(line)
        runningTotal = runningTotal + line.subtotal
    endSale()
        ended = true
    makePayment(amount)
        change = amount - runningTotal
        ...
```

```
class Register
    enterItem(id, qty)
        desc = catalog.find(id)
        currentSale.makeLineItem(desc, qty)
    endSale()
        currentSale.becomeComplete()
    makePayment(amount)
        require currentSale.isComplete()
        currentSale.makePayment(amount)
```

In the "after" the controller holds no line items or totals. The one check it keeps enforces the order of operations, which Larman counts as a controller's job.

## Source

- Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]]: 17.8, PDF pp. 429-432 (the question, Model-View Separation, adapting the UI event, the variants, the facade for few operations); 17.13, PDF pp. 448-460 (facade versus use-case controllers, the delegation guideline, use-case state, the Web-MVC distinction, the bloating signs and cures, the Command pointer); 18.4, PDF pp. 477 and 492-493 (choosing the facade, the `getTotal` trade-off); 18.5, PDF p. 499.
- This wiki's own: the code reading of the signs, the selecting condition against neighbouring pages, the scenario-state exception, the limits on scripts and on prescribed entry points, the reading of the pass-through trade-off, and the pseudocode. The book's Swing and Struts listings (pp. 454-456) are framework-specific and are not carried over.
