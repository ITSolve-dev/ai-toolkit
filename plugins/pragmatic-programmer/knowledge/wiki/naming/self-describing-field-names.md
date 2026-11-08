---
title: Self-describing field names
category: naming
summary: "A stored or wire-format key is a position or sequence number such as field10, f_19 or col3, so its value means nothing without the code that decodes it."
tags: [rule, naming, data-format]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

Readable characters do not make data understandable. The name beside a value does that, and in stored data that name is often the only documentation that survives the program.

## Rule

The book stresses the informational part of plain text: a line assigning an opaque value to a numbered field is of little use, because the reader has no idea what the value means, so the text should be made legible (p. 109). Its example is a legacy data file in which customer social security numbers sit in numbered `FIELD10` tags (p. 110). Recognising the number format lets you extract them even with little other knowledge of the file, which a run of digits packed into a fixed line would not allow (p. 110). Yet the tag itself helps little in understanding the meaning (p. 111). A tag named for the content makes the data far clearer and helps it outlive the project that made it (p. 111).

## Sign in code

- A key in a stored or transmitted record is a sequence number or position: `field10`, `f_19`, `col3`, `attr2`.
- A lookup table in application code maps those keys to their real meanings.
- Readers must count columns or positions to find a value.

## When not to apply

The limits are this wiki's own.

- The numeric tag is defined by a schema file kept with the data, so the schema is the description.
- The name belongs to an external standard that readers can look up.
- The format is internal to one run of one process and is never read from outside.

## Repair

1. Rename each key to the thing the value is, in the terms of the domain.
2. Include the unit where it is not obvious.
3. For existing data, have readers accept the old and new keys, migrate, then drop the old key.

## Before and after

```
// before: the value's meaning lives in a mapping in the code
<field10>123-45-6789</field10>

value = record["field10"]
```

```
// after: the record explains itself
<social-security-number>123-45-6789</social-security-number>

value = record["social-security-number"]
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation: [[pragmatic-programmer]], pp. 109-111. The rule and the numbered-tag example are the book's. The tag names are transcribed from the book's example in corrected form, because the extraction is noisy there, and have not been checked against the page image. The signs, limits, repair and pseudocode are this wiki's own, and the pseudocode adapts the book's example. See [[plain-text-for-persistent-data]] for the format question.
