---
title: Inheritance weakens encapsulation
category: objects
summary: "Concept: a subclass inherits its parent's implementation, so a change inside a concrete parent method is not hidden from the subclass and ripples down the hierarchy (Cabbie.giveDirections reaching PartTimeCabbie), while a class that only calls the parent's public interface is insulated from it."
tags: [concept, inheritance, encapsulation, coupling, ripple-effect]
paradigm: oop
sources: [object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

Encapsulation splits a class into a public interface and a hidden implementation, so the implementation can change without other classes noticing ([[interface-and-implementation]]). Weisfeld calls it a paradox of object orientation that inheritance, one of its core concepts, «некоторым образом фактически нарушает инкапсуляцию» (p. 141). Citing Coad and Mayfield, he states the risk precisely: inheritance means «сильную инкапсуляцию по отношению к остальным классам, но слабую инкапсуляцию между суперклассом и его подклассами» (p. 142).

## The mechanism

If a subclass inherits an implementation and the parent's implementation is later modified, the change spreads down the hierarchy; this ripple can reach every subclass (p. 142). Weisfeld's example is `Cabbie` with `giveDirections()` and its subclass `PartTimeCabbie`: a change to `giveDirections()` in `Cabbie` directly affects `PartTimeCabbie` and every subclass written later, so «изменения реализации Cabbie не обязательно инкапсулируются в классе Cabbie» (p. 143). A class that only *uses* `Cabbie` through its public interface is, in theory, insulated from the same change (p. 142). Even so, the book adds, classes using `Cabbie` must be re-tested after a change to it (p. 142).

## What it changes in code

- **The is-a test.** A strict specialization feels a parent's change in a natural and expected way; if a change to the parent breaks the child, the child was no specialization (p. 143). That test is applied on [[containment-or-inheritance]].
- **Testing.** Testing a parent alone does not cover its subclasses; with the ripple effect, the book warns, testing can become a nightmare (p. 142). The rule is [[test-inherited-methods-in-each-subclass]].
- **Code shapes this concept explains.** A subclass reading a concrete parent's fields is [[inheritance-tax]]; a subclass overriding a method the parent's other methods call is [[final-or-abstract]]. This page names why both are risky and owns no sign of its own.

## Limits

This wiki reads the claim as being about *inherited implementation*. A parent that supplies only abstract methods (`Shape.draw()`, p. 146) gives subclasses no body to be broken by, so the ripple runs only through signatures, as it would through any interface. The chapter does not draw this distinction; it is this wiki's reading, consistent with the book's preference for interfaces where only some kinds share a behaviour (p. 136; see [[override-that-does-nothing]]).

## Source

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), ch. 7, pp. 141-143, after Coad and Mayfield, *Java Design*; via [[object-oriented-thought-process]]. The quotations were checked against `raw/`. This wiki's own: the mapping to [[inheritance-tax]] and [[final-or-abstract]], and the limit for parents with only abstract methods.
