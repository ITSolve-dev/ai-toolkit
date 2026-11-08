---
title: Divergent change and shotgun surgery
category: structure
summary: "Concept: two opposite failures of 'one change, one place' after Fowler: one class serving two unrelated concerns (tax rules beside line formatting), or one concern spread as small fragments across many classes; names the code-visible shapes, routes them to their owners, and holds Fowler's repairs for each."
tags: [concept, cohesion, coupling, divergent-change, shotgun-surgery, change]
paradigm: any
sources: [fowler-refactoring]
created: 2026-11-07
updated: 2026-11-07
---

Fowler names two "closely related pungencies" that both defeat the goal of making each change at "a single clear point in the system" (ch. 3, Divergent Change, PDF p. 90). They are opposites:

- **Divergent change**: "one module is often changed in different ways for different reasons" (PDF p. 90). His example is a module where three functions change for each new database and four for each new financial instrument.
- **Shotgun surgery**: "every time you make a change, you have to make a lot of little edits to a lot of different classes" (Shotgun Surgery, PDF p. 91). The edits are hard to find, and it is easy to miss one.

## From history to a sign

Fowler states both in terms of how the code changes over time. Under this wiki's charter a change history is not a sign, so this wiki names what can be seen in the code itself, and routes each shape to its owner:

- **Divergent change**: one class whose methods fall into groups that use disjoint fields or vocabularies (one group computes tax from rate tables, another formats lines for a locale). The owner is [[class-interface-coherent-abstraction]], whose sign is groups of methods each touching a disjoint half of the fields. Single functions that interleave the two concerns are [[routine-cohesion]].
- **Shotgun surgery**: the same concept, such as a status value, a format or a rule constant, handled by small fragments in many classes. The repeated test of one fact is [[dry]]. A representation decision visible at many use sites is [[hide-secrets-behind-one-access-point]]. Where only the change log shows the parallel edits, the warning sign is listed on [[coupling]] and in [[refactoring-warning-signs]].

Which modules or layers a program has is the project's architecture, out of this wiki's scope; this page applies Fowler's split to classes and functions inside a module. Fowler's own example separates database interaction from financial processing (PDF p. 90); where that boundary falls is likewise taken from the project.

This wiki uses one sentence to tell the two apart: one concern spread over many classes is shotgun surgery, and one class holding many concerns is divergent change. A version history that shows files changing together confirms either reading. It is evidence from outside the code.

## Fowler's limit

Fowler warns that the boundary is often visible only after several changes have arrived: "context boundaries are usually unclear in the early days of a program and continue to shift" (PDF p. 90). This wiki reads that as a limit: do not split a young class along a guessed axis of change ([[replaceable-code-over-forecast]]). Wait for the second concern to show up in the code.

## Fowler's repairs

For **divergent change** (PDF p. 91):

- If the two aspects form a sequence (fetch data, then process it), use Split Phase with a clear data structure between them ([[split-phase]]).
- If calls go back and forth, create the modules and use Move Function ([[move-function]]).
- If single functions mix both, use Extract Function first, then move.
- If the modules are classes, use Extract Class.

For **shotgun surgery** (PDF p. 91):

- Move Function and Move Field, to put the changes into one module.
- For functions operating on similar data, Combine Functions into Class. For functions that transform or enrich a data structure, Combine Functions into Transform. Use Split Phase if the common functions can feed one consuming phase.
- Inline Function or Inline Class, to pull poorly separated logic together, then extract again. Fowler accepts the large intermediate: "we aren’t afraid of creating something large as an intermediate step to reorganization" (PDF p. 91).

## Example

Divergent change, before and after, inside one module:

```
class Invoice
    field lines
    field taxRates
    field locale
    method taxFor(region): sum of line.amount * taxRates[region]
    method exemptLines(region): lines whose category taxRates marks exempt
    method formatLine(line): line.amount formatted for locale
    method formatTotal(): total formatted for locale
```

```
class TaxCalculator
    field taxRates
    method taxFor(lines, region)
    method exemptLines(lines, region)

class InvoiceFormatter
    field locale
    method formatLine(line)
    method formatTotal(total)

class Invoice
    field lines
```

## Source

[[fowler-refactoring]], Fowler, *Refactoring*, 2nd ed., ch. 3, "Divergent Change", PDF pp. 90-91, and "Shotgun Surgery", PDF p. 91. The code-visible shapes, the routing to owner pages, the selecting sentence, the scope note on modules and layers, the reading of Fowler's remark on shifting boundaries as a limit, and the pseudocode are this wiki's own.
