---
title: Subclass that differs only in data
category: objects
summary: "A derived class that overrides nothing but constants or fixed return values (Male and Female overriding genderCode), often tested by clients with instanceof or chosen by a loader's switch on a data code, or a class constructed at exactly one site, where an object of an existing class with different field values would do."
tags: [rule, inheritance, objects-vs-classes, singleton, remove-subclass]
paradigm: oop
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

McConnell warns that a class with a single instance may mean that objects have been confused with classes (p. 142). Fowler's refactoring **Remove Subclass** (formerly Replace Subclass with Fields) is the same repair from the other end: fold subclasses that no longer earn their keep back into their superclass, as a field that records the difference (*Refactoring*, 2nd ed., ch. 12, PDF pp. 409-416). It is the inverse of [[replace-type-code-with-subclasses]].

## Rule

Be suspicious of classes of which only one object is created: «Использование единственного экземпляра класса может указывать на то, что вы спутали объекты с классами» (p. 142). Ask whether an object could be created instead of a new class, and whether a particular derived class could be represented only by data rather than as a separate class (p. 142). The book names the Singleton pattern as a notable exception (p. 142).

Fowler grants that subclasses are a good way to program by difference, but says they can lose their value as the variations they support are moved elsewhere or removed, and some are added in anticipation of features that are never built (PDF p. 410). His verdict: "A subclass that does too little incurs a cost in understanding that is no longer worthwhile" (PDF p. 410). Replace such a subclass with a field on the superclass.

## Sign in code

- A derived class whose overrides only return literals or set constants that the base uses (a `GoldCustomer` that returns `discount = 0.1`; Fowler's `Male` and `Female` overriding `genderCode`, PDF p. 411), with no fields and no other behaviour.
- Clients branch on such a concrete class with `instanceof` or a type test (`people.filter(p => p instanceof Male)`, PDF p. 412). Fowler says of `instanceof` that it "never smells good" (PDF p. 413).
- A loader or caller switches on a data code only to choose which of these near-empty subclasses to construct (PDF p. 412).
- A class instantiated in exactly one place, as a search of its creation sites shows, whose instance is distinguished from siblings only by fixed values.
- This wiki adds: a subclass that differs in data today but whose behaviour is expected to diverge is still a finding, because the forecast is not a sign.

This wiki assigns the neighbouring shapes as follows. A subclass or parent left with no field and no method of its own (at most a constructor passing its arguments to super) is [[collapse-hierarchy]]; a base with exactly one derived class that both hold code of their own is [[base-class-with-one-subclass]]; a subclass that overrides only constants or fixed return values is [[subclass-that-differs-only-in-data]]. Subclasses each holding a sequence of steps over a different field list are [[describe-variants-in-data-not-subclasses]]. Subclasses made from a type code, each carrying fields or methods of its own kind, are [[replace-type-code-with-subclasses]]; a subclass that overrides only constants or fixed return values is [[subclass-that-differs-only-in-data]], even inside such a family. A type test on a subclass that overrides only constants or fixed return values is [[subclass-that-differs-only-in-data]]; a type test on a class that has real behaviour of its own is [[avoid-introspection-and-casting]]. A switch whose arms only construct subclasses that override nothing but constants is [[subclass-that-differs-only-in-data]]; any other switch that only chooses which class to instantiate is [[factory-object-for-creation]]. A method whose whole body returns a constant, overridden per subclass, is [[subclass-that-differs-only-in-data]]; sibling methods with a computing body that differs only in literals are [[parameterize-function]].

## When not to apply

- The book's own exception, Singleton, conflicts with [[no-singletons]], which owns the shape of a static instance accessor. This wiki resolves it per setting: the question here is whether a separate class is warranted at all; whether one object should be reached globally is decided by [[no-singletons]] and [[global-data]].
- Behaviour that depends on the subclass sits in the clients and belongs in the subclasses. Fowler checks this before removing: "it’s usually worth checking to see if there’s any subclassdependent behavior in the clients that should be moved in there" (PDF p. 411; the extracted text drops the hyphen). If there is, the subclasses have a job: move that behaviour in ([[polymorphism-or-type-switch]]), and do not delete them.
- The subclasses carry fields or methods valid only for their kind. They are then the shape [[replace-type-code-with-subclasses]] creates on purpose. This limit is this wiki's own.
- A framework or test harness requires one subclass per variant (a handler, a fixture), or the project's convention does. This limit is this wiki's own.

## Repair

The book's refactoring for subclasses that differ only in returned constants: stop overriding the methods, have the subclasses initialise the base class with the constants, and put the general code using them in the base (p. 562). This wiki takes the step further: once the subclasses hold nothing but that initialisation, make the varying values fields of the base class, set through its constructor, and create configured objects instead of subclasses.

Fowler's mechanics for the same end (PDF pp. 410-411):

1. Put the subclass constructors behind factory functions ([[factory-function-over-constructor]]). If clients pick the subclass from a data field, put that choice in a superclass factory; Fowler extracts the existing selection `switch` into the factory (PDF pp. 412-413).
2. If code tests the subclass types, extract each test into a function and move it onto the superclass (`isMale`). Test after each change.
3. Create a field for the subclass type and change the methods that refer to the subclass to use it.
4. Delete the subclass. Test.

For a group of subclasses, encapsulate all of them first (factory, moved type tests), then fold them in one at a time (PDF p. 411). The underlying move, in Fowler's words: "Whenever I want to change how I represent something, I try to first encapsulate the current representation to minimize the impact on any client code" (PDF p. 412). During the change he lets the superclass refer to a subclass for a moment, saying "this code isn’t going to last until my next cup of tea" (PDF p. 414): a transient state, not a target. Afterwards he makes the factory symmetric, passing the default code explicitly too, since "A future reader of the code will always wonder about this lack of symmetry" (PDF p. 415), and he warns against forgetting the default case for records that fit neither code (PDF pp. 414-415).

## Before and after

```
class Customer     { discount(): 0 }
class GoldCustomer   extends Customer { discount(): 0.10 }
class SilverCustomer extends Customer { discount(): 0.05 }

goldCount = customers.filter(c -> c instanceof GoldCustomer).length
```

```
class Customer
    constructor(tier: Tier)
    discount(): tier.discount
    isGold(): tier.name == "gold"
Tier(name, discount)

// at the assembly point
gold = Customer(Tier("gold", 0.10))
goldCount = customers.filter(c -> c.isGold()).length
```

## Source

- [[code-complete]], p. 142: the rule, the two questions, the Singleton exception; p. 562: the refactoring that replaces virtual methods with data initialisation.
- [[fowler-refactoring]], ch. 12, Remove Subclass, PDF pp. 409-416: the motivation, the `instanceof` and loader signs, the check of client behaviour, the mechanics, the encapsulate-first principle, the temporary superclass-to-subclass reference, the symmetry point and the default case.
- This wiki's own: the signs as worded, the owner assignments, the resolution against [[no-singletons]], the kind-specific-fields and framework limits, the step from initialised subclasses to configured objects, and the pseudocode.
- The book also shows how to build a singleton with a private constructor and a static accessor (pp. 147-148); that mechanism is language detail and is not kept as a rule here.
