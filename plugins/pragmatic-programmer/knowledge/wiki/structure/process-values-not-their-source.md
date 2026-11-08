---
title: Process values, not their source
category: structure
summary: "A class doing one computation that takes a file name or reads input itself: pass it the values, so the source can change without touching it."
tags: [rule, orthogonality, cohesion, input]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

The book judges the class that only splits strings to be more orthogonal, since it is focused on its own job and neglects details such as where the strings come from: «пренебрегая такими подробностями» (p. 349). See [[orthogonality]].

## Rule

Let a unit of processing receive the data it works on, and leave obtaining that data to someone else. The book gives two gains: the code is easier to develop, and it is more flexible, because the same class can work on strings read from a file, produced by another routine or passed in through the environment (p. 349).

## Sign in code

- A constructor or function whose job is a computation, taking a file name, a URL or a connection, and opening it itself.
- A test of a computation that has to create a file or start a service to supply a few strings.

This wiki assigns the neighbouring cases as follows. This page owns a source the signature names and the computation opens itself. An input the signature does not show is [[global-data]].

## When not to apply

The book states no limit here. The limits below are this wiki's own.

- The unit's whole job is reading: it is the adapter that the rest of the code calls.
- A short script that has one source and will be run once. Separating the two adds a layer nobody uses.
- The input is too large to hold in memory. Pass a stream or iterator rather than the values: the unit stays independent of the source, but this variation does tie it to sequential reading.

## Repair

1. Move the reading out to the caller, or to a dedicated reader.
2. Change the signature to take the data, or a stream of it.
3. Replace test fixtures that create files with direct values.

## Before and after

Before: splitting a line requires a file.

```
class FieldSplitter
  constructor(path):
    this.line = readFirstLine(path)
  fields():
    return split(this.line, ",")
```

After: the source is the caller's concern.

```
class FieldSplitter
  constructor(line):
    this.line = line
  fields():
    return split(this.line, ",")

splitter = FieldSplitter(readFirstLine(path))
```

## Source

[[pragmatic-programmer]], Thomas and Hunt, 20th Anniversary Edition, Russian translation (Dialektika, 2020), answer to exercise 1, p. 349. The judgement and both gains are the book's. The general rule, the signs and their assignment against [[global-data]], the limits, the repair and the pseudocode are this wiki's own. Related: [[orthogonality-tests]], [[do-not-rely-on-unguaranteed-context]], [[global-data]].
