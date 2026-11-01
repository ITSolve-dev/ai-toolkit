---
title: Uncertain Piece Goes Earlier
category: ordering
summary: After a cut, order the piece whose duration is least known ahead of pieces already understood, so the uncertainty is removed while there is still room to act on it.
tags: [rule, prioritization, risk, splitting]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Uncertain Piece Goes Earlier

When a task is cut, the order of its pieces is a separate decision. In Cohn's search screen example, the order was set by uncertainty and not by what a user would want next:

> These iterations were prioritized this way because there was a lot of uncertainty about how long it would take to develop the data display grid. Removing that uncertainty in the second iteration was deemed better than leaving it until the third.
>
> — [[cohn-agile-estimating-planning]], L2629

Cohn gives the piece left for last as the one the team understood: "Since the team had already achieved a solid understanding of what was necessary to create the query builder, they considered that work to be low risk." (L2629).

This is a single example, and Cohn draws no guideline from it: the guideline at the end of that passage concerns cutting by operations (L2631). The rule below is this wiki's generalization. It agrees with "most risky" in the Complicated row of [[how-far-to-split-up-front]], and it reads the grid's uncertainty as uncertainty about means ([[end-and-means-uncertainty]]).

## The rule

Among the pieces of one cut, once a first [[vertical-slice]] exists, place the piece with the least known duration ahead of the pieces that are understood.

The first clause comes from the order Cohn actually used: the grid was the second piece and not the first, and a first iteration with a working query path came before it (L2627). The grid's uncertainty was about how long it would take. This wiki reads uncertainty about what the work is as a different matter, which goes to [[spike-as-last-resort]] or [[find-core-complexity]].

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Uncertainty of each piece | The estimator's statement; whether similar work was finished before, from board history |
| Dependencies among the pieces | The cut itself, per [[sequence-versus-wait]] |
| Value of each piece | The purpose in the request, or the person steering |

The order was wrong if the piece marked uncertain took about what was expected, while a piece left for later because it was understood took much longer. It was also wrong if a valuable piece slipped past a date to make room for an uncertain one that could have waited. Both tests are this wiki's.

## Trade-off

The order can delay what is most useful. In this example the remaining search fields waited a further iteration. Cost of delay can outweigh the uncertainty, and [[ordering-by-value-and-urgency]] decides that comparison. This wiki reads the rule as a tie-breaker inside one cut and not as a general order for the board.

## Agent executor note

The example is a human team's judgement with no measurement. This wiki reads the reasoning as surviving an agent executing, since a late surprise costs the plan whoever does the work. What changes is the source of the uncertainty: a human team's unknowns are not necessarily an agent's, so "the team had already achieved a solid understanding" (L2629) cannot be carried across and has to be read from the project's own finished work.
