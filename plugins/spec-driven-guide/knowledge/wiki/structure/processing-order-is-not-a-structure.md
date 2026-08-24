---
title: Processing order is not a structure
category: structure
summary: Organising a description by the sequence of steps is the default that feels natural and reliably produces the arrangement in which every change propagates.
tags: [failure-mode, information-hiding, structure, symptom]
sources: [web-page-on-the-criteria-to-be-used-in-decomposing-systems-into-modules]
created: 2026-08-06
updated: 2026-08-06
---

The most available way to organise a description of anything that happens is to follow the order in
which it happens: first this, then that, finally the other. Parnas's finding is that this
arrangement is not merely weaker than the alternative — it is the one that produces maximum
propagation, and it is chosen by nearly everyone.

> One might say that to get the first decomposition one makes a flowchart. This is the most common
> approach to decomposition or modularization. It is an outgrowth of all programmer training which
> teaches us that we should begin with a rough flowchart and move from there to a detailed
> implementation.
>
> — [[parnas-criteria-for-decomposing-systems]], L211

His conclusion is unusually flat for the paper's register: "it is almost always incorrect to begin
the decomposition of a system into modules on the basis of a flowchart" (L314).

## Why the sequence misleads

A step in a sequence is defined by *when* it runs. A decision is not: "design decisions transcend
time of execution, modules will not correspond to steps in the processing" (L314). Organising by
sequence therefore cuts across the decisions rather than around them, so each decision ends up
spread over several steps — and a change to it reaches all of them.

Parnas adds a second piece of evidence from a later project, a translator for a Markov algorithm:
decomposed by hidden decision, the same arrangement held for a compiler and for several
interpreters, though their running forms differ deeply. Decomposed "along the classical lines"
— syntax recogniser, code generator, run-time routines — it would not have (L272-L276). The
sequence-based cut is bound to one execution strategy; the decision-based cut outlives the choice.

He lists the rule among his specific recommendations too: "The sequence in which certain items will
be processed should (as far as practical) be hidden within a single module" (L262-L266).

## The symptom in a document

A document organised by processing order reads as a narrative of execution: *first the request
arrives, then it is validated, then it is written, then the notification is sent.* The symptom is
that its section boundaries answer **when**, not **what is committed to**.

This is the ancestor of the most common defect in documents that describe a decision: a section
that enumerates the steps of carrying it out. Such a section is bound to one way of doing the work
and must be rewritten whenever that way changes, which is far more often than the decision it sits
next to.

The check is direct: **if a section could be retitled "step N", ask what commitment it states.**
When the answer is a commitment, the ordering is incidental and the section is fine. When the
answer is only "this happens third", the section describes execution and belongs wherever
execution is described.

Related: [[information-hiding]] for the criterion this rule follows from, and
[[the-changeability-test]] for the evidence that separates the two arrangements.

## Worked pair

**Provenance:** produced by running this base's reviewers against a document written to carry the
defect, not taken from a source. See [[over-specification]] for the same note.

**Before** — the document's four top-level sections:

> ## Implementation steps
> We will build this in the order below.
> ### Step 1 — set up the consumer
> ### Step 2 — render the message
> ### Step 3 — deliver
> ### Step 4 — wire it up

**After** — the same material, four sections again:

> ## The problem
> ## What the service commits to
> ## What it does not do
> ## Why these choices

**The test that produces the rewrite.** Take each step and ask what it *commits to* rather than what
it *does*. Step 1 commits to consuming an event that already exists and acknowledging only after
delivery. Step 2 commits to what the message must carry. Step 3 commits to email as the channel. The
commitments survive; the ordering does not, because it describes one execution.

**What the before-shape costs a reader.** A reader deciding whether the design is right has no
section to disagree with — the commitments have to be reconstructed out of a build narrative. And
every one of them is rewritten the moment the build order changes, which happens far more often than
the design changes.

**The ordering is not waste.** It goes to an execution document, which cites the argument document
for *why* ([[splitting-a-document]]). Deleting it destroys work someone needs and guarantees it will
be rewritten worse.
