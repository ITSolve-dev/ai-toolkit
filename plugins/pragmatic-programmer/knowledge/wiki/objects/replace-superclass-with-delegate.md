---
title: Replace superclass with delegate
category: objects
summary: "A subclass that extends a class describing a kind of thing while it represents one physical instance or copy of that kind (PhysicalCar extends CarModel, Scroll extends CatalogItem), so the kind's data is copied into every instance: the type-instance homonym. Hold the kind in a field, shared by reference, and forward to it instead."
tags: [rule, inheritance, delegation, type-instance-homonym, refactoring]
paradigm: oop
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Replace Superclass with Delegate, formerly Replace Inheritance with Delegation, turns the superclass into a field of the former subclass and forwards to it the operations the subclass needs ([[fowler-refactoring]], ch. 12, PDF pp. 447-453). Fowler names two kinds of misinheritance that it repairs. One is the classic stack built as a subclass of list, which exposes list operations that do not fit a stack (PDF p. 447). The other is the **type-instance homonym**: a class that represents a kind of thing is reused as the parent of a class that represents one instance of it. In his example a car model class (name, engine size) is extended to represent a physical car with a VIN and a manufacturing date (PDF p. 448).

## Rule

Inheritance is right only when two semantic conditions hold: every method on the supertype applies to the subtype, and every instance of the subtype is an instance of the supertype (PDF p. 448). Where either fails, replace the inheritance with delegation: "Using delegation makes it clear that it is a separate thing—one where only some of the functions carry over" (PDF p. 448).

Fowler goes further. Even where the subclass is reasonable modelling he may make this change, because the subclass is easily broken by changes in the superclass (PDF p. 448). But he rejects avoiding inheritance altogether: "my advice is to (mostly) use inheritance first, and apply Replace Superclass with Delegate when (and if) it becomes a problem" (PDF p. 448).

## Sign in code

The type-instance homonym, which this page owns: a subclass whose own fields identify one physical item or copy (a serial number, a VIN, a shelf location, the date it was last cleaned), extending a parent whose fields describe the kind or the catalogue entry shared by many such items (model name, title, tags, list price). A second sign confirms it: the kind's data is copied into each instance, so several subclass objects carry the same parent field values, which have to be updated together. Fowler says of his scrolls that to update either he must be careful that all copies of the same catalogue item are updated correctly (PDF p. 450).

This wiki assigns the neighbouring shapes as follows. A class inheriting from a container and exposing its operations (`Stack` extends `List`) is [[mixed-abstraction-levels-in-interface]]. A whole extending one of its parts is [[containment-or-inheritance]]. A class extending a framework or persistence base class for its machinery is [[delegate-to-services]]. A subclass that changes the meaning of an inherited method is [[liskov-substitution-principle]]. A subclass whose fields identify one instance while its parent describes the kind is [[replace-superclass-with-delegate]].

## When not to apply

- Both semantic conditions hold, and the subclass has not yet broken on a change to its parent. Fowler keeps inheritance then (PDF p. 448). In a project following [[choose-an-alternative-to-inheritance]]'s stance against inheritance, that page decides instead. This wiki resolves the disagreement per setting: where both conditions hold, Fowler's default holds unless the project convention says otherwise.
- The kind's data never changes. Fowler grants that in many situations he can get away with this error, since the title and tags can be thought of as copies of catalogue data that never change (PDF p. 450). He would still change the relationship, because the false model is likely to confuse programmers in the future (PDF p. 450). This wiki therefore reports such a case at lower severity, naming the copied kind fields.
- **Cost:** every operation that host and delegate share needs a forwarding function. Fowler finds these boring but "too simple to get wrong" (PDF p. 448). Where the forwards come to make up most of the class, see [[hide-delegate-or-remove-middle-man]].

## Repair

Fowler's mechanics (PDF pp. 448-449):

1. In the subclass, add a field that refers to a new instance of the superclass.
2. For each superclass element that is used, write a forwarding function to the field. Test after each consistent group (a getter and setter pair can be tested only once both are moved).
3. When everything is forwarded, remove the inheritance link.

For a type-instance homonym the basic change leaves each instance with a private copy of its kind. Fowler then goes on to share it, with Change Value to Reference ([[reference-or-value]], PDF pp. 451-453):

4. Give the instance its own identity field. The old structure stored the instance's id in the parent, and once the parent is shared that id belongs to the kind.
5. Pass the kind's id and a repository to the constructor, and look the kind up instead of constructing it. This wiki moves that lookup to the creation site and passes the found kind in, because a lookup in a constructor body is the sign of [[constructors-without-code]].
6. Remove the kind's data (title, tags) from the instance's constructor.

During step 4 Fowler briefly builds the kind with a null id, which he says would usually raise red flags, accepting it only as a temporary state (PDF p. 451).

## Before and after

```
class ProductModel
    field sku
    field name
    field listPrice
    method name(): return name

class StockUnit extends ProductModel
    field serialNo
    field receivedOn
    constructor(sku, name, listPrice, serialNo, receivedOn)
        super(sku, name, listPrice)
        ...

-- the same name and listPrice are copied into every unit of one model
```

```
class ProductModel
    field sku
    field name
    field listPrice
    method name(): return name

class StockUnit
    field serialNo
    field receivedOn
    field model                      -- shared reference
    constructor(serialNo, receivedOn, model)
        this.model = model
    method name(): return model.name()

-- at the creation site
unit = new StockUnit(serialNo, today, catalog.get(sku))
```

In the "after" no instance carries a copy of its kind, and the unit's interface has only the forwards it uses. The "before" fails the second semantic condition, because a stock unit is not a product model, so the limit for valid inheritance does not cover it.

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed. (Addison-Wesley, 2018), ch. 12, Replace Superclass with Delegate, PDF pp. 447-453: the stack and list example, the type-instance homonym and its car example, the two semantic conditions, coupling as a reason even for reasonable subclasses, the forwarding cost, the advice to use inheritance first, the mechanics, and the Scroll and CatalogItem example (copies of catalogue data, getting away with it, the follow-on Change Value to Reference, the temporary null id). This wiki's own: the sign worded as instance-identity fields beside kind-describing fields, the owner assignments, the reading of the "get away with it" case as a lower-severity finding, the per-setting resolution against [[choose-an-alternative-to-inheritance]], moving the lookup out of the constructor, and the pseudocode.
