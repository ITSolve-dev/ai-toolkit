---
title: Replanning on New Knowledge
category: reading-history
summary: A plan is a point-in-time guess revised at regular points on observed evidence: each cycle shows a result to reduce product uncertainty and corrects the plan to reduce build uncertainty; a change needs something learned, and the date is one lever among dropping or shrinking scope; the release plan is revisited after each iteration by default, four to six weeks only while velocity is steady and planning brings no surprises.
tags: [rule, retrospective-analysis, plan-versus-fact, learning, release, iterations, uncertainty, replanning, decision-rule, planning, scope]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Replanning on New Knowledge

Replanning on new knowledge is the practice of treating a plan as an estimate that the project's own output keeps correcting, updated at regular points. Cohn's premise is that the plan "is not a guarantee of what will occur. In fact, it is only a point-in-time guess." ([[cohn-agile-estimating-planning]] L794). His phrase for a plan is "one view of the future but many views are possible." (L722). He treats revision as the condition for a plan staying useful: "An agile estimating and planning process recognizes that our knowledge is always incomplete and requires that plans be revised as we learn." (L4843).

## The rule

At the start of each iteration, check whether the release plan still holds, and change it if it does not.

> Take advantage of the start of each new iteration to assess the relevancy of the current release plan. If the release plan is based on outdated information or on assumptions that are now false, update it.
>
> — [[cohn-agile-estimating-planning]], L4919

How often this may stretch is on *Updating the Release Plan* (below).

## What a project produces

Cohn says projects should be viewed "as rapidly and reliably generating a flow of useful new capabilities and new knowledge rather than as just the execution of a series of steps." (L894). He splits the knowledge into two kinds (L812):

- **Product knowledge:** what the product should be.
- **Project knowledge:** "information about the team, the technologies in use, the risks, and so on".

Chapter 22 names the same split by what stays unknown ([[ordering-for-early-user-feedback]]), and says what each does to a plan:

- **End uncertainty** concerns what is being built: "End uncertainty (about the product ultimately being built) is reduced as product increments are shown to potential users and other stakeholders at the end of each iteration." (L4899). It changes scope, as new features are added to the release plan (L4843).
- **Means uncertainty** concerns how it is built: "Means uncertainty (about how the product will be built) is reduced as the team learns more about the technologies in use and themselves." (L4899). It changes the rate and sometimes the approach (L4929). His example is an early finding that a third-party component cannot meet performance requirements, after which "The time to find and switch to the new component will need to be factored into new plans once the need is identified." (L4905).

The input to a replan is what was observed. Cohn says estimates and plans should rest on "real, observed values" whenever possible (L4935-L4939), and estimating a rate from little evidence is a fallback for when no observations exist (L4935).

## Two things that can be wrong in a plan

Cohn separates what new knowledge corrects (L796-L798):

| What changes | Evidence | Response |
|---|---|---|
| Accuracy | The team "over- or underestimated their rate of progress", or "a certain type of work is more time-consuming than previously thought" | Adjust what the plan expects |
| Value | From seeing the software, the product owner learns users want more of one feature type and less of another | Move "more of the desired features into the release at the expense of some of the lesser-valued features" |

This wiki reads the separation as useful when explaining a gap between plan and fact: slower than expected and wanted something else are different explanations with different fixes. The accuracy row goes through [[velocity]] or [[re-estimate-when-relative-size-changes]]. The value row goes through *Changing the Plan Without Changing the Date* (below).

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

- The plan's expected content is unchanged across several iterations although completed work has fallen short of or passed it. The verdict side of this is on [[good-plan-test]].
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

Learning "how well they are working together" (L4843) is a human matter and falls away. Learning about technologies survives, but an agent does not carry it between runs on its own, so it reaches a replan only if it was written down ([[conversation-moves-into-the-task]]). That reading is this wiki's.

Related: [[timeboxed-iteration]], [[fitting-stories-into-a-release]], [[conditions-of-satisfaction]], [[forecast-range-and-probability]], [[adding-scope-to-a-release-plan]], [[velocity-range-forecast]].

