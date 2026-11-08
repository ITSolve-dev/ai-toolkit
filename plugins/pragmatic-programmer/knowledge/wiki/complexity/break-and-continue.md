---
title: Break and continue
category: complexity
summary: "Three or more break statements at different depths of one loop body, a continue that follows real work, an unlabelled break inside a switch or if nested in a loop, a loop body wholly wrapped in one filtering if, or a done flag threaded through a while with if-not-done guards deepening the nesting: decide between break, flags, split loops and a top-of-loop continue."
tags: [decision-rule, loops, control-flow, nesting, early-exit]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

`break` leaves a loop by its normal exit, and `continue` skips the rest of the current pass, acting as a shorthand for an `if` around the remainder (p. 372). McConnell neither bans nor endorses them. He gives a test for when each helps and when each signals a loop that is badly understood.

## Rule

- **break over flags.** Consider `break` instead of boolean flags in a `while`. Flags added to fake an exit can make the code harder to read. A few separate `break`s placed beside the code that triggers them can remove levels of indentation (p. 372). Chapter 24 lists the same move as a refactoring: if a variable such as `done` controls a loop, remove it and leave with `break` or `return` (p. 560).
- **But not many.** «Остерегайтесь цикла с множеством операторов break, разбросанных по всему коду» (p. 372). Many exits suggest the loop's structure or role is unclear, and that it could be expressed more clearly as several loops. McConnell calls the count a warning sign, not proof of a bug (p. 372).
- **continue only at the top.** «Используйте continue для проверок в начале цикла» (p. 373): skip unwanted records with a guard at the top, which removes an indent from the whole body. If the `continue` would fall in the middle or at the end, use an `if` instead (p. 373).
- **Name the target.** Where the language has labelled `break`, use it. The book's case is the outage of 15 January 1990, which took the New York telephone network down for nine hours (SEN, 1990, p. 372): a `break` meant for an `if` instead left the enclosing `switch` inside a `do` loop. A labelled `break` makes the target unambiguous (p. 373).
- **Last resort.** «Используйте break только после того, как рассмотрели все альтернативы» (p. 374). McConnell's reason is that structured-programming opinion is divided, so you should be able to argue for each use.
- **Long loops get one exit** (p. 377; see [[loop-length-and-nesting]]).

## Sign in code

- Three or more `break`s in one loop body, at different depths.
- A `continue` that follows real work in the body.
- A `break` inside a `switch` or `if` nested in a loop, in a language where it leaves the innermost `switch` or loop, with no label naming its target.
- A loop body wholly wrapped in one filtering `if`, with nothing after it, where a `continue` at the top would remove the indent from the whole body.
- A `while` driven by a `done` flag that is set in several branches, each followed by `if not done` guards that deepen the nesting.

This wiki assigns the neighbouring cases as follows. This page owns exits by `break` and `continue` and the flags that stand in for them. A single `break` that turns a top-and-bottom duplication into a middle exit is [[loop-with-exit-in-the-middle]]. An assignment to a `for` index to force an exit is [[for-or-while]]. Several exits in a loop too long to see at once are this page; [[loop-length-and-nesting]] decides only whether the loop is long.

## When not to apply

- A short loop. McConnell allows riskier structures such as `break`, `continue`, multiple exits and complex conditions in short loops (p. 377).
- A single `break` that removes a top-and-bottom duplication is [[loop-with-exit-in-the-middle]], which owns that shape.
- One `break` from a short `for` that searches a bounded range is accepted; [[break-and-continue]] owns it and does not report it. A search loop with *no* exit at the hit is [[stop-loop-once-answer-known]].

This wiki resolves the apparent conflict between the first two bullets of the rule by count and position. Breaks beside the condition that triggers them, replacing flags, are the repair. Breaks scattered at several depths are the symptom.

## Repair

1. For a flag-driven `while`, replace each flag assignment with a `break` at the point the condition is known, and delete the guards the flag required.
2. For many scattered `break`s, find the phases the loop runs through and split it into one loop per phase, each with one exit, or extract the body into a routine that returns.
3. For a `continue` after work, invert its condition into an `if` around the remaining work, or move the test to the top if it does not depend on the work.
4. For a nested ambiguous `break`, use a labelled `break`, or extract the inner construct into a routine and `return`.

## Before and after

```
done = false
while not done and i < n:
    if invalid(item[i]):
        done = true
    if not done:
        if limitReached():
            done = true
        if not done:
            process(item[i])
            i = i + 1
```

```
while i < n:
    if invalid(item[i]): break
    if limitReached(): break
    process(item[i])
    i = i + 1
```

`continue` as a top guard:

```
while not file.atEnd():
    record = file.read()
    if record.type == target:
        handle(record)
        log(record)
```

```
while not file.atEnd():
    record = file.read()
    if record.type != target: continue
    handle(record)
    log(record)
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]], section 16.2, "Досрочное завершение цикла", pp. 371-374, p. 377 for long loops, and section 24.3, p. 560, for the refactoring form. The count-and-position resolution, the threshold of three in the first sign, the wording of the third and fifth signs, the bounded-search limit, the assignment against the neighbouring pages, repair steps 2 and 4 except the labelled `break`, and the pseudocode are this wiki's own.
