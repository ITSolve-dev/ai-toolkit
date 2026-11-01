---
title: Conditions of Satisfaction
category: task-content
summary: The criteria by which the product owner will judge a release or a feature; they carry schedule, scope and resources at release level, with one factor usually preeminent, and high-level tests at iteration level, where a story is finished when shown to meet all of them and they are written ahead only for stories likely to be taken next; planning repeats on a lessened set when they cannot all be met.
tags: [rule, task-content, acceptance-criteria, release, iterations, readiness, done]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Conditions of Satisfaction

Conditions of satisfaction are "the criteria that will be used to gauge the success of the project" ([[cohn-agile-estimating-planning]] L853): what the customer or product owner holds the result to. They exist at both release and iteration level, and in Cohn's model they are the input to planning at each (L870).

## Two levels

| Level | What the conditions contain | Citation |
|---|---|---|
| Release | Scope, schedule, budget and quality; user stories, budget, schedule in Figure 3.2; schedule, scope and resources in the release planning chapter | L857, L868, L2802 |
| Iteration | "the features she’d like developed next and some high-level tests about each feature" | L872 |

Cohn poses, and does not answer, why budget and schedule appear only at release level (L908). This wiki reads the answer as: inside an iteration the schedule is already fixed by the [[timeboxed-iteration]], so what remains to agree is what is built and how it is shown to work.

## At release level

The conditions come first in Cohn's release planning: "Before starting to plan a release, it is important to know the criteria by which the project will be evaluated as a success or a failure." (L2802). Behind them stands a financial goal: "For most projects, the ultimate scorecard is the amount of money saved or generated." (L2802). Schedule, scope and resources serve as leading indicators of that scorecard, so the owner's conditions are a combination of goals on those three (L2802). The source's example is four themes worth 200 story points in three months without adding personnel (L2804).

"While a target for each factor is often identified, one is usually preeminent." (L2804). Which one is preeminent is the test on [[date-driven-vs-feature-driven]]. The SwimStats example shows the form in practice: the season starts in four months, the release must exist a month earlier, the feature set is open, and the budget is fixed to the people already on staff (L2891).

This wiki reads this list as the same conditions as L857 under other words, with resources in place of budget and quality left out of the trade, as the section on quality below says.

## At feature level: the worked example

For the story "As a user, I want to be able to cancel a reservation." the developers learn these conditions (L874-L880):

- "A user who cancels more than 24 hours in advance gets a complete refund"
- "A user who cancels less than 24 hours in advance is refunded all but a $25 cancellation fee"
- "A cancellation code is displayed on the site and is emailed to the user"

This wiki notes that each can be checked by observing the result, which is what [[testable-acceptance]] demands of a task. It also notes what the example leaves out: a cancellation at exactly 24 hours is covered by neither condition. In Cohn's setting a conversation settles that. For an agent executor, this wiki reads such a gap as something it will guess at.

## At feature level: the stopping rule

Chapter 18 gives the feature-level form its fullest statement:

> A product owner’s conditions of satisfaction for a user story are the high-level acceptance tests that she would like to see applied to the story before considering it finished. A user story is finished when it can be demonstrated to meet all of the conditions of satisfaction identified by the product owner.
>
> — [[cohn-agile-estimating-planning]], L4125

This wiki reads two properties as making this usable as a task field. Each condition must be demonstrable: "These are the things that can be demonstrated as true about a story once it is fully implemented." (L4223). And finished is defined by all of them passing, which makes the set the stopping rule for the work.

## When they are written

Cohn calls them the most useful outcome of work done ahead of an iteration (L4125), and bounds how far ahead that goes: "it is unlikely (and unnecessary) that a team identify them for all user stories in advance of the iteration" (L4127).

The reason is that "the exact set of stories that will be undertaken in the next iteration are not known until the end of the iteration planning meeting" (L4127). The product owner and team can guess the likely ones, and the conditions are written for those. This wiki notes that preparing the rest would spend effort on stories that may never be taken.

Cohn's baseline is that a team can start from something vague: "Going from vague requirement to working software in one iteration is usually easier on a single team project than it is when there are multiple teams." (L4121). The case for more detail up front is coordination: "The additional detail allows multiple teams to coordinate work." (L4121). For Cohn, earlier detail is therefore a multi-team need rather than a general one ([[multi-team-techniques-scale-limit]]).

