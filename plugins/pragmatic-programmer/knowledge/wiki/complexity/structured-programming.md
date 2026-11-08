---
title: Structured programming
category: complexity
summary: "Concept: control constructs with one entry and one exit; any control flow can be built from sequence, selection and iteration, so break, continue, return and throw are each examined for whether they make the flow easier to follow."
tags: [concept, structured-programming, control-flow]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Structured programming, named in Dijkstra's 1969 NATO paper, is in McConnell's summary the simple idea that a program should use control constructs with one entry and one exit: a block of code with a single place it can start and a single place it can end (p. 448). The book separates it from top-down structured design: it concerns the coding level only (p. 448).

## Why it matters

A structured program can be read top to bottom and executes in nearly the same order; less disciplined code gives a less clear picture of how it runs, and the book chains that to worse understanding and, in the end, worse quality (p. 448). The book says its concepts still apply to the use of `break`, `continue`, `throw`, `catch` and `return` (p. 448).

## The three constructs

- **Sequence**: statements executed in order, such as assignments and calls (pp. 448-449).
- **Selection**: one of several blocks is chosen, as in `if-then-else` and `case`/`switch`. The book treats `if` and `case` as conceptually alike; a `case` can be emulated with `if`s (p. 449).
- **Iteration**: a group of statements executed repeatedly, as in `for`, `while` and the loop with exit (p. 450).

The core thesis, after Böhm and Jacopini (1966): any control flow can be built from these three (p. 450). McConnell's own position is that programming has progressed largely by restricting what languages let us do, and that any control structure beyond the three, such as `break`, `continue`, `return` and `throw-catch`, «должны рассматриваться под критическим углом зрения» (p. 450).

## How this wiki applies it

The book asks for scrutiny of early exits, not their removal: in the same chapter it lists guard clauses, a block with exit (`break`) and exceptions among the repairs for deep nesting (pp. 440, 448). This wiki reads the concept as a test for each non-structured exit: does it make the routine's flow easier to follow top to bottom than the nested alternative? It does not read it as a single-return rule. Pages that apply the test: [[guard-clauses]], [[break-and-continue]], [[loop-with-exit-in-the-middle]], [[goto-as-last-resort]], [[tame-deep-nesting]], [[decision-point-count]].

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, section 19.5, pp. 448-450: see [[code-complete]]. The definition, the three constructs, the Böhm-Jacopini thesis and the call for critical scrutiny are the book's. The reconciliation with the chapter's own early-exit repairs and the per-exit test are this wiki's reading.
