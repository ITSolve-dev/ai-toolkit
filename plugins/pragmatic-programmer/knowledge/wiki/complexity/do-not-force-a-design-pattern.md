---
title: Do not force code into a design pattern
category: complexity
summary: "Pattern scaffolding (a factory, strategy interface, observer, visitor, or a proxy that passes every call through) with one implementation and one caller, or a diff that restructures working code into pattern roles, adding classes, while the behaviour and the number of variants stay the same."
tags: [rule, design-patterns, accidental-complexity, speculative-design]
paradigm: oop
sources: [code-complete, object-oriented-thought-process, larman-applying-uml-and-patterns]
created: 2026-11-06
updated: 2026-11-07
---

McConnell recommends design patterns as ready-made abstractions: they reduce complexity because naming one ("this uses Factory Method") conveys a whole set of interactions, they reduce errors by standardising details that surface only after solving a problem several times, they suggest options to a designer who scans the list, and they let developers discuss design at a higher level (pp. 99-101). He then names two traps, which are this page's rule (pp. 101-102).

## Rule

- **Forcing code to fit a pattern.** A small change that brings code into line with a known pattern can make it clearer, but «если адаптация кода к стандартному шаблону требует слишком крупного изменения, это может привести к усложнению программы» (p. 101).
- **Using a pattern for its own sake**: «применение шаблона, продиктованное не целесообразностью, а желанием испытать шаблон в деле» (p. 102).

Weisfeld's *The Object-Oriented Thought Process* gives the reason from the side of the pattern's own description. Of its four elements (name, problem, solution, consequences), the problem may list conditions that must hold for the pattern to make sense, and the consequences, its costs and trade-offs, are often left unstated though they are essential to weighing it (pp. 286-287). On MVC he warns that between a sound design and a cumbersome one there is «тонкая грань» (pp. 288-289). This wiki reads that as this page's test: a pattern whose problem is absent keeps its costs and loses its benefit. The concept is [[design-pattern]].

Larman closes his GoF case studies with the same caution: "there have been reports of designers excessively force-fitting patterns in a creative frenzy of pattern-itis" (35.10, PDF p. 818). His own conclusion is that patterns "require study in multiple examples to be well-digested", and that the case studies do not show the correct solution, since "there isn't a single best solution"; their point is that design "can be reasoned through by core principles such as low coupling and the application of patterns" (p. 818). This wiki reads his chapter 35 designs as showing the order this page asks for: each pattern there arrives after a concrete variation already in the problem (several remote services that may fail, several device vendors, several payment kinds, several kinds of square), never ahead of it. He proposes a `CacheStrategy` family only for a designer who "is unsure which approach to use and wants to experiment with alternatives" (35.2, PDF p. 788); this wiki reads the family as scaffolding of this page once that experiment is over and one strategy remains.

## Sign in code

This wiki's signs, since the book names none:

- A pattern's roles exist with one occupant each: a strategy interface with one implementation, a factory that only ever builds one class, an observer list with one subscriber registered at one place, a proxy or decorator whose every method passes the call through unchanged.
- Names of pattern roles (`OrderStrategy`, `ReportVisitor`, `ConfigFactory`) over code whose behaviour does not vary.
- A change whose only effect is to introduce pattern roles (new interfaces or classes named for roles) while every call site keeps one variant.
- A diff that restructures working code into pattern roles, adding classes, while the behaviour and the number of variants stay the same: the shape-bending refactor of p. 101.

This wiki assigns the neighbouring cases as follows. A named pattern role (factory, strategy, observer, visitor) with one occupant is [[do-not-force-a-design-pattern]], in a diff or in code as it stands; any other single-implementation layer is [[know-when-to-stop]] where a change adds it and [[minimal-but-complete-functionality]] in code as it stands. For an interface or adapter in front of a stable, pervasive dependency, [[low-coupling]] supplies Larman's reason that the coupling was not worth removing. An abstract base class with one subclass, template method included, is [[base-class-with-one-subclass]], even when it plays a pattern role.

## When not to apply

- The variation is present now: two or more implementations, or a test double that genuinely needs the seam. The book's benefits then hold.
- A class used from another module, or one a test substitutes, takes an interface even with one implementation; [[public-methods-implement-interfaces]] owns that setting. This page applies to scaffolding used only inside its module and never substituted. The resolution is this wiki's own.
- The project's framework mandates the shape (a plugin registry, a framework callback); the scaffolding is the framework's, not a choice. The same holds where the pattern is a convention every module of the project follows: removing it in one place makes that place the odd one. The convention case is this wiki's own.
- A small adjustment that makes code match a pattern a reader will recognise is what the book endorses (p. 101).
- A seam justified by a stated, current need is not this page; a seam justified by a forecast is owned by [[replaceable-code-over-forecast]]. This page owns scaffolding with no justification stated at all, and the shape-bending refactor.
- The layer confines a third-party product or wraps an external resource. [[hide-third-party-apis]] and [[global-data]] own those shapes, and one implementation is normal there. This limit is this wiki's own.

## Repair

Collapse the pattern to the direct code: call the one implementation, construct the one class, invoke the one subscriber. Reintroduce the pattern when a second case arrives.

## Before and after

```
interface TaxStrategy
    function tax(amount)
class FlatTax implements TaxStrategy
    function tax(amount) = amount * RATE
class TaxStrategyFactory
    function create(): TaxStrategy = new FlatTax()

total = amount + TaxStrategyFactory().create().tax(amount)
```

```
function tax(amount) = amount * RATE

total = amount + tax(amount)
```

## Source

[[code-complete]], section 5.3, Russian edition, pp. 99-102. Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]], ch. 15, pp. 286-289: the four elements, the conditions and the unstated consequences, the fine line; the quotation was checked against `raw/`; reading the problem and consequences elements as this page's test is this wiki's own. Larman, *Applying UML and Patterns*, 3rd ed., via [[larman-applying-uml-and-patterns]], 35.10, PDF p. 818 (pattern-itis, no single best solution, core principles) and 35.2, PDF p. 788 (the experimental `CacheStrategy`); the quotations are in English and were checked against `raw/`; the reading of his designs as variation first and pattern second, and of the cache family as scaffolding once one strategy remains, are this wiki's own. The benefits and the two traps are the book's; the signs, the limits other than p. 101, the shape-bending sign as worded, the pass-through proxy sign, the ownership lines against [[replaceable-code-over-forecast]], [[hide-third-party-apis]], [[global-data]], [[know-when-to-stop]] and [[base-class-with-one-subclass]], the resolution against [[public-methods-implement-interfaces]], and the repair are this wiki's own. Related: [[know-when-to-stop]], [[proxy]], [[abstract-factory]].
