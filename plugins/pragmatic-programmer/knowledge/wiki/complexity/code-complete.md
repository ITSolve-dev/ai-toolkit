---
title: Code Complete (McConnell)
category: complexity
summary: "Source page, no rules of its own: McConnell's Code Complete, 2nd ed., Russian edition, a broad construction handbook whose thesis is managing complexity; records its authority and limits, which chapters this wiki took from, what was left out, and where the book disagrees with other sources."
tags: [summary, source, construction, defensive-programming, variables, naming, control-structures, testing, debugging, refactoring, performance, comments, design]
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-07
---

Steve McConnell's *Code Complete*, 2nd edition, read in the Russian edition (889 pages, 35 chapters). Citations on other pages name the printed page of this edition. The whole book has been ingested; this page records what each chapter contributed and what was left out.

## The book

**Thesis.** Managing complexity is software's primary technical imperative ([[managing-complexity]]), and construction (detailed design, coding, debugging, developer testing and integration) is where most of it is won or lost. The closing chapter restates the threads: complexity, conventions, readability, programming *into* a language, and iteration ([[coding-conventions]], [[code-for-the-reader]], [[program-into-the-language]]).

**Authority.** McConnell writes as a practitioner, but leans on published research far more than the other sources here: defect studies, inspection rates, maintenance figures and productivity data, with a bibliography per chapter. That makes many of its claims checkable. Many of the figures date from the 1970s to the 1990s, and this wiki keeps them as the book's support, not as current measurements.

**Scope.** Seven parts: foundations and prerequisites (ch. 1-4), high-quality code (design, classes, routines, defensive programming, pseudocode; ch. 5-9), variables and data types (ch. 10-13), statements and control structures (ch. 14-19), code improvement (quality, collaborative construction, testing, debugging, refactoring, tuning; ch. 20-26), system considerations (size, management, integration, tools; ch. 27-30), and craftsmanship (layout, self-documenting code, character, themes; ch. 31-35).

**Limitations for this wiki.** Its examples are in C++, Java and Visual Basic, and its language-specific advice is not transferred (charter: Scope). Large parts concern requirements, process, team, management and personal character, which have no sign in code and were left out. Formatting (ch. 31) is mostly mechanical style that tooling catches. Several quotations were transcribed from extracted text and are flagged on their pages for checking against the page image.

**Key takeaways, as this wiki reads them.**

- A routine or class is judged by whether the reader can safely ignore most of the rest of the program while working on it ([[managing-complexity]], [[information-hiding]], [[class-interface-coherent-abstraction]]).
- Defensive code is a choice of boundary and of reaction, made once for the system ([[barricade]], [[assertion-or-error-handling]], [[robustness-versus-correctness]], [[consistent-error-handling-strategy]]).
- Control structures stay readable when nesting, decision points and loop bodies are kept small and conditions are named ([[tame-deep-nesting]], [[decision-point-count]], [[name-complex-conditions]], [[loop-length-and-nesting]]).
- Testing and debugging are methods, not luck ([[structured-basis-testing]], [[boundary-value-analysis]], [[debugging-procedure]], [[fix-the-root-cause]]).
- Performance work comes after measurement and at the right level ([[premature-code-tuning]], [[code-tuning-procedure]]).
- A comment says what the code cannot; code that needs explaining is rewritten first ([[self-documenting-code]], [[comment-why-not-how]], [[rewrite-tricky-code]]).
- Design warning signs are cues to read, not verdicts ([[design-warning-signs]]).

## Chapters 1-4: foundations and key construction decisions

What this wiki took from them: the source code as the one description that is always current ([[source-code-as-the-authoritative-description]], ch. 1); reuse before writing your own ([[use-existing-components-before-writing-your-own]], ch. 2) and the incremental growth metaphor ([[tracer-code]], ch. 2); from the architecture section 3.5, the decisions that show in code, namely [[consistent-error-handling-strategy]], [[fault-tolerance-techniques]], [[uniform-robustness-level]], [[single-owner-of-data-access]], [[logic-testable-without-ui]] and [[anticipate-likely-changes]]; and from ch. 4, [[program-into-the-language]].

Left out on purpose: metaphors beyond the incremental one, requirements, the prerequisite checklists and the choice of language, which have no sign in code. Architecture — layering, subsystem splitting, dependency rules between modules — is left out under the 2026-11-06 scope; pages kept from section 3.5 and chapter 5 apply a rule inside a module and name the architecture as a setting.