## Iterating Reduces Uncertainty

Cohn separates two uncertainties a plan ignores and treats iteration as the remedy for both. About the product, "We assume that users will not change their minds, refine their opinions, or come up with new needs during the period covered by the plan." ([[cohn-agile-estimating-planning]] L658). About the build, we assume precision we do not have and cannot "hope to identify every activity" (L660).

> The best way of dealing with uncertainty is to iterate.
>
> — [[cohn-agile-estimating-planning]], L664

Cohn says each uncertainty is reduced by a different action, and this wiki keeps them apart because they fail separately.

| Uncertainty | What reduces it | What happens if it is ignored |
|---|---|---|
| What the product should be | "work in short iterations and show (or, ideally, give) working software to users every few weeks" (L664) | A project finishes on schedule without capabilities identified after the plan was made (L680) |
| How to build it | "missing tasks can be added to plans, bad estimates can be corrected, and so on" (L664) | Missed activities, then lateness, dropped features or poor quality trade-offs (L680) |

Cohn's phrase for the effect is that "the focus shifts from the plan to the planning." (L664). See [[planning-horizons]]. Chapter 9 names the two end uncertainty and means uncertainty, and uses them for ordering; see [[ordering-for-early-user-feedback]].

### The rule

At the end of each cycle, do both: put a working result in front of the people it is for, and change the plan on what was learned. Doing one alone leaves the other uncertainty in place. The pairing as a rule is this wiki's reading of Cohn's two sentences.

### Sign of violation

- **In board history:** across several cycles, no task was added, removed or re-estimated, and only states changed. The plan has not learned anything, or what was learned has not been written down.
- **In board history:** cycles close with tasks finished and no result shown to anyone outside the team.
- **In the plan:** a complete specification treated as settled, with no place for what users say later.

These signs are this wiki's derivation from Cohn's claims. A board that does not change is a question and not a verdict: stable, well-understood work may need no changes.

### Why

What breaks is correction. This wiki reads the consequence as a plan whose errors, without a cycle that returns information, stay until the end of the work, when there is the least room to deal with them.

### Cost

This wiki notes that showing a result every cycle costs preparation and the attention of those who look at it, and that a changing plan makes earlier forecasts stale, which [[mid-period-change]] has to manage.

### Which setup this applies under

Cohn writes about fixed iterations. This wiki reads the mechanism as a loop of showing and replanning, which an iteration setup runs at each period's end ([[period-length]]). Under a flow setup there is no period, so the loop has to be attached to something else, most naturally each presented result. That transfer is this wiki's, and this chapter does not address it.

### Agent executor note

Uncertainty about the product sits with users and does not change with the executor. Uncertainty about the build survives, and this wiki notes that an agent's guess can hide it: a finished result does not show which assumptions were made ([[agent-silence-is-not-completeness]]). Cohn's "every few weeks" reflects human pace and has no evidence behind it for an agent-run project, so this wiki sets no cadence from it. The limiting factor is likely what the people steering and the users can take in.

## Changing the Plan Without Changing the Date

The rule separates two things that are often merged: revising a plan and moving its date. Cohn:

> Just because we’re changing the plan does not mean we change the dates.
>
> — [[cohn-agile-estimating-planning]], L487

### The decision

**Should the plan change?** Yes, if something was learned; no, otherwise.

> We don’t want to change the plan just for the sake of changing, but we want to change because change means we’ve learned something or that we’ve avoided a mistake.
>
> — [[cohn-agile-estimating-planning]], L483

Cohn's examples of learning are that users want more of one feature or less of another, that usability matters more than believed, and that a new language takes longer than expected (L483). He adds that the financial impact of each can be assessed and, "if worthy," can alter plan and schedule (L483).

**Which lever?** Cohn lists "We can drop a feature, we can reduce the scope of a feature, we can possibly add people to the project, and so on." (L487). Moving the date is one option among these and does not have to come first.

### Inputs and where they are read

