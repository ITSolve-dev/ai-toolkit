---
title: Ordering by Kano Category
category: ordering
summary: Within a release, schedule all must-haves, then as many linear features as fit, then a few exciters; a must-have constrains what is in the release and not when it is built, and past a base level more of it buys little.
tags: [decision-rule, ordering, prioritization, value, kano, release]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Ordering by Kano Category

This rule chooses what goes into a release from the categories of the [[kano-model]]. It gives three tiers of emphasis, and this wiki reads it as a rule about what belongs in the release rather than a sequence of work.

## The rule

1. **All threshold features.** "emphasis should be placed on prioritizing the development of all threshold features" ([[cohn-agile-estimating-planning]] L2413), because must-haves are "required for a product to even play in its market segment" (L2413).
2. **As many linear features as fit.** "Secondary emphasis should be placed on completing as many linear features as possible." (L2415), since each adds satisfaction directly. The source's exception: "(Excluding, of course, such situations as a product that is already bloated with too many features.)" (L2415).
3. **A few exciters.** "Finally and with time permitting, at least a few delighters should be prioritized such that they are included in the release plan." (L2415).

## Must-have does not mean first

This is the discriminating criterion of the page:

> A product’s must-have features do not need to be developed in the first iterations of a release. However, since users consider these features as mandatory, they need to be available before the product is released.
>
> — [[cohn-agile-estimating-planning]], L2413

This wiki reads a must-have as a constraint on membership of the release and not on position within it. The position is left to other factors, and the chapter's own summary lists learning and risk among them (L2547-L2555). A task's place in the queue should not be read off its category, and calling a feature a must-have says nothing on [[urgent-versus-important]]: it is a statement of importance only.

## How much of a must-have

The tier asks for presence and not excellence: "partial implementation of must-have features may be adequate since gains in customer satisfaction drop off quickly after a base level of support for threshold features has been established" (L2413). The source's example is one level of undo in FrameMaker: "For me personally they moved pretty far up the customer satisfaction axis with a one-level undo feature, yet I would have preferred much more." (L2413). This wiki reads that as one user's report and not a measurement, and the author's closing clause as a reminder that adequate is not the same as satisfying.

The mirror case for exciters comes from the model: even a partial implementation raises satisfaction sharply (L2400). This wiki reads both as arguments for cutting small in these two tiers ([[vertical-slice]]), and for spending the depth on the linear tier, which is the only one where more keeps paying.

## Signs this rule detects

- **A must-have outside the plan.** A theme classed as must-have has no task in the release, or its tasks are open as the release date comes up. Read this from board state.
- **Gold-plating a threshold feature.** A task deepens a must-have that already has base-level support, while linear features wait. The sign is in the task's text: a further level or further options of something users already take for granted.
- **Exciters ahead of must-haves.** The plan contains exciters while a must-have is unscheduled.

These signs are this wiki's application. A sign raises a question: the category may be stale ([[kano-model]]) or wrong.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Each theme's category | [[kano-questionnaire]], or a guess a person confirms, with its origin stated |
| Which tasks belong to which theme | Each task's stated purpose ([[task-must-justify-itself]]) |
| What base-level support means for this feature | The person steering, or the acceptance criteria ([[testable-acceptance]]) |
| Whether the product is bloated | The person steering; the source gives no measure |
| What fits | The release's capacity ([[fitting-stories-into-a-release]]) |

The source gives no tests of the choice, so these are this wiki's.

- **A must-have was overrated** if the release went out without it, or with a partial version, and users did not object.
- **A must-have was missed** if users rejected or avoided the release over something classed lower.
- **Depth was misjudged** if complaints after release name the limit of a partial must-have.
- **A category had gone stale** if users object to the absence of something recorded as an exciter.

## Setting

The rule assumes a release with an edge. With periods or milestones on the board it reads directly: must-haves gate the milestone. In continuous flow with no release, this wiki has no source for the gate, and reads it as the next point at which users receive the product. The tiers still rank, and nothing marks when the must-have tier has to be complete.

## Cost

The rule ignores cost within and across tiers, so a costly must-have outranks a cheap linear feature whatever the return ([[relative-weighting]] sees that and this rule does not). It also needs a category per theme, which is a survey or a guess. Holding all exciters to "time permitting" risks shipping none, and the source guards against that only with "at least a few".

## Agent executor note

The tiers concern users and survive. This wiki expects the gold-plating sign to matter more with an agent, because adding more is cheap for the executor while the people steering still have to review it. That extension is unmeasured.
