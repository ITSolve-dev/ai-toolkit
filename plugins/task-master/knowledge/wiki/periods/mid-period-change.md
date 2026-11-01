---
title: Mid-Period Change
category: periods
summary: During a period the list of work may change and the goal may not; a change that endangers the goal is refused, and a goal gone obsolete is cancelled openly and not quietly replaced.
tags: [rule, iterations, commitment, scrum]
sources: [scrum-guide-2020, kanban-guide]
created: 2026-11-01
updated: 2026-11-01
---

# Mid-Period Change

Under a fixed period, this rule says what can change once the period has started. The Scrum Guide sets out four conditions:

> During the Sprint:
>
> - No changes are made that would endanger the Sprint Goal;
> - Quality does not decrease;
> - The Product Backlog is refined as needed; and,
> - Scope may be clarified and renegotiated with the Product Owner as more is learned.
>
> — [[scrum-guide-2020]], L193-L198

The Guide repeats the point under the goal itself: "If the work turns out to be different than they expected, they collaborate with the Product Owner to negotiate the scope of the Sprint Backlog within the Sprint without affecting the Sprint Goal." (L303). The way out is a separate rule: "A Sprint could be cancelled if the Sprint Goal becomes obsolete. Only the Product Owner has the authority to cancel the Sprint." (L204).

This wiki reads those together as a rule with three outcomes. The list of work is free to change. The goal and the standard of done are not. A goal that no longer makes sense ends the period and is not edited inside it.

## The rule

A change proposed during a period is judged by its effect on the goal.

1. **It serves the goal or leaves it unaffected:** it may go in, by agreement with whoever owns the scope.
2. **It would endanger the goal:** it waits for the next period.
3. **The goal itself is obsolete:** the period is cancelled and a new one begins.

## Sign of violation

- **In board history:** the goal's text changed during the period.
- **In board history:** a task with no relation to the goal was added while selected tasks that serve the goal slipped.
- **In board history:** a task crossed the finished point against a relaxed check during the period, which contradicts "Quality does not decrease".
- **In board history:** most of a period's selection replaced with no cancellation recorded. A goal that was in fact abandoned then looks like one that was met or missed.

The Guide states the rule. These signs are this wiki's.

## Why

What breaks is the meaning of the commitment. If the goal moves with the work, nothing was committed to and a period cannot be judged ([[commitment-over-a-period]]).

## Cost

Urgent work that does not serve the goal waits, or it costs a cancellation. The Guide offers no third route. The Kanban Guide does, through a declared exception ([[what-may-move]]), which is one reason the choice of setup matters for a project with frequent interruptions.

## Which setup this applies under

- **Iteration setup:** as above.
- **Flow setup:** this rule has nothing to protect. There is no goal to endanger, and the order of unstarted tasks can change at any time. An urgent item goes next on the next capacity signal, or it uses an exception that was declared in advance: "Any acceptable exceptions to controlling WIP should be made explicit as part of the DoW." ([[kanban-guide]] L143). This statement of the contrast is this wiki's.

## Agent executor note

The rule depends on a negotiation between two roles, Developers and Product Owner. With a few people steering an agent, those roles are often one person, so the check has no second party. The plugin can stand in only as far as showing the effect of a change on the goal. It proposes, and the people steering decide. Cancelling a period and editing a goal are theirs alone, in line with the Guide's "Only the Product Owner has the authority". An agent that finds its work is different from what was expected has no standing to renegotiate, and it stops and reports.
