---
title: Ranking findings
category: reviewing
summary: Rank by how far the damage travels — first outside the document, then to the reader implementing, then within the text — because a report ordered by how easy a defect was to find gets stopped reading.
tags: [method, review, severity, wiki-authored]
sources: []
created: 2026-08-06
updated: 2026-08-06
---

**Provenance: this page is this wiki's own, and no source supplies it.** Every rule page here states
a symptom and a check; none states what a defect costs or how to weigh one against another. The
nearest sourced idea is *cost of reversal* in [[architecturally-significant]], and it is scoped to
whether a decision earns a record, not to how bad a document defect is. It is kept because a review
that cannot rank is unusable, and it should be replaced when a source treating severity is
ingested.

---

A review produces more findings than anyone will act on. The order they are presented in decides
which get fixed, and ordering by how easy each was to find — which is what happens by default —
puts the cheapest findings first and buries the expensive ones.

## The axis: how far the damage travels

**First — damage already outside the document.** The defect has produced a wrong artifact
elsewhere: a decision record overwritten instead of superseded, a downstream document built on a
claim this one got wrong, an implementation shipped against a misread. These rank above everything
because the document is no longer the only thing that needs fixing, and because the damage
compounds silently — see [[superseding-not-editing]] on a broken record chain invalidating
everything written against it.

**Second — damage to whoever acts on the document.** The reader must decide something the document
should have settled, and will decide it arbitrarily: a missing obligation
([[the-use-test]]), a problem raised and never answered
([[a-problem-with-no-decision]]), an unresolvable reference to content that was lost
([[unresolvable-references]]). Nothing is wrong yet; something will be.

**Third — damage to the document's own durability.** The document is correct today and will be
wrong soon: a leaked format, a pasted definition, a named version. These are the findings this
wiki's rules are best at producing ([[what-a-design-doc-omits]],
[[over-specification]]) and they belong third, because a stale sentence in an otherwise sound
document costs less than an unanswerable question in a fresh one.

**Fourth — damage to reading.** Drift between levels, generic vocabulary, a section in the wrong
order. Real, and cheapest to live with.

## Two adjustments

**Reach beats depth within a rank.** A mild defect in the passage everyone reads outranks a severe
one in an appendix. If the document has a section its readers demonstrably use — the interface, the
decision — defects there move up.

**A defect the author will reject costs more than it returns.** If a finding is arguable and the
argument is not overwhelming, it dilutes the rest of the report. Where two rules disagree about a
passage, resolve the disagreement before reporting it ([[resolving-a-scale-conflict]]) or leave it
out; a report at high false-positive rate stops being read, and the findings that matter go with
it.

## What ranking is not

It is not a count. Three ceiling violations do not outrank one broken decision chain, and a
document with many third-rank findings can be in better shape than one with a single first-rank
finding. Report the counts, but rank by the axis.

One pass is exempt. [[pruning-a-document]] produces findings that are all the same severity and all
the same repair, so its output is a list rather than a ranking.

## One fragment of this is now sourced

The provenance note above still holds for the damage axis. But the ordering has a second, narrower
justification that does come from a source: [[functional-and-deep-quality]] establishes that deep
quality is conditional on functional quality, so a functional defect outranks a deep one because
repairing the deep one while it stands cannot succeed. Where that ordering and the damage axis
disagree, the damage axis governs.
