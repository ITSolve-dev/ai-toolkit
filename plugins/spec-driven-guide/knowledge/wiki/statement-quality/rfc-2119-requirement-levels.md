---
title: "RFC 2119 — Key words to indicate requirement levels"
category: statement-quality
summary: Three pages fixing what MUST, SHOULD and MAY mean, plus a rule restricting when an imperative may be used at all.
tags: [summary, obligation-language, standard]
sources: [web-page-rfc-2119-key-words-for-use-in-rfcs-to-indicate-requirement-levels-rfc-editor]
created: 2026-08-06
updated: 2026-08-06
---

A 1997 IETF Best Current Practice by S. Bradner, three pages long, that does one thing: it fixes
the meaning of the words a specification uses to signal how binding a statement is. Its definitions
are "an amalgam of definitions taken from a number of RFCs" (L93) — it standardised existing
practice rather than inventing it.

Documents adopting it say so explicitly, near the beginning, by naming the key words and citing the
RFC (L41).

## What it supplies

- The levels themselves and what each commits the reader to — [[obligation-language]].
- A restriction on when an imperative may be used at all —
  [[imperatives-constrain-outcomes-not-methods]]. This is the section that matters most here, and
  the one least often quoted.

## The scoping remark

One sentence in the abstract carries more than its length suggests:

> Note that the force of these words is modified by the requirement level of the document in which
> they are used.
>
> — L47

**In the RFC's own context** this is about standards-track maturity: an IETF document occupies a
defined position — Proposed Standard, Best Current Practice, Informational — and a MUST inside an
Informational document does not bind what a MUST inside a standard binds. The force of a statement
is capped by the standing of the document making it.

**Extending that beyond the IETF is this wiki's move, and it needs stating as one.** The
generalisation is that a document cannot lend its statements more authority than it has, so the
same MUST means something different in a normative specification and in a draft design document.
That is plausible, and it is close to what [[state-marks-authority]] makes explicit with a declared
state field. It is not what the RFC says, and no source here supports it directly.

## How to read it

**Authoritative on:** the vocabulary. This is the reference that makes capitalised MUST and SHOULD
mean something specific rather than emphatic, and it is short enough to read in full.

**Narrow by design.** It defines words; it does not say how to write a good requirement, and it
offers no guidance on structure, testability or completeness. Its one piece of writing advice is
the restriction in section 6.

**Its own register is worth noticing.** The rules on imperatives are stated partly in lowercase
("must be used with care and sparingly") and partly in the defined uppercase ("they MUST only be
used where…") — the document applies its own convention to itself, and reserves the binding form
for the binding claim.

**Caveat on the extraction.** The captured page includes the RFC text as a preformatted block with
page-break artefacts ("Bradner Best Current Practice [Page 1]") interleaved at L62, L97 and L107,
and a note that the RFC "was updated" without saying by what (L23). RFC 8174 later refined the
handling of lowercase uses of these words; that update is not in this source.
