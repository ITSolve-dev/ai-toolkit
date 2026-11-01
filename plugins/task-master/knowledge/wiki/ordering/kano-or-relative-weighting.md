---
title: Kano or Relative Weighting
category: ordering
summary: The source offers both and leaves the choice to the reader; this wiki resolves it by setting. Filter hard constraints first, use Kano where users can be reached and the question is what kind of need a feature meets, use relative weighting to rank what remains by value per cost, and use neither alone where urgency differs.
tags: [decision-rule, ordering, prioritization, value, kano]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Kano or Relative Weighting

The chapter presents two ways to judge desirability and leaves the choice open, asking only what the relative merits are in the reader's organization ([[cohn-agile-estimating-planning]] L2565). The charter requires a disagreement to be resolved per setting, so **everything in the resolution below is this wiki's reading of sourced positions.** The two methods also answer different questions, so in most settings they are steps and not rivals.

## How they differ

| | [[kano-questionnaire]] | [[relative-weighting]] |
|---|---|---|
| Evidence | Users' answers; the fallback is an educated guess (L2423) | "expert judgment" (L2510) |
| Result | A category | A number per feature |
| Sees presence and absence | Yes | Yes, as benefit and [[relative-penalty]] |
| Sees cost | No | Yes |
| Treats a must-have as | Required, whatever else is on offer ([[ordering-by-kano-category]]) | One high score among others |
| Needs | Reachable users, about 20-30 by the source's figure | Judges and an estimate per feature |

The row on must-haves is the real disagreement. Kano's tiers are non-compensatory: no amount of linear value replaces a threshold feature. Relative weighting is compensatory: a low ratio simply ranks low. The compliance feature on [[relative-penalty]] shows the gap.

## The rule

1. **Filter first.** A feature whose absence cannot be accepted is taken out of the ranking and placed by constraint. This applies whichever method follows, and it holds even where no survey is possible.
2. **If users can be reached and what you lack is knowledge of their reaction,** classify by Kano. This fits a new product or a [[theme]] whose users' reaction nobody on the project can predict.
3. **If users cannot be reached, or the people steering already know the domain,** use relative weighting, or a classification by educated guess, stated as a guess.
4. **Within what remains, rank by value per cost** using relative weighting. Kano cannot rank within a category.
5. **If tasks differ in what waiting does to them, neither method suffices.** Use [[ordering-by-value-and-urgency]], with [[cost-of-delay-over-duration]] inside a rank. Neither of the two instruments here has a term for urgency.

Dependencies constrain any result ([[sequence-versus-wait]]).

## Per project setup

| Setup | Holds |
|---|---|
| A release or milestone with a scope to choose, and users to ask | Kano for membership, then relative weighting inside the linear tier |
| A release or milestone with a scope to choose, and no users to ask | Filter, then relative weighting |
| Continuous flow with a queue of mixed requests | [[ordering-by-value-and-urgency]]; the absence question goes into the value band, and Kano adds little without a release to gate |
| Internal tool with its users among the people steering | A survey has no population. Ask them directly and use relative weighting |

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Is there an unacceptable absence? | The request and the person steering ([[relative-penalty]]) |
| Can users be reached, and how many? | The person steering; the project setup |
| Is the scope being chosen for a date or milestone? | The board's setup: periods, milestones, or flow |
| Do the tasks differ in urgency? | [[urgent-versus-important]] |

The choice of method was wrong in these ways, all this wiki's:

- **Weighting was used where Kano was needed:** a high-ranked feature shipped and users were indifferent, or a low-ranked one turned out to be mandatory for them.
- **Kano was used where it was not needed:** the survey cost a round of waiting and changed nothing in the plan.
- **The filter was too wide:** most of the list counted as unacceptable to omit, and the ranking stopped deciding anything. That is [[priority-inflation]] under a different name.

## Cost

Doing both means two sets of judgement for one decision. The filter in step 1 can be abused, since it removes a task from all comparison, and only a person who owns the loss should apply it. The setups table has not been tested on a real project.

## Agent executor note

The plugin knows the project setup and can pick the branch. The judgements inside the branch stay with the people steering. Asking them for a full table per task would spend the budget [[clarifying-questions]] protects, so this wiki reads step 3's cheaper path as the default for a few people, with Kano reserved for the case where they say they do not know how users will react.
