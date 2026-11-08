---
title: "Offensive programming: make errors loud during development"
category: errors
summary: "A default or else arm for an unexpected case, or an assertion handler, lets the program continue silently or after a keypress in development builds, so a known problem can be skipped instead of fixed."
tags: [rule, fail-fast, development-builds, assertions]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell, citing Howard and LeBlanc (2003), calls it offensive programming: exceptional cases should be handled so that they are obvious during development and recoverable in production (p. 201). «Иногда нападение — лучшая защита.» (p. 201)

## Rule

The book's example is a case statement expected to handle only five kinds of event: during development the default arm should raise a warning that says another case exists and the program needs fixing; in production the reaction should be politer, for example a write to an error log (p. 201).

The techniques it lists (p. 201):

- Make assertions abort the program, so programmers do not get in the habit of pressing Enter to skip a known problem.
- Fill any allocated memory, so that allocation errors can be detected.
- Fill files and streams completely, to flush out file-format errors.
- Make the default or else arm of every case statement stop the program or otherwise demand attention.
- Fill an object with junk just before it is deleted.
- Set the program up to send you its error logs, where that is possible, to see what errors occur in production.

The reasoning: the stricter the requirements during development, the easier the program is to operate (p. 201).

## Sign in code

- An assertion or failure handler that prints and waits for confirmation, or prints and continues, in the development configuration.
- A default arm over a closed set of cases whose body is a comment or a log line, the same in every build. An empty one is [[assert-the-impossible]].
- Released objects or freed buffers left with their last valid contents in a debug build, where the project's language exposes such memory.

This wiki assigns the neighbouring cases as follows. A missing default arm altogether, or a default that does the work of one nameable case, is [[default-branch-catches-the-unexpected]], which owns whether a multi-way branch over a closed set has a final `else` or `default` reserved for the unexpected; an impossible branch that logs and carries on is [[crash-early]] where the module's production reaction must also be a stop. This page owns the difference between builds: a reaction that is the same, and quiet, in development and in production, where the production reaction may be polite. Where the fill of freed memory belongs inside an allocation wrapper, [[isolate-unsafe-memory-operations]] owns the wrapper; this page owns whether the reaction differs between builds.

## When not to apply

- Where [[crash-early]] holds for production too, the polite production reaction does not apply: an impossible state in a correctness-critical module stops the program in every build ([[robustness-versus-correctness]]).
- Memory and stream filling applies only where code manages raw memory or file layouts itself; in a managed runtime it has no counterpart in application code. This limit is this wiki's own.

## Repair

Make the development reaction to an unexpected case fatal and specific. Give the production build its own, chosen reaction (log, report, polite stop) through one switch rather than per call site ([[switchable-debug-aids]]).

## Before and after

```
# before
switch event.kind:
    case OPEN: ...
    case CLOSE: ...
    case MOVE: ...
    case RESIZE: ...
    case FOCUS: ...
    default:
        log("unknown event")       # same in every build
```

```
# after
switch event.kind:
    case OPEN: ...
    case CLOSE: ...
    case MOVE: ...
    case RESIZE: ...
    case FOCUS: ...
    default:
        unexpected_case("event kind", event.kind)

function unexpected_case(what, value):
    if build.is_development:
        abort("unhandled " + what + ": " + value + " - fix the program")
    else:
        error_log.write("unhandled " + what, value)
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, [[code-complete]]: p. 201 for the rule, the case-statement example and the list of techniques. The signs, the split with neighbouring pages, the limits, the repair and the example are this wiki's own.
