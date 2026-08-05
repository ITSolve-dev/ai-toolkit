---
title: Shared Kernel
category: context-mapping
summary: Two teams designate a small, explicitly bounded subset of the domain model and code to share — an intimate interdependency that can leverage design work or undermine it.
tags: [pattern, context-mapping, integration, ubiquitous-language, coupling, shared-kernel]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

A **Shared Kernel** is an explicit agreement between two teams to share part of the domain model and its
code. "Sharing part of the model and associated code forms a very intimate interdependency, which can
leverage design work or undermine it." (raw L2477)

## Definition

Designate, with an explicit boundary, some subset of the [[bounded-context|domain model]] that the
teams agree to share. **Keep the kernel small.** This shared subset has special status and "shouldn't
be changed without consultation with the other team." Define a continuous integration process that
keeps the kernel tight and aligns the [[ubiquitous-language]] of the teams (raw L2477). *(Definition
largely quoted from Evans, raw L2473.)*

## Trade-offs

The upside is that shared design work is not duplicated. The downside is the *intimate
interdependency*: the kernel couples the two contexts at the model level, so any change requires
cross-team consultation and continuous integration to keep it coherent. A kernel that grows past
"small" turns from a leverage point into a source of coupling that undermines both models — hence the
discipline to keep it minimal and gated by consultation. It is the one accepted exception to the "one
team per [[bounded-context]]" rule.

## Failure mode: accidental Shared Kernel via replication

Pursuing autonomy the wrong way can force an unwanted Shared Kernel. Simply replicating an upstream
context's databases into a dependent context "would force the local system to take on many undesirable
responsibilities. That would require the creation of a Shared Kernel, which doesn't really achieve
autonomy." (raw L2579) The autonomy-preserving alternative is to translate minimal state through an
[[anticorruption-layer]] instead — see [[bounded-context-autonomy]].

## Related

- [[bounded-context]] — the "one team per context" rule this is the exception to.
- [[ubiquitous-language]] — what continuous integration keeps aligned.
- [[anticorruption-layer]], [[bounded-context-autonomy]] — the autonomy-preserving alternative.
- [[context-map]] — where the relationship is labelled.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
