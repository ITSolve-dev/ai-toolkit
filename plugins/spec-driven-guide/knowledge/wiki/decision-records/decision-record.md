---
title: Decision record
category: decision-records
summary: A short document capturing one decision, the forces that produced it, and everything that follows from it — written for a future reader deciding whether to keep it.
tags: [concept, decision-record, genre]
sources: [web-page-documenting-architecture-decisions]
created: 2026-08-06
updated: 2026-08-06
---

A **decision record** captures a single decision, the forces it responds to, and its consequences.
[[documenting-architecture-decisions]] models it on an Alexandrian pattern — "though the decisions
themselves are not necessarily patterns, they share the characteristic balancing of forces" — and
fixes what is central: "the decision is the central piece here, so specific forces may appear in
multiple ADRs" (L32).

One record, one decision. Forces are shared; decisions are not.

## The parts, and the rule inside each

| Part | What it holds | The rule that makes it checkable |
|---|---|---|
| **Title** | A short noun phrase | Names the decision, not the discussion of it |
| **Context** | The forces at play — technological, political, social, project-local | "The language in this section is value-neutral. It is simply describing facts." Forces "are probably in tension, and should be called out as such" (L50-L53) |
| **Decision** | The response to those forces | "It is stated in full sentences, with active voice. 'We will …'" (L55-L56) |
| **Status** | proposed, accepted, deprecated, superseded | See [[superseding-not-editing]] |
| **Consequences** | The resulting context after applying the decision | See [[consequences-include-the-negative]] |

Two of these rules are unusually easy to check against a text. **Context written in value-neutral
language** fails visibly the moment it starts advocating — if the context section argues for the
decision, the decision has leaked upward and the reader can no longer tell what was given from what
was chosen. **Active voice with an explicit subject** fails visibly too: "it was decided that" and
"the system should" name no one and commit no one.

## Length and register

One or two pages. The register is prescribed and the reason is given:

> We will write each ADR as if it is a conversation with a future developer. This requires good
> writing style, with full sentences organized into paragraphs. Bullets are acceptable only for
> visual style, not as an excuse for writing sentence fragments.
>
> — L69

This is a rule with a symptom. A record made of fragments has usually dropped the connective
reasoning — *because*, *therefore*, *despite* — which is the only content a future reader actually
needs. A bulleted list of forces states what was true; a paragraph states why it forced anything.

## How records compose

"The consequences of one ADR are very likely to become the context for subsequent ADRs" (L75). The
records form a chain rather than a set: earlier decisions create the space later ones are made
inside. A record whose context ignores the consequences of prior records is either wrong or
describes a decision made in ignorance of them.

Related: [[architecturally-significant]] for what earns a record, and
[[design-doc]] for the neighbouring genre — a design doc argues one design at length and decays
with the system; a decision record fixes one point of that argument and outlives it.