This wiki's reading of what the rule needs, since Cohn gives no procedure:

- **What was learned:** a discovery recorded on a task, or a task that took materially more or less than forecast.
- **Whether the date is fixed:** stated by whoever needs the date, in the project's setup or the request.
- **What can be cut:** open tasks ordered by value, per [[prioritization-factors]].

**What later fact would show the choice wrong.** The cut scope is requested again soon after the date, or the date is still missed after the cut.

### Failure signs

These are this wiki's questions to check:

- A date moved with no scope considered: the board's history shows the date changing while the open scope is unchanged.
- Order or scope reshuffled with no stated reason, which is the "for the sake of changing" case.
- Learning recorded with no change to the plan, which is the failure Cohn warns of under [[good-plan-test]].

### Trade-offs

Cutting scope to hold a date costs value, and Cohn's June example shows that sometimes a slightly later date with more features is the better answer (L403). This wiki reads the rule as not favouring dates: it only keeps the date from being the automatic lever. Where the date is the fixed thing from the start, the rule becomes [[fitting-stories-into-a-release]]. Within a running period, [[mid-period-change]] governs what may move. When the learning is a new feature worth having, [[adding-scope-to-a-release-plan]] decides whether it enters.

### Agent executor note

For a few people steering an agent, this wiki reads "add people" as usually unavailable, which makes dropping and reducing scope the practical levers alongside the date. Cohn hedges the lever himself with "possibly" (L487).

## Updating the Release Plan

A release plan ([[planning-horizons]]) is a live document. "The release plan should be revisited and updated with some regular frequency." ([[cohn-agile-estimating-planning]] L2857). Cohn warns against filing it away, and in his summary a plan is not left hanging on a wall to rot (L2973). What the update folds in is on the rule at the top of this page, and the computation is on [[velocity-range-forecast]]. This section holds the cadence.

### The cadence and its conditions

The figure comes with its condition:

> If the development team’s velocity has remained fairly constant and iteration planning hasn’t introduced any big surprises, you may want to go as long as four to six weeks without formally updating the release plan.
>
> — [[cohn-agile-estimating-planning]], L2857

Cohn's default leans shorter: "many projects benefit from establishing a rule that the release plan will be revisited after each iteration" (L2857), and the summary says the plan is usually updated at the start of each iteration (L2973). Chapter 22 states the outer limit in iterations: "The release plan is updated either after each iteration or, at worst, after every few iterations." (L4833). It gives "every few" no number.

This wiki reads the two as one rule. Revisit after each iteration by default. The longer gap is an allowance earned only while both conditions hold, and four to six weeks is the outer limit under them, not a schedule.

### Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Velocity trend | The last iterations' completed points, on [[velocity]] |
| Surprises in iteration planning | Whether expanding stories into tasks changed their size or revealed new ones, on [[planning-horizons]] |
| Plan assumptions | Team, iteration length, first and last dates, where stated on the release plan ([[planning-horizons]]) |

This wiki's test: the longer gap was a mistake if the first update after it moved the plan by more than the steady velocity would have implied, or if people relied on a date the arithmetic had already ruled out.

### Sign of a violation

Seen in board history: the release plan has not changed since it was made, while iterations have completed. A stronger form is a plan whose story list still sums to more than remaining iterations × current velocity, so the plan is no longer arithmetically possible by [[fitting-stories-into-a-release]]. The source gives the rule without a sign, so both signs are this wiki's derivation.

### What breaks when it is ignored

This wiki's reading: the plan stops being the current expectation of where the team will arrive, which is the job the source gives it (L2773), and people relying on it for dates are relying on an old forecast.

### Trade-off

Each update costs attention, and this wiki reads a project with steady velocity as getting little from one, which is why the source allows the longer gap.

### Agent executor note

This wiki reads the need as strengthening where velocity history is short or unstable, since the stability condition for the longer gap cannot be shown. The update itself is arithmetic the plugin can prepare from board history, so its cost falls. The four-to-six-week figure comes from human teams on iterations of weeks and should not be carried over as a number.