Preparation stays inside the current period. Those preparing work should not run a full iteration ahead: "their primary responsibility should remain the work of the current iteration, but in planning the current iteration they should include some tasks related to preparing for the next iteration." (L4123). This wiki keeps the shape of that advice and drops its staffing detail about analysts and designers, which is about people.

The trade-off is that writing conditions ahead costs effort on stories that planning may then pass over, which is why the rule covers only likely stories. This wiki notes that skipping them moves the cost to the moment the work is presented and found not to be what was wanted.

## Unwritten conditions

Cohn's school-paper anecdote separates the stated condition, five pages, from "a number of additional, unwritten conditions of satisfaction" such as being well-written, the student's own work, and in English (L855). This wiki reads a person as filling these in from context, and that as the mechanism that does not survive an agent executing: a condition left unwritten is, for the agent, a condition that does not exist ([[conversation-moves-into-the-task]]).

## Quality is outside the trade

Cohn says "agile teams typically prefer to treat quality as non-negotiable" (L857), and that scope, schedule and budget are common factors alongside it. This wiki reads quality held fixed as what keeps the [[potentially-shippable-increment]] meaningful.

## When they cannot all be met

The conditions are not fixed input. Cohn says "When no feasible solution can be found, the conditions of satisfaction must change." (L859). To reach a plan, "the product owner may need to relax one or more of her conditions of satisfaction." (L898). He says exploring them is iterative, and that feedback from each product increment flows back into them at both levels (L863, L886).

They are both the input and the exit test of planning a release. The steps iterate "until the release’s conditions of satisfaction can best be met" (L2796, Figure 13.1). A first answer is assessed against the goals, and if it misses, a longer or shorter project may be tried (L2777). The chapter summary states what happens on failure: "If a project cannot be planned that meets the set of initial conditions of satisfaction, the planning process is repeated to see if a lessened set of conditions can be met—perhaps the desired functionality can be delivered a little later or with a larger team." (L2971).

This wiki reads that as a rule about what planning may output: when the arithmetic on [[fitting-stories-into-a-release]] does not reach the conditions, the result is a changed condition stated openly, not a plan that keeps all three targets and hopes.

## Signs to check

The rule is about task content, so its sign can be the omission itself.

- A task with no statement of what would be observed when it is right.
- Conditions that cannot be checked by looking at the result, such as "works well".
- Numeric or threshold conditions whose boundaries are not covered, as in the 24-hour example.
- A release with a list of stories but no stated date, budget or quality expectation.
- A story list and a date exist, and no one can say what would make the release a failure, so a cut of any size cannot be judged.
- A task likely to be taken next carries no conditions, or only a title.
- A task was marked done with a condition unmet or never checked.
- Conditions were written for the whole backlog. This is the opposite failure: the cost was paid for stories that may never be taken.

These signs are this wiki's. Cohn also asks what risks follow from proceeding without agreement on the conditions (L906). This wiki reads disagreement among stakeholders on them as a question to surface before planning, not something the plugin can settle.

## Agent executor note

This wiki reads the mechanism as not specific to human executors, so it survives. The resource lever does not transfer as written. The source's "larger team" (L2971) assumes adding people changes velocity; for a few people steering an agent, whether more agent throughput or more steering capacity is the limit is not something this chapter answers.

The rule on writing conditions ahead survives more strongly than in the source. The transfer here is ours. Cohn's single-team allowance for vague requirements leans on people closing the gap in conversation during the iteration. An executor that guesses instead of recalling does not reliably close that gap, so this wiki reads his multi-team condition as the normal condition for a task an agent executes: the conditions are written before it starts ([[conversation-moves-into-the-task]]), and the person steering is the product owner. The limit to likely-next tasks still holds, for the same reason as Cohn's.

## Relation to other pages

[[testable-acceptance]] holds the test for one criterion on one task, and the shared standard is on [[started-and-finished-points]]. This page adds what they do not: conditions exist at release level too, carry schedule and budget there, and can be renegotiated. Cohn's "high-level tests" (L872, L4125) are this wiki's acceptance criteria at the task level. Reducing them during a period is on [[narrowing-a-task-mid-period]].

Related: [[user-story]], [[fixed-date-variable-scope]], [[release-versus-iteration]], [[release-plan]], [[multi-team-techniques-scale-limit]].
