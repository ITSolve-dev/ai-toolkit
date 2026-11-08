---
title: Refactoring, 2nd ed. (Fowler)
category: change
summary: "Source page, no rules of its own: Fowler's Refactoring, 2nd ed. (English, 2018), the catalogue of behaviour-preserving changes made in small tested steps; records its authority and limits, which chapters this wiki took from, what was left out, and where it disagrees with other sources."
tags: [summary, source, refactoring, code-smells, testing, small-steps, inheritance, catalog]
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Martin Fowler's *Refactoring: Improving the Design of Existing Code*, 2nd edition (Addison-Wesley, 2018), read in English from an e-book with a clean text layer but no printed page numbers. Pages cite the chapter, the refactoring or smell name and the PDF page from the `<!-- p. N -->` markers. Quotations are in English and were checked against `raw/`. The whole book has been ingested; this page records what each chapter contributed and what was left out.

## The book

**Thesis.** Refactoring is a change to the internal structure of code that leaves its observable behaviour unchanged, made as a sequence of small steps each of which keeps the program working, and tested after each ([[refactoring]], [[refactor-in-small-tested-steps]]). Design is not done once up front: code is kept easy to change by improving it continuously, just before and just after the work that needs it ([[preparatory-refactoring]], [[when-to-refactor]], [[easier-to-change]]). The smells of chapter 3 tell where to look; the catalogue says what exactly to change.

**Authority.** Fowler writes as a practitioner, revising his first edition of 1999; the claim that its names became the common vocabulary is this wiki's, from memory. The book argues from worked examples and experience, not from measurement. The catalogue entries are recipes he has run many times, and their mechanics are the most checkable part of the book.

**Scope.** Twelve chapters: a worked first example (ch. 1); principles: definition, when and why to refactor, performance, tooling (ch. 2); the smells (ch. 3, with Kent Beck); self-testing code (ch. 4); and a catalogue of refactorings: the first set (extract and inline, variables, declarations, ch. 6), encapsulation (ch. 7), moving features (ch. 8), organising data (ch. 9), simplifying conditional logic (ch. 10), refactoring APIs (ch. 11) and dealing with inheritance (ch. 12). Chapter 5 introduces the catalogue's format.

**Limitations for this wiki.** The examples are JavaScript; the pages take the ideas only, in this wiki's pseudocode, and language mechanics (JavaScript modules, `class` syntax, prototype details) are not transferred. The catalogue's mechanics are procedures, so many pages are `method` pages; a refactoring kept as a `rule` page needed a sign in code that Fowler usually gives only as a motivation, and most signs and limits here are therefore this wiki's own, marked on each page. The book overlaps heavily with *Code Complete*'s chapter 24 ([[code-complete]]); its claims were merged into the owners already in place rather than given pages beside them. Material on team practice, continuous integration, code ownership, legacy-code strategy and the history of refactoring tools has no sign in code and was left out.

**Key takeaways, as this wiki reads them.**

- A change that would be large is made safe by being made small: each step keeps the tests green, and a red test means stepping back, not pressing on ([[refactor-in-small-tested-steps]], [[parallel-change]], [[extract-before-changing-many-callers]]).
- Adding a feature and restructuring are separate activities, switched between deliberately ([[do-not-refactor-while-adding-features]]).
- A smell is a cue for judgement, not a verdict, and several of the second edition's smells are narrowed on purpose: repeated switches rather than every switch ([[polymorphism-or-type-switch]]), and speculative generality judged by present users ([[speculative-generality]]).
- Clarity first, speed afterwards, measured: well-factored code is easier to tune ([[refactor-first-tune-afterwards]]).
- Many refactorings come in inverse pairs, and the book's value is the condition between them: inline or extract ([[extract-function]], [[inline-function]]), parameter or query ([[parameter-or-query]]), function or command ([[function-or-command-object]]), pull up or push down ([[pull-up-method]], [[push-down-method-and-field]]), subclasses or a field ([[replace-type-code-with-subclasses]], [[subclass-that-differs-only-in-data]]), hide the delegate or remove the middle man ([[hide-delegate-or-remove-middle-man]]).
- Inheritance is used first and replaced by delegation when it starts to rub ([[replace-subclass-with-delegate]], [[replace-superclass-with-delegate]]).
- A test suite is what makes refactoring possible at all ([[self-testing-code]]).

## Chapters 1-2: the first example and the principles

From the worked example: [[split-phase]], [[replace-temp-with-query]], [[remove-loop-accumulator]], [[rename-extracted-code-for-clarity]], [[do-not-mutate-input-data]], [[exact-representation-for-money]], and the first appearance of [[replace-conditional-with-polymorphism]]. From the principles: the definition ([[refactoring]]), [[when-to-refactor]], [[preparatory-refactoring]], [[do-not-refactor-while-adding-features]], [[refactor-first-tune-afterwards]] and [[code-tuning-procedure]], [[automated-refactoring]], [[parallel-change]], and corroboration for [[replaceable-code-over-forecast]] and [[easier-to-change]].

## Chapter 3: bad smells

