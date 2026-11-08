---
title: Name complex conditions
category: complexity
summary: "An if, else-if or while condition of three or more operands joined by and/or/not, wrapping a line or holding an inline range check, whose purpose (end reached, input valid, entry repeated) is named nowhere in the code; the same compound condition in two places; an if-else-if chain whose arms do different work and can only be told apart by reading each test; an if/else on an unnamed compound test whose legs are inline formulas: name the parts with boolean variables, the whole with a boolean function, and the legs with functions."
tags: [rule, boolean-expressions, conditions, readability, extract-function, decompose-conditional]
paradigm: any
sources: [code-complete, fowler-refactoring]
created: 2026-11-06
updated: 2026-11-07
---

A compound condition is read in full by everyone who passes the `if`, whether they care about it or not. McConnell's repair is to give the condition, or its parts, a name: intermediate boolean variables for the parts, and a boolean function for the whole when the test repeats or distracts from the main line of the algorithm (*Code Complete*, section 12.5, pp. 292-293, and section 19.1, p. 427).

## Rule

**Boolean variables.** Assign the parts of a condition to boolean variables named for what they test: the test then documents itself and becomes simpler to read and to change (pp. 292-293). In the book's first example, `elementIndex < 0 || MAX_ELEMENTS < elementIndex || elementIndex == lastElementIndex` leaves unclear whether it checks completion, an error or something else; rewritten as `finished` and `repeatedEntry`, it says it checks two things (pp. 292-293). Its second example joins end-of-stream, an input-error flag, a line-count range and an error-processing call in one `If`. The book predicts that a reader will not try to understand it and will put it off, and warns that this is «это абсолютно то же самое, что сделают другие люди, читая ваш код» (p. 293). Section 19.1 repeats the advice: instead of monstrous conditions «с полудюжиной элементов», assign the parts to intermediate variables (p. 427).

**Boolean functions.** Where a test is repeated or pulls attention from the main flow, put it in a separate function and test the function's value (p. 427). The book's reason is that such a condition «выглядит ужасно, и вам приходится его читать, даже если оно вам неинтересно» (p. 427). Moving it into a function isolates it and lets the reader forget it until needed. McConnell extends the rule to a test made only once: «Если вы проверяете условие только раз, вам может показаться, что его не стоит помещать в отдельный метод» (p. 428), and answers that a well-named function improves readability, which is reason enough. He also argues that the function's name documents the purpose of the test in code, and that this beats a comment because code is more likely to be read and changed than a comment (p. 428). See [[comment-why-not-how]].

**Chains.** Chapter 15 applies the function form to `if`-`else if` chains: one reason such a chain is hard to read is that each test is itself complicated, and the repair is to replace each test with a call to a function that returns a boolean (p. 351). In the book's character-classification chain, the long comparison for punctuation and the ranges for letters become `IsPunctuation(c)` and `IsLetter(c)` (pp. 350-351). The checklist asks whether complex tests are turned into calls to boolean functions (p. 357), and a margin note names the well-named boolean variable as the other way (p. 354).

**Condition and legs.** Fowler's *Decompose Conditional* (*Refactoring*, 2nd ed., ch. 10, PDF pp. 290-292) carries the function form one step further: name not only the condition but each leg. Complex conditional logic is for him one of the most common sources of complexity, because "the code, both in the condition checks and in the actions, tells me what happens but can easily obscure why it happens" (p. 290). He replaces each chunk with a call to a function named after its intention, "for the conditional part and each of the alternatives", so that "I highlight the condition and make it clear what I'm branching on. I also highlight the reason for the branching." (p. 290). He calls it a particular case of Extract Function that has often given remarkably good value (p. 290). After extraction, a two-legged conditional that only chooses a value can become a ternary (p. 292).

Where a complex condition tests several variables, the book recommends a decision table over `if` or `case`: less control structure, fewer places for errors, and the table can change without the code (p. 428). [[drive-repeated-dispatch-from-a-table]] owns that shape.

## Sign in code

The thresholds below are this wiki's own; the book names only «полудюжиной элементов».

