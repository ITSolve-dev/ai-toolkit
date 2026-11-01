---
title: Re-Estimate Only When Relative Size Changes
category: sizing
summary: An estimate is changed when a task's size relative to other tasks has changed, not because the task took longer than expected; slow progress is absorbed by velocity, and a lesson about a class of work is applied to the whole class.
tags: [decision-rule, estimation, velocity, story-points, re-estimation]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
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

This wiki draws two things from the table. Velocity is 11 in both the second and third scenarios, so the correction comes from the remaining estimates, not from the measured rate. And the third scenario does change a finished story's estimate, so this wiki reads the prohibition as narrower than a ban on touching finished tasks: what fails is changing a finished task *without* the open tasks of its kind (see [[hindsight-re-estimation]]).

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

[[similar-tasks-overrun-together]] says to revise the siblings when the first of a group overruns, which can read as contradicting this page's refusal to re-estimate for slowness. This wiki reads the two as one rule at two scopes. The siblings there are the named subset here, so Cohn's Chapter 2 and Chapter 7 agree. If "similar" turns out to mean every remaining task, nothing changes relative to anything else, and the correction belongs to velocity.

## Agent executor note

This wiki expects the rule to survive an agent executing and a person steering, because it rests on the arithmetic of relative size, not on human memory or morale. The source's motive for the bad case, a team that "doesn’t feel good" about its velocity (L1416), is human, but the person steering can have the same motive. What may change with an agent is which classes of work get mis-sized; the source does not address this.

Related: [[story-points]], [[ideal-days]], [[velocity]], [[partial-credit-for-unfinished-tasks]]. A figure for work remaining on an open item is a different number and moves freely; see [[re-estimate-remaining-work]].
