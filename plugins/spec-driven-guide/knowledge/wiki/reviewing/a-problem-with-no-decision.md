---
title: A problem with no decision
category: reviewing
summary: Every problem a document names must be answered by something the document decides — an orphaned problem is a defect, and the check is a coverage pass over the document's own opening.
tags: [failure-mode, review, symptom, wiki-authored]
sources: []
created: 2026-08-06
updated: 2026-08-06
---

**Provenance: this page is this wiki's own, and no source supplies it.** [[design-doc]] states the
relation it depends on — "given the context (facts), goals and non-goals (requirements), the design
doc suggests solutions and shows why a particular one best satisfies those goals" — and no source
turns that relation into a check. It is kept because the check fires on real documents and because
the relation it enforces is already established; it should be grounded when a source treating
requirement coverage is ingested.

---

A document that opens by naming several problems and closes having answered fewer is defective, and
the defect is invisible to every other check here. Each individual section can be well written, at
the right level, properly sourced — and the document still fails at the thing it was written to do.

## The check

It is a coverage pass, and it runs over the document's own claims rather than over an external
standard:

1. **Enumerate the problems the document names**, in its own words, from its opening. Not the
   problems you think it should address — the ones it says it addresses.
2. **For each, find the passage that resolves it.** A resolution is a decision, a constraint, or an
   explicit deferral. Restating the problem later is not a resolution.
3. **Report every problem with no resolving passage.**

Three outcomes, and they need distinguishing:

- **Resolved** — a passage decides it.
- **Deliberately deferred** — the document says it is out of scope. That is a [[non-goals]] entry
  and is correct behaviour, provided it is stated rather than implied by absence.
- **Orphaned** — named, never answered, never deferred. The defect.

## Why the orphan is expensive

The reader most affected is the one implementing. They read a problem statement, build a mental
model of what the document is for, and then find the document silent at the point it mattered. They
resolve it themselves, silently and at their discretion — the same failure
[[non-goals]] describes for an unmentioned candidate goal, but worse: here the document *raised*
the question and then dropped it, so the reader has positive reason to believe it was handled.

The most damaging variant is when the document's own solution reproduces the problem it opened
with. That is not an omission but a contradiction between the opening and the body, and it means
the document shipped without anyone running this check.

## Its relation to the neighbouring checks

- [[the-use-test]] finds the same class of defect empirically and more expensively; this check is
  the cheap textual approximation, and it only finds problems the document was honest enough to
  name.
- [[implementation-manual]] asks whether *any* argument remains after removing procedure. This asks
  whether the argument that remains answers the question that was asked.
- [[alternatives-considered]] covers unexamined solutions. This covers unanswered problems, and a
  document can fail either independently.
