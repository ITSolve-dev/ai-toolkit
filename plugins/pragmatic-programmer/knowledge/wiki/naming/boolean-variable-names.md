---
title: Boolean names imply true/false and are stated positively
category: naming
summary: "A boolean named for a thing or dimension (status, state, sourceFile, mode) where true has no clear meaning; a vague success/ok where one specific outcome is meant; or a negated name (notFound, notDone) that ends up under another negation."
tags: [rule, naming, booleans]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell gives three rules for naming booleans and a set of typical names (*Code Complete*, Russian edition, pp. 261–262).

## Rule

- **The name implies true or false.** `done` and `success` work because something is either done or not, and an operation either succeeds or fails. `status` and `sourceFile` do not. McConnell asks what `status == true` could mean: everything has a status (p. 261). He renames them `error` or `statusOK`, and `sourceFileAvailable` or `sourceFileFound` (p. 261).
- **Typical names have one meaning each.** `done` is false before an action and true after it. `error` is false when all is well. `found` is false until a value is found. `success`/`ok` is true when an operation succeeded. He adds that `success` should be made more specific where possible: `processingComplete` when success means processing finished, `found` when it means a value was located (p. 261).
- **Positive, not negated.** Names such as `notFound`, `notDone` and `notSuccessful` become hard to read once negated (`if not notFound`). Use `found`, `done` or `processingComplete` and negate them where needed (p. 262).

**The is- prefix is a trade-off.** Prefixing `is` turns the name into a question whose answer is the value, and it rules out empty names, since `isStatus` makes no sense. McConnell counts against it that it makes conditions harder to read: «условие if ( isFound ) менее понятно, чем if ( found )» (p. 261). The book leaves the choice open.

## Sign in code

- A boolean (by type, or by being assigned only true/false) named for a thing or a dimension rather than a condition: `status`, `state`, `file`, `mode`, `check`.
- A boolean named with `not`/`no`/`dis-` that appears under a negation operator anywhere (`!notFound`, `not isNotValid`).
- `success` or `ok` where the code means one specific thing (finished, found, valid).

This wiki assigns the neighbouring cases as follows. This page owns the name of a boolean variable or field. A boolean method's name (`isX`, `exists`) is [[builder-and-manipulator-names]]. A name containing `flag` is [[status-variable-not-flag]]. A status boolean tested directly by functions outside its owner, where the question is whether it should stay a boolean at all, is [[status-variable-as-enumeration]].

## When not to apply

- Where the project's language or convention requires a prefix for boolean properties (`is`/`has` accessors), follow it. The rule still requires that the rest of the name state a condition. This wiki's reading of the book's open trade-off.
- A negative name that is never negated, and whose negative is the natural concept (`disabled` in a configuration file whose default is enabled), may stay. This wiki's limit; the book's argument is about double negation.

## Repair

Rename the boolean to the condition that holds when it is true (`sourceFileFound`, `statusOK`). Flip a negated name to its positive form, invert its assignments, and remove the now-doubled negation at each use. Where it means a specific kind of success, name that kind.

## Before and after

```
notFound = true
for each item in items
    if item.id == wanted
        notFound = false
if not notFound
    use(wanted)
```

```
found = false
for each item in items
    if item.id == wanted
        found = true
if found
    use(wanted)
```

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 11.2, pp. 261–262 ([[code-complete]]): typical boolean names, names implying true/false, the is- prefix trade-off, and positive names. The signs as worded, the assignment against the neighbouring pages and the limits for prefix conventions and never-negated negatives are this wiki's own. The pseudocode is this wiki's own.
