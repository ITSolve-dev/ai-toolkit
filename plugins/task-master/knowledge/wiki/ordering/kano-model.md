---
title: Kano Model
category: ordering
summary: Kano's model sorts features by how satisfaction responds to presence and absence: threshold, linear, exciter. Within a release, take all must-haves, then as many linear features as fit, then a few exciters, and no indifferent ones; a must-have constrains membership and not position or urgency. A category is measured by a paired questionnaire (two peaks in one row mean two populations) or guessed and labelled as a guess, decays over time, and is an input a stated reason can override; Kano decides membership where users can be reached, and relative weighting ranks what remains.
tags: [concept, ordering, prioritization, value, kano, decision-rule, release, method]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Kano Model

The Kano model sorts the features of a product by how customer satisfaction responds to them. It originates with Noriaki Kano (1984), and Cohn uses it to decide "how to prioritize work for a new product release" ([[cohn-agile-estimating-planning]] L2384). The model says what kind of thing a feature is. The order that follows is on *Ordering by Kano Category* (below), and the way to measure a category instead of guessing it is on *Kano Questionnaire* (below).

## The three categories

| Category | Other names | When present | When absent | Line |
|---|---|---|---|---|
| Threshold | Must-have, basic | Adds little: "Improving the performance or amount of a threshold feature will have little impact on customer satisfaction." | The feature "must be present in the product for it to be successful" | L2392 |
| Linear | Performance, one-dimensional | "customer satisfaction is correlated linearly with the quantity of the feature" | Less of it, less satisfaction | L2394 |
| Exciter | Delighter, unknown need | Great satisfaction, and even a partial implementation raises it sharply | "the lack of an exciter or delighter will not decrease customer satisfaction below neutral" | L2396, L2400 |

Two further limits come with these. For a threshold feature, "no matter how much of a must-have feature is added, customer satisfaction never rises above the mid-point." (L2398). For a linear feature, "product price is often related to linear attributes" (L2394). Exciters are called unknown needs because "customers or users do not know they need these features until they see them" (L2396). This wiki reads that as the reason a request rarely names one.

## What separates them

This wiki reads the three categories as one discriminating test: an asymmetry between presence and absence.

- Absence hurts and presence does not help: threshold.
- Presence helps and absence does not hurt: exciter.
- Both directions move satisfaction: linear.

The consequence is that a single rating of value cannot separate a threshold feature from an exciter, since both can be called valuable and they call for opposite handling. The fictional case study in Chapter 23 (L4961) states the mechanism when a product manager asks why a 1-to-5 importance rating would not do:

> A single scale like that just tells us how strongly a user values a feature. It doesn’t tell us how strongly the user would react to the absence of the feature. I wouldn’t prioritize wheels very highly if you asked me about features on a car but I’d be mad if you took them away.
>
> — [[cohn-agile-estimating-planning]], L5634-L5638

This wiki reads that as saying importance and reaction to absence are two different measurements, and a feature can be low on one and high on the other. That is the reason [[relative-weighting]] scores absence separately, and why the Killer band of [[ordering-by-value-and-urgency]] names both what doing a thing gains and what not doing it loses.

## The categories in the case study

The chapter uses the model without naming it and points to Chapter 11 for the method (L5943). Its names are mandatory, linear and exciter, and it adds what the table above leaves out. The speakers are characters.

**Mandatory is the cost of entry.** Some features are so obvious that the analyst does not ask about them: "Supporting them is really the cost of entry." (L5992).

**Linear does not mean optional.** An artist objects that art cannot be optional, and the analyst separates a floor from a slope: "I didn’t say these are optional, Rose," then "There is a certain baseline we can’t fall below" and "These are linear because the more of them the better." (L6050). This wiki reads that as the discriminating criterion: a linear feature can carry a mandatory minimum, so the category does not license dropping it whole.

**Few exciters is an unfinished search.** "Remember that exciters are unexpected features." and "Every product should have at least one or two exciters" (L5984). A survey showing few of them is read as a reason for open-ended interviews, and not as a dull product (L5984). This wiki reads that as following from an exciter being an unknown need: a list built from what is already asked for has little chance of holding one.

