---
title: "Nygard — Documenting Architecture Decisions (2011)"
category: decision-records
summary: Source summary — the origin of the decision-record genre, and its sharpest contribution: the dilemma facing a reader who meets a past decision without its rationale.
tags: [summary, decision-record, genre]
sources: [web-page-documenting-architecture-decisions]
created: 2026-08-06
updated: 2026-08-06
---

The post the entire architecture-decision-record practice descends from. It proposes keeping "a
collection of records for 'architecturally significant' decisions", each a short file describing
"a set of forces and a single decision in response to those forces" (L30-L32).

It is itself written in the format it proposes, which makes it a worked example as well as a
definition. The five parts and the rules inside them are tabulated in [[decision-record]] rather
than repeated here.

## The problem it solves

Its motivation is stated as a dilemma facing anyone meeting a past decision without its rationale.
They can **blindly accept** it, which is fine while the decision holds and dangerous once context
has moved: "If the project accumulates too many decisions accepted without understanding, then the
development team becomes afraid to change anything and the project collapses under its own weight."
Or they can **blindly change** it, which "could mean damaging the project's overall value without
realizing it" — the example given is a decision supporting a non-functional requirement not yet
tested (L18-L28).

The record exists to make both blind moves unnecessary. This is a sharper purpose than
"documentation": the target reader is someone deciding whether to *keep* a decision.

## What it supplies

- The genre and its parts, with the writing rules under each — [[decision-record]].
- An entry test for what deserves one — [[architecturally-significant]].
- Two rules with checkable symptoms — [[consequences-include-the-negative]] and
  [[superseding-not-editing]].

## Its argument for smallness

Not brevity for its own sake — a claim about what survives:

> Agile methods are not opposed to documentation, only to valueless documentation. Documents that
> assist the team itself can have value, but only if they are kept up to date. Large documents are
> never kept up to date. Small, modular documents have at least a chance at being updated.
>
> — L14

This is the argument for keeping decisions separate from the documents that made them: a design doc
is large and decays ([[design-doc]]); a one-page record has a chance of being maintained, and its
subject — a decision and its rationale — decays more slowly anyway.

## How to read it

**Authoritative on:** what a decision record is, what belongs in each part, and why the genre
exists. Published under a copyright waiver, so it can be quoted freely.

**Incomplete on one point that matters here.** The original format has **no alternatives section** —
rejected options are left to surface inside Context or Consequences, if at all. A record following
this format literally will not say what else was considered. See
[[alternatives-considered]] for what is lost, and the later template variants for how the gap was
closed.

**Dated in its asides**, not its substance: the discussion of whether version control makes records
inaccessible to non-developers (L85) reflects 2011 tooling.
