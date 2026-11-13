---
title: Stating a Date or Forecast
category: periods
summary: How any date, count or release forecast is stated: a range, its basis and assumptions, and a probability where recorded data computed one; Vacanti requires range and probability, Cohn a range or a confidence, and this wiki resolves them by what the project has recorded. A single date, a fractional iteration count, a date from an average, a straight-line projection and a Little's Law division are gut checks, never commitments; a stated range is narrowed as unknowns go, and a date is safe because of the conditions around it, not its exactness.
tags: [rule, estimation, forecasting, predictability, date-commitment, forecast, uncertainty, release, failure-mode, plan-content, averages, distribution, retrospective, flow-metrics, burn-up, throughput, s-curve, concept, overrun, expectations]
sources: [vacanti-actionable-agile-metrics, cohn-agile-estimating-planning, flow-metrics-scrum-teams]
created: 2026-11-01
updated: 2026-11-02
---

# Stating a Date or Forecast

This page is the base's one rule for how a date, a count or a release forecast is stated. Vacanti's form comes first, then the table that resolves it against Cohn by what the project has recorded, then Cohn's form of the statement and the failures both authors name: a single date, a range never narrowed, a date from an average, a straight-line projection, a division by Little's Law, and a date taken as a promise. Whether anyone decided to hold to a date is a different test, on [[estimate-versus-commitment]].

## Vacanti: range and probability

A **forecast**, in Vacanti's usage, is a calculated statement about when an item or items will finish, and it is incomplete unless it states both a date range and the probability of landing in that range. A single date, or a range with no probability, is an unqualified claim about an uncertain future.

> A forecast is a calculation about the future completion of an item or items that includes both a date range and a probability.
>
> — [[vacanti-actionable-agile-metrics]], L3534

> You should never—and I mean never—communicate a forecast that does not include at least two things: a date range and a probability for that date range occurring.
>
> — [[vacanti-actionable-agile-metrics]], L3530

## Reasoning

Vacanti's argument is that uncertainty about the future requires a probabilistic statement: "A forecast without an associated probability is deterministic, and, as you know, the future is anything but deterministic." (L3544). What breaks when the rule is ignored, as this wiki reads it, is the ability to check the statement afterwards: a bare date is simply hit or missed, and a miss cannot be told apart from an ordinary outcome that the distribution already allowed.

## Sign

A date in a plan, a milestone, a status answer or a reply to "when will this be done?" that states no probability, or a range that states none. As everywhere in this base, the sign raises a question and not a verdict; the question to check is what the date is. *Single-Date Plan* (below) is the wider failure.

## What separates neighbouring cases

- **Forecast versus estimate.** Vacanti allows that "an estimate can be thought of as a forecast" (L3526) but sets the forecasts of the chapter apart as "much more scientific than just some poor guy’s best guess" (L3526). This wiki reads the discriminator as the origin of the two numbers: a forecast's range and probability are computed from recorded data, for instance from [[service-level-expectation]]. An invented "90% sure" meets the form of the rule and misses its point.
- **Forecast versus deadline.** This distinction is ours, not the source's: a deadline is a date somebody demands, a forecast is a date somebody calculates. A deadline carrying no probability is not a violation; the violation is presenting one as the other. See [[estimate-versus-commitment]].
- **A date versus a count.** [[flow-metrics-scrum-teams]] applies the same pattern to how many items fit: "We have a 50% chance of getting 18 or more PBIs to done in this Sprint" (L958). This wiki notes that the range is open at one end. The book says a bare count misleads in a specific way: told "18", a reader assumes "the team has a 100% chance of getting exactly 18 items done" (L966), when the book puts that chance at about 6%. This wiki reads a bare count someone will rely on as the same sign as a bare date. The method is on [[throughput-monte-carlo]].
- **Time versus other forecasts.** Vacanti limits the chapter to completion times but says the principles "are applicable to any type of forecast" (L3528). This wiki reads that as covering a relative estimate once it is converted into a date: the points carry no date claim, and the conversion does.

## Which holds under which setup

Vacanti requires range and probability together. Cohn asks for a confidence, a range, or both, and this wiki already prefers the range where nothing produced a percentage (*Stating Plan Uncertainty* (below)). The resolution below is this wiki's, and it turns on what the project has recorded.

