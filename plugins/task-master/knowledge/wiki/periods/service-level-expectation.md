---
title: Service Level Expectation
category: periods
summary: A per-item statement of how long an item should take from started to finished, as an elapsed time and a probability read from cycle time history; the Kanban Guide calls it a forecast and Vacanti a small-c commitment owed at the moment of pulling, it carries no penalty, and its example figures are not targets. The percentile is chosen with whoever receives the work, usually starting at the 85th, from about 11 to 30 finished items (11 or 12 at the least) of a process that obeys Little's Law; one item, epic or project is forecast from finished items of the same type only; start with one global SLE and split by type only once the whole system is predictable and the split is needed.
tags: [rule, forecast, commitment, kanban, flow-metrics, cycle-time, percentiles, decision-rule, estimation, method, forecasting, percentile, sla, segmentation, class-of-service]
sources: [kanban-guide, scrum-guide-2020, radzikowska-waiting-blocked, kanban-playbook-right-sizing, vacanti-actionable-agile-metrics, flow-metrics-scrum-teams]
created: 2026-11-01
updated: 2026-11-02
---

# Service Level Expectation

A service level expectation (SLE) is the Kanban Guide's forecast of how long one item should take. This rule chooses: it fixes the expectation that aging and sizing are then judged against.

> A service level expectation (SLE), which is a forecast of how long it should take a work item to flow from started to finished. The SLE itself has two parts: a period of elapsed time and a probability associated with that period (e.g., “85% of work items will be finished in eight days or less”). The SLE should be based on historical cycle time and, once calculated, should be visualized on the DoW. If historical cycle time data does not exist, a best guess will do until there is enough historical data for a proper SLE calculation.
>
> — [[kanban-guide]], L115

This wiki reads the following from that passage.

- **Both parts are required.** "Eight days" is not an SLE without its probability.
- **85% and eight days are the Guide's example.** They are not a recommended level. Neither figure comes with a setting, so they carry no information about what a project should expect.
- **It is a forecast.** The Guide calls it that, and it does not call it a commitment. An item may miss it by design, since the probability is below 100%.
- **It is per item.** It says nothing about what a period will contain.
- **The phrase "enough historical data" is undefined.** The Guide gives no count. Vacanti does: see choosing the percentile, below.

Cycle time is defined on [[cycle-time]].

## Vacanti: owed at the moment of commitment

Line references in this section and the next two are to [[vacanti-actionable-agile-metrics]]. Vacanti treats the statement as the other half of deferred commitment: a team that delays committing until it pulls an item owes a forecast at that moment ([[backlog-versus-commitment]]).

> we must—at the time of commitment—also communicate to our customers a date range and confidence level for each and every committed-to work item.
>
> — [[vacanti-actionable-agile-metrics]], L3012

The range is not guessed for the item. It is read from the percentile lines on the scatterplot of finished work (L3026; [[cycle-time-percentile-lines]]). In the book's example (Figure 10.5) the 50th, 85th and 95th percentiles of cycle time are 20, 43 and 63 days:

> any item that enters our process has a 50% chance of finishing in 20 days or less, an 85% chance of finishing in 43 days or less, or a 95% chance of finishing in 63 days or less.
>
> — [[vacanti-actionable-agile-metrics]], L3028

This wiki reads that sentence as true only while the process that produced the data keeps behaving the same way: the chapter makes the same point when it says the quality of the data depends on how well the process obeys the assumptions of [[littles-law]] (L3054). The figures are one chart's and carry no target.

## The name

The book's chapter uses "SLA" because the industry does, and Vacanti objects to the term himself.

> SLA sounds too much like the language of formally negotiated contracts with penalties for nonconformance.
>
> — [[vacanti-actionable-agile-metrics]], L3014

> Better nomenclature for the concept of a SLA, in my opinion, is “Service Level Expectation” or “Cycle Time Target”.
>
> — [[vacanti-actionable-agile-metrics]], L3024

This wiki uses SLE for the concept and keeps "SLA" only inside quotations and when reporting the source's wording.

## Forecast or commitment

The Kanban Guide says forecast and Vacanti says commitment, about the same statement. This wiki reads the gap as smaller than the words: Vacanti's commitment is the small-"c" kind ([[backlog-versus-commitment]]), and he separates it from a contract with the same test as the Guide's probability.

- **SLE versus contract.** A contract carries a penalty for missing it. An SLE does not: "A team or an individual should not be punished for missing these commitments" (L3022). A miss starts a question instead: "the team should take any missed SLA as an opportunity to learn." (L3022)
- **SLE versus estimate of an item.** An estimate is a statement about one item. This wiki reads an SLE as a statement about the process, applied to each item as it enters. No item-level number is produced: the only item-level question it leaves is the yes/no of [[right-sizing]].

