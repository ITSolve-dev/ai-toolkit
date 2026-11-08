---
title: Prefer interfaces for polymorphism
category: objects
summary: "A base class with no shared behaviour, there only so unrelated classes fit one collection; a class needing a second parent; a hierarchy level no code is typed by."
tags: [rule, interfaces, polymorphism, inheritance, type-hierarchy]
paradigm: oop
sources: [pragmatic-programmer, elegant-objects, object-oriented-thought-process]
created: 2026-11-01
updated: 2026-11-06
---

Developers who like types use inheritance to state how classes relate, and draw hierarchies. The book compares them to Victorian naturalists sorting nature into categories (p. 201). Interfaces and protocols give the same substitutability without that structure.

## Rule

«Выражать полиморфизм предпочтительнее с помощью интерфейсов» (p. 204). An interface declares what a class must provide and contains no behaviour. Any class implementing it can be used as that type, so unrelated classes can sit in one collection and be processed through the shared methods (pp. 203-204). A class may implement several.

The book gives two failures of type hierarchies. They grow to wall-sized diagrams as levels are added for fine distinctions, and changes then spread up and down the levels, which makes the application brittle. And a thing often is several kinds at once. The book's car is a vehicle, an asset, an insured item and loan collateral, which calls for multiple inheritance. Many modern object-oriented languages do not support that, so the taxonomy cannot be modelled exactly even by someone content with complex trees (p. 202).

Weisfeld's *The Object-Oriented Thought Process* draws the same line by what each mechanism represents (ch. 8). An abstract class carries implementation shared by strictly related classes: his `Mammal` holds a concrete `generateHeat()`, because every mammal makes heat, and an abstract `makeNoise()`, because each makes its own sound; «Абстрактный класс представляет некоторую реализацию» (p. 164). Strict inheritance needs kinship, since the classes «при строгом наследовании должны быть связанными» (p. 164). An interface serves unrelated classes: a dog and a lizard can both be named though a lizard is no mammal, and «интерфейс моделирует только поведение» (p. 164). With an interface one need not worry about a formal inheritance structure (p. 161), and he rejects reading interfaces as a workaround for missing multiple inheritance: «Интерфейсы представляют собой отдельную методику проектирования» (p. 161). A has-a part takes neither: contracts are not used for composition (p. 160), and his `Dog extends Mammal implements Nameable` holds its `Head` as a field (pp. 164-165).

The books disagree on abstract classes. *Elegant Objects* holds they are no longer worth using (p. 53); Weisfeld uses one wherever related classes share an implementation. This wiki resolves it per setting: under the *Elegant Objects* convention shared behaviour goes into a composed part or decorator ([[delegate-to-services]]); elsewhere an abstract base is right when its subclasses are true is-a kin and share code, and an interface when they share only a capability.

## Sign in code

This wiki reads the sign as any of these:

- A base class holds no fields and no method implementations that subclasses use, and exists so that subclasses share one type.
- Classes with nothing in common descend from one ancestor, and code treats them uniformly through a loop over a collection of that ancestor.
- A class needs to count as two kinds of thing, and one of them is expressed by a stub, a duplicate or a workaround because it can have only one parent.
- A hierarchy level adds a single method or field that separates one sibling from another, and no parameter, field or collection is typed by that level. This sign needs a search of the code, and this wiki gives no verdict on it without one.

A base or level with exactly one subclass is [[base-class-with-one-subclass]] whatever it holds; one with two or more subclasses that holds no shared fields or implementations, or a level no code is typed by, is [[prefer-interfaces-for-polymorphism]].

## When not to apply

The book states no limit on interfaces. These are this wiki's own.

- There is one implementation and the code in view has no second. An interface there is an abstraction that does not yet pay for itself.
- Implementations need the same behaviour. An interface supplies none, so each class would rewrite it. Add a shared part: [[mixins-share-functionality]] or [[delegate-to-services]]; where the implementers are true is-a kin, Weisfeld's abstract base holding the shared body (p. 164). His own Shop listings copy `getName()`/`setName()` identically into two implementers of `Nameable` (pp. 173-175); reading that as this limit's case is this wiki's.
- In a language where interfaces carry default method bodies, "an interface has no implementation" no longer holds, and the choice reduces to kinship: related is-a classes against an unrelated capability. This reduction is this wiki's own.
- A framework dictates the shape of the type. That choice is made by the framework and is decided at work time.

A class used from another module, or one a test needs to substitute, takes an interface even with one production implementation (*Elegant Objects*' answer that such an interface is used at least twice, p. 53); that dependency is [[public-methods-implement-interfaces]]. A class with neither has no client to protect, and [[prefer-interfaces-for-polymorphism]]'s one-implementation limit decides.

## Repair

1. Name the role the caller actually uses, by what it does. The book uses behaviours like drivable and locatable (p. 203).
2. Declare an interface with only the methods that caller needs.
3. Make each class implement it, and type the parameter or collection by the interface.
4. Remove the base class if nothing else depends on it.

## Before and after

```
class Trackable
    abstract method position()

class Truck extends Trackable
    method position(): ...

class Parcel extends Trackable
    method position(): ...

items = list of Trackable
```

```
interface Locatable
    method position()

class Truck implements Locatable, Insurable
    method position(): ...
    method premium(): ...

class Parcel implements Locatable
    method position(): ...

items = list of Locatable
```

`Truck` now takes on a second role without needing a second parent.

## Source

[[pragmatic-programmer]], Thomas and Hunt, 20th Anniversary Edition, Russian translation (Dialektika, 2020), topic 31, pp. 201-204. The rule, the two failures of hierarchies and the first and third repair steps are the book's. The signs, the limits and the fourth repair step are this wiki's own. The pseudocode is this wiki's. [[elegant-objects]], p. 53: the answer that an interface a test substitutes is used at least twice; the split with [[public-methods-implement-interfaces]] built on it is this wiki's, as is the split with [[base-class-with-one-subclass]] by the number of subclasses. Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]], ch. 8: p. 160 (no contracts for composition), p. 161 (no formal inheritance structure, a design technique of its own), pp. 164-165 (`Mammal`, `Nameable`, `Head`, abstract class against interface), pp. 173-175 (the Shop listings). The quotations were checked against `raw/`. This wiki's own for that part: the per-setting resolution against *Elegant Objects*, the reading of the Shop duplication and the default-method limit. What a contract is: [[contract-via-abstract-methods]]. Related: [[inheritance-tax]], [[choose-an-alternative-to-inheritance]].
