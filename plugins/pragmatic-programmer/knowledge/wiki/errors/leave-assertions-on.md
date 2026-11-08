---
title: Leave assertions on in production
category: errors
summary: "A release build, flag or macro switches all assertions off, or checks sit inside a debug-only guard, instead of disabling only the check that really hurts performance."
tags: [rule, assertions, production]
paradigm: any
sources: [pragmatic-programmer, code-complete]
created: 2026-11-01
updated: 2026-11-06
---

A common view holds that assertions are a debugging aid to remove once code ships. *The Pragmatic Programmer* rejects it as resting on two false assumptions (p. 154).

## Rule

Keep assertions enabled in released code. The first false assumption is that testing finds every bug, when complex code can have only a tiny share of its permutations tested. The second is that the program runs somewhere safe, when production is where memory runs out, cables fail and logs fill the disk (p. 154). If performance is at stake, turn off only the assertions that really hurt it and leave the rest (p. 154).

The book's supporting story concerns a small network-device company that left assertions in its releases. Their reports, shown to the end user through a tidy interface, gave developers enough to fix subtle, hard-to-reproduce bugs and security holes (p. 155). This wiki reads p. 286 as limiting that: what a production assertion reports must be fit for whoever receives it. See [[do-not-disclose-in-output]].

*Code Complete* assumes assertions are compiled out of production (pp. 185-186, [[code-complete]]) and asks instead which checks the release keeps. This wiki resolves the two books on [[defensive-code-in-production]]; the condition that selects the reading, in the words both pages use: what a failure of the check costs the user in production, and what the check costs to run. This page owns the shape of a release that switches every check off; that page classifies the checks for the repair.

## Sign in code

- Build or deploy configuration disables assertions for all of a release.
- A debug-only macro or an `if debug:` guard wraps every check.
- An assertion's failure path discards what it knew, so a production failure reports nothing useful.

Debug code with no switch, or with a switch edited by hand in source, is [[switchable-debug-aids]]; a build or deploy setting that switches all checks off is [[leave-assertions-on]]. A throw that records no values is [[exception-message-carries-context]]; this page owns an assertion's report.

## When not to apply

- One check that really hurts performance, such as an extra full pass over data on a hot path (p. 154). That check alone becomes optional. This wiki adds that the cost should be measured first.

## Repair

Enable assertions in the release configuration. Where the language's assertion statement is removed by the runtime and the setting is out of your control, use an always-on check function instead. Put a named switch on each check that is proven slow. Make a failure report the values involved to an audience allowed to see them, and read [[crash-early]] on what may run after it.

## Before and after

```
# before (release configuration)
assertions = disabled

function merge_sorted(a, b):
    result = merge(a, b)
    assert is_sorted(result)
    assert length(result) == length(a) + length(b)
    return result
```

```
# after (release configuration)
assertions = enabled
expensive_checks = disabled

function merge_sorted(a, b):
    result = merge(a, b)
    if expensive_checks: assert is_sorted(result)    # extra pass over the data
    assert length(result) == length(a) + length(b)
    return result
```

## Source

Thomas, Hunt, *The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation, [[pragmatic-programmer]]: pp. 154-155 for the rule, its reasoning and the limit, and p. 286 for output. McConnell, *Code Complete*, Russian edition, [[code-complete]], pp. 185-186, for the opposing assumption. The signs, the splits with neighbouring pages, the requirement to measure, the audience condition, the repair and the example are this wiki's own.
