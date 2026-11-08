---
title: Program into the language, not in it
category: structure
summary: "Concept: Gries's distinction between letting the language's constructs and defaults set the design (in) and deciding the design first, then expressing it with the language plus conventions and helpers (into); its signs live on the pages it points to: a hidden form or parallel copy of UI logic, ad-hoc surfaces or checks, a global or goto used because the language allows it."
tags: [concept, conventions, language-limits]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell borrows a distinction from Gries. Programming *in* a language means limiting design to the constructs the language supports directly. Programming *into* a language means first deciding which structure the program needs, then expressing it with whatever the language offers, conventions included (p. 65). McConnell calls this distinction the key to understanding his whole book: «Большинство важных принципов программирования зависит не от конкретных языков, а от способа их использования» (p. 66). Where the language falls short: «Если язык не поддерживает нужные конструкции или имеет другие недостатки, попробуйте их компенсировать» (p. 66), with your own coding conventions, standards and class libraries.

## Two failure modes the book shows

1. **The language's defaults set the structure.** In McConnell's Visual Basic example, the tool pushed as much code as possible into the form files. Left alone, some forms would have held business logic, others database access and others neither, and nobody could say which form does what (p. 65). The signs in code, a hidden form kept for its validation method and validation copied out and kept in parallel (p. 66), are owned by [[logic-testable-without-ui]].
2. **A previous language's constructs are carried over.** A team moving from Fortran to C++ wrote code that «компилировался на C++, но на самом деле это был замаскированный Fortran» (p. 60): goto and global data, with the language's object-oriented features ignored. This wiki treats "disguised Fortran" as a reason, not a sign, since "organised like another language" could be said of nearly any code; the constructs themselves are [[global-data]] and [[goto-as-last-resort]].

## The return in chapter 34

The best programmers, McConnell says, first decide what they want to do, then work out how to do it with the tools at hand; taking the most obvious path the language offers is programming *in* it (p. 823). He draws two demands from it:

- **Do not use a feature because it is there.** «Не нужно использовать глобальные данные или операторы goto только потому, что их поддерживает язык.» (p. 823). He asks the same of a class member that does not fit the class's abstraction but is more convenient than a consistent design (p. 823); that shape is [[class-interface-coherent-abstraction]]. Using exceptions only because the language offers them is on [[exceptions-for-the-exceptional]].
- **Build what the language lacks.** «Ваш язык не поддерживает утверждения? Напишите собственный метод assert().» (p. 823). Where a language has no enumerations or named constants, a naming convention over disciplined variables can emulate them (pp. 823, 825). The signs of a missing helper or an inconsistent surface are on [[coding-conventions]]; a literal repeated where the language has no constants is [[named-constants-over-literals]].

## Limits

- McConnell's own: in very primitive environments, especially new technologies, the tools may force significant changes to the preferred approach, and the wish to program into the language has to be weighed against the accidental complexity of fighting it. Usually the mismatch is small and forces only small concessions (pp. 823-824).
- Refusing a feature on principle is not this idea. McConnell counts the zealous rejection of global data among the forms of "religion" in programming (p. 831).
- This wiki's own: the distinction is against letting the language *limit* the design, not a call to fight the language's idioms, which are decided at work time from the project's conventions, per this charter. Which structure the program has (where storage access or domain logic lives) is architecture, taken as given from the project; this page only asks that the code follow it rather than the tool's defaults.

## Source

[[code-complete]], ch. 4, Russian edition: "disguised Fortran", p. 60; Gries's in/into distinction and the Visual Basic example, pp. 65-66; the key-principle quotations, p. 66. Ch. 34.4, pp. 823-824, with 34.5, p. 825 and 34.9, p. 831: the return to in/into, the globals-and-goto and class-member remarks, the hand-written `assert`, emulated constants, the primitive-environment limit and the religion remark. This wiki's own: reading "disguised Fortran" as a reason rather than a sign, the idiom and architecture limit, and the routing of each shape to its owning page. The page was a rule page; its signs moved to [[logic-testable-without-ui]] and [[coding-conventions]] on 2026-11-06.