## Chapter 5: design in construction

What this wiki took from it (pp. 74-117): [[managing-complexity]], [[minimal-but-complete-functionality]], [[limit-fan-out]], and [[isolate-volatile-dependencies-behind-a-layer]] from the design characteristics (5.2); the heuristics of 5.3, gathered on [[design-heuristics]], with [[abstraction]], [[information-hiding]], [[hide-secrets-behind-one-access-point]], [[class-data-versus-global-data]], [[circular-dependency]], [[status-variable-as-enumeration]], [[semantic-coupling]], [[coupling]], [[cohesion]] and [[do-not-force-a-design-pattern]]; from the practices of 5.4, [[top-down-and-bottom-up-design]], [[throwaway-prototype]] and [[design-notes-in-code-headers]]; and the chapter checklist, folded into [[design-heuristics]].

## Chapter 6: working classes

What this wiki took from it (pp. 120-157): abstract data types ([[abstract-data-type]], [[replace-direct-data-manipulation-with-adt]], [[adt-instances-without-classes]], [[storage-independent-names]]); good class interfaces ([[class-interface-coherent-abstraction]], [[mixed-abstraction-levels-in-interface]], [[provide-opposite-operations]], [[semantic-interface-to-programmatic]], [[minimize-member-accessibility]], [[uniform-access]], [[semantic-encapsulation-violation]]); containment and inheritance ([[containment-or-inheritance]], [[private-data-not-protected]], [[liskov-substitution-principle]], [[override-that-does-nothing]], [[do-not-reuse-names-of-non-overridable-methods]], [[subclass-that-differs-only-in-data]], [[base-class-with-one-subclass]], [[deep-inheritance-hierarchy]], [[multiple-inheritance-only-for-mixins]]); and reasons to create a class ([[reasons-to-create-a-class]], [[god-class]], [[class-with-only-data-or-only-behaviour]]).

Left out on purpose: class mechanics specific to one language.

## Chapter 7: high-quality routines

What this wiki took from it (pp. 158-181): reasons to create a routine ([[extract-routine-to-name-a-step]]), cohesion ([[routine-cohesion]]), names ([[routine-names]]), length ([[routine-length]]), the parameter guidelines ([[parameter-order]], [[remove-unused-parameters]], [[do-not-reuse-parameters-as-working-variables]], [[state-the-contract]], [[limit-parameter-count]], [[pass-what-the-routine-uses]], [[match-arguments-to-parameters]]), the choice between function and procedure ([[function-or-procedure]]), return values ([[every-path-sets-the-return-value]]), and the chapter's checklist as a procedure ([[routine-review-checklist]]).

## Chapter 8: defensive programming

The chapter's frame is careful driving: a routine should not break when handed bad data, even when the data was spoiled by another program (p. 182). It ranks defensive code below not introducing defects in the first place, and treats it as an addition to design, pseudocode and tests written before code (p. 184).

What this wiki took from it (pp. 182-208):

- [[barricade]]: validate at a chosen boundary, assume clean data behind it; public methods of a class as the class-level barricade (pp. 198-200).
- [[convert-input-at-entry]]: turn input strings into their proper type at the moment of input (p. 199).
- [[assertion-or-error-handling]]: handlers for expected events, assertions for events that must never occur; assertions as executable documentation of pre- and postconditions (pp. 184-188).
- [[assertion-side-effects]]: no executable code inside an assertion (pp. 186-187).
- [[assert-then-handle-anyway]]: in large, long-lived systems the same condition is asserted and then handled (p. 188).
- [[robustness-versus-correctness]]: the menu of reactions to a bad value, from a neutral value to shutdown, chosen by what a wrong result costs (pp. 189-192).
- [[consistent-error-handling-strategy]]: the reaction is an architectural decision, applied consistently, with every return code checked (pp. 190-192, 197-198).
- [[exceptions-for-the-exceptional]], [[exception-at-the-interface-abstraction]], [[exception-message-carries-context]], and the empty-catch rule folded into [[crash-early]] (pp. 193-198).
- [[offensive-programming]] and [[switchable-debug-aids]]: loud failures during development, debug code that can be switched off cleanly (pp. 200-204).
- [[defensive-code-in-production]]: which checks stay in the release and which go (pp. 204-205).
- The chapter closes with a warning against too much defence: excess checks make code large, slow and more complex, and defensive code has defects of its own (p. 206). This wiki records that inside [[barricade]] and [[caller-owns-the-precondition]].