**Indifferent is a fourth outcome.** "it just means that the person didn’t have a strong preference either way" (L5972). What the chapter does with such features is on *Ordering by Kano Category* (below).

## Categories decay

> Keep in mind that features tend to migrate down the Kano diagram over time. A short time ago, wireless Internet access in a hotel room was a delighter. Now it’s a linear feature well on its way to becoming a threshold feature.
>
> — [[cohn-agile-estimating-planning]], L2419

This wiki reads that as saying a category carries a date, like any rating ([[ordering-by-value-and-urgency]], step 5). The direction runs one way in the source's example: exciter, then linear, then threshold. This wiki takes the observable sign to be users beginning to object to the absence of something recorded as an exciter. A category kept from an earlier release should be asked again before it decides anything, and the source gives no figure for how fast this happens.

## What the model is applied to

The source classifies features and themes ([[theme]], L2423), and all its examples are things a user meets in the product. This wiki's reading is that a technical task has no category of its own. It takes the category of the theme it serves, through its stated purpose ([[task-must-justify-itself]]). A task that serves no theme cannot be classified, and goes to [[incomparable-tasks]].

A category also belongs to a population and not to the feature alone: this wiki reads the two-peak rows on *Kano Questionnaire* (below) as meaning the same feature can be a must-have for one group of users and an exciter for another.

## Setting

The source's setting is a product with customers, a market and releases, and the example is a website with prospective users. A project with no users outside the people steering it has no satisfaction curve to read, so the model tells it little. That limit is this wiki's.

## Agent executor note

The model concerns the reaction of users, not the executor, so it survives an agent executing. A category is a task-only fact in the sense of [[recoverable-versus-task-only-facts]]: the repository cannot show how users would feel. The plugin can propose a category and a person confirms it.

## Ordering by Kano Category

This rule chooses what goes into a release from the categories of the *Kano Model* (above). It gives three tiers of emphasis, and this wiki reads it as a rule about what belongs in the release rather than a sequence of work.

### The rule

1. **All threshold features.** "emphasis should be placed on prioritizing the development of all threshold features" ([[cohn-agile-estimating-planning]] L2413), because must-haves are "required for a product to even play in its market segment" (L2413).
2. **As many linear features as fit.** "Secondary emphasis should be placed on completing as many linear features as possible." (L2415), since each adds satisfaction directly. The source's exception: "(Excluding, of course, such situations as a product that is already bloated with too many features.)" (L2415).
3. **A few exciters.** "Finally and with time permitting, at least a few delighters should be prioritized such that they are included in the release plan." (L2415).

### Must-have does not mean first

This is the discriminating criterion of the page:

> A product’s must-have features do not need to be developed in the first iterations of a release. However, since users consider these features as mandatory, they need to be available before the product is released.
>
> — [[cohn-agile-estimating-planning]], L2413

This wiki reads a must-have as a constraint on membership of the release and not on position within it. The position is left to other factors, and the chapter's own summary lists learning and risk among them (L2547-L2555). A task's place in the queue should not be read off its category, and calling a feature a must-have says nothing on [[urgent-versus-important]]: it is a statement of importance only. That page agrees: its release test (would this block the next release) applies to defects and requests against a release under way, not to planned must-haves, whose urgency rises only as the release date approaches ([[a-date-is-not-urgency]]).

### How much of a must-have

The tier asks for presence and not excellence: "partial implementation of must-have features may be adequate since gains in customer satisfaction drop off quickly after a base level of support for threshold features has been established" (L2413). The source's example is one level of undo in FrameMaker: "For me personally they moved pretty far up the customer satisfaction axis with a one-level undo feature, yet I would have preferred much more." (L2413). This wiki reads that as one user's report and not a measurement, and the author's closing clause as a reminder that adequate is not the same as satisfying.

