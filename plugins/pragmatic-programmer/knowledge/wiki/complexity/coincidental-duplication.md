---
title: Coincidental duplication
category: complexity
summary: "Two functions with identical bodies whose names and inputs refer to different things: decide whether they state one requirement or two before merging them."
tags: [decision-rule, duplication, knowledge, code-review]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-07
---

Not every duplication of code is a duplication of knowledge. The book makes this a section of its own (p. 64), and it is the main limit on [[dry]].

## Rule

Identical code is a violation only when it represents the same knowledge. The book's example is two validators in a wine-ordering application, one for age and one for quantity, with identical bodies, and the site owner's requirement covers both: each must be a positive number (p. 64). A reviewer who rejects them under DRY is wrong, because the two functions validate different data that happen to follow the same rules: «Это всего лишь совпадение, а не дублирование» (p. 64).

## Sign in code

Two functions or blocks have the same body, and their names, parameters or call sites refer to different domain facts. The opposite case, real duplication, shows as bodies that restate one named rule or one constant's meaning, so that changing one means changing the other. That case is [[dry]]'s, which owns the sign of a restated fact; this page owns the decision when the bodies match and the facts may not.

The source gives the example and not a general test. This wiki's test: write the requirement each body implements as one sentence, without looking at the other. If the two sentences name the same fact, it is duplication. If they name different facts that happen to agree today, it is coincidence.

This wiki assigns a narrower neighbour as follows. Two existing functions with identical bodies whose names refer to different things are [[coincidental-duplication]]; a block of statements inside a routine that computes what one existing function already computes is [[replace-inline-code-with-function-call]], whose name test (would the function's name read right in place of the block?) is the same decision at the level of one block.

## When not to apply

- If a requirement says the two must stay in step, so that changing one means changing the other, the likeness is knowledge, not chance, and [[dry]] applies. A requirement that merely lists both under the same constraint is not that, as the book's example shows. This condition is this wiki's own.
- Where the requirements behind the two bodies cannot be found in the code or from anyone who owns them, this test has no answer. The page then has nothing to report, and neither merging nor keeping them is grounded. This condition is also this wiki's own.

## Repair

Leave the two functions separate and reject the merge. The book asks for no change. This wiki notes that the book's validators already call shared lower-level checks for type and minimum, so the mechanism is shared and only the statement of what applies to each datum remains separate. That is the shape to aim for when the bodies grow.

## Before and after

This page's verdict is that the code stays, so its pair shows a review note and its answer. Before, the sign and the note it prompts:

```
// review note: identical bodies, merge into validate_count
function validate_rental_days(value)
    require_integer(value)
    require_at_least(value, 0)

function validate_seat_count(value)
    require_integer(value)
    require_at_least(value, 0)
```

After, the note is rejected and the two functions stay. This is the form it asked for, which would tie two facts to one statement:

```
// rejected: not written
function validate_count(value)
    require_integer(value)
    require_at_least(value, 0)

validate_count(rental_days)
validate_count(seat_count)
```

With the two kept apart, a change to the rental limit leaves `validate_seat_count` untouched.

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation (Dialektika, 2020), Topic 9, p. 64, via [[pragmatic-programmer]]. This wiki's own: the one-sentence test, the split with [[dry]], both limits, the remark on shared lower-level checks, and the pseudocode.