## Chapter 9: the Pseudocode Programming Process

The procedure for building one routine from intent-level pseudocode (pp. 209-227): [[pseudocode-programming-process]]. Its style rules for pseudocode, which become the routine's comments, are folded into [[comment-why-not-how]]; its calibration of 2-10 code lines per comment, and the repair when a block outgrows it, into [[extract-routine-to-name-a-step]].

At the check step (p. 223) the chapter sets understanding against superstition: about 5% of errors lie in hardware, compilers or the OS (after Ostrand and Weyuker, 1984), so suspect your own code first, and know the role of every line. This wiki folded that into [[select-isnt-broken]] and [[programming-by-coincidence]]. At error removal it prefers rewriting a method whose behaviour cannot be explained to patching it (p. 224): [[rewrite-a-method-you-do-not-understand]].

## Chapter 10: general principles of using variables

In this chapter "variable" covers both objects and built-in types (p. 231). What this wiki took from it (pp. 230-251):

- Initialization (10.3, pp. 233-237) and persistence (10.5, p. 245): [[initialize-close-to-first-use]]; constructor initialization stays on [[initialize-every-member-in-every-constructor]].
- Span and live time (10.4, pp. 238-243): [[keep-variable-live-time-short]].
- Narrowest scope first (10.4, pp. 243-245): [[smallest-scope-first]], with globals on [[global-data]].
- Binding time (10.6, pp. 246-247), which completes the first treatment on p. 104: [[binding-time]].
- One purpose per variable and hybrid coupling (10.8, pp. 249-250): [[one-variable-one-purpose]], [[hybrid-coupling]].
- Data shapes and control structures (10.7, pp. 247-248): after Jackson (1975), sequential data matches a sequence of statements, selective data matches `if`/`case`, and iterative data matches loops. This wiki found no sign in code it could state without a forecast, so the idea is recorded here and not on a page of its own.

Left out on purpose: the data-literacy quiz and reading list (10.1); implicit declarations, `Option Explicit` and compiler warnings, which are rules of a language or toolchain; memory fill patterns such as 0xCC and 0xDEADBEEF and memory-access checkers (p. 237), tooling for manual memory management; and unused variables (p. 250), which a linter catches.

## Chapter 11: the power of variable names

What this wiki took from it (pp. 253-281):

- Names that say what the variable holds (11.1, pp. 253-255): [[name-describes-what-the-variable-represents]]; length by scope (pp. 255-256): [[name-length-matches-scope]]; computed-value qualifiers, `Count`/`Index` over `Num` and antonym pairs (pp. 256-257): [[computed-value-qualifier-at-end]].
- Specific kinds of data (11.2, pp. 257-263): [[loop-index-names]], [[status-variable-not-flag]], [[temporary-variable-names]], [[boolean-variable-names]], [[constant-names-abstract-not-value]].
- Why conventions pay, when to adopt one and what it encodes (11.3-11.4, 11.7, pp. 263-269, 278-280): [[naming-conventions]]; type names against variable names (pp. 265-266): [[type-name-vs-variable-name]]; input-only parameters (p. 267): [[mark-input-only-parameters]].
- Standardized prefixes (11.5, pp. 272-274): the bound prefixes on [[range-bound-names]], the prefix trap folded into [[naming-conventions]]. The concrete prefix schemes are a language's style and are left out.
- Short names and names to avoid (11.6-11.7, pp. 274-279): [[abbreviation-discipline]], [[names-differ-by-more-than-a-character]], [[similar-meaning-names]], [[numbered-names]], [[misleading-or-arbitrary-names]].

## Chapter 12: fundamental data types

What this wiki took from it (pp. 283-308):

- Magic numbers, characters and strings, and named constants (12.1, 12.4, 12.7, pp. 283, 289, 299-301): [[named-constants-over-literals]], which now owns the bare literal that [[binding-time]] first named.
- Integers (12.2, pp. 284-286): [[integer-overflow-and-division]]; floating point (12.3, pp. 286-288): [[floating-point-precision]], [[exact-representation-for-money]].
- Strings (12.4, pp. 289-290): [[one-internal-string-format]]; substring endpoints are folded into [[array-index-discipline]].
- Boolean variables (12.5, pp. 292-293): [[name-complex-conditions]].
- Enumerated types (12.6, pp. 294-299): [[enum-instead-of-codes-and-flags]], [[enum-sentinels-and-gaps]].
- Arrays (12.8, pp. 301-303): [[array-index-discipline]].
- Programmer-defined types (12.9, pp. 303-308): [[define-domain-types]].

