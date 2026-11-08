---
title: Renaming a widely used field in small steps
category: change
summary: "Procedure for renaming a record field or a class's accessor pair used across a program without one big-bang edit: encapsulate, rename the private field, accept both names in the constructor, migrate callers, rename the accessors."
tags: [method, rename, small-steps, encapsulation, refactoring]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

**Rename Field** is Fowler's procedure for changing the name of a field in a record structure, or of a class's getter and setter, which "form an effective field for users of the class" (*Refactoring*, 2nd ed., ch. 9, PDF p. 273).

## Why it matters

Fowler grounds it in Brooks: "Show me your tables, and I won't usually need your flowcharts; they'll be obvious" (PDF p. 273). Data structures are the key to understanding, and understanding of the data improves as one works, so "it's vital that this improved understanding is embedded into the program" (p. 273). Whether a name needs changing belongs to [[rename-when-meaning-drifts]] and [[self-describing-field-names]]; this page is the safe way to carry it out.

## Procedure

1. **Limited scope?** If the record is used locally, as in one function, rename all accesses in one go and test; skip the rest (PDF pp. 273, 276).
2. Otherwise apply Fowler's Encapsulate Record, if the record is not a class with accessors already (PDF p. 273). This wiki has no page for it; [[encapsulate-variable]] is the nearest procedure.
3. Rename the private field; keep the old accessor names reading and writing it. Test.
4. Let the constructor accept both the old and the new key, the new one taking precedence (`title = data.title if present else data.name`). Migrate constructor callers one by one, then drop the old key (the book's example, PDF p. 275).
5. Rename the accessors ([[change-function-declaration]]).

Encapsulating first turns one change into four independent places (getter, setter, constructor, internal field), and Fowler argues this is less work, not more: "Smaller steps mean fewer things to go wrong in each step—therefore, less work" (PDF p. 274). Where the callers cannot all be migrated in one change, steps 4 and 5 are a [[parallel-change]]; this link is this wiki's own.

This wiki assigns the neighbouring procedures as follows. Renaming or re-parameterising a function whose callers can all be edited in this change is [[change-function-declaration]]; a change some of whose users lie outside this change (a published interface, stored data, a library used throughout) is [[parallel-change]]; a changed value that callers inspect, such as a sentinel they compare to, is [[extract-before-changing-many-callers]]; renaming a record field or a class's accessor pair is [[rename-widely-used-field]].

## Choosing the weight

- Fowler: "if my tests break, that's a sign I need to use the more gradual procedure" (PDF p. 276).
- With an immutable data structure, skip encapsulation: copy the value under the new name, move users over gradually, remove the old name. With mutable data the same copy is "a recipe for disaster", because the two names can diverge (p. 276).

## Example

```
// step 3: private field renamed, public name unchanged
class Organization
  constructor(data) -> this.title = data.name
  name()            -> return this.title

// step 4: both keys accepted while callers migrate
  constructor(data) -> this.title = data.title if defined else data.name

// step 5: accessors renamed after all callers use the new key
  constructor(data) -> this.title = data.title
  title()           -> return this.title
```

## Source

Fowler, *Refactoring*, 2nd ed., ch. 9, Rename Field, PDF pp. 272-276 ([[fowler-refactoring]]). The procedure, the Brooks citation, the limited-scope shortcut, the small-steps argument, the tests-break test and the immutable copy variant are the book's. The pointers to neighbouring pages, the selecting sentence, the link to parallel change, the reason that the mutable copy fails (the two names diverging) and the pseudocode are this wiki's own.

Related: [[small-steps-with-feedback]], [[refactor-in-small-tested-steps]].
