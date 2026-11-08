---
title: Software entropy
category: change
summary: "Why code decays: visible neglect spreads (broken windows), and small steps go unnoticed (boiled frog). The two mechanisms need different responses; only the first has a local sign in code."
tags: [concept, entropy, software-rot, technical-debt, broken-windows]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

**Software entropy** is the growth of disorder in software. The book names the result software rot and remarks that the kinder name, technical debt, implies a repayment that will most likely never happen (p. 34). Whatever it is called, it can spread unchecked. This page defines the idea under [[broken-windows]] and [[first-do-no-harm]]; it carries no sign of its own.

## What drives it

The book says the most important factor in rot is probably the psychology or culture around a project, and that this holds even for someone working alone (p. 34). Good plans and good people do not protect a project by themselves. Its strongest claim is about speed: «пренебрежение ускоряет деградацию быстрее, чем любой другой фактор» (p. 35).

## Two mechanisms

The book separates two ways decay proceeds, and warns against conflating them (p. 39).

- **Contagion, the broken window.** People lose the will to fight entropy because they read it as everyone else's indifference. The thought that follows is «Вся остальная часть этого кода написана скверно, и я поступлю точно так же» (p. 36). The decay is seen, and being seen is what spreads it.
- **Unnoticed drift, the boiled frog.** «А лягушка просто не замечает никаких изменений.» (p. 39). The book describes the software form: a system departs from its specification one feature at a time, and patch after patch lands on a piece of code until nothing original is left in it (p. 38). Each step looks harmless, so nobody decides anything.

This wiki draws a consequence for review that the book does not state. Contagion has a local sign, because the defect sits in the code in front of the reader. Drift has none: every single diff passes, and the damage shows only when a function is compared with its own history or with its specification. An inspector given one diff can report the first and cannot report the second unless it is also given that history.

## What the evidence covers

The studies the book cites concern buildings, an abandoned car and contagious depression (pp. 35-36, footnotes 8 and 9), not code. This wiki therefore treats contagion as an explanation of why the rules matter, and not as a measured property of codebases.

## Related

[[broken-windows]], [[first-do-no-harm]], [[good-enough-versus-broken-window]], [[pragmatic-programmer]].

## Source

[[pragmatic-programmer]], Topic 3, pp. 34-36, and Topic 4, pp. 38-39. This wiki's own: the consequence for review under *Two mechanisms*, and the reading of the evidence as an explanation and not a measurement.
