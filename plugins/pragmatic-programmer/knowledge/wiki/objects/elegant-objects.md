---
title: Elegant Objects (Bugayenko)
category: objects
summary: "Source page, no rules of its own: a deliberately radical book on objects (nouns for class names, constructors without code, small immutable objects, no static methods, getters or NULL, recovery only at entry points, classes final or abstract) that disagrees with common practice and with The Pragmatic Programmer in places."
tags: [summary, objects, elegant-objects]
sources: [elegant-objects]
created: 2026-11-02
updated: 2026-11-03
---

Bugayenko's *Elegant Objects* argues that most code written in languages called object-oriented is still procedural. It offers a set of deliberately strict rules meant to make objects real objects. This summary covers the whole book: the preface, Chapter 1, "Birth" (sections 1.1-1.3), Chapter 2, "Education" (sections 2.1-2.9), Chapter 3 (sections 3.1-3.7), Chapter 4, "Retirement" (sections 4.1-4.4), and the epilogue.

## Edition and authority

Edition read: the Russian translation, Piter, 2018, Java edition. The edition details come from this wiki's charter and were not confirmed in the text read, which starts after the title pages. The raw file is noisy OCR of a two-up scan, so every quotation on the pages drawn from it was transcribed from OCR and has not yet been checked against the page image.

The book argues from the author's practice and from worked Java examples, not from measurement. Most sections end with a reader discussion from the author's blog (section 3.1 has none, p. 116), and several of the pages here draw their limits from those objections and the author's replies.

## Thesis

- The book's single goal is maintainability, which the author measures as the time needed to understand code (p. 17). Every rule is justified by that goal, not by speed. On allocation cost the author says plainly that he prefers maintainability to speed (p. 73).
- The preface's diagnosis is that C++ and Java inherited the procedural model from C through a chain of compromises. Code still consists of statements executed in sequence and manipulating data in memory, so code written in Java, Ruby or Python is hard to maintain «поскольку оно никогда не было объектно-ориентированным» (p. 12).
- The epilogue restates the thesis as a hope: languages it calls pseudo-OOP will be replaced by stricter ones, and the change has to begin in how programmers think, not in the languages (p. 238).

## Scope and limitations

- The author warns readers to expect many contradictions and says he does not think he is right about everything (p. 13). This wiki takes that as licence to state limits the book does not state.
- The author treats his Java listings as pseudocode, because Java is not purely object-oriented in his view, and says not every recommendation fits the software a reader is writing now (p. 37).
- By the author's own admission some numbers come from his head: 2-3 methods and 5-10 constructors (p. 28), four encapsulated objects (p. 44), five public methods (p. 115). Of the 250-line limit he says the exact number matters less than being small (p. 90). The five-parameter ceiling carries no such admission (p. 34). The pages that use them say so.
- Some theses are tied to Java. The claim that all exceptions should be checked gives, by the author's own account, no practical advice in languages without checked exceptions (p. 211). [[chain-exceptions]] records the rule as the book states it for a language with checked exceptions, gives no rule for a language without them, and names the sign that survives in any language. The RAII section is framed by Java's lack of destructors (pp. 237-238).
- The book contradicts itself without saying so: its RAII example acquires a file in the constructor (p. 237), against section 1.3. [[exception-safe-release]] resolves it per setting. Two more self-disagreements are under *Where it disagrees*.

## Key takeaways

This wiki reads the book as making four claims that change code, each carried by several pages:

1. **An object stands for something; it is not a procedure container.** Names, constructors, interfaces and the ban on getters, statics and singletons all follow from [[object-as-representative]].
2. **Objects are small and do not change.** [[keep-objects-small]], [[immutable-objects]] and [[prefer-constant-objects]].
3. **Behaviour is composed, not inherited or switched on.** [[composable-decorators]], [[declarative-style]], [[final-or-abstract]] and [[no-public-constants]].
4. **Failure is loud.** No null in or out ([[never-return-null]], [[no-null-arguments]]), exceptions chained and caught only at the entry point ([[chain-exceptions]], [[recover-only-at-entry-points]]).

## Pages from Chapter 1

- [[object-as-representative]]: the concept the book rests on. An object represents the data it encapsulates; it is not a conduit for procedures over that data. A class is a factory of objects, not a template.
- [[name-classes-for-what-they-are]]: no class names ending in -er or -or, no -able, no Util/Utils (section 1.1, pp. 20-28).
- [[one-primary-constructor]]: fields are assigned in one constructor and the others delegate to it (section 1.2, pp. 28-33).
- [[constructors-without-code]]: a constructor only assigns. Work on the arguments is deferred to methods, and caching is added by a decorator (section 1.3, pp. 34-41).
- [[keep-objects-small]]: at most four encapsulated objects, at most five constructor parameters, Builder rejected as a mask for a class that is too big (pp. 26-27, 33-34, and section 2.1, pp. 42-46).

## Pages from Chapter 2