What is left of the difference is who stands behind it. This wiki reads the choice of a percentile as the step that turns a forecast into something agreed, which matches the separation on [[estimate-versus-commitment]]: history gives the probabilities, and choosing one with the receiver of the work is the decision. A statement read off the chart and never agreed stays a forecast.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Cycle times of finished items | Board history: timestamps at the [[started-and-finished-points]] |
| The probability | Chosen at project setup, with whoever receives the work: see choosing the percentile, below |
| The items that count as comparable | Items with the same started and finished points |

The SLE was wrong if, over later items, the share finishing within the stated time is far from the stated probability. A share much higher than stated means the SLE is too loose to warn anyone. A share much lower means it no longer describes the workflow.

## What it is used for

The Guide's use is aging: "Ensuring work items do not age unnecessarily, using the SLE as a reference." (L134). See [[overrun-triggers-a-recut]]. Vacanti's chapter conclusion names the same use with the commitment beside it:

> SLAs not only allow teams to make commitments at the individual work item level, but they also give us extremely useful information about when teams need to intervene to ensure the timely completion of those items.
>
> — [[vacanti-actionable-agile-metrics]], L3166

The intervention points are on [[percentile-intervention-triggers]].

The Kanban Playbook adds another use, before a task starts: is there a good chance it finishes within the SLE? ([[kanban-playbook-right-sizing]] L30). See [[size-ceiling]], which also deals with the circle this creates. The Playbook warns that history full of oversized or tiny items "reflects that noise, not your system's real performance." (L22). This wiki reads that as a reason to compare like with like, and it does not take from it that an SLE is useless until a project has right-sized.

Vacanti goes further, on a condition: "if a team follows all of the principles presented in this book" ([[vacanti-actionable-agile-metrics]] L3166), then "the SLA can be used as a substitute for many upfront planning and estimation activities" (L3172). See [[right-sizing]]. This wiki reads the condition as load-bearing, so a project breaking the assumptions of [[littles-law]] does not get this substitution.

## Two meanings of SLE

The term does not mean one thing across this wiki's sources. In the Kanban Guide an SLE is a forecast with a probability, from started to finished, and Vacanti's "SLA" is the same statement under another name. In the Kanban Maturity Model text on [[waiting-versus-blocked]], "agreed waiting time (service level expectation \[SLE\])" ([[radzikowska-waiting-blocked]] L53) is an agreed time on one outside wait, and passing it changes an item's state. This wiki uses SLE in the Guide's sense, and calls the other an expected end.

## Choosing the percentile

Choosing an SLE means picking which percentile of past cycle time the team will commit to. It is a choice about how often a miss is acceptable, so it is made with the receiver of the work, from data the team has already looked at. The source calls the same thing an SLA; see the note on the name on the SLE page.

### Inputs and where each is read from

- **Percentile lines:** the cycle time scatterplot built from board history ([[cycle-time-percentile-lines]]).
- **Tolerance for missing:** asked of the customer or stakeholder. It is not on the board. "They may opt" for a shorter SLE with more uncertainty, or a longer one with more certainty ([[vacanti-actionable-agile-metrics]] L3074-L3080).
- **Context the team lacks:** "Our customers and stakeholders almost certainly have contextual information that we do not that will have some bearing on our choice of an SLA." (L3080)

### The choice

Given lines at 20 days (50th) and 43 days (85th), a customer content to see half of commitments missed gets 20 days at 50%, and one who wants more certainty gets 43 days at 85% (L3028).

The default starting point is an observation from Vacanti's experience, not a rule: most teams start at the 85th percentile (L3030). Whether the standard percentiles fit a given context is deferred to a later book: "begin with these standard ones and experiment from there" (L3052). [[flow-metrics-scrum-teams]] names settings for a forecast of a period, on [[throughput-monte-carlo]] (its L954). This wiki reads them as a starting point for an SLE as well, which the book does not say.

The goal after choosing has two stages: "first meet that SLA at least 85% of the time (true predictability)" (L3036), then lower the number of days the percentile stands for.

### How much data

> As few as maybe 11 or 12. Probably no more than 30.
>
> — [[vacanti-actionable-agile-metrics]], L3054

That figure is conditional. Vacanti immediately says "The bigger question is in terms of quality not quantity." (L3054) The better a process obeys the assumptions of [[littles-law]], the fewer points it needs, and one that keeps violating them gets no trustworthy confidence level from any amount of data (L3054-L3060). The figure is from his practice and is stated without a study behind it.

