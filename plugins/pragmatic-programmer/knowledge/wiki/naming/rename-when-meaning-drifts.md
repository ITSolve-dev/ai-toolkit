---
title: Rename when meaning drifts
category: naming
summary: "A name no longer matches the body, such as a get function that writes a file, or a comment has to explain what the name really does."
tags: [rule, naming, change, refactoring]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-07
---

Code changes and its names do not follow by themselves. A name that has come to mislead does more harm than one that says nothing (p. 295). This wiki adds that the reason is that readers trust words before code.

## Rule

«Именуйте правильно; а по мере надобности переименовывайте» (p. 295). Code gets reorganized, emphasis shifts and meaning moves a little. Without vigilance a codebase soon holds «запутанных имен, вызывающих еще большие проблемы, чем имена бессмысленные» (p. 295). The book's example is an explanation nobody should have to give: «Подпрограмма getData на самом деле записывает данные в архивный файл» (p. 295).

When a name no longer expresses intent or misleads, fix it at once, as with any defect (p. 295; see [[software-entropy]]), using a full regression suite to catch any instances that were missed.

If for some reason a wrong name cannot be changed now, the book says there is a bigger problem: the ease-of-change principle is broken ([[easier-to-change]]). Fix that first, then change the name, and make renaming easy and frequent (p. 295).

This wiki takes the reasoning from the priority of words described in [[name-by-role]]: a reader takes in the name before reading the body.

## Sign in code

- A function named `get`, `is`, `check` or `calculate` writes to storage or changes state.
- A comment beside a name corrects it, in the manner of "actually sends the email too".
- A variable or class keeps a name for something its type or content no longer holds.
- A name refers to a component, format or service that nothing else in the codebase defines.

A method that mutates and returns a value describing that mutation (a count, a flag, a previous value), or a method named for its action that also returns a result it computed (an item found), belongs to [[command-query-separation]]; a method whose name promises a read or a result and which also writes as a side job belongs to [[rename-when-meaning-drifts]].

Names an extraction carried over from the caller are [[rename-extracted-code-for-clarity]]; a name that a later change made untrue is [[rename-when-meaning-drifts]].

## When not to apply

The book's rule assumes the rename is the team's to make. This wiki's limit: a public interface with outside callers cannot be renamed in one step, and in that case the safe move is to add the new name, keep the old one as a marked alias, and remove it on a stated schedule. A tool-generated name or a name fixed by an external format is also outside the rule, and a comment should say why.

This wiki's limit: a getter that fills a private cache or initializes lazily, with no effect a caller can observe, is not a misleading name.

## Repair

1. Name the thing for what it does now, and if an honest name needs "and", split it first.
2. Find every use, including strings, configuration and tests.
3. Run the regression suite.
4. If the rename cannot be done safely, fix the reason first, because that reason is the larger problem.

## Before and after

Before: the name promises a read, and the body also writes.

```
function get_report():
    report = new_report()
    archive.write(report)
    return report

report = get_report()
```

After: an honest name would need "and", so the function is split, and the write shows at the call site.

```
function archive_report(report):
    archive.write(report)

report = new_report()
archive_report(report)
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, Dialektika, 2020 ([[pragmatic-programmer]]): p. 295. This wiki's own: the link from p. 295 to the priority of words on pp. 291-292, the signs, the limits on public interfaces, fixed names and caches, the repair steps beyond the regression suite, and the pseudocode. Related: [[refactoring]], [[refactor-early-and-often]], [[one-name-per-concept]].
