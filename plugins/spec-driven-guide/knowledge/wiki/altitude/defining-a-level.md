---
title: Defining a level
category: altitude
summary: A level is fixed by four things — its scope, what it may contain, what surrounds it, and who reads it — and the audience is what most often decides the rest.
tags: [method, altitude, levels, audience]
sources: [c4-model]
created: 2026-08-06
updated: 2026-08-06
---

[[the-c4-model]] specifies each of its levels with the same four fields, and the discipline is in
the specification rather than in the particular levels chosen.

| | Scope | Primary elements | Intended audience | Recommended by default |
|---|---|---|---|---|
| **System context** | A single software system | The system in scope, its people and its external dependencies | "Everybody, both technical and non-technical people, inside and outside the software development team" | Yes, for all teams |
| **Container** | A single software system | The applications and data stores within it | "Technical people inside and outside the software development team; including software architects, developers and operations/support staff" | Yes, for all teams |
| **Component** | A single container | The components inside that container | "Software architects and developers" | No — only if it adds value |

*(c4-model, L455-L557)*

## The audience is the discriminator

The most useful column is the third, because it is the one that decides the others. Each level's
content follows from who has to read it: the system-context view is "the sort of diagram that you
could show to non-technical people" and therefore "the focus should be on people […] and software
systems rather than technologies, protocols and other low-level details" (L463). The constraint on
content is derived from the reader, not asserted independently.

This gives a practical way to settle an altitude argument that otherwise runs on taste: **name the
reader, and the permissible content follows.** A passage that only its author's immediate
colleagues can use has selected an audience, whether or not anyone chose one.

## Volatility decides what a level excludes

The container level is explicitly stripped of deployment concerns, and the stated reason is one
this wiki reaches from several directions:

> This diagram says very little about deployment aspects such as clustering, load balancers,
> replication, failover, etc because it will likely vary across different environments (e.g.
> production, staging, development, etc).
>
> — L525

The material is excluded not because it is too detailed but because **it varies** — across
environments here, across time in [[the-changeability-test]]. Where it does not vary, it gets its
own artifact: "Deployment information is better captured via one or more deployment diagrams, one
per environment."

That is the general move. Content that varies along a dimension the current level does not model
belongs at a level that does, not nowhere.

## Applying it to a document

Before writing, fix the same four things: what the document is about, what kinds of thing it may
name, what it may refer to but not explain, and who has to be able to act on it. The result is a
declared altitude, which is what makes the discipline in
[[mixed-levels-of-abstraction]] checkable — a section can only be shown to sit at the wrong level
once a level has been claimed.
