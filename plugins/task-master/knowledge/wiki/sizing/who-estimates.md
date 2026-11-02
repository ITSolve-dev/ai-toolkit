---
title: Who Estimates
category: sizing
summary: An estimate is shared and not one expert's: the executor may not be known, others remember past misses, a surprising number exposes a misunderstanding, and a time estimate binds to one executor (two runners). With an agent executing the executor is known but the estimator usually is not it, so a check against a second source and board history is the default; the problem returns when the executor changes.
tags: [rule, estimation, shared-estimate, cohn, failure-mode, ideal-days, discriminating-criterion]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Who Estimates

Cohn's position is that an estimate is shared: "Agile teams do not rely on a single expert to estimate." ([[cohn-agile-estimating-planning]] L1212). This rule chooses who supplies an estimate. Applied to a person steering an agent, its reasons do not transfer evenly, and that is the part that matters here.

## The rule

> Despite well-known evidence that estimates prepared by those who will do the work are better than estimates prepared by anyone else (Lederer 1992), estimates are best derived collaboratively by the team, which includes those who will do the work.
>
> — [[cohn-agile-estimating-planning]], L1212

This wiki notes that the sentence concedes the evidence and then overrides it for two reasons of Cohn's. The later citation points the same way: Jørgensen is quoted as concluding that "the people most competent in solving the task should estimate it." (L1362). This wiki has read neither study. The Scrum Guide's position on who sizes is on [[filling-a-period]].

## The two reasons

**The executor is not known yet.** A specialist may be busy when the time comes. "So, since anyone may work on anything, it is important that everyone have input into the estimate." (L1214).

**Others catch what the estimator forgets.** Someone who could not do the work may still recall how it went: "Kristy, you’re nuts; the last time you worked on a feature like that it took a lot longer. I think you’re forgetting how hard it was last time." (L1216). Cohn's report of the outcome is his experience and not a measurement: "However, more often than not in my experience, she will acknowledge that she was indeed underestimating the feature." (L1216).

## Who counts

- All disciplines that touch the work. Cohn's "developers" covers programmers, testers, database engineers, analysts and designers (L1312).
- Not the person who wants the work: "The product owner participates in planning poker but does not estimate." (L1312). The chapter gives no reason. The role is kept for answering questions (L1316).
- At least two people. Even when estimating in spare moments Cohn says: "I’d prefer that when someone has a few spare minutes to devote to estimating that he find at least one other person and that they estimate jointly." (L1356). For sub-groups of a larger team he asks for "at least three estimators" per group (L1344), a condition of a scale this wiki does not address.

## Failure sign

A task whose estimate was set by one person, or by the requester, with no other input. Board history may show who set the field. It will not show a conversation, so the sign raises a question only, per [[smell-is-not-a-finding]]. This sign is ours.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Who executes | Project setup, or the task's assignee if set |
| Who reviews and steers | Project setup |
| Who asked for the work | The task or the originating request |

The choice was wrong if finished work repeatedly lands far from its estimate in a way someone present could have predicted, for instance for a kind of work the project has done before. That reading is ours.

## Agent executor note

The transfer here is ours, and no source in this chapter treats it.

When an agent executes, the first reason as Cohn states it mostly falls away, because the executor is known in advance. What it protected does not: the estimate is usually made by someone other than that executor, the plugin or a person steering, so the Lederer advantage of the doer's own estimate is not on offer either, and a check by a second source stays the default. That check now rests on the second reason, not the first. The Lederer point also becomes awkward: "those who will do the work" would be the agent, and these sources say nothing about whether an agent's estimate of its own work has that advantage.

The second reason survives, in a changed form. What Kristy's colleague supplies is a memory of how similar work actually went. On a project steered by few people, that memory is in the steering person and in the board's history. So the plugin's estimate is a proposal that a person who remembers can correct, set against evidence from similar finished tasks, as on [[triangulation]]. It should not stand as a sole opinion. How the two views are compared is on [[independent-estimates]].

The product owner's exclusion is a question for a project of one or two people, where the person who wants the work may be the only person available. Chapter 6 does not treat that case. This wiki would keep the separation where there is a second person and otherwise record that the estimate is single-sourced.

## Collaborative Task Estimation

Collaborative estimation means that a number is produced or challenged by more than the person expected to do the work. The story-level position and who counts as an estimator are on the rule at the top of this page. This section holds Cohn's fuller argument from iteration planning, which adds two reasons to that one. Cohn accepts the standard advice that the best estimates come from those who will do the work, citing Lederer and Prasad 1992, and still holds that "task estimating on an agile project should be a group endeavor" ([[cohn-agile-estimating-planning]] L3248). His claim is made at the level below this wiki's task ([[unit-of-work]]), and this wiki carries the reasoning up to its own level.

### Cohn's reasons