The mirror case for exciters comes from the model: even a partial implementation raises satisfaction sharply (L2400). This wiki reads both as arguments for cutting small in these two tiers ([[vertical-slice]]), and for spending the depth on the linear tier, which is the only one where more keeps paying.

### Worked walk through a release

The fictional case study in Chapter 23 (L4961) assembles a release scope by walking the categories in order with points in view, and divides by velocity only afterwards. Scope is decided first: "I have no idea yet. Let’s figure out what you want and then we can see how long it will take," (L6129-L6131). The figures are illustrations.

| Step | Available | Taken | Running total |
|---|---|---|---|
| Mandatory by judgement | 32 | 32 | 32 |
| Mandatory by survey | 56 | 56 | 88 |
| Linear | 32 | 32 | 120 |
| Exciters | 20 | 12 | 132 |
| Indifferent | 6 | 0 | 132 |

The table sums L6012, L6038, L6070, L6086, L6101 and L6145. The reasoning at each step:

- **Mandatory:** all in (L6111-L6113).
- **Linear:** by judgement of how much is enough. The product manager takes all of them, including a cheap one on cost alone: "Maybe the user can’t change songs but that’s only 1 point so for now I’m going to say we want it." (L6117).
- **Exciters:** a couple, weighed by cost. A programmer reminds the room of the bad-move warning, "Remember, that’s an 8-point story," and "I can enhance it to find really bad moves but it’s not trivial." (L6135). The product manager drops it and keeps the 3-point warning that blocks a losing move (L6139).
- **Indifferent:** out. "We’re unlikely to sell more games or games at a higher price from adding features that players are indifferent about." (L6090).

#### A category is an input and not a verdict

The analyst overrides the data twice and says why. A strong opponent goes in as mandatory because "I think many users will outgrow what you’re defining as the medium-strength engine." (L6020). Playing another human scored 58 indifferent (L5954) and goes in anyway: "I’ve included that as mandatory because we’ve already said it’s a good milestone." (L6044). This wiki reads the second as a sequencing reason legitimately outranking a value reading, and the stated reason as what marks an override as sound. Annotated saved games, with a mandatory and indifferent split much like the strong opponent's (L5962), is left out with no reason stated, and the source does not say why the two were treated differently.

#### Failure mode: everything is in

The product manager says it himself: "I know. I want it all, right? Just like every product manager in the world." (L6121). The sign is that nothing, or almost nothing, sits below the line. This wiki notes that in the case 132 of 146 points are in, so only 14 lie outside, which leaves little to cut if velocity runs to the long end, and the cut would come from linear features already selected. The range and its lever are on [[forecast-range-and-probability]], and the first figure for velocity on [[choosing-velocity-estimate-approach]].

### Signs this rule detects

- **A must-have outside the plan.** A theme classed as must-have has no task in the release, or its tasks are open as the release date comes up. Read this from board state.
- **Gold-plating a threshold feature.** A task deepens a must-have that already has base-level support, while linear features wait. The sign is in the task's text: a further level or further options of something users already take for granted.
- **Exciters ahead of must-haves.** The plan contains exciters while a must-have is unscheduled.
- **An override with no reason.** A theme sits in a tier its category does not give it, and nothing says why.

These signs are this wiki's application. A sign raises a question: the category may be stale (see *Categories decay*, above) or wrong.

### Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Each theme's category | *Kano Questionnaire* (below), or a guess a person confirms, with its origin stated |
| Each task's size | Its estimate on the project's scale |
| Which tasks belong to which theme | Each task's stated purpose ([[task-must-justify-itself]]) |
| What base-level support means for this feature | The person steering, or the acceptance criteria ([[testable-acceptance]]) |
| Whether the product is bloated | The person steering; the source gives no measure |
| What fits | The release's capacity ([[fitting-stories-into-a-release]]) |

The source gives no tests of the choice, so these are this wiki's.

- **A must-have was overrated** if the release went out without it, or with a partial version, and users did not object.
- **A must-have was missed** if users rejected or avoided the release over something classed lower.
- **Depth was misjudged** if complaints after release name the limit of a partial must-have.
- **A category had gone stale** if users object to the absence of something recorded as an exciter.
- **The scope was too full** if observed velocity projects past the stated range ([[forecast-range-and-probability]]), or a newly found exciter forces an extension or an equal removal (L6183).