The smells joined the owners already in place: [[refactoring-warning-signs]] as the index, and among others [[dry]], [[routine-length]], [[limit-parameter-count]], [[global-data]], [[mutable-data]], [[divergent-change-vs-shotgun-surgery]], [[group-related-data-into-a-structure]], [[replace-primitive-with-class]], [[polymorphism-or-type-switch]], [[replace-loop-with-pipeline]], [[lazy-element]], [[speculative-generality]], [[hide-delegate-or-remove-middle-man]], [[god-class]], [[alternative-classes-with-different-interfaces]], [[class-with-only-data-or-only-behaviour]], [[inheritance-tax]], [[delegate-to-services]] and [[self-documenting-code]].

## Chapter 4: building tests

[[self-testing-code]], [[test-by-risk-not-by-method]], [[fresh-fixture-per-test]], [[one-verification-per-test]], [[adding-tests-to-existing-code]] and [[test-suite-adequacy]], with corroboration on [[code-coverage]], [[find-bugs-once]] and boundary probing in [[test-data-classes]].

## Chapters 6-9: the first set, encapsulation, moving features, organising data

Chapter 6: [[extract-function]], [[inline-function]], [[extract-variable]], [[change-function-declaration]], [[encapsulate-variable]], [[combine-functions-into-class]], [[combine-functions-into-transform]] and [[split-phase]]. Chapter 7: [[encapsulate-collection]], [[replace-primitive-with-class]], [[replace-temp-with-query]], [[substitute-algorithm]] and the extract and inline class moves on [[keep-objects-small]] and [[lazy-element]]. Chapter 8: [[move-function]], [[move-field]], [[move-statements-across-call-boundary]], [[slide-statements]], [[replace-inline-code-with-function-call]], [[identical-code-in-every-branch]], [[replace-loop-with-pipeline]] and [[remove-dead-code]]. Chapter 9: [[one-variable-one-purpose]], [[rename-widely-used-field]], [[stored-derived-data]] and [[reference-or-value]].

## Chapter 10: simplifying conditional logic

[[consolidate-conditional-expression]], [[name-complex-conditions]], [[guard-clauses]], [[replace-conditional-with-polymorphism]], [[introduce-special-case]] with [[null-object-or-optional]], the migration technique [[extract-before-changing-many-callers]], and Introduce Assertion on [[assert-the-impossible]] and [[assertion-or-error-handling]].

## Chapter 11: refactoring APIs

[[command-query-separation]] (Separate Query from Modifier), [[parameterize-function]], [[semantic-coupling]] (Remove Flag Argument), [[pass-what-the-routine-uses]] (Preserve Whole Object), [[parameter-or-query]] (Replace Parameter with Query and its inverse), [[immutable-objects]] (Remove Setting Method), [[factory-function-over-constructor]] and [[function-or-command-object]] (Replace Function with Command and its inverse). Replace Error Code with Exception and Replace Exception with Precheck are not in the second edition's printed catalogue and were not taken.

## Chapter 12: dealing with inheritance

[[pull-up-method]] (with Pull Up Field), [[pull-up-constructor-body]], [[push-down-method-and-field]], [[replace-type-code-with-subclasses]], [[subclass-that-differs-only-in-data]] (Remove Subclass), [[extract-superclass]], [[collapse-hierarchy]], [[replace-subclass-with-delegate]] and [[replace-superclass-with-delegate]]. Form Template Method joined [[shared-behavior-in-superclass-varying-step-polymorphic]], and the two delegate refactorings are cross-referenced from [[choose-an-alternative-to-inheritance]].

## Where it disagrees with other sources

- **Inheritance.** *The Pragmatic Programmer* argues against inheritance for reuse ([[inheritance-tax]], [[choose-an-alternative-to-inheritance]]); Fowler uses it first and moves to delegation when it rubs. The delegate pages resolve it per setting: one axis inside one module keeps inheritance; a second axis, a run-time change of kind or a type-instance homonym calls for delegation in both books.
- **Flag arguments.** *Code Complete* accepts a flag with a declared enumeration; Fowler counts enum and string literals as flags too. [[semantic-coupling]] resolves it by whether the caller writes a literal or passes data.
- **Whole object or values.** Fowler leans to the whole record in Preserve Whole Object and calls the choice open in Change Function Declaration; [[pass-what-the-routine-uses]] decides by McConnell's abstraction test, with Fowler's different-modules limit read as agreeing with it.
- **Command-query separation.** *Elegant Objects* bans any return from a manipulator; Fowler follows the rule "most of the time" and exempts unobservable changes such as caching ([[command-query-separation]]).
- **Immutability.** *Elegant Objects* rejects mutable objects; Fowler removes only the setters of fields that should not change ([[immutable-objects]]).
- **Switches.** Fowler narrowed the first edition's "switch statements" to repeated switches, which agrees with *Code Complete*'s view that a single case statement is not bad in itself ([[polymorphism-or-type-switch]]).

## Source

The book itself, as normalized in `raw/fowler-refactoring.md`. The thesis, scope and the claims each listed page attributes to Fowler are his; the reading of the key takeaways, the selection of what was kept, and the resolutions against other sources are this wiki's own.
