---
title: "Design Docs at Google (Malte Ubl)"
category: document-types
summary: The most widely cited account of the design-doc genre — what it carries, what it deliberately omits, when not to write one, and how it ages.
tags: [summary, design-doc, genre]
sources: [web-page-design-docs-at-google]
created: 2026-08-06
updated: 2026-08-06
---

An account of how design docs are used at Google: informal documents written by the authors of a
system before implementation, recording "the high level implementation strategy and key design
decisions with emphasis on the trade-offs that were considered" (L32).

Its opening frame is the reason it belongs here: engineering's job "is not to produce code per se,
but rather to solve problems", and prose can be the better instrument early, because it
"communicates the problems and solutions at a higher level than code" (L34).

## What it supplies

- The genre itself and what makes a document one — [[design-doc]].
- **Explicit omission rules with their reasoning** — [[what-a-design-doc-omits]]. This is the
  section most often misremembered: the post argues *against* pasting interface definitions,
  schemas and code into a design doc, and argues it on volatility grounds.
- The decision of whether to write one at all — [[when-to-write-a-design-doc]].
- Two section-level rules with checkable symptoms — [[non-goals]] and
  [[alternatives-considered]].
- A discriminator for how a doc should be shaped — [[degree-of-constraint]].
- The failure mode it names outright — [[implementation-manual]].

## Its structure, and how firmly it is meant

The post lists a structure — context and scope, goals and non-goals, the actual design,
alternatives considered, cross-cutting concerns — but disclaims it first: "Design docs are informal
documents and thus don't follow a strict guideline for their content. Rule #1 is: Write them in
whatever form makes the most sense for the particular project" (L47). The structure is offered as
what "has established itself as really useful", not as a template. Read the sections for the
reasoning inside them, not as a form to fill.

Two of its section rules are worth carrying regardless of structure. Context "isn't a requirements
doc" and "should be entirely focused on objective background facts" (L53) — a genre boundary
inside a section. And the design section is "*the place to write down the trade-offs* you made";
the post ties long-term value directly to that focus (L63).

## How to read it

**Authoritative on:** what a design doc is for, what it should not contain, and when writing one is
not worth it. It is a practitioner account from an organisation with a large sample, and it is
candid about cost — reviews are "a dangerous trap of overhead" (L140), and the doc itself is
overhead to be justified.

**Weaker on:** anything checkable. It gives few detectable symptoms; most guidance is stated as
practice rather than as a rule whose violation you could point at. The exceptions —
[[non-goals]], [[implementation-manual]], and the omission rules — are the parts this wiki can
lean on.

**Out of scope here:** the review-process and lifecycle material (L121-L156) is organisational
practice, and the tooling asides are excluded by the charter. One lifecycle observation is kept
under [[design-doc]] because it bears on what the genre is for: docs drift from reality, and
amendments accumulate in separate documents rather than being folded back in.
