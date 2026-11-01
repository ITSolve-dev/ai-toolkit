---
title: Collaborative Task Estimation
category: sizing
summary: Cohn's case that estimates below the story level are also made by more than the presumed doer; the doer is not yet known, others remember past misses, a high number exposes a misunderstanding, and shared estimates are easier to retract.
tags: [rule, estimation, cohn]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Collaborative Task Estimation

Collaborative estimation means that a number is produced or challenged by more than the person expected to do the work. The story-level position and who counts as an estimator are on [[who-estimates]]. This page holds Cohn's fuller argument from iteration planning, which adds two reasons to that one. Cohn accepts the standard advice that the best estimates come from those who will do the work, citing Lederer and Prasad 1992, and still holds that "task estimating on an agile project should be a group endeavor" ([[cohn-agile-estimating-planning]] L3248). His claim is made at the level below this wiki's task ([[unit-of-work]]), and this wiki carries the reasoning up to its own level.

## Cohn's reasons

1. **The doer is not yet known.** Tasks are not allocated during planning, so there is no specific person to ask (L3248). See [[tasks-are-not-assigned-at-planning]].
2. **Others hold the memory of past misses.** James says a task will take two hours. A colleague answers: "But, James, the last time you worked on a similar task you thought it would be two hours and it took you sixteen." (L3250). James then either gives a real reason this case differs or admits to a cost he has been forgetting (L3250). The fictional case study in Chapter 23 (L4961) plays the same scene: a colleague tells a programmer he is "always optimistic at the start of a new engine" (L5738), and his 6-hour card becomes 12 (L5734-L5742). This wiki keeps the mechanism, a peer who remembers the estimator's record, and not the factor of two, which is an anecdote in a fiction.
3. **A number exposes a misunderstanding.** "Upon hearing an unexpectedly high estimate, a product owner or analyst may discover that the team is heading toward a more detailed solution than necessary." (L3252). The correction arrives before effort is spent.
4. **Shared numbers are easier to retract.** Pride makes a sole estimator reluctant to admit error, and collaboration removes that (L3254).

Cohn announces three reasons and gives a fourth under "Finally". All are coaching observation, with no measurement behind them. The two-versus-sixteen case is an illustration and not data.

## The rule, at this wiki's level

The transfer here is ours. Do not accept an estimate on one source alone. Challenge it against similar finished work, and treat a surprising number in either direction as a question about what the task means.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The proposed estimate | The task |
| Similar finished work and how long it lived | Board history |
| What the requester expected | The task's purpose and the person steering |

The estimate was wrong if similar tasks keep landing far from their estimates in the same direction. This wiki reads that pattern as the "systematically forgetting" of L3250. A high estimate that was accepted without challenge was wrong if the delivered solution turns out to be larger than what was asked for.

## Sign of violation

These signs are this wiki's: an estimate far below what a similar finished task took, with no stated reason for the difference, and a number well above the requester's expectation with no conversation about scope.

## Trade-off

The rule takes time from more than one person for each estimate, which is why it pays mainly on the surprising numbers. Cohn's ideal-hours unit, an estimate that counts working time and ignores the rest of the day (L3246), is not used at this wiki's level, and the scale is fixed on [[estimation-scale]].

## Agent executor note

Reason 4 is about pride and does not transfer. Reason 1 changes form: with an agent executing, the estimator usually is not the executor, so a group check is the default and not a concession. Reason 2 is the strongest transfer, since board history can stand in for a colleague's memory, and an agent has none of its own. Reason 3 survives as a check that the people steering run. Cohn's argument does not settle whether an agent's own estimate can stand alone ([[filling-a-period]] leaves that open), because every estimator in it is a person with a stake in the work.