### Setting

The rule assumes a release with an edge. With periods or milestones on the board it reads directly: must-haves gate the milestone. In continuous flow with no release, this wiki has no source for the gate, and reads it as the next point at which users receive the product. The tiers still rank, and nothing marks when the must-have tier has to be complete.

### Cost

Chapter 11's rule ignores cost within and across tiers, so a costly must-have outranks a cheap linear feature whatever the return ([[relative-weighting]] sees that and this rule does not). The case study weighs cost by hand inside the linear and exciter tiers, as above, and not across them. It also needs a category per theme, which is a survey or a guess. Holding all exciters to "time permitting" risks shipping none, and the source guards against that only with "at least a few".

### Agent executor note

The tiers concern users and survive. This wiki expects the gold-plating sign to matter more with an agent, because adding more is cheap for the executor while the people steering still have to review it. That extension is unmeasured.

## Kano Questionnaire

This procedure replaces a guess about a feature's category on the model (above) with an answer from users. The source ranks the two ways plainly:

> The easiest way to make use of a Kano model on an agile project is to think about each theme and make an educated guess about the type of each. A much better way, however, is to speak with customers or users in order to truly determine the type of each theme.
>
> — [[cohn-agile-estimating-planning]], L2423

### Procedure

1. **Write two forms of one question per feature.** The functional form asks how the user would feel if the feature were present, the dysfunctional form how they would feel if it were absent: "If you can graph a swimmer’s times in an event over the past season, how do you feel?" and its "cannot" twin (L2447-L2449).
2. **Offer the same five answers to both:** I like it that way; I expect it to be that way; I am neutral; I can live with it that way; I dislike it that way (L2427-L2435).
3. **Cross-reference each user's pair** in the table below, so that "a prospective user’s responses can be reduced to a single meaning" (L2479).
4. **Aggregate across users** into a percentage distribution per feature, and read the category from it (L2490).
5. **Where a row has two high values, split the respondents** before reading it (L2502-L2506).

### The cross-reference table

Rows are the answer to the functional question, columns the answer to the dysfunctional one. M is must-have, L linear, E exciter, I indifferent, R reverse, Q questionable.

| Functional / Dysfunctional | Like | Expect | Neutral | Live with | Dislike |
|---|---|---|---|---|---|
| Like | Q | E | E | E | L |
| Expect | R | I | I | I | M |
| Neutral | R | I | I | I | M |
| Live with | R | I | I | I | M |
| Dislike | R | R | R | R | Q |

This table is rebuilt from the extracted text of Figure 11.3 (L2488), not from an image. Two cells can be checked against the prose: expect plus dislike gives must-have (L2479-L2483, L5609-L5613), and like plus neutral gives exciter, where the user "may be willing to pay extra for it" (L5630).

The source defines Q by example, where a user likes having a feature and also likes not having it: "it is possible for a user to give inconsistent responses" (L2477). Chapter 11 gives I and R only as labels. This wiki reads I as a user who does not care either way and R as a user who prefers the feature absent. Chapter 23 confirms the first: "it just means that the person didn’t have a strong preference either way" (L5972). Its example of an unreadable answer is "someone said they dislike background music but that they also dislike it when there’s no background music" (L5976), and it uses the low values of reverse and questionable as reassurance (L5976). A large I share is, on this wiki's reading, a reason to ask whether the feature should be built at all, and the chapter leaves such features out (*Ordering by Kano Category* (above)).

### Keeping it short

The fictional case study in Chapter 23 (L4961) shows two moves that limit the list, and its figures are illustrations and say nothing about response rates.

