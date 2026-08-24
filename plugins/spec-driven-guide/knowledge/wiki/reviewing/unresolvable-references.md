---
title: Unresolvable references
category: reviewing
summary: A document naming something it never introduces — the cheapest defect to detect mechanically, and evidence that content was lost between drafting and publication.
tags: [failure-mode, review, symptom, wiki-authored]
sources: []
created: 2026-08-06
updated: 2026-08-06
---

**Provenance: this page is this wiki's own, and no source supplies it.** The charter lists
"unresolvable references" among what reviewing covers, and none of the ingested sources addresses
it. It is kept because it names the most mechanically detectable defect found in the real documents
this wiki was tested against, and because leaving the charter bullet empty was worse. It should be
replaced or grounded when a source that treats it is ingested.

---

An **unresolvable reference** is a name a document uses without ever introducing: a labelled
alternative whose siblings are absent, a section referred to that does not exist, a term used as
though defined earlier, a link to a document that was never written.

## Why it is worth its own check

Two properties make it unusually valuable:

**It is decidable without judgement.** Every other check in this wiki requires weighing whether
something is too detailed, too vague, or too binding. This one asks whether a name has an
antecedent, and the answer is yes or no.

**It is evidence of a specific event.** A label like "Approach B" is not a stylistic choice — it
proves an enumeration existed and did not survive into the text. Something was decided, written or
discussed, and the record of it was lost between drafting and publication. The reference is a
receipt for missing content, which is why it is worth more than the two words it occupies.

## The check

Collect every name the document uses as though already known, then confirm each has an antecedent:

- **Ordinal or lettered labels** — "Approach B", "the second option", "Phase 2". Confirm the
  siblings exist. A label with no sibling is the strongest instance of this defect.
- **Definite references to document parts** — "as described above", "see the constraints section".
  Confirm the part exists and says what is claimed.
- **Terms used as though defined** — a name introduced without definition and then relied on.
- **External pointers** — links, document names, ticket numbers. Confirm the target exists; a
  pointer into a repository is checkable, a pointer into someone's memory is not.

The last category has a variant worth separating: a reference the author never verified, phrased
with a hedge — "the existing tests (if any)", "the style guide (if it describes this)". That is not
an unresolvable reference but an **unverified precondition**: the author is issuing instructions
about artifacts whose existence they did not check. In a document meant to be executed, the hedge
is where the execution will stop.

## What it is not

**Not a missing alternative.** [[alternatives-considered]] covers a document that never considered
an option. This covers a document that *did* consider one and lost the text — a different defect
with a different repair, and a much stronger claim, because the document itself is the evidence.

**Not a broken cross-document link.** [[consistency-across-a-set]] covers references between
documents in a set. This one is internal, and detectable without holding the set.
