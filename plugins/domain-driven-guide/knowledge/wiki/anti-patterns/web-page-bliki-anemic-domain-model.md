---
title: "Source Summary — Fowler: Anemic Domain Model"
category: anti-patterns
summary: Martin Fowler's 2003 bliki essay naming the Anemic Domain Model anti-pattern; distilled in full into the anemic-domain-model page.
tags: [summary, anti-pattern, domain-model, fowler]
sources: [web-page-bliki-anemic-domain-model]
created: 2026-07-25
updated: 2026-07-25
---

**Source:** Martin Fowler, *"Anemic Domain Model"* (bliki, 25 November 2003). Origin:
<https://martinfowler.com/bliki/AnemicDomainModel.html>. Raw extraction:
`raw/web-page-bliki-anemic-domain-model.md`.

## What it is

A short, canonical essay naming and arguing against the **Anemic Domain Model** — a model with
domain-shaped objects that hold data but no behaviour, all logic having been drained into service
objects. Fowler wrote it after noticing, with Eric Evans, that the anti-pattern was spreading; it
remains the reference statement people cite for it.

## Relevance verdict — fully in scope

The wiki's `SCHEMA.md` charter names anemic domain models explicitly as an in-scope **failure
mode**. The essay is squarely on-charter and was distilled in full into [[anemic-domain-model]]:
the symptom (behaviour-free bags of getters/setters), the core argument (all the cost of a domain
model, none of the benefit → Transaction Scripts in disguise), the layering distinction that is
*not* the anti-pattern (thin Application/Service Layer over a behaviour-rich Domain Layer, with
Evans' own layer definitions), why it is common (data-background habits, Entity Beans), and the
punchline test ("if all your logic is in services, you've robbed yourself blind").

Nothing was dropped as out of scope — the whole essay is on-topic. Outbound links in the raw
source to Fowler's *P of EAA* catalogue entries (Transaction Script, Service Layer, POJO, Domain
Model) are referenced but not given their own pages: they are general enterprise-architecture
patterns, not DDD tactical/strategic patterns per this charter.

## How to read it

Authoritative and enduring. It is a *position* essay, not a how-to: it diagnoses the failure and
draws the layering boundary, but the constructive "what to do instead" is carried by the
behaviour-rich building blocks — see [[value-object]], [[entity]], [[aggregate]]. The
present-day [[web-page-ddd-guide-2026]] independently restates the same warning, which is recorded
as corroboration on [[anemic-domain-model]].

## Reader discussion

Not fetched — Fowler's bliki carries no reader comment thread on this page.
