---
title: Replanning on New Knowledge
category: reading-history
summary: A plan is a point-in-time guess; at each iteration start, what was learned about progress and about value is folded in, and a release plan resting on outdated information or false assumptions is updated, while priorities stay relatively stable between iterations.
tags: [rule, retrospective-analysis, plan-versus-fact, learning, release]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Replanning on New Knowledge

Replanning on new knowledge is the practice of treating a plan as an estimate that the project's own output keeps correcting, updated at regular points. Cohn's premise is that the plan "is not a guarantee of what will occur. In fact, it is only a point-in-time guess." ([[cohn-agile-estimating-planning]] L794). His phrase for a plan is "one view of the future but many views are possible." (L722). He treats revision as the condition for a plan staying useful: "An agile estimating and planning process recognizes that our knowledge is always incomplete and requires that plans be revised as we learn." (L4843).

## The rule

At the start of each iteration, check whether the release plan still holds, and change it if it does not.

> Take advantage of the start of each new iteration to assess the relevancy of the current release plan. If the release plan is based on outdated information or on assumptions that are now false, update it.
>
> — [[cohn-agile-estimating-planning]], L4919

How often this may stretch is on [[updating-the-release-plan]].

## What a project produces

Cohn says projects should be viewed "as rapidly and reliably generating a flow of useful new capabilities and new knowledge rather than as just the execution of a series of steps." (L894). He splits the knowledge into two kinds (L812):

- **Product knowledge:** what the product should be.
- **Project knowledge:** "information about the team, the technologies in use, the risks, and so on".

Chapter 22 names the same split by what stays unknown ([[end-and-means-uncertainty]]), and says what each does to a plan:

- **End uncertainty** concerns what is being built: "End uncertainty (about the product ultimately being built) is reduced as product increments are shown to potential users and other stakeholders at the end of each iteration." (L4899). It changes scope, as new features are added to the release plan (L4843).
- **Means uncertainty** concerns how it is built: "Means uncertainty (about how the product will be built) is reduced as the team learns more about the technologies in use and themselves." (L4899). It changes the rate and sometimes the approach (L4929). His example is an early finding that a third-party component cannot meet performance requirements, after which "The time to find and switch to the new component will need to be factored into new plans once the need is identified." (L4905).

The input to a replan is what was observed. Cohn says estimates and plans should rest on "real, observed values" whenever possible (L4935-L4939), and estimating a rate from little evidence is a fallback for when no observations exist (L4935).

## Two things that can be wrong in a plan

Cohn separates what new knowledge corrects (L796-L798):

| What changes | Evidence | Response |
|---|---|---|
| Accuracy | The team "over- or underestimated their rate of progress", or "a certain type of work is more time-consuming than previously thought" | Adjust what the plan expects |
| Value | From seeing the software, the product owner learns users want more of one feature type and less of another | Move "more of the desired features into the release at the expense of some of the lesser-valued features" |

This wiki reads the separation as useful when explaining a gap between plan and fact: slower than expected and wanted something else are different explanations with different fixes. The accuracy row goes through [[velocity]] or [[re-estimate-when-relative-size-changes]]. The value row goes through [[changing-the-plan-without-changing-the-date]].

## When

Cohn says "At the start of each new iteration, an agile team incorporates all new knowledge gained in the preceding iteration and adapts accordingly." (L796). The release plan follows: it "is updated throughout the project (usually at the start of each iteration)" (L837).

## The limit: not ad hoc

Cohn guards the other side: "None of this is to say that agile teams take an ad hoc view of changing priorities. Priorities do tend to be relatively stable from one iteration to the next." (L800). The power he claims is for altering priorities "between iterations" (L800), so this wiki reads the boundary as where this change belongs.

## Failure: planning as if everything were known

> Failing to plan to acquire new knowledge leads to plans built on the assumption that we know everything necessary to create an accurate plan.
>
> — [[cohn-agile-estimating-planning]], L814

Cohn quotes Ward Cunningham as saying "it’s more planning what you want to learn, not what it [the product] will be in the end." (L814).

Chapter 22 states the same failure from the other end: "When we create a plan early in a project and do not update the plan as we acquire new knowledge, we lose the opportunity to synchronize the plan with reality." (L4897). Locking features early also leads to "delivering projects with features that users don’t want" (L4897).

## Signs to check

The source names one process sign: changes are refused, or forced through "an onerous change control process" (L4897). It gives none at board level. This wiki reads the following as questions.

- The plan's expected content is unchanged across several iterations although completed work has fallen short of or passed it. The verdict side of this is on [[plan-conformance-as-success]].
- The rate the plan assumes differs from recent history and nobody has changed it.
- Tasks were added or dropped and the forecast did not move.
- A known discovery, such as a component replaced, has no time against it in the plan.
- A plan contains no item for what the project needs to find out, only for what it will build.
- The opposite failure: the order is reshuffled heavily at every iteration, or during one, with no new evidence named. That is the ad hoc view the source rules out.

## Trade-offs

This wiki notes that replanning costs effort at every boundary and removes the comfort of a stable plan, and that a forecast moving every iteration is harder for others to rely on. It reads the stable-priorities limit as there because a plan that changes without evidence is not more informed, only less usable. A replan that finds nothing to change should say so, confirming the plan and not rewriting it, so a stable forecast stays visibly stable.

Cohn adds a benefit to the planning itself: knowing a plan can be revised "shifts a team’s focus from creating a perfect plan (an impossible goal) to creating a plan that is useful right now." (L4839). This wiki reads that as an argument against spending effort on precision that the next iteration will discard.

## Which setup this applies under

The resolution here is this wiki's. Under an iteration setup, the boundary is the start of the iteration, and a change inside a period is judged on [[mid-period-change]]. Under a flow setup there is no such boundary, so the rule keeps its two parts, a scheduled point for looking again as on [[planning-horizons]] and a named piece of evidence for each change. Reordering unstarted work needs no boundary there, per [[interrupting-started-work]].

## Agent executor note

This wiki reads the rule as surviving an agent executing: it is about the plan, and it can be read from board history. The product side still comes from people seeing the result, so it needs someone to present to. This wiki adds that rates must come from agent-executed work, since an earlier human team's rate says little about it ([[filling-a-period]]).

Learning "how well they are working together" (L4843) is a human matter and falls away. Learning about technologies survives, but an agent does not carry it between runs on its own, so it reaches a replan only if it was written down ([[fact-stranded-outside-the-task]]). That reading is this wiki's.

Related: [[iterating-reduces-uncertainty]], [[timeboxed-iteration]], [[fixed-date-variable-scope]], [[conditions-of-satisfaction]], [[stating-plan-uncertainty]].
