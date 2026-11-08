---
title: Design pattern
category: complexity
summary: "Concept: a named problem, solution and consequences; a pattern applied where its problem's conditions do not hold shows as classes named for pattern roles (Factory, Strategy, Observer, Visitor) with one implementation, one caller and nothing varying behind them."
tags: [concept, patterns, trade-offs, over-engineering, anti-patterns]
paradigm: oop
sources: [object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

A design pattern is a documented solution to a recurring design problem. Weisfeld frames it as recorded best practice, so that other developers benefit from what someone has already done well (p. 285). He quotes Alexander: a pattern describes a recurring problem and the core of its solution in a way that can be used a million times, «никогда не делая это дважды одинаковым образом» (p. 286). This wiki reads that as a shape to adapt, not code to paste.

## The four elements

Following the Gang of Four, the book gives four elements (pp. 286-287):

- **Name.** A short handle for the problem, the solution and the consequences, which lets people design and discuss at a higher level of abstraction.
- **Problem.** When to apply the pattern, sometimes with a list of conditions that must hold for applying it to make sense (p. 286).
- **Solution.** The elements, their relations and collaborations, as an abstract arrangement rather than a concrete implementation.
- **Consequences.** The results and trade-offs of applying it, often in space and time, and its effect on flexibility, extensibility and portability. The book stresses that consequences are often left unstated although they are essential for weighing costs against benefits (p. 287).

The book groups the patterns into creational, structural and behavioural (p. 289), and its examples are Singleton, Adapter and Iterator, carried here on [[no-singletons]], [[hide-third-party-apis]] and [[iterator]]. The text credits the catalogue of 23 patterns to Alexander's *A Pattern Language* (p. 289); this wiki notes that the catalogue is that of *Design Patterns* (Gamma et al., 1995).

## Why the consequences element matters in code

On MVC, and then of object-oriented design generally, the book warns that a good design can become complex because so much has to be attended to in advance, and that between a sound design and a cumbersome one there is «тонкая грань» (pp. 288-289).

This wiki reads the problem and consequences elements as the test for that line. A pattern earns its indirection only where its problem is present: the variation it isolates, the incompatible interface it bridges, the structure it hides. Where the problem's conditions do not hold, the costs remain and the benefit does not arrive. In code that shows as classes named for a pattern's roles with one implementation, one caller and nothing that varies. The rule that owns that sign is [[do-not-force-a-design-pattern]]; a layer with one implementation that is not a named pattern is [[know-when-to-stop]].

## Anti-patterns

The book contrasts patterns, drawn from success, with anti-patterns, drawn from failure (pp. 297-298). It cites Koenig's two kinds: one describing a bad solution that leads to a bad situation, and one describing how to get from there to a good solution (p. 298). It quotes Ambler's Robust Artifact, documented, general, tested and supplied with examples, and far more likely to be reused, against the Reuseless Artifact, declared reusable and never reused, which should be reworked into a robust one (p. 298). Its conclusion is that anti-patterns drive review and continuous refactoring of existing designs (p. 298). This wiki keeps that as context: a claim of reusability has no sign in code, so it yields no rule here.

## Source

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), ch. 15, via [[object-oriented-thought-process]]: best practice and the Alexander quotation (pp. 285-286), the four elements (pp. 286-287), the fine line (pp. 288-289), the categories (p. 289), anti-patterns (pp. 297-298). The quotations were checked against `raw/`. This wiki's own: the reading of problem and consequences as the test for over-engineering, the pattern-named-class sign, the routing to owner pages and the correction of the catalogue attribution.
