---
title: Automated refactoring
category: change
summary: "Concept: how far a tool-made refactoring can be trusted without running tests. A syntax-tree tool on statically resolved names most; a tool that asks a person to pick call sites, or text search-and-replace, much less; names also used through reflection or strings are where tools miss."
tags: [concept, refactoring, tooling, change-safety, static-typing]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Automated refactoring is a refactoring carried out by a tool rather than by hand. Fowler calls tool support perhaps the biggest change to refactoring in a decade and notes that with a mature tool he is "usually sufficiently confident in its work that I don't bother running the test suite" (ch. 2, PDF p. 81). How far that confidence is earned depends on how the tool works and on the language.

## Text versus syntax tree

- **Text manipulation**, such as search-and-replace for a name or a macro for Extract Variable, is crude and, in Fowler's words, "certainly can't be trusted without rerunning tests", though it is a handy first step (PDF p. 82).
- **Syntax-tree manipulation** is what doing it properly requires: operating on the tree is "much more reliable to preserve what the code is doing" (PDF p. 82). The tool must also re-render the tree as text.

## Static typing

Many refactorings are made much safer by static typing (PDF p. 82). Fowler's case: two classes, a salesman and a server, each with an `addClient` method of different intent. Renaming only the salesman's method without static types leaves the tool unable to tell which calls mean which; it lists the call sites and a person decides, which makes it "a nonsafe refactoring that forces me to rerun the tests" (PDF p. 83). With static types the tool resolves each call to its class and the rename can be completely safe.

## Edge cases

Even sophisticated tools slip on edge cases; less mature ones struggle with reflective calls. Fowler's practice is to run the test suite every so often even with mostly safe refactorings, and he usually mixes automated and manual ones (PDF p. 83).

## Reading against code

This wiki reads the chapter as a ranking of trust a reviewer can apply to a change that claims to be a pure refactoring:

```
safest     tool rename/extract, statically resolved, no reflection on the name
           tool operation needing a person to pick call sites (dynamic dispatch by name)
           text search-and-replace of a name
least safe hand edit with no tests
```

This wiki's own extension of Fowler's reflection remark: a name that also appears in strings used for dynamic lookup (reflection, configuration keys, serialized field names) is where a tool rename most often misses, and is worth a test or a search before trusting it.

Without a test suite, Fowler names safe automated refactorings as one way to refactor at all, while still preferring self-testing code (ch. 2, PDF p. 72; [[self-testing-code]]); the step discipline with tests is [[refactor-in-small-tested-steps]]. Hand-maintained output of restructuring and translation tools is a different matter, covered on [[mechanical-code-transformation]].

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 2, "Automated Refactorings" (PDF pp. 81-83), and "Testing" (PDF p. 72) for refactoring without tests. This wiki's own: the trust ranking and the strings-for-dynamic-lookup example.
