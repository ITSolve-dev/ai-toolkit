---
title: Tracer code
category: change
summary: "A stub or trivial routine sits behind a final interface in a system still being built along one path: not a defect while it has real error handling; a stub left after the path is declared complete is dead code."
tags: [method, incremental, skeleton, stubs, accretion]
paradigm: any
sources: [pragmatic-programmer, code-complete]
created: 2026-11-01
updated: 2026-11-06
---

This page tells an inspector how to read code written under one setting: the project is being built as a thin end-to-end path that is then thickened. How the system is split and layered is the project's architecture, taken as given; this page prescribes neither the split nor the build order.

## The setting

*The Pragmatic Programmer* calls the path tracer code: «Пользуйтесь методом трассирующих пуль для отыскания цели» (p. 84). It is aimed at new systems where requirements are vague and the techniques are unfamiliar (p. 83). One simple feature is built through every part of the system, then each new feature thickens the components along its path, replacing stand-in routines with real ones (pp. 84-85, 88). Its quality bar is the point most easily lost: «Трассирующий код пишется не для одноразового применения, а надолго» (p. 86). It carries the error checking, structure and documentation of production code. «Он просто не полностью функционален» (p. 86).

McConnell describes the same setting as **incremental development**, pictured as accretion (p. 14): «Инкрементное проектирование, конструирование и тестирование — одни из самых эффективных концепций разработки ПО» (p. 14). His first version is a runnable skeleton that need not accept real data or produce real output, and may call fake classes for each main function; each fake class is then replaced with a real one (pp. 14-15). He prefers this picture to the farming metaphor, which he rejects because it implies no direct control over how the system develops (p. 14). Chapter 29 calls the same shape T-shaped integration (p. 685).

**Where the two books differ, and how this wiki resolves it.** *The Pragmatic Programmer* wants the path production quality from the start; McConnell's skeleton lets input, processing and output be simulated at first (p. 15). This wiki reads them as stages of one method: the skeleton may come first, and the tracer quality bar applies from the moment a fake class is replaced with a real one.

## What it looks like in code

This wiki's own reading. One complete path runs through the code, the paths not yet built are absent, and a trivial routine sits behind its final interface with real error handling around it. Such a stand-in is the method working and is not reported as a defect. The same holds for stubs returning fixed values or fake input and output while the system is still being built, provided each sits behind the interface its real replacement will have.

Two shapes are not this method:

- A stub left in place after the path is declared complete is ordinary dead or misleading code.
- A production path that reads canned input or imports a spike folder is a prototype that shipped: [[tracer-code-vs-prototype]].

A first end-to-end path through a system that does not yet run is [[tracer-code]]; adding pieces one at a time to a skeleton that already runs is [[small-steps-with-feedback]].

## Source

[[pragmatic-programmer]], Topic 12, pp. 83-89: the tip, the setting, the quality bar. [[code-complete]], ch. 2, section 2.3, Russian edition, pp. 13-15: incremental development, accretion against the farming metaphor, the skeleton with fake classes; ch. 29, p. 685: T-shaped integration. This wiki's own: the framing as a setting rather than a procedure, the reconciliation of the two books, the section *What it looks like in code*, the dead-stub reading, and the assignment against [[small-steps-with-feedback]]. The books' build procedures, worked examples and lists of benefits are left out: under this wiki's scope they are process, and they change no report on code.
