---
title: Collaborative Domain Modeling
category: domain-modeling
summary: Interactive, play-based techniques (event storming, CRC modeling, event modeling) for building a shared domain model and ubiquitous language across engineers and business stakeholders — the recommended first step when modernizing a legacy system.
tags: [technique, event-storming, crc-modeling, event-modeling, ubiquitous-language, domain-modeling, tdd-kata, cosmic-python]
sources: [web-page-cosmic-python-book]
created: 2026-07-26
updated: 2026-07-26
---

# Collaborative Domain Modeling

Before restructuring code, Cosmic Python recommends **domain modeling as the first step** when carving a new system out of a big ball of mud (raw L6845). The rationale is a communication breakdown: "In many overgrown systems, the engineers, product owners, and customers no longer speak the same language. Business stakeholders speak about the system in abstract, process-focused terms, while developers are forced to speak about the system as it physically exists in its wild and chaotic state." (raw L6846)

## The techniques

Modeling is done collaboratively and interactively "because humans are good at collaborating through play" (raw L6852). Named techniques:

- **Event storming** — a workshop mapping a business process out of its domain events (see eventstorming.com).
- **CRC modeling** — Class-Responsibility-Collaborator card modeling.
- **Event modeling** — "another technique that brings engineers and product owners together to understand a system in terms of commands, queries, and events" (raw L6854) (see eventmodeling.org).

## The goal: a shared ubiquitous language

The output that matters is not a diagram but agreement: "The goal is to be able to talk about the system by using the same [[ubiquitous-language|ubiquitous language]], so that you can agree on where the complexity lies." (raw L6860) Locating the complexity is what tells you where your core subdomain and [[aggregate]] boundaries should fall.

## Demonstrating value cheaply

Modeling can be started as a low-risk experiment: "We've found a lot of value in treating domain problems as TDD kata." (raw L6862) The availability service's first code was just its batch/order-line model, done as "a lunchtime workshop, or as a spike at the beginning of a project." Once modeling demonstrably delivers value, "it's easier to make the argument for structuring the project to optimize for modeling" (raw L6862) — and, per the [[strangler-fig-pattern]], to grow that model into a new [[bounded-context]].

## Related

- [[ubiquitous-language]] — the shared language modeling produces.
- [[refactoring-toward-ddd]] — the in-place modernization this precedes.
- [[strangler-fig-pattern]] — growing the modeled context into a replacement system.
- [[aggregate]] — the boundaries the model reveals once complexity is located.
