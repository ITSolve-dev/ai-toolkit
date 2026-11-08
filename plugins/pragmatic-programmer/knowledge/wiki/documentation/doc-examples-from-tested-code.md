---
title: Documentation examples come from tested code
category: documentation
summary: "A code sample in a document or docstring is a hand-pasted copy, with no include directive and no test running it, so it can drift from the code it shows."
tags: [rule, documentation, duplication, examples]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

A code example in documentation is a second copy of knowledge held in the code. If nothing ties the two together, the example will go stale with no signal, and it will still read as authoritative. [[documentation-in-the-source]] covers where prose lives; this page covers samples.

## Rule

This wiki states the rule so: show in a document only code that a build has run, pulled from the tested source by name and not pasted. The book describes this as its own practice for producing a book. The authors consider it essential to verify every code fragment shown in the book, and they did so for all its examples (p. 136). Following [[dry]], they refuse to copy lines from tested programs into the text, since that duplicates code and «буквально гарантировало бы, что мы забудем обновить пример кода» when the program changes (p. 136). Instead, a simple script called during formatting extracts named segments from the source file, then highlights the segment and converts it to the typesetting syntax (p. 136). Named segments also solve the problem of examples that lack the scaffolding needed to compile and run: the source holds it, and the document shows only the segment (p. 136). The book's index works on the same principle: entries are marked in the text of the book itself and built by script, because a separately kept index is hard to maintain through changes (p. 136).

## Sign in code

- A fenced sample in a README, guide or docstring that matches code elsewhere, with no include directive or extraction marker.
- A sample whose calls no longer match the current signature of the function it shows.
- Documentation samples that no test or build step executes.

## When not to apply

The limits are this wiki's own.

- The sample is schematic and shows a shape and not a call that exists in the project. It should then not look like runnable code.
- A one-line usage hint in a docstring next to the function it describes sits where a change would be seen. An example run by the test tooling removes the risk altogether.
- The sample shows code in another project that you do not build.

## Repair

1. Move the example into a file that compiles and runs under the test suite.
2. Mark the shown part as a named segment.
3. Have the document build include that segment.
4. Where a toolchain runs examples embedded in docs, use it, and the copy problem goes away.

## Before and after

```
// before: copied by hand when connect took one argument
README:
    client = connect(host)
    client.send(message)

source:
    function connect(host, timeout): ...
```

```
// after: the sample runs in the suite, and the document includes it
examples/usage (run by the test suite):
    // begin: usage
    client = connect(host, timeout = 5)
    client.send(message)
    // end: usage

README:
    {include examples/usage#usage}
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation: [[pragmatic-programmer]], Topic 21, p. 136. The practice, its reasoning and the index example are the book's, which describes them for producing a book. The rule as worded and its transfer to READMEs and docstrings are this wiki's own, as are the signs, limits, repair and pseudocode.
