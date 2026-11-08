---
title: "Facade: one entry point to a group of classes"
category: structure
summary: "Client classes import and call several classes of one group of the project's own code (a loader, an evaluator, a cache) to perform one service, each client repeating the same call sequence, so replacing the group means editing every client; give the group one front object and make the rest private."
tags: [rule, facade, gof, low-coupling, indirection, protected-variations]
paradigm: oop
sources: [larman-applying-uml-and-patterns]
created: 2026-11-07
updated: 2026-11-07
---

Facade is the GoF pattern for the case where "A common, unified interface to a disparate set of implementations or interfaces" is required and there "may be undesirable coupling to many things in the subsystem, or the implementation of the subsystem may change". The solution is to "Define a single point of contact to the subsystem", a "facade object that wraps the subsystem" (26.9, p. 627). Larman summarizes: "It hides a subsystem behind an object" (p. 629). He uses "subsystem" informally, for "a separate grouping of related components" (p. 628). This wiki applies the rule to such a grouping inside a module and does not prescribe how a system is split.

## Rule

Clients see only the facade. The other classes of the group "are private and can't be seen by external components" (p. 628). The facade gives [[protected-variations]] from changes in the group's implementation "by adding an Indirection object to help support Low Coupling", so that external objects are "coupled to one point" (p. 629). See [[low-coupling]].

Larman's case is pluggable business rules whose implementation is still undecided: a Strategy family, an open-source rule interpreter or a commercial engine. `Sale.makeLineItem` calls `POSRuleEngineFacade.isInvalid(lineItem, sale)` near its start and returns early if a rule rejects the item (p. 628). The facade lets the implementation behind it be swapped, even for "a non-object-oriented solution", while the client sees "only its one public access point" (p. 629). He notes that facades are usually reached through a Singleton; this wiki's position on that access point is [[no-singletons]].

## Sign in code

This wiki's reading of the sign:

- Client classes import and call several classes of one group (a parser, a loader, an evaluator, a cache) to perform one service, and each client repeats the same call sequence.
- Replacing the group's implementation would mean editing every client, because clients name its internal classes.
- The group's internal classes are public only because outside code reaches into them.

Adapter and Facade both fire on a class that wraps something. **Selecting condition:** if the wrapper exists so that a third-party product, or several of them with different interfaces, reach the application through the application's own interface, [[hide-third-party-apis]] owns it; if it exists to give one entry point to a group of the project's own classes, [[facade-single-entry-point]] owns it. Larman: an adapter "is a kind of facade, but the emphasis is to provide adaptation to varying interfaces" (p. 629). A front object whose methods are only one-line forwards to one field is [[hide-delegate-or-remove-middle-man]].

## When not to apply

- The group has one class or a very small surface that clients already use through one object. A facade would only forward calls, the middle man of [[hide-delegate-or-remove-middle-man]]. This limit is this wiki's own.
- Different clients really need different parts of the group's interface. A single facade then grows into a large class mixing unrelated services ([[god-class]]). Split by client need instead. This limit is this wiki's own.
- Whether a group should be a separate subsystem or module at all is architecture and is outside this wiki's scope. This page assumes the grouping is given.

## Repair

1. Name the services clients actually use from the group, and define them as methods on one facade class.
2. Move the call sequences that clients repeat into those methods.
3. Switch clients to the facade, then reduce the visibility of the internal classes.

## Before and after

```
class Sale
  method makeLineItem(desc, qty)
    item = SalesLineItem(desc, qty)
    rules = RuleLoader.load("enterItem")
    ctx = RuleContext(item, this)
    if RuleEvaluator(rules).anyFails(ctx) return
    lineItems.add(item)

class Register
  method applyChange(sale, change)
    rules = RuleLoader.load("chooseCashChange")
    ctx = RuleContext(change, sale)
    if RuleEvaluator(rules).anyFails(ctx) return
    sale.setChange(change)
```

```
class RuleEngineFacade
  method isInvalid(subject, sale, point)
    rules = loader.load(point)
    return evaluator.anyFails(rules, RuleContext(subject, sale))

class Sale
  method makeLineItem(desc, qty)
    item = SalesLineItem(desc, qty)
    if ruleEngine.isInvalid(item, this, "enterItem") return
    lineItems.add(item)

class Register
  method applyChange(sale, change)
    if ruleEngine.isInvalid(change, sale, "chooseCashChange") return
    sale.setChange(change)
```

## Source

Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 26.9, PDF pp. 627-629. The problem, the solution, the privacy of the group, the rule-engine example, the Singleton remark and the Adapter distinction are Larman's. The solution is quoted in two parts because a punctuation mark between them is lost in `raw/`. The second client (`Register.applyChange`, after Larman's `chooseCashChange` rule point, p. 627), the signs, the selecting condition as worded, the limits and the pseudocode are this wiki's own.
