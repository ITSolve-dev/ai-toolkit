---
title: Build debug aids in early and make them switchable
category: debugging
summary: "Debug checks sit commented out, or behind a constant edited by hand in source (`DEBUG = true`, `if false`), instead of behind one build-configured switch or a check routine with a full and an empty implementation."
tags: [rule, debug-aids, build-configuration, defensive-programming]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Debugging aids are, for McConnell, a key part of defensive programming: they find errors fast (p. 200).

## Rule

Do not apply production constraints to the development version automatically: production must be fast, while the development version «может себе позволить работать медленно» (p. 200; a word rejoined across a hyphenation break). It may use resources freely and offer extra capabilities without a security risk (p. 200). The book's examples: a menu item that checks the integrity of a heavily used four-way linked list, and Microsoft Word checking the integrity of its Document object every few seconds when idle in debug mode, which catches corruption quickly (p. 200).

Introduce debugging aids early: usually they are added only after a problem has bitten several times, but added after the first time, or carried over from a previous project, they help through the whole project (p. 200).

Plan to remove them: decide in advance how to avoid shuffling debug code in and out of the program (p. 201). The book's options: version control and build tools that build variants from the same sources (p. 201); a preprocessor symbol, possibly with levels, or a macro wrapping debug code (p. 202); a home-made precompiler for languages without one, which also makes it impossible to compile the unprocessed code by accident (p. 203); and debugging stubs, a routine such as `CheckPointer()` that performs every check it can bear during development and is replaced by an empty routine in production (pp. 203-204). Stubs cost only a little performance and are quicker to set up than a precompiler; keep both versions to switch quickly (p. 203).

## Sign in code

- Blocks of commented-out checks, prints or dumps around the code they would inspect.
- Debug-only code guarded by a hand-edited constant (`if false`, `DEBUG = True` in source).
- A check that walks a whole structure (every node, every record) on each call, with no switch. Whether it may stay on in the release is decided by [[leave-assertions-on]] and [[defensive-code-in-production]].

This wiki assigns the neighbouring case as follows. Debug code with no switch, or with a switch edited by hand in source, is [[switchable-debug-aids]]; a build or deploy setting that switches all checks off is [[leave-assertions-on]].

## When not to apply

- Code the author runs only for themselves, where the book allows leaving all debug aids in (p. 201).
- What must stay in production is decided by [[defensive-code-in-production]], not by convenience; a switch must not be used to drop a check for an important error. The condition that selects the reading: what a failure of the check costs the user in production, and what the check costs to run.
- The project already has a mechanism for this (log levels, a debug build flag, the language's assertion switch). Use it; this page then asks only that debug code sit behind it, not behind a hand-edited constant.

## Repair

Collect debug checks behind one named switch from the build configuration, or behind a check routine with a full and an empty implementation. Turn hand-run integrity checks into a routine the debug build calls at defined points. Remove the hand-edited constants.

## Before and after

```
# before
function do_something(list):
    # print("list size", list.size)       # uncomment when debugging
    # verify_links(list)
    ...
```

```
# after
function do_something(list):
    assert list.head is not none or list.size == 0
    check_list_thoroughly(list)
    ...

# debug build
function check_list_thoroughly(list):
    verify_links(list)          # walks every node: slow, thorough

# release build
function check_list_thoroughly(list):
    return
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, [[code-complete]]: p. 200 for debug versus production constraints and early debug aids, pp. 201-204 for planning removal, preprocessors, precompilers and stubs. The signs, the split with [[leave-assertions-on]], the second and third limits, the repair and the example are this wiki's own.
