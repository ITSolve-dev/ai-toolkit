---
title: Layout must tell the same story as the logic
category: complexity
summary: "Indentation or spacing implies a grouping the language does not apply: an unbraced if/for/while/else followed by two or more statements at the same deeper indent, an else lined up with an if it does not belong to, spacing like 3+4 * 2+7 that contradicts precedence, or an expression mixing operators of different precedence with no parentheses."
tags: [rule, readability, layout, precedence, misleading-indentation]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell's Fundamental Theorem of Formatting is that good visual layout shows the logical structure of a program (p. 715). The part of it this wiki keeps is not aesthetics, which the project's formatter owns, but the case where layout and logic **disagree**. The human reader infers structure from what the code looks like, the compiler from braces, keywords and precedence, and where the two diverge the reader is misled about what runs. In the source's words, formatting is the «ключ к структуре программы», and a good scheme tells «одну и ту же историю» to the human and to the computer (p. 716).

## Rule

Where layout implies a grouping, the grouping must be the one the language actually applies. Two shapes from the source (p. 716):

- **Indentation that implies a block that does not exist.** A listing indents three statements under a `for` with no braces; a reader takes all three as the loop body, while the compiler runs the first one `MAX_ELEMENTS` times and the other two once.
- **Spacing that implies a precedence that does not hold.** In `x = 3+4 * 2+7` a reader tends to see `(3+4) * (2+7)`, that is 63, while the compiler computes `3 + (4*2) + 7`, that is 18.

A related prescription from the same chapter: use parentheses more often than seems necessary, to clarify expressions of two or more terms; they may be unneeded, but they «добавляют ясности и ничего вам не стоят» (p. 721). His test is `12 + 4 % 3 * 7 / 8`: even experienced programmers cannot answer with full confidence without a reference, so use parentheses whenever there is the slightest doubt how an expression evaluates (p. 721).

The theorem also gives a tie-break the source states outright: where one technique shows structure better and another looks prettier, use the one that shows structure (p. 715).

## Sign in code

- A control statement (`if`, `for`, `while`, `else`) with no block delimiters, followed by two or more statements at the same deeper indentation.
- An `else` whose indentation lines it up with an `if` it does not belong to.
- An expression mixing operators of different precedence where whitespace clusters operands the way precedence does not (tight spacing around a lower-precedence operator, wide around a higher one).
- An expression mixing arithmetic, modulo, shift, bitwise or logical operators of different precedence with no parentheses at all.

This wiki assigns the neighbouring cases as follows. This page owns a disagreement between layout and semantics. Nesting that is visible and correct but too deep is [[tame-deep-nesting]]. A compound condition that is correctly parenthesised but hard to read is [[name-complex-conditions]].

## When not to apply

- Whitespace and indentation rules as such (indent width, brace placement, where `begin` and `end` go) are not this page. The source itself presents several brace styles as consistent with the theorem (pp. 722-726), and the charter leaves that choice to the project's formatter and conventions. This page fires only when layout and semantics disagree.
- Where a formatter or a misleading-indentation warning runs on the code, the indentation half is caught mechanically and is no finding here. Where neither runs, report the line.
- End-of-line alignment as a style (statements aligned under a keyword in the middle of the line above) is formatting, which the formatter rewrites; its one semantic case, an `else` lined up with the wrong `if`, is the second sign.
- In languages where indentation *is* the block structure, the indentation half cannot occur; the precedence half still can.
- An expression of a single operator kind, or an idiom whose precedence no reader of the language doubts (`a * b + c`), does not need parentheses. The source says to parenthesise whenever there is doubt, without saying where doubt ends.

All but the first limit are this wiki's own.

## Repair

- Add the block delimiters the indentation implies, or dedent the statements that are not part of the body, whichever matches the intent. Decide the intent first: the source reads its listing as an author who meant all three statements to run in the loop (p. 716).
- Respace the expression so visual clusters match precedence, and add parentheses around every sub-expression whose evaluation order a reader might doubt.

## Before and after

```
// brace-delimited language: without braces only the first line is the body
// swap left and right elements across the array
for (i = 0; i < MAX; i++)
    tmp = left[i];
    left[i] = right[i];
    right[i] = tmp;

x = 3+4 * 2+7
r = base + offset % size * scale / unit
```

```
// swap left and right elements across the array
for (i = 0; i < MAX; i++) {
    tmp = left[i];
    left[i] = right[i];
    right[i] = tmp;
}

x = 3 + (4 * 2) + 7
r = base + (((offset % size) * scale) / unit)
```

The "after" puts the body in a block, so the layout and the compiler agree, and every mixed-precedence sub-expression is parenthesised.

## Source

- McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 31: the Fundamental Theorem and the structure-over-beauty tie-break, p. 715; human against computer interpretation and the two listings, p. 716; parentheses, p. 721; brace styles, pp. 722-726; end-of-line layout degrading under nesting, p. 727. See [[code-complete]].
- Quotations were transcribed from the extracted text and need the page-image check.
- This wiki's own: the reduction of the chapter to the disagreement case (the charter drops formatting as such), the list of signs, the assignment against neighbouring pages, the limits on tooling, end-of-line alignment and indentation-significant languages, the limit on where parentheses stop helping, and the pseudocode.
