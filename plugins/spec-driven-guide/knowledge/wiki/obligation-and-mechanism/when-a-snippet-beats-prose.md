---
title: When a snippet beats prose
category: obligation-and-mechanism
summary: The one stated exception to the rule against code in a document — a fragment earns its place when it encodes the decision more exactly than sentences can, and is trimmed to the part that decides.
tags: [decision-rule, ceiling, discriminator, symptom]
sources: [web-page-matt-pocock-skills-formats, web-page-design-docs-at-google]
created: 2026-08-08
updated: 2026-08-08
---

Every source in this wiki that mentions code in a document argues against it, on volatility
grounds. [[skills-for-real-engineers-formats]] restates that rule — "Do NOT include specific file
paths or code snippets. They may end up being outdated very quickly" (L140) — and is the only one
that then states an exception:

> Exception: if a prototype produced a snippet that encodes a decision more precisely than prose
> can (state machine, reducer, schema, type shape), inline it within the relevant decision and note
> briefly that it came from a prototype. Trim to the decision-rich parts — not a working demo, just
> the important bits.
>
> — L142

## Reading the exception as a test

This wiki extracts three conditions, all of which the passage requires together:

1. **The snippet encodes the decision, not its realisation.** A state machine *is* the decision
   about legal transitions; a function that implements it is one way of running it.
2. **Prose cannot state it as precisely.** The named forms — state machine, reducer, schema, type
   shape — share a property: each is a structure whose exactness is the point, and each becomes
   ambiguous when narrated. A paragraph describing five states and their transitions is longer and
   less exact than the table.
3. **It is trimmed to what decides.** "Not a working demo, just the important bits." A runnable
   fragment carries setup, error handling and naming that decide nothing, and every line of that is
   a commitment the document did not intend to make.

Condition 1 is the discriminator, and it is the same one
[[abstract-interface-vs-representation]] draws. Parnas puts operation names, parameter counts and
types on the side a description may state; a type shape is exactly that. The exception is therefore
not a hole in the rule — it is the rule applied to a form of content that happens to look like
code.

## What this settles

The same source lists what its spec's decisions section may contain: "The interfaces of those
modules that will be modified […] Schema changes […] API contracts" (L133-L137), immediately before
forbidding file paths and snippets. The boundary it draws is therefore **contract versus
implementation**, not **prose versus code**.

That resolves a question the wiki's other sources leave open by omission.
[[what-a-design-doc-omits]] records that a design doc "should rarely contain code, or pseudo-code
except in situations where novel algorithms are described" and that pasted interface definitions go
stale — read alone, that reads as a ban on precision. This page holds the other half: a contract
stated exactly is a commitment, and stating a commitment exactly is what the document is for.

## The symptom

**A snippet you can delete without losing a decision.** Remove it and read the surrounding prose:
where the prose still says everything the document commits to, the snippet was illustration.

**A snippet that runs.** Imports, initialisation, a `main`, error paths — each is a line the reader
may take as a commitment, and none of them decides anything. The trim test is mechanical: keep the
lines a reader would have to change in order to change the decision, and delete the rest.

**A pasted definition with no note of where it came from.** The exception requires the provenance
note; without it, a reader cannot tell whether the fragment is a commitment or a copy that has
since drifted from its original ([[the-changeability-test]]).

Related: [[state-the-commitment-not-the-means]], the rule this is an application of;
[[implementation-manual]], the failure mode reached by admitting snippets that fail all three
conditions.
