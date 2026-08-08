---
title: "Oxide RFD 1 — Requests for Discussion"
category: document-types
summary: A document genre that deliberately admits unfinished work, and the state field that makes doing so safe.
tags: [summary, genre, rfd, authority]
sources: [web-page-1-requests-for-discussion-rfd-oxide]
created: 2026-08-06
updated: 2026-08-06
---

Oxide's founding process document, itself an RFD. It defines a genre for "the written expression of
an idea", explicitly modelled on the earliest IETF Requests for Comments and drawing its workflow
from the Go, Joyent, Rust and Kubernetes proposal processes (L39-L45).

Its opening claim is the reason the genre exists: writing an idea down "allows them to be
rigorously formulated (even while nascent), candidly discussed and transparently shared" (L38).

## What it supplies that the other sources do not

Every other source here pushes toward rigour. This one pushes the other way, deliberately, and
supplies the mechanism that makes the looseness safe:

- [[timely-rather-than-polished]] — the position that unfinished writing is worth publishing, and
  the two reasons given for saying so out loud.
- [[state-marks-authority]] — the metadata field that tells a reader how settled a document is,
  without which the first position is dangerous.

## Its scope, and how wide it is

The listed occasions for an RFD are far broader than a design doc's: "Add or change a company
process", an architectural or design decision, a customer-facing or internal API change, an
internal process change, "A design for testing" (L51-L56). It covers non-technical matters
explicitly: "RFDs not only apply to technical ideas but overall company ideas and processes as
well" (L58).

The genre is therefore defined by *the need for discussion*, not by subject — which makes it the
process sibling of [[when-to-write-a-design-doc]], where the trigger is ambiguity in a solution.

## What it asks a document to contain

Three things, for anything reaching a determination (L67-L69):

- The viable options, with the benefits and drawbacks of each — see [[alternatives-considered]].
- The reasoning, "including data and references wherever possible; making it easy for our future
  selves (and those who join in the future) to understand the decisions we've made and why".
- The determination itself.

Around that core it names four dimensions to consider where they apply — economic cost over short
and long term, customer outcomes against alternatives, performance including whether a regression
is customer-visible, and security (L81-L90). These are posed as questions rather than sections,
which is what keeps them from becoming a form to fill.

And the depth is explicitly variable: "Not every RFD is equal. Some have more sense of urgency and
therefore might not be as rigorous as others… weigh rigor and urgency to your best judgement"
(L104).

## How to read it

**Authoritative on:** how a document set can hold work at different degrees of settledness without
misleading anyone. That is its real contribution, and it is not addressed by any other source here.

**Out of scope for this wiki:** the entire life-cycle half — branch naming, the creation script,
pull request mechanics, the shell dependencies, the API, chat bot, short URLs and labels
(L163 onward). That is tooling and process, which the charter excludes.

**Read as a position, not a survey.** It argues for its own way of working rather than comparing
approaches, and its supporting example — a car company's battery presentation (L93-L100) — is an
illustration of reasoning style rather than evidence.