Left out on purpose: C string handling, null terminators and language-specific string and character-set choices (pp. 290-291), which are rules of a language.

## Chapter 13: unusual data types

What this wiki took from it (pp. 310-335):

- Structures (13.1, pp. 310-314): [[group-related-data-into-a-structure]].
- Pointers (13.2, pp. 314-326): the language-independent advice on naming participants and simplifying access chains is [[explaining-variable]]. Isolating pointer operations in routines and wrapping allocation and release with checks (dog tags, garbage fill, a list of allocated pointers, the memory parachute) is [[isolate-unsafe-memory-operations]], which applies only where code manages memory by hand. Avoiding casts and generic pointer types, stated for C, is carried to typed code in general on [[avoid-type-casts]]. Pointer arithmetic and the remaining C++ and C specifics are language rules and are left out.
- Global data (13.3, pp. 326-335): merged into [[global-data]]; access routines at the domain level are [[access-routines-at-domain-level]].

## Chapter 14: organizing straight-line code

What this wiki took from it (pp. 338-345):

- Statements whose order matters (14.1, pp. 338-342): making dependencies obvious through data flow, naming and parameters, with comments and status flags as fallbacks, merged into [[pass-state-dont-hoard-it]].
- Statements whose order does not matter (14.2, pp. 342-344): the Principle of Proximity and the box test, merged into [[keep-variable-live-time-short]], which already owned the interleaved shape from section 10.4.

## Chapter 15: using conditionals

What this wiki took from it (pp. 346-358):

- `if` statements (15.1): [[nominal-path-first]], [[no-empty-then-branch]], [[document-the-missing-else]]; boolean functions for complex tests, merged into [[name-complex-conditions]]; ordering a chain by frequency, [[order-branches-by-frequency]]; the final `else` that catches the unexpected, [[default-branch-catches-the-unexpected]].
- `case` statements (15.2): [[case-or-if-chain]], [[order-branches-by-frequency]], [[keep-case-arms-short]], [[default-branch-catches-the-unexpected]], [[avoid-case-fall-through]].
- The chapter checklist as a procedure (pp. 357-358): [[conditional-statement-checklist]].

## Chapter 16: controlling loops

What this wiki took from it (pp. 359-377):

- Choosing the kind of loop (16.1): [[loop-with-exit-in-the-middle]], [[for-or-while]].
- Controlling the loop (16.2): the black-box idea, [[loop-as-black-box]]; [[loop-header-holds-only-control]]; initialization directly before the loop, merged into [[initialize-close-to-first-use]]; [[loop-housekeeping-at-one-end]]; [[break-and-continue]]; [[do-not-use-loop-index-after-loop]]; meaningful index names and index cross-talk, merged into [[loop-index-names]]; loop length and nesting, [[loop-length-and-nesting]].
- The book disagrees with itself on reading an index after its loop: chapter 11 names the surviving counter `recordCount` (p. 258), chapter 16 forbids depending on the index's final value (p. 370). [[loop-index-names]] and [[do-not-use-loop-index-after-loop]] resolve it by who sets the value: a counter the body increments may be read, a `for` loop's own index may not.

Safety counters (p. 371): [[safety-counter]].

Left out on purpose: building a loop from the inside out (16.3) and the correspondence between loops and arrays (16.4), which have no sign in code.

## Chapters 17-19: unusual control structures, table-driven methods, general control issues

What this wiki took from them: multiple returns ([[guard-clauses]]), recursion ([[recursion-or-iteration]], [[recursion-safeguards]], and the recursion case of [[safety-counter]]) and `goto` ([[goto-as-last-resort]], [[error-exits-sharing-cleanup]]) from ch. 17; table access ([[choose-table-access-scheme]], [[isolate-table-key-computation]], [[stair-step-lookup-boundaries]], [[describe-variants-in-data-not-subclasses]], [[drive-repeated-dispatch-from-a-table]]) from ch. 18; and from ch. 19, boolean expressions ([[test-a-value-by-its-kind]], [[prefer-positive-conditions]], [[guard-before-the-guarded-operand]], [[order-comparisons-along-the-number-line]]), nesting ([[tame-deep-nesting]]), [[structured-programming]] and [[decision-point-count]].

