---
title: Estimating an Underspecified Item
category: sizing
summary: An item whose details are missing still gets a size; state assumptions, guess from the plausible range, and move on, without treating the estimate as evidence that the item is ready.
tags: [rule, estimation, uncertainty, readiness]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Estimating an Underspecified Item

An item that is not fully defined still receives a size estimate. Cohn's position is that incomplete definition does not exempt an item from estimation:

> On an agile project it is not uncommon to begin an iteration with incompletely specified requirements, the details of which will be discovered during the iteration. However, we need to associate an estimate with each story, even those that are incompletely defined.
>
> — [[cohn-agile-estimating-planning]], L998

## The rule

> When you’re given a loosely-defined user story (or dog), you make some assumptions, take a guess, and move on.
>
> — [[cohn-agile-estimating-planning]], L1000

Cohn's example is the two ambiguous entries in the dog list. Poodle covers toy, miniature and standard; terrier covers more than twenty breeds, from under a foot to nearly two feet tall (L998). He gives both 3 points, reasoning from the spread and from a reference item:

> I reasoned that even the largest are smaller than labrador retrievers and that the small terriers and poodles would be 1 or 2 point dogs, so on average a 3 seemed reasonable.
>
> — [[cohn-agile-estimating-planning]], L1000

This wiki states the choice as follows, framing Cohn's example as a rule: bound the item against a reference, then take a value representing the spread, not the worst case and not the most optimistic reading.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The plausible readings of the item | The item's text |
| The sizes of already estimated reference items | The estimated set, as on [[triangulation]] |

The choice was wrong if the resolved item lands outside the assumed spread, or if the work turns out to be several items. Both are this wiki's reading.

## What the estimate does not establish

This wiki draws a line the chapter does not draw. An item being estimable says nothing about its being ready: the rule answers how big, not whether it can be started ([[underspecified-task]], [[recoverable-versus-task-only-facts]]). An estimate on a vague item is a planning placeholder, and the assumptions behind it are the content worth keeping, since they are what a later fact can contradict. Where an unknown is worth resolving before sizing at all, the choice is on [[unknowns-surfaced-by-estimating]].

## Sign of a violation

These signs are this wiki's derivation. Each raises a question to check.

- Items sit unestimated in a planned set because details are missing, so the size total silently understates the plan. Whether the empty field is a defect at that stage is judged on [[empty-fields]].
- A guessed value carries no stated assumption, so nobody can tell whether it was later contradicted.
- A very wide spread is averaged into one mid-scale value. Cohn's own example spans under a foot to nearly two feet (L998). This wiki reads a spread that wide as a question about whether the item is one thing, and the chapter sets no threshold for it.

## Trade-offs

This wiki notes that following the rule keeps the plan complete and cheap to produce at the price of false precision on the items least understood. Their error reaches the total, and only some of it is the kind that [[velocity-self-correction]] absorbs. Later chapters add one support: Cohn reports that being asked to justify an estimate helps compensate for missing information, on [[independent-estimates]].

## Agent executor note

The transfer here is this wiki's, not Cohn's. The two halves of the claim behave differently.

- **Estimating with gaps survives.** The guess is made by whoever sizes the item, and it costs nothing downstream until execution.
- **Discovering details during the iteration does not transfer as stated.** That clause (L998) rests on people filling gaps from context and conversation. An executor that guesses instead of recalling will resolve a gap silently. So a loose item may be sized but has to be clarified before an agent starts it, per [[conversation-moves-into-the-task]].
