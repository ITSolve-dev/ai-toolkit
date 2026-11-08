---
title: Move Function in steps
category: change
summary: "Procedure for relocating a function whose body reaches mostly into another class, module or enclosing scope (or a nested helper that has value on its own): move the least-dependent function of a cluster first, copy and adapt, turn the original into a delegator, test, then inline the delegator."
tags: [method, refactoring, move-function, modularity, encapsulation, nested-functions]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

**Move Function** (formerly Move Method) relocates a function from one context (a class, a module, an enclosing function) to another. Fowler calls it the main tool for making the grouping of code follow a better understanding of it. He distinguishes casual moves between nested functions from "a deeper change in the context of the function", which he steps through deliberately (ch. 1, PDF p. 46).

Which function belongs where is decided by the pages that own the sign, such as feature envy on [[refactoring-warning-signs]] and [[information-expert]]; this page is the procedure that carries out the move and the decisions taken while running it.

## Why move a function

Fowler places the heart of design in modularity: "my ability to make most modifications to a program while only having to understand a small part of it" (ch. 8, PDF p. 225). Understanding grows, so the grouping has to be changed as it grows (p. 225). The reasons he lists (p. 225):

- The function references elements in another context more than elements in its own. Moving it next to them improves encapsulation, and the rest of the code depends less on this module's details.
- Its callers live elsewhere, or the next enhancement needs to call it from elsewhere.
- A helper nested inside another function has value of its own and should be reachable.

To decide, look at three things: which functions call this one, which functions it calls, and which data it uses (p. 225). If a group of functions needs a new home, create one first (Combine Functions into Class, Extract Class).

Fowler also says the choice is often not worth agonising over: "the more difficult this choice, often the less it matters" (p. 226). He tries a context, sees how well it fits and moves the function again if it does not. This wiki reads that as permission to decide quickly when the counts of references are close, because the move can be reversed. It is not permission to leave a function where nearly all its references point elsewhere.

## Procedure

1. **Examine everything the function uses in its current context** and decide whether some of it should move too. If a called function should move, move it first, so a cluster moves starting with "the one that has the least dependency on the others in the group" (p. 226). If a high-level function is the only caller of its subfunctions, you can inline them, move the one function, and extract them again at the destination.
2. **Check for polymorphism.** In an object-oriented language, check whether superclasses or subclasses declare the same method.
3. **Copy the function to the target and adapt it.** Do not cut yet. Elements of the source context that the body uses are either passed as parameters or reached through a reference to the source; in the chapter 1 example, parameter references become the host's own fields (`aPerformance` becomes `this.performance`, PDF p. 47). The function often needs a new name that fits the new home. Fowler gives the copy a temporary name while both exist, so the two are easy to tell apart (p. 228).
4. **Run static analysis.** Undefined symbols in the copy show what still depends on the old context; in Fowler's example the static analysis flags the copy's undefined `distance` and `points` (p. 228). Of a plain compile in chapter 1 he notes that it catches syntax errors "but little more than that. Even so, that can be a useful step" (p. 47).
5. **Make the source function delegate to the target. Test and commit.** Fowler calls this the crucial point for testing (p. 230). Every existing caller still works, and behaviour now runs through the new home.
6. **Consider inlining the source function** (Inline Function, [[inline-function]]). A delegator can stay indefinitely, but "if its callers can just as easily reach the target directly, then it's better to remove the middle man" (p. 226). See [[hide-delegate-or-remove-middle-man]].
7. Repeat for the next function of the cluster.

A safe intermediate step for a nested helper: first nest the functions it depends on inside it, and check with static analysis and tests that nothing broke. Only then copy the whole cluster out (p. 229).

## Why this order

This wiki reads the order as follows: each step leaves the code working, so a failing test points at the one step just taken, and the delegator lets the move be verified before any caller changes. The general rhythm is [[refactor-in-small-tested-steps]].

Where callers cannot all be edited in the same change, step 6 is deferred and the delegator becomes the old form of a [[parallel-change]]; this link is this wiki's own.

## Decision: pass the value or pass the object

When Fowler moves `overdraftCharge` from `Account` to `AccountType`, the body still needs `daysOverdrawn`, which varies per account (pp. 232-233). He passes the plain value for now and would switch to passing the account "if I require more than just the days overdrawn from the account—especially if what I want from the account varies with the account type" (p. 233). Passing the account trades a wider dependency for a stable signature. Compare [[pass-what-the-routine-uses]] and [[tramp-data]].

## Nested functions

Fowler moves the nested distance helpers to the top level and says: "I'm wary of nested functions—they too easily set up hidden data interrelationships that can get hard to follow" (p. 232). He controls visibility with the module system rather than by nesting, and grants that in some languages nesting may still be the visibility tool. This wiki reads the hidden relationship as the closure: a nested helper that silently reads the enclosing function's parameters has an input that its signature does not show.

## When the full procedure is not needed

Fowler moved nested functions casually when the move did not change the function's context (p. 46). The full copy-delegate-inline sequence is for moves that change what the function's body refers to.

## Failure modes

These are this wiki's own reading of the procedure.

- Moving a function that is overridden in subclasses without accounting for the hierarchy (step 2 skipped).
- Keeping a delegator forever when its callers could reach the target directly, which leaves a middle man.
- Keeping the old name, which read well in the old context but misleads in the new one.

## Example

```
// step 5: original becomes a delegator
function amountFor(perf)
    return new Calculator(perf, playFor(perf)).amount()

// step 6: delegator inlined at its caller
function enrich(perf)
    calc = new Calculator(perf, playFor(perf))
    copy = shallowCopy(perf)
    copy.amount = calc.amount()
    return copy
```

Passing the varying value into the new home:

```
class Account
    bankCharge(): return 4.5 + (daysOverdrawn > 0 ? type.overdraftCharge(daysOverdrawn) : 0)

class AccountType
    overdraftCharge(daysOverdrawn)
        if not isPremium then return daysOverdrawn * 1.75
        base = 10
        return daysOverdrawn <= 7 ? base : base + (daysOverdrawn - 7) * 0.85
```

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed.: ch. 1, "Moving Functions into the Calculator", PDF pp. 46-48, for the chapter 1 steps and the casual-move remark; ch. 8, "Move Function", PDF pp. 225-234, for the motivation, the reasons, the mechanics (least-dependent first, polymorphism check, temporary name, delegate, inline), the nested-helper step, the value-or-object decision and the wariness of nested functions. This wiki's own: the explanation of why the order works, the link to [[parallel-change]], the pointers to the owners of the sign, the reading of "the less it matters" as conditional on close reference counts, the reading of a nested function's hidden relationship as an unlisted closure input, the failure modes and the pseudocode.
