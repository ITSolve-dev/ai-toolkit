---
title: "Preparatory refactoring: refactor first, then add the feature"
category: change
summary: "A diff adds a feature or fix by copying an existing function and changing only its literal values, its output format or one step (statement copied to htmlStatement), by wrapping a condition around every line that builds output, or by fixing one of several copies; restructure first so the change lands in one place."
tags: [rule, refactoring, preparatory-refactoring, duplication, parameterize-function]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Preparatory refactoring restructures code just before a change so that the change itself becomes simple. Fowler opens *Refactoring* with it. Faced with a working function that prints a bill, he asks what is wrong with code that works, and answers that structure matters because a person changes the code: a poorly designed system is hard to change because it is hard to see what to change and how the change interacts with what is there, and that is where bugs come from (ch. 1, PDF p. 8). His tip: "When you have to add a feature to a program but the code is not structured in a convenient way, first refactor the program to make it easy to add the feature, then add the feature." (PDF p. 8). In chapter 2 he calls this the best time to refactor (PDF p. 62) and quotes Kent Beck: "for each desired change, make the change easy (warning: this may be hard), then make the easy change" (PDF p. 64).

The refactoring and the feature stay separate steps; mixing them in one step is [[do-not-refactor-while-adding-features]]. This wiki assigns the neighbouring cases as follows. Two copies already standing in code are [[dry]]; a copy a diff adds as the route for a feature or fix, beside the function it copies, is [[preparatory-refactoring]]. Another page's finding left standing on lines a change touches is ruled on [[refactor-early-and-often]].

## Rule

When the requested change does not fit the current structure, first refactor (behaviour unchanged, tests green) until the change has one natural place to go, then make the change.

Fowler's chapter 2 example: a function does almost everything the feature needs but has literal values that conflict with it. Copying the function and changing the values leads to duplicated code that must later be changed in both places (and, worse, found), and does not help the next variation. With the refactoring hat on he applies Parameterize Function, after which the feature is a call with the right parameters (PDF p. 62).

The same applies to bug fixes: once the cause is found, unifying the three copies that caused the error, or separating update logic from queries, makes the fix easier and raises the chance the bug "will stay fixed" (PDF p. 62).

## Sign in code

The sign is relational: it needs the change in hand, so this page fires on a diff or a planned change, not on code standing still. Fowler's chapter 1 example names two shapes (PDF pp. 8-9) and chapter 2 a third and a fourth (PDF p. 62):

- A function added as a copy of an existing one that differs only in how it emits results (`statement` copied to `htmlStatement`), so the calculation logic now exists twice.
- A condition on the new variant wrapped around every statement that appends to the result inside one long function.
- A function added as a copy of an existing one that differs only in literal values, or in one inserted step.
- A bug fix applied to one of several copies of the same logic, the others left as they were.

The wording of the signs as diff shapes is this wiki's generalisation of the book's cases. Fowler's other bug-fix case, separating update logic from queries, has its sign on another page: A bug fix applied to one of several copies of the same logic is [[preparatory-refactoring]]; a function that both updates state and returns a value is [[command-query-separation]], whatever fix lands in it.

## Rule of three versus preparatory parameterization

Fowler also gives Don Roberts' rule of three: the first time, just do it; the second time, "you wince at the duplication, but you do the duplicate thing anyway"; the third time, refactor (PDF p. 62). Read literally, that tolerates the very copy his preparatory example rejects. This wiki resolves it per setting. Where the second case is a copy of an existing function differing only in values or in output, and the variation can be named as a parameter or a separate renderer, refactor now: the abstraction is already visible and costs one refactoring. Where the second case is merely something similar whose common shape is not yet clear, the rule of three holds and the duplication is tolerated until a third case shows the shape. Telling real duplication from a chance likeness is [[coincidental-duplication]].

## When not to apply

- The code works and nobody needs to change or understand it. Fowler: "If the code works and doesn’t ever need to change, it’s perfectly fine to leave it alone." (PDF p. 9).
- The program will never change again. Fowler calls copy-and-paste fine for such a program and a menace only in a long-lived one (PDF p. 9).
- The needed refactoring is large and the feature is small. Fowler sometimes adds the feature and leaves the larger refactoring, calling it a judgement call he cannot quantify (PDF p. 68). The same holds where the code is rarely touched, or where it is not yet clear what improvement to make (PDF p. 68).
- There are no tests around the code to be restructured; build them first ([[self-testing-code]], [[test-early-often-automatically]]).

Size alone is not a limit. Fowler calls the starting function tolerable to read as it is (PDF p. 8), yet refactors that same short function before the HTML change (pp. 8-9), because the change, not the length, drives the refactoring.

## Repair

1. Revert or set aside the copy.
2. Pin current behaviour with self-checking tests.
3. Separate the parts the feature will vary (literal values, output format, per-case calculation) from the parts it shares: Parameterize Function for values; [[extract-function]], [[replace-temp-with-query]], [[remove-loop-accumulator]] and [[split-phase]] for calculation against output; each in [[refactor-in-small-tested-steps]]. Commit the refactoring on its own.
4. Add the feature or fix as a call to, or a new piece beside, the one shared place.

## Before and after

```
// before: the feature arrives as a copy with one literal changed
function tenPercentRaise(person):
    person.salary = person.salary * 1.10

function fivePercentRaise(person):          // new, copied
    person.salary = person.salary * 1.05
```

```
// after: refactor first, then the feature is a call
function raise(person, factor):
    person.salary = person.salary * (1 + factor)

raise(person, 0.05)
```

The output-format case, as in Fowler's chapter 1:

```
// before: HTML requested; the plan is to copy
function statement(invoice):
    total = 0
    text = "Statement for " + invoice.customer
    for perf in invoice.performances:
        amount = <price rules by play type>
        text += line(perf, amount)
        total += amount
    return text + footer(total)

function htmlStatement(invoice):   // same price rules, pasted
    ...
```

```
// after: refactor first, then add the HTML renderer
function amountFor(perf):  <price rules by play type>
function totalAmount(invoice): sum of amountFor over performances

function statement(invoice):     render text using amountFor, totalAmount
function htmlStatement(invoice): render html using amountFor, totalAmount
```

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 1, "Comments on the Starting Program", PDF pp. 8-9: the tip, the reasoning from change, the two chapter 1 cases and the limits on code that never changes. Ch. 2, "The Rule of Three" and "Preparatory Refactoring" (PDF p. 62), the Kent Beck quotation (p. 64), "Slowing Down New Features" (p. 68): the parameterization example, the bug-fix case and the judgement-call limits. This wiki's own: the signs as diff shapes and the note that the sign needs a change in hand, the resolution between the rule of three and preparatory refactoring, the selecting sentences against [[dry]], [[refactor-early-and-often]] and [[command-query-separation]], and the pseudocode; the raise example echoes the shape of Parameterize Function, not a listing from the book.
