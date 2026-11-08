---
title: Architecture prototype questions
category: structure
summary: "A module needs data it cannot reach, or cannot reach when it needs it: for each datum a module reads, ask who produces it and at what point in the run."
tags: [method, architecture, coupling, responsibilities, data-access]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

The source gives a short list of questions to ask of a prototype of a whole system (p. 92). Most of them restate rules held elsewhere: responsibilities and collaborations, coupling, duplication, interfaces. See [[orthogonality]] and [[dry]]. One group adds something: does every module have an access path to the data it needs during execution, and does it have that access when it needs it (p. 92)?

That group matters most: «Последний ряд вопросов приносит больше всего неожиданностей» (p. 92), and the source adds that it yields the most valuable results of the prototyping exercise.

The prototype itself need not be code, and individual modules need not function in any special way, which is what separates it from [[tracer-code]] (p. 91). The wider procedure is on [[tracer-code-vs-prototype]].

## Running the check against a module map

This wiki extends the check to existing code. That transfer is ours; the source addresses only prototypes. For each module, and for each datum it reads, a reader can note who produces that datum and at what point in the run.

The check tends to find a value that is required before the step that creates it, or data reachable only by way of a component that should not be involved.

## Limits

This wiki adds that the check is about system shape. It says nothing about whether any one module is written well, and a clean answer here does not stand in for reviewing the code.

## Source

[[pragmatic-programmer]], Topic 13, pp. 91-92: the questions and the weight of the last group. The section on running the check against a module map, its examples of what the check finds, and the Limits section are this wiki's own.
