---
title: Design doc
category: document-types
summary: A document written before implementation that argues why a design is the right one — its load-bearing content is the trade-offs, not the description of what will be built.
tags: [concept, design-doc, genre]
sources: [web-page-design-docs-at-google]
created: 2026-08-06
updated: 2026-08-06
---

A **design doc** is written by the authors of a system before implementation, and records "the
high level implementation strategy and key design decisions with emphasis on the trade-offs that
were considered during those decisions" ([[design-docs-at-google]], L32).

Its distinguishing content is the argument, not the description. The genre's own statement of this
is unambiguous: the design doc is "*the place to write down the trade-offs* you made in designing
your software. Focus on those trade-offs to produce a useful document with long-term value" (L63).
A document describing the same design without that argument is a different thing — see
[[implementation-manual]].

## What the argument is made of

Three ingredients, in a fixed relation: **given the context (facts), goals and non-goals
(requirements), the design doc suggests solutions and shows why a particular one best satisfies
those goals** (L63).

Each carries a genre constraint of its own:

- **Context** is background, not requirements. It "isn't a requirements doc" and "should be
  entirely focused on objective background facts" (L53). A context section that argues for the
  chosen solution has absorbed the design section.
- **Goals and [[non-goals]]** are the requirements, and the non-goals do most of the work of
  bounding what the document claims.
- **The design** is where the trade-offs live, and what it may and may not contain is governed by
  [[what-a-design-doc-omits]].
- **[[alternatives-considered]]** shows the chosen solution was chosen rather than defaulted to.

## Length as a signal

The stated range is "around 10-20ish pages" for a large project, with an explicit floor: "it is
absolutely possible to write a 1-3 page 'mini design doc'" for incremental work, doing "all the
same steps as for a longer doc, just keep things more terse" (L111).

The upper bound carries a diagnosis rather than a style preference. The source reads excess length
as evidence about the *problem* rather than about the writing: a document that runs far past the
range is a document whose subject was too large, not one that was written verbosely (L111). What to
do about an over-large subject is a question about planning, which this wiki's charter puts out of
scope; the length is kept here as a symptom, not as an instruction.

## How it ages

A design doc goes stale, and the genre accepts this. Docs "tend to get out of sync with reality
over time" while remaining "the most accessible entry point to learn about the thinking that guided
the creation of the system" (L154). The recommendation is to update while the system has not
shipped; after that, practice drifts toward amendments in separate documents, producing "an
eventual state more akin to the US constitution with a bunch of amendments rather than one
consistent piece of documentation" (L150).

That drift is the argument for keeping durable decisions somewhere other than the design doc that
made them, since the design doc is expected to decay while the decision is not.

Related: [[when-to-write-a-design-doc]] for whether to write one at all, and
[[degree-of-constraint]] for how the solution space shapes what the document has to do.
