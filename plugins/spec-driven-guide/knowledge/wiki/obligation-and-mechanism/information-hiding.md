---
title: Information hiding
category: obligation-and-mechanism
summary: Organise a description around the decisions likely to change, giving each part the job of hiding one — the criterion that decides what a document may state.
tags: [concept, information-hiding, criterion]
sources: [web-page-on-the-criteria-to-be-used-in-decomposing-systems-into-modules]
created: 2026-08-06
updated: 2026-08-06
---

**Information hiding** is the criterion that a description should be organised around the
decisions most likely to change, with each part responsible for concealing one such decision from
everything else. Parnas states it as a replacement for the obvious alternative — organising by the
order in which processing happens:

> We propose instead that one begins with a list of difficult design decisions or design decisions
> which are likely to change. Each module is then designed to hide such a decision from the others.
>
> — [[parnas-criteria-for-decomposing-systems]], L314

The companion rule governs what the resulting boundary says about itself: "Its interface or
definition was chosen to reveal as little as possible about its inner workings" (L213).

## Why it works

A decision that is hidden can change without disturbing anything that does not know it. A decision
that is exposed cannot: everything that read it must be revised with it. So the cost of a future
change is set not by how hard the change is, but by **how many places were told about the decision
it revises**. Parnas demonstrates rather than asserts this, by tracing five candidate changes
through two decompositions of one system — see [[the-changeability-test]].

This is why *likelihood of change* is the selection criterion and not, say, size or complexity.
Hiding a decision that will never change buys nothing.

## Applied to a document — this wiki's transfer, not Parnas's

Parnas writes about modules. This wiki applies the criterion to documents, and the transfer needs
its own argument rather than a restatement.

The argument: a module boundary and a document both decide **what a reader is permitted to depend
on**, and both pay the same price for deciding wrongly. Name a decision, and everyone who read the
name has to be found and corrected when it changes. Withhold it, and the change is confined. The
mechanism that makes hiding pay in code — cost proportional to how many places were told — is
present in prose unchanged, because it is a property of readers, not of compilers.

So the rule transfers as: **a document should state what its subject commits to, and conceal how
that commitment is met.**

**And it transfers with one asymmetry that Parnas has no reason to mention.** A compiler enforces a
module boundary; nothing enforces a prose one. A caller that reaches past a module boundary fails
to build. A reader who needs what a document withheld simply guesses, and the guess is invisible
until it is expensive. Hiding in prose is therefore *not* free the way hiding in code is, and this
criterion must be applied against a floor: see [[minimal-is-not-short]]. Applied without it, the
rule reads as licence to say less and produces the failure in
[[the-right-altitude-for-an-agent]].

Two consequences follow, each with its own page:

Two consequences follow, each with its own page:

- What the boundary may name is not a matter of taste —
  [[abstract-interface-vs-representation]] draws the line where Parnas draws it.
- Revealing more than the commitment requires is a defect in its own right, even when everything
  revealed is true — [[over-specification]].

## This page is the method, not the conclusion

Information hiding is Parnas's way of *arriving* at a rule that several unrelated sources also
reach by other routes. If you are citing the shared conclusion — that a description states the
commitment and withholds the means — cite [[state-the-commitment-not-the-means]], which holds the
convergence and the tests each ground supplies. This page holds the criterion for organising a
description around what will change.

## What it does not say

Information hiding is not a rule against detail. Parnas's own abstract interfaces name operations,
their parameters and their types in full, and he treats that precision as necessary rather than
tolerated. The rule discriminates between **kinds** of detail, not between more and less of it.
