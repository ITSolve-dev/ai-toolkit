---
title: The Object-Oriented Thought Process (Weisfeld)
category: objects
summary: "Source page, no rules of its own: an introductory book on thinking in objects before learning a language (interface against implementation, a minimal public interface, private attributes, constructors that leave a stable state, composition against inheritance, abstract classes and interfaces as contracts), followed by chapters on data exchange, persistence, web clients and three design patterns."
tags: [summary, objects, object-oriented-thought-process]
sources: [object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

Matt Weisfeld's *The Object-Oriented Thought Process* teaches the concepts of object-oriented design apart from any language, method or tool. This summary covers the whole book: the introduction and chapters 1-15.

## Edition and authority

Edition read: the Russian translation of the 4th edition, Piter, 2014, 304 pages. The text layer is clean and the headings come from the PDF outline, so quotations on the pages drawn from it were checked against `raw/`. Some chapter openers carry only a PDF page marker, and the pages citing them say where a printed page number was inferred.

The book argues from the author's teaching and practice and from small examples in Java, C# .NET, VB .NET and Objective-C, not from measurement. It is an introduction: most claims are definitions and design advice at the level of a first course, and it states almost no signs in code and few limits.

## Thesis

- Object orientation is a way of thinking, and learning it does not reduce to learning a development method, a language or a set of design tools (p. 15). The author warns against moving to a language or to UML before the concepts: many programmers who call themselves C++ programmers turn out to be C programmers using a C++ compiler (pp. 15-16).
- Chapters 1-10 give the fundamental concepts (encapsulation, inheritance, polymorphism, composition), and chapters 11-15 apply them to common technologies (p. 17).
- The idea that carries most of the book's pages here is the separation of interface from implementation ([[interface-and-implementation]]): users see a minimal interface and nothing of the internals.

## Scope and limitations

- Chapters 11-14 are largely technology description (XML and JSON syntax, serialization APIs, web services, mobile and hybrid applications, client-server marshalling). This charter keeps only the few claims there that change code: [[validate-exchanged-data-against-a-declared-schema]], [[object-persistence]], and the both-sides validation folded into [[barricade]]. Chapter 14 yielded no page.
- The book's listings sometimes contradict its prose, and the pages say so: the `Iterator` listing takes a concrete list ([[iterator]]); the `Singleton` listing regulates creation through `static` while the note beside it says lifecycle should not be left to `static` ([[no-singletons]]); the `MyMailTool` adapter hands its adaptee back out ([[hide-third-party-apis]]); a sample setter silently ignores `null` and is called validation ([[object-persistence]]).
- A few factual slips are recorded rather than carried: Java's default access is called `protected` (p. 199, see [[uniform-access]]), and the catalogue of 23 patterns is credited to Alexander (p. 289, see [[design-pattern]]).
- The book repeatedly says design is not an exact science and has no single right answer (p. 187). The pages turn that into stated limits rather than into vagueness.

## Key takeaways

This wiki reads the book as making five claims that change code:

1. **Interface and implementation are separate, and the interface is as small as possible.** [[interface-and-implementation]], [[minimize-member-accessibility]], [[abstract-intent-revealing-interface]], [[hide-third-party-apis]].
2. **Attributes are private and every write goes through the owner.** [[uniform-access]], [[no-getters-and-setters]], [[class-invariant]], [[global-data]] (class attributes as the closest thing to global data).
3. **A constructor leaves the object in a stable state.** [[initialize-every-member-in-every-constructor]], [[robustness-versus-correctness]], [[shadowed-field-names]], [[prefer-deep-copy]], [[object-equality]].
4. **Composition and inheritance are chosen by is-a against has-a, and inheritance weakens encapsulation.** [[containment-or-inheritance]], [[aggregation-vs-association]], [[association-cardinality-in-field-types]], [[inheritance-weakens-encapsulation]], [[liskov-substitution-principle]], [[base-class-with-one-subclass]], [[override-that-does-nothing]], [[class-interface-coherent-abstraction]], [[near-decomposability]].
5. **Abstract classes and interfaces are contracts.** [[contract-via-abstract-methods]], [[prefer-interfaces-for-polymorphism]], [[public-methods-implement-interfaces]], [[polymorphism-or-type-switch]].

## Pages by chapter

- Ch. 1-2: [[interface-and-implementation]], [[containment-or-inheritance]], [[abstract-intent-revealing-interface]], [[hide-third-party-apis]], [[uniform-access]].
- Ch. 3: [[robustness-versus-correctness]], [[shadowed-field-names]], [[object-equality]], [[operator-overloading-meaning]], [[prefer-deep-copy]].
- Ch. 4-5: [[class-with-only-data-or-only-behaviour]], [[coupling]], [[smallest-scope-first]], [[test-scaffolding]], [[naming-conventions]], [[initialize-every-member-in-every-constructor]], [[isolate-volatile-dependencies-behind-a-layer]], [[minimize-member-accessibility]].
- Ch. 6-7: [[liskov-substitution-principle]], [[inheritance-weakens-encapsulation]], [[base-class-with-one-subclass]], [[override-that-does-nothing]], [[test-inherited-methods-in-each-subclass]].
- Ch. 8: [[contract-via-abstract-methods]], [[prefer-interfaces-for-polymorphism]], [[public-methods-implement-interfaces]], [[polymorphism-or-type-switch]], [[one-name-per-concept]], [[dry]].
- Ch. 9-10: [[aggregation-vs-association]], [[association-cardinality-in-field-types]], [[near-decomposability]], [[class-interface-coherent-abstraction]] (mixing domains), [[uniform-access]] (private attributes in notation).
- Ch. 11-13: [[validate-exchanged-data-against-a-declared-schema]], [[object-persistence]], [[barricade]].
- Ch. 15: [[design-pattern]], [[no-singletons]], [[hide-third-party-apis]] (Adapter), [[iterator]], [[do-not-force-a-design-pattern]].
- Also cited on: [[recover-only-at-entry-points]], [[null-field-hides-another-class]].

## Where it disagrees with the other sources

Each owning page resolves the disagreement per setting.

- **Singleton.** Weisfeld teaches it as the model creational pattern; *Elegant Objects* bans it. [[no-singletons]].
- **Minimal interface.** Weisfeld adds nothing until a user asks; *Code Complete* makes a member public whenever it fits the abstraction. [[minimize-member-accessibility]].
- **Accessors.** Weisfeld treats getters and setters as controlled access; *Elegant Objects* forbids them. [[no-getters-and-setters]].

## Source

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014). The introduction is cited as pp. 15-17; `raw/` marks its first page only by its PDF page, so p. 15 is inferred. The reading of the book as five claims and the grouping of pages under them are this wiki's own.
