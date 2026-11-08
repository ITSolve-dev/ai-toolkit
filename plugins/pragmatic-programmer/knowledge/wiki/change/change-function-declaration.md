---
title: Change Function Declaration
category: change
summary: "Procedure for renaming a function or changing its parameters: edit the declaration and every caller at once only when callers are few or a tool does it reliably; otherwise (many or hard-to-reach callers, a polymorphic method, a name that is not unique, a published API) extract the body into a new function, inline the old one caller by caller, then rename; for a published API, stop after extracting and deprecate the old function."
tags: [method, refactoring, change-signature, rename, parameters]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

**Change Function Declaration** (also Rename Function and Change Signature; formerly Rename Method, Add Parameter, Remove Parameter) changes a function's name or its parameter list. Fowler calls declarations the "joints in our software systems" (*Refactoring*, 2nd ed., ch. 6, PDF p. 142), and this is the refactoring with which they are reshaped as understanding improves. Unusually, he gives two sets of mechanics and a test for choosing between them.

## Why change the joint

- **The name.** "If I see a function with the wrong name, it is imperative that I change it as soon as I understand what a better name could be" (PDF p. 142). Left alone, the wrong name has to be decoded again at every later reading. One technique he gives: write a comment describing the function's purpose, then turn the comment into the name (PDF p. 142). What makes a name wrong is [[routine-names]] and [[rename-when-meaning-drifts]].
- **The parameters.** They set the contexts in which the function can be used and how coupled it is. Whether to take an object or one of its values is [[pass-what-the-routine-uses]]. A parameter the body never reads is [[remove-unused-parameters]].

## Choosing the mechanics

Fowler asks whether the declaration and all its callers can easily be changed in one go (PDF p. 143).

- **Simple mechanics** fit when callers are few, or an automated refactoring tool does the rename reliably. Static typing and a good IDE make that safe ([[automated-refactoring]]). Without static typing, text search "will then have a lot of false positives" (PDF p. 145).
- **Migration mechanics** fit when there are many callers, the callers are hard to reach, the method is polymorphic, the change is complicated, the name is not unique (Fowler's `changeAddress` exists on both a person and an insurance agreement), or the function is a published API used by code that cannot be changed (PDF pp. 143-145).
- If the simple mechanics go wrong, revert to the last good state and redo the change with the migration mechanics (PDF p. 145).

This wiki groups these criteria into one list; the book gives them across the motivation and the mechanics.

This wiki assigns the neighbouring procedures as follows. Renaming or re-parameterising a function whose callers can all be edited in this change is [[change-function-declaration]]; a change some of whose users lie outside this change (a published interface, stored data, a library used throughout) is [[parallel-change]]; a changed value that callers inspect, such as a sentinel they compare to, is [[extract-before-changing-many-callers]]; renaming a record field or a class's accessor pair is [[rename-widely-used-field]].

## Simple mechanics

1. When removing a parameter, check the body does not reference it.
2. Change the declaration.
3. Update every reference.
4. Test.

Keep changes separate: rename and test, then add the parameter and test again (PDF pp. 143-145).

## Migration mechanics

1. If needed, refactor the body so the next step is easy, for example Extract Variable on the value that will become the new parameter ([[extract-variable]]).
2. Extract the whole body into a new function ([[extract-function]]). If it will eventually take the old name, give it a temporary name that is easy to search for.
3. Add any new parameters to the new function using the simple mechanics. Test.
4. Inline the old function into its callers, one at a time, testing after each ([[inline-function]]).
5. Rename the new function to the final name. Test.

A polymorphic method needs a forwarding method for each binding: on the superclass where there is one hierarchy, on each implementing class where there is none (PDF p. 144).

For a **published API**, stop after step 2 and deprecate the old function, which becomes a pass-through; remove it only when, and if, every client has moved: "Even if I’m never able to reach the happy point of deleting circum, at least I have a better name for new code" (PDF p. 146). That general shape, including stored fields and libraries, is [[parallel-change]].

Adding a parameter in JavaScript, Fowler first puts an assertion in the new function that the parameter is supplied, so a caller converted without it fails at once (Introduce Assertion, PDF p. 147; see [[assert-the-impossible]]). This wiki extends that to any dynamically typed language.

Automated tools make the migration mechanics needed less often; where a tool cannot do the whole change, it still speeds up the two key moves, extract and inline (PDF p. 150).

## Example: a parameter narrowed to one of its properties

```
function inNewEngland(customer)
    return NEW_ENGLAND_STATES.contains(customer.address.state)

caller: customers.filter(c -> inNewEngland(c))
```

Steps: extract `stateCode = customer.address.state` as a variable; extract the body as `tmpInNewEngland(stateCode)`; inline the variable; inline the old function into each caller; rename `tmpInNewEngland` back to `inNewEngland`.

```
function inNewEngland(stateCode)
    return NEW_ENGLAND_STATES.contains(stateCode)

caller: customers.filter(c -> inNewEngland(c.address.state))
```

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 6, "Change Function Declaration", PDF pp. 141-150: the joints metaphor, the rename imperative and the comment technique, the choice between two mechanics and its criteria, both sets of mechanics, polymorphism, the published-API pause, the assertion and the note on tools. This wiki's own: the extension of the assertion to any dynamically typed language, the selecting sentence against [[parallel-change]], [[extract-before-changing-many-callers]] and [[rename-widely-used-field]], the grouping of the criteria into one list, the links to the pages that judge names and parameters, and the pseudocode.
