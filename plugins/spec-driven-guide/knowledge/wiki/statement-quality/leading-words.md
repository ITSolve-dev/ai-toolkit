---
title: Leading words
category: statement-quality
summary: One word the reader already holds a concept for can carry a behaviour that a paragraph defines badly — and the word must be repeated as a token, never restated as a sentence.
tags: [mechanism, phrasing, economy, symptom]
sources: [web-page-writing-for-agents]
created: 2026-08-08
updated: 2026-08-08
---

A **leading word** is "a compact concept already living in the model's pretraining that the agent
thinks with while running the document (*lesson*, *fog of war*, *tracer bullets*)"
([[writing-for-agents-reference]], L81). The mechanism is repetition of the token without
repetition of the definition: "Repeated as a token, never as a sentence, it accumulates a
distributed definition and anchors a whole region of behaviour in the fewest tokens, by recruiting
priors the model already holds."

The source is specific about coinages: "a made-up word recruits no priors — you pay in definition
tokens what a pretrained word gives free; reach for an existing word first" (L81).

## Why it belongs in a wiki about abstraction

It is the one lever here that shortens a document **and** raises its altitude at the same time.
Every other economy rule trades something away. The worked examples show the trade absent
(L87-L88):

| Spelled out | Leading word |
|---|---|
| "fast, deterministic, low-overhead" | *tight* — a *tight* loop |
| "a loop you believe in" | *red* — "a fuzzy gate becomes a binary observable state" |

This wiki reads the second row as the more instructive. The replacement did not merely compress the
phrase; it converted an unverifiable statement into a checkable one, which is the same repair
[[imprecise-terminology]] asks for. A leading word that names an observable state does the work of
[[obligation-language]] and of pruning in one edit.

The source's instruction is to hunt for these rather than wait for them: "Assume every document is
carrying restatements that leading words retire — go find them" (L90).

## Negation, the failure mode beside it

> steering by prohibition drags the forbidden behaviour into context and makes it *more* available,
> not less. *Don't think of an elephant*, and the elephant is all there is […] Prompt the
> **positive** — state the target behaviour ("write one-line comments") so the banned one is never
> spoken.
>
> — L92

The source allows one exception, with a condition attached: "A prohibition earns its place only as
a hard guardrail you cannot phrase positively; even then, pair it with the positive target so
attention lands on what to do."

This wiki notes the tension with its own material. [[non-goals]] and an out-of-scope section are
prohibitions by construction, and both are load-bearing genre elements. The reconciliation this
wiki draws: a non-goal states what the *document* does not commit to, which is a boundary on the
text; a negated instruction states what the *reader* must not do, which is a behaviour. The rule
above governs the second.

## The symptom

**A phrase of three or more words appearing at more than one site, always in the same sense.** That
is the restatement a leading word retires, and it is found by search rather than by judgement.

**An instruction whose main verb is negated, where a positive form exists.** "Do not use raw SQL" →
"query through the repository". The test for whether the exception applies: try to write the
positive form. Where none can be written, the prohibition is a guardrail and stays — with the
target stated beside it.

Related: [[pruning-a-document]], which grades a leading word by the same test it grades a sentence —
a word too weak to change behaviour is load spent for nothing.
