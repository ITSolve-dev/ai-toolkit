---
title: Planning Horizons
category: periods
summary: Plan at the release, iteration and day levels, with detail shrinking as the horizon nears and each level doing a different job; a release is ended by a set of functionality and an iteration by a date, a release plan is a coarse ordered list with its assumptions, detail goes only into the next period and the cut line, and a plan that runs past what can be seen needs built-in points to look again. Planning is a continuing activity; no planning and over-planning are its two failures.
tags: [rule, iterations, planning-levels, release, uncertainty, concept, planning, release-planning, estimation, value, human-mechanism, failure-mode, over-planning, decision-rule, period-versus-milestone, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Planning Horizons

A planning horizon is the distance ahead at which a plan can still be trusted. Cohn's position is that a plan loses accuracy quickly past that distance, so planning happens at several nested levels, each with its own reach and its own grain, rather than once for the whole project.

## The rule

Cohn says "the accuracy of a plan decreases rapidly the further we attempt to plan beyond where we can see." ([[cohn-agile-estimating-planning]] L820).

His illustration is a small boat: eyes nine feet above the water see slightly over four miles, so a twenty-mile trip needs at least five looks ahead (L820). This wiki reads the arithmetic as exact only for the boat, and the figure as an analogy and not a planning number.

Cohn states the risk, and it has two parts that must both hold:

> A project is at risk if its planning extends well beyond the planner’s horizon and does not include time for the planner to raise her head, look at the new horizon, and make adjustments.
>
> — [[cohn-agile-estimating-planning]], L822

This wiki reads that as saying a long plan alone is not the defect. The defect is a long plan with no scheduled point at which it is looked at again.

## The three levels

Cohn says "The three horizons are the release, the iteration, and the current day." (L828). His planning onion places product, portfolio and strategy outside them, and "Most agile teams are only concerned with the three innermost levels of the planning onion." (L837).

| Level | Reach (L896) | Grain | Precision (L4857) | Revised |
|---|---|---|---|---|
| Release | Typically three to six months | User stories or themes; answers scope, schedule, resources (L837) | "the least precise of all" | Usually at the start of each iteration (L837) |
| Iteration | Typically one to four weeks | Tasks that turn a feature request into working, tested software (L839) | Less precise than a day's plan, because each story is imperfectly specified | At the start of each iteration (L839) |
| Day | The next day (L841) | Tasks and the activities leading to their completion (L841-L845) | Fairly precise | Daily |

The book gives the release reach four ways: two to six months (L776), three to six (L872, L896, L2761, L3057) and three to nine (L3061-L3065, L3381). This wiki reads them as one loose figure, months and not weeks, and states the inconsistency once, here. None is derived, and none transfers to a few people steering an agent as a number.

Cohn makes the link between reach and grain explicit: "Because we are looking at a closer horizon than with release planning, the components of the plan can be smaller." (L839). At release level he says the plan contains "only a prioritized list of desired user stories and one or more estimates of how much of the desired functionality is likely to be delivered by the desired release date" (L4857).

## What each level is for

> Do not make the mistake of thinking that a release plan makes an iteration plan unnecessary, or the other way around.
>
> — [[cohn-agile-estimating-planning]], L4913

Cohn gives two benefits (L4857, L4859). Different levels make plain that plans exist for different reasons, so no level has to hold precision it cannot have. They also give different views of the project: the iteration plan coordinates work inside a short period, while "A release plan provides a broader perspective on the project and ensures that the team does not lose the forest of the release for the trees of an iteration." (L4859).

This wiki's reading is that a plan should be judged against the precision of its own level: a release plan that lists tasks is over-precise, and a daily plan that lists themes is useless. [[forecast-range-and-probability]] gives the test.

## Failure when a level is missing

> A team that works iteration to iteration without awareness of a more distant goal runs the risk of continually pursuing short-term goals while missing out on targeting a truly lucrative longer-term goal.
>
> — [[cohn-agile-estimating-planning]], L4859

## Signs to check

Cohn gives the risk statements above but no board-level sign. This wiki reads the following as what to check; each raises a question, not a verdict.

- A plan with dated commitments far ahead and no marked point at which it will be revised.
- Far-off work already cut to task grain, which spends cutting effort on detail past the horizon and will be stale when reached ([[how-far-to-split-up-front]]).
- Near work still held at release grain when an iteration is about to take it.
- **No release level:** a project has iterations but no stated goal beyond the next one, and each iteration's work cannot be related to any forecast. A small project may need no release plan at all.
- **No iteration level:** tasks are started directly from a long list, and nothing states what the next period is meant to produce.

## Trade-offs

This wiki notes that revising at each level costs repeated effort, and that a plan that keeps moving offers less to promise against. It reads Cohn as accepting this cost because the alternative is precision that the horizon does not support ([[cone-of-uncertainty]]).

## Which setup this applies under

The three levels assume an iteration setup. Under a flow setup there is no iteration level, leaving a release or milestone horizon and the next tasks to be started. This wiki reads the two-part risk as still holding there, with the point of looking again supplied by something other than the start of an iteration. That reading is this wiki's, and Cohn does not address it. [[commitment-over-a-period]] covers the difference between those arrangements.

## Agent executor note

This wiki reads the horizon argument as surviving an agent executing, because its mechanism is what is unknown about the future, not how a person works. The reaches in the table are figures from human teams and should not be carried over as they stand. The daily level rests on a standup, "team member commitments made to each other" (L896), a human coordination mechanism that does not transfer; what survives is only that the nearest plan has the shortest reach and the smallest grain. Chapter 22 places it in "a team’s daily meeting" (L4857), and running such a meeting is out of scope in any case.

The iteration level's stated reason, "the highly coordinated work of a cross-functional team" (L4859), also assumes people. This wiki reads a few people steering an agent as possibly needing that level for a different reason, which is to plan what they can review in a period. That reading is unmeasured.

Related: [[timeboxed-iteration]], [[replanning-on-new-knowledge]], [[fitting-stories-into-a-release]].

## Agile Planning

Agile planning, in Cohn's usage, is planning treated as a continuing activity whose output is expected to be revised. Its defining move is to shift attention from the document to the work of producing it.

### Plan versus planning

> Plans are documents or figures, they are snapshots of how we believe a project might unfold over an uncertain future. Planning is an activity.
>
> — [[cohn-agile-estimating-planning]], L481

Cohn's reason for preferring the activity is that "The knowledge and insight we gain from planning persists long after one plan is torn up and a revised one put in its place." (L485).

### The four properties

Cohn says agile planning (L491-L499):

- is focused more on the planning than the plan
- encourages change
- results in plans that are easily changed
- is spread throughout the project

The second is qualified. Cohn says "An agile plan is one that we are not only willing but anxious to change." (L483), but he excludes change for its own sake: the change must mean something was learned or a mistake avoided (L483). See [[replanning-on-new-knowledge]].

### Why it is spread out

> Because we acknowledge that we cannot totally define a project at its outset, it is important that we do not perform all of a project’s planning at the outset.
>
> — [[cohn-agile-estimating-planning]], L489

Cohn says planning is "spread more or less evenly across the duration of a project" (L489). Release planning sets the stage, rounds of iteration planning follow, and the whole cycle repeats "perhaps a handful of times" on a project (L489). Why each round pays is on [[replanning-on-new-knowledge]].

The effort trade-off is explicit: planning effort is balanced against the knowledge that the plan will be revised (L483). This wiki reads that as the cost side of [[cone-of-uncertainty]]: detail produced early is paid for and then likely replaced, so precision bought before decisions are made buys little.

### Agent executor note

This wiki reads "easily changed" concretely for a board steered by a few people: the plan lives as ordered tasks and a forecast, so changing it means reordering, cutting or rescoping, without rewriting a document. Chapter 1 does not say this. Its limit is the opposite failure, covered in *No Planning or Over-Planning* (below). How often the plan is looked at again, and at what grain, is on the levels at the top of this page.

## Purpose of Planning

In Cohn's account the purpose of planning is to find the best available answer to what should be built, given features, resources and schedule. He says estimating and planning "are not just about determining an appropriate deadline or schedule" ([[cohn-agile-estimating-planning]] L403). Cohn separates three questions: planning ("what should we build and by when?"), estimating ("How big is this?") and scheduling ("When will this be done?" and "How much can I have by then?") (L316).

### The claim

Cohn grants that organizations demand estimates for ordinary reasons, such as marketing campaigns, release activities and training internal users, and that the difficulty of estimating does not excuse anyone from providing them (L395). He then calls those needs perfunctory and states the larger reason:

> Planning—especially an ongoing iterative approach to planning—is a quest for value.
>
> — [[cohn-agile-estimating-planning]], L403

Cohn says the question "cannot be answered all at once" and "must be answered iteratively and incrementally" (L403). His example is a product scoped for August 31, where in June the team may decide that slightly later with slightly more, or slightly sooner with slightly fewer, is better (L403).

### What a planning process supports

Cohn lists five supports (L405-L415). The notes on what each changes in this setting are this wiki's reading.

- **Reducing risk.** Estimating discussions expose what nobody knows. See [[unknowns-surfaced-by-estimating]].
- **Reducing uncertainty.** New knowledge about product and technology has to be fed back into the plan (L425-L431). See [[good-plan-test]] and [[replanning-on-new-knowledge]].
- **Supporting better decision making.** Trade-offs need both a cost and a benefit figure. See [[prioritization-factors]].
- **Establishing trust.** Reliable delivery of promised features builds trust, and "Reliable estimates enable reliable delivery." (L451).
- **Conveying information.** A plan sets baseline expectations and is not a guarantee. See [[forecast-range-and-probability]].

### The trust loop, and whether it survives an agent

Cohn describes a loop: "Reliable estimates benefit developers by allowing them to work at a sustainable pace." (L453), which yields fewer bugs, which "lead back to more reliable estimates because less time is spent on highly unpredictable work such as bug fixing." (L453).

This wiki reads the loop as half transferable. The first link depends on a human executor's pace and does not survive an agent executing, because an agent has no pace to protect. The second link survives: unpredictable rework still degrades forecasts whoever does it. The trust claim survives for the person steering, who is the one deciding whether to believe a forecast. Cohn makes no claim about agents; this transfer is the wiki's.

### Scale

Chapter 1 argues at whole-project scale, with teams of people and budgets in the millions in its examples. Its go/no-go reasoning is not kept here as a rule. This wiki reads what carries to a few people as the ordering of questions: what to build comes before when it lands. See *Agile Planning* (above) for how Cohn distributes that work over time.

## No Planning or Over-Planning

These are the two extremes Cohn says teams fall to once they notice that planning is hard and plans are often wrong:

> Teams often respond to this by going to one of two extremes: they either do no planning at all or they put so much effort into their plans that they become convinced that the plans must be right.
>
> — [[cohn-agile-estimating-planning]], L372

### No planning

**What breaks.** Cohn says "The team that does no planning cannot answer the most basic questions such as “When will you be done?” and “Can we schedule the product release for June?”" (L372).

**Observable sign.** The sign Cohn gives is the unanswerable question. This wiki adds where to read it: a request for a date or a scope by a date has no answer derivable from the board, for example open work with no estimates and no ordering.

### Over-planning

**What breaks.** Cohn says the team "deludes themselves into thinking that any plan can be “right.”" (L372), and adds: "Their plan may be more thorough but that does not necessarily mean it will be more accurate or useful." (L372). This wiki reads thoroughness and accuracy as separate properties, and takes the reason from the [[cone-of-uncertainty]]: early in a project the unknowns are unresolved however much detail is written down.

**Observable sign.** Cohn gives none beyond the belief itself. This wiki proposes these as questions to check, not verdicts: tasks for distant work detailed as finely as the next work; many tasks all created at the project's start with few added later; a detailed plan with no recorded revision although delivery has already diverged from it. Each has an innocent explanation, such as a small and well-understood project.

### Telling the middle from either extreme

This wiki's test: the amount of planning is enough when it supports the decision currently waiting on it, per [[good-plan-test]]. More detail than that decision needs is over-planning; too little to make it is under-planning. Cohn calls the two extremes "equally dangerous" and leaves the right amount as an open question for each project (L513). He gives no number.

### Related

*Agile Planning* (above) is Cohn's position between the extremes. *Purpose of Planning* (above) explains why skipping planning is not an available way out. Distant work left coarse on purpose is the subject of the levels at the top of this page.

## Release Versus Iteration

A release and an iteration are both spans of work, but they are defined differently. An iteration is defined by time. A release is defined by a body of related functionality, delivered across one or more iterations.

> A release comprises one or more (usually more) iterations that build upon each other to complete a set of related functionality.
>
> — [[cohn-agile-estimating-planning]], L776

Cohn's reason a release exists at all is that one iteration is too short for a result users would want: "a single iteration does not usually provide sufficient time to complete enough new functionality to satisfy user or customer desires" (L776).

### The test

This wiki states the discriminating question as: what ends this unit? If the end is a date and the content gives way, it is a period, handled as a [[timeboxed-iteration]]. If the end is a coherent set of functionality, it is a release, which is Cohn's closest equivalent of a milestone. Cohn does not phrase the test this way; the phrasing is this wiki's, drawn from the definitions at L764 and L776. It is the same test as "A period versus a milestone" on [[commitment-over-a-period]], which asks which of the two gives way when they collide.

A release can still carry a date. Whether its date or its content yields is settled through [[conditions-of-satisfaction]], not by its definition: Cohn says the product owner "may, for example, be equally satisfied with a release in five months that includes one set of user stories as with a release a month later" (L857).

### Numbers, with their conditions

- "While iterations are most commonly one to four weeks, a release is typically two to six months." (L776).
- The summary and the discussion of Figure 3.2 give three to six months for a release plan (L872, L896). The inconsistency across the book is noted under the levels table at the top of this page.
- Worked case: an investment management system, one release for mutual and money market funds, six two-week iterations, roughly three months; a second release for stocks and bonds, four more two-week iterations (L776).
- "Releases may occur at varying intervals." (L776). This wiki reads that as iteration length tending to be regular while release length does not need to be.

These figures describe human teams. This wiki reads the shape as surviving a few people steering an agent, and the month counts as not surviving it.

### Signs to check

Cohn gives none. This wiki reads these as questions.

- A period on the board has a target set of features and its end date moved to fit them. It is being run as a release while named as an iteration.
- A release has no coherent statement of what it completes, only a date. It is then a long period, and it cannot use Cohn's definition.

Related: [[fitting-stories-into-a-release]], [[potentially-shippable-increment]].

## Release Plan

A release plan is the plan one level above an iteration. Cohn defines it plainly: "Release planning is the process of creating a very high-level plan that covers a period longer than an iteration." ([[cohn-agile-estimating-planning]] L2761). His typical figures are three to six months and three to twelve or more iterations, with the count depending on iteration length (L2761), and he adds that releases can run more or less often depending on the type of software (L2947). Those figures describe a human team shipping a product, and this wiki does not transfer them to a few people steering an agent as a target size. The level sits in the levels at the top of this page.

### What it is for

The source gives three reasons (L2763-L2767):

1. It decides how much must be developed and how long that takes before the product is releasable.
2. It conveys what is likely to be developed and when, which other planning depends on.
3. It is a guidepost. "Without the concept of a release, teams move endlessly from one iteration to the next." (L2767). "A release plan provides context that allows iterations to combine into a satisfying whole." (L2767).

The third reason is the one that carries a failure. Cohn's image is the hiker who heads for the highest visible peak, reaches it, finds it a false peak, and repeats (L2767). The cure he names is a plan "that shows a team’s current expectation of where they ultimately wish to arrive" (L2773). He calls this "a fundamental concern with any iterative process, not just agile ones" (L2767).

### What it contains

"The release plan itself is usually documented as simply a list of the user stories that will be developed during the project." (L2779). Items are stories, meaning descriptions of functionality to be delivered, not engineering tasks (L2781). What it deliberately leaves out is on *Release Plan Level of Detail* (below).

Where the setting warrants it, the plan also states its key assumptions: who is on the team, how long the iterations are, when the first iteration starts and when the last finishes (L2783-L2789). This wiki reads those assumptions as what makes the plan checkable later: each is a fact that can be compared with what happened, and a change in one is a reason for [[replanning-on-new-knowledge]].

### Period versus milestone

The line between the two is on *Release Versus Iteration* (above). This wiki reads this chapter as agreeing with it: an iteration is bounded by the calendar, and a release is judged against its [[conditions-of-satisfaction]], of which a date is one that may be fixed. Whether the date or the scope gives way, and how stories are selected for it, are on [[fitting-stories-into-a-release]].

### Sign of the failure

This wiki's sign for the false-peak failure: iterations follow one another on a board and nothing above them names what they add up to, so asking what is left before something can ship has no answer from the board. The sign raises a question: a project of independent small fixes may have no release to name.

### Agent executor note

This wiki reads the guidepost reason as not depending on a human executor. It arguably strengthens, because an agent works the task in front of it and does not carry the destination between tasks unless something states it. The source does not address this.

## Iteration Plan Versus Release Plan

An iteration plan and a release plan are the two stages of what Cohn calls one process. The release plan gives the long view with rough edges, and the iteration plan gives a detailed view of a single iteration, made as that iteration begins.

| | Release plan | Iteration plan |
|---|---|---|
| Planning horizon | 3-9 months | 1-4 weeks |
| Items in plan | User stories | Tasks |
| Estimated in | Story points or ideal days | Ideal hours |

The table is Cohn's ([[cohn-agile-estimating-planning]] L3061-L3065). The prose just before it says "usually three to six months out at the start of a new project" (L3057), while the table and the chapter summary (L3381) say three to nine. The inconsistency is noted once, under the levels table at the top of this page.

### What the second stage is for

> The primary purpose of iteration planning is to refine suppositions made in the more coarse-grained release plan.
>
> — [[cohn-agile-estimating-planning]], L3069

Cohn gives two reasons the refinement has value: the release plan is "usually intentionally vague" about story order, and the team knows more at iteration start than when the release plan was last updated (L3069). This wiki reads the discriminating criterion as timing against knowledge. Detail belongs in a plan only when it is made late enough to use what has been learned. Cohn adds that an iteration plan "still has some rough edges and continues to be uncertain" (L3075), so the second stage narrows uncertainty without ending it.

### Levels in this wiki's vocabulary

Cohn's user story is this wiki's task, and Cohn's task is the level below it, which the plugin does not produce ([[unit-of-work]]). The transfer here is ours: for the plugin, the second stage means confirming the selection and order for the period, starting from a refreshed order ([[reprioritize-before-each-iteration]]). It does not mean expanding each task into hour-sized pieces, and how far the second stage looks into the how is on [[planning-stops-at-guesses]].

### Failure mode and its sign

The sign is this wiki's: detail written far past the coming period, such as fully sequenced work items several iterations out. That detail was fixed before the knowledge that should shape it existed, so it will either be rewritten or followed against better information. See [[how-far-to-split-up-front]] and *Release Plan Level of Detail* (below).

### Agent executor note

The two-stage logic rests on when facts become known and not on who executes, so this wiki expects it to survive an agent executing. The horizons and the estimation units come from human teams. Ideal hours do not transfer ([[size-ceiling]]), and the choice of period length is on [[period-length]].

### Related

Filling the second stage is on [[filling-a-period]]. The levels of planning as a whole are at the top of this page.

## Release Plan Level of Detail

A *Release Plan* (above) stays coarse on purpose. Detail is added as late as it can be, for specific reasons, which is the grain side of the levels at the top of this page.

### What stays out

> During release planning we do not want to create a plan that indicates which developers will work on which user stories or tasks or the sequence in which work will be performed within an iteration.
>
> — [[cohn-agile-estimating-planning]], L2781

Cohn calls that level of detail "dangerous and misleading during release planning" (L2781). Three things are excluded:

- **Who does what.** "Decisions about who works on what and the sequence of activities are best left to the individuals working on those tasks and are best deferred as long as possible." (L2781).
- **Sequence inside an iteration.** Same passage.
- **Engineering tasks.** Items are stories. "During release planning it is too early and some user stories may be insufficiently understood to be disaggregated into engineering tasks." (L2781). They are split at the start of the iteration that contains them (L2781); see *Iteration Plan Versus Release Plan* (above).

### What goes in which iteration

Placing stories into named iterations is optional, and the source gives the trade-off (L2838):

- **For:** more detail, useful when coordinating work among multiple teams.
- **Against:** it takes more time, and "even if we do preliminarily assign work to specific iterations, we do so with less knowledge than we’ll have at the start of each iteration."
- **Net:** "Undoubtedly, the plan will change as we learn more throughout the project.", so the effort should be weighed against that.

Cohn's own position:

> What I find to be a good compromise is to place specific work into the first one to three iterations, treating the rest of the release plan as one large bucket. It’s almost always worth allocating specific work to the first iteration, especially if it is starting immediately.
>
> — [[cohn-agile-estimating-planning]], L2838

The summary states the same thing in softer form: it is usually enough to identify the stories for the first couple of iterations and leave the rest to be placed later (L2969).

### Where the detail goes

The fictional case study in Chapter 23 (L4961) narrows this further, to two places. Everything between them is a stack in priority order: "I’ll stack up the story cards you said you really want in the release and that’s our plan" (L6207).

> The most important thing is to know what is going to be worked on next.
>
> — [[cohn-agile-estimating-planning]], L6195

> The next most important thing is to know those features at the bottom of the list that may or may not make it into the release.
>
> — [[cohn-agile-estimating-planning]], L6195

**The next period,** because the rest of the plan expires quickly: "In two weeks we’ll know so much more than we do today. Why plan what we’ll do in an iteration until we have to?" (L6203).

**The bottom of the list,** because items near the cut line are the ones an outside promise can get wrong: "we wouldn’t want marketing to design packaging that said, ‘Now with background music’ if that’s a feature that may get dropped at the last minute." (L6199). The source adds that this matters little at the first planning and more near the end of the release (L6199).

The exception is scale: "On a larger project, particularly with multiple teams that need to coordinate work, we might look ahead two or three iterations." (L6203). This wiki notes that the exception concerns coordination across teams, which is out of scope here, so for a few people the rule stands as stated. The form for several teams is Cohn's rolling lookahead plan, detail for the next two or three iterations dropped as they finish (L4166, L4225), which this wiki does not keep at its scale.

### Sign of a violation

These signs are this wiki's reading, seen in board state:

- Stories assigned to iterations more than about three ahead.
- A release-horizon story already split into engineering tasks long before its iteration.
- Assignees or an internal order set on work that has not reached an iteration.
- An ordered list with no marked items that may not make it, while something outward-facing depends on them.

Each sign raises a question rather than a verdict. The source allows that some projects warrant more detail (L2838), and multi-team coordination is the reason it names. That reason is at a scale this wiki does not serve, so for a few people it rarely applies.

### What breaks when it is ignored

The source does not spell out how the misleading happens, so this reading is this wiki's. The plan claims precision it does not have, and a reader takes it as commitment ([[estimate-versus-commitment]]). Effort spent on far-iteration placement is lost when the plan changes, which the source expects.

### Trade-off

Following the rule leaves the far part of the release as an undifferentiated bucket, so the plan cannot answer what ships in a given late iteration, and someone who wants that answer gets a range ([[forecast-range-and-probability]]). It also gives up any cross-team coordination that depended on that detail.

### Agent executor note

This wiki reads the two reasons differently. "best left to the individuals" (L2781) is a human-autonomy argument and does not carry over: with one agent there may be no choice of assignee to defer. The knowledge argument carries over unchanged and is the stronger of the two: a story expanded into tasks early is expanded on assumptions the earlier iterations may change, and an agent fills gaps by guessing, not by asking ([[underspecified-task]]). So the no-early-disaggregation rule survives on the second reason alone.
