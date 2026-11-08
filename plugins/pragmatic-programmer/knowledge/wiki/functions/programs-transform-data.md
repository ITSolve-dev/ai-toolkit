---
title: Programs transform data
category: functions
summary: "Design that starts from classes and modules instead of asking what goes in, what comes out and which stages lie between; shows as logic organised around holders of data rather than around the flow."
tags: [concept, transformation, pipeline, data-flow, coupling]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

The transformational view treats every program as a conversion of input into output, and makes that conversion the first thing designed. The classes, modules, data structures and frameworks come second. Thomas and Hunt argue that attention to code alone loses sight of this, and that going back to it makes many earlier worries disappear: data structures become clearer, error handling more consistent, and coupling smaller (p. 186). This wiki notes that the claim rests on the authors' experience and that the chapter offers no measurement for it.

## The model

The book's picture is an assembly line: raw material enters, finished product leaves, and each station does one conversion (p. 188). The Unix pipeline that lists the longest files in a tree is its example. It is a chain of steps from a directory name to a file list, to line counts, to a sorted list, to the last five entries (pp. 187-188). This wiki adds that each step knows only its own input and output.

A program in this model alternates code and data: code, data, code, data (p. 194). Data stops being attached to one group of functions, as it is in a class definition, and becomes the visible unfolding of the work.

## What it changes

- **Coupling moves to the shapes of values.** A function can be reused wherever its parameters match the output of some other function (p. 194). The authors say some coupling remains, but that in their experience it is easier to manage than in object-oriented code. A statically typed language also reports an attempt to connect two incompatible stages at compile time (p. 194).
- **The top-level function reads as the requirement.** Its body is the list of stages, each taking the previous stage's output (pp. 192-193).
- **State is carried, not stored.** See [[pass-state-dont-hoard-it]].
- **Errors need a convention.** A linear chain has no obvious place for conditional checks. See [[wrap-values-between-transformations]] and [[handle-errors-in-stages-or-in-the-pipeline]].

## It is not a syntax

The book calls this way of thinking a design principle and not a language feature: «Это скорее принцип проектирования» (p. 193). Where a language has no pipe operator, the same design is written as a sequence of assignments, each using the previous result. The authors call that laborious but workable (p. 193).

Exercise 23 asks how such assignments differ from a chain of method calls and which is preferable (pp. 198-199). The book's answer prefers the assignments. In the chain, each step returns an object that must implement the next call, so that object is bound to the calling code. A new step, such as removing comment lines, is easy to add to the assignments and has no obvious home in the chain, and the authors say this coupling is why the chained style is sometimes called a [[train-wreck]] (p. 358). This wiki reads the difference as one of binding: in a method chain the stages belong to the type of the previous result, and that is the coupling the model set out to remove. The rule drawn from this is [[transformation-pipeline-over-method-chain]].

## Where the model strains

The book's limit is only that the habit takes time to form (p. 198). The rest is this wiki's own reasoning. The model fits work with a clear beginning and end. It says less about something whose behaviour is its life over time, such as a connection, a cache or a long-running session. There the state is the subject and not an intermediate result. The limits on [[pass-state-dont-hoard-it]] draw that line in code.

The procedure for finding the stages is [[decompose-into-transformations]].

## Source

[[pragmatic-programmer]], Thomas and Hunt, 20th Anniversary Edition, Russian translation (Dialektika, 2020), topic 30, pp. 186-199, and p. 358 for the answer to exercise 23. The remark on the claim's evidence, the note on what each step knows, the reading of exercise 23 as binding of stages to a type, and the section on where the model strains, are this wiki's own.
