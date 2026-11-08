---
title: Break the build on interface change
category: change
summary: "A function keeps its name and signature while its meaning, unit or result convention changes, so every caller still compiles and is now wrong."
tags: [rule, change-safety, interfaces, compile-time]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

Refactoring keeps behaviour fixed, but sometimes the work goes beyond that. This wiki holds that when behaviour or an interface does change, the most useful thing the compiler can do is refuse the old callers, because each refusal is a place that needs attention.

## Rule

When a change goes beyond refactoring and alters external behaviour or interfaces, the book says this may lead to a deliberate breaking of the build: «преднамеренному нарушению сборки» (p. 264). Old clients of the code fail to compile, and this shows what has to be updated (p. 264).

This wiki states the reason as follows: a change that callers cannot detect leaves them all silently wrong. A change that stops them compiling converts an unknown set of defects into a finite list of errors.

## Sign in code

- A function keeps its name and parameter types while the diff changes the unit, meaning or range of a parameter or result.
- A result convention changes under the same return type, for instance from a missing-value marker to an exception.
- A parameter is added with a default that changes behaviour for callers who did not ask for it.

## When not to apply

- Nothing checks the callers. If no compiler or type checker sees them, a renamed symbol fails only at run time, so search and tests have to do this work.
- The interface has external users you cannot update in one step. Then a deprecation period with both forms side by side is the usual course. The book does not say whose clients these are, and this wiki takes its case to be clients whose code you can change.
- The change is truly compatible, so that no caller needs updating.

## Repair

1. Change the signature so that the old call no longer compiles: rename the function, or give the value a distinct type that names its unit.
2. Follow the compiler's errors through every caller, and decide each one.
3. Do not keep the old form as a convenience wrapper with the new meaning.

## Before and after

```
// before: was seconds, now milliseconds; all callers compile
function connect(host, timeout: Number): ...

connect(primary, 30)
```

```
// after: old calls stop compiling, and each is converted
function connect(host, timeout: Duration): ...

connect(primary, Duration.seconds(30))
```

## Source

[[pragmatic-programmer]], Topic 40, p. 264, for the deliberate break and its purpose. The book mentions this in one sentence, as something such a change may lead to. The imperative in this page's title, the reasoning, the signs, the limits, the repair and the example are this wiki's own. Related: [[refactoring]], [[state-the-contract]].
