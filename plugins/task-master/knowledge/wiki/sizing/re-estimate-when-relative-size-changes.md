---
title: Re-Estimate Only When Relative Size Changes
category: sizing
summary: Change an estimate only when belief about relative size changed, for a subset that can be named, never for slowness alone, which velocity absorbs; raising finished tasks after they ran long mixes scales (4.5 against 9 iterations). The first overrun of similar tasks is evidence about its siblings: revise durations, and relative sizes only for a shared, nameable cause.
tags: [decision-rule, estimation, velocity, story-points, re-estimation, failure-mode, board-history, rule, refinement]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Re-Estimate Only When Relative Size Changes

An existing estimate should be changed only when belief about a task's size *relative to other tasks* has changed. Taking longer than expected is not, on its own, a reason. The rule follows from what an estimate measures: size, not duration.

## Why the rule holds

Cohn says story points and ideal days estimate "the overall size and complexity of the feature being implemented", and "Story points in particular are not an estimate of the amount of time it takes to implement a feature" ([[cohn-agile-estimating-planning]] L1396). Duration is a function of two things: size and the rate of progress given by [[velocity]] (L1396). This wiki reads a task that ran long as carrying two possible explanations, of which only one concerns its size. Cohn's rule is that "we should re-estimate only when we believe a story’s relative size has changed" (L1398), and "Do not reestimate solely because progress is not coming as rapidly you as you’d expected" (L1512).

## The discriminating criterion

**Can the surprise be pointed at?** This wiki's reading of the two opposed cases in the source is that they differ on one question: can you name which remaining tasks the lesson applies to?

- *Not re-estimated.* Four stories were all estimated at 3 and two took twice as long. The team still believes all four are equivalent, so doubling the two forces doubling the other two, and "their situation is the same as if they’d left all the estimates at 3 and velocity at 6" (L1416-L1418). The lesson applied to everything, so nothing changed relative to anything else.
- *Re-estimated.* Six stories, of which three display charts. The team finds it "completely underestimated the general difficulty of displaying charts" (L1460). The lesson applies to a named subset, so that subset's size changed relative to the rest.

This wiki reads the first case as what [[velocity-self-correction]] absorbs. If no subset can be named, the difference belongs to velocity.

## The worked case: three scenarios

The setting: stories 1-6 estimated at 3, 5, 3, 3, 3, 5, with stories 1-3 being charts. The iteration planned stories 1, 2 and 6 (13 points). Stories 1 and 6 finished. Story 1 proved twice as big as estimated (L1449-L1460).

| Scenario | Estimates changed | Velocity read | Next plan | Result |
|---|---|---|---|---|
| No re-estimating | none | 8 | stories 2 and 3 are 8 points | Too much, because each chart is expected to be double: "It’s 8 points but it’s too much" (L1470) |
| Finished story only | story 1 to 6 | 11 | stories 2, 3, 4 are 11 points | The same problem: charts 2 and 3 still run double (L1474-L1476) |
| Whole class | stories 1, 2, 3 doubled | 11 | story 2 alone, now 10 points | The plan fits: "so big there is no room for an additional story" (L1480) |

This wiki draws two things from the table. Velocity is 11 in both the second and third scenarios, so the correction comes from the remaining estimates, not from the measured rate. And the third scenario does change a finished story's estimate, so this wiki reads the prohibition as narrower than a ban on touching finished tasks: what fails is changing a finished task *without* the open tasks of its kind (see *Hindsight Re-Estimation* (below)).

## How much to re-estimate

Cohn writes: "Whenever the team feels one or more stories are mis-estimated relative to other stories, re-estimate as few stories as possible to bring the relative estimates back in line" (L1506). He also warns: "Do not become overly concerned with the need to re-estimate" (L1506).

He adds that re-estimating should serve "as a learning experience for estimating future user stories" (L1508). This wiki takes the usable form of that to be: record the class of work that was mis-sized, so later estimates of that class start from the corrected comparison.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The finished task's estimate and how it actually went | The task and its board history |
| Open tasks of the same kind and their estimates | The backlog |
| Whether the surprise applies to some open tasks and not others | Comparing them, with the finished task as evidence |

These later facts are this wiki's derivations from the scenarios, not statements in the source.

