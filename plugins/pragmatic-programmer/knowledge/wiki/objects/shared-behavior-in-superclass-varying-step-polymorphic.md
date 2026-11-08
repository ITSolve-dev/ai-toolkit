---
title: Put identical behavior in the superclass and make only the varying step polymorphic
category: objects
summary: "Sibling subclasses of one project superclass override the same method with bodies that match line for line except one expression or call; implement the method once in the superclass and make only that step a polymorphic operation."
tags: [rule, polymorphism, inheritance, duplication, template-method]
paradigm: oop
sources: [larman-applying-uml-and-patterns, fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

In the Monopoly iteration of chapter 35, landing on a square is already polymorphic: each kind of square that behaves differently has its own `landedOn` method (35.9, PDF p. 814). The iteration adds three kinds of property square: lot, railroad and utility. Larman says the existing design "shows off the beauty of polymorphism to handle new, similar cases" (PDF p. 815): new kinds of square arrive as new subclasses with their own methods. He then notes that "all the PropertySquares have identical landedOn behavior, so this method can be implemented once in the superclass and inherited by the subclasses of PropertySquare" (PDF p. 816). Only the rent differs, so by the Polymorphism principle "there is a getRent polymorphic operation in each subclass" (PDF p. 816). The per-kind side of that principle is [[polymorphism-or-type-switch]].

## Rule

When subclasses of one superclass share an algorithm and differ in one step, put the algorithm in the superclass once and make the step the polymorphic operation each subclass implements. This wiki notes that this is the shape the GoF call Template Method; Larman does not use that name here. Fowler names it Form Template Method (PDF p. 391).

## Sign in code

This wiki's reading of the sign, since the source names none:

- Two or more subclasses of the same project superclass override one method, and the bodies match line for line except one expression or call.
- The overrides match entirely: the method belongs in the superclass as it stands, with no step to vary.

This wiki assigns the neighbouring cases as follows. Overrides of one method on subclasses of a common superclass of the project's own, identical but for one step or wholly identical, are [[shared-behavior-in-superclass-varying-step-polymorphic]]. Method bodies repeated on sibling classes that share no superclass of the project's own are [[mixins-share-functionality]]. A shared frame around a differing middle in functions that override nothing is [[similar-functions-varying-middle]]. An abstract base class with one subclass, template method included, is [[base-class-with-one-subclass]]. Identical or near-identical overrides of a method the superclass already declares are [[shared-behavior-in-superclass-varying-step-polymorphic]]; identical methods or fields that sibling subclasses each define and the superclass does not declare are [[pull-up-method]]. Fowler's Form Template Method, for methods with the same overall flow and different details, is this page's shape ([[fowler-refactoring]], ch. 12, PDF p. 391).

## When not to apply

- The bodies only look alike now, and the subclasses differ in what the shared lines mean: one names a rule the other does not have. Merging them then couples two requirements. That decision is [[coincidental-duplication]]'s. This limit is this wiki's own.
- The project prefers composition to inheritance, or follows *Elegant Objects* conventions. The varying step is then passed in as a strategy object instead of being overridden ([[strategy-for-varying-algorithms]], [[choose-an-alternative-to-inheritance]]). This is the same separation without a hierarchy. This alternative is this wiki's own.
- The subclasses are not substitutable for the superclass. Pulling behavior up then deepens a hierarchy that [[liskov-substitution-principle]] already reports. This limit is this wiki's own.

## Repair

1. Move one copy of the shared method to the superclass.
2. Replace the varying expression with a call to a new abstract operation, or one with a default where most subclasses agree.
3. Implement that operation in each subclass with the expression it had, using the subclass's own fields or the arguments passed in, so the subclasses do not read the superclass's fields ([[private-data-not-protected]]).
4. Delete the subclass overrides of the shared method. Where the project marks methods final, mark the superclass's method final, so the subclasses only supply the step ([[final-or-abstract]] accepts that refinement).

## Before and after

```
class LotSquare extends PropertySquare
  field price
  method landedOn(player)
    if owner == none then player.tryToBuy(this)
    else if owner != player then player.pay(owner, price / 10)

class RailroadSquare extends PropertySquare
  method landedOn(player)
    if owner == none then player.tryToBuy(this)
    else if owner != player then player.pay(owner, 25 * owner.railroadCount())
```

```
abstract class PropertySquare extends Square
  final method landedOn(player)
    if owner == none then player.tryToBuy(this)
    else if owner != player then player.pay(owner, rent(owner))
  abstract method rent(owner)

class LotSquare extends PropertySquare
  field price
  method rent(owner) return price / 10

class RailroadSquare extends PropertySquare
  method rent(owner) return 25 * owner.railroadCount()
```

The rent formulas are invented: the source shows them only in figures not reproduced in `raw/`.

## Source

- Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 35.9 "Example: Monopoly", PDF pp. 814-817: polymorphic `landedOn`, the beauty-of-polymorphism quotation, `landedOn` implemented once in `PropertySquare`, polymorphic `getRent`. The quotations are in English and were checked against `raw/`.
- Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 12, Pull Up Method, PDF p. 391: a similar overall flow with differing details points to Form Template Method.
- This wiki's own: the Template Method note, the signs and their assignment against [[mixins-share-functionality]], [[similar-functions-varying-middle]] and [[base-class-with-one-subclass]], the limits, the repair and the pseudocode.

Related: [[information-expert]] (Do It Myself, 35.8), [[dry]].
