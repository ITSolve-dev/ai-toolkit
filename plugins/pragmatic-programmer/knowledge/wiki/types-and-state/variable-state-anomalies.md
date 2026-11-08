---
title: Variable state anomalies
category: types-and-state
summary: "On one path a variable is assigned twice with no read between, assigned and never read before return or release, read after its resource was freed or closed, freed twice, or a local is read before any assignment."
tags: [rule, state, data-flow, variables]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

The normal life of a variable is: defined, used one or more times, perhaps killed. McConnell lists sequences of these states (see [[data-flow-testing]] for the vocabulary) that should raise suspicion, and tells the reader to check code for them *before* testing starts (pp. 501-502).

## Rule

Check each variable's sequence of define / use / kill / entry / exit actions, and treat these as defects or suspects (pp. 501-502):

| Sequence | Verdict in the book |
|---|---|
| define - define | Wasteful and error-prone even if not wrong |
| define - exit | Pointless for a local; may be fine for a parameter or global |
| define - kill | An unneeded variable, or missing code that should have used it |
| entry - kill | A problem for a local; for a parameter or global fine only if defined elsewhere earlier |
| entry - use | A problem for a local (used before defined); for a parameter or global fine only if defined elsewhere |
| kill - kill | Sloppy; a double free of a pointer is fatal |
| kill - use | A logic error |
| use - define | May or may not be a problem; check that a definition also precedes the use |

On kill-use, McConnell says that if the code still works, for instance because the pointer still points at freed memory, «это лишь случайность» (p. 501).

## Sign in code

A reader can point at each of these on one path through a routine:

- an assignment to a variable followed by another assignment to it with no read in between;
- a local assigned and then not read before `return`;
- a local assigned and then released, closed or out of scope with no read;
- a local read before any assignment;
- a resource released, closed or freed twice;
- a read through a reference after the resource it points to was released or closed;
- a variable read and later assigned: check that an assignment also precedes the read on every path.

This wiki assigns the neighbouring cases as follows. This page owns the sequence on a path. A local read on a path where no assignment precedes it is [[variable-state-anomalies]]; a local assigned on every path but far above its first read, or not reset before a repeated block, is [[initialize-close-to-first-use]]; a variable reassigned for an unrelated second job is [[one-variable-one-purpose]]; a resource opened in one routine and closed in another is [[finish-what-you-start]]; a release skipped on an exception path is [[exception-safe-release]].

## When not to apply

- Parameters and globals: entry-use and entry-kill are normal when the value was defined by the caller, and define-exit on an output parameter or global is normal (pp. 501-502).
- use-define is a check prompt, not a defect. This wiki adds that an accumulator read and then reassigned in a loop is the ordinary case when it was initialised before the loop.
- This wiki adds: many compilers, linters and type systems flag uninitialised reads, dead stores and use-after-move. Where the project's tooling already reports a sequence, it is mechanical and out of this wiki's scope; the rule still applies to sequences the tooling cannot see, such as a closed handle stored in a field and used by another method.
- This wiki adds: a deliberate reset (define-define) that restores an invariant before reuse, documented as such, is not an anomaly.

## Repair

This wiki's repairs, by sequence:

- define-define, define-exit, define-kill: delete the dead assignment or the variable; or, if a use is missing, add it, since the anomaly may mark lost code.
- entry-use on a local: initialise at declaration, close to first use.
- kill-use, kill-kill: give one place ownership of the release; after release, drop the reference, or scope the resource so the reference cannot outlive it.
- use-define: move the definition before the use, or show that one exists on every path.

## Before and after

```
function report(path):
    total = 0
    total = loadDefault()        // define - define
    f = open(path)
    lines = read(f)
    close(f)
    header = parse(read(f))      // kill - use: f already closed
    unused = count(lines)        // define - exit: never read
    return format(header, total)
```

```
function report(path):
    total = loadDefault()
    with f = open(path):
        lines = read(f)
    header = parse(lines)
    return format(header, total)
```

The header is now parsed from the lines already read. The scope binding also removes [[exception-safe-release]]'s sign, the release with no finally in the before; only the kill-use is this page's.

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, section 22.3, pp. 500-502, via [[code-complete]]: the state vocabulary, the anomaly list with its verdicts, the parameter/global limits and the advice to check before testing. This wiki's own: the sign list, the owner assignments, the accumulator, tooling and reset limits, the repairs and the pseudocode.
