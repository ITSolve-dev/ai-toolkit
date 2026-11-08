---
title: Source code as the authoritative description
category: documentation
summary: "Concept: the code is the one description of a program that stays current, so a fact a maintainer needs belongs in names, types, constants and reason-giving comments, not only in a document beside the code."
tags: [concept, documentation, self-documenting-code, drift]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

McConnell argues that what construction produces, the source code, is often the only accurate description of a program. Programmers frequently have no documentation besides the code; requirements and design documents go out of date, while the code always matches what the program does, so the code has to be of the highest possible quality (p. 6). In his words: «исходный код актуален всегда» (p. 6). He adds that the methods for improving source code are applied most effectively during construction (p. 6).

This is the reasoning behind several rules in this wiki. It is not a rule itself, because it has no sign of its own in code.

## What it changes in practice

This wiki reads McConnell's argument as follows; the inference is ours, not his:

- When a fact a maintainer needs exists only in a ticket, a wiki page or a design doc, it will drift, and the code will not show the drift. The durable place for it is the code: a name that states the intent, a named constant in place of a literal, a type that rules out an invalid value, or a comment that gives a reason the code cannot state. See [[documentation-in-the-source]].
- A comment is part of this same description, but it does not share the code's guarantee of staying current, because nothing runs it. A comment that repeats the code is the external document moved closer, and it drifts like one. See [[comment-why-not-how]].
- McConnell contrasts a detailed, correct and therefore informative program with a Rube Goldberg device (p. 6). This wiki takes that to mean a reader should be able to rebuild the design from the code alone.

## Limits

These limits are this wiki's own; McConnell states none here.

- The code's executable parts are authoritative only about what the program *does*. A reason or a rejected alternative can sit in a comment ([[design-notes-in-code-headers]]), but without the code's guarantee of staying current. The requirement, and a decision spanning several applications, belong in project documents, which are `spec-driven-guide`'s concern, not this wiki's.
- The argument does not license deleting external documentation. It says which description wins when the two disagree.

## Failure modes

This wiki's own observations of how the idea is misapplied:

- Taking "the code is the documentation" as a reason to write no comments at all, including where a reason cannot be read from the code.
- Fixing drift by editing the external document while the code stays unreadable, so the next reader faces the same gap.

## Related

[[documentation-in-the-source]], [[comment-why-not-how]], [[tests-instead-of-documentation]].

## Source

[[code-complete]], ch. 1, section 1.2, Russian edition, p. 6: code is often the only accurate description; specs and design documents drift; code must be of high quality; the methods are best applied during construction; the Rube Goldberg contrast. Everything under *What it changes in practice*, *Limits* and *Failure modes* is this wiki's own extension. The quotation was taken from `raw/`, whose text layer carries hyphenation noise in this passage; it is to be checked against the page image.
