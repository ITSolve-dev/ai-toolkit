---
title: Coupling hidden in language features
category: structure
summary: "Multiple inheritance, exceptions, operator overloading, overridden parent methods and shared data formats add coupling that is not visible at the call site."
tags: [concept, coupling, cohesion, orthogonality, language-features]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-06
---

The book's position is that good orthogonal code can be written in almost any language, and that every language has lures: features that raise coupling and lower [[orthogonality]] (p. 349). This wiki draws the point for a reader of code: this coupling does not appear as a call or an import, so a dependency count misses it. See [[coupling]].

## In object-oriented languages

The book names multiple inheritance, exceptions, operator overloading and overriding of parent methods as ways of adding coupling in not quite obvious ways (p. 349). The book does not explain the mechanism of each, so the following readings are this wiki's own:

- Overriding ties a subclass to when and why the parent calls that method. See [[inheritance-tax]].
- Multiple inheritance ties a class to two parents' names and to how they are resolved.
- An exception ties a caller to the failure types of code several levels down.
- Overloading means `a + b` no longer says which code runs. What an overload may mean is [[operator-overloading-meaning]].

## Coupling that is good

Binding code to its data in a class is itself coupling, and the book counts it as usually good: in that case «мы называем его сцеплением» (p. 349). The book's condition is focus: classes that are not sufficiently centred on specific tasks lead to bad interfaces (p. 349). This wiki takes the discriminating test to be whether both sides change for one reason: then the bond is cohesion, and otherwise it is coupling.

## In functional languages

The book says functional languages encourage many small decoupled functions, combined in many ways, and that this often works in practice. Coupling still appears, because such functions transform data and one's output becomes another's input. A format change in one function can then cause a failure further down, «сбою где-нибудь дальше в потоке» (p. 350). Good type systems help in part (p. 350).

This wiki draws the consequence for [[transformation-pipeline-over-method-chain]]: a pipeline removes coupling to intermediate objects and keeps coupling to the data's shape. It is a smaller coupling, and it is not zero.

## Source

[[pragmatic-programmer]], Thomas and Hunt, 20th Anniversary Edition, Russian translation (Dialektika, 2020), answer to exercise 2, pp. 349-350. The list of features, the remark on cohesion and the functional case are the book's. The per-feature mechanisms, the discriminating test and the pipeline consequence are this wiki's own.