- **Group stories into themes.** "I can group some of the user stories we identified into _themes._" (L5646), so two background-music stories become one question. The [[theme]] is the unit Chapter 11 classifies. The trade-off comes with it: "The longer the questionnaire, the lower the response rate" and "if I combine too many stories into one question the answers we get back may not be very useful." (L5968).
- **Do not ask what is known.** "I’m not going to waste time asking about saving games and restoring games. We know those are mandatory features." (L5646).

The case's numbers are just over 500 email invitations, 35 phone calls and 78 answers (L5943), against an expected "50 or so responses" (L5642). The questionnaire has 24 questions, about 15 minutes by phone and 7 on average online (L6107).

### Worked distribution

Table 11.1 (L2494-L2498), percentages of respondents:

| Theme | E | L | M | I | R | Q | Category |
|---|---|---|---|---|---|---|---|
| Graph event times | 18.4 | 43.8 | 22.8 | 12.8 | 1.7 | 0.5 | Linear |
| Can upload photos | 8.3 | 30.9 | 54.3 | 4.2 | 1.4 | 0.9 | Must-have |
| Post autobiographical profile | 39.1 | 14.8 | 36.6 | 8.2 | 0.2 | 1.1 | Exciter / Must-have |

The category is read "From observation of this table" (L2490), and no cut-off is given. The figures are the book's illustration and not a measurement.

### How many users

The figure is that "you may need to survey as few as 20–30 users to accurately prioritize requirements" (L2423), cited to Griffin and Hauser (1993). The chapter does not give the setting that produced it, so this wiki holds it as an order of magnitude only. Splitting by sub-population divides the same respondents, so the number that suffices for one homogeneous group does not obviously suffice for each of several. That caution is ours.

### Failure modes

- **Two peaks read as one category.** The sign is a row with two high values, as with the profile at 39.1 and 36.6. The source's reading: "This indicates that different types of customers and users have different expectations." (L2502). This wiki adds that taking the top value would file the profile as an exciter while over a third of respondents treat it as mandatory. The remedy is to analyse by a factor that differentiates respondents, such as company size, job role or industry segment (L2506). Chapter 23 shows the same row in its own data: a strong opponent scores 39 mandatory and 32 indifferent (L5953), someone asks why not take the highest value (L5978), and the analyst answers "The reason we see two spikes in the values for a strong opponent is that we are probably selling into two audiences" (L5980). This wiki reads that as a rule: when two categories are close, report the split, since the top value alone would hide a group of buyers.
- **Asking only about presence.** This wiki's reading is that almost any feature is liked when offered, so the dysfunctional form is what separates a must-have from an exciter. The source's own wording is that "We need a way for looking at both answers simultaneously" (L2477), and the mechanism is on *Kano Model* (above). The sign is a questionnaire, or a value rating, with no question about absence. See [[relative-weighting]].
- **A guess recorded as a measurement.** The source accepts the educated guess as the easy way. The sign, on this wiki's reading, is a category on a task with no note of where it came from; the origin should be stated.

### Defects in the source's text

The chapter's example was renamed incompletely, and a reader checking citations will meet the leftovers. The prose says "reviews on the website are a threshold feature" (L2483), then "reviews are a one-dimenstional (linear) feature and that shipping options are a mandatory (threshold) feature" (L2490), and later refers to "detailed photos" (L2502). No such rows exist in the table. This wiki reads them as Graph event times, Can upload photos and Post autobiographical profile, by position and by the Category column. Table 11.2 also disagrees with this table about photos: see [[relative-weighting]].

### Cost

The source calls this "surprisingly easy because it can be done with a written questionnaire" (L2423). This wiki reads that as a claim about effort, assuming users can be reached. It costs a pair of questions per feature for each respondent. It yields a category only: nothing in it sees cost, so it cannot rank within a category. *Kano or Relative Weighting* (below) says when to pay for it.

### Agent executor note

The plugin can draft the question pairs and tabulate answers. It cannot supply the answers. An agent answering in the users' place produces the educated guess and not the survey, and should be labelled as a guess. For a few people steering an agent the method holds only where a population of users exists to ask, which the charter's scale does not guarantee.

