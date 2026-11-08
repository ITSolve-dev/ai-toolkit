---
title: Do not accept NULL as an argument
category: errors
summary: "A method branches on `param == null` to pick a behaviour (\"if mask is null, return all files\"), or its contract documents null as a meaningful value of a parameter."
tags: [rule, null, contracts, null-object]
paradigm: oop
sources: [elegant-objects]
created: 2026-11-03
updated: 2026-11-03
---

A method that treats a null argument as "no value, so do the default" has to compare the argument with null before it can use it. Bugayenko holds that this comparison takes responsibility away from the object: instead of asking the argument to act, the method asks whether the argument is worth talking to, and the argument becomes a passive data structure. His verdict in section 3.3 is absolute: «никогда не принимайте NULL в качестве аргумента метода. Никаких исключений.» (p. 153). Null as a return value is treated in section 4.1 of the book; see [[never-return-null]].

## Rule

A method never gives null a meaning. Where a caller has "nothing" to pass, it passes an object that stands for nothing: a **null object** that implements the same interface and behaves as the empty case. The book's example is a `Mask` interface with `matches(file)` and an `AnyFile` mask whose `matches` always returns true (p. 151). The method `find(mask)` then has one path, `mask.matches(file)`, and does not know it was given the edge case (p. 152).

The book rejects the convenience argument for null. Allowing null in three optional parameters looks cheaper than writing many methods (the book counts nine), but it contradicts the principle that every object is fully responsible for its own behaviour (p. 147).

## Sign in code

- A branch on a parameter compared with null that selects a behaviour, not one that rejects the value: `if (mask == null) { all files } else { filtered }`.
- A doc comment or contract line of the form "if X is null, ..." describing a valid use.
- A primitive or string parameter whose absence is encoded as null where a typed object with an empty case would do (the book moves from `find(String mask)` to `find(Mask mask)`, p. 148).

A guard that throws on null is not this sign; it is the defensive variant discussed under Repair.

This wiki assigns the neighbouring cases as follows. This page owns null passed in as a parameter with a meaning. A field initialised to null and filled later is [[null-field-hides-another-class]]. Null or a sentinel returned from a method is [[never-return-null]]. Which form of absence to use instead is decided on [[null-object-or-optional]].

## When not to apply

- At a boundary that receives values the program does not control (parsed input, deserialized data, a foreign library that returns null). There null is a fact about the input, not a design choice, and it is converted once at the boundary into a null object, an absent-value type or an error. This limit is this wiki's own.
- This wiki's own limit, where the book says «Никаких исключений» (p. 153): the interface has no behaviour that makes sense for "nothing". A null object must act; if none of its methods used by the code at hand has an honest answer (each throws or returns an invented value), the absence belongs to the caller's decision, see [[null-object-or-optional]].
- Where the project's language or conventions give absence a checked type (an option type, a nullable type the compiler tracks), the project's convention decides how absence is expressed; this wiki reads the rule as still forbidding an unchecked meaning for it.

## Repair

1. Replace the primitive or nullable parameter with an interface that names what the method needs from it (`Mask.matches`).
2. Write the empty case as a class of that interface (`AnyFile`), so the edge case lives in one place.
3. Remove the null branch from the method; let it talk only to the interface.
4. Callers that passed null now pass the null object.

If a caller still passes null despite the contract, the book names two reactions: a **defensive** one, which checks and throws `IllegalArgumentException`, and an **ignoring** one, which does nothing and lets the first dereference fail. Bugayenko prefers ignoring: «Не засоряйте код лишними проверками.» (p. 152), reasoning that in well-designed code null references should not exist at all.

This wiki resolves that choice against [[crash-early]] per setting, and the resolution is its own: ignoring is safe when the argument is used at once, inside the method, so the failure appears at the call that caused it. When the argument is stored (a constructor field, a queue, a cache) and used later or on another thread, the eventual failure surfaces far from its cause, and a guard at entry is the fail-fast choice. Inputs from outside the program are always checked, per [[distrust-external-input]].

## Before and after

Before:

```
function find(mask: String or null): list of File
    result = []
    for file in allFiles()
        if mask == null
            result.add(file)
        else if globMatches(mask, file.name)
            result.add(file)
    return result

find(null)        // means "all files"
```

After:

```
interface Mask
    matches(file): Boolean

class Glob implements Mask
    pattern: String
    matches(file) = globMatches(pattern, file.name)

class AnyFile implements Mask
    matches(file) = true

function find(mask: Mask): list of File
    result = []
    for file in allFiles()
        if mask.matches(file)
            result.add(file)
    return result

find(new AnyFile())
```

The after holds no null comparison, and `AnyFile` has a meaningful behaviour, so it falls inside this page's limits.

## Discussion recorded in the book

- Kevin Rutherford, speaking of a function that returns NULL, argues that null creates coupling: every frame up the stack must share the convention about what null means and when it is returned, and each check adds a branch to test and read (p. 153).
- Madmenyo objects that null objects only replace null checks with `isNobody()` calls or try/catch. Bugayenko answers that null checks clutter the code because they are semantically foreign to the rest of the program, while those alternatives stay closer to the problem domain (pp. 153-155). He also disowns `isNobody`: «не думаю, что я предлагал такое» (p. 154). This wiki reads the objection as a real limit: a null object that callers must test with `isNobody()` has reintroduced the sign under another name.
- Martin defends `Optional`; the dispute is resolved on [[null-object-or-optional]].

## Source

Bugayenko, *Elegant Objects*, Java Edition, Russian translation (Piter, 2018), section 3.3, pp. 147-157; see [[elegant-objects]]. The quotations from pp. 152-153 were checked against the page image; the one from p. 154 is transcribed from OCR and must be checked against it. This wiki's own: the sign list beyond the `mask == null` example, the assignment of neighbouring cases, the boundary limit, the limit for an interface with no behaviour for "nothing", the language-convention limit, the reading of Madmenyo's objection and the stored-argument resolution with [[crash-early]]. Related: [[tell-dont-ask]], [[caller-owns-the-precondition]], [[design-by-contract]].
