---
title: Attack surface
category: errors
summary: "Every entry and exit point of a program counts against it: complex code, external input, unauthenticated services, disclosing output and exposed debug information."
tags: [concept, errors, security, defensive-code, complexity]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

The attack surface of a system is the sum of all the access points where an attacker can enter or extract data or invoke a service (p. 284). An obscure service gets no exemption: the book answers the objection that nobody cares about this code with «Безвестность никак не защищает.» (p. 284).

## The vectors

The book gives five as examples (pp. 285-286):

- **Code complexity.** Excessive complexity itself widens the surface, because complex code offers more room for unforeseen side effects (p. 285).
- **Input data.** See [[distrust-external-input]].
- **Unauthenticated services.** Anyone in the world can call them, which at minimum invites denial of service.
- **Output data.** See [[do-not-disclose-in-output]].
- **Debug information.** See [[do-not-disclose-in-output]] and [[test-window]].

The tip that closes the list is «Не усложняйте код и минимизируйте поверхности атак» (p. 286).

## Use in review

This wiki's reading is that the concept helps most as a question about a change rather than as a verdict: which new entry or exit point does this diff add, and who can reach it? A new route, parameter, file read or message field counts. A refactoring inside a function counts only if it makes the code more complex, the first vector above.

Related principles from the book's list of basic principles (p. 284): [[least-privilege]], [[secure-defaults]] and [[keep-secrets-out-of-source]]. [[do-not-implement-cryptography]] comes from the passage that follows the list (pp. 288, 290).

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020 ([[pragmatic-programmer]]): pp. 284-286, 288, 290. This wiki's own: the review question.
