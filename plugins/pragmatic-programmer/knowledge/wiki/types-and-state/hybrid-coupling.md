---
title: Hybrid coupling
category: types-and-state
summary: "One variable or field whose value ranges carry different meanings: a count where -1 means error, an id where values above a threshold denote a different entity, a size whose negative values hold another quantity."
tags: [rule, hidden-meaning, sentinel, hybrid-coupling, invalid-states]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

Hybrid coupling is McConnell's second way of giving a variable more than one purpose. This wiki reads it as: the variable does one job at a time, but different values of it mean different kinds of thing. The term is Page-Jones's (1988), and the book's wording is «гибридным сопряжением» (p. 250). The book's diagnosis is that the variable is torn between two jobs, so its type is wrong for one of them. Its example is `pageCount`, normally an integer count of pages, where -1 signals an error: «целое число работает по совместительству» as a boolean (p. 250).

## Rule

«Избегайте переменных, имеющих скрытый смысл» (p. 250). The book's three examples (p. 250):

- `pageCount` is the number of pages printed, unless it equals -1, which means an error occurred.
- `customerId` below 500 000 is a customer number. Above it, you subtract 500 000 to get the number of an overdue account.
- `bytesWritten` is positive for the number of bytes written to the output file and negative for the number of the disk used for output.

The book's argument for the rule: even if the double meaning is clear to the author, someone else will not understand it, and the clarity that two variables give is worth far more than the storage they cost (p. 250).

## Sign in code

- Code compares a variable or field against a threshold or a special value (`== -1`, `< 0`, `> 500000`) and then treats the value as a different kind of quantity or entity on each side.
- Arithmetic decodes a second meaning from a value, for example subtracting an offset to get a different id.
- A comment or a document says that a range of a field "means" something other than the field's name.

This wiki assigns the neighbouring cases as follows. This page owns a variable or field, held in state or passed around, whose ranges encode different meanings. A sentinel *returned from a function* to signal an absence that a correct program can meet is [[never-return-null]]. One signalling a state only a bug can produce is [[crash-early]]. One returned from a catch below an entry point is [[recover-only-at-entry-points]]. A value returned by a routine whose in-band -1, null or empty result signals failure is [[wrap-values-between-transformations]] where a correct program can meet the failure, or [[crash-early]] where only a bug can; [[hybrid-coupling]] owns a value stored in a variable or field and read elsewhere, whose ranges encode different meanings. A value that fits its field only by coincidence, such as a phone number in a numeric field, is [[representation-that-fits-by-coincidence]]. Reassigning a variable to an unrelated meaning over time is [[one-variable-one-purpose]].

## When not to apply

The limits below are this wiki's own:

- An interface fixed by an outside party, such as an operating-system call that returns -1 with an error code or a wire protocol, carries its encoding as given. Decode it once at the boundary, and do not let the encoded value travel further into the code.
- A documented, language-wide convention whose special value every reader knows, such as `indexOf` returning -1, is arguably not hidden. Within the project's own types, prefer an explicit result; see [[null-object-or-optional]].
- In performance-critical packed data, encoding several facts in one word may be deliberate. Then keep it behind accessors that decode it, so the meaning is stated in one place.

## Repair

1. Split the value into one variable or field per meaning: a count and a separate status, or a customer id and a separate overdue-account id.
2. Where the meanings are exclusive alternatives, model them as a type with one variant per meaning (a tagged union, a small class hierarchy, or a result type), so that a value of the wrong kind cannot be read as the other.
3. Replace every threshold comparison and decoding offset with a read of the new field or a match on the variant.

## Before and after

Before:

```
// job.bytes_written is set elsewhere: negative means the output disk's number
if job.bytes_written < 0
    mount_disk(-job.bytes_written)
else
    log_size(job.bytes_written)

if customer_id > 500000
    show_overdue(customer_id - 500000)
else
    show_customer(customer_id)
```

After:

```
match job.output
    ToDisk(number)  -> mount_disk(number)
    ToFile(bytes)   -> log_size(bytes)

match reference
    CustomerRef(id)       -> show_customer(id)
    OverdueAccountRef(id) -> show_overdue(id)
```

## Source

McConnell, *Code Complete*, Russian edition, via [[code-complete]], section 10.8, p. 250: the rule, the three examples, the term hybrid coupling (after Page-Jones, 1988), the diagnosis that the type is wrong for one job, and the clarity argument. The checklist on p. 251 asks whether any variable has a hidden meaning. This wiki's own: the reading that the variable does one job at a time, the signs as worded, the assignment against the sentinel pages and [[wrap-values-between-transformations]], all the limits, the repair steps (the book only says to avoid such variables and use two variables for two kinds of data) and the pseudocode.
