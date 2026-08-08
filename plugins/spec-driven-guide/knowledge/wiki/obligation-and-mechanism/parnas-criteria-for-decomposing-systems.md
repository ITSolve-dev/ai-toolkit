---
title: "Parnas — On the Criteria To Be Used in Decomposing Systems into Modules (1972)"
category: obligation-and-mechanism
summary: The source of information hiding, and the root argument for why a description should be organised around what is likely to change rather than around the order of processing.
tags: [summary, information-hiding, foundations, paper]
sources: [web-page-on-the-criteria-to-be-used-in-decomposing-systems-into-modules]
created: 2026-08-06
updated: 2026-08-06
---

A 1972 CACM paper by D. L. Parnas that asks a question its contemporaries left unasked: not
*whether* to divide a system into parts, but **by what criterion**. It answers with
[[information-hiding]] — begin from the decisions likely to change, and give each part the job of
hiding one.

## Why it belongs in a wiki about writing

The paper argues about module boundaries in code and never once about prose documents. **The
transfer to writing is this wiki's, not Parnas's**, and the two claims should be kept apart.

**What Parnas states.** The two decompositions he compares may produce the same running artifact
and still be different systems: "the runnable representation need only be used for running; other
representations are used for changing, documenting, understanding, etc. **The two systems** will
not be identical in those other representations" (L147-L159). His subject there is the system as
documented — its work assignments, module specifications and source — not a prose design document.

**What this wiki adds, and on what argument.** The transfer holds because both a module boundary
and a document are instruments for *deciding what a reader may depend on*, and both pay the same
price when that decision is wrong: everything told about a revised decision must be revised with
it. That is the whole of the argument, and it is enough to carry [[information-hiding]] and
[[the-changeability-test]] across.

**Where the transfer weakens, and it matters.** A module boundary is enforced. A caller that
reaches past it fails to compile, so the hidden decision stays hidden whether or not anyone is
disciplined. A prose boundary is enforced by nobody: a reader who needs what the document withheld
does not get an error, they **guess** — and act on the guess. So the same omission that is free in
code has a cost in prose, and hiding is not automatically safe the way Parnas's argument implies.

This is the reason the criterion cannot be applied to a document without a floor. That floor is
[[minimal-is-not-short]], and the failure it prevents is documented from the other side in
[[the-right-altitude-for-an-agent]].

What the paper supplies:

- The criterion itself, with its reasoning — [[information-hiding]].
- A discriminating rule for what a description may state and what it must withhold —
  [[abstract-interface-vs-representation]]. This is the paper's most useful gift to this wiki: it
  puts operation names and parameter types on the *revealed* side and storage formats and table
  organisation on the *hidden* side.
- An operational method for deciding either question — [[the-changeability-test]].
- Two failure modes with worked symptoms — [[over-specification]] and
  [[processing-order-is-not-a-structure]] — plus the reader-side symptom in
  [[comprehensible-only-as-a-whole]].

## Its central worked example

A KWIC index system: it takes lines of words, produces every circular shift of every line, and
prints them alphabetised (L49). Parnas cuts it two ways — once by processing step (input →
circular shift → alphabetise → output), once by hidden decision (line storage, circular shifter,
alphabetiser as *abstract services*) — then runs five likely changes through both. The comparison,
not the assertion, is what makes the paper persuasive, and it is reproduced in
[[the-changeability-test]].

## How to read it

**Authoritative on:** the criterion for decomposition, why the flowchart criterion fails, and what
an interface should reveal. These are the sections from the abstract through the "specific
examples of decompositions" list (L14-L266).

**Out of scope here:** everything from the efficiency discussion onward (L268-L312) — procedure
call overhead, assembling modules from collected code, hierarchy and partial ordering. These are
implementation concerns of 1972, and the charter excludes them.

**Extraction caveat.** The available full text is a digitised transcription that opens by
disclaiming accuracy against the author's original: "It is not guaranteed to be an accurate copy
of the author's original work" (L12). It also carries visible OCR damage — `SETCHAR(rpv,c,d)` for
what must be `SETCHAR(r,w,c,d)` (L92-L95), `SKI WORD` (L291), reference numbers run into the text
as `[41` and `[1,10.23]`. Quotations here were taken only from passages free of such damage;
before publishing a verbatim quotation elsewhere, check it against the ACM Digital Library
version.

**Dated in vocabulary, not in argument.** Core memory, four-characters-per-word packing and
Fortran date the examples. The criterion does not: its shortest statement is in the paper's closing
paragraph (L314), one sentence before the closing sentence, which is about implementation
efficiency rather than about the criterion.
