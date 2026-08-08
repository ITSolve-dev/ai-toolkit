---
title: The implementation manual
category: failure-modes
summary: A document that says how the work will be carried out without arguing why — the named symptom that a design doc has become something else, and evidence it need not have been written.
tags: [failure-mode, symptom, design-doc, genre]
sources: [web-page-design-docs-at-google]
created: 2026-08-06
updated: 2026-08-06
---

An **implementation manual** is a document that describes how something will be built without
establishing why it should be built that way. [[design-docs-at-google]] names it as the sign that a
design doc was not needed:

> A clear indicator that a doc might not be necessary are design docs that are really
> *implementation manuals*. If a doc basically says "This is how we are going to implement it"
> without going into trade-offs, alternatives, and explaining decision making (or if the solution
> is so obvious as to mean there were no trade-offs), then it would probably have been a better
> idea to write the actual program right away.
>
> — L117

The judgement is stronger than "this document is at the wrong level". It is that the document
carries no information: if the solution is obvious enough to describe without argument, describing
it costs more than doing it.

## The symptom

The check is a subtraction. **Remove every passage that states how the work is carried out. What
argument remains?**

- A defensible position — the trade-offs, the rejected alternatives, why the goals force this
  shape — means the document is a design doc that happens to carry procedural passages, and the
  passages are the defect.
- Nothing — means the document *is* the manual, and the defect is the document.

The distinction matters because the two have different repairs. The second is either turned into a
real argument or replaced by the work itself.

The first usually should not be edited at all. Procedural passages sitting beside a sound argument
are normally content somebody needs, written in the wrong place — so the repair is a split rather
than a deletion, and cutting them destroys work that will be rewritten worse. See
[[splitting-a-document]].

## Its relationship to the neighbouring failures

This is the genre-level form of [[processing-order-is-not-a-structure]]. Parnas's finding is that
organising *by* sequence produces maximum propagation; the implementation manual is what a document
becomes when sequence is not merely the organising principle but the entire content.

It is also the failure that [[what-a-design-doc-omits]] guards against at the section level: pasted
definitions, schemas and code are each a step toward a document whose content is realisation.
A document accumulating those sections is on its way here.

## Why it is easy to write by accident

Procedural content is the easiest kind to produce and the easiest to feel productive writing. It is
concrete, it is uncontroversial, and it can be generated at length without deciding anything. An
argument about trade-offs cannot: it requires having a position and defending it. A document drifts
toward the manual under exactly the conditions where the design work has not actually been done —
which is what makes the symptom diagnostic rather than merely stylistic.

Related: [[when-to-write-a-design-doc]] for the prior question this failure answers in retrospect.
