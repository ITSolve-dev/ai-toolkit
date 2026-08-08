---
title: When to write a design doc
category: document-types
summary: Ambiguity in the solution is the trigger — where the answer is obvious, the document costs more than it returns, and writing it produces an implementation manual.
tags: [decision-rule, design-doc, genre]
sources: [web-page-design-docs-at-google]
created: 2026-08-06
updated: 2026-08-06
---

Writing a design doc is overhead, and [[design-docs-at-google]] treats the decision to write one as
a trade-off in its own right rather than a default:

> At the center of that decision lies whether the solution to the design problem is
> ambiguous — because of problem complexity or solution complexity, or both. If it is not, then
> there is little value in going through the process of writing a doc.
>
> — L115

**Ambiguity is the trigger.** Not size, not risk, not seniority of the author. A large but obvious
change does not earn a design doc; a small but contested one does.

## The retrospective check

The decision is made before the document exists, so it is easy to get wrong. There is a check that
works afterwards: a document that turned out to be an [[implementation-manual]] is evidence the
ambiguity was not there. If the finished text argues no trade-offs because there were none, the
answer had been obvious all along and "it would probably have been a better idea to write the
actual program right away" (L117).

## The secondary reasons

Ambiguity is the primary trigger; the post lists others that can carry the decision on their own,
and suggests writing one when three or more apply (L162-L170):

- Uncertainty about the right design that upfront time would resolve.
- Value in involving senior engineers who cannot review every change.
- A design contentious enough that organisational consensus is itself worth producing.
- A team that forgets cross-cutting concerns — privacy, security, logging — unless a document
  forces them.
- A need for high-level entry points into systems that already exist.

Note what these have in common: each is a reason the *document* does work that the code cannot, by
reaching people or concerns the code never surfaces. None of them is "we always write one".

## Against the agile objection

The post pre-empts the argument that upfront documents conflict with rapid iteration, and concedes
the narrow form of it — the overhead "may not be compatible with prototyping and rapid iteration".
Then it draws the boundary:

> most software projects do have a set of *actually known problems*. Subscribing to agile
> methodologies is not an excuse for not taking the time to get solutions to actually known
> problems right.
>
> — L119

It also folds prototyping into the writing rather than opposing it: "'I tried it out and it works'
is one of the best arguments for choosing a design" (L119). Empirical evidence is design-doc
content, not a substitute for it.

Related: [[design-doc]] for what the document then has to contain.
