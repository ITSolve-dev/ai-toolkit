---
title: Just-in-Time Prioritization
category: ordering
summary: Rank work only when the process signals free capacity, and only as many items as there are free slots; ranking deeper is waste because needs and knowledge change before the next pull.
tags: [rule, prioritization, pull-system, backlog, wip-limit, vacanti]
sources: [vacanti-actionable-agile-metrics, cohn-agile-estimating-planning]
created: 2026-11-02
updated: 2026-11-02
---

# Just-in-Time Prioritization

Just-in-time prioritization is the rule that the choice of what comes next is made at the moment capacity appears, for exactly as much work as that capacity admits, and not ahead of it. The source's definition:

> In a pull system, a prioritization conversation only happens when there is a clear indication that the team has capacity to do new work.
>
> — [[vacanti-actionable-agile-metrics]], L2248

## The rule

**Inputs, and where each is read from:**

- The Ready column's bound on [[wip-control]], from the board's policy.
- The number of items currently in Ready, from board state.
- Free slots: the limit minus that count.

The question asked is then limited to that number. In Vacanti's Figure 8.1 the Ready limit is six and four items sit there, so the process is "unambiguously signaling" capacity for two (L2256), and the only question is "what are the next two most important items that we should start at this time?" (L2262). Those figures are an illustration of one board, not a recommended limit.

> Any discussion beyond deciding on just those two items is waste (e.g., having a conversation, say, about prioritizing the top ten items).
>
> — [[vacanti-actionable-agile-metrics]], L2262

## Why

Vacanti's mechanism is that information keeps arriving between a ranking and the pull it was meant to serve: business needs, customer feedback, regulatory concerns (L2262). By the time new work can start, "new requirements will have shown up, or you will have gained new information, or both" (L2242), and the earlier ranking is moot. Much backlog content is also never worked on, so ranking it pays for a decision that is never used (L2242). That last claim is asserted without a figure, so this wiki keeps the mechanism and takes no size from it.

This does not depend on a volatile market. The rule holds "even if you are running what you assume to be a stable project", because finishing requirements itself produces knowledge of the problem domain, through analysis, development and customer reviews (L2264).

## What would show the choice wrong

This wiki's transfer, since the source gives no test: the rule was the wrong depth if work repeatedly stalls with free slots and nothing chosen to pull, meaning ranking was too shallow or too late. Conversely, board history where deep rank positions change repeatedly on items that are never pulled is the sign of the violation Vacanti describes, and raises the question of what that ranking was for.

## Trade-offs and limits

- The source does not name a cost. This wiki reads the cost as losing a long-range order: nobody can read a far-future sequence from the board, so a request for one has to be answered from elsewhere, such as a forecast, not from the backlog's rank.
- A rule built on a capacity signal has no input where the board has no limit on the commitment column. This wiki reads that as a prerequisite: without a [[wip-control]] the rule cannot be applied and the board should be asked why it has none.
- Ranking within the free slots is still not pure importance order: see [[conditioning-flow]].

## Tension with the other ordering pages

Most of `ordering` ranks work ahead of time, and a release plan needs an order over many periods ([[fitting-stories-into-a-release]]). This wiki keeps the reading on [[backlog-versus-commitment]]: a rank on uncommitted items is a proposal for the next commitment decision, cheap to change and owed to nobody. What this rule forbids is spending effort to keep that rank fine-grained, or treating it as settled before capacity exists.

## Per setup

This section is the wiki's own reading.

- **Pull:** the depth of ranking equals free slots, and the trigger is a slot opening.
- **Iterations:** this wiki reads the same logic as bounding fine ranking to what the next iteration can hold, since [[backlog-versus-commitment]] sits at the period there. That reading is compatible with [[reprioritize-before-each-iteration]], though Cohn keeps a fully ranked list, "the most valuable story is at the top, the least valuable is at the bottom" ([[cohn-agile-estimating-planning]] L3104), and Vacanti's depth limit is not his.
- **Iterations with a release plan:** a coarse order beyond the next period is needed for the forecast, and its detail is what is not worth maintaining ([[planning-horizons]]).

## Agent note

The mechanism is information arriving, not human memory or pace, so it survives an agent executing. The source's example is a team meeting to replenish Ready (L2262); this wiki takes only the trigger from that, a slot opening, and not the meeting. With a few people steering an agent, free slots may be one or two, which keeps ranking cheap and makes the rule stricter, not looser.