This wiki's adaptation, which no source tests, is to keep the paired question as a prompt for the person ordering the work: what happens if this is never built? That keeps the test of absence without the survey, at the cost of replacing users' reactions with one person's guess, and the result is labelled that way, as on *Kano or Relative Weighting* (below).

## Kano or Relative Weighting

The chapter presents two ways to judge desirability and leaves the choice open, asking only what the relative merits are in the reader's organization ([[cohn-agile-estimating-planning]] L2565). The charter requires a disagreement to be resolved per setting, so **everything in the resolution below is this wiki's reading of sourced positions.** The two methods also answer different questions, so in most settings they are steps and not rivals.

### How they differ

| | *Kano Questionnaire* (above) | [[relative-weighting]] |
|---|---|---|
| Evidence | Users' answers; the fallback is an educated guess (L2423) | "expert judgment" (L2510) |
| Result | A category | A number per feature |
| Sees presence and absence | Yes | Yes, as benefit and penalty ([[relative-weighting]], its penalty section) |
| Sees cost | No | Yes |
| Treats a must-have as | Required, whatever else is on offer (*Ordering by Kano Category* (above)) | One high score among others |
| Needs | Reachable users, about 20-30 by the source's figure | Judges and an estimate per feature |

The row on must-haves is the real disagreement. Kano's tiers are non-compensatory: no amount of linear value replaces a threshold feature. Relative weighting is compensatory: a low ratio simply ranks low. The compliance feature on [[relative-weighting]] shows the gap.

### The rule

1. **Filter first.** A feature whose absence cannot be accepted is taken out of the ranking and placed by constraint. This applies whichever method follows, and it holds even where no survey is possible.
2. **If users can be reached and what you lack is knowledge of their reaction,** classify by Kano. This fits a new product or a [[theme]] whose users' reaction nobody on the project can predict.
3. **If users cannot be reached, or the people steering already know the domain,** use relative weighting, or a classification by educated guess, stated as a guess.
4. **Within what remains, rank by value per cost** using relative weighting. Kano cannot rank within a category.
5. **If tasks differ in what waiting does to them, neither method suffices.** Use [[ordering-by-value-and-urgency]], with [[cost-of-delay-over-duration]] inside a rank. Neither of the two instruments here has a term for urgency.

Dependencies constrain any result ([[sequence-versus-wait]]).

### Per project setup

| Setup | Holds |
|---|---|
| A release or milestone with a scope to choose, and users to ask | Kano for membership, then relative weighting inside the linear tier |
| A release or milestone with a scope to choose, and no users to ask | Filter, then relative weighting |
| Continuous flow with a queue of mixed requests | [[ordering-by-value-and-urgency]]; the absence question goes into the value band, and Kano adds little without a release to gate |
| Internal tool with its users among the people steering | A survey has no population. Ask them directly and use relative weighting |

### Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Is there an unacceptable absence? | The request and the person steering ([[relative-weighting]]) |
| Can users be reached, and how many? | The person steering; the project setup |
| Is the scope being chosen for a date or milestone? | The board's setup: periods, milestones, or flow |
| Do the tasks differ in urgency? | [[urgent-versus-important]] |

The choice of method was wrong in these ways, all this wiki's:

- **Weighting was used where Kano was needed:** a high-ranked feature shipped and users were indifferent, or a low-ranked one turned out to be mandatory for them.
- **Kano was used where it was not needed:** the survey cost a round of waiting and changed nothing in the plan.
- **The filter was too wide:** most of the list counted as unacceptable to omit, and the ranking stopped deciding anything. That is [[priority-inflation]] under a different name.

### Cost

Doing both means two sets of judgement for one decision. The filter in step 1 can be abused, since it removes a task from all comparison, and only a person who owns the loss should apply it. The setups table has not been tested on a real project.

### Agent executor note

The plugin knows the project setup and can pick the branch. The judgements inside the branch stay with the people steering. Asking them for a full table per task would spend the budget [[clarifying-questions]] protects, so this wiki reads step 3's cheaper path as the default for a few people, with Kano reserved for the case where they say they do not know how users will react.
