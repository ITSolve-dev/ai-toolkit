---
title: What a design doc omits
category: altitude
summary: Interface definitions, schemas and code are kept out of a design doc because they are verbose, carry unnecessary detail, and go stale faster than the document — the volatility argument, stated by practice rather than theory.
tags: [rule, altitude, ceiling, volatility]
sources: [web-page-design-docs-at-google]
created: 2026-08-06
updated: 2026-08-06
---

The design-doc genre has a ceiling, and [[design-docs-at-google]] states it as three parallel
rules rather than as a principle. Each names an artifact and gives the same reason.

**Interface definitions.** Sketching an exposed interface is "usually a good idea", but:

> In most cases, however, one should withstand the temptation to copy-paste formal interface or
> data definitions into the doc as these are often verbose, contain unnecessary detail and quickly
> get out of date. Instead focus on the parts that are relevant to the design and its trade-offs.
>
> — L77

**Storage schemas.** Systems that store data "should likely discuss how and in what rough form
this happens", but "copy-pasting complete schema definitions should be avoided", for the same
reasons (L81).

**Code.** "Design docs should rarely contain code, or pseudo-code except in situations where novel
algorithms are described. As appropriate, link to prototypes that show the implementability of the
design" (L85).

## The reasoning, and why it is the same reasoning

Three artifacts, one argument: they *quickly get out of date*. That is
[[the-changeability-test]] arriving from practice rather than from theory — an element that
changes faster than the document containing it will make that document wrong, and being wrong is
worse than being absent.

The rules are not a ban on precision. Each has a permitted form alongside the forbidden one:

| Forbidden | Permitted |
|---|---|
| Pasted formal interface definitions | A sketch of the interface, focused on what the trade-offs turn on |
| Complete schema definitions | How and in what rough form data is stored |
| Code and pseudo-code | A link to a prototype demonstrating the design is implementable |

The discriminator in every row is the same: **keep what the design's trade-offs turn on, drop what
merely realises them.** That is [[abstract-interface-vs-representation]] with the line drawn one
grain higher, because a design doc's subject is a system rather than a module.

## The stated exception

Pseudo-code is allowed "in situations where novel algorithms are described". The exception is
consistent rather than a concession: when the algorithm *is* the design decision, describing it is
describing the commitment, and omitting it would withhold the substance of the doc. When the
algorithm is a known one being applied, its expression is realisation and the rule holds.

This is the operative test for the borderline case: **does the design's argument survive if this
passage is deleted?** If the trade-offs still stand, the passage was mechanism.

## When this rule collides with the obligation rule

[[abstract-interface-vs-representation]] puts operation names, parameters and types on the side a
description *may* state. This page says not to import interface definitions. Applied to the same
passage they contradict — and the passage is a common one. **Neither rule should be applied alone
there.** [[resolving-a-scale-conflict]] separates the grain question from the form question, which
is what makes both usable.

## Note on how this is usually misremembered

The section headings — "APIs", "Data storage", "Code and pseudo-code" — read like a list of things
a design doc should contain, and are frequently cited that way. The text under each heading argues
the opposite. Anyone invoking this source as licence for pasted definitions is citing the table of
contents.

## Where the ban stops

This source states the ceiling and never states its exception, which makes it easy to read as a ban
on precision. [[when-a-snippet-beats-prose]] holds the other half: a fragment that encodes the
decision more exactly than prose can — a schema, a state machine, a type shape — is a commitment
stated exactly, and stating commitments exactly is what the document is for.
