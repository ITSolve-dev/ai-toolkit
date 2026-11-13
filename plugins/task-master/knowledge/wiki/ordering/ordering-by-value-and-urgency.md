---
title: Ordering by Value and Urgency
category: ordering
summary: When value cannot be put in numbers, rate each task on three bands of value and three of urgency, separately, and order by the combination; the bands are the source's, the two extreme combinations are the source's, and the order of the seven between them is this wiki's derivation.
tags: [decision-rule, ordering, cost-of-delay, prioritization]
sources: [black-swan-qualitative-cod]
created: 2026-11-01
updated: 2026-11-01
---

# Ordering by Value and Urgency

This rule chooses what comes first when nobody can say what a task is worth. It rates [[cost-of-delay]] in words instead of numbers. The author's offer is modest, and the rule should be held to it: a way to start thinking about cost of delay, with "many of the benefits of a quantitative approach" given up (L23).

## The bands

Value is rated apart from urgency, in three bands. The author rejects a plain scale: "Rather than using a simple High, Medium, Low (where everything tends to end up as “High”) we’re going to use some descriptive words for each of the levels." (L42).

| Value band | The author's description | Line |
|---|---|---|
| Killer | "These are the few things where if we do them, we stand to make an absolute killing, or; if we *don’t* do something, it will probably kill us." | L44 |
| Bonus | The middle band; "What this means will be context dependent (of course)" | L45 |
| Meh | "This is the work that keeps the lights on but won’t get anyone too excited or move the needle significantly." | L46 |

| Urgency band | The author's description | Line |
|---|---|---|
| ASAP | "If we don’t deliver this ASAP, then the value (whatever total value that might be) will quickly evaporate" | L56 |
| Soon | "If we don’t deliver this Soon, then the value will start to decline or the risk of loss increase" | L57 |
| Whenever | "What this means is that the total value isn’t *massively* affected by delay." | L58 |

The author leaves one setting to the reader: "Whether Soon means in a matter of days, weeks or months you will need to decide for your context, given the distribution of urgency you are dealing with." (L57). This wiki gives no figure either. Under a project's own history, this wiki reads Soon against how long tasks take there, as the point where the time left no longer covers the task and the queue ahead of it ([[a-date-is-not-urgency]]).

The author's examples are commercial, with customers, revenue and competition. For a project with no revenue to point at, this wiki reads the value bands as questions a person can answer: would not doing this end or badly damage the thing the project exists for (Killer), would doing it be a change the people served would notice and want (Bonus), or is it upkeep (Meh)? That translation is ours.

## The rule

1. Rate value and urgency separately, one band each ([[urgent-versus-important]]).
2. Write down, in one sentence each, what the value is and what waiting would do to it.
3. Order by the table below.
4. Within one rank, use [[cost-of-delay-over-duration]]. Where a task cannot be rated, use [[incomparable-tasks]].
5. Rate again before the rating decides anything, because a rating made at intake describes that day ([[cost-of-delay]]).

Dependencies constrain the result: a task whose prerequisite is unfinished cannot start whatever its rank ([[sequence-versus-wait]]).

## The order of the nine combinations

The source's matrix image is lost, and its text fixes only the two corners ([[black-swan-qualitative-cod]] L71). A rule that chooses has to decide the other seven, so ranks 2 to 8 are this wiki's derivation and not the source's matrix. If the image is ever recovered, it should be compared with this table.

| Rank | Value | Urgency | Basis |
|---|---|---|---|
| 1 | Killer | ASAP | The source: "Very High" (L71) |
| 2 | Killer | Soon | Derived |
| 3 | Bonus | ASAP | Derived |
| 4 | Bonus | Soon | Derived |
| 5 | Meh | ASAP | Derived |
| 6 | Meh | Soon | Derived |
| 7 | Killer | Whenever | Derived |
| 8 | Bonus | Whenever | Derived |
| 9 | Meh | Whenever | The source: "Very Low" (L71) |

The derivation has two steps, both read from the band descriptions.

- **A Whenever task yields to any task whose value is leaking.** By its definition, its value "isn’t *massively* affected by delay" (L58), so waiting costs little however large that value is.
- **Between two leaking tasks, the higher value goes first.** The author says the distribution of value "tends to be a non-linear, power law" (L42), which this wiki reads as making a step in value larger than a step between ASAP and Soon. This is the weakest step here. A Bonus task at ASAP can lose everything while a Killer task at Soon loses a little, and the bands alone cannot settle that pair, so it is the first place to look if the order proves wrong.

The author's own statement of the aim is to "help you focus more on the things that are both valuable and urgent" (L83), and ranks 1 and 2 agree with it.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| What delivering the task would gain, or what not delivering it would lose | The request, then the task's stated purpose ([[task-must-justify-itself]]); the person steering confirms the band |
| What happens to that value if the task waits | The request, or the requester's answer to that question ([[clarifying-questions]]) |
| Any date, and what happens at it | The request; see [[a-date-is-not-urgency]] |
| When the rating was made | Board history |

Both ratings are task-only facts in the sense of [[recoverable-versus-task-only-facts]], because the repository cannot show what something is worth or how fast that drains away. The plugin can propose a band and it cannot establish one.

No source says what would show the rating wrong, so these tests are this wiki's.

- **Value was overrated** if the task was delivered and the gain written down at rating time did not happen. Read this from the people steering, against the sentence in step 2.
- **Value was underrated** if the same need keeps coming back as new requests or duplicates of a low-rated task.
- **Urgency was overrated** if the task waited longer than its band allows and the loss written down at rating time did not occur.
- **Urgency was underrated** if the task arrived after the value had gone, for instance the requester no longer wanted it.
- **The order itself was wrong** if a lower-ranked task lost more while waiting than the higher-ranked task gained by going first.

The sentence in step 2 is what makes these tests possible. Without it, a band is an opinion with nothing to check it against. That is the part this wiki keeps from the author's advice to score in a group, "where you can challenge each other’s assumptions and perhaps surface new information" (L79).

## Cost

- The rating is coarse. Nine cells cannot separate many tasks, and ties are expected.
- A Killer task at Whenever can wait indefinitely under this table. That is what the band means, and step 5 is the only check on it.
- Someone has to supply two judgements per task, and with a few people there may be no second person to challenge them. The cost of a wrong rating then falls on one judgement.
- The bands invite inflation ([[priority-inflation]]).

## Agent executor note

The rule concerns the result and not the executor, so it survives. Two limits apply. The evidence is one article with no measurement ([[black-swan-qualitative-cod]]), written for groups of people rating portfolios and backlogs. And an agent can read a request and propose a band, but no source here tests how well, so the band belongs to the person steering and the plugin's proposal should say so.
