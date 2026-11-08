---
title: Extract superclass
category: objects
summary: "Two classes with no common parent each declare the same field (name, id) and a method with the same body over a corresponding value (annualCost = monthlyCost * 12 beside totalAnnualCost = totalMonthlyCost * 12), often under different names; a repeated field group alone, with no shared method, is containment-or-inheritance."
tags: [rule, inheritance, duplication, refactoring, superclass]
paradigm: oop
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Extract Superclass is Fowler's refactoring for two classes that do similar things: create a common parent and move the shared data and behaviour into it with [[pull-up-method]] (with Pull Up Field) and [[pull-up-constructor-body]] ([[fowler-refactoring]], ch. 12, PDF p. 417). Fowler rejects the view that inheritance has to be planned up front from a "real world" classification. Such a classification is a hint, "but just as often inheritance is something I realize during the evolution of a program, as I find common elements that I want to pull together" (PDF pp. 417-418).

## Rule

When two classes carry the same data and the same behaviour over it, pull those into a superclass. Its alternative is Extract Class, so the choice is between inheritance and delegation as the way to unify duplicate behaviour. Fowler states his own order: "Often Extract Superclass is the simpler approach, so I’ll do this first knowing I can use Replace Superclass with Delegate (399) should I need to later" (PDF p. 418).

Before pulling methods up, check whether methods with different names and different bodies represent the same intent. If they do, rename them to one name with [[change-function-declaration]] first, and only then pull them up (PDF p. 421). Fowler's example has a department's `totalMonthlyCost`, a sum over its staff, and an employee's stored `monthlyCost`. He renames the first to `monthlyCost`, so that both classes' annual-cost methods become the same text, which can then go into the parent.

## Sign in code

Two classes with no common parent (other than a root object type) each declare:

- one or more fields with the same name and meaning (`name`, `id`), with identical accessors, **and**
- at least one method whose body is the same expression over a value each class supplies, even when the method names differ (`annualCost` returning `monthlyCost * 12` in one class, `totalAnnualCost` returning `totalMonthlyCost * 12` in the other).

This wiki assigns the neighbouring shapes as follows. A group of fields repeated across several classes with no shared method over them is [[containment-or-inheritance]], whose table routes data shared without behaviour to a contained object. Classes with no superclass of the project's own that repeat the same fields and a method over them, where every instance of each class would be a valid instance of one shared parent, are [[extract-superclass]]; repeated method bodies on classes whose instances would not be valid instances of one parent, or repeated without shared fields, are [[mixins-share-functionality]]. Subclasses of one existing superclass that override the same method with near-identical bodies are [[shared-behavior-in-superclass-varying-step-polymorphic]].

## When not to apply

- Fowler gives Extract Class as the alternative and does not fix when it wins. This wiki reads the choice through the conditions Fowler states under Replace Superclass with Delegate: inheritance suits only when every method of the new parent applies to each child and every child instance is a valid parent instance (PDF p. 448). Where either fails, extract a class and delegate instead ([[containment-or-inheritance]]).
- If the language allows only one superclass and either class already uses it, or the classes will need a different axis of variation, the parent slot is taken. Fowler calls inheritance a card that can only be played once (PDF p. 424). Applying that limit to this refactoring is this wiki's.
- Methods with the same body but a different intent are a chance likeness, not duplicated knowledge ([[coincidental-duplication]]). Fowler's rename step depends on the question whether they represent the same intent (PDF p. 421), and only the domain can answer it.
- Where the project prefers composition, the shared part goes into a contained object ([[choose-an-alternative-to-inheritance]]). This limit is this wiki's own.

## Repair

Fowler's mechanics (PDF p. 418):

1. Create an empty superclass and make both classes extend it. Adjust the constructors if needed. Test.
2. Move common elements up one at a time: constructor body, fields, then methods. Fowler starts with the data (PDF p. 420).
3. Where methods differ only in name for the same intent, rename them to one name, then pull up.
4. In the methods that remain on the subclasses, look for common parts: extract each into its own function, then pull it up.
5. Check the clients of the original classes, and consider having them use the superclass interface.

Test after each step ([[refactor-in-small-tested-steps]]). This wiki adds: where the project follows *Elegant Objects*, the pulled-up methods are final and the parent is abstract ([[final-or-abstract]]).

## Before and after

```
class Contractor
    field name
    field dailyRate
    method name(): return name
    method weeklyCost(): return dailyRate * 5

class Crew
    field name
    field members
    method name(): return name
    method totalDailyRate(): return sum(m.dailyRate for m in members)
    method totalWeeklyCost(): return totalDailyRate() * 5
```

```
class Payee
    field name
    constructor(name): this.name = name
    method name(): return name
    method weeklyCost(): return dailyRate() * 5
    abstract method dailyRate()

class Contractor extends Payee
    field rate
    method dailyRate(): return rate

class Crew extends Payee
    field members
    method dailyRate(): return sum(m.dailyRate() for m in members)
```

In the "after" there are no repeated fields or method bodies left. Both children are payees whose whole interface applies to them, so the delegation limit above does not fire.

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed. (Addison-Wesley, 2018), ch. 12, Extract Superclass, PDF pp. 417-422: the motivation, inheritance discovered rather than planned, the Extract Class alternative and the order of trying them, the mechanics, the rename-before-pull step. This wiki's own: the sign as worded, the owner assignments, applying Fowler's semantic conditions (PDF p. 448) and his one-axis limit (PDF p. 424) to this refactoring, the chance-likeness and composition limits, the *Elegant Objects* form of the repair, and the pseudocode.