## Chapters 20-22: quality, collaborative construction, developer testing

What this wiki took from them: [[quality-characteristics-trade-offs]] and [[defect-detection-techniques-are-complementary]] (ch. 20); [[code-inspection]] (ch. 21); and from ch. 22, [[developer-testing]], [[structured-basis-testing]], [[data-flow-testing]], [[variable-state-anomalies]], [[equivalence-partitioning]], [[boundary-value-analysis]], [[test-data-classes]], [[code-coverage]], the clean/dirty-test material in [[test-the-contract]], [[test-values-checkable-by-hand]], [[regression-testing]], the defect-concentration part of [[metric-outlier-review]], [[where-defects-come-from]], [[test-code-is-defect-prone]], [[test-scaffolding]] and [[perturb-state-to-expose-uninitialized-data]].

Left out on purpose: review meeting logistics, pair-programming advice and team roles, which have no sign in code.

## Chapter 23: debugging

What this wiki took from it (pp. 527-550):

- Debugging as the scientific method, the five-step procedure, the hypothesis tips and the rules before fixing (23.2-23.3): merged into [[debugging-procedure]]; stabilising and reducing a failure, [[stabilize-the-error]]; halving the code and the versions, merged into [[binary-search-debugging]]; brute force after a time limit, [[timebox-quick-debugging]].
- Fixing (23.3): the special case keyed on one input, merged into [[fix-the-root-cause]]; [[one-change-at-a-time]], with voodoo programming; checking the fix, the regression test and similar defects, merged into [[after-a-surprising-bug]].
- Psychological considerations (23.4): [[mental-set-in-debugging]]; psychological distance and Table 23-1, merged into [[names-differ-by-more-than-a-character]].
- Tools (23.5): diff, profiler and debugger are folded into [[debugging-procedure]]; compiler warnings, [[do-not-silence-warnings]].

Left out on purpose: the chapter's material on programmers and teams, which has no sign in code, and descriptions of particular tools beyond what the method needs.

## Chapter 24: refactoring

What this wiki took from it (pp. 551-571):

- The definition, the Main Rule of Software Evolution and what is not refactoring (24.1, 24.5): merged into [[refactoring]].
- Reasons to refactor (24.2): [[refactoring-warning-signs]], which routes each sign to its owner; new owners from this list are [[tramp-data]], [[replace-primitive-with-class]] and [[hide-delegate-or-remove-middle-man]]. Setup and takedown code around a call, and passing an object or its fields, merged into [[pass-what-the-routine-uses]]; repeated case statements and parallel hierarchies, into [[polymorphism-or-type-switch]]; a subclass using little of its parent, into [[delegate-to-services]]; code that might be needed someday, into [[replaceable-code-over-forecast]].
- Specific refactorings (24.3): those with a sign were folded into owner pages: encapsulate collection into [[class-invariant]]; `break`/`return` instead of a control flag into [[break-and-continue]]; return as soon as the answer is known into [[guard-clauses]]; boolean variables and functions into [[name-complex-conditions]]. The rest of the catalogue repeats Fowler by name and adds no sign; it is left out.
- Safe refactoring (24.4): merged into [[refactor-in-small-tested-steps]]; the risk scale and small changes, [[scale-review-to-refactoring-risk]].
- Refactoring strategies (24.5): [[where-to-refactor]].

Consolidating a fragment duplicated at the end of both branches of an `if` (p. 560) is [[identical-code-in-every-branch]].

## Chapter 25: code-tuning strategies

What this wiki took from it (pp. 572-594):

- Tuning during writing, the Pareto figures and the myths (25.2): [[premature-code-tuning]], with its selection condition against [[fastest-algorithm-is-not-always-best]].
- The levels of performance work and the common sources of inefficiency (25.1, 25.3): [[fix-performance-at-the-right-level]].
- Measurement, iteration and the tuning procedure (25.4-25.6): [[code-tuning-procedure]].

Left out on purpose: requirements-level and hardware-level trade-offs, which are outside the code, and timing figures tied to particular languages and compilers, which go stale.

