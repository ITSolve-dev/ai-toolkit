---
title: No static methods
category: objects
summary: "Behaviour exposed as static methods or a utility class (private constructor, only static members, e.g. XUtils.doThing(x)) cannot be substituted or composed; replace it with an object that takes its inputs in the constructor, and wrap unavoidable library statics in one adapter class."
tags: [rule, static-methods, utility-class, coupling, testability]
paradigm: oop
sources: [elegant-objects]
created: 2026-11-03
updated: 2026-11-03
---

Bugayenko treats static methods as a problem as large as `NULL`, or larger, and asks that the keyword `static` not appear in one's own code at all (*Elegant Objects*, section 3.2, pp. 117, 143). The book is deliberately radical here: it says there is no justification for static methods in any situation and that performance does not count as one (p. 118). This page records the argument, then resolves the disagreement with common practice per setting.

A **utility class** is the shape this rule most often meets: a class that is only a collection of static methods, usually with a private constructor so no instance can be made, such as `java.lang.Math` (p. 132). The book says it is not a class at all, because a class is a factory of objects and a utility class makes none, and that everything said against static methods applies to it many times over (pp. 132-133).

## Rule

Do not write static methods or utility classes. Express the behaviour as an object that receives what it needs through its constructor and exposes it through an instance method (pp. 117-118). Where a library offers only static methods, wrap them in a class of your own so that the rest of your code works only with objects (p. 131).

The book's summary is that static methods worsen maintainability (p. 118). It argues it through the contrast of imperative and declarative style (see [[declarative-style]]):

- **Substitution.** An object can be passed as a constructor argument; a static method cannot (p. 127). A static `between()` built from static `min()` and `max()` cannot be given a different algorithm without rewriting it, short of passing a fourth parameter, which the author calls ugly (p. 127). A `Between` object can take its inner number through a second constructor (p. 126).
- **Lazy evaluation.** A static call computes at once. An object declared but not asked for its value may never compute it, so code that conditionally uses a result does no wasted work (pp. 124-125).
- **Contagion.** The author argues the two styles cannot be mixed: once reusable components are static methods, a class built on top of them has to call them directly inside itself, so it cannot use constructors and encapsulation for them, and the static code spreads (p. 130). He compares static methods to a tumour (p. 130).
- **Composition.** Static methods cannot be composed into larger objects, which defeats [[composable-decorators]] (p. 142).

This wiki reads the substitution argument as the one that is checkable in code and holds outside the book's paradigm: a direct static call is a hard-coded dependency that a test or a caller cannot replace.

## Sign in code

- A method declared static in your own code. The book exempts none, static factories included (p. 143).
- A class whose members are all static, often with an empty private constructor (p. 132).
- A class with fields whose method calls `SomeUtils.method(...)` directly in its body, so that the callee cannot be supplied from outside, other than the single adapter class that wraps a library's static method (repair 3).
- A static method composed from other static methods, such as `between` calling `max` and `min` (p. 123).

This wiki assigns the neighbouring cases as follows. This page owns the declaration of static behaviour and direct calls to static methods. A read of the wall clock is [[test-is-first-client]], whatever its syntax, except a zero-field class whose methods read the clock, which is [[global-data]] (*Elegant Objects*' `Year`). Any other static call is decided by whether it reaches a mutable external resource ([[global-data]]) or not ([[no-static-methods]]). A call that reaches a mutable external resource (file system, database, network, service) is [[global-data]] whatever its syntax, static or not. [[no-static-methods]] owns static calls to computation that reaches no external resource. A static *field*, a singleton accessor or other global data read in a body is [[global-data]], and so is a class with no instance fields whose methods reach static or global calls. A class that declares a static instance of itself is [[no-singletons]]. `new` of a collaborator inside a method is [[new-only-in-secondary-constructors]].

## When not to apply

The book admits no exceptions (p. 118). This wiki resolves the disagreement per setting:

- **Functional code and languages where free functions are the unit of design.** The book's argument rests on objects being the units of composition. Where functions are first-class values passed as arguments, the substitution argument is met by passing the function, which the book acknowledges is possible in Java 8, Ruby, PHP and Python while saying it has nothing to do with OOP (p. 127, footnote). For `paradigm: fp` code this page does not apply.
- **Pure, trivial computations with no dependency worth replacing**, such as a numeric maximum. Replacing them buys substitution nobody needs. The book's own position is the opposite; this limit is this wiki's, and it holds where the project's convention accepts such helpers.
- **Published library APIs where discoverability matters.** In a reader's comment, the objection is that a single `StringUtils` with IDE autocompletion is easier for other teams to learn than many small classes; the author agrees that IDEs are built for utility classes and offers no alternative (pp. 142-143). This wiki takes the reader's side for a library API published to other teams, and the author's inside an application.
- **Resource-constrained code** (firmware, mobile, games), where allocating short-lived objects has a measured cost. A reader raises this; the author answers that programmer time costs more than hardware (pp. 144-145). This wiki takes the reader's side where a profile shows the allocation matters, and the author's elsewhere.
- **The single adapter class that wraps a library's static method** (repair 3) is where that call belongs; its call is not sign 3.
- **A static entry point or callback the language or framework requires;** keep it to forwarding into objects.
- A project convention that sanctions static factories or helpers overrides this page.

## Repair

1. Turn the static method's parameters into constructor arguments stored in final fields, and its body into an instance method named for what the object returns rather than what it does (pp. 117-118; naming per [[builder-and-manipulator-names]]).
2. Callers that used the static method receive the object, or a factory for it, through their own constructors, so it can be replaced.
3. For a library's static method, write one adapter class that implements an interface your code already uses and calls the static method inside; only that class calls it (p. 131). The book shows `FileLines` implementing an iterable of strings around Apache Commons' `FileUtils.readLines()`.

## Before and after

```
class WebPage
  static read(uri)
    response = http get uri
    return response as text

html = WebPage.read("http://example.com")
```

```
interface Page
  content()

class WebPage implements Page
  field uri
  constructor(uri)
  content()
    response = http get this.uri
    return response as text

html = new WebPage("http://example.com").content()
```

`WebPage` is now the project-owned wrapper around HTTP, the one place [[global-data]] lets the direct call stay; callers hold a `Page`.

Wrapping a library static, after the book's `FileLines` (p. 131):

```
// before: callers everywhere
lines = FileUtils.readLines(file)
```

```
// after: one adapter, the only place the static is called
class FileLines implements Iterable of String
  field file
  iterator()
    return FileUtils.readLines(this.file).iterator()

lines = new FileLines(file)
```

## Source

- [[elegant-objects]], section 3.2: `WebPage` before and after, pp. 117-118; no justification in any situation, performance excluded, p. 118; `between` and `Between`, pp. 123-126; substitution through a constructor, pp. 126-127; contagion, p. 130; isolating library statics with `FileLines`, p. 131; utility classes, pp. 132-133; composition, p. 142; reader comments on IDE discoverability and on performance, pp. 142-145. OCR noise is heavy in these pages.
- This wiki's own: the sign list as worded (sign 1 rests on the book's advice on p. 143 never to use the keyword static in one's own code), the adapter, entry-point and published-library resolutions, the assignment of neighbouring cases, all limits except the two reader objections (which are the book's printed comments, with this wiki choosing the side per setting), the pseudocode.
