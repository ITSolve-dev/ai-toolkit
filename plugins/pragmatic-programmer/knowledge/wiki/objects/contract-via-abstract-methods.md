---
title: Contract via abstract methods
category: objects
summary: "Concept: Weisfeld's 'contract' is a method left unimplemented in an abstract class or interface, so the compiler rejects a concrete subclass that does not supply it; it fixes signatures only and is not Design by Contract."
tags: [concept, contracts, abstract-class, interfaces, polymorphism]
paradigm: oop
sources: [object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

In Weisfeld's chapter 8 a **contract** is any mechanism that makes a developer follow an API's specification: method names, parameter counts, signatures (pp. 156-157). In code it means one thing: «Простое правило при определении контракта заключается в обеспечении нереализованного метода с помощью либо абстрактного класса, либо интерфейса» (p. 165). A subclass that means to honour the contract implements the unimplemented methods of its parent class or interface.

## Not Design by Contract

Weisfeld warns that the word has other meanings in software (p. 157). His contract concerns *signatures* that the type checker enforces and says nothing of preconditions, postconditions or invariants, which are [[design-by-contract]]. The separation beyond the book's one-line warning is this wiki's.

## How it is enforced

- The abstract methods are the contract: «Эти абстрактные методы представляют собой контракт» (p. 159). Concrete methods in the same abstract class (the book's `setColor()` on `Shape`) are inherited and are not part of it.
- The compiler enforces it: a `Circle` that inherits from `Shape` without a `draw()` «не пройдет даже компиляцию» (p. 159). A subclass that leaves the method out is itself abstract, and a further subclass must supply it (p. 159).
- Implementing an interface is an is-a relation as far as the type checker is concerned: `Nameable N = D;` compiles for a `Dog`, so both inheritance and interfaces are an is-a relation (p. 165).
- A broken contract can leave code unusable, not only break a convention: the book's browser calls `run()` on an applet implementing `Runnable`, and if `run()` is missing an error occurs (p. 168).

## What it buys

- **Polymorphism.** Each subclass implements `draw()` its own way, and the caller sends one message to any shape (p. 158). See [[polymorphism-or-type-switch]].
- **Extension points.** Code plugs into any object that honours the contract instead of binding to one class (p. 168). See [[public-methods-implement-interfaces]].
- **One syntax for one behaviour** across classes, so callers do not look up each class's spelling (p. 166). See [[one-name-per-concept]].

Which mechanism carries a given contract, abstract class or interface, is decided on [[prefer-interfaces-for-polymorphism]].

## What it costs

The book names the trade-off itself: contracts can be overused; they make reuse more achievable, but «несколько усложняют работу» (p. 168). This wiki reads the cost in code as one more type a reader must follow; whether a contract with one implementation pays is judged on [[base-class-with-one-subclass]] and [[public-methods-implement-interfaces]].

## A defect in the book's own listing

On p. 159 the abstract method is declared `draw()` but `Circle` and `Rectangle` define `Draw()`. In a case-sensitive language that does not satisfy the contract, which is the failure the compiler is said to catch. This is this wiki's observation, not the book's.

## Source

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), ch. 8, pp. 156-159, 165-168, via [[object-oriented-thought-process]]. The quotations were checked against `raw/`. This wiki's own: the separation from Design by Contract beyond the book's warning, the reading of the cost, and the note on the `Draw`/`draw` mismatch.
