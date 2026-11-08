---
title: Override that does nothing
category: objects
summary: "A subclass overrides an inherited method with an empty body (or one that only returns/ignores) because this kind of object lacks the ability (ScratchlessCat.scratch, a penguin's fly); class names start to stack negations such as ScratchlessTaillessCat. Seen from the base: a behaviour only some subclasses have, placed in the parent."
tags: [rule, inheritance, contracts, containment]
paradigm: oop
sources: [code-complete, object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-07
---

McConnell treats a derived class that overrides a method and leaves it empty as evidence of a flaw in the base class design (p. 143).

Weisfeld's *The Object-Oriented Thought Process* reaches the same flaw from both ends. From the base class (ch. 5): a class meant to be extended must hold nothing that stands in the way of extending it, so supervisor functions do not belong in `Employee`, because a class that needs none of them may inherit from it; «Person должен содержать только данные и поведения, специфичные для него» (p. 106). The condition is that extension is actually intended (p. 106). From the subclass (ch. 7, after Meyers): `Bird` has `fly()`, and the penguin and the ostrich cannot fly; the behaviour can be overridden locally, «однако метод по-прежнему будет иметь имя fly» (p. 135), and a method named `fly` makes no sense on birds that only waddle, run or swim.

## Rule

Be suspicious of classes that override a method to do nothing (p. 143). The book's example: `Cat` has `Scratch()`, some cats have no claws, and `ScratchlessCat` overrides `Scratch()` to do nothing. It lists three costs (p. 143):

- it breaks the abstraction, the interface contract, of `Cat` by changing the semantics of its interface;
- it does not scale: a cat without a tail, one that does not catch mice, one that does not drink milk lead to classes such as `ScratchlessTaillessMicelessMilklessCat`;
- over time the derived classes' behaviour drifts far from the base interfaces, which makes the code hard to maintain.

The repair is in the original class, not in a derived one: «Корень наших бед — предположение, что все коты царапаются» (p. 143).

This wiki reads pp. 106 and 135 as Weisfeld's form of the same rule, seen from the base: put a behaviour in a parent only if every subclass has it. He states it only for a class meant to be extended (p. 106), and accepts not splitting where no lacking subclass exists (p. 137).

## Sign in code

- An overriding method whose body is empty, or only returns a neutral value, where the parent's method does work. A class name or comment saying the object lacks the capability confirms it.
- Sibling subclasses whose names combine negations or absences of base features.

This wiki assigns the neighbouring cases as follows. This page owns the empty or neutral override. A superclass member of the project's own that only one subclass, or a few, read, write or call, with no override in the others, is [[push-down-method-and-field]]; an empty override of it in the other subclasses is [[override-that-does-nothing]], and an override that throws or rejects is [[liskov-substitution-principle]]. A non-empty override of a method the parent implements is owned by [[final-or-abstract]]; one that throws "not supported", narrows the inputs the base method accepts, changes what the result means, or does something other than what the inherited method's name says is [[liskov-substitution-principle]]. A base-class method that tests which subclass it runs in to skip its work is a branch on runtime type: a branch whose key is an object's runtime type or class name is [[avoid-introspection-and-casting]], however many arms.

## When not to apply

- A base class that defines an intentionally empty hook (a template-method step documented as optional) and a subclass that leaves it empty: nothing in the base's contract promised behaviour. This limit is this wiki's.
- No subclass that lacks the behaviour exists. Weisfeld's breeder who keeps no yodeling dogs needs no split (p. 137), and he limits prediction: foreseeing every scenario a class will be reused in is practically impossible (p. 106). Splitting ahead of need is [[base-class-with-one-subclass]].
- A Null Object that implements an interface with no-op behaviour is the purpose of that class, not a subclass escaping a contract; see [[null-object-or-optional]]. This limit is this wiki's.

## Repair

Move the varying capability out of the base class. Three forms, by setting:

- **A contained part.** McConnell creates a `Claws` class and includes it in `Cat` (p. 143). This wiki adds that the part may be optional or have a null variant, so a cat without claws holds no claws rather than being a different class.
- **An intermediate class.** Weisfeld keeps in `Dog` what all dogs share (they pant) and moves the varying behaviour into `BarkingDog` and `YodelingDog` (p. 136); supervisor behaviour would likewise move from `Employee` into a `Supervisor` subclass (this application of p. 106 is this wiki's).
- **An interface** that only the capable classes implement, which Weisfeld calls «наилучшим решением» for bark and yodel (p. 136). Callers needing the behaviour then depend on that narrower type.

The trade-off, in Weisfeld's terms: splitting `Dog` models reality better than assuming every dog barks, «однако такой подход все немного усложняет» (p. 137), and in a large system such decisions add up fast (p. 137).

## Before and after

```
class Cat { scratch(): ... }
class ScratchlessCat extends Cat { scratch(): }   // empty
class ScratchlessTaillessCat extends ScratchlessCat { wagTail(): }
```

```
class Cat {
    claws: Claws?        // contained part
    scratch(): if claws != none: claws.scratch()
}
```

This wiki reads the optional part as outside [[null-field-hides-another-class]]: the absent claws do not change which kind of object the cat is, so the check is the optional-attribute case of that page's limits.

## Source

- [[code-complete]], ch. 6.3, Russian edition, p. 143: the rule, the Cat example, the three costs, the repair with `Claws`.
- Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]]: ch. 5, p. 106 (only what is specific to the base, the supervisor example, the condition that extension is intended, reuse scenarios unpredictable); ch. 7, pp. 135-137 (the penguin after Meyers, `BarkingDog` and `YodelingDog`, the interface as best solution, the complexity cost, the breeder with no yodeling dogs). The quotations were checked against `raw/`. This wiki's own for that part: the reading of pp. 106 and 135 as one rule, the routing of a base-class subclass test to [[avoid-introspection-and-casting]], and the `Supervisor` form of the repair.
- This wiki's own: the signs, the owner assignment against [[final-or-abstract]], [[liskov-substitution-principle]] and [[push-down-method-and-field]], both limits, the optional-part refinement, the pseudocode.