1. **The doer is not yet known.** Tasks are not allocated during planning, so there is no specific person to ask (L3248). See [[tasks-are-not-assigned-at-planning]].
2. **Others hold the memory of past misses.** James says a task will take two hours. A colleague answers: "But, James, the last time you worked on a similar task you thought it would be two hours and it took you sixteen." (L3250). James then either gives a real reason this case differs or admits to a cost he has been forgetting (L3250). The fictional case study in Chapter 23 (L4961) plays the same scene: a colleague tells a programmer he is "always optimistic at the start of a new engine" (L5738), and his 6-hour card becomes 12 (L5734-L5742). This wiki keeps the mechanism, a peer who remembers the estimator's record, and not the factor of two, which is an anecdote in a fiction.
3. **A number exposes a misunderstanding.** "Upon hearing an unexpectedly high estimate, a product owner or analyst may discover that the team is heading toward a more detailed solution than necessary." (L3252). The correction arrives before effort is spent.
4. **Shared numbers are easier to retract.** Pride makes a sole estimator reluctant to admit error, and collaboration removes that (L3254).

Cohn announces three reasons and gives a fourth under "Finally". All are coaching observation, with no measurement behind them. The two-versus-sixteen case is an illustration and not data.

### The rule, at this wiki's level

The transfer here is ours. Do not accept an estimate on one source alone. Challenge it against similar finished work, and treat a surprising number in either direction as a question about what the task means.

### Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The proposed estimate | The task |
| Similar finished work and how long it lived | Board history |
| What the requester expected | The task's purpose and the person steering |

The estimate was wrong if similar tasks keep landing far from their estimates in the same direction. This wiki reads that pattern as the "systematically forgetting" of L3250. A high estimate that was accepted without challenge was wrong if the delivered solution turns out to be larger than what was asked for.

### Sign of violation

These signs are this wiki's: an estimate far below what a similar finished task took, with no stated reason for the difference, and a number well above the requester's expectation with no conversation about scope.

### Trade-off

The rule takes time from more than one person for each estimate, which is why it pays mainly on the surprising numbers. Cohn's ideal-hours unit, an estimate that counts working time and ignores the rest of the day (L3246), is not used at this wiki's level, and the scale is fixed on [[estimation-scale]].

### Agent executor note

Reason 4 is about pride and does not transfer. Reason 1 as stated falls away, since the executor is known; what it protected survives, because the estimator is usually not that executor, so a check by a second source is the default and not a concession. This is the same reading as the agent note on who estimates, above, and the check rests on reason 2. Reason 2 is the strongest transfer, since board history can stand in for a colleague's memory, and an agent has none of its own. Reason 3 survives as a check that the people steering run. Cohn's argument does not settle whether an agent's own estimate can stand alone ([[filling-a-period]] leaves that open), because every estimator in it is a person with a stake in the work.

## Executor-Bound Estimates

An estimate of time describes a pairing of work and worker, not the work alone. Cohn's section title states it: "My Ideal Days Are Not Your Ideal Days" ([[cohn-agile-estimating-planning]] L1598).

### The discriminating case: size against duration

Cohn's example is two runners at a trail, one fast and one slow. They can agree that it is one kilometre and about half the length of another trail, and these discussions are meaningful (L1600). If they discuss time instead, one says six minutes and the other at least ten: "Each would be right, of course" (L1602). The only way out is to agree always to talk in terms of one particular runner (L1602).

The criterion that separates the two is whether the disagreement can be settled. A dispute about size has something to settle it, namely the comparison with other work. A dispute about duration between two people of different speed has not: "they may each be right and they have no basis on which to argue and establish a single estimate." (L1650).

### What breaks

With ideal days the example becomes three days against five, and both may be right (L1604). Choosing the estimate of whoever is expected to do the work bets on the assignment holding: "by the time we actually do the work you may be too busy and I have to do it. And I’ll be late because it’s estimated at three days for you but will take me five." (L1604).

### When ignoring it is acceptable

"What most teams do is ignore the issue. This is acceptable if all developers are of approximately the same skill or if programmers always work in pairs, which helps balance out extreme differences in productivity." (L1606).

### Observable signs

These signs are this wiki's derivation. Each raises a question to check.

- Estimating comments give different numbers, each justified by how long that person would take.
- An estimate is recorded along with the name of the person it assumes.
- In board history, tasks that changed assignee overrun their estimates more often than those that did not.

### The remedy and its limit

Expressed in [[story-points]], the same people can converge: "Two developers of different skill or experience can agree on the size of something while disagreeing about how long it will take to do." (L1636). This wiki notes that the duration question has not gone away. It has moved to the point where size is converted to time through [[velocity]]. The choice is on [[ideal-days]], and who supplies an estimate is on the rule at the top of this page.

### With an agent executing

This wiki reads Cohn's first condition as largely met when one agent does all the work, so the problem shrinks. It returns when the executor changes: a person taking over a task from an agent, or a different model or tool picking it up. A time estimate carried across that change has the failure above.
