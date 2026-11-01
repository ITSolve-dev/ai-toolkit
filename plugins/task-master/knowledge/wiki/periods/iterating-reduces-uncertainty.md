---
title: Iterating Reduces Uncertainty
category: periods
summary: Uncertainty about what to build and about how to build it are both reduced by iterating; show working results to users, and feed what is learned back into the plan. A plan that never changes across cycles is not getting the benefit.
tags: [rule, iterations, uncertainty, replanning]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Iterating Reduces Uncertainty

Cohn separates two uncertainties a plan ignores and treats iteration as the remedy for both. About the product, "We assume that users will not change their minds, refine their opinions, or come up with new needs during the period covered by the plan." ([[cohn-agile-estimating-planning]] L658). About the build, we assume precision we do not have and cannot "hope to identify every activity" (L660).

> The best way of dealing with uncertainty is to iterate.
>
> — [[cohn-agile-estimating-planning]], L664

Cohn says each uncertainty is reduced by a different action, and this wiki keeps them apart because they fail separately.

| Uncertainty | What reduces it | What happens if it is ignored |
|---|---|---|
| What the product should be | "work in short iterations and show (or, ideally, give) working software to users every few weeks" (L664) | A project finishes on schedule without capabilities identified after the plan was made (L680) |
| How to build it | "missing tasks can be added to plans, bad estimates can be corrected, and so on" (L664) | Missed activities, then lateness, dropped features or poor quality trade-offs (L680) |

Cohn's phrase for the effect is that "the focus shifts from the plan to the planning." (L664). See [[agile-planning]]. Chapter 9 names the two end uncertainty and means uncertainty, and uses them for ordering; see [[end-and-means-uncertainty]] and [[ordering-for-early-user-feedback]].

## The rule

At the end of each cycle, do both: put a working result in front of the people it is for, and change the plan on what was learned. Doing one alone leaves the other uncertainty in place. The pairing as a rule is this wiki's reading of Cohn's two sentences.

## Sign of violation

- **In board history:** across several cycles, no task was added, removed or re-estimated, and only states changed. The plan has not learned anything, or what was learned has not been written down.
- **In board history:** cycles close with tasks finished and no result shown to anyone outside the team.
- **In the plan:** a complete specification treated as settled, with no place for what users say later.

These signs are this wiki's derivation from Cohn's claims. A board that does not change is a question and not a verdict: stable, well-understood work may need no changes.

## Why

What breaks is correction. This wiki reads the consequence as a plan whose errors, without a cycle that returns information, stay until the end of the work, when there is the least room to deal with them.

## Cost

This wiki notes that showing a result every cycle costs preparation and the attention of those who look at it, and that a changing plan makes earlier forecasts stale, which [[mid-period-change]] has to manage.

## Which setup this applies under

Cohn writes about fixed iterations. This wiki reads the mechanism as a loop of showing and replanning, which an iteration setup runs at each period's end ([[period-length]]). Under a flow setup there is no period, so the loop has to be attached to something else, most naturally each presented result. That transfer is this wiki's, and this chapter does not address it.

## Agent executor note

Uncertainty about the product sits with users and does not change with the executor. Uncertainty about the build survives, and this wiki notes that an agent's guess can hide it: a finished result does not show which assumptions were made ([[agent-silence-is-not-completeness]]). Cohn's "every few weeks" reflects human pace and has no evidence behind it for an agent-run project, so this wiki sets no cadence from it. The limiting factor is likely what the people steering and the users can take in.