- An `if`, `else if`, `while` or ternary condition with three or more operands joined by `and`/`or`/`not`, or one that wraps onto a second line, or an inline range check (`MIN <= n and n <= MAX`) inside a larger condition, with no variable, function or comment naming what it tests.
- The same compound condition, or the same sub-expression of one, written out in two or more places (then the repair is a function).
- A condition mixing levels: a range check, an end-of-input check and a status flag in one expression, with no name for what they jointly mean.
- An `if`-`else if` chain whose arms do different work and can only be told apart by reading each condition in full (pp. 350-351).
- An `if`/`else` whose condition is such an unnamed compound test (two negated date comparisons that together mean "in summer") and whose legs are inline computations of the same kind of value with different formulas, nothing naming which is which (Fowler, p. 291).

This wiki assigns the neighbours as follows. This page owns a single compound condition, in an `if`, `else if` or `while`, whether the repair is a variable or a function. A range or format check on one domain value held as a primitive, written out again at two or more use sites, is [[replace-primitive-with-class]], whose type holds the check once; a compound condition over several values, or one not tied to a single domain value, is [[name-complex-conditions]]. An `if`-`else if` chain whose every arm only assigns a category from one input compared with literal lists or ranges is [[drive-repeated-dispatch-from-a-table]]. A chain whose arms do different work, or whose tests combine different inputs, is [[name-complex-conditions]], which names each test with a boolean function (pp. 350-351). Nested branches on state and then on event are [[finite-state-machine]]. A deep access chain inside an expression, with no compound condition, is [[explaining-variable]]; other unnamed fragments of a routine are [[extract-routine-to-name-a-step]]. How the new boolean is named is [[boolean-variable-names]]. Fowler's leg extraction belongs to [[name-complex-conditions]] when it accompanies naming the condition: the legs of an `if`/`else` whose condition is being named are extracted in the same pass; a leg that is long on its own, under a simple condition, is [[extract-routine-to-name-a-step]]. A run of separate checks with one shared result is [[consolidate-conditional-expression]], which hands its combined condition back to this page. A condition that is hard to read because of negations, not because of length, is [[prefer-positive-conditions]]'s shape. A condition whose spacing or missing parentheses suggest a precedence the language does not apply is [[layout-must-tell-the-same-story-as-the-logic]]; where both hold, apply this page first, since naming the parts often removes the negations.

## When not to apply

The book states no limits here. These are this wiki's own.

