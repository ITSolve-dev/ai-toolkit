---
title: Tell, don't ask
category: objects
summary: "Outside code reads an object's fields or getters, decides, then writes back through setters to that same object."
tags: [rule, encapsulation, responsibilities, coupling]
paradigm: oop
sources: [pragmatic-programmer, elegant-objects, larman-applying-uml-and-patterns]
created: 2026-11-01
updated: 2026-11-07
---

Tell, don't ask (TDA) forbids a caller from deciding on the basis of an object's internal state and then updating that object. The book's reason is that this cancels the benefit of encapsulation and spreads knowledge of the implementation through the code (p. 171). The principle is stated as «Указывай, а не спрашивай» (p. 171).

## Rule

Give the object the request and let it apply the change to its own state. Do not pull its state out, compute on it elsewhere and push the result back.

The book's motivating case is a new business limit on a value that any code can set. With the fields open to everyone, adding the check to the one function that seems responsible may be only part of the answer, and nothing tells the next maintainer that every other writer must obey it too (p. 170). This wiki reads the point as: an invariant needs a single place to live, and open fields deny it one. See [[class-invariant]].

The book's diagnosis of such an object is that it «служит лишь контейнером» (p. 170) for fields anyone may query and update.

## Sign in code

A function outside a class reads a field or getter of an instance and then, in the same function, assigns to fields of that same instance, or calls its setters, on the strength of what it read. The shape to look for is `x = obj.getPart()` followed by `x.a = x.a - d`.

This wiki notes that accessors alone do not meet this rule: [[uniform-access]] hides how a value is stored, and the decision can still sit outside the object. A class whose public methods are only accessors over its fields is [[no-getters-and-setters]]; this page keeps the call-site read followed by a write back, and comes first when both fire.

A second sign, from the book's own walkthrough: a caller fetches a collection from an object and searches it, where the owner could return the element directly (p. 171).

A lookup on an object followed by a command on the result, as in the pair below, is this page's repair and not a chain to break up. [[transformation-pipeline-over-method-chain]] owns chains of three or more links that convert data.

This wiki assigns the neighbouring cases as follows. This page owns a read followed by a write back. Whether the outside code writes back into the object it read decides between [[information-expert]] and [[tell-dont-ask]]: a read followed by a write back, or a collection fetched from an object to be searched, is [[tell-dont-ask]]; a read-only computation of a derived value from another class's data is [[information-expert]]. A field-less class whose methods all take the same one record and read or write only its fields, while the record has only fields or accessors, is [[class-with-only-data-or-only-behaviour]]; where its methods each read and write several data-only classes, [[god-class]] owns it; a single method of an otherwise sound class that reads another object and writes back is [[tell-dont-ask]]. A bare read or write of a field, with no decision between, is [[uniform-access]], and an accessor is no repair here. A field bound by a rule is [[class-invariant]], which comes first, and the repair is the method here; this wiki reads the book's discount case (p. 170) as such a field. On an object concurrent code reaches, a check and an update are [[check-then-act-must-be-atomic]]. Where a caller outside the aggregate reads its parts and writes the result back into it, [[tell-dont-ask]] owns it and comes first; [[pass-what-the-routine-uses]] owns the signature of a collaborator that receives parts it could take as the whole aggregate.

## When not to apply

- The book says TDA is not a law of nature: «Но принцип TDA нельзя считать законом природы.» (p. 171) It is a pattern for recognising trouble. It does not oblige `customer.applyDiscountToOrder(id)`.
- Stop at the application's top-level concepts. The book holds that in every application some concepts are universal and exist on their own, so hiding orders entirely inside customers makes no sense, and an API that hands out an order is acceptable (p. 172).
- This wiki reads the rule's wording, which is about deciding and then updating, as not covering a read that writes nothing back, such as formatting an object's values for display. The book does not discuss this case. *Elegant Objects* treats the display read as the very problem (p. 173). This page exempts it on the call side. Whether the class should print itself is judged on [[no-getters-and-setters]], and only where that page's sign holds.
- This wiki also reads the rule as tied to mutable objects. Where a function takes an immutable record and returns a new one, there is no internal state being overwritten behind the object's back, so the rule does not transfer. The book does not discuss this case.

## Repair

The book's walkthrough gives the steps, in order (pp. 170-171):

1. Move the computation and the write into a method on the object that holds the state.
2. Replace a collection handed to the caller with a lookup on the owner, so the caller no longer searches.
3. Hide helper objects the owner happens to use, by giving the owner the method. The book asks why the outside world should know that an order keeps its totals in a separate object.
4. Stop when the next step would wrap one top-level concept entirely inside another.

Larman gives a second direction for the same shape. When object A keeps needing the data in object B, either A should hold that data, or B should have the responsibility (25.1, p. 583). In his Monopoly redesign Player kept getting its square from Piece, used it, and assigned the new square back; Player came to hold the square itself, "since the Player keeps collaborating with its Square" (p. 583), and Larman then questions whether Piece is needed at all. This wiki resolves the two directions by use. Where the caller uses the read object as a collaborator across several of its operations and the holder does nothing with it besides store it, move the field to the caller and delete the holder's accessor pair. Otherwise follow the steps above and move the behaviour to the holder.

Trade-off, as this wiki states it: each step adds a method to the owner's interface, so applying the rule without the stopping point turns the top-level class into a forwarding list for everything beneath it.

## Before and after

```
// before: the caller reads, computes and writes the plan's internals
function extendPlan(user, plan_id, days):
    term = user.plans.find(plan_id).getTerm()
    term.endDate = term.endDate + days
    term.extendedBy = days
```

```
// after: the plan owns the change; finding a plan on a user stays public,
// because a plan is a concept in its own right
function extendPlan(user, plan_id, days):
    user.findPlan(plan_id).extend(days)
```

Any limit on `days` now has one home, inside `extend`.

## Source

[[pragmatic-programmer]], Topic 28, Russian edition, pp. 170-172: the rule, its reasoning, the steps of the repair and the first two limits. [[elegant-objects]], section 3.5, p. 173: the display read as the problem. Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 25.1, PDF p. 583: move the data or the responsibility, and the Player/Piece redesign; the resolution between the two directions by use is this wiki's own. This wiki's own: the wording of the signs, the note on accessors, the separation from a chain, the assignment of neighbouring cases, the limits marked as its reading, the trade-off, and the example. Related: [[train-wreck]], [[coupling]], and [[object-as-representative]], the object's side of the same idea in *Elegant Objects*.