- **Per-item cycle times exist:** both parts are required, and they are read from the same percentile ([[service-level-expectation]], [[throughput-monte-carlo]]).
- **Finish dates exist and start dates do not:** a count or a date can still carry both parts, from daily Throughput ([[throughput-monte-carlo]]), because that needs only when items finished.
- **Only a velocity history exists, under iterations:** give the range with its basis, from [[velocity-range-forecast]] once four or more iterations have closed and from [[choosing-velocity-estimate-approach]] before that, and say that no probability was computed. That meets Cohn's form and half of Vacanti's rule, and the statement should not claim more.
- **No history of this project:** a range from [[choosing-velocity-estimate-approach]] (another project's history, a see-what-fits forecast or a labelled planned velocity), with no probability claimed, which meets Cohn's form and not Vacanti's. A figure with neither range nor basis is a guess and is labelled one. This wiki's position; the chapter does not address that case.

## Trade-off

The rule costs the appearance of commitment: the reader gets "43 days or less 85% of the time" (L3580) in place of a date, and the remaining share is stated openly. It also needs recorded history.

## Agent executor note

This wiki's reading is that the rule survives: it concerns the statement and not who does the work, and nothing in its mechanism relies on human pace or memory.

## See also

[[service-level-expectation]], [[throughput-monte-carlo]]

## Stating Plan Uncertainty

A plan that names one date and one fixed scope claims a certainty nobody has. Cohn: "No plan is certain. Be sure to include an expression of uncertainty in any release plan you produce." ([[cohn-agile-estimating-planning]] L4917). Summing points, dividing by a guessed velocity and reading off a date produces a precise-looking result from imprecise inputs. *Estimates as Ranges* (below) says why an early estimate carries a range, and *Single-Date Plan* (below) is the wider failure of a forecast that carries nothing else. This section says what form the statement takes and where the uncertainty goes.

### The mistake

Cohn's example is saying “we’ll ship on June 14, which is 7.2 iterations from now.” His objection:

> This is wrong because it gives the impression that the knowledge from which we construct the plan is sufficiently precise as to support this type of estimate.
>
> — [[cohn-agile-estimating-planning]], L4593

### The rule

Hold one of scope and date fixed and state the other as a range.

- **Scope fixed:** give a date range: “We’ll finish in the third quarter” or “we’ll finish in between 7 and 10 iterations” (L4917).
- **Date fixed:** give a scope range: “We’ll be done on December 31 and the product will include at least these new features but probably no more than those other new features.” (L4917).
- **Greater uncertainty:** "Use bigger units (iterations, months, then quarters, for example) when the amount of uncertainty is greater." (L4917).

For a target date, Cohn's alternatives (L4597-L4601) are to include "either your degree of confidence in the estimate, a range of possible dates, or both", for example:

- "I am 90% sure we’ll complete the planned functionality by July 31"
- "Based on our assumptions about the project size and team performance, the project will take three to four months."

### Range or confidence

Cohn allows either, but his chapter gives no way to derive a percentage. This wiki therefore prefers the range when generating output: [[velocity-range-forecast]] computes one from board history, while "90% sure" with nothing behind it is the same false precision in another form. A confidence belongs only where something produced it.

### What a good statement carries

Ron Jeffries' wording, quoted by Cohn, is the fullest model (L4605). This wiki extracts four parts from it:

- **Size:** "Right now, this appears to be a 200-point project."
- **Basis, stated even when weak:** "Based on our performance on other projects (or a random guess)".
- **Conditions and range:** "with N programmers on it, and your intimate involvement in the project, a project of this size will take between 4 and 6 months".
- **How it will change:** "As we go forward, we’ll all see how fast we’re progressing, and our estimate of the time needed will improve."

### The range survives the arithmetic

The fictional case study in Chapter 23 (L4961) shows a range defended against a figure that looks settled. Dividing 132 points by a planned velocity of 18 gives just over seven iterations (L6173). The product manager asks to call it seven, and the coach refuses:

> I’d prefer to give the estimate as a range. If we’re looking at enough work to go into an eighth iteration, we should probably say the project will take 6–10 iterations.
>
> — [[cohn-agile-estimating-planning]], L6179

At two weeks per iteration that is 12 to 20 weeks (L6181, L6185). The chapter gives no derivation for the range. This wiki computes the spread as about 18% below and 36% above the 7.33 point estimate, so it is deliberately wider on the late side. It rests on a planned velocity with no iteration finished ([[choosing-velocity-estimate-approach]]), so it should not be reused for a schedule with observed velocity behind it, which goes through [[velocity-range-forecast]].

**Failure mode: the range is heard as its low end.** The reply in the case is "I really don’t want this project to take 20 weeks. But you’re saying it might only take 12, right?" and the answer is "It might. But it might take 20," (L6181, L6183). Sign: notes downstream quote only the earlier bound. The sign is this wiki's.

**Scope is the lever that holds the range.**

> You can help it avoid taking 20 weeks by removing your lowest priority features if velocity shows that we’re headed toward 10 iterations. Keep in mind, too, that Delaney is actively looking for more features. If she comes up with something we’ll have to extend the schedule or take the same amount of current features out.
>
> — [[cohn-agile-estimating-planning]], L6183

This wiki reads that as saying the fact that shows the estimate wrong is observed velocity projecting past the upper bound, and the response is a change of scope and not a reworded date. Any addition carries a stated cost, either an extension or an equal removal. See [[replanning-on-new-knowledge]].

### Accurate versus precise

This distinction separates a good early plan from a bad one. "For a plan to be useful it must be accurate, but we accept that early plans will be imprecise." (L4841). Cohn's example, invented for the purpose: an early plan says 300–400 story points in the third quarter, and it turns out accurate when 305 are delivered in August, though it was never very precise. Later the same project's plan narrows to 380-400 points in September (L4841).

An imprecise plan can be right. A precise plan can be wrong. Early on, the range "may very likely be a sufficient basis for making decisions" (L4841), and that gives the test: a plan is precise enough when the decision waiting on it can be made. The purpose of a plan, per Cohn, is to serve as the basis for the organization's decisions (L4829), which is also [[good-plan-test]]. This wiki reads narrowing as something the plan owes only as those decisions come due, by way of [[replanning-on-new-knowledge]].

### Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Which of scope and date is fixed | The project's stated commitment ([[fitting-stories-into-a-release]]); if neither is, ask |
| Remaining size | The board, in the project's scale ([[size-versus-duration]]) |
| The rate | Board history; a range and not a single value where history varies |
| The decision the plan serves | Whoever asked for the forecast |

The choice was wrong if the outcome fell outside the stated range, which means the range was too narrow, or if the range was so wide that the decision could not be made from it. The table and these tests are this wiki's derivation. Chapter 22 gives no method for computing a range, and Chapter 21 gives [[velocity-range-forecast]].

### Sign of violation

- A release forecast with a single date and a fixed scope.
- A calendar date stated alone.
- An iteration count with a fractional part. This wiki reads the decimal in 7.2 as the clearest mark, because no period ends at 0.2.
- A precision out of keeping with its horizon, such as a day named two quarters ahead ([[planning-horizons]]).
- A date that stays the same across several closed periods, even though velocity has changed. Cohn: "Plans are updated throughout the project and these updates need to be communicated." (L4575)

The first four are this wiki's derivation.

### Trade-offs

A range reads as evasive to someone who needs a date, and someone may read only one end of it. The case study accepts that a demand for a figure will come anyway: "everyone wants to know at least an idea of what the schedule looks like" (L6189). Cohn's own qualifier is "When possible" (L4593-L4597). Jeffries' version makes a range easier to accept by promising frequent delivery and the right to stop at any point. This wiki reads that as setup-dependent: on a project that cannot ship until the end, the range has no such offset.

### Agent executor note

The rule rests on nothing specific to a human executor and survives. The plugin should give ranges and never a point when it plans a date. A short or newly changed history gives a wider honest range, which is the rule working as intended ([[filling-a-period]]).

See also [[a-date-is-not-urgency]], [[iteration-summary-plan-versus-fact]].

## Estimates as Ranges

A date given for uncertain work should show how uncertain it is. Cohn names ignored uncertainty the fourth cause of planning failure, and says it appears as false precision: we "pretend we can assign precise estimates (“2 weeks”) to imprecise work" ([[cohn-agile-estimating-planning]] L660), and schedules are "expressed as a single, unqualified date" (L662).

> During the earliest part of a project we are the most uncertain. The estimates we give should reflect our uncertainty. One way of doing this is by expressing the end date as a range.
>
> — [[cohn-agile-estimating-planning]], L662

Cohn's pair of examples is “We will ship on June 30,” against “We’ll ship sometime between June and August,” (L662). This wiki reads a range as one way of stating uncertainty and not the only one: Cohn says "One way".

### The rule

Give a date for uncertain work as a range, whose width reflects how much is still unknown. Narrow it as the unknowns are removed. Cohn's words are "As the project progresses and as uncertainty and risk are removed from the project, estimates can be refined and made more precise." (L662). This is the [[cone-of-uncertainty]] applied to a stated date, and *Single-Date Plan* (below) is the wider failure of a forecast that carries nothing else with it. What removes the unknowns is on [[replanning-on-new-knowledge]]. How a release plan words it, and which of scope or date takes the range, is on *Stating Plan Uncertainty* (above).

### Sign of violation

- **In a stated date:** a single date, with no range or stated uncertainty, for work not yet begun.
- **In board history:** the same width, or the same date, is repeated as the work proceeds, so nothing learned has reached the estimate.

The first is Cohn's. The second is this wiki's derivation.

### Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| How much of the work is still undone or unclear | Board state and task text |
| How similar work actually ran | Board history |

The range was wrong if actual finishes repeatedly land outside it, or if it never narrows. Cohn gives no method for setting the width in this chapter.

### Why

What breaks is what a listener takes from the number. This wiki reads a single date as seeming more known than it is, which invites [[estimate-versus-commitment]]. Cohn also says that plans which ignore uncertainty about how to build miss activities, which raises the chance of lateness, dropped features or inappropriate quality trade-offs (L680).

### Limit

Cohn's example is a project's end date, in months. This wiki reads the same reasoning as covering any stated date, and it does not extend to a size step, which states no date at all ([[size-ceiling]]).

### Cost

This wiki notes that a range does not give someone with a fixed deadline what they asked for, and a wide one can read as evasion. Choosing the date to hold to is then a separate decision ([[estimate-versus-commitment]]).

### Agent executor note

The rule concerns what is known and not who works, so it survives. This wiki adds a plugin-side consequence: anything the plugin says about when work will be done should come out as a range or as a forecast from history, because a point date from a tool reads as more exact than a person's guess. The width of an agent-executed project is unsourced here, and history from a different setup is a poor guide to it, as [[filling-a-period]] notes.

## Single-Date Plan

A single-date plan is a forecast stated as one date or duration with nothing showing how it was reached. Cohn's diagnosis:

> Far too often a plan is reduced to a single date and all of the assumptions and expectations that led to that date are forgotten.
>
> — [[cohn-agile-estimating-planning]], L457

### What an estimate does not promise

> A plan does not guarantee an exact set of features on an exact date at a specified cost.
>
> — [[cohn-agile-estimating-planning]], L457

Cohn says a plan "describes one possibility of what may come to pass" and establishes "a set of baseline expectations" (L457). Whether anyone has agreed to answer for a date is a separate question, on [[estimate-versus-commitment]].

### Why it breaks

The reader of a bare date cannot assess it. In Cohn's example, an answer of seven months with no explanation leaves no way to tell "whether I’ve thought about the question sufficiently or whether my estimate is realistic", and he concludes "You should be skeptical of my estimate." (L463).

This wiki adds that the bare date also claims more precision than the [[cone-of-uncertainty]] allows while work is unresolved, and that once the assumptions are gone, nobody can tell which change in fact should move the date.

### What the plan should carry instead

Cohn's alternative is a plan that (L465):

- estimates completion in a range: "seven to nine months"
- shows what work will be completed in the first one or two months
- documents key assumptions
- establishes an approach for how progress will be measured collaboratively

With these, Cohn says the reader "can look at my plan and draw conclusions about the confidence you should have in it." (L465). The rule for the range itself is on *Estimates as Ranges* (above). This section is the wider failure: a range with no assumptions and no near-term work still cannot be judged.

### Observable sign

The rule detects an omission, so the omission is its sign. This wiki reads it as: a forecast or milestone recorded as one date, with no range, no stated assumptions and no named near-term work. A sign raises a question; a date imposed from outside, such as a fixed event, is not an estimate, and the question there is what scope fits it. See [[replanning-on-new-knowledge]].

### Trade-off

This wiki notes that a range is less satisfying to the person asking and takes longer to produce. Cohn does not treat that as a reason to give one number. He expects precision to grow with time: early a plan may say the third quarter rather than the second, later it needs to be more exact (L469). See [[good-plan-test]].

### Agent executor note

This wiki reads the mechanism as surviving unchanged: the failure is on the reader's side, and the person steering is that reader. If anything an agent makes it worse, since it will produce a confident date on request. The plugin should not emit a date without its range and assumptions.

## Forecasting from an Average

**Forecasting from an average** means turning a mean, such as average throughput, average velocity or average cycle time, into a completion date. Vacanti rejects it outright: "You never want to make a forecast based on an average." ([[vacanti-actionable-agile-metrics]] L3552). The defect is that the result cannot carry a probability, so it fails Vacanti's rule at the top of this page by construction.

### Reasoning

Vacanti calls the average "a meaningless statistic unless you know something about the underlying distribution of the data from which the average was calculated" (L3552). Without the distribution, nobody knows which percentile the word "average" refers to:

> depending on the shape of the distribution, the mean could be significantly less than 50%, exactly 50%, or significantly more than 50%.
>
> — [[vacanti-actionable-agile-metrics]], L3558

Vacanti then closes the chain: "If we do not know the distribution, then we cannot give a probability of where the average falls. If we do not know a probability, then we cannot make a forecast." (L3560). This wiki reads the practical consequence as follows: a date from an average is not a coin-flip date either, since even "half the time" is an unsupported reading of it. The shape of real cycle times is on [[cycle-time-scatterplot]] and [[completion-time-distribution]].

### Sign

- A date whose working divides remaining items or points by an average rate.
- A figure labelled "average cycle time" or "average velocity" offered as the answer to "when?".
- A trend line through throughput read off as a release date; see *Straight-Line Projection of a Release Date* (below).

The question each sign raises is whether the distribution behind the number is known and whether a probability was stated. The first sign also describes Cohn's division by velocity; that disagreement is resolved on *Little's Law Does Not Forecast* (below).

### What to do instead

Vacanti's direction is to acquire the distribution: "Further, I would argue it is worth investing in acquiring that knowledge." (L3564), and with it to leave average-based methods for percentile-based ones. For one item that is [[service-level-expectation]]; for several, [[throughput-monte-carlo]].

### Trade-off

A percentile needs per-item history, not one rate. This wiki notes that the board history already holds it, so the cost is reading and not logging.

### See also

[[service-level-expectation]], [[throughput-monte-carlo]]

## Little's Law Does Not Forecast

[[littles-law]] describes a period that has already finished. It does not predict a coming one. Vacanti: "The first thing that you need to know about Little’s Law is that it is concerned with looking backward over a time period that has completed" ([[vacanti-actionable-agile-metrics]] L1078). Little's own phrasing, quoted by Vacanti, is that "we are in the measurement business, not the forecasting business" (L1078-L1084).

### What it cannot do

Vacanti's worked example: a team has average WIP of 20 items, average Cycle Time of 5 days and average Throughput of 4 items a day. Raising WIP to 40 and holding Cycle Time at 5 does not yield 8 items a day, "even if you add staff to the keep the WIP to staff ratio the same" (L1086). The law says only that a change in WIP results in a change to Cycle Time, Throughput or both, and that the result will still obey the relation. It does not say what the change will be (L1086).

His forecasting chapter gives two independent reasons (L1096 defers them to it):

1. **Assumptions cannot be foreseen.** It is "impossible to predict which of the Law’s assumptions will be violated in the future and how many times they will be violated", and "each violation of an assumption invalidates the exactness of the law" (L3550).
2. **It is a relationship of averages.** "You never want to make a forecast based on an average." (L3552). The law does not care about the underlying probability distributions, so it gives no probability, and a statement without one is not a forecast (L3560). See *Forecasting from an Average* (above) and Vacanti's rule at the top of this page.

### The rule

Vacanti draws the line by what the number is used for, so the input is the use, read from the plan or the question asked.

- **Allowed:** measuring a completed period, and quick estimates about the future, as a "quick gut-check to decide if something like a project is worth any further exploration" (L1098). A "gut check validation of a forecast for a _qualitative_ determination is perfectly acceptable" (L3562).
- **Not allowed:** the basis of a commitment. "I would not, however, make any commitments, staff hiring or firing decisions, or project cost calculations based on this type of calculation alone" (L1098). Chapter 14 repeats it: "you would not want to make any staffing, cost, or project commitments based on these back-of-the-envelope calculation type calculations" (L3562).

### Observable sign

This wiki's reading of where the violation shows: a date, plan or promise whose only derivation is open items divided by average Throughput, or a plan that expects Throughput to scale with added WIP. The question to check is whether the number was used to sanity-check a forecast or to produce one. The same applies to a plugin's own output. A figure computed this way must be labelled a rough check and must not be offered as a delivery date.

### What to use instead

Conformance comes first. Once a process mostly matches the assumptions, its data can be trusted and it is "probabilistically predictable", at which point something like [[throughput-monte-carlo]] on historical data can be used with some confidence in its results (L1088-L1094). Once distribution information exists, "we are going to run away from Little’s Law for forecasting" (L3564). The checks and the policies are on [[littles-law]].

Vacanti adds that predictability is not mainly about forecasts: "The bigger part of predictability is operating a system that behaves in a way that we expect it to" (L1100). See [[good-plan-test]].

### Discriminating test

Measuring asks what the averages were over a finished window. Forecasting asks what they will be. Only the first is the law; the second is a rough estimate whose quality depends on whether the future keeps the past's conditions.

### Positions

**Vacanti:** a forecast from averages is at most a gut-check (L1096-L1098).

**Cohn:** divides remaining points by measured velocity and repeats after every period ([[velocity-range-forecast]]). This wiki reads that as the same arithmetic as the sign above, in points per period and not items per day: both divide what is open by a mean rate.

### Which holds under which setup

The resolution is this wiki's, and it turns on how the figure is stated, since neither source tests its method against the other's. A single date from a division is a gut-check under any setup. Under an iteration setup, Cohn's division is acceptable as a forecast only in the form this base already requires: a range built from several velocity values ([[velocity-range-forecast]]), with its basis stated and redone each period (*Stating Plan Uncertainty* (above)). That keeps the method and answers Vacanti's objection to a deterministic result, though a range taken from a few means is not the probabilistic modelling he asks for. Under a flow setup the per-item forecast is [[service-level-expectation]].

### Trade-off

This wiki notes the cost of the rule: a rough figure is cheap, and refusing to promise from it means waiting for enough history to forecast probabilistically. A new project has no such history, so a gut-check may be all that is available. It should then be presented as exactly that.

### Agent executor note

The rule concerns arithmetic on past averages, so it survives. In this wiki's reading the warning weighs more with an agent: a change of model or review practice changes the system the history describes, so the assumption that the future keeps the past's conditions fails sooner.

## Straight-Line Projection of a Release Date

A **straight-line projection** extends a trend line from the throughput line of a burn-up chart until it meets the backlog line, then reads the date below the intersection as the release date. Vacanti's example of the reasoning: "If a backlog has 100 items in it and the team is averaging 10 items per week" ([[vacanti-actionable-agile-metrics]] L3592), the trend line gives the date. He does not recommend it for a completion date, "because both approaches are based on averages and neither give a probability of success" (L3634, the other approach being [[littles-law]]).

### What breaks

1. **It rests on an average**, with every problem in *Forecasting from an Average* (above) (L3594).
2. **Both lines move.** Vacanti notes "variability in both the Backlog and Average Throughput" (L3596), and that a single projected view "could cause managers to either panic or be overly confident depending on which way the variability pendulum swings on any given day" (L3596).
3. **There is no date range**, so it fails Vacanti's rule at the top of this page (L3598).
4. **Delivery is often not a line.** Vacanti observes that "any time you start a project with zero WIP and end with zero WIP, the resulting pattern of the Throughput line on the CFD mimics an “S-curve”" (L3606), and that "Using a straight line to approximate an S-curve is problematic at best and dangerous at worst." (L3606). See [[reading-a-cfd]].

### The patch that does not repair it

Advocates draw optimistic and pessimistic lines for backlog and throughput, which gives several intersections and hence a range. Vacanti grants this is better but asks how the lines were determined, and then: "But most importantly, what is the probability of hitting this range?" (L3604). This wiki reads that as a discriminating test for any cone-style chart: a range drawn by judgement meets half the rule, and the missing half is the one that makes it checkable.

### Sign

A release or project date read from the intersection of a trend line and a backlog line, with or without optimistic and pessimistic variants, and with no stated probability. The question to check is how the date will be used, as below.

### Decision: when it is tolerable

- **Gut check.** Vacanti allows it for "a quick gut check on project status" (L3608), but adds "any insight you may gain is certainly not actionable" (L3608), since acting on it "would probably be akin to tampering" (L3608).
- **A stabilised process.** Vacanti concedes the method degrades less under good process discipline: "If you truly can keep continuous WIP, minimally violate the assumptions of Little’s Law, not introduce CoS, then this type of approach might be good enough." (L3610-L3616). His stance there is permissive: "If it is and it works for you, then, great, keep doing it." (L3616)
- **Anything else.** A commitment should come from a method that yields a probability: [[service-level-expectation]] for one item, [[throughput-monte-carlo]] for many. A burn-up can be kept and improved with [[burn-up-with-percentile-lines]].

The inputs to this choice are read from board history: whether WIP stayed continuous or the project began and ended at zero, and whether classes of service were used. This wiki's reading of what would show the choice wrong is a projected date that keeps shifting from one reading to the next, as the second problem above predicts.

### Which holds under which setup

Cohn reads a finish date off a straight edge laid along a release burndown ([[release-burndown-chart]]). This wiki reads that as the same projection from the other direction. The resolution is this wiki's and follows the one on *Little's Law Does Not Forecast* (above). A single date read off any straight edge is a gut check under every setup. Under an iteration setup the division stays acceptable as a forecast only as a range with its basis ([[velocity-range-forecast]], *Stating Plan Uncertainty* (above)). Under a flow setup, percentiles replace it.

### Trade-off

The method is cheap and is easily explained to anyone reading the chart. Vacanti dismisses the heavier alternative of fitting S-curves, because those methods also come "with no range and probabilities attached" (L3606) and the effort is better spent on modern forecasting methods (L3606).

### See also

[[throughput-monte-carlo]], [[velocity-range-forecast]]

## An Estimate Is Not a Promise

An elapsed forecast is an estimate even when it is printed as a time. Cohn's example is the television guide listing a football game from 1:00 to 4:00: "most football fans know that when a football game is scheduled to end at 4:00 that is only an estimate" ([[cohn-agile-estimating-planning]] L1096). This section concerns how a forecast is received and what makes it safe. Whether anyone decided to hold to a date is the separate question on [[estimate-versus-commitment]].

> No one is surprised when the game goes till 4:15 (an overrun of 8%). They may be frustrated or annoyed, but not surprised. Why then are we surprised when a software project estimated at twelve months takes thirteen (an equivalent 8% overrun)?
>
> — [[cohn-agile-estimating-planning]], L1096

This wiki reads the 8% as arithmetic used for the comparison: fifteen minutes on three hours and one month on twelve. It is not a finding about how large an overrun is normal, and the chapter gives no such threshold.

### Why the network's forecast survives

Cohn lists what the network knows and the viewer does not (L1094):

- The content can flex: "they plan to add or remove a few commercials based on how quickly the game is progressing".
- The spread is narrow around the forecast: "most games are somewhere close to three hours".
- An early finish is absorbed by commercials, interviews or other filler.
- A late finish is tolerated: "If the game goes long, so what?" Interested viewers keep watching, and others wait if the delay is short.
- Expectation has been set: "after decades of televising football games, the networks have accustomed us not to expect a precise finish time".

Cohn calls the last of these the important difference (L1096). This wiki reads the list as saying that a date is safe because of the arrangements around it, and that accuracy is only part of it. A date is safer when scope can flex, history shows a narrow spread, the cost of lateness is low, and the reader knows it is an estimate. The list as a set of conditions is this wiki's arrangement; Cohn gives it as a description of one network.

### How to use it

This wiki reads the following checks as a way to apply this when a date is reported, since each condition can be read from the plan or the board:

- Is there scope that can be added or removed near the end? See [[fitting-stories-into-a-release]].
- Does history for similar work show a narrow spread? See [[velocity]].
- What does a late finish actually cost the person waiting?
- Has the person receiving the date been told it is an estimate? See *Estimates as Ranges* (above).

A date that fails all four raises a question about the plan. It does not show the estimate was wrong.

### Trade-offs

The football comparison has a limit that the source does not discuss. This wiki notes that the audience has decades of experience with the same event, while a software project is usually unique, so the narrow spread cannot be assumed. The comparison explains why surprise is unreasonable and gives no basis for assuming a software date will land within 8%.

### Agent executor note

This wiki reads this as independent of who executes: it concerns how a forecast is received, and that reader is the same person. Related: [[ideal-days]], where the problem is a number's meaning rather than its accuracy.
