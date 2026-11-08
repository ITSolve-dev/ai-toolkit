---
title: Similar functions with a varying middle
category: functions
summary: "Two or more functions share the same opening and closing lines and differ only in the algorithm between them."
tags: [rule, duplication, composition, strategy]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-07
---

A family of functions that open and close alike, and differ only inside, is a structural form of [[dry]] violation. The book lists avoiding it among the coding practices for [[orthogonality]] (p. 75).

## Rule

Avoid similar functions. The book describes a set of functions that share common code at the start and the end with a different algorithm in the middle, and says of it: «Такое дублирование кода служит явным признаком структурных недостатков» (p. 75). It points to the Strategy pattern as a better implementation (p. 75).

## Sign in code

At least two functions have the same setup lines and the same teardown lines, in the same order, around a block that differs.

This wiki assigns the neighbouring case as follows. This page owns a shared frame around a differing middle, and [[dry]] sends it here. Functions whose bodies differ only in literal values are [[parameterize-function]]; functions that share opening and closing lines and differ in the algorithm between them are [[similar-functions-varying-middle]]. Method bodies repeated on sibling classes that share no superclass of the project's own are [[mixins-share-functionality]]. Overrides of one method on subclasses of a common superclass of the project's own, identical but for one step or wholly identical, are [[shared-behavior-in-superclass-varying-step-polymorphic]].

## When not to apply

The limits are this wiki's own, since the source states none:

- If the matching opening and closing lines express different facts, the likeness is a coincidence. Apply [[coincidental-duplication]].
- If extraction needs flags or many parameters to cover differences in the frame itself, the functions are not of the same shape, and the shared frame would be harder to read than the repetition.

## Repair

Move the shared frame into one function, and make the varying block a parameter: a strategy object, or in a language that passes functions, a function. Each former function becomes a call that supplies its own step.

## Before and after

Before:

```
function export_csv(rows)
    text = new_buffer()
    write_banner(text)
    for row in rows
        text.append(join(row, ","))
    write_totals(text, rows)
    return text.contents()

function export_tsv(rows)
    text = new_buffer()
    write_banner(text)
    for row in rows
        text.append(join(escape_all(row), TAB))
    write_totals(text, rows)
    return text.contents()
```

After:

```
function export(rows, encode_row)
    text = new_buffer()
    write_banner(text)
    for row in rows
        text.append(encode_row(row))
    write_totals(text, rows)
    return text.contents()

export(rows, csv_row)
export(rows, tsv_row)
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation (Dialektika, 2020), Topic 10, p. 75, via [[pragmatic-programmer]], citing Gamma et al. for Strategy. This wiki's own: the wording of the sign and its assignment, the limits, the detail of the repair, and the pseudocode.