- *Should have re-estimated:* a period planned to the measured velocity overruns again, and the overrun sits on tasks of the same kind as the earlier surprise.
- *Should not have re-estimated:* the re-estimated tasks finish in about the time their old estimates implied, or the re-estimated class turns out not to behave differently from the rest of the backlog.

## Trade-offs

These costs are this wiki's reading of the scenarios.

- Following the rule makes the next plan smaller at once. In the third scenario one story fills the iteration where the other two scenarios planned two or three. The forecast worsens early, which is the point, but it is a visible cost.
- Leaving a real change of relative size uncorrected costs an overfilled period, as in the first two scenarios.
- The rule asks for a judgement about a class of work from one finished task. In the source, the case is conditional: "Suppose that rather than one difficult story" (L1460). One story being hard is not yet evidence about its neighbours, and the source does not say how much evidence suffices.

## Relation to similar tasks overrunning together

*Similar Tasks Overrun Together* (below) says to revise the siblings when the first of a group overruns, which can read as contradicting this page's refusal to re-estimate for slowness. This wiki reads the two as one rule at two scopes. The siblings there are the named subset here, so Cohn's Chapter 2 and Chapter 7 agree. If "similar" turns out to mean every remaining task, nothing changes relative to anything else, and the correction belongs to velocity. The evidence needed is settled the same way on both: one overrun is enough to treat the siblings as suspect, and enough to revise them where estimates are durations; under relative estimates it is enough only when the cause is named and shared by a subset that can be pointed at. The source sets no count of overruns beyond that, and this wiki does not invent one.

## Agent executor note

This wiki expects the rule to survive an agent executing and a person steering, because it rests on the arithmetic of relative size, not on human memory or morale. The source's motive for the bad case, a team that "doesn’t feel good" about its velocity (L1416), is human, but the person steering can have the same motive. What may change with an agent is which classes of work get mis-sized; the source does not address this.

Related: [[story-points]], [[ideal-days]], [[velocity]], [[all-or-nothing-counting]]. A figure for work remaining on an open item is a different number and moves freely; see [[overrun-triggers-a-recut]].

## Hindsight Re-Estimation

Hindsight re-estimation is raising the estimates of tasks after they ran long, without moving comparable open tasks to the same scale. Velocity rises, the remaining total does not, and the forecast improves although nothing more was delivered.

### What breaks

The damage is a mixture of scales in one calculation: "I am mixing revised and original estimates" ([[cohn-agile-estimating-planning]] L1439). The source's arithmetic: fifty one-point stories, five finished in the first iteration of a planned ten. Re-estimating those five at 2 gives a velocity of 10 with 45 points left, so "I expect to finish the project in 4.5 iterations" (L1439). Left alone, velocity is 5 and the project takes 10 iterations in all (L1437). By this wiki's calculation, that means 4.5 iterations remaining against 9 for the same delivered work.

The revision cannot be extended to the open tasks to repair this: "when still looking forward at the remaining 45 stories I cannot predict which of those one-point stories I will want to say were worth two points in hindsight" (L1439).

The move also gains nothing even when applied evenly. Doubling every story doubles velocity and doubles remaining work, leaving "their situation" unchanged (L1418). This wiki concludes that, among re-estimates made because work ran slow, the only one that changes the forecast is the one that makes it wrong. A re-estimate of a whole class for a change in relative size is the exception, and it corrects the forecast (the rule at the top of this page, L1480).

A milder form appears in the worked case: re-estimating the finished chart story from 3 to 6 and leaving the other charts at their old estimates gives velocity 11 and an 11-point plan that the team "will not be able to" average (L1474-L1476).

### Observable signs

These signs are this wiki's derivations from the mechanism; the source states the mechanism, not a detection method. Each one raises a question.

- **In board history:** a task's estimate changed after it was closed, while open tasks of the same kind kept their estimates.
- **In period figures:** velocity rises between periods while the count of closed tasks does not.
- **In the forecast:** the projected finish moves earlier in a period that delivered no more than the one before.
- **In the stated reason:** the justification for an estimate change is that the task took longer, not that it was bigger compared with something named.

What to check: whether the change was applied to the whole class of work, as in the legitimate case in the rule at the top of this page, where finished and open chart stories were doubled together (L1480).

### Why it happens

In the source the trigger is disappointment. The team "doesn’t feel good about this" and doubles the points, after which their velocity is 12, "which they feel better about" (L1416). This wiki notes that the same pressure can reach a person steering an agent, because the figure reported upward is the one that improves.

