---
title: Every argument carries a because
category: decision-records
summary: A grammar that forces reasoning into the sentence — each option, consequence and outcome is labelled good, bad or neutral and completed with a because-clause.
tags: [rule, decision-record, symptom, rationale]
sources: [madr]
created: 2026-08-06
updated: 2026-08-06
---

The [[madr-template]] does not ask for reasoning; it makes reasoning the only grammatical way to
fill the template. Every evaluative line has the same shape:

- `Chosen option: "{title of option 1}", because {justification…}` (L209)
- `* Good, because {positive consequence…}` (L212) / `* Bad, because {negative consequence…}` (L213)
- `* Neutral, because {argument c}` (L226) — the template annotates this one: "use 'neutral' if the
  given argument weights neither for good nor bad" (L225)

Three labels and a mandatory clause. A line that stops before *because* is visibly unfinished.

## Why the grammar does the work

Instructions to "explain your reasoning" are followed unevenly, because nothing marks their
absence. A sentence template marks it: the fragment "Good" with nothing after it is obviously
incomplete in a way that a paragraph of unsupported assertion is not.

The three-way labelling adds a second effect. Forcing a label makes the writer classify each
statement before writing it, which surfaces the ones that resist classification — and a statement
that is neither good nor bad nor neutral is usually not a consequence at all, but a description of
the mechanism that crept in.

This is why version 3 merged the previously separate positive and negative consequence sections
into one: a single list "to enable similar grammar as in 'Pros and Cons of the Options'" (L82). One
grammar, applied everywhere evaluation happens.

## The symptom

**A bullet without a because.** Directly detectable, and it survives review because the line reads
as a fact rather than as a missing argument.

Two subtler forms:

- **A because that restates the claim.** "Good, because it is better" carries the grammar and none
  of the content. The test is whether the clause could have been written by someone who disagreed
  with the decision — a genuine reason survives that; a restatement does not.
- **No neutral entries anywhere.** The count is the check; what its absence means is set out in
  [[consequences-include-the-negative]], along with the caveat that the interpretation is this
  wiki's inference rather than a source's claim.

## Beyond decision records

The grammar generalises to any place a document evaluates something — a trade-off in a
[[design-doc]], a rejected option in [[alternatives-considered]]. Wherever a document asserts that
something is better or worse, the same test applies: the assertion and its reason belong in one
sentence, so that removing the reason breaks the sentence.

## Worked pair

**Provenance:** produced by running this base's reviewers against a document written to carry the
defect, not taken from a source. See [[over-specification]] for the same note.

**Before.**

> We will use Kafka rather than polling the database, for consistency with the rest of the platform.
>
> We chose email over in-app notification.

**After.**

> **Email rather than in-app.** The problem statement is that the user is not looking at the product
> when the export finishes — a four-hour export outlasts the session. An in-app notification is
> delivered exactly where the user is not, which leaves the 40 tickets untouched.
>
> **Consume the existing event rather than poll.** The completion fact already exists and is already
> published. Polling would derive the same fact a second way, and the two would diverge the first
> time the pipeline changed how it decides an export is complete.

**Two different defects, and the second is the instructive one.** "We chose email over in-app" has
no because at all — the obvious case. "For consistency with the rest of the platform" *has* the
grammar and fails anyway: it is a reason to prefer the familiar, not a reason Kafka answers this
problem. Someone proposing polling would concede it and carry on proposing polling.

**The test that separates them.** A because earns its place when the claim breaks without it. Remove
"the completion fact already exists and is already published" and the Kafka choice becomes
arbitrary. Remove "for consistency with the rest of the platform" and nothing changes — which is how
you know it was never carrying the argument.

**Ordering follows.** In the *after*, the email decision comes first because it is load-bearing: it
is the one that determines whether the original complaint stops. The *before* had no order at all.
