---
title: Sizing a Bounded Context
category: context-mapping
summary: Right-size a Bounded Context so it expresses its complete Ubiquitous Language — neither more nor less — and resist architectural or staffing pressures that produce wrong-sized contexts.
tags: [heuristic, decision-rule, bounded-context, ubiquitous-language, modules, failure-mode]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

Asked how many **Modules**, [[aggregate]]s, [[domain-event]]s, and **Domain Services** a Bounded
Context should hold, Vernon answers: "That's a bit like asking, 'How long is a piece of string?' A
[[bounded-context]] should be as big as it needs to be in order to fully express its complete
[[ubiquitous-language]]." (raw L2047) The invariant that sets the size is **linguistic completeness**,
not any technical or organizational metric.

The governing image is the *Amadeus* line: "There are just as many notes as I required, neither more
nor less." (raw L2053) A model should have "the unmistakable sound of completeness, purity, power" —
the number of building blocks inside "neither more nor less than what the correct design requires" (raw
L2061).

## The rule: driven by language, both ways

- **Factor out extraneous concepts.** "If a concept is not in your Ubiquitous Language, it should not
  be introduced in your model in the first place." (raw L2049) Strays usually belong in a separate
  Supporting or Generic [[subdomain]], or in no model at all.
- **But don't over-prune.** "Be careful not to mistakenly factor out concepts that do truly belong in
  the [[core-domain]]." (raw L2051) Too-stringent constraint leaves "gaping holes… from vital but
  missing contextual concepts" (raw L2061). Good judgment is required; a [[context-map]] helps shape
  it.

## Failure modes — wrong-sized contexts

1. **Too small / miniaturized by architecture.** Letting a platform, framework, or packaging
   convention decide the boundary treats it "as technical rather than linguistic" (raw L2063).
2. **Boundaries drawn to distribute tasks.** Splitting contexts so developers get smaller chunks "plays
   false to the linguistic motivations of contextual modeling" and fragments the Language (raw L2065).
   Use **Modules** — not fake contexts — to divide developer responsibilities (raw L2071).
3. **Too big / muddy.** Piling on concepts that don't express the core problem "muddy the waters so
   much that we will fail to observe… what is essential" (raw L2061). This slides toward
   [[blending-models-in-one-context]] and a [[big-ball-of-mud]].

The test question is always: "What does the Language of the domain experts indicate about the real
contextual boundaries?" (raw L2067) And the standing caution: "Don't be too quick to miniaturize them."
(raw L2083)

## Modules relieve the pressure to split

Many apparent reasons to split a context are really deployment or task-management concerns that
**Modules** solve better. The SaaSOvation *Collaboration Context* could have become ten contexts — one
per facility (Forum, Calendar, …) — since the facilities were largely uncoupled and each was a natural
deployment unit. Producing ten domain models was unnecessary and would "work against the modeling
principles of the Ubiquitous Language" (raw L2283). Instead the team **kept one model** and shipped a
**separate JAR per facility** (plus one for shared objects like `Tenant`, `Moderator`, `Author`),
meeting deployment goals while keeping a unified Language (raw L2285).

## Related

- [[bounded-context]] — the boundary being sized.
- [[ubiquitous-language]] — the completeness criterion that sets the size.
- [[subdomain]], [[core-domain]] — where factored-out concepts belong.
- [[blending-models-in-one-context]], [[big-ball-of-mud]] — the over-sized failure modes.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
