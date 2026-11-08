---
title: Loop header holds only control
category: complexity
summary: "A for header that initializes or updates a variable the termination test does not read (a record counter), while the statement that really advances the loop sits in the body; or a loop with an empty body whose work happens inside its condition, such as while ((ch = readChar()) != EOF) ;. An empty body made visible with {} or a no-op is the book's fallback where the rewrite is not clearer (pp. 437-438)."
tags: [rule, loops, control-flow, side-effects]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

The header of a loop says how the loop starts, when it stops and what moves it toward stopping. The body does the work. When the two are mixed, the reader is misled about which variables control the loop. McConnell shows both directions: work pushed into the header, and a header that does all the work while the body stays empty.

## Rule

«Зарезервируйте заголовок цикла for для выражений, управляющих циклом» (p. 367): the expressions that initialize, terminate and move toward termination. In the book's example, a record counter sits in the header while the call that actually advances the file sits in the body. McConnell's point is that this falsely suggests the counter controls the loop. The correct version puts the advancing call in the header and the counter in the body. He adds that a `while` may still suit the task better (p. 367).

The mirror case is the empty loop: «Избегайте пустых циклов» (p. 368). In his example a `while` condition both reads a character and tests for end of file, and the body holds only `;`. The rewrite moves the read into the body of a bottom-tested loop. It takes three lines instead of one, which McConnell accepts because the code does three lines of work (p. 368).

He returns to it in section 19.3: most loops with an empty body rely on a side effect in the control expression, and in most cases the code reads better when those side effects are performed explicitly in the body. The explicit form needs an extra variable and more lines, but it puts the emphasis on simple programming over clever use of side effects, which he calls preferable in production code (p. 438). Where an empty statement is truly intended, in an empty loop or a `switch` case that deliberately does nothing, he makes it visible with a `DoNothing()` marker, which shows that the case was considered and needs no action (p. 438).

This wiki reads chapter 31 as the strongest case for the empty-loop rewrite, although the book makes it there about putting one operation on each line. A compact copy loop in the shape of `strcpy`, which advances both pointers, copies and tests in its condition, looks familiar, so an experienced reader names it and moves on: «вы узнали код, а не прочитали его» (p. 744). The book's version holds a bug, plain once the loop is written one operation per line: both pointers advance before the first character is copied (p. 744). Profiled, the compact form was also 11% slower than the plain one (4.81 s against 4.35 s for 5,000,000 copies, p. 744); the book adds that results vary between compilers and that the point is to measure first (p. 745). Side effects elsewhere in an expression, outside a loop condition, are [[one-side-effect-per-statement]].

This wiki adds the reasoning: an expression in the header that does not control the loop is a side effect in a place the reader scans for control. This wiki reads it as an analogy to [[command-query-separation]], not an assignment: this page owns where the call sits (the loop condition); whether the called method should both change state and return is CQS's question, asked at its definition.

## Sign in code

- A `for` header whose initialization or update clause touches a variable that the termination test does not read, such as a counter of processed items.
- A `for` header whose update clause does not advance toward termination, while the statement that does advance it sits in the body.
- A loop whose body is empty (`;` or `{}`) and whose condition contains an assignment or a call with a side effect.

This wiki assigns the neighbouring cases as follows. Which loop form to use is [[for-or-while]]; this page owns what goes inside the header of the form chosen, including side effects in a loop condition. A side effect in any other expression is [[one-side-effect-per-statement]]. A `for` whose header holds only control but whose termination depends on data read in the body is accepted by the book (p. 367): [[for-or-while]] may prefer a `while`, and [[loop-header-holds-only-control]] does not report it.

## When not to apply

- The extra variable in the header advances in lockstep with the controlling one and is itself an index, such as two pointers walking the same array towards each other. Both then control the loop. This limit is this wiki's own.
- A busy-wait or polling loop on hardware, where the empty body is the point. This limit is this wiki's own; the book's `DoNothing()` marker (p. 438), or a comment, still says so.
- The book applies the empty-loop rewrite "in most cases" (p. 438), not all. This wiki adds: where the language's own idiom for the loop is the condition-driven form and the project's convention uses it, the convention wins, because language idioms are decided at work time.

## Repair

1. Move every header expression that does not take part in termination into the body, or before the loop for an initial value.
2. Move the statement that actually advances toward termination into the update clause, or turn the loop into a `while` with that statement in the body.
3. For an empty loop, move the side effect out of the condition into the body, and use a bottom-tested loop if the body must run before the first test.
4. For a body or `switch` case that is empty on purpose, put an explicit no-op there: a call to a routine such as `DoNothing()` that returns at once, or the language's own construct for "no action".

## Before and after

```
for file.rewind(), count = 0; not file.atEnd(); count++:
    file.readRecord()

while (ch = file.readChar()) != EOF:
    ;
```

```
count = 0
file.rewind()
while not file.atEnd():
    file.readRecord()
    count = count + 1

do:
    ch = file.readChar()
while ch != EOF
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, via [[code-complete]], section 16.2: the reserved header, pp. 366-367; the empty loop, p. 368; section 19.3, pp. 437-438: making empty statements visible, empty bodies relying on side effects and the `DoNothing()` marker; section 31.5, pp. 744-745: the copy loop, recognising instead of reading, and the timing figures. The book's marker is a C++ preprocessor macro, which this page states as a routine because macros are a language matter. The reading of chapter 31 as the strongest case, the analogy to command-query separation, the treatment of a data-driven `for` header, all three limits except the book's "in most cases" and its marker, and the pseudocode are this wiki's own; the pseudocode is adapted from the book's file examples.
