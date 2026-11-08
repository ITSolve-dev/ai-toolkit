---
title: Plain text for persistent data
category: types-and-state
summary: "Persisted or exchanged data is written as a binary or fixed-offset layout whose only description is the application code that decodes it."
tags: [rule, types-and-state, persistence, data-format]
paradigm: any
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

A storage format decides who can read data later, and with what. The book takes plain text as the best format for keeping data, and its tip reads «Храните свои знания в виде простого текста» (p. 109). Plain text here means printable characters conveying information, and it can be structured: HTML, JSON, YAML, and network protocols such as HTTP and SMTP all count (pp. 109-110).

## Rule

Keep persistent data in a readable text form. The problem the book finds with most binary formats is that the context needed to understand the data is separated from the data itself (p. 109). It adds that such data may be encrypted, which makes analysing it without the application logic pointless (p. 109). It gives three reasons for text (p. 110).

- **Protection against obsolescence.** Readable, self-describing data outlives other forms and the applications that made it, and can be parsed with only partial knowledge of the format, while most binary files need the format in full detail (p. 110).
- **Reach of tools.** Almost every computing tool works on plain text: version control tracks a configuration file's history, diff tools show what changed, and checksums detect modification (p. 111). Text is also easier to search, as with a recursive `grep` over a configuration directory (p. 111).
- **Simpler testing.** Synthetic test data in text can be written and changed with no special tools, and regression output in text can be analysed with shell commands or a small script (p. 112).

In heterogeneous environments, the book says, the advantages outweigh the drawbacks, since all parties need one common standard (p. 112). The field names inside such text carry a rule of their own: see [[self-describing-field-names]].

## Sign in code

- Writers use fixed offsets, packed structures or a language's object serialiser for data that outlives the process.
- A reader of the saved file can be found only in the application, with no format description beside it.
- Test fixtures are binary blobs that a test author cannot edit by hand.

## When not to apply

- Optimisation. The book notes that some Unix systems also keep a binary form of certain databases for speed, and that a plain-text version is kept to pair with it (p. 111). This wiki reads that as the pattern to follow: the binary form is a derived cache, and text stays the original.

The following limits are this wiki's own. The data may be inherently binary, such as images or audio. Data that lives only within one process run has no reader to protect. A measured size or parse cost on a hot path may justify binary, with a schema that travels with the data.

## Repair

1. Choose a standard text format and do not invent one.
2. Write fields by name.
3. Add a reader for the old format, and convert what exists.
4. If performance needs a binary form, generate it from the text and treat it as disposable.

## Before and after

```
// before: the meaning of each byte is held in this function alone
function saveCustomer(out, c):
    out.writeBytes(packFixed("2s 9d 4s", c.region, c.ssn, c.flags))
```

```
// after: the record explains itself to any tool
function saveCustomer(out, c):
    out.writeLine(toJson({
        region: c.region,
        socialSecurityNumber: c.ssn,
        flags: c.flags
    }))
```

## Source

*The Pragmatic Programmer*, 20th Anniversary Edition, Russian translation: [[pragmatic-programmer]], Topic 16, pp. 109-112. The rule, the three reasons and the note on optimisation are the book's. The book does not name the drawbacks it says are outweighed. The reading of the optimisation limit as a derived cache, the remaining limits, the signs, the repair and the pseudocode are this wiki's own.
