---
title: Naming conventions, what they buy and what they encode
category: naming
summary: "Concept: what a naming convention buys and must distinguish; the one sign kept here is identifiers mixing natural languages or spelling dialects (color/colour) in one codebase; two names for one quantity is one-name-per-concept, loose related data group-related-data-into-a-structure."
tags: [concept, naming, conventions, consistency]
paradigm: any
sources: [code-complete, object-oriented-thought-process]
created: 2026-11-06
updated: 2026-11-06
---

McConnell grants that programmers sometimes reject standards for a sound reason: some are too rigid and inefficient, they stifle creativity and lower quality. He still calls effective standards one of the most powerful tools there are (*Code Complete*, Russian edition, p. 263). He also argues that any convention is usually better than none, and that the convention itself can be arbitrary: «Сила конвенций именования объясняется не конкретными аспектами, а самим фактом их использования» (p. 264). Its value is that it structures the code and leaves fewer things for the reader to worry about.

Weisfeld's *The Object-Oriented Thought Process* (ch. 5) agrees and adds the second half. Which convention is chosen «не так важно, как просто выбор одного соглашения и следование ему» (p. 107), but within it names of classes, attributes and methods must be descriptive: a reader should be «способен, исходя из имени, сказать, что представляет собой соответствующий объект» (p. 107). Organisations often fix the convention in coding standards (p. 107). He warns of conventions that make sense to their author and are opaque to everyone else, and of forcing them on people (p. 107), and notes that descriptive naming holds across development paradigms (p. 107). In code the descriptive half is owned by [[name-describes-what-the-variable-represents]] and [[abbreviation-discipline]].

## What conventions provide

The book lists these benefits (p. 263):

- **More can be taken for granted.** One global decision replaces many narrow ones, so attention goes to the parts of the code that matter.
- **Knowledge carries over** from earlier projects, because similar names make unfamiliar variables easier to read.
- **New code is learned faster**, because it is consistent instead of reflecting each author's habits.
- **Names do not multiply.** Without a convention, one quantity easily gets two names, such as `pointTotal` and `totalPoints`. The author may follow it, but a later reader may be seriously misled.
- **They make up for a language's weaknesses.** A convention can imitate named constants and enumerations, distinguish local, class and global data, and mark types the compiler does not know.
- **They show how items relate.** Where a language lacks objects, a shared prefix shows that `employeeAddress`, `employeePhone` and `employeeName` belong together, which bare `address`, `phone` and `name` do not.

## When a convention pays

McConnell recommends a convention when any of these holds (p. 264): several programmers work on the project; others will change and maintain the program, which is almost always the case; other programmers review it; the program is too large to hold in one's head; it will live long enough that you return to it after weeks or months; or the domain has unusual terms that should be used uniformly in the code.

How formal the convention should be depends on the number of people, the size of the program and its expected life. For tiny throwaway projects a strict convention «наверное, окажется пустой тратой сил» (p. 264). On larger projects with several programmers a formal convention is a key means of readability.

## What a convention encodes

McConnell says a variable's name should carry three kinds of information (p. 269): what the variable represents; what kind of entity it is (a named constant, a plain variable, a user-defined type or a class); and its scope (private, class, package or global).

The language-independent distinctions he asks a convention to make are variables against routines, classes against objects (see [[type-name-vs-variable-name]]), globals, class members, type definitions, named constants, enumeration members, and input-only parameters (see [[mark-input-only-parameters]]) (pp. 264-267). He reasons that marking a global tells the reader to treat it with care, and that marking a named constant tells you whether an assignment copies something that can change (pp. 266-267). His checklist asks whether the convention tells local, class and global data apart, and types, named constants, enumerations and variables (p. 280).

**Natural language.** All names should use one natural language, and one dialect of it, so nobody has to remember whether a variable is `color` or `colour`, `check` or `cheque` (pp. 278-279). For a team of several nationalities McConnell's rule is «обяжите их именовать все элементы программы, используя один естественный язык» (p. 278).

**Several languages in one project.** McConnell advises shaping the convention for overall consistency and readability, even where that means departing from one language's own convention (p. 269).

**Semantic prefixes.** Where a project uses standardized prefixes, the book's warning is that the main trap is «отказ от дополнения префикса выразительным именем переменной» (p. 274): `ipa` says it is an index into an array of paragraphs, but not which paragraphs, so prefer `ipaActiveDocument`. The bound prefixes `first`, `last`, `lim`, `min` and `max` from the same table are [[range-bound-names]].

## How this applies in code

This wiki reads the benefits as two kinds. Most are about readers and teams, and have no sign of their own in code. Two have one. Name proliferation shows as two names for one quantity in one scope; [[one-name-per-concept]] owns that sign, and [[computed-value-qualifier-at-end]] supplies the fixed order that prevents it. Hidden relations show as loose variables that always travel together. The book's remedy in chapter 11 is a shared prefix, for languages without objects; in chapter 13 the book itself recommends gathering such data into a structure, which is [[group-related-data-into-a-structure]].

A missing convention, in this wiki's own reading of the source, shows as inconsistency: within one codebase the same kind of entity is named in several styles, such as member fields both with and without a marker, constants both in capitals and in lower case, or enum members sometimes qualified by the enum name and sometimes not. The book itself asks not to mix ways of separating words (p. 267). Mixed capitalisation and markers are mechanical style, which the charter leaves to a linter, so this wiki keeps one form as a sign in code: identifiers mixing natural languages or spelling dialects (`color` beside `colour`, pp. 278-279). Inconsistency is the sign, not any particular style.

## Limits and the language's own convention

- McConnell tells the reader to follow the naming conventions of the language in use (p. 267). This wiki's charter goes further. The concrete prefixes and capitalisation (`g_`, `m_`, `t_`, `c_`, all-capitals constants, camel against snake case) are a language's style, taken at work time from the project's tooling and conventions, not from this page; see also [[follow-local-naming-culture]]. What this page keeps is the language-independent part: that the convention exists, that it is applied uniformly, and which distinctions it must let a reader see.
- The "compensate for the language" benefit is dated in part: modern languages provide namespaces, enumerations and scoping that the conventions once imitated. This wiki notes that much of what McConnell's prefixes encode, such as scope, constness and user-defined type, is now shown by editors and enforced by type checkers. A prefix that duplicates such a guarantee adds noise rather than information.

## Source

Weisfeld, *The Object-Oriented Thought Process*, 4th ed., Russian translation (Piter, 2014), via [[object-oriented-thought-process]], ch. 5, pp. 106-107: one convention followed consistently, descriptive names, organisational standards, conventions others understand; the quotations were checked against `raw/`. The routing of the descriptive half to other pages is this wiki's.

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 11.3-11.7, pp. 263-269, 272-274, 278-280 ([[code-complete]]). The benefits of conventions, the 'any convention beats none' claim, when to adopt one and how formal, the three kinds of information a name carries, the distinctions to draw, the single-natural-language rule, the advice not to mix word-separation styles (p. 267) and the prefix trap come from the book. The reading of which benefits have signs in code, the assignment of the two-names sign, the inconsistency sign, deferring concrete prefixes and capitalisation to the language, and the remark on type checkers and editors are this wiki's own.
