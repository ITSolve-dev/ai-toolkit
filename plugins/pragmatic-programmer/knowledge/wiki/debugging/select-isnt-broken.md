---
title: select isn't broken
category: debugging
summary: "A sleep, retry, reimplementation or comment works around a library, OS or compiler call, blaming it with no link to a reproduced defect in that dependency."
tags: [rule, debugging, dependencies]
paradigm: any
sources: [pragmatic-programmer, code-complete]
created: 2026-11-01
updated: 2026-11-06
---

When a program misbehaves near a platform call, the likely fault is in how the program uses that call. The name comes from a senior engineer on one of the authors' projects, who was convinced that the `select` system call was broken in Unix (p. 132).

## Rule

The tip reads «Системный вызов select работает нормально» (p. 132). A defect may be in the operating system, compiler or third-party product, but that should not be the first thought (p. 132). It is much more likely that the application calls a library wrongly than that the library is broken (p. 132). In the story, argument failed to move the engineer, and the fact that all other networked applications worked on the platform was ignored; he spent weeks on workarounds that did not remove the fault, then read the documentation for `select` and fixed the problem in minutes (p. 132). The book's image is that hoofprints should suggest horses before zebras (p. 132). Even when the fault does lie in a third-party product, you must still eliminate the faults in your own code before filing a report (p. 132).

McConnell states the same order of suspicion with a figure. He calls suspecting the compiler or the hardware a symptom of superstition, a feel for the program in place of understanding it, and cites Ostrand and Weyuker (1984): «только около 5% всех ошибок связано с аппаратурой, компиляторами или ОС» (*Code Complete*, Russian edition, p. 223). He adds that the share is probably smaller now, and that the programmer who has reached understanding looks first at their own code (p. 223). This wiki notes the figure is dated and is the book's only quantity here; it sets the order of suspicion and not a ban.

## Sign in code

- A sleep, double call, retry or wrapper around a dependency call, with a comment blaming the dependency and no link to a report or a minimal reproduction.
- A local reimplementation of a standard routine, justified only by a claim that the original is unreliable.
- A version pin or a suppressed error attributed to a dependency, with no reference to a known defect.

This wiki counts a comment as blaming a dependency when it calls the dependency broken, flaky or unreliable. A comment citing the dependency's documented limit gives a reason, which [[comment-why-not-how]] accepts.

This wiki assigns the neighbouring cases as follows. This page owns a workaround whose comment blames a dependency, and it comes first, because the other repairs assume a cause nobody has checked. A delay before reading a result something else produces, with no such comment, is [[temporal-coupling]]. A delay or retry beside a run of overlapping calls, with no stated cause, is [[remove-calls-you-cannot-justify]]. A retry a fix adds at the failing line, blaming nothing, is [[fix-the-root-cause]]. A delay none of these explains is a question under [[comment-why-not-how]].

## When not to apply

- The dependency is the one thing that changed. If you changed a single component and the system stopped working, that component is the likely cause, however improbable it seems (p. 132). The changed component may be outside your view: a new operating system version, a compiler, or other third-party software can damage code that worked before (p. 132).
- A new release can also bring new defects that break earlier workarounds, and APIs and behaviour change (p. 132).

This wiki adds a third limit: a reproduction using only the dependency, with none of your code, shows the fault. The workaround is then legitimate and should link that reproduction.

## Repair

1. Read the documentation for the call, as in the story (p. 132).
2. Ask what changed, including the environment (p. 132).
3. Reduce to a program with the call alone and your actual arguments.
4. If the small program works, the fault is probably in your use of the call, or in a context the small program lacks, such as load, timing or earlier state. Add that context back until the failure returns, fix what it shows, and delete the workaround only once the failure is gone under its original conditions.
5. If it fails, attach it to a report, and leave the workaround with the link.

## Before and after

The book does not say what the defect in the story was. The example is this wiki's own illustration.

```
// before: the platform is blamed, and the workaround does not cure it
// poll is unreliable on this OS, so try twice
ready = poll(sockets, timeout)
if ready is empty:
    sleep(50)
    ready = poll(sockets, timeout)
```

```
// after: the documentation says poll overwrites the set it receives
ready = poll(copyOf(sockets), timeout)
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation: [[pragmatic-programmer]], pp. 131-132. The rule, the story and the two limits about change are the book's. The 5% figure and the superstition framing are McConnell's, [[code-complete]], p. 223. The signs, the reading of blame and the assignment against the neighbouring pages, the third limit, repair steps 3 to 5 and the pseudocode are this wiki's own. See [[prove-dont-assume]] for how this rule sits with the demand to verify everything: this page sets the order of suspicion, and that page sets the evidence needed to clear a suspect. The defect-origin figures behind this order of suspicion are collected in [[where-defects-come-from]].