- The condition already reads as its meaning, such as `count > 0 and not closed` or `user.isActive() and order.isPaid()`. A name adds a hop and nothing else.
- Extracting into a function would need many arguments drawn from local state (the book's example already takes three). The book prefers a function even for a test made once (p. 428). This wiki keeps a local variable instead where the test needs locals that would become many parameters, and otherwise follows the book.
- The parts depend on short-circuit order to be safe (see [[guard-before-the-guarded-operand]]). Precomputing every part into a variable evaluates them all; keep the guard in the expression, nest the test, or use a function.
- A part calls something with side effects or a costly call. Moving it into an eagerly computed variable changes behaviour or cost, and naming it hides the effect behind what looks like a pure test. The book's own example calls `ErrorProcessing()` inside the condition, which this wiki reads as a query that must stay side-effect free ([[command-query-separation]]).
- A name that does not match the test (it says `isValid` but checks only one field) is worse than the raw expression, because the reader trusts the name.
- Fowler states no limits for *Decompose Conditional*. This wiki adds: a leg that is one short expression whose meaning is plain from its operands gains little from a function; extracting the legs is worth it where they read as formulas a reader must decode.
- Cost when followed: more local names. The page fires on unclear conditions, not on every `and`.

## Repair

1. Find the groups of operands that mean one thing together (all data read, line count in range).
2. Assign each group to a boolean variable named for that meaning in the problem (`allDataRead`, not `cond1`).
3. Keep guarded or side-effecting clauses inline, after the variables they depend on.
4. If the whole test recurs or interrupts the main flow, move it, with its variables, into a function whose name states what is being checked, and call it in the condition. In an `if`-`else if` chain, do this for each arm's test.
5. If several such conditions select among categories, consider a table instead ([[drive-repeated-dispatch-from-a-table]]).
6. For an `if`/`else` whose legs are formulas, extract the `then` leg and the `else` leg into functions named for what each produces, testing after each; if the conditional now only selects between two values, consider a conditional expression (Fowler, pp. 290-292).

## Before and after

Variables, on the book's chapter 12 example:

```
if (index < 0 or MAX_ELEMENTS < index or index == last_index)
  stop()
```

```
finished = index < 0 or MAX_ELEMENTS < index
repeated_entry = index == last_index
if finished or repeated_entry
  stop()
```

A function, when the test interrupts the main flow:

```
if stream.atEnd and not inputError
   and MIN_LINES <= lineCount and lineCount <= MAX_LINES
   and not processingFailed:
    process(document)
```

```
function documentIsValid(stream, lineCount, inputError, processingFailed):
    allDataRead    = stream.atEnd and not inputError
    legalLineCount = MIN_LINES <= lineCount and lineCount <= MAX_LINES
    return allDataRead and legalLineCount and not processingFailed

if documentIsValid(stream, lineCount, inputError, processingFailed):
    process(document)
```

Functions in a chain whose arms do different work:

```
if c < SPACE:
    handleControl(c)
else if c == ' ' or c == ',' or c == '.' or c == '!' or c == '(' or c == ')'
        or c == ':' or c == ';' or c == '?':
    appendPunctuation(c)
else if ('a' <= c and c <= 'z') or ('A' <= c and c <= 'Z'):
    appendLetter(c)
else:
    internalError("unexpected character type")
```

```
if isControl(c):          handleControl(c)
else if isPunctuation(c): appendPunctuation(c)
else if isLetter(c):      appendLetter(c)
else:                     internalError("unexpected character type")
```

Condition and both legs, after Fowler's example:

```
if not date.isBefore(plan.summerStart) and not date.isAfter(plan.summerEnd) then
    charge = quantity * plan.summerRate
else
    charge = quantity * plan.regularRate + plan.regularServiceCharge
```

```
charge = if isSummer(date) then summerCharge(quantity) else regularCharge(quantity)

function isSummer(date)
    return plan.summerStart <= date and date <= plan.summerEnd
function summerCharge(quantity)
    return quantity * plan.summerRate
function regularCharge(quantity)
    return quantity * plan.regularRate + plan.regularServiceCharge
```

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition: section 12.5, pp. 292-293 (booleans to document and to simplify a test, both examples); section 15.1, pp. 350-351 (boolean functions in an `if`-`else if` chain), the margin note on p. 354 and the checklist on p. 357; section 19.1, pp. 427-428 (variables, functions, the once-only case, the name as documentation, decision tables); section 24.3, p. 560, where decomposing a boolean expression into named variables and moving it into a named boolean function, which also ends parallel edits of a repeated expression, recur as refactorings. The rule, the reasons, the once-only case and the decision-table advice are the book's. The numeric thresholds in the signs, the split with neighbouring pages (including the per-setting split of chains with [[drive-repeated-dispatch-from-a-table]]), all limits (including the resolution of the once-only case against many parameters), the repair order and the pseudocode are this wiki's own; the examples follow the shape of the book's `finished`/`repeatedEntry`, `DocumentIsValid` and character-classification examples, with the chain's arms changed to do different work. The quotation of p. 293 is transcribed from `raw/` and needs the page-image check. This page absorbed the former page on naming parts of a condition with boolean variables. Related: [[order-comparisons-along-the-number-line]].

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 10, *Decompose Conditional*, PDF pp. 290-292: the motivation, the extraction of the condition and both legs, and the final ternary. The pseudocode follows the book's example in this wiki's notation. The leg sign as worded, the short-leg limit, the positive form of `isSummer` in the "after" (the book keeps the negations) and the assignment of leg extraction against [[extract-routine-to-name-a-step]] and [[consolidate-conditional-expression]] are this wiki's own.
