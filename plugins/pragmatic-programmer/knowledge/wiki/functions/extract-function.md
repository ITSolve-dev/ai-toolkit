---
title: "Extract Function: the mechanics"
category: functions
summary: "Procedure for moving a fragment of a long function into its own function without breaking it: name it for what it does, sort the fragment's locals into read-only (parameters, including a structure mutated in place), one modified (return it, initialise it inside), and accumulators (shadow and return); abandon or simplify first when many locals are assigned or several values must come out; extract to sibling level when the function will move elsewhere."
tags: [method, refactoring, extract-function, local-variables, comments]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Extract Function is the refactoring Fowler reaches for first in his example. When he decides what a fragment does (the `switch` in `statement` computes the charge for one performance), he treats that conclusion as insight that must leave his head: quoting Ward Cunningham, the understanding is "in my head—a notoriously volatile form of storage", so he moves it into code as a function named after what it does, `amountFor(aPerformance)` (ch. 1, PDF p. 11).

When a fragment deserves its own routine is [[extract-routine-to-name-a-step]], which owns the sign and carries Fowler's intention-versus-implementation test from the catalogue entry (ch. 6, PDF p. 122); this page is the procedure that carries out the extraction. Its inverse, putting a body back into its callers, is [[inline-function]].

## Procedure

1. **Find the seam.** In a long function, look for points that separate different parts of the behaviour; Fowler's first candidate is the `switch` in the middle of the loop (PDF p. 10).
2. **List the locals that leave scope.** Look in the fragment for every variable that will no longer be in scope once the code is moved (PDF p. 11).
3. **Read-only locals become parameters.** Variables the fragment uses but does not modify are passed in (PDF p. 12).
4. **One modified local becomes the return value.** Fowler notes that modified variables need more care; with only one, return it, and move its initialisation inside the new function (PDF p. 12).
5. **An accumulator gets a shadow.** A variable added to on every loop pass (`volumeCredits`) is initialised as a fresh local inside the new function and returned; the caller adds the result (PDF p. 21). Removing the accumulator altogether is [[remove-loop-accumulator]].
6. **Replace the fragment with a call**, then compile, test and commit ([[refactor-in-small-tested-steps]]).
7. **Tidy the new function.** Rename its locals and parameters for their new role ([[rename-extracted-code-for-clarity]]).
8. **Delete comments the name now says.** After extracting `volumeCreditsFor`, Fowler removes the comment "add volume credits" as "unnecessary (and, in this case, downright misleading)" (PDF p. 22). See [[comment-why-not-how]].

The catalogue entry (ch. 6, "Extract Function", PDF pp. 123-131) adds to these steps:

- **Name it by what it does, not how.** Create the new function under that name before copying anything (PDF p. 123).
- **A structure modified in place** (a record or collection the fragment updates) is still passed as a parameter and mutated (PDF p. 128).
- **A local declared outside but used only inside** the fragment moves into it; slide the declaration next to its use first if it is far away (PDF pp. 124, 128).
- **An assignment to a parameter** is split into a temp first, with Split Variable ([[do-not-reuse-parameters-as-working-variables]]) (PDF p. 128).
- **Compile**, where the language checks anything at compile time, to catch locals that were missed (PDF p. 124).
- **Point other copies at it.** Look for code elsewhere that does the same thing and replace it with a call, Replace Inline Code with Function Call (PDF p. 124).
- **Too many locals assigned** inside the fragment: Fowler abandons the extraction, simplifies the variables with Split Variable or Replace Temp with Query, and comes back (PDF p. 124).
- **More than one value would come out:** he prefers a different fragment, or splitting it so that each function returns one value; a returned record is the fallback (PDF p. 131).

After the call is in place he renames the returned temp `result` inside the new function and makes the caller's variable immutable (PDF p. 131). The book presents that as his style, not as part of the method.

The fewer locals the fragment touches, the easier steps 2-5 are. Fowler therefore removes temporaries before extracting ([[replace-temp-with-query]]): "usually I’ll take out local variables before I do any extractions" (PDF p. 19).

In languages that allow nested functions, Fowler extracts into a function nested in the original in chapter 1, so data in the enclosing scope need not be passed (PDF p. 13), and the catalogue mechanics nest where the language allows (PDF p. 123). For a function he expects to move to another context, he qualifies this: a nested function avoids the variable problems only until it is moved, so he extracts "to at least the sibling level of the source function first, so I can immediately tell if the extracted code makes sense" (PDF p. 131). This wiki treats nesting as a language setting.

This wiki notes where the procedure stops: if steps 3-5 leave the new function needing many of the routine's locals, the limit on [[extract-routine-to-name-a-step]] applies and the extraction trades a long block for a long parameter list ([[limit-parameter-count]]). Where extracting a fragment would need most of the routine's locals as parameters or results, the temps are removed first ([[replace-temp-with-query]]); where they still tangle, [[function-or-command-object]] owns the choice of a command object; where the routine is to stay whole, the intent comment is split into finer steps ([[extract-routine-to-name-a-step]]).

## Example

```
// before
function statement(invoice):
    for perf in invoice.performances:
        play = plays[perf.playID]
        thisAmount = 0
        switch play.type:
            "tragedy": thisAmount = 40000; if perf.audience > 30: thisAmount += 1000 * (perf.audience - 30)
            "comedy":  ...
        total += thisAmount
```

```
// after: perf and play are read-only -> parameters; thisAmount is the one modified -> returned
function amountFor(perf, play):
    result = 0
    switch play.type: ...
    return result

function statement(invoice):
    for perf in invoice.performances:
        play = plays[perf.playID]
        total += amountFor(perf, play)
```

A trial extraction that does not help is inlined again, and Fowler counts it as no loss: "As long as I’ve learned something, my time wasn’t wasted" (PDF p. 123).

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 6, "Extract Function", PDF pp. 121-131: naming by what, the variable cases (structure mutated in place, declaration moved in, parameter assignment), compile, Replace Inline Code with Function Call, abandoning on many assigned locals, one value per function, the sibling level, `result` and the extract-and-inline-back remark. Ch. 1, "Decomposing the statement Function" and "Removing Volume Credits", PDF pp. 10-14, 19, 21-22; the catalogue entry is Extract Function (106). The steps are the book's as used in the example. This wiki's own: the numbering into one procedure, the treatment of nested functions as a language setting, the stopping point against [[limit-parameter-count]], and the pseudocode.
