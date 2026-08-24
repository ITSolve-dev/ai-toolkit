---
title: Timely rather than polished
category: document-types
summary: A deliberate lowering of the bar for what may be written down, with the two failure modes it exists to prevent named explicitly.
tags: [position, genre, authority, counterweight]
sources: [web-page-1-requests-for-discussion-rfd-oxide]
created: 2026-08-06
updated: 2026-08-06
---

[[oxide-rfd-process]] adopts, verbatim, the standard set by the third IETF Request for Comments
(L39) — a standard whose content is the deliberate absence of one:

> The content of a note may be any thought, suggestion, etc. […] Notes are encouraged to be timely
> rather than polished. Philosophical positions without examples or other specifics, specific
> suggestions or implementation techniques without introductory or background explication, and
> explicit questions without any attempted answers are all acceptable. The minimum length for a
> note is one sentence.
>
> — L41

Each clause licenses something the rest of this wiki would flag: a position without evidence, a
technique without its context, a question with no attempted answer.

## The two reasons, and why stating them matters

The source keeps the original's justification, which is sharper than the permission itself:

> These standards (or lack of them) are stated explicitly for two reasons. First, there is a
> tendency to view a written statement as ipso facto authoritative, and we hope to promote the
> exchange and discussion of considerably less than authoritative ideas. Second, there is a natural
> hesitancy to publish something unpolished, and we hope to ease this inhibition.
>
> — L43

**The first is a claim about readers.** Writing something down confers apparent authority on it
regardless of the author's intent. A document therefore has a default force it did not choose, and
one that will be wrong for anything tentative.

**The second is a claim about writers.** The same effect suppresses the writing: knowing that a
written statement will be read as a position, people withhold ideas that are not yet positions —
and the ideas most worth discussing are exactly those.

Together they describe a trap. Unstated authority makes tentative writing risky, so tentative
writing does not happen, so nothing gets discussed until it is already decided.

## What this corrects in the rest of this wiki

Almost every other rule here raises a bar. Obligations should declare their force
([[obligation-language]]); consequences should be complete
([[consequences-include-the-negative]]); arguments should carry their reasons
([[every-argument-carries-a-because]]). Applied without exception, these standards prevent the
document that says "I think this is wrong and I do not yet know why" — which is frequently the most
valuable thing anyone will write about a subject.

The reconciliation is not that the standards are optional. It is that **standards attach to a
document's claimed status, not to writing as such**, and a document must therefore be able to
declare its status. That is what [[state-marks-authority]] provides, and without it this position
degrades into an excuse for sloppy work presented as settled.

## The symptom this predicts

A body of documents in which everything is finished. If no document in a set is visibly tentative,
either the ideas arrive fully formed — implausible — or the tentative ones are being written
somewhere unrecorded, and the reasoning that produced the finished documents is lost.
