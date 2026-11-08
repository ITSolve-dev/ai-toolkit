---
title: Abstract Factory for families of related objects
category: objects
summary: "Several creation sites each switch on the same discriminator (vendor, platform, theme) to pick the concrete class of a different member of one family (cash drawer, coin dispenser), so members of different families can be mixed and a new family means editing every switch; let one concrete factory per family create them all behind one factory interface."
tags: [rule, gof, creation, factory]
paradigm: oop
sources: [larman-applying-uml-and-patterns]
created: 2026-11-07
updated: 2026-11-07
---

Abstract Factory is a GoF creational pattern. Larman's context and problem: "How to create families of related classes that implement a common interface?" (35.7, p. 804). His case: the point-of-sale terminal needs a cash drawer, a coin dispenser and other devices, and each vendor (IBM, NCR) ships its own set of classes implementing the same standard interfaces (p. 804).

## Rule

Solution, in the source: "Define a factory interface (the abstract factory). Define a concrete factory class for each family of things to create. Optionally, define a true abstract class that implements the factory interface and provides common services to the concrete factories that extend it" (p. 804).

Larman's refinement, the *abstract class abstract factory*, answers the question "How does the application know which abstract factory to use?" (p. 805). An abstract factory class reached through a Singleton `getInstance()` reads a system property naming the concrete factory class, creates it by reflection and returns it. Code then calls `JavaPOSDevicesFactory.getInstance().getNewCashDrawer()`, and switching vendors means editing a properties file (p. 806). He names `java.awt.Toolkit` as a library example (p. 805).

This wiki reads the gain as consistency: the choice of family is made once, so a client cannot end up with an IBM drawer and an NCR dispenser.

## Sign in code

This wiki's reading of the sign:

- Several switches, in one method or several, on the same discriminator (vendor, platform, theme), each picking the concrete class of a different product type.
- Adding a family (a new vendor) means editing every one of those switches.

This wiki assigns the neighbouring cases as follows. One choice among concrete classes of one product type, made in a domain class, is [[factory-object-for-creation]]; several creation sites that each switch on the same discriminator to build different members of one family are [[abstract-factory]]. A switch on a type code outside creation is [[polymorphism-or-type-switch]].

## When not to apply

- There is one product type, not a family. A plain factory or a constructor parameter does the job ([[factory-object-for-creation]]). This limit is this wiki's own.
- There is one family and no second one in the code. The abstract factory interface would have one implementation ([[do-not-force-a-design-pattern]]). This limit is this wiki's own.
- The Singleton-plus-reflection refinement is a choice the source makes for its case. This wiki notes that it hides where the dependency comes from and makes the factory global state ([[no-singletons]], [[global-data]]). Where the project passes dependencies in explicitly, the concrete factory is passed to the constructor instead. This trade-off is this wiki's own.

## Repair

1. Define a factory interface with one creation method per product type.
2. Write one concrete factory per family, each returning its own family's classes.
3. Choose the concrete factory once, at the place the project wires objects, and give clients the factory interface.
4. Delete the per-product switches.

## Before and after

```
class Register
  constructor(vendor)
    if vendor == "IBM" then drawer = IbmCashDrawer()
    else drawer = NcrCashDrawer()
    if vendor == "IBM" then dispenser = IbmCoinDispenser()
    else dispenser = NcrCoinDispenser()
```

```
interface PosDevicesFactory
  newCashDrawer(): CashDrawer
  newCoinDispenser(): CoinDispenser

class IbmDevicesFactory implements PosDevicesFactory ...
class NcrDevicesFactory implements PosDevicesFactory ...

class Register
  constructor(devices: PosDevicesFactory)
    drawer = devices.newCashDrawer()
    dispenser = devices.newCoinDispenser()
```

## Source

- Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 35.7, PDF pp. 804-807: the problem, the solution, the abstract class variant with Singleton and system property, and the Toolkit example.
- This wiki's own: the reading as family consistency, the signs, the owner assignments, the limits including the Singleton trade-off, the repair and the pseudocode (which passes the factory in instead of using the source's Singleton).

Related: [[proxy]], [[factory-object-for-creation]].
