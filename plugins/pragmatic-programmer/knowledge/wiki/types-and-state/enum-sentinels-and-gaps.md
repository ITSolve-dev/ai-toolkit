---
title: "Reserve an invalid first member; beware gaps when iterating an enum"
category: types-and-state
summary: "An enum whose first (zero) member is a valid value, a loop over an enum by hard-coded first and last members (for c = RED to BLUE), or iteration over an enum whose members have explicit non-consecutive values (1, 2, 4, 8)."
tags: [rule, enums, initialization, loops, sentinels]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

*Code Complete* gives four pieces of advice about the members of an enumeration rather than about using one: reserve the first as invalid, mark the first and last for loops, fix the convention project-wide, and beware explicit values (Russian edition, pp. 296-298).

## Rule

- **Reserve the first member as invalid.** Most compilers give the first member the value 0, and an uninitialized variable is more likely to hold 0 than any other wrong value; making 0 invalid exposes it (p. 297). The book's example adds `Country_InvalidFirst = 0` and starts the real members at 1.
- **Mark the first and last members** (`Country_First`, `Country_Last`) so that loops and array sizes cover the whole type without naming a particular member (pp. 296-297).
- **Make it a project rule.** These markers raise questions: do real members start at 0 or 1, are First and Last themselves valid? The book's answer is that if the technique is used, the coding standard should require InvalidFirst, First and Last for every enumeration without exception (p. 297).
- **Beware explicit values.** Where members have explicit values such as 1, 2, 4 and 8, a loop variable of that type running from first to last also takes 3, 5, 6 and 7, which are not members (p. 298).

The book also advises checking for invalid values whenever an enum drives an `if` or `case`, with an `else` arm that reports an internal error (p. 296). That sign is owned by [[default-branch-catches-the-unexpected]].

## Sign in code

- An enumeration whose zero or default member is a meaningful value, and a declaration or field of that type in view has no explicit initial value.
- A loop over an enumeration bounded by its currently first and last named members (`for c = RED to BLUE`), which silently stops covering the type when a member is added.
- A loop or array indexed by an enumeration whose members have explicit, non-consecutive values.
- Enumerations in one codebase that disagree on whether a sentinel exists and whether First and Last are valid.

This wiki assigns neighbouring cases as follows. This page owns the members of an enum. Whether to use an enum at all is [[enum-instead-of-codes-and-flags]]. A branch over an enum without a default arm is [[default-branch-catches-the-unexpected]]. A variable left without an initial value is [[initialize-close-to-first-use]].

## When not to apply

The book states no limits here. The limits below are this wiki's own:

- **A language whose enumerations are not integers**, or that requires every variable to be initialized, or that offers iteration over members (`values()`), removes the reason for the sentinel and for First/Last; use what the language gives.
- **An enum serialised to an outside format** cannot have an invalid member inserted without changing every stored value; add it only with a migration.
- **Flag sets** whose members are bit values are combined, not iterated; the gap warning applies only to iteration and array indexing.
- **A project convention** on enums decides; where none exists and the technique is wanted, the book's own advice is to make one.

## Repair

1. Where the zero value can arise by accident, add an explicit invalid member at 0 and start valid members after it; treat the invalid member as an error wherever it is read.
2. Replace loops bounded by particular members with loops over First..Last markers, or over the language's member list.
3. For enums with explicit gapped values, iterate the member list rather than the numeric range.
4. Write the convention down once and apply it to every enumeration.

## Before and after

```
enum Color { RED = 0, GREEN = 1, BLUE = 2 }
for c = RED to BLUE
  rate[c] = compute(c)

enum Access { READ = 1, WRITE = 2, EXEC = 4 }
for a = READ to EXEC
  describe(a)
```

```
enum Color { INVALID = 0, FIRST = 1, RED = 1, GREEN = 2, BLUE = 3, LAST = 3 }
for c = Color.FIRST to Color.LAST
  rate[c] = compute(c)

for a in Access.members()
  describe(a)
```

## Source

[[code-complete]], McConnell, *Code Complete*, 2nd ed., Russian edition, chapter 12: checking invalid values with `Case Else`, p. 296; First and Last as loop bounds, pp. 296-297; reserving the first member, p. 297; the project-standard rule, p. 297; explicit values and gaps, p. 298. This wiki's own: the signs, all limits, the member-list repair, the split with neighbouring pages, and the pseudocode.
