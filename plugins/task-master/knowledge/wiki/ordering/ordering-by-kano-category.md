---
title: Ordering by Kano Category
category: ordering
summary: Within a release, schedule all must-haves, then as many linear features as fit, then a few exciters picked with cost in view, and no indifferent ones, deciding scope before asking how long it takes; a must-have constrains what is in the release and not when it is built, past a base level more of it buys little, and a category is an input that a stated reason can override.
tags: [decision-rule, ordering, prioritization, value, kano, release]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
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

## Worked walk through a release

The fictional case study in Chapter 23 (L4961) assembles a release scope by walking the categories in order with points in view, and divides by velocity only afterwards. Scope is decided first: "I have no idea yet. Let’s figure out what you want and then we can see how long it will take," (L6129-L6131). The figures are illustrations.

| Step | Available | Taken | Running total |
|---|---|---|---|
| Mandatory by judgement | 32 | 32 | 32 |
| Mandatory by survey | 56 | 56 | 88 |
| Linear | 32 | 32 | 120 |
| Exciters | 20 | 12 | 132 |
| Indifferent | 6 | 0 | 132 |

The table sums L6012, L6038, L6070, L6086, L6101 and L6145. The reasoning at each step:

- **Mandatory:** all in (L6111-L6113).
- **Linear:** by judgement of how much is enough. The product manager takes all of them, including a cheap one on cost alone: "Maybe the user can’t change songs but that’s only 1 point so for now I’m going to say we want it." (L6117).
- **Exciters:** a couple, weighed by cost. A programmer reminds the room of the bad-move warning, "Remember, that’s an 8-point story," and "I can enhance it to find really bad moves but it’s not trivial." (L6135). The product manager drops it and keeps the 3-point warning that blocks a losing move (L6139).
- **Indifferent:** out. "We’re unlikely to sell more games or games at a higher price from adding features that players are indifferent about." (L6090).

### A category is an input and not a verdict

The analyst overrides the data twice and says why. A strong opponent goes in as mandatory because "I think many users will outgrow what you’re defining as the medium-strength engine." (L6020). Playing another human scored 58 indifferent (L5954) and goes in anyway: "I’ve included that as mandatory because we’ve already said it’s a good milestone." (L6044). This wiki reads the second as a sequencing reason legitimately outranking a value reading, and the stated reason as what marks an override as sound. Annotated saved games, with a mandatory and indifferent split much like the strong opponent's (L5962), is left out with no reason stated, and the source does not say why the two were treated differently.

### Failure mode: everything is in

The product manager says it himself: "I know. I want it all, right? Just like every product manager in the world." (L6121). The sign is that nothing, or almost nothing, sits below the line. This wiki notes that in the case 132 of 146 points are in, so only 14 lie outside, which leaves little to cut if velocity runs to the long end, and the cut would come from linear features already selected. The range and its lever are on [[stating-plan-uncertainty]], and the first figure for velocity on [[planned-velocity]].

## Signs this rule detects

- **A must-have outside the plan.** A theme classed as must-have has no task in the release, or its tasks are open as the release date comes up. Read this from board state.
- **Gold-plating a threshold feature.** A task deepens a must-have that already has base-level support, while linear features wait. The sign is in the task's text: a further level or further options of something users already take for granted.
- **Exciters ahead of must-haves.** The plan contains exciters while a must-have is unscheduled.
- **An override with no reason.** A theme sits in a tier its category does not give it, and nothing says why.

These signs are this wiki's application. A sign raises a question: the category may be stale ([[kano-model]]) or wrong.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Each theme's category | [[kano-questionnaire]], or a guess a person confirms, with its origin stated |
| Each task's size | Its estimate on the project's scale |
| Which tasks belong to which theme | Each task's stated purpose ([[task-must-justify-itself]]) |
| What base-level support means for this feature | The person steering, or the acceptance criteria ([[testable-acceptance]]) |
| Whether the product is bloated | The person steering; the source gives no measure |
| What fits | The release's capacity ([[fitting-stories-into-a-release]]) |

The source gives no tests of the choice, so these are this wiki's.

- **A must-have was overrated** if the release went out without it, or with a partial version, and users did not object.
- **A must-have was missed** if users rejected or avoided the release over something classed lower.
- **Depth was misjudged** if complaints after release name the limit of a partial must-have.
- **A category had gone stale** if users object to the absence of something recorded as an exciter.
- **The scope was too full** if observed velocity projects past the stated range ([[stating-plan-uncertainty]]), or a newly found exciter forces an extension or an equal removal (L6183).

## Setting

The rule assumes a release with an edge. With periods or milestones on the board it reads directly: must-haves gate the milestone. In continuous flow with no release, this wiki has no source for the gate, and reads it as the next point at which users receive the product. The tiers still rank, and nothing marks when the must-have tier has to be complete.

## Cost

Chapter 11's rule ignores cost within and across tiers, so a costly must-have outranks a cheap linear feature whatever the return ([[relative-weighting]] sees that and this rule does not). The case study weighs cost by hand inside the linear and exciter tiers, as above, and not across them. It also needs a category per theme, which is a survey or a guess. Holding all exciters to "time permitting" risks shipping none, and the source guards against that only with "at least a few".

## Agent executor note

The tiers concern users and survive. This wiki expects the gold-plating sign to matter more with an agent, because adding more is cheap for the executor while the people steering still have to review it. That extension is unmeasured.
