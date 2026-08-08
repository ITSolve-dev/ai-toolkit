---
title: Confirmation
category: decision-records
summary: How compliance with a decision will be checked — the section that makes a decision record verifiable instead of merely recorded.
tags: [rule, decision-record, verifiability]
sources: [madr]
created: 2026-08-06
updated: 2026-08-06
---

The **confirmation** section of a [[madr-template]] record states how anyone will be able to tell
whether the decision is actually being followed:

> Describe how the implementation of/compliance with the ADR can/will be confirmed. Is the chosen
> design and its implementation in line with the decision? E.g., a design/code review or a test
> with a library such as ArchUnit can help validate this. Note that although we classify this
> element as optional, it is included in many ADRs.
>
> — L217

The worked example makes the shape concrete: check that the chosen library is the only one of its
kind among the dependencies; revisit the pros-and-cons evaluation against experience at review
points; and decide in advance whether and when the decision itself gets re-examined (L308-L312).

## Why it matters more than its optional marking suggests

A decision record without confirmation records an intention. Nothing in it distinguishes a decision
that is being honoured from one that was quietly abandoned, and both look identical to a reader a
year later — who will then either follow a dead rule or ignore a live one.

This is verifiability applied to a decision. No source in this wiki asks for verifiability of a
*requirement* — the catalogues that do were never obtained — so MADR's confirmation section is the
only place any source here demands that a claim be checkable at all. The nearest neighbouring test
is the substitution check in [[imprecise-terminology]], which separates a statement that can be
agreed or disagreed with from one that cannot.

## The symptom

**A confirmation that restates the decision.** "Confirmation: the team uses X" is not a check; it
names the desired state without saying how anyone would observe it. A usable confirmation names an
*observation*: something to look at, a place to look, and what a violation would look like there.

The second symptom is a confirmation that only works once. The example above avoids it deliberately
by including a recurring check and a scheduled re-examination — a decision that will be enforced
only at the moment it is made is not enforced.

## Its relation to the surrounding sections

- [[consequences-include-the-negative]] records what the decision does. Confirmation records how
  you would find out it stopped doing it.
- [[superseding-not-editing]] handles the case where the decision is deliberately changed.
  Confirmation catches the case where it erodes without anyone deciding anything, which is the more
  common one and leaves no trace.
