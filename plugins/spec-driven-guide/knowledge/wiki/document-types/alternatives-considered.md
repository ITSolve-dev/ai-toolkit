---
title: Alternatives considered
category: document-types
summary: The section that shows a design was chosen rather than defaulted to — its content is the trade-offs of each rejected option, not a description of it.
tags: [rule, design-doc, rationale]
sources: [web-page-design-docs-at-google, madr]
created: 2026-08-06
updated: 2026-08-06
---

**Alternatives considered** lists designs that would reasonably have achieved a similar outcome and
were not chosen. [[design-docs-at-google]] rates it unusually highly for a section that describes
things the project is not doing:

> While it is fine to be succinct about solution that ended up not being selected, this section is
> one of the most important ones as it shows very explicitly why the selected solution is the best
> given the project goals and how other solutions, that the reader may be wondering about,
> introduce trade-offs that are less desirable given the goals.
>
> — L101

## What belongs in it

Not a description of each alternative — **the trade-offs each one makes, and how those trade-offs
led to rejecting it** (L99). Brevity about the option is fine; brevity about why it lost is not.
The asymmetry follows from what the section is for: the reader already knows what the alternatives
are, which is precisely why they are wondering.

## The two symptoms

**Alternatives nobody would have chosen.** A list of straw options makes the section look complete
while doing none of its work. The check: would a competent person have argued for this one? If not,
it is padding, and its presence conceals the absence of the alternative that was genuinely
plausible.

**A missing obvious candidate.** The reverse, and the more expensive one. A reader who thinks of an
alternative the document never mentions cannot tell whether it was considered and rejected or never
occurred to anyone — and the document has failed at the one thing this section exists to do.

Both symptoms are the same defect from opposite sides: the section is meant to close the reader's
open questions about the solution space, and it fails whenever a reasonable question stays open.

## A structural form of the same section

Where a design doc leaves this section's shape to the writer, the [[madr-template]] fixes it: a
flat list of *Considered Options* naming what was on the table, and a *Pros and Cons of the
Options* section giving each one its own labelled arguments (L203, L219-L235). The separation is
useful — the list answers "was this considered?" at a glance, while the pros and cons answer "why
not?" for whoever needs it.

That template also forces the reasoning into the sentence rather than requesting it; see
[[every-argument-carries-a-because]]. The two symptoms above become mechanically visible under
that grammar: a straw option shows up as one with only bad entries and no good ones, and a missing
candidate shows up as an absence in a list short enough to scan.

## Why it outlives the rest of the document

A design doc decays as the system changes ([[design-doc]]), but the reasoning for rejecting an
option decays more slowly — the constraints that made an option bad usually outlast the
implementation that resulted. This is the content most worth extracting into a durable record when
the design doc itself is superseded.

Related: [[non-goals]], which does the same job for outcomes that this section does for solutions —
both distinguish a decision from an oversight for anyone reading later.
