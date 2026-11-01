---
title: Choosing a Buffer
category: periods
summary: Buffer only when uncertainty or the cost of being wrong about a date is high, match the buffer's unit to what is uncertain (time for schedule, features for scope), combine them where both are firm-ish, and skip buffers when no precise date and scope are needed.
tags: [decision-rule, planning-a-date, buffer, uncertainty, setup-dependent]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Choosing a Buffer

Whether to buffer a plan, and with what, follows from two questions: what is firm, and what is it worth to be wrong. Cohn treats buffering as risk management: useful "In cases where there is significant uncertainty or the cost of being wrong is significant" ([[cohn-agile-estimating-planning]] L3843), and otherwise not worth doing.

## When to buffer

The source names these situations (L3821-L3829, L4061):

- planned far in advance
- a firm deadline with a reasonably firm set of functionality
- contracted from one organization to another
- requirements understood only superficially
- significant cost, financial or otherwise, of being wrong about a date

Each brings either more uncertainty or heavier consequences (L3831). Conversely, where "a precise deadline with a precise set of delivered functionality is not needed" and the team simply delivers as fast as it can over a sustained period, "don’t take on the small extra work of adding buffers to your project" (L4053).

## Which buffer: match the unit

The rule is "we buffer feature uncertainty with features and schedule uncertainty with time" (L4020). Cohn's shoulder belts and air bags make the point that different buffers cover different collisions (L4016). This wiki resolves the choice by project setup; the first three rows follow Figure 17.5 (L4022), and the setup column is ours.

| Setup | Buffer | Why |
|---|---|---|
| Scope fixed, date may move | None needed for the date, or a larger [[schedule-buffer]] if a date is promised anyway | Figure 17.5(a): delivers when the set is done |
| Date fixed, scope open | [[feature-buffer]] | Figure 17.5(b): the date holds, contents vary |
| Date and core scope both firm | Both, each smaller | Figure 17.5(c) |
| Neither precise, continuous delivery | None | The caveat at L4053 |

Combining is usually the better answer: "this is usually a good idea as it allows the size of each to be smaller" (L4067).

When one constraint cannot flex, the load moves. "When we cannot buffer a constraint appropriately, we are forced to increase the size of other buffers" (L4045). Guaranteed functionality means a larger schedule buffer. This wiki reads the mirror case as following: a date with no room means a larger feature buffer.

## Inputs and the fact that would show the choice wrong

- **Firmness of date and of scope:** from the person who owns them; a board does not show this, and it is the setup decision the plugin must ask about ([[date-driven-vs-feature-driven]]). That a date is written down does not make it firm: see [[a-date-is-not-urgency]].
- **Size of the plan:** at least ten items for a formula-sized buffer ([[project-buffer-sizing]]). Below that, the source advises against buffering at all (L4010).
- **Uncertainty:** the spread between items' 50% and 90% estimates ([[completion-time-distribution]]).

This wiki reads these as the disproving facts. A buffer was unnecessary if the date slipped with no consequence, or if the same buffer goes untouched across several plans. It was the wrong kind if the date was met by dropping work that turned out to be mandatory, or if time ran out with optional items already built.

## Scale

The budget or personnel buffer the chapter also describes (L4031-L4035) is dropped from this wiki: Cohn himself says it is seen less on small projects, and "It is difficult to buffer anything in small numbers" (L4035). This wiki reads the ten-item floor as meaning that for a few people, buffers belong to a release-sized plan and not to a handful of tasks.