This wiki adds a consequence: a project with fewer than about a dozen finished items has no SLE to read from history. The Kanban Guide's best guess stands in until then, labelled as a guess, and anything that depends on a measured SLE, such as [[right-sizing]], has only that guess to stand on. How little a percentile says on few dots is on [[cycle-time-percentile-lines]], and what can be said below that point is on [[how-much-flow-data]].

### What later fact shows the choice wrong

This test is the wiki's reading of the stated goal (L3036): the share of finished items at or under the SLE stays below the stated confidence. At 85%, more than 15% of items finishing late means the commitment is not being met, and the question is whether the percentile or the process is at fault. Each miss also gets its own question: "Why did we miss the SLA?" (L3022)

### Three mistakes and their signs

Vacanti names three (L3062-L3068). The signs are this wiki's phrasing of what each would look like.

1. **Set without analysing cycle time data.** Sign: no scatterplot or percentile behind the published number. The mistake is not disagreeing with the data: "there is nothing (necessarily) wrong with choosing an SLA that is not supported by the data" (L3070), so an 85th percentile of 45 days can sit beside a published 35 days at 85%, provided the choice follows a look at the data (L3070). This wiki notes that such an SLE is predicted by its own data to be missed more often than it claims.
2. **Set by an external manager or management group.** Sign: the number arrives from outside the people doing the work. The reasoning is ownership: "Since it is the team who is making the commitment, it should be the team that chooses what that commitment point is." (L3072)
3. **Set without the customer or stakeholders.** Sign: the receiver of the work cannot say what confidence they agreed to.

The source rules out two parties and admits one: the only other party in the decision is a customer or stakeholder (L3072).

### Trade-offs

A higher percentile buys certainty with a longer promise, and how much it costs depends on the shape of the data: see [[cycle-time-percentile-lines]], where 15 points of confidence cost more than double the days. In that real case the customer chose the 70% SLE to start (L3050).

### Per setting, for the choice

This section is the wiki's reading. On a project of a few people steering an agent, mistakes 2 and 3 can collapse into one person: the person steering is both the team and the customer. Mistake 1 stays fully applicable, since it needs only board history.

## Forecasting a single item from the percentiles

A **single-item forecast** answers "when will this one thing finish?" by reading a percentile off the recorded cycle times of finished items of the same type. Vacanti calls this "very straightforward" ([[vacanti-actionable-agile-metrics]] L3632) and identifies it with the SLA method of his scatterplot chapter (L3632, L3642), which this wiki keeps on this page. It satisfies [[forecast-range-and-probability]] because the percentile is the probability and the cycle time at that percentile bounds the range.

### Procedure

1. Collect "the Cycle Time data for the all same types of work items" (L3568), as a [[cycle-time-scatterplot]] does.
2. Vacanti's next step: "You will just choose the percentile that you want to attach to your forecast and use the corresponding range." (L3574)
3. State both numbers together. His example is that "a typical work item completes in 43 days or less 85% of the time" (L3580).

### Inputs and where they come from

- **Cycle times of finished items:** board history, read from when an item entered and left the states being measured.
- **Item type:** the board's work types. Type is the discriminator: "If the work items we are interested in were epics or projects, for example, then we would need to capture the Cycle Time data for epics or projects" (L3580). This wiki reads that as a prohibition on forecasting an epic from story history; a percentile from another type answers another question.
- **Percentile:** a choice, not a finding. Vacanti later says "85<sup>th</sup> percentile (or whatever percentile you feel comfortable with)" (L3618). The choice is made as in choosing the percentile, above.

### Numbers and their conditions

The 43 days at 85% comes from one sample scatterplot of one team's user stories (L3574-L3580). It is an illustration of the form, not a benchmark, and 85% is not given as a recommended level beyond that example.

### What would show it wrong

The source does not state this; the following is the wiki's own check. If materially more than 15% of later items of that type exceed the 85th-percentile value, the history no longer represents the current process and the percentile needs rereading. The precondition is on [[throughput-monte-carlo]].

### Limits

These limits are this wiki's reading, not the source's.

- **Clock start.** A cycle time runs from the start of work, so the method gives a duration once an item starts. A date for an unstarted item also depends on when it will start, which this method does not supply.
- **Few people, little history.** The chapter gives no minimum sample. On a small project with few finished items of a type, the percentile rests on very few points, and the statement should say how many ([[cycle-time-percentile-lines]]).

### Agent executor note on a single item

This wiki's reading: the mechanism is an empirical distribution, so it does not depend on human pace and survives an agent executing. It does depend on the history coming from the same way of working: cycle times recorded under human execution, or under a different setup for steering an agent, do not describe the current process.