## Chapter 26: code-tuning techniques

What this wiki took from it (pp. 595-625): [[stop-loop-once-answer-known]], [[order-branches-by-frequency]], [[drive-repeated-dispatch-from-a-table]], [[cache-must-earn-its-complexity]], [[one-loop-one-job]], [[name-repeated-subexpression]], [[explaining-variable]] and [[do-not-hand-inline-for-speed]]. Each is kept as a readability rule or with its cost stated, under [[premature-code-tuning]].

Left out on purpose: the timing tables per language and compiler, which go stale.

## Chapters 27-30: program size, managing construction, integration, tools

What this wiki took from them: [[metric-outlier-review]] (ch. 28 with 30.2); [[smoke-test]], the incremental half of [[tracer-code]] and the localisation argument on [[small-steps-with-feedback]] (ch. 29, whose integration orders are system-level process and are left out); [[mechanical-code-transformation]] and [[independent-checking-tool]] (ch. 30).

Left out on purpose: estimation, staffing, configuration management and tool catalogues, which are process.

## Chapter 31: layout and style

What this wiki took from it: only what is not mechanical style, namely [[layout-must-tell-the-same-story-as-the-logic]], [[one-side-effect-per-statement]] and grouping by proximity in [[keep-variable-live-time-short]]. Indentation and brace styles, and one class per file (31.8), are left to tooling and the language's conventions.

## Chapter 32: self-documenting code

What this wiki took from it: [[self-documenting-code]], [[comment-kinds]], [[comment-why-not-how]], [[maintainable-comment-style]], [[marker-comments]], [[end-of-line-comments]], [[comment-data-declarations]], [[routine-header-comment]] and [[rewrite-tricky-code]], with the pseudocode-as-comments link to [[pseudocode-programming-process]].

## Chapter 33: personal character

Mostly out of scope. Its remarks on understanding why a program works were merged into [[programming-by-coincidence]].

## Chapter 34: themes in software craftsmanship

What this wiki took from it (pp. 817-833): the restatement of [[managing-complexity]] and its list of tools (34.1); [[coding-conventions]] (34.1, 34.5); [[code-for-the-reader]] (34.3); the return to [[program-into-the-language]] (34.4); [[high-level-code-in-problem-terms]] (34.6); [[design-warning-signs]] (34.7); and the error-handling line of 34.1, folded into [[consistent-error-handling-strategy]].

Left out on purpose: the process and iteration themes (34.2, 34.8) and the warning against "religion" in software (34.9), except where [[program-into-the-language]] uses it as a limit. Chapter 35, the reading list, has no rules.

## Where it disagrees with other sources

- On assertions in production, McConnell assumes they are compiled out and asks which checks to keep (pp. 185-186, 204-205); *The Pragmatic Programmer* says leave them on. [[defensive-code-in-production]] resolves this per setting.
- On checking one condition twice, McConnell reports Microsoft Word asserting and then handling (p. 188) against Meyer's one-check view, and clamps inside a routine in his own example. [[assert-then-handle-anyway]] resolves this against [[caller-owns-the-precondition]].
- On stopping, McConnell's spectrum from robustness to correctness (p. 192) limits the unconditional reading of [[crash-early]].
- On a procedure returning a status, McConnell allows it (pp. 177-178) where *Elegant Objects* forbids a manipulator returning anything. [[function-or-procedure]] resolves this per setting against [[command-query-separation]].
- On exceptions for expected outcomes, McConnell reserves exceptions for the truly exceptional (p. 194) where *Elegant Objects* prefers an exception to a returned null. [[exceptions-for-the-exceptional]] states the condition, and [[null-object-or-optional]] picks the form for an absence.
- On enumerations, McConnell recommends them (pp. 294-296) where *Elegant Objects* treats them as public constants. [[enum-instead-of-codes-and-flags]] resolves this per setting against [[no-public-constants]].
- On forwarding every method of a delegate, McConnell allows inheriting from it instead (p. 563) where *The Pragmatic Programmer* says has-a beats is-a. [[delegate-to-services]] resolves this per setting.
- On global data, McConnell accepts several uses behind access routines (pp. 329-331) where *The Pragmatic Programmer* says avoid it and *Elegant Objects* bans singletons. [[global-data]] resolves the three.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition. The grouping, the mapping to pages, the key takeaways and the assessment of the book's authority and limits are this wiki's own.
