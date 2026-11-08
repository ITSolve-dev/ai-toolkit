---
title: Name a repeated subexpression
category: complexity
summary: "The same non-trivial arithmetic or call subexpression, with the same operands (rate / 12 in both numerator and denominator), is written out two or more times in one statement or routine instead of being computed once into a variable named for its meaning."
tags: [rule, duplication, expressions, naming, readability]
paradigm: any
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

Among his code-tuning techniques McConnell includes eliminating common subexpressions: when an expression is repeated, assign it to a variable and use the variable in each place (p. 624). He notes that with a well-chosen name the change «не только повысит производительность кода, но и улучшит его удобочитаемость» (p. 624). That second effect is why the technique belongs in this wiki: it holds even where the speed gain is nil. This wiki reads his definition of tuning (p. 596), a change that degrades structure for speed, as placing a change that also improves readability among standard coding practices rather than tuning.

## Rule

Compute a repeated subexpression once, give it a name that says what it means in the problem, and use that name.

McConnell's measurement shows why the justification has to be readability rather than speed. Naming `interestRate / 12.0` in a loan-payment formula saved 4% in Java and cost 1% in Python (p. 625). He suggests that the expensive `pow` call swamped the saving, or that the compiler had already removed the duplicate (p. 625). This wiki reads that as: do it for the name, not for the clock.

## Sign in code

An identical, non-trivial subexpression with the same operands, unchanged between the occurrences and free of side effects, appears two or more times in one statement or one routine body, for example `rate / 12` in both the numerator and denominator of a formula.

This wiki assigns the neighbouring shapes as follows. A repeated compound boolean condition is [[name-complex-conditions]]. A non-trivial subexpression repeated within one statement or routine is [[name-repeated-subexpression]]; a repeated block of statements is [[dry]]. An expression computing an index into a lookup table is [[isolate-table-key-computation]]'s, wherever it repeats; [[dry]] and [[name-repeated-subexpression]] defer to it. A single expression that combines several sub-calculations, none written twice, is [[extract-variable]]; an identical subexpression written two or more times is [[name-repeated-subexpression]]; a chain of field hops or dereferences is [[explaining-variable]].

## When not to apply

- The two occurrences only look alike and mean different things in the problem. Naming them as one value couples two facts that may change separately; see [[coincidental-duplication]]. This criterion is this wiki's; the source does not discuss it.
- The repeated expression is trivial (a single field access or `x + 1`), and a name would add a line without adding meaning. This limit is ours too.

## Repair

Introduce a local variable before the first use, holding the subexpression, named for its meaning (`monthlyInterest`, not `tmp`), and replace each occurrence. Fowler's Extract Variable mechanics give the order: declare the variable immutable, replace one occurrence and test, then the others one at a time; where the name would mean something outside this routine, make it a function instead (*Refactoring*, 2nd ed., ch. 6, PDF pp. 136-137; see [[extract-variable]]).

## Before and after

Before:

```
payment = loanAmount / ((1 - pow(1 + rate / 12, -months)) / (rate / 12))
```

After:

```
monthlyInterest = rate / 12
payment = loanAmount / ((1 - pow(1 + monthlyInterest, -months)) / monthlyInterest)
```

## Source

- McConnell, *Code Complete*, 2nd ed., Russian edition, section 26.4: the technique and the readability remark, p. 624; the measurements and their explanation, p. 625; the definition of tuning, p. 596. See [[code-complete]].
- Fowler, *Refactoring*, 2nd ed., via [[fowler-refactoring]], ch. 6, "Extract Variable", PDF pp. 136-137: the immutable declaration, the one-at-a-time replacement and the variable-or-function decision.
- This wiki's own: the reading of p. 596 that places the technique outside tuning, the sign's wording (including the unchanged, side-effect-free operands), the assignment against neighbouring pages, both limits, and the pseudocode, adapted from the book's loan example rather than copied.
