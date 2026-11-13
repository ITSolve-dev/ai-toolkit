---
title: Good Plan Test
category: reading-history
summary: A plan is judged by whether it was reliable enough to decide on, not by accuracy or by conformance to its original list; six months delivered in seven was still useful, in twelve was not, and regular updates are part of the verdict. A run of answers is scored instead by its accuracy (Vacanti's predictability). A plan stated beyond belief to get a share of it, or never revised after learning, cannot be compared with fact.
tags: [decision-rule, plan-vs-fact, estimation, retrospective, failure-mode, value, scope, commitment, plan-versus-fact, concept, predictability, retrospective-analysis, flow]
sources: [cohn-agile-estimating-planning, vacanti-actionable-agile-metrics]
created: 2026-11-01
updated: 2026-11-02
---

# Good Plan Test

The test judges a plan by what it was for:

> A good plan is one that stakeholders find sufficiently reliable that they can use it as the basis for making decisions.
>
> — [[cohn-agile-estimating-planning]], L469

This wiki reads that as separating a useful plan from an accurate one: a plan can be wrong and still good.

## Cohn's worked boundary

In his example a six-month release plan feeds marketing, advertising and customer-upgrade decisions (L471-L473).

| Actual | Verdict | Reason |
|---|---|---|
| 12 months | Not a good plan | "If development takes twelve months, instead of the planned six, then this was not a good plan." (L473) |
| 7 months | Probably still useful | Incorrect and may have "led to some slightly mistimed decisions", but within PMI's budgetary margin (L475) |

This wiki reads the figures as holding only for that case: a half-year release at budgetary-estimate stage. This wiki's arithmetic against [[cone-of-uncertainty]]: seven months is about 17% over, inside PMI's +25% for a budgetary estimate; twelve is 100% over, outside even the +75% of an order-of-magnitude estimate.

## The update clause

The verdict depends on whether the plan was kept current:

> In that case, the one-month late delivery should not have been a last-minute surprise to anyone.
>
> — [[cohn-agile-estimating-planning]], L475

Cohn says the plan "should have been updated regularly throughout the course of the project" (L475). This wiki reads that as judging a plan across its revisions, not by its first date alone.

## Inputs and where they are read

This wiki's reading for applying the test to a finished period or milestone:

- **Plan:** the forecast and its assumptions as recorded, per [[forecast-range-and-probability]].
- **Fact:** completion dates from board history.
- **Decisions taken on the plan:** stated by the person steering; a board does not show them.
- **Revision history:** when the forecast moved, relative to when the slip was knowable.

**Question it answers.** Did the miss hurt a decision taken in good faith, and did the plan warn in time?

**What later fact would show the verdict wrong.** A slip called harmless turns out to have cost a dependent decision.

## Precision has to rise over time

Cohn's test moves with the project. Early, a useful plan may say the third quarter and "approximately a described set of features"; later, "in order to remain useful for decision making, this plan will need to be more precise." (L469). His release plan splits features into those certain to ship and those that may ship "depending on how well things progress." (L471). This wiki reads that split as usable directly in a forecast for a few people.

## Failure signs

These are this wiki's questions to check: a plan-versus-fact reading that scores only the size of the miss, which ignores what the plan was used for; or a forecast that moved only at the very end, which is the last-minute surprise. See also *Plan Conformance as Success* (below), the neighbouring error of scoring a project against its original list.

## Trade-off

This wiki notes that a usefulness test depends on knowing the decisions, which are not recorded on a board, so the plugin must ask. Stakeholders are the judges in Cohn's definition, which makes the test partly subjective.

## Plan Conformance as Success

This failure treats matching the original plan as the measure of success. Cohn's target is the CHAOS studies' definition (Standish 2001): on time, on budget, and with all originally specified features ([[cohn-agile-estimating-planning]] L433).

> This is a dangerous definition because it fails to acknowledge that a feature that looked good when the project was started may not be worth its development cost once the team begins on the project.
>
> — [[cohn-agile-estimating-planning]], L433

> A project that delivers all features on the initial plan is not necessarily a success.
>
> — [[cohn-agile-estimating-planning]], L433

### What breaks

The reasoning rests on knowledge arriving during the work. Cohn says a team generates new knowledge about product and technology, and that this has to be "acknowledged and factored into an iterative planning process" (L425-L431). He then says:

> The most critical risk facing most projects is the risk of developing the wrong product.
>
> — [[cohn-agile-estimating-planning]], L431

This wiki reads that as a risk a conformance score cannot see. Cohn's concrete harm is users left unsatisfied because "wonderful new feature ideas had been rejected in favor of mediocre ones simply because the mediocre features were in the initial plan." (L433).

One of his own criteria for a failed project is "a project on which no one came up with any better ideas than what was on the initial list of requirements." (L433). This wiki reads that as a personal definition and a provocation; Cohn gives no measure for it.

### Observable sign

These are this wiki's questions to check, not verdicts:

- A plan-versus-fact report whose only measures are date, cost and percentage of the original list delivered.
- A period's scope unchanged from its start, although completed tasks recorded discoveries that bear on what remains.
- Newly raised requests all deferred behind the original list, with no comparison between the two.

A stable scope is not a defect by itself: a small, well-understood piece of work may have nothing to revise. The question is whether anything learned was weighed.

### What to do instead

Cohn wants "projects on which investment, schedule, and feature decisions are periodically reassessed." (L433). This wiki reads that, when explaining a difference between plan and fact, as treating a difference as potentially a success: a dropped task may be a good decision, and the explanation should say which it was. See [[replanning-on-new-knowledge]] for the mechanics and the test at the top of this page for judging the plan itself.

### Trade-off

This wiki notes that giving up conformance as the measure removes a simple, hard-to-argue number and opens a route for excusing any miss as learning. A dropped commitment with no named discovery is that excuse, and the rule in [[replanning-on-new-knowledge]] is its check.

### Agent executor note

This wiki reads the mechanism as surviving an agent, and possibly sharpening: an agent delivers the task as written and will not volunteer that it is no longer worth doing unless asked. That is the wiki's reading, not Cohn's.

## Plan Deliberately Overstated

A plan is deliberately overstated when someone states more work, or an earlier date, than they expect, in the hope of getting a fixed share of it. Cohn gives both forms and one anecdote.

### The source's cases

- A product owner gives developers "artificial dates" ([[cohn-agile-estimating-planning]] L4581).
- Developers "give estimates that the product owner knows are unrealistic" (L4581).
- One team reported that "their executives ask for more work than can reasonably be expected because “that way if they get 80%, they’re happy.”" (L4581)

The 80% is that team's account of its executives' reasoning. It is an anecdote from one team, not a measured figure.

### What breaks

Cohn's mechanism is trust: once a false figure is discovered, trust goes, and information stops flowing. A developer who knows a task will take far longer must feel safe saying so, or "problems such as this will remain hidden longer" (L4583).

This wiki reads a second break that needs no social mechanism. A plan nobody believes cannot be compared with fact, so the difference between them says nothing and [[iteration-summary-plan-versus-fact]] loses its use.

### Observable signs

Cohn gives no sign. The ones below are this wiki's, and each raises a question to check, not a verdict; see [[smell-is-not-a-finding]].

- Planned points sit above the top of the [[velocity-range-forecast]] period after period.
- Planned and earned points keep a stable ratio, as if the gap were expected.
- A date is held although no value in the range reaches it.

A single overfull iteration is not this defect. An honest plan misses too, and the sign is the repetition.

### Agent executor note

Trust between people is a management concern outside this wiki's scope, so that mechanism is recorded only as Cohn's reasoning. In a setting of a few people steering an agent, this wiki reads the defect as surviving in reduced form: nobody is pressured, but a person can still fill a period past what history supports, and the agent will not object on its own. The cost that remains is the loss of plan-versus-fact.

See also [[filling-a-period]], [[commitment-over-a-period]], [[priority-inflation]].

## Predictability

In Vacanti's usage, predictability is how accurately a process answers one question. He calls “When will it be done?” the first thing customers ask and, "for the most part, it is the only thing they are interested in until you deliver" ([[vacanti-actionable-agile-metrics]] L384-L386).

> Whether your process is predictable or not is judged by the accuracy of your answer.
>
> — [[vacanti-actionable-agile-metrics]], L394

This wiki reads that as a definition that can be scored: compare the answer given with when the item finished. It follows that a project which never records its answers has nothing to score. [[forecast-range-and-probability]] covers what a stated answer has to carry so that it can be compared afterwards.

### What it is not

**It is not adherence to a practice.** The source's case is Bennet Vallet, who ran mature Agile teams following established practice: "In his mind he was doing everything right, so he reasonably believed that predictability would inevitably follow. Yet he constantly struggled to accurately answer the most important questions that his customers were asking." (L398). This wiki reads that as agreeing with *Plan Conformance as Success* (above): following the procedure and getting the outcome are separate facts, and only the second is scored.

**It is not a standing property.** Vallet's remark is that predictability is a verb and not a noun, and the author extends it: "It is that you “do” predictability. Predictability is proactive and not reactive." (L524). The practical content is in the next sentence: "The actions you take today have the biggest impact on your predictability tomorrow." (L524). This wiki reads that as saying a forecast depends on what the project does after giving it, such as starting more work.

**It is not only a forecast.** Chapter 3 widens the Chapter 1 definition: "The bigger part of predictability is operating a system that behaves in a way that we expect it to." (L1100). The author says a process that conforms, or mostly conforms, to the assumptions of [[littles-law]] gives data that can be trusted, and is then "probabilistically predictable" (L1088-L1094). This wiki reads the two definitions as complementary: an answer can be scored only after the fact, while conformance can be checked during the work, by the assumption checks on that page.

### What produces it

The source places the cause in policy and not in circumstance:

> Amongst other things you start new work at a faster rate than you finish old work, you work on too many items at the same time, you ignore systemic dependencies and impediments, and you expedite requests that do not need to be expedited.
>
> — [[vacanti-actionable-agile-metrics]], L232

The author says these policies exist "Whether explicit or not" (L232). This wiki reads that as an instruction for review: the policy in force is the one board history shows, which can differ from the one the project declared. [[signs-of-poor-flow]] gives the reading, and [[littles-law]] gives the policies stated positively.

The author also describes a loop: the metrics "will immediately reflect policies you have in place", that data suggests a policy change, and the change appears in the next data (L242). The mechanism is observable, but this part of the book reports no worked instance of it.

### Cost

The author names the cost directly. "It will mean saying no to customer requests to start new work immediately. It will mean placing much less emphasis on upfront estimation and planning." (L234).

### Accuracy against usefulness

Vacanti's test scores the answer. The test at the top of this page records Cohn's opposite emphasis, that a plan is good if stakeholders find it "sufficiently reliable that they can use it as the basis for making decisions" ([[cohn-agile-estimating-planning]] L469), so a plan can be wrong and still good.

The resolution is this wiki's, and it turns on what is being scored. Vacanti asks the reader to count "how many times you have been wrong" (L394), which scores a process across its answers, so one miss says little. Cohn scores one plan against the decisions it fed, so one miss matters only through those decisions. Read a single plan with the test at the top of this page, and read a run of answers here. An answer given as a probability is scored the way [[service-level-expectation]] scores an SLE: by the share of items that finished within the stated time.

### Against estimation

The source's strongest claim is conditional: "If you can get to a process that has stable, predictable flow, then the act of estimating and planning—the act of making predictions—becomes trivial." (L522). The condition carries the claim. A project with no history, or with unstable flow, gets nothing from it.

This disagrees with the estimating position elsewhere in this base, and the resolution is this wiki's. The sentence is about estimates used as predictions. Estimating also finds unknowns ([[unknowns-surfaced-by-estimating]]) and gives a size at which a task is cut ([[size-ceiling]]), and stable flow replaces neither. So under a stable flow, stop producing a date by adding up estimates and keep the sizing where the project uses it. Without stable flow, the route from size to date on [[size-versus-duration]] stands unchanged. Which unit the answer is stated in is on [[points-or-time-and-count]].

### Agent executor note

The definition does not depend on the executor: the answer and the finish can be compared under any arrangement. The policies listed are set by whoever decides what starts, which here means the people steering, so they survive too. Whether an agent's run durations are stable enough for the conditional claim above to apply is not shown by this source, whose setting is human teams at Siemens Health Services. This wiki treats that as open.