- [[keep-objects-small]] also carries section 2.1: state is identity, and identity is a few coordinates.
- [[global-data]] carries section 2.2, the class that encapsulates nothing and reaches for static calls (pp. 47-50), as the same shape seen from the object side.
- [[public-methods-implement-interfaces]]: every public method implements an interface (section 2.3, pp. 50-54).
- [[command-query-separation]] and [[builder-and-manipulator-names]]: a method either builds and is a noun, or manipulates and is a verb (section 2.4, pp. 54-64).
- [[no-public-constants]]: share functionality, not data; no public constants and no enums used to select behaviour (section 2.5, pp. 65-73).
- [[immutable-objects]] (section 2.6, pp. 74-91), with its narrower consequences on their own pages: [[mutable-hash-key]], [[failure-atomicity]], [[temporal-coupling]] (the setter form), [[null-field-hides-another-class]] and [[class-size]].
- [[tests-instead-of-documentation]]: do not document code, make it cleaner, and let the unit test be the documentation (section 2.7, pp. 93-95).
- [[prefer-fakes-over-mocks]]: fakes shipped with the interface instead of mocks (section 2.8, pp. 97-108); its definition of a unit test's job is folded into [[brittle-tests]].
- [[small-interface-with-smart-class]]: interfaces stay small, derivable shortcuts go to a smart class nested in the interface (section 2.9, pp. 109-113).

## Pages from Chapter 3

- [[fewer-than-five-public-methods]]: class size measured by public methods (section 3.1, pp. 115-116).
- [[no-static-methods]], [[no-singletons]], with the concepts [[declarative-style]] and [[composable-decorators]] (section 3.2, pp. 117-145).
- [[no-null-arguments]] and the decision [[null-object-or-optional]] (section 3.3, pp. 147-157).
- [[immutable-versus-constant-object]] and [[prefer-constant-objects]], the book's return to immutability (section 3.4, pp. 157-169).
- [[no-getters-and-setters]] (section 3.5, pp. 172-187).
- [[new-only-in-secondary-constructors]] (section 3.6, pp. 189-195).
- [[avoid-introspection-and-casting]] (section 3.7, pp. 195-200).

## Pages from Chapter 4

- [[never-return-null]] (section 4.1, pp. 202-210; section 4.2, p. 216, for -1 as a sentinel).
- [[recover-only-at-entry-points]]: fail fast rather than fail safe, and catch without rethrowing only where the outside world enters (section 4.1, pp. 206-208; section 4.2, pp. 214-223).
- [[chain-exceptions]]: wrap the caught exception as the cause, one exception type per library (section 4.2, pp. 217-219, 224-227).
- [[final-or-abstract]]: inheritance only to refine, never to extend (section 4.3, pp. 230-237).
- [[exception-safe-release]] takes section 4.4, RAII and the close protocol (pp. 237-238), into the existing page.

## Where it disagrees

- With itself: section 2.6 sets a 250-line limit (p. 89), and section 3.1 calls it not the most important measure (p. 115); [[class-size]] and [[fewer-than-five-public-methods]] divide the two. Section 1.2 puts a positivity check in the primary constructor (p. 31), while the author's reply on p. 42 says «в конструкторе не должна происходить проверка введенных данных» (transcribed from noisy OCR); [[one-primary-constructor]] moves the check into a wrapping object.
- With common practice: the book rejects Manager/Controller/Helper names, Builder, work in constructors, getters named `get`, `isX` boolean names, public constants, enums, mutable objects, mocks, static helpers, singletons, getters and setters, `instanceof`, `Optional`, local retries and concrete non-final classes. Each page resolves the disagreement per setting and most name the project or framework convention that overrides the book.
- With [[crash-early]]: a reader objects that deferring work out of the constructor breaks fail-fast (p. 41), the author replies that «отказ должен происходить не во время создания объекта, а только во время его использования» (p. 42), and his answer to another reader is to throw only when the object is put to work (p. 41). [[constructors-without-code]] resolves this per setting. In Chapter 4 the book itself argues for fail-fast (pp. 206-207), so on failure handling the two books agree, and [[recover-only-at-entry-points]] and [[crash-early]] divide the shape by whether a correct program can meet the failure.
- With [[log-and-rethrow]]: this book asks every method to catch, chain and rethrow (p. 219), and *The Pragmatic Programmer* prefers the bare call. [[chain-exceptions]] resolves this per setting.
- With [[documentation-in-the-source]]: *The Pragmatic Programmer* asks for doc comments on exports, and this book says not to document code (p. 95). [[tests-instead-of-documentation]] resolves this per setting.
- With [[name-by-role]]: the two books name methods by different tests, purpose against part of speech. [[builder-and-manipulator-names]] and [[name-by-role]] state which page owns which method.
- With [[class-invariant]]: *The Pragmatic Programmer* protects mutable state with invariants, while this book holds that mutable objects have no right to exist (p. 76). [[immutable-objects]] resolves this per setting.
- With [[inheritance-tax]]: both books distrust inheritance, for different reasons. *The Pragmatic Programmer* prices the coupling of reuse, this book the override of implemented methods. [[final-or-abstract]] and [[inheritance-tax]] divide the shape by whether the subclass overrides.

## Source

Bugayenko, *Elegant Objects*, Russian translation, Piter, 2018: preface pp. 10-13, Chapter 1 pp. 17-41, Chapter 2 pp. 42-113, Chapter 3 pp. 115-200, Chapter 4 pp. 202-238 and the epilogue on p. 238, including the reader discussions printed after each section. The characterisation above, the four takeaways, the cross-references and the per-setting resolutions are this wiki's own.
