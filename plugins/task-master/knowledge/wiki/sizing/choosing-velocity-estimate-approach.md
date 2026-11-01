---
title: Choosing How to Estimate Velocity
category: sizing
summary: Prefer observed iterations, then actuals from a related project by the same team, then a see-what-fits forecast; replace whatever was used with observed values as soon as they exist.
tags: [decision-rule, velocity, release-planning, iterations]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Choosing How to Estimate Velocity

Three sources can supply a [[velocity]] estimate, and they are ranked, not interchangeable. Cohn notes that "Circumstances often guide you and constrain your options" ([[cohn-agile-estimating-planning]] L3785) and gives the order of desirability (L3787-L3791):

1. Run one or more iterations before giving the number, if at all possible. "There’s no estimate like an actual and seeing the team’s actual velocity is always your best choice" (L3787).
2. Use the actual velocity from a related project by this team.
3. Estimate by seeing what fits.

The chapter presents historical values first (L3590-L3596), but that is section order; the ranking above is what governs.

## Inputs and where they come from

| Input | Read from | Effect |
|---|---|---|
| Can an iteration finish before the number is due? | The date the estimate is demanded, against iteration length and project start | Yes: [[run-iterations-to-observe-velocity]] |
| Does this team have actuals from related work? | Board history of the earlier project | Yes: test it with [[historical-velocity-comparability]] |
| Does the project exist yet? | Whether it is funded, contracted and staffed | No: [[forecast-velocity-by-what-fits]] |

The forecast path is for cases where running iterations is impossible or pointless: a project starting in twelve months, one that starts only if a client signs (L3684), or a team that does not exist yet (L3779). Cohn says "Forecasting velocity is rarely your first option" (L3686). When a project has started and a schedule is wanted before its first iteration ends, the fallback is [[planned-velocity]].

## What later fact shows the choice wrong

The first observed iterations land outside the stated [[velocity-estimate-range]]. This wiki reads that as pointing to one of three things: history that was not comparable, a forecast sample that was not representative, or a range that was too narrow.

## Replace it with actuals

The choice is temporary whichever way it goes: "Regardless of which approach you use, switch to using actual, observed values for velocity as soon as possible" (L3793). Cohn's example is a see-what-fits estimate given six months ahead for a rough answer, replaced by measured velocity once the project starts (L3793-L3797). How often a plan is then recomputed is on [[updating-the-release-plan]].

## Sign of violation

Board history shows completed iterations, while the plan's dates are still computed from the pre-project forecast or from a previous project's mean. This sign is this wiki's, and it raises a question: check whether the plan was recomputed and simply kept the same figure.

## Agent executor note

The transfer here is ours. The ranking rests on observation beating prediction, which does not depend on who executes, so it survives. An iteration may also be cheaper to run than it was for the teams Cohn describes, which would push the first option further forward, but this source says nothing on that and the plugin should not assume it.
