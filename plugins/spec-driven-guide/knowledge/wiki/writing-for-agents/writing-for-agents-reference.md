---
title: "writing-for-agents (Skills for Real Engineers)"
category: writing-for-agents
summary: A practitioner reference on documents an agent reads, and the only source here that argues about a document's volume rather than about the kind of content in it.
tags: [summary, agent-reader, pruning, structure]
sources: [web-page-writing-for-agents]
created: 2026-08-08
updated: 2026-08-08
---

A skill from an open-source Claude Code plugin, written as a reference for authoring any document
an agent consumes. It states its own reach in the first line: "Reference for writing any document
an agent consumes — a skill, an `AGENTS.md` / `CLAUDE.md`, a doc reached by a pointer. The
packaging differs; the writing does not" (L24).

## Why it matters to this wiki

Every other source here argues about **what kind** of content to remove — the volatile, the
mechanical, the redundant. This one is the first that argues about **how much**, and names the
defect: "a document simply too long, even when every line is live and unique" (L61). That closes
the gap [[synthesis]] records on the volume side, and it does so without licensing the cut
[[minimal-is-not-short]] forbids, because its own remedy is relocation rather than deletion.

## What it supplies

- [[context-pointer]] — how out-of-context material is reached, and why the wording of the
  reference decides reliability.
- [[the-two-loads]] — the two budgets a document spends, and why one of them is not to be
  minimised.
- [[the-information-hierarchy]] — steps versus reference, and the three rungs a piece of material
  can sit on.
- [[sprawl]] — the volume failure, with the remedy that distinguishes it from ordinary cutting.
- [[pruning-a-document]] — four checks that remove load without removing obligation, including the
  environment-as-source-of-truth rule.
- [[leading-words]] and [[completion-criteria]] — two levers on phrasing, both about how few words
  can carry a behaviour.

## Where it sits relative to the wiki's other sources

Its reasoning is neither Parnas's volatility nor RFC 2119's interoperation. The stated ground is
**attention and maintenance under repeated automated reading** — the same ground as
[[effective-context-engineering]], reached by a practitioner rather than by the model vendor, and
carried much further into the mechanics of a document. Where the two overlap they agree; this
source is the more specific of the two.

Its distinctive move is to treat the surrounding **environment** as a source of truth competing
with the document: a document that restates what a config file already says is "a **cache**: a copy
of a lookup, earning its load only when the lookup is expensive" (L97). This wiki reads that as the
volatility argument arriving from a fifth direction, and as the sharpest positive statement any
source here gives of what a document is *for* — see [[pruning-a-document]].

## How to read it

**Authoritative on:** documents written to be read by an agent, repeatedly, as part of a running
process. It is a working artifact rather than a published essay, and it argues from observed
behaviour of agents running its own documents.

**In scope, partly.** The reference proper is in scope. Its companion file on skill mechanics —
frontmatter fields, invocation modes, router skills — is tooling for one plugin system and is
excluded by this wiki's charter, as is the "split by invocation" half of L72-L77.

**Unsourced in the way a practitioner document is.** Its claims are stated as findings without
experiments behind them. The mechanisms it names are checkable against a text, which is why they
are kept here; the magnitudes it implies are not.
