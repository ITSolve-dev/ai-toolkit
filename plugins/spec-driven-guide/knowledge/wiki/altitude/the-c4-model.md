---
title: "The C4 model (Simon Brown)"
category: altitude
summary: Source summary — a diagramming model, from which this wiki takes only its reasoning about levels: how a level is specified, and why mixing them is a defect.
tags: [summary, altitude, levels]
sources: [c4-model]
created: 2026-08-06
updated: 2026-08-06
---

An approach to describing software structure through four nested levels — software system,
container, component, code — each with a diagram type. Its guiding analogy is a map: "a way to
create 'maps of your code', at various levels of detail, in the same way you would use something
like Google Maps to zoom in and out of an area you are interested in" (L143).

It is about diagrams, and this wiki is not. What transfers is everything the model says about
**levels**: how one is defined, what fixes its boundary, and what goes wrong when they blur.

## What it supplies

- [[defining-a-level]] — the four-part specification each level carries, including the one this
  wiki's other sources omit: the intended audience.
- [[mixed-levels-of-abstraction]] — the defect named in its problem list, with the rest of that
  list as symptoms.
- [[imprecise-terminology]] — a worked argument that vague vocabulary, not insufficient levels, is
  usually what makes a description unplaceable.
- [[consistency-across-a-set]] — its separate list of what goes wrong across a collection rather
  than within one artifact.

## Two positions worth carrying

**Do not produce a level because it exists.** "You don't need to use all 4 levels of diagram; only
those that add value" — context and container are "sufficient for most software development teams",
and the component level is explicitly not recommended by default: "only create component diagrams
if you feel they add value" (L449, L557). The hierarchy is available, not obligatory.

**Levels are named for convenience, not for correctness.** "Feel free to modify the terminology
that you use to describe software architecture at different levels of abstraction. Just make sure
that everybody explicitly understands it" (L411). The discipline is that the levels are *defined*
and *shared*, not that they carry these particular names.

## How to read it

**Authoritative on:** what makes a level a level, and on the symptoms of level confusion. The
model has a large user base and its author is candid about where it does not fit.

**Bounded to structure.** It describes static structure and says so; it offers nothing about
argument, rationale, or obligation, which the other sources here supply.

**Out of scope for this wiki:** the history section (L151-L183), the microservices and messaging
modelling guidance (L297-L399), and notation, tooling and the diagram-drawing advice itself. What
was taken is the reasoning about levels, not the practice of drawing.

**One level is described here that the wiki never specifies.** The model names four — software
system, container, component, code — and this wiki's [[defining-a-level]] tabulates only the first
three. The code level is omitted deliberately: the source itself recommends against producing it by
default, and its content is implementation, which the charter excludes. The hierarchy is quoted as
four; the levels this wiki works with are three.
