---
title: A "temporary" variable is named for its real role
category: naming
summary: "A variable named temp, tmp, t, x, val, res, result2 or aux holding a single intermediate value that has a nameable meaning (a discriminant root, a subtotal, a price before tax)."
tags: [rule, naming, variables]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-07
---

Temporary variables hold intermediate results and service values, and they usually get names like `temp` or `x`. McConnell treats this with suspicion: «использование временных переменных говорит о том, что программист еще не полностью понял проблему» (p. 260). He adds that programmers handle variables officially labelled temporary more carelessly than others, which makes errors more likely, and that in some sense almost every variable is temporary (p. 260).

## Rule

When you are about to call a variable temporary, ask whether you understand its real role, and name it for that role. In the book's example, `sqrt(b^2 - 4*a*c)` is worth keeping in a variable, especially as it is used later, but `temp` says nothing about it. The book calls it `discriminant` (p. 260).

This wiki notes that the book's name is itself slightly off: the stored value is the square root of the discriminant, so `discriminantRoot` would meet [[name-describes-what-the-variable-represents]] more exactly. A reviewer applying this page should check that the new name is also accurate, not just less vague.

## Sign in code

- A variable named `temp`, `tmp`, `t`, `x`, `val`, `res`, `result2`, `aux` that holds a value with a statable meaning.
- A `temp` read more than once, or further than the next line or two from its assignment.

This wiki assigns the neighbouring cases as follows. This page owns a temporary-style name on a variable with one purpose. If the same variable is later reassigned to an unrelated value, [[one-variable-one-purpose]] owns it, and its split comes first. A full word too general for its value (`data`, `value`, `current`) is [[name-describes-what-the-variable-represents]]. A short name on a wide scope that is not an intermediate value is [[name-length-matches-scope]].

`result` as the returned value of a short function that computes one value names a role and is [[rename-extracted-code-for-clarity]]'s convention; `result`-style names on one of several intermediates in a longer routine are [[temporary-variable-names]].

## When not to apply

- The scratch slot of a textbook swap (`temp = a; a = b; b = temp`) inside a three-line block has no role beyond the swap, and `temp` says exactly that. This wiki's own limit; the book does not mention it.
- If the value does not need storing at all, the repair is to inline it, not to rename it. This is this wiki's addition, and it belongs to function-level simplification rather than naming.

## Repair

State in words what the intermediate value is ("square root of the discriminant", "price before tax") and use that as its name. If no statement comes, that is the sign the book points at: the computation is not yet understood, and the code around it should be re-read before naming.

## Before and after

```
temp = sqrt(b*b - 4*a*c)
root1 = (-b + temp) / (2*a)
root2 = (-b - temp) / (2*a)
```

```
discriminantRoot = sqrt(b*b - 4*a*c)
root1 = (-b + discriminantRoot) / (2*a)
root2 = (-b - discriminantRoot) / (2*a)
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 11.2, p. 260 ([[code-complete]]): suspicion of temporaries, careless handling, and the discriminant example. The names in the sign other than `temp` and `x`, the second sign, the remark that `discriminant` is itself imprecise, the assignment against the neighbouring pages, the swap limit and the inline repair are this wiki's own. The pseudocode is this wiki's own version of the book's example.
