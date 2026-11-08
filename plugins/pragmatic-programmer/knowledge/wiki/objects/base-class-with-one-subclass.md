---
title: Base class with one subclass
category: objects
summary: "An abstract or base class that has exactly one derived class in the codebase and no test double deriving from it."
tags: [rule, inheritance, speculative-generality, yagni]
paradigm: oop
sources: [code-complete, object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-07
---

McConnell reads a base class with a single derived class as a trace of someone who "designed ahead", trying to anticipate future needs without fully understanding them (p. 143).

## Rule

Be suspicious of base classes with only one derived class (p. 143). The best preparation for future work is not extra levels of base classes that might be needed some day, but code that is as clear, understandable and simple as possible: do not complicate the hierarchy without real need (p. 143). The same chapter's note on NASA's reuse work makes the matching point: reusable classes there were identified at the end of a project, not designed for reuse up front, which prevented gold-plating (p. 151).

Weisfeld's *The Object-Oriented Thought Process* states the trade-off underneath. In theory the best approach is to factor out as much commonality as possible, but «Чем большую общность вы выделяете, тем сложнее становится ваша система» (p. 136), and there are no hard rules for the choice (p. 137). His examples are a `YodelingDog` level for a breeder who keeps only barking dogs, and a `Canine` root with hyenas and foxes for a pet seller, which a zoo keeper might need (p. 137). The added functionality may bring nothing back, since «окупаемости инвестиций может не произойти» (p. 137); the aim is a system that is flexible «но не настолько сложной, что может рухнуть под собственной тяжестью» (p. 137). Composition has the same edge: between a model detailed enough to be expressive and one too detailed to understand and maintain «проходит тонкая грань» (p. 140). This wiki reads the books as agreeing: a level is added when the code in view uses the distinction.

## Sign in code

A base or abstract class in the project's own code with exactly one class deriving from it, and no test double or second implementation in the repository.

An abstract base class with one subclass, template method included, is [[base-class-with-one-subclass]], even when it plays a pattern role; other pattern scaffolding with one occupant is [[do-not-force-a-design-pattern]]. A subclass or parent left with no field and no method of its own (at most a constructor passing its arguments to super) is [[collapse-hierarchy]]; a base with exactly one derived class that both hold code of their own is [[base-class-with-one-subclass]]; a subclass that overrides only constants or fixed return values is [[subclass-that-differs-only-in-data]]. Otherwise a base or level with exactly one subclass is [[base-class-with-one-subclass]] whatever it holds; one with two or more subclasses that holds no shared fields or implementations, or a level no code is typed by, is [[prefer-interfaces-for-polymorphism]]. This page owns a class, abstract or concrete, from which exactly one class derives; an interface with no implementation of its own is not this page's.

## When not to apply

- The base is a published extension point that outside code implements; the second subclass exists, just not in this repository. Finding that requires knowing the users, so this page can only ask, not assert.
- Weisfeld concedes that a model not designed now for a later need costs much more to change later (p. 138), and gives no test for when that outweighs the complexity. This wiki reads it as: the later cost must be argued from the code in view, not assumed, and a published extension point (above) is the case where it can be.
- This wiki adds: if the base exists to give tests a substitute and a test double derives from it, there are two subclasses.
- This wiki adds: where the project's architecture puts an interface at a boundary it defines, one implementation is that architecture's choice and is taken as given; this page does not fire.

## Repair

Merge the base into its only subclass, or keep only the interface a client actually needs; reintroduce the base when a second variant arrives.

## Before and after

```
abstract class Document { save() ; layout() }
class Letter extends Document { layout(): ... }
```

```
class Letter { save() ; layout() }
```

## Source

- [[code-complete]], p. 143 (the rule and its reasoning), p. 151 (NASA, reuse classes identified at the end).
- Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]], ch. 7, pp. 135-140: the more commonality, the more complexity; the breeder, pet seller and zoo examples; return on investment; the later cost of not designing ahead; the fine line for composition. The quotations were checked against `raw/`. This wiki's own for that part: the reading of the two books as agreeing and the reading of the later-cost concession.
- This wiki's own: the sign, the owner splits, the published-extension-point, test-double and architecture limits, the repair and the pseudocode.

Related: [[replaceable-code-over-forecast]], [[know-when-to-stop]].
