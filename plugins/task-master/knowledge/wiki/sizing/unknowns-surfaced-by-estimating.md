---
title: Unknowns Surfaced by Estimating
category: sizing
summary: Estimating exposes what nobody knows; the unknown is then either resolved by learning now, or noted and reflected in a larger estimate or a range.
tags: [decision-rule, estimation, risk, spike]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Unknowns Surfaced by Estimating

An estimate's side product is a list of what nobody knows. Cohn:

> The discussions that occur while estimating raise questions that expose potential dark corners of a project.
>
> — [[cohn-agile-estimating-planning]], L421

His example is estimating integration with an existing mainframe legacy system the estimator knows nothing about, which "will expose the integration features as a potential risk." (L421).

## The choice

Cohn gives the options (L421):

1. **Remove the unknown now.** "The project team can opt to eliminate the risk right then by spending time learning about the legacy system."
2. **Note it and carry it in the estimate.** "Or the risk can be noted and the estimate for the work either made larger or expressed as a range to account for the greater uncertainty and risk."

At project scale he adds a third outcome: some projects are so risky "that we may choose not to start once we’ve learned about the risks", and others contain features whose risks "can be contained by early attention" (L419).

This wiki reads the first option as a [[spike-as-last-resort]] when the learning is large enough to be a task of its own, and the second as what [[estimates-as-ranges]] asks for.

## Inputs and where they are read

Cohn gives no criterion for choosing. The following is this wiki's reading:

- **Does the work downstream depend on the answer?** Read from the task's dependencies. If the task's shape, or tasks after it, would change with the answer, learn first.
- **What does learning cost against the width it removes?** Read from the estimate range. If the learning costs more than the range's spread, carrying it is cheaper.
- **Could the executor guess past it?** Read from the task text. An unknown left in a task is one an agent will fill by guessing, so a noted unknown has to be stated in the task itself ([[underspecified-task]]).

**What later fact would show the choice wrong.** The task overran on exactly the noted unknown, when it should have been resolved first; or the learning task ended and changed nothing about the estimate or the plan.

## Sign

This wiki's question to check: a task touching an unfamiliar system or integration that has a point estimate and no stated unknown. The unfamiliarity has to be visible in the task text or history for this to be readable.

## Trade-offs

This wiki notes three costs. Learning now spends effort on work that delivers nothing directly. A larger estimate hides the reason unless it is written down. A range keeps the reason visible, at the cost of a less definite forecast; see [[single-date-plan]].

## Agent executor note

Cohn's mechanism is a human discussion. Without one, this wiki reads the transfer as requiring something to do the asking: the plugin, when sizing a task, has to name what it does not know, since an agent that is not asked will not stop ([[agent-silence-is-not-completeness]]). That transfer is the wiki's and comes from no source. The reason these resolve over time is the [[cone-of-uncertainty]]. A task that cannot be sized at all because of what it hides is on [[size-ceiling]].
