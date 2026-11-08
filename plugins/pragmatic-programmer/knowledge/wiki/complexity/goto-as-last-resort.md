---
title: goto only as a last resort, and disciplined
category: complexity
summary: "A goto where an equivalent built-in construct (loop, break, return, finally, extracted routine) exists; a backward jump; several labels per routine; an unused label; a jump into the middle of another branch's block."
tags: [rule, goto, control-flow, structured-programming]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell weighs both sides of the goto debate (pp. 389-393 of [[code-complete]]). Against goto: code with it is hard to indent so that the indentation shows the logic, it defeats compiler optimisation, it breaks top-to-bottom flow, and once one is allowed more follow. For goto: a well-placed one removes duplicated code, and it centralises cleanup. His verdict: nine gotos in ten, in simple and in complex cases alike, can be replaced by sequential constructs; in the one case in a hundred where goto is legitimate, document it and use it (p. 400). «Стремление к коду без goto — это не цель, а результат» (p. 391). That result comes from systematic decomposition and a sensible choice of control structures.

## Rule

- Do not use goto where an equivalent built-in construct exists (p. 400).
- Use goto to emulate structured constructs only in languages that lack them, and emulate them exactly (p. 400).
- Measure any goto added for performance, and document the gain so that it is not removed (p. 400).
- One goto label per routine, and jumps forward only, unless emulating control constructs (pp. 400-401).
- Every label is used. An unused label may point to unfinished code; remove it. No goto may leave code unreachable (p. 401).
- Do not reject others' suggestions for removing a goto: «Они могут заметить то, на что вы не обратили внимания» (p. 400).

The chapter's wider stance follows from this. Software development has progressed largely by restricting what programmers can do with their code. Computed jump targets, jumps into the middle of another routine, and code generated and run on the fly trade structure and control of complexity for flexibility (p. 401).

## Sign in code

- A goto that only replaces a loop, `break`, `continue`, `return` or `finally`.
- A backward goto, or more than one label in a routine, outside a hand-built control construct.
- A label nothing jumps to, or code after an unconditional goto that no path reaches.
- A goto that jumps from one branch into the middle of another branch's block so that both share a tail. The book's example jumps into an `else` and calls it nearly impossible to read and hard to rewrite correctly (p. 399).

This wiki assigns ownership as follows. The cleanup-label goto is owned by [[error-exits-sharing-cleanup]], which weighs it against its alternatives. A jump into a loop body other than through its top is [[loop-with-exit-in-the-middle]].

## When not to apply

- Emulating a structured construct the language lacks (p. 400).
- A goto that measurement shows is needed for speed, documented as such (p. 400).
- The rare case where a programmer who fully knows the alternatives without goto chooses goto for readability and maintainability (pp. 392-393). The book's analogy: if you are wearing rubber boots, there is no need to walk around the block to avoid a puddle (p. 400).

## Repair

For a jump into another branch, move the shared code into a routine of its own and call it from both places, which keeps the original conditional structure. The book calls this generally the best approach (p. 399). Where extraction is impractical, restructure the condition so that the shared code follows both branches, at the cost of retesting a condition (pp. 399-400). The book's own rewrites cost a little size and speed, so «если этот код не исключительно критичен к скорости и объему, перепишите его, не задумываясь об эффективности» (p. 399).

When rewriting any goto, verify that the new code behaves the same on every path. The book quotes a textbook whose «простой» rewrite of a loop exit changed behaviour, and reports that several expert programmers rewrote the jump into an else incorrectly (pp. 392, 399). This wiki reads that as the main failure mode of the repair. Pin the behaviour with a test before the rewrite, especially on the boundary input that triggers the jump.

## Before and after

```
if statusOk:
    if dataAvailable:
        value = x
        goto SHARED
else:
    value = getValue()
    SHARED:
    ... many lines ...
```

```
if statusOk:
    if dataAvailable:
        value = x
        doSharedWork(value)
else:
    value = getValue()
    doSharedWork(value)
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 17.3-17.4, pp. 389-401: [[code-complete]]. The arguments, the guidelines, the jump-into-else example and its two rewrites, and the account of incorrect rewrites are the book's. The advice to pin behaviour with a test before rewriting is this wiki's own transfer, as are the ownership notes and the pseudocode.
