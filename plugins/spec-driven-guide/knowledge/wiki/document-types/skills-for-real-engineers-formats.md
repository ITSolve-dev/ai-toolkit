---
title: "ADR-FORMAT and to-spec (Skills for Real Engineers)"
category: document-types
summary: Two working document formats from one practitioner toolkit — the shortest decision-record format this wiki holds, and a spec format that draws the detail line and then states its exception.
tags: [summary, design-doc, decision-record, ceiling]
sources: [web-page-matt-pocock-skills-formats]
created: 2026-08-08
updated: 2026-08-08
---

Two files from the same open-source toolkit, ingested together because each is short and each takes
a position the wiki's other sources do not. Neither is an essay; both are instructions a tool
follows, which means their rules are stated as decisions rather than as arguments.

## What they supply

- [[a-record-can-be-one-paragraph]] — the minimal end of the decision-record spectrum, against
  [[madr-template]], plus a three-part entry gate sharper than any other here.
- [[when-a-snippet-beats-prose]] — the detail rule with its exception stated, which is the
  counterweight this wiki was missing on the ceiling side.

## Where each sits against the wiki's other sources

**On decision records**, it sits at the short end of a range the other sources already allow. It
gives a title and one to three sentences, and says so plainly: "That's it. An ADR can be a single
paragraph. The value is in recording *that* a decision was made and *why* — not in filling out
sections" (L49). Status, considered options and consequences are demoted to optional: "Only include
these when they add genuine value. Most ADRs won't need them" (L53).

The wiki initially read that as a disagreement with [[madr-template]], and it is not. MADR ships
"bare" and "minimal" templates and describes itself as "a template allowing to craft short,
medium-sized, and large decision records" (madr, L264, L77). Both accept a short record; they differ
in what a short record keeps — this source removes the headings, MADR keeps them and lets each be
brief.

The narrow live disagreement is with [[consequences-include-the-negative]], which this wiki holds as
a rule against a source that makes the section optional. It is resolved on
[[a-record-can-be-one-paragraph]] rather than left open.

**On the detail ceiling**, the source restates the rule this wiki's other sources reach — "Do NOT
include specific file paths or code snippets. They may end up being outdated very quickly" (L140) —
using the same volatility ground as [[what-a-design-doc-omits]] and [[the-changeability-test]]. Its
contribution is the sentence after it (L142), which is the only stated exception in any source
here.

## What this wiki does not take from it

Its spec template (L106-L160) is a section list, which the charter excludes. Two of its instructions
are also worth recording as *not* adopted, since a reader may meet them:

- **"A LONG, numbered list of user stories […] extremely extensive"** (L118, L126). This wiki has no
  source supporting exhaustive enumeration as a genre requirement, and [[sprawl]] and
  [[canonical-examples-not-edge-cases]] both argue against it. The instruction is noted, not kept.
- **Its numbering and directory mechanics** (L59-L61) are doc tooling, excluded by the charter; the
  trade underneath them is on [[decision-log]].

## How to read it

**Authoritative on:** nothing, in the sense of being a studied position. It is one practitioner's
working configuration, published as such.

**Useful because it is opinionated at the boundary.** Both of its in-scope claims are places where
the wiki's other sources hedge or go silent, and a stated position — even a contestable one — is
what a boundary question needs. Weigh it as one practice against MADR's and Nygard's, not as a
settlement.
