---
title: Factory object for complex or variable creation
category: objects
summary: "A domain or business class chooses which concrete class to instantiate (branching on configuration, vendor or type code) or carries many lines of construction logic inside a method whose job is something else; move the choice and the construction into a separate factory object that returns the interface."
tags: [rule, factory, simple-factory, pure-fabrication, cohesion, creation]
paradigm: oop
sources: [larman-applying-uml-and-patterns]
created: 2026-11-07
updated: 2026-11-07
---

Factory, also called Simple or Concrete Factory, is not one of the GoF patterns. Larman calls it "extremely widespread" and a simplification of Abstract Factory (26.4, p. 606). It answers the question his adapter design raises: who creates the adapters, and who decides which adapter class to create? (See [[hide-third-party-apis]] for the adapters.)

## Rule

When creation has "special considerations, such as complex creation logic, a desire to separate the creation responsibilities for better cohesion", Larman's advice is to "Create a Pure Fabrication object called a Factory that handles the creation" (26.4, p. 606). Its stated advantages are that it separates the responsibility of complex creation into cohesive helper objects, hides that logic, and makes room for caching or recycling of instances (p. 606).

His reasoning against the obvious alternative is cohesion. If a domain object such as `Register` creates the adapters, its responsibilities go "beyond pure application logic ... and into other concerns related to connectivity with external software components", and that "lowers its cohesion" (p. 606). Of separation of concerns he writes: "Fundamentally, it is an application of the GRASP High Cohesion principle" (p. 606). See [[cohesion]] and [[pure-fabrication]].

Three specifics follow from his designs:

- **One factory per family.** Pricing strategies get their own `PricingStrategyFactory`, separate from the `ServicesFactory` for adapters, so "each factory is cohesively focused on creating a related family of objects" (26.7, p. 615).
- **Data-driven choice of class.** The factory reads the implementation class name from an external property and loads it dynamically, so a new adapter or strategy needs no change to the factory's source. Larman calls this a partial data-driven design that gives [[protected-variations]] for the implementation class (26.4, p. 607).
- **Caching depends on how fast the choice changes.** Because the pricing policy may change every hour, the strategy factory does not cache the instance; it re-reads the property and creates a fresh one each time (26.7, p. 615).

## Sign in code

This wiki's reading of the sign:

- A domain or business class contains `new` on several concrete classes picked by a condition on configuration, vendor name or type code.
- Construction of a collaborator takes many lines inside a method whose job is something else, for example reading settings, choosing a class and wiring dependencies inside `Register.initialize`.
- The same selection among concrete classes of one product type is repeated at several call sites.

This wiki assigns the neighbouring cases as follows. A call site that invokes a constructor where a named factory function would lift a constructor's limits is [[factory-function-over-constructor]]; a domain class that branches on configuration or type to decide which concrete class to instantiate is [[factory-object-for-creation]]. A plain `new` of one fixed class, with no choice and no setup, is [[creator]] where a part or record is constructed and [[new-only-in-secondary-constructors]] where a collaborator is. A choice among concrete classes, or many lines of construction logic, made in a domain class is this page's; once moved into a factory, that one creation switch is the intended result of [[polymorphism-or-type-switch]], not a finding there. Several creation sites that each switch on the same discriminator to build different members of one family are [[abstract-factory]]. A factory that only ever builds one class is [[do-not-force-a-design-pattern]]. A branch whose key names which third-party product is configured, its arms calling that product's own API, is [[hide-third-party-apis]]; a branch whose arms only choose which concrete class to instantiate is [[factory-object-for-creation]]. A switch whose arms only construct subclasses that override nothing but constants is [[subclass-that-differs-only-in-data]]; any other switch that only chooses which class to instantiate is [[factory-object-for-creation]]. A branch whose key names what kind of thing the switched-on object is (a shape, a square, a transaction) is [[polymorphism-or-type-switch]]; a branch whose key names a policy the object applies to compute one result, with that policy's parameters stored as fields of the object, is [[strategy-for-varying-algorithms]].

## When not to apply

- Creation is a plain constructor call with no selection and no setup. Then Creator, the class that holds or aggregates the object, is enough ([[creator]]). Larman's problem statement limits the pattern to creation with "special considerations" (p. 606).
- The project assembles objects in a composition root or a dependency-injection container. That setting already removes creation from domain classes, so a hand-written factory duplicates it. This limit is this wiki's own.
- Dynamic loading by class name from configuration trades compile-time checking for runtime flexibility: a typo in a property fails only when the code runs. Use it only where the class really has to be swappable without a rebuild. This trade-off is this wiki's own; Larman presents only the benefit.

## Repair

1. Collect the selection and construction logic into one method on a new factory class named for the family it creates, such as `ServicesFactory.getAccountingAdapter()`.
2. Return the interface type, not a concrete class.
3. Replace the call sites' branching with a call to the factory.
4. Give a second family its own factory, not a second method on an unrelated one (26.7, p. 615).

## Before and after

```
class Register
  method initialize()
    name = settings.get("tax.calculator")
    if name == "TaxMaster"
      tax = TaxMasterAdapter(settings.get("tm.url"), settings.get("tm.key"))
    else
      tax = GoodAsGoldAdapter(settings.get("gg.host"))
```

```
class ServicesFactory
  method getTaxCalculatorAdapter(): TaxCalculatorAdapter
    name = settings.get("tax.calculator")
    if name == "TaxMaster"
      return TaxMasterAdapter(settings.get("tm.url"), settings.get("tm.key"))
    return GoodAsGoldAdapter(settings.get("gg.host"))

class Register
  method initialize()
    tax = services.getTaxCalculatorAdapter()
```

## Source

Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 26.4, PDF pp. 606-607, and 26.7, PDF p. 615. The problem, the solution, the advantages, the cohesion argument, one factory per family, data-driven selection and the no-cache case are Larman's. The signs, the owner assignments against neighbouring pages, the second and third limits and the pseudocode are this wiki's own.

Related: [[abstract-factory]], [[strategy-for-varying-algorithms]].
