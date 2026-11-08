---
title: Do not silence warnings
category: debugging
summary: "A compiler or analyser warning is suppressed by a pragma, annotation or lowered warning level with no stated reason, or a change adds a warning to the build and leaves it there."
tags: [rule, debugging, compiler-warnings, static-checks]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell calls the compiler one of the simplest and most effective debugging tools (p. 545). This page is not about what a particular compiler catches, which changes with the toolchain and is out of this wiki's scope, but about the code and build settings that hide its findings.

## Rule

Set the compiler to its strictest diagnostic level and remove every error and warning (p. 545). The book says ignoring errors is foolish and turning warnings off is more foolish: «Отключая вывод предупреждений, вы совершаете такую же ошибку: вы лишь перестаете их видеть, но их причины никуда не исчезают» (p. 545). Assume the compiler writers know the language better than you and look for the real meaning of each warning (p. 545). Where possible, treat warnings as errors, which raises their weight and stops a build from going on past them (pp. 545-546). The book's closing question: how will you fix subtle errors if you ignore the obvious ones (p. 550). Chapter 34 says the same in its advice to make defects conspicuous: if a program produces warnings, fix them, because you are unlikely to notice subtle warning signs while ignoring the ones that say WARNING outright (p. 829).

Chapter 33 adds what has to come before any decision about a warning: understanding it. McConnell lists, among the forms professional honesty takes, «стремление разобраться в предупреждениях компилятора вместо их отключения» (p. 806). His reasoning is about cost. A programmer who does not understand a warning, or thinks he does but has no time to check, will probably end up solving the problem from scratch while the compiler was holding out the answer (p. 807). His anecdote: asked to help debug, he asks whether the program compiles with no errors and no warnings. He is told it does and hears the symptoms, and says it looks like an uninitialised pointer, which the compiler should have warned about. The answer is that it did warn, but they thought the warning meant something else (p. 807). The book calls the belief that one understands the compiler's messages a widespread flaw (p. 807).

## Sign in code

- A pragma, annotation or comment directive disables a warning at a site, with no comment naming why the warning is wrong there.
- Build configuration lowers the warning level or removes a warning class project-wide.
- The change under review adds a warning to the build, or leaves one standing on lines it touches.
- A suppression covers a whole file or module where the warning fires on one line.

A build under investigation for a bug that still emits warnings on the failing path is the first step of [[debugging-procedure]], which owns that case; [[do-not-silence-warnings]] owns the suppression constructs and the build settings.

## When not to apply

The book states no limit. The following are this wiki's own.

- The warning is a confirmed false positive at that site. Suppression is then acceptable when it is the narrowest available, at the site, and carries the reason.
- Generated or vendored code outside the project's control; it is excluded at the boundary, not inside project code.
- A legacy build already carries many warnings. Then the rule asks the change not to add any and to clear those on the lines it touches; clearing the rest is separate work. This matches the limit on step 1 of [[debugging-procedure]]. The book gives a reason that supports it: warnings seen over and over are either ignored, and then hide more important ones, or simply irritate (p. 224).

## Repair

1. Remove the suppression and read the warning against the code it points at, until you can state what it claims (p. 807).
2. Change the code so the warning's cause is gone, or, for a confirmed false positive, narrow the suppression to the site and state the reason.
3. Restore the strict level in the build and, where the toolchain allows it, make warnings fail the build.

## Before and after

```
// before
@suppress("unused-result")
function save(record):
    store.write(record)       // the write's status is dropped
```

```
// after
function save(record):
    status = store.write(record)
    if status is failure:
        raise SaveFailed(record.id, status)
```

A warning switched off because it was misread, in the shape of the book's uninitialised-pointer anecdote:

```
// before
// build flags: warnings about uninitialised variables disabled
function total(items)
    declare sum
    for each item in items
        sum = sum + item.price      // tool warned: sum may be used uninitialised
    return sum
```

```
// after
// build flags: all warnings on
function total(items)
    sum = 0
    for each item in items
        sum = sum + item.price
    return sum
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition: [[code-complete]], section 23.5, pp. 545-546, and p. 550. The rule and its reasons are the book's, paraphrased except where quoted; the quotation was transcribed from the extracted text with line-break hyphens joined. The book also asks for project-wide standard compiler settings (p. 546); this wiki leaves that out as process. Section 33.4, pp. 806-807: understanding warnings as a form of professional honesty, the cost argument and the uninitialised-pointer anecdote; that quotation too was transcribed from the extracted text. Section 34.7, p. 829: fixing warnings as part of making defects conspicuous. Section 9.3, p. 224: the same advice at compile time, and the reason quoted in the legacy-build limit. The signs, the limits (apart from that reason), the assignment against [[debugging-procedure]], the repair and the pseudocode are this wiki's own; the book shows no code for these points. Related: [[programming-by-coincidence]], [[isolate-unsafe-memory-operations]].
