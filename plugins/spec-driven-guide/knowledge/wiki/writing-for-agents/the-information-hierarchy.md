---
title: The information hierarchy
category: writing-for-agents
summary: Material sits on one of three rungs — an in-file step, in-file reference, or reference pushed behind a pointer — and the placement decision is made by which branches need it, not by how long it is.
tags: [method, agent-reader, structure]
sources: [web-page-writing-for-agents]
created: 2026-08-08
updated: 2026-08-08
---

A document mixes two content types: **steps**, "the ordered actions the agent performs", and
**reference**, "definitions, rules, facts consulted on demand"
([[writing-for-agents-reference]], L49). They combine freely — all steps, all reference, or both.

The placement decision is a ladder "ranked by how immediately the agent needs the material"
(L49-L53):

1. **In-file step** — "the primary tier: what the agent does, in order."
2. **In-file reference** — "consulted on demand. Often a legitimately flat peer-set (every rule of
   a review on one rung) — a fine arrangement, not a smell."
3. **Disclosed reference** — "pushed out into a separate file, reached by a context pointer, loaded
   only when the pointer fires."

The tension is stated symmetrically: "Push too little down and the top bloats; push too much and
you hide material the agent actually needs" (L55).

## The test that decides a rung

**Branching.** "Inline what every branch needs, and push behind a pointer what only some branches
reach" (L57). The source calls this "the cleanest disclosure test" and names nothing it is cleaner
than.

This wiki keeps it for a reason of its own: it is the only placement test here that can be run
against the text. Enumerate the distinct cases the document handles, then check each block against
them.

The move down the ladder is **progressive disclosure**, and the source is explicit that its purpose
is not economy: "Not primarily a token optimisation: it is how the hierarchy is protected" (L57).
What it protects against is stated sharply — where a document has steps, misplaced in-file
reference "buries them and turns attending to them into a coin-flip" (L57). This wiki notes the
consequence for review: the defect shows up as *inconsistent* execution rather than as wrong
execution, so it is invisible to any check run once.

## Co-location: the same decision, within a file

Where the ladder decides how far down a piece sits, **co-location** decides what sits beside it
once there: "Keep a concept's definition, rules, and caveats under one heading rather than
scattered, so reading one part brings its neighbours with it" (L59).

The source separates it from a defect it resembles: duplication "repeats one meaning in two
places"; scattering "fragments one meaning across many" (L59). One is a maintenance cost, the other
a comprehension cost, and the repairs are opposite — delete versus gather.

## The symptom

**A rule whose exception lives under a different heading.** Read any one heading in isolation and
ask whether a reader stopping there would act correctly. Where the answer depends on a caveat
sections away, the meaning is scattered.

For the ladder itself: **a block of reference that only one branch reaches, sitting between two
steps.** That is the placement error the branching test names, and it is visible without knowing
anything about the reader.

Related: [[sprawl]], the failure this ladder is the cure for; [[splitting-a-document]], for the cut
made when the material is two genres rather than two rungs; [[comprehensible-only-as-a-whole]], for
the defect scattering produces at the scale of a whole document.
