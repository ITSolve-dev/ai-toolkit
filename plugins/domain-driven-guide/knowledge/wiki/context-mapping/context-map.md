---
title: Context Map
category: context-mapping
summary: A diagram (and ultimately the integration source code) showing how the Bounded Contexts in a solution relate to one another — the solution-space assessment every DDD project should draw first.
tags: [practice, context-mapping, bounded-context, integration, solution-space]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

A **Context Map** is the tool that makes the *relationships between* [[bounded-context]]s visible. It
can be expressed two ways: the easy way is a simple diagram of the mappings between two or more existing
Bounded Contexts; the more detailed way is the actual source-code implementations of those
integrations. "The drawing illustrates how the actual software Bounded Contexts in the solution space
are related to one another through integration." (raw L2379)

Where [[subdomain]] analysis is a *problem-space* assessment, the Context Map is the **solution-space
assessment** (raw L2381) — see [[problem-space-and-solution-space]]. It captures the software as it is
actually built and integrated.

## Why it is essential

When you start a DDD effort, "first draw a visual Context Map of your *current project situation*" (raw
L2395) — the current Bounded Contexts and the integration relationships between them. The map is drawn
primarily to give *your* team the solution-space perspective; other teams should draw their own (raw
L2401).

Beyond an inventory of systems you must interact with, the map is a **catalyst for inter-team
communication** (raw L2413). Its greatest value is forcing you to think carefully about every project
you depend on. The classic cautionary tale: your team assumes a [[customer-supplier-development]]
relationship with a legacy team, but that team, providing only what they already have, silently forces
you into a [[conformist]] relationship — a mismatch that, discovered late, can delay or sink delivery
(raw L2415). Drawing the map early surfaces that risk.

## How to draw one

- **Map the existing terrain, not the imagined future.** "First, you should map the present, not the
  imagined future." (raw L2427) Update it as the landscape changes.
- **Keep it informal.** Hand-drawn whiteboards rule; if you use a tool, keep it informal (raw
  L2429–2431).
- Show at a high level where the boundaries are, the relationships between them and their teams, the
  kinds of integrations, and the necessary translations (raw L2437).
- When useful, zoom in and add **Modules**, significant [[aggregate]]s, team allocation, and the
  [[upstream-downstream]] direction (raw L2441).
- Post it prominently; add strategic insight as conversations reveal it.

## What it is not

"A Context Map is *not* an Enterprise Architecture or system topology diagram." (raw L2447) It conveys
interacting models and DDD organizational patterns. It can still expose architectural deficiencies
(integration bottlenecks) and sticky governance issues that other methods hide (raw L2449).

## The patterns a map is labelled with

Each relationship end is labelled with the pattern in play. Vernon groups them into **organizational /
team relationships** and **integration techniques**, commonly abbreviated on the connectors:

- **[[partnership]]** — two contexts succeed or fail together.
- **[[shared-kernel]]** — two teams intentionally share a small subset of the model.
- **[[customer-supplier-development]]** — the cooperative [[upstream-downstream]] relationship.
- **[[conformist]]** — the downstream team adopts the upstream model wholesale.
- **[[anticorruption-layer]]** (ACL) — a downstream translation/isolation layer.
- **[[open-host-service]]** (OHS) — an upstream published protocol.
- **[[published-language]]** (PL) — the shared vocabulary exchanged over it.
- **[[separate-ways]]** — no integration at all.
- **[[big-ball-of-mud]]** — a boundary drawn around a legacy tangle.

(raw L2503–2509) SaaSOvation used the *Segregated Core* refactoring
([[blending-models-in-one-context]]) to reach clean boundaries once it recognized that security, users,
and permissions did not belong inside its Collaboration Core Domain (raw L2531, L2541). Where a
downstream context must stay usable even when an upstream one is down, the implementation choices are
governed by [[bounded-context-autonomy]].

## Trade-offs and failure modes

The governing tension is **simplicity vs. ceremony**: "The more ceremony you add, the fewer people will
want to use the Map." (raw L2443) A map uploaded to a wiki "where information goes to die" is worthless —
maps stay "hidden in plain sight unless the team pays regular attention to them" (raw L2457). You are
unlikely to keep a highly detailed map current far into a project (raw L2787); the enduring value is
what can be posted on a wall and pointed at during discussion.

## Related

- [[bounded-context]] — the nodes the map connects.
- [[upstream-downstream]] — the directional axis drawn on each relationship.
- [[problem-space-and-solution-space]] — the problem-space counterpart to this solution-space view.
- The relationship/integration patterns listed above.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
