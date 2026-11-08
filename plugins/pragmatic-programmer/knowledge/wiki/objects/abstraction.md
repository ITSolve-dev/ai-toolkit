---
title: Abstraction and encapsulation
category: objects
summary: "Abstraction lets a reader work with a routine, class or package interface while ignoring irrelevant detail; encapsulation forbids seeing past it. An interface that makes a caller handle parts at the wrong level of detail lacks the first."
tags: [concept, abstraction, encapsulation, interfaces, levels]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

*Code Complete* defines abstraction as the ability to use a concept while ignoring some of its details, and working with different details at different levels (p. 86). Its point in terms of complexity: «С точки зрения сложности, главное достоинство абстракции в том, что она позволяет игнорировать нерелевантные детали.» (p. 86)

## Three levels

The book places abstraction at the interfaces of routines, classes and packages, which it maps onto a doorknob, a door and a house (pp. 86-87). A base class lets a reader focus on what derived classes share; a good class interface lets one use the class without its internals; a routine interface gives the same at a finer grain, and a package or subsystem interface at a coarser one (p. 86). The failure the book names is building systems "at the level of wood fibres and varnish molecules": without more general abstractions the system becomes too complex to understand (p. 87).

This wiki reads the level as checkable at a call site: if callers of a class repeatedly assemble its lower-level parts themselves (open, seek, read, parse, close around a "load config" need), the abstraction is missing at that level. The rule page that owns that shape is [[abstract-intent-revealing-interface]].

## Encapsulation

The book draws the difference in two sentences: abstraction says «Вы можете рассмотреть объект с общей точки зрения», encapsulation adds «Более того, вы не можете рассмотреть объект с иной точки зрения» (p. 87). Encapsulation is what keeps the simplified view from being bypassed; it manages complexity by forbidding access to it (p. 87). The rules that follow from it are on [[information-hiding]], [[hide-secrets-behind-one-access-point]], [[uniform-access]] and [[semantic-encapsulation-violation]].

## Inheritance and polymorphism as abstraction

The book presents inheritance as a complement to abstraction: general routines for what all doors share (`Open()`, `Close()`), specific ones for particular doors, with the language resolving which applies at run time, which is polymorphism (p. 88). Its heading limits it to where it simplifies the design, and it warns that misapplied inheritance does considerable harm (p. 88). The rules on when to choose it are on [[choose-an-alternative-to-inheritance]], [[inheritance-tax]] and [[liskov-substitution-principle]].

## Related

[[abstract-data-type]], [[coupling]], [[cohesion]], [[design-heuristics]], [[mixed-abstraction-levels-in-interface]], [[interface-and-implementation]].

## Source

[[code-complete]], section 5.3, Russian edition, pp. 86-88. The call-site reading of a missing level is this wiki's own.
