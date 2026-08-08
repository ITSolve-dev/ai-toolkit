---
title: Minimal is not short
category: writing-for-agents
summary: The target is the smallest set of information that fully specifies the expected behaviour — cutting past that point removes obligations, not verbosity.
tags: [rule, altitude, agent-reader, corrective]
sources: [web-page-effective-context-engineering-for-ai-agents]
created: 2026-08-06
updated: 2026-08-06
---

Every rule about removing detail invites the wrong reading, and
[[effective-context-engineering]] blocks it in a parenthesis:

> you should be striving for the minimal set of information that fully outlines your expected
> behavior. (Note that minimal does not necessarily mean short; you still need to give the agent
> sufficient information up front to ensure it adheres to the desired behavior.)
>
> — L47

The operative phrase is **fully outlines**. Minimality is measured against a fixed requirement —
the behaviour must be fully specified — not against a page count. A shorter text that leaves
behaviour underspecified is not more minimal; it has failed the requirement and is simply smaller.

## Why the corrective is needed

The whole family of rules this wiki collects — hide what will change, omit what goes stale, keep
imperatives sparse — reads as "cut". Applied without a floor, each of them cuts past obligations
into vagueness, arriving at the upper failure mode in
[[the-right-altitude-for-an-agent]] while feeling like discipline.

The floor is what stops it. **A document may drop anything that is not required to establish what
it commits to. It may not drop what is.** That is the same asymmetry the central rule states from
the other side: mechanism goes, obligations stay ([[information-hiding]]).

## The symptom

**A document that reads as principled and leaves a reader unable to act.** It is the harder defect
to see, because every individual sentence looks defensible and nothing in the text is wrong. What
is wrong is absent.

The test is behavioural rather than textual: give the document to someone — or something — with no
outside context and a decision to make, and see whether they can make it. A reader who has to
choose arbitrarily has found a missing obligation, and the arbitrary choice marks its location.

## The related trap

Brevity is also a poor proxy in the other direction. A document can be long and still minimal, if
its length is worked examples rather than hedging — see
[[canonical-examples-not-edge-cases]], where the recommended fix for a failure is *more* text of a
specific kind. Length is not the variable being optimised in either direction.

## The ceiling that stands opposite this floor

This page is the floor; [[sprawl]] is the ceiling, and the two are only usable together. Sprawl is
the failure of a document that is too long **while every line in it is live and unique** — so its
repair is relocation, never the cut this page forbids. A reviewer applying one without the other
gets it wrong in a predictable direction: the floor alone excuses length, the ceiling alone excuses
deletion.

The mechanical checks that shorten a document without touching obligations are in
[[pruning-a-document]].
