---
title: Prioritizing Infrastructure
category: ordering
summary: Infrastructure scores low on value, so it moves early only for a named reason; a cost saving net of later change and carried complexity, knowledge the work produces, or the risk of the component failing.
tags: [decision-rule, ordering, prioritization, dependencies, risk]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Prioritizing Infrastructure

This rule orders work that no user asks for, such as an architectural element, against work users do ask for. These two are hard to compare directly ([[incomparable-tasks]]). Cohn ([[cohn-agile-estimating-planning]]) compares them by running the item through each of the four [[prioritization-factors]] (L1833-L1847), using a security framework as his example.

## The four questions

| Factor | Cohn's reasoning | Direction in his example |
|---|---|---|
| Value | "The application must do something before security is relevant." (L1837) | Late |
| Cost | Cheaper to add now, which is "the basis for many arguments in favor of developing them early", but it may change by the end, and it may add complexity (L1839) | Unclear until the additions are counted ([[cost-now-versus-cost-later]]) |
| New knowledge | Unlikely to teach anything about the product, but it may teach something about the project (L1841) | Depends |
| Risk | "Perhaps not in this example." (L1847) | Depends on the component |

The worked example is on knowledge. A team that had to authenticate through an LDAP server had no one who had done it, so nobody could say what it would take. To remove that doubt, the stories "were moved up to around the middle of a project rather than being left near the end" (L1841-L1845). This wiki notes the size of the move: the middle, not the start. An item needs to come early enough to act on what it reveals, not as early as possible.

On risk, Cohn's general claim is that "the failure of a framework, key component, or other infrastructure is often a significant risk to a project. This may be enough to warrant moving development sooner than would be justified solely on the basis of value." (L1847).

## The rule

This statement of it is this wiki's reading of the worked example. Infrastructure takes its position from value, which is usually late, and moves earlier only for a reason that can be named as one of these:

1. Cost now is lower after counting later change and carried complexity.
2. The work produces knowledge that a decision is waiting for.
3. The component's failure would stop the project, and doing the work shows whether it fails.

This wiki adds that dependencies still apply: a feature that needs the component cannot start without it ([[sequence-versus-wait]]). That sets a floor on the position and is separate from these three.

This wiki also pairs the rule with cutting: where possible, the item is built thin and with a feature that uses it ([[vertical-slice]]), because infrastructure with no feature attached is the way the risk-driven failure happens ([[ordering-by-one-factor]]). This pairing comes from the base and not from this chapter.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| Which features use it | The tasks that depend on it |
| Stated reason for moving it | The move recorded by [[combining-prioritization-factors]] |
| What failure of the component would stop | The design, or the person steering |
| Whether the requirement behind it is settled | Open questions on those tasks |

These tests are this wiki's.

- **Moved too early** if the component was reworked once its first real user arrived, or if the features it supported were dropped.
- **Left too late** if its arrival forced changes across finished work, or if a failure surfaced with too little time left to respond.

## Cost

This wiki notes that early infrastructure spends capacity before anything is shown to users, and that delays the feedback argued for in [[ordering-for-early-user-feedback]]. Late infrastructure accepts the chance of retrofit.

## Agent executor note

Cohn's LDAP case rests on unfamiliarity: "None of the developers had done this before" (L1841). That trigger depends on human experience. This wiki reads the surviving version as whether the integration has been shown to work in this system, whoever is executing. Reasons 1 and 3 survive unchanged. Reason 2 needs its finding recorded ([[end-and-means-uncertainty]]).
