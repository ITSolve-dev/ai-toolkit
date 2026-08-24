---
title: State marks authority
category: document-types
summary: A declared state tells a reader how settled a document is — the mechanism that lets unfinished work be published without being mistaken for a decision.
tags: [mechanism, authority, genre, lifecycle]
sources: [web-page-1-requests-for-discussion-rfd-oxide]
created: 2026-08-06
updated: 2026-08-06
---

If a written statement is read as authoritative by default ([[timely-rather-than-polished]]), then
publishing tentative work requires a way to say otherwise. [[oxide-rfd-process]] does it with a
required metadata field carrying one of six values (L122-L159).

| State | What it tells the reader |
|---|---|
| `prediscussion` | Not ready to discuss; a placeholder under rapid iteration. "Essentially a collaborative extension of an engineer's notebook" |
| `ideation` | Only a description of the topic and its scope. Not under active revision — "a scratchpad for related ideas", which anyone may pick up "with or without the participation of the original author" |
| `discussion` | Actively being discussed |
| `published` | Discussion converged. This is where "an idea represents the consensus or direction" |
| `committed` | Entirely implemented |
| `abandoned` | Non-viable, deliberately never implemented, or otherwise to be ignored |

## The rule that makes the scale load-bearing

The states are not merely descriptive; two of them are fenced off from meaning agreement:

> These states shouldn't be used for ideas that have been committed to, organizationally or
> otherwise; by the time an idea represents the consensus or direction, it should be in the
> `published` state.
>
> — L151

So `prediscussion` and `discussion` cannot be used to hold a settled decision. Without that
restriction the scale would decay: everything would sit in a middle state permanently, and the
reader would learn nothing from it.

## Why six rather than three

Three of the six mark things that are easy to conflate and expensive to confuse:

- **`ideation` versus `prediscussion`** — both unfinished, but one is being worked on and one is
  not. The difference tells a reader whether picking it up would duplicate effort, and the source
  makes the invitation explicit for the inactive one.
- **`published` versus `committed`** — decided versus built. A reader consulting documentation to
  learn how a system works needs to know which of these they are holding, and the answer is
  otherwise invisible.
- **`abandoned`** — retained rather than deleted, for the same reason a superseded decision is
  ([[superseding-not-editing]]): knowing something was considered and rejected is information, and
  its absence invites the idea to return.

## Two properties worth carrying regardless of the vocabulary

**Published is not frozen.** "Note that just because something is in the `published` state does not
mean that it cannot be updated and corrected" (L147). The state records the degree of agreement,
not editorial closure.

**Comment routing follows the state.** Comments on a `committed` document "should generally be
raised as issues", and where a comment "represents a call for a significant divergence from or
extension to committed functionality, a new RFD may be called for" (L155). Where a document sits
determines what disagreeing with it produces — which is the practical payoff of having the field
at all.

Related: [[decision-log]] and [[consistency-across-a-set]] — a state field is also what lets a
reader navigate a large collection without reading everything, since it filters by settledness
before subject.