Related: [[velocity-self-correction]], [[velocity]], [[all-or-nothing-counting]].

## Similar Tasks Overrun Together

Cohn's point is that the durations of software tasks are not statistically independent: how long one takes says something about how long its neighbours will take. Two consequences follow, which are that errors do not cancel in a total, and that an overrun on one task is evidence about the others.

> Activities are said to be independent if the duration of one activity does not influence the duration of another activity.
>
> — [[cohn-agile-estimating-planning]], L608

Cohn's contrast cases are coin flips and a house, where the time to excavate a basement says nothing about the time to paint the walls, so a late finish on one can be offset by an early finish on another (L608). His software case is a client application: if "the first screen takes 50% longer than scheduled there is a good chance that each of the remaining screens are also going to take longer than planned." (L610). This wiki reads the 50% as an illustration and not a measured figure, and Cohn does not say the rest overrun by the same proportion.

### The rule

> The real knowledge we should gain in a situation like this is that when an activity takes longer than planned, all similar activities are also likely to take longer than planned.
>
> — [[cohn-agile-estimating-planning]], L612

This wiki notes that Cohn's sentence says what the first overrun is evidence of and says nothing about re-estimating. Its setting is Chapter 2's critique of activity-based plans, where an estimate is a duration. For relative estimates Cohn says a story is not re-estimated "solely because" progress was slow (L1398, L1512), and a class is re-estimated when the team has "completely underestimated the general difficulty" of it (L1460).

The rule is therefore this wiki's reading. Treat the first overrun of a group as evidence about its siblings, and do not plan on recovering the time. Where estimates are durations, revise the siblings. Where they are relative sizes, revise them only when the cause is shared and the siblings can be named apart from the rest of the backlog; otherwise let velocity absorb the slowness (the rule at the top of this page).

This wiki reads that as applying to any forecast that adds estimates. Cohn says "If the activities of a development effort are not independent then variations in completion time will not balance out." (L610), so a total that assumes errors will wash out overstates its own confidence.

### Sign of violation

- **In a comment or report:** Cohn's stock phrase, “Yes, I was late this time but I’ll make it up on the rest.” (L612).
- **In board history:** one of a set of similar tasks ran well past its estimate for a cause the remaining ones will meet too, and their estimates did not change. Under relative estimates this fires only where those siblings can be named apart from the rest of the backlog; slowness spread over everything belongs to velocity. This reading is this wiki's.

### Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Estimate and actual of the first task | Task record and board history |
| Which tasks are similar | Task text: same kind of work, same parts of the system |
| Whether the overrun's cause is shared | The first task's record: was the cause particular to that task, or something the others will meet too |

The revision was wrong if the remaining tasks then finish at their original estimates. Cohn does not define "similar" and gives no multiplier, so this wiki sets none, and the third input is this wiki's own addition.

### Two meanings of independent

This word means something different on [[independent-tasks]]. There, Wake's sense is that tasks do not overlap and can be done in any order. Here, Cohn's sense is that their durations are uncorrelated. This wiki notes that the two are separate tests: a set of screens can pass the first and fail the second.

### When the first task really does pay for the rest

There is a real case where the first of a set absorbs most of the effort, as in Wake's "3 points for the first report, then 1 point for each of the others" ([[independent-tasks]]). Cohn rejects the belief that first-item learning makes up an overrun, describing it as a belief that "the knowledge gained from completing the first activity will allow the remaining similar activities to be completed more quickly than called for in the plan." (L612). This wiki reads the two as compatible: Cohn's rule concerns variance against the plan. If the plan already priced the first item higher, then an overrun beyond that price is still evidence about the rest, and the shared infrastructure does not excuse it.

### Why

What breaks if this is ignored is the earliest warning a plan gets. The first overrun is available well before the total is at risk, and treating it as a one-off leaves the plan wrong for the whole of the set. [[overrun-triggers-a-recut]] acts on the overrunning task. This rule acts on its siblings.

### Cost

This wiki notes that revising on one data point will sometimes overcorrect for a task whose trouble was particular to it, which is why the cause is an input.

### Agent executor note

The mechanism sits in the work, in shared unknowns and shared difficulty, so it survives an agent. This wiki adds that the excuse is weaker still with an agent: the expected recovery rests on knowledge carried from the first item to the next, and an agent carries that only if it is written down somewhere the next run reads. That point is unmeasured.
