---
title: Do not rely on unguaranteed context
category: structure
summary: "A utility module reads an environment variable, the current directory, a UI handle or locale directly, or makes a network call with no timeout or failure path."
tags: [rule, context, assumptions, dependencies, coupling]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-07
---

Code written in one setting absorbs that setting without anyone deciding it should. The book calls this an accident of context: a module works because of the circumstances in which it happened to be developed, not because those circumstances are guaranteed. It is one form of [[programming-by-coincidence]].

## Rule

A module relies only on what is guaranteed to it. The book frames this as a question to ask of each dependency: «На что еще не стоит полагаться, если оно не гарантируется?» (p. 249).

The book's list of things commonly assumed (p. 249):

- a graphical interface, because the module is being built in one
- English-speaking users
- users with special training
- a readable current directory
- particular environment variables or configuration files
- how accurate the server's clock is
- network availability and speed

It also asks whether copied code really shares the context it was found in, and calls imitation without context cargo cult development (p. 249).

## Sign in code

- A utility or library module reads an environment variable, a configuration file or a path relative to the current directory, rather than taking the value as a parameter.
- Non-UI code touches a UI handle, or a user-facing string in one language is embedded in a shared module.
- A network call has no timeout and no failure path.
- Code compares time across hosts with no tolerance.

Copied code has no sign of its own, because where a passage came from is not visible in it. Judging it needs the origin, for instance a link in a comment or the commit history.

This wiki assigns the neighbouring cases as follows. This page owns a reusable module that assumes something about its surroundings, even at one site. Knowledge of how configuration is stored, spread across many sites, is [[configuration-behind-a-thin-api]]. An input the signature does not show, in code that is not meant to be reused elsewhere, is [[global-data]]. An assumption built into a data shape is [[representation-that-fits-by-coincidence]], which owns the book's exercise 26: phone numbers in a numeric field, tested across North America, then complaints from elsewhere (p. 252). The book's answer rules that field out (p. 360). Domain code that calls a presentation routine or dialog in the middle of a computation, or to report a failure, is [[logic-testable-without-ui]]; a reusable module that reaches a UI handle it was not given is [[do-not-rely-on-unguaranteed-context]].

## When not to apply

- The code is the application's entry point or wiring layer, where context is legitimately read and passed inward.
- The assumption is stated. A module documented as running only in one environment has made a decision and is not relying on an accident.
- The environment gives a real guarantee, for instance a runtime that promises the value exists.
- There is one deployment and the parameter would never vary. This wiki warns that lifting every value into a parameter adds complexity that may not pay for itself.

## Repair

1. Pass the dependency in as a parameter, and read it at the entry point.
2. Where it must be taken from the surroundings, check it and fail with a clear error instead of proceeding.
3. Where it cannot be checked, state it as a precondition of the module.
4. Give network and clock dependencies an explicit timeout, tolerance and failure path.

## Before and after

```
// before: a shared formatter
function exportPath(name):
    return readEnv("EXPORT_DIR") + "/" + name + ".csv"
```

```
// after: the context is handed in by the caller
function exportPath(directory, name):
    return directory + "/" + name + ".csv"

// entry point
directory = requireEnv("EXPORT_DIR")   // fails here, with a message, if unset
```

## Source

[[pragmatic-programmer]], Topic 38, p. 249, for the rule and the list of assumptions, p. 252 for exercise 26, and p. 360 for its answer. The signs, the assignment of neighbouring cases, the limits, the repair and the example are this wiki's own.