### See also, for a single item

[[forecast-range-and-probability]], [[forecast-from-an-average]], [[burn-up-with-percentile-lines]], [[throughput-monte-carlo]]

## An SLE per work item type

Cycle time scatterplots can be filtered by work item type the same way cumulative flow diagrams can, and any such cut is valid as analysis ([[vacanti-actionable-agile-metrics]] L3084). Using a cut to offer a different SLE per type is a separate decision, and Vacanti treats it as advanced.

### Two reasons to segment

1. **To see a kind of outcome.** Items that did not finish normally, such as abandoned ones, can be tagged and shown alone. "Displaying only the abandoned items would give you a good visualization as to the time wasted on those activities." (L3086). See [[non-standard-departure]].
2. **To offer different SLEs.** Stories and defects probably have very different percentiles (L3094), so "our SLA for user stories might be 14 days at 85% but for defects it might be five days at 85%" (L3094).

The first reason commits to nothing. The second makes a promise per subtype, which is where the condition below applies.

### The rule

> If you are going to offer different SLAs for different work items types, then you have to ensure that all the assumptions for Little’s Law for each and every subtype are adhered to.
>
> — [[vacanti-actionable-agile-metrics]], L3096

> If you are just starting out with flow principles, I would highly recommend just setting one global SLA for all your work items types and get predictable that way first.
>
> — [[vacanti-actionable-agile-metrics]], L3098

Vacanti's order is global first, then subtypes only on need: "Get predictable at an overall system level first. You may find that is good enough. Only optimize for subtypes later if you really need to." (L3098). He calls the advice to design classes of service up front misguided (L3098); the full case is on [[class-of-service]]. The checks per subtype are on [[littles-law-assumptions]], and [[littles-law]] says the law holds for each type as well as for the whole.

### Inputs and what would show the choice wrong

- **Whether the global SLE is met:** the share of finished items within it, from board history.
- **Whether a subtype has its own stable data:** finished items of that type alone, read against the data needed in choosing the percentile, above.
- **Whether a split is needed:** a receiver who actually asks for a different promise per type.

This wiki reads the later fact as follows: per-type SLEs were premature if the types' percentiles drift or the types' finished counts stay too thin to read. A global SLE was too coarse if a type's items consistently sit far from the line for the rest, and the receiver cares about that difference.

### Failure sign

This sign is the wiki's phrasing of the warning at L3096: separate SLEs per type on a board whose global SLE is not yet being met, or whose subtypes have too few finished items for a percentile to mean anything. As with every sign here, it raises a question, not a verdict ([[smell-is-not-a-finding]]).

### Scale note

This note is the wiki's own. A few people's board finishes few items, so splitting by type spreads the count thin faster than on a larger team. The source's data-point range of about 11 to 30 applies per promise, so the global SLE is the natural default for this setting.

## Which holds under which setup

- **Flow setup:** required, and it is the only forecast the setup has.
- **Iteration setup:** not required. The Scrum Guide forecasts a whole selection, not an item ([[filling-a-period]]), and the period is the coarse limit.
- **Iterations with a WIP control:** optional, and useful as an earlier warning than the period's end, because age can be checked while a task is open. [[flow-metrics-scrum-teams]] uses it this way, at selection and inside the period (L1044, L1146).

The resolution is this wiki's. An SLE under a period tends to be capped by the period's length, so history from such a project is not comparable with history from a flow setup. The cap is not firm: [[flow-metrics-scrum-teams]] rejects the idea that all items finish inside a two-week period (L1130), and this wiki keeps a returned task's whole span ([[unfinished-at-period-end]]), so such a task can run past the period's length.

## Cost

An SLE needs finished items, and a few people finish few of them. On a small board a percentile rests on a handful of items, so one outlier moves it. That caution is this wiki's, and the Guide does not discuss small samples. Vacanti's claim that percentiles resist outliers is reconciled with it on [[cycle-time-percentile-lines]].

A higher probability costs a longer promise, by an amount that depends on the shape of the data: [[cycle-time-percentile-lines]].

## Agent executor note

The SLE is read from a project's own history, so it survives a change of executor better than any borrowed figure does. Four cautions apply, and all four are this wiki's reasoning, unmeasured.

- A human team's SLE does not transfer to an agent, so a new project starts from the Guide's "best guess".
- An agent-run task's cycle time includes the time it waits for a person, so the SLE may mostly measure review and not execution.
- Changing the model, or how tasks are reviewed, changes the system the history describes, so older history then stops applying.
- On a project of a few people the customer is often the person steering. The commitment then has less of an external audience, and its intervention use matters more than its promise.
