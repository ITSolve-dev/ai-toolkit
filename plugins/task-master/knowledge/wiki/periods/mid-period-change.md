---
title: Mid-Period Change
category: periods
summary: During a period the commitment is protected; the Scrum Guide protects a goal and lets the list of work change, Cohn protects the selected features and limits the period by how long priorities hold, and the setup decides which applies. A change that endangers the commitment waits, and a goal gone obsolete is cancelled openly and not quietly replaced.
tags: [rule, iterations, commitment, period-length, scrum]
sources: [scrum-guide-2020, kanban-guide, montgomery-tracker-smells, cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Mid-Period Change

Under a fixed period, this rule says what can change once the period has started. The Scrum Guide and Cohn both protect the commitment, and they differ on what the commitment is.

## Scrum Guide: the goal is protected

The Scrum Guide sets out four conditions:

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

## Cohn: the selection is held still

Cohn states the rule from the commitment side and links it to period length.

> Once a development team commits to completing a specific set of features in an iteration, it is important that they not be redirected from that goal. It is therefore important that the product owner not change priorities during the iteration and that she help protect the team from others who may attempt to change priorities. Because of this, the length of time that priorities can go unchanged is a factor in selecting the iteration length.
>
> — [[cohn-agile-estimating-planning]], L3455

This wiki reads two consequences in that passage. Whoever owns the order holds it still and also shields the team from other people's changes. And a project whose priorities will not hold has too long a period, not merely a discipline problem ([[period-length]]).

This wiki reads Cohn's freeze as aimed at redirection from outside the team. For work the team itself discovers, he has a route that agrees with the Guide: the team and the product owner "may need to reduce the functionality of a story or drop one entirely" to meet the iteration goal (L3299). So the two sources differ on a swap brought in from outside that leaves the goal intact, and not on an overflow ([[commitment-over-a-period]]).

## The rule, by setup

Cohn's commitment is "a specific set of features". The Scrum Guide protects the goal and lets the list of work change. This wiki resolves it by setup, and the resolution is this wiki's.

| Setup | What is protected | A swap during the period |
|---|---|---|
| A goal is stated for the period | The goal | Allowed if the goal is unaffected, by agreement with the owner of the scope |
| A selection and no goal | The selection, which is then the only commitment there is | A change to the commitment, decided by the people steering and recorded |

The setup is what the plugin knows, so it applies the row that matches and does not ask which author is right.

Where a goal is stated, a change proposed during a period is judged by its effect on the goal.

1. **It serves the goal or leaves it unaffected:** it may go in, by agreement with whoever owns the scope.
2. **It would endanger the goal:** it waits for the next period.
3. **The goal itself is obsolete:** the period is cancelled and a new one begins.

## Reserve for support work

The rule does not cover work that was planned for. Cohn says a team with concurrent maintenance or support duties "will hold some amount of time in reserve" for them, and the protected case is an idea that "does not fit as part of their maintenance or support reserve" (L3459). This wiki reads that as a discriminating test: a request that fits the declared reserve is not a redirection, and one that does not must wait or be treated as a change. How the reserve is set is on [[iteration-capacity]].

## Sign of violation

- **In board history:** the goal's text changed during the period.
- **In board history:** a task with no relation to the goal was added while selected tasks that serve the goal slipped.
- **In board history:** a task added to a period outside any declared reserve while selected tasks slip, where the setup has no goal to judge it against.
- **In board history:** a task crossed the finished point against a relaxed check during the period, which contradicts "Quality does not decrease".
- **In board history:** most of a period's selection replaced with no cancellation recorded. A goal that was in fact abandoned then looks like one that was met or missed.
- **In board history:** repeated changes of this kind across periods, which suggests the length is wrong and not that someone misbehaved.

The sources state the rule. These signs are this wiki's, and each raises a question and not a verdict ([[smell-is-not-a-finding]]).

A task added during a period is not by itself a sign, and the signs above do not treat it as one. The study behind [[montgomery-tracker-smells]] lists "After a sprint has begun, new issues are added to the sprint." (L206) as a smell, and 5 of 15 disagreed or said it depends (L548). P08 said it "happens every sprint" and is "normal operations", and P21 said it is not a problem "as long as you get your work done" (L548). This agrees with the Guide, which lets the list change. Others described the cost: P01 called customer-driven additions "stressful, inefficient, and it puts a lot of pressure on the team" (L548). That cost is human strain, and it does not transfer as it stands to an agent ([[interrupting-started-work]]). The study gives no count of additions that is too many, so the test stays the effect on the commitment.

## Why

What breaks is the meaning of the commitment. If the goal moves with the work, nothing was committed to and a period cannot be judged ([[commitment-over-a-period]]). If the selection can be redirected, then the period no longer tests what the team said it would do. Cohn gives this as a matter of importance and does not spell out a consequence, so this statement of the mechanism is this wiki's.

## Cost

Urgent work that does not serve the goal waits, or it costs a cancellation ([[interrupting-started-work]] says when that is worth it). The Guide offers no third route. The Kanban Guide does, through a declared exception ([[what-may-move]]), which is one reason the choice of setup matters for a project with frequent interruptions.

The freeze has a measurable price: an idea that arrives during a period waits. On Cohn's assumptions it reaches working software after 1.5 periods on average ([[new-idea-latency]]). By this wiki's arithmetic a four-week period therefore costs six weeks on average. Cohn says separately that "most organizations can (with sufficient training) learn not to adjust priorities for two weeks while doing so for four weeks can be very difficult." (L3508). Linking that difficulty to the wait is this wiki's reading.

## Which setup this applies under

- **Iteration setup:** as above.
- **Flow setup:** this rule has nothing to protect. There is no goal to endanger, and the order of unstarted tasks can change at any time. An urgent item goes next on the next capacity signal, or it uses an exception that was declared in advance: "Any acceptable exceptions to controlling WIP should be made explicit as part of the DoW." ([[kanban-guide]] L143). This statement of the contrast is this wiki's.

## Agent executor note

The rule depends on a negotiation between two roles, Developers and Product Owner. With a few people steering an agent, those roles are often one person, so the check has no second party. Cohn's product owner protects people from interruption. The protection of the commitment still matters with an agent, though the human cost of interruption does not carry over ([[interrupting-started-work]]). The person who would change priorities and the person who would protect them are often the same.

The plugin can stand in only as far as showing the effect of a change on the commitment and what it would displace. It proposes, and the people steering decide. Cancelling a period and editing a goal are theirs alone, in line with the Guide's "Only the Product Owner has the authority". An agent that finds its work is different from what was expected has no standing to renegotiate, and it stops and reports.
