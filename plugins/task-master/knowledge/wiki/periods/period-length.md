---
title: Period Length
category: periods
summary: A period has a fixed length of one month or less, in practice one to four weeks, chosen per project from how long a goal stays valid, how often results can be reviewed and Cohn's seven factors, then held; work is sized to the period and never the period to the work, and two weeks is one practitioner's preference with stated conditions.
tags: [rule, iterations, period-length, planning, scrum]
sources: [scrum-guide-2020, kanban-guide, montgomery-tracker-smells, cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Period Length

The length of a period is chosen per project at setup, and then held. The Scrum Guide sets an upper bound and states the trade-off:

> They are fixed length events of one month or less to create consistency. A new Sprint starts immediately after the conclusion of the previous Sprint.
>
> — [[scrum-guide-2020]], L189

> Sprints enable predictability by ensuring inspection and adaptation of progress toward a Product Goal at least every calendar month. When a Sprint’s horizon is too long the Sprint Goal may become invalid, complexity may rise, and risk may increase. Shorter Sprints can be employed to generate more learning cycles and limit risk of cost and effort to a smaller time frame.
>
> — [[scrum-guide-2020]], L200

This wiki reads "one month" as a rule of the Guide with a stated condition, Scrum as defined there. It is an upper bound and not a recommendation, and the Guide gives no lower bound. The Guide also does not say how to pick a value below the bound.

Cohn treats that choice as one made per project and not a constant. Most teams land between one and four weeks, and "There’s no one magic iteration duration that is right for all teams under all circumstances" ([[cohn-agile-estimating-planning]] L3399). The same team may need a different length on a different project (L3399). This wiki reads his range as sitting inside the Guide's bound, so the two do not disagree. Cohn names seven factors and refuses to rank them: "There is no predetermined importance to these factors." (L3425). His case studies show why, because the same factor carries different weight in each.

## Choosing the length

This wiki's starting test is built from the trade-off the Guide names: choose the shortest length in which a selected task at the 85th percentile of Cycle Time can finish and be reviewed, and no longer than the goal stays valid. The 85th percentile is the test on [[iteration-length-versus-cycle-time]]: a length set from the median passes a test on typical tasks and leaves about one task in seven unable to fit.

| Input | Read from |
|---|---|
| How long a task takes from started to finished, at the 85th percentile | Board history |
| How long a goal has stayed valid in earlier periods | Board history: goals gone obsolete, and tasks added or dropped mid-period |
| How often the people steering can review | The people steering |

At setup a new project has no board history for the first two inputs, so the test gives no answer. This wiki's branch for that case: take the review cadence of the people steering as the length, label it a guess, and re-check it against the 85th percentile once enough tasks have finished to read one ([[how-much-flow-data]]). No source gives a length for this case.

The length was too long if goals repeatedly go obsolete during the period ([[mid-period-change]]). It was too short if tasks repeatedly go back unfinished for reasons of size ([[unfinished-at-period-end]]), or if the review of one period runs into the next.

Cohn's seven factors say what moves the answer from there. In this section and the two after it, line numbers are to [[cohn-agile-estimating-planning]]. The first three columns are Cohn's (L3403-L3417, L3429-L3492). The last two are this wiki's, added because a rule that chooses must say where its inputs are read from and what later fact would show it wrong.

| Factor | Effect on length | Why | Read from | Later fact showing the choice wrong |
|---|---|---|---|---|
| Length of the release | Shorter release, shorter period | Period ends set how often work can be shown, progress measured and course corrected (L3431-L3435) | The planned release date | Release reached with too few corrections behind it |
| Uncertainty about needs, velocity or technology | More uncertainty, shorter | "The more uncertainty of any type there is, the shorter the iterations should be." (L3443) | Open questions on tasks; decisions reversed in earlier periods | A period's result rejected for a misunderstanding that an earlier review would have caught |
| Ease of getting feedback | Either way | Some reviewers give informal feedback freely and skip scheduled reviews; others are the reverse (L3449) | The people steering: who reviews, and how | Reviews skipped, or a result still unreviewed when the next period starts |
| How long priorities can stay unchanged | Shorter span, shorter period | A committed team must not be redirected (L3455) | Board history: changes during earlier periods | The signs on [[mid-period-change]] recur |
| Willingness to go without outside feedback | Lower tolerance, shorter | "the less often a team receives outside feedback, the more likely we may go astray and the greater the loss will be when that happens." (L3472) | The people steering: how much work they accept losing | A whole period's result thrown away at review |
| Overhead of iterating | Higher overhead, longer | "each iteration must be fully regression tested." (L3476) | How long closing a period takes in practice | Closing work consumes a growing share of the period |
| Feeling of urgency | The length at which pressure is even | Too long and work relaxes, then panics (L3496) | Spread of finishes across the period | [[end-of-period-crunch]] appears |

The priorities factor also sets a price on any length: while priorities are held still, a new idea waits ([[new-idea-latency]]).

### The release-length figure

> My general rule-of-thumb is that any project will benefit from having at least four or five such opportunities.
>
> — [[cohn-agile-estimating-planning]], L3439

Cohn gives the threshold as a release of "four or more months" for monthly or four-week periods (L3439), but his count is not consistent. His three-month example with monthly periods yields "only two opportunities" (L3437), presumably because the last period end is the release and leaves nothing to correct. Counted the same way, four months yields three, which is below his own minimum. This wiki reads the rule as release length divided by period length of at least five. That gives four corrections on his count and five on a straight count, so both readings are met, and it is stricter than his four-month figure. Where there is no release date, this factor has no input and drops out.

The figure is a rule of thumb from experience, and the chapter shows no data behind it.

## What the case studies show

| | Napa: four weeks (L3524-L3530) | Goodman: two weeks (L3536-L3542) |
|---|---|---|
| Team | Seven people, one site | Eighteen developers in two coordinated teams |
| Horizon | Thirteen months estimated, at least six | First release at six months, a year overall |
| Uncertainty | "fair but not excessive", with the old system as a model | "a tremendous amount"; market position decided and re-decided |
| Feedback | Users nearby but with restricted time | No internal users; proxies used |
| Priorities | Mostly held for four weeks | Held for only a few days |
| Overhead | Very little | Low, through test automation from the start |

This wiki reads the two cases as showing the factors are not additive. Goodman's horizon alone allowed four weeks: "the team could have used four-week iterations" (L3538). Uncertainty decided it. Napa shows feedback can argue for longer: "Showing them new versions every two weeks would have been too much in this environment." (L3528).

The Goodman case also shows the limit of the priorities factor. "Priorities could not remain constant for more than a few days in this environment" (L3542), yet the team chose two weeks. This wiki reads that as evidence that the factor pushes toward shorter and is not a hard cap inside the usual range. The source does not say how those mid-period changes were handled.

Both teams are larger than the few people this wiki serves, so the factors transfer and the chosen values do not.

## Cohn's preferred lengths

Cohn writes "I find two-week iterations to be ideal." (L3508). This is one practitioner's preference after experimenting with lengths, and the charter grades it on its mechanisms. Those mechanisms are:

- **One week or less:** "can be very hectic and stressful", and it leaves no recovery time if someone is out sick or something goes wrong (L3498). "Unless a project already has fully automated tests for all parts of the system, I do not often recommend starting with one-week iterations." (L3504).
- **Two weeks:** planning and testing overhead is manageable when spread across two weeks, the two weeks feel less different from each other than four do, and "most organizations can (with sufficient training) learn not to adjust priorities for two weeks while doing so for four weeks can be very difficult." (L3508).
- **Four weeks:** leaves room for more creative solutions, and "An experienced agile team working on a highly exploratory phase of a project may benefit from a four-week iteration." (L3506). The cost is a relaxed beginning and a frantic end (L3506).

## The rule that detects

Once chosen, the length does not move to suit the work.

> Through experimentation on many projects I have since learned that teams are far better off sizing the work to the length of the iteration (rather than sizing the iteration to the work).
>
> — [[cohn-agile-estimating-planning]], L3486

Cohn's early teams chose each length from the work coming in, so two weeks could be followed by six and then four (L3486). He later dropped the practice.

## Sign of violation

- **In board history:** a period's end date moved later while its work was unfinished.
- **In board history:** successive periods of different lengths with no change of setup recorded, or lengths that track the size of the selection.
- **In board history:** a gap between periods, which contradicts "starts immediately after".

The signs are this wiki's derivation from the Guide's L189 and Cohn's L3486. A planned macro-cycle, such as Cohn's "six two-week iterations followed by a one-week iteration" (L3512), is not a violation if it is recorded as setup.

The study behind [[montgomery-tracker-smells]] lists the first two as smells: "Instead of moving open issues to the next sprint, the sprint end date is extended." (L218) and "Sprints are not consistent lengths." (L221), along with "The same sprint is delayed over and over." (L227). The results for these three are in a figure that is lost, so this wiki cannot say how practitioners judged them, and it cites them only as independent statements of the sign. A fourth, "The sprint length differs from the recommendations made by Agile." (L224), is not a sign here, because this wiki's sources recommend no length that holds across projects: the Guide gives only the upper bound, and Cohn's two weeks is a preference with conditions.

## Why

What breaks is the comparison. Past performance only predicts the next period if the periods are alike, and [[filling-a-period]] rests on that. An extended period also hides the fact that the selection was too big, which is the evidence the period exists to produce. Those two reasons are this wiki's, and they do not depend on human pace. Cohn's own reason is rhythm: a fixed duration "provides a constant which helps establish a development (and delivery) rhythm" (Simon Baker, quoted at Cohn L3488).

## Cost

A fixed length leaves some periods with spare time and others short. The Guide accepts this and treats the fixed end as what makes inspection regular. It also means work is cut or deferred to fit the period, and the period is never stretched for the sake of one good result.

A short period raises the share of time spent closing it, and a long one raises the loss when a period goes wrong and the wait for a new idea ([[new-idea-latency]]).

## Which setup this applies under

Under an iteration setup, as above. Cohn's chapter takes iterating as given and does not weigh it against flow. Under a flow setup there is no period. The Kanban Guide says reviews "can occur continuously, at regular intervals, or through a combination of both" ([[kanban-guide]] L137), so a regular interval there is a review habit and not a container for work.

## Agent executor note

The month is a figure from human teams, whose work takes days to weeks. An agent may finish a task in much less time, so the shortest usable length is likely set by the people steering and not by the executor. This wiki has no evidence of what length suits a few people steering an agent, and it reads the Guide's bound as a limit and offers no value inside it.

Cohn's factors do not all survive an agent executing and a person steering. This reading is this wiki's and is untested.

- **Survive unchanged:** release length, uncertainty, ease of feedback, willingness to go without feedback, and how long priorities hold. All of them concern the people steering and the outside world.
- **Survives with a change:** overhead of iterating, where Cohn's main cost is regression testing. Automated checks shrink it, which removes his condition against one-week periods when they exist. Review by the people steering becomes the larger cost.
- **Do not survive for the executor:** urgency, sustained pace and the recovery argument about someone being out sick. They describe people. They may still describe the people steering, who review on a human clock.

## Where a period or release ends

Cohn warns: "If you tie iterations to the ends of months, one out of every three iterations will coincide with the end of a fiscal quarter." ([[cohn-agile-estimating-planning]] L3552). His case is one release planned for March 31 that slipped a week to April 7, so its revenue could not be recognised until the next quarter (L3554-L3556). It is one project, and his "at all costs" (L3552) is stronger than one case supports. This wiki keeps the mechanism, a step in value at a date, where a one-week slip costs a week before the step and a full quarter across it ([[a-date-is-not-urgency]]). The sign is a planned release or final period end on or just before a known step in value, with no room for a normal slip as read from planned-against-actual dates in board history. The source gives no margin, and a date with no outside effect is not a violation.

## Related

Whether stories fit a period at all, read from Cycle Time history, is on [[iteration-length-versus-cycle-time]].
