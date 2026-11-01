---
title: FIFO Pull Order
category: moving-work
summary: Once work is committed, pull the item waiting longest; strict FIFO is impractical, so the working form is mostly first-in-first-served. In Vacanti's simulation, changing only pull policy moved the 85th percentile cycle time from 50 to 100 days.
tags: [rule, pull-policy, class-of-service, cycle-time, flow-metrics, kanban]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# FIFO Pull Order

This rule fixes the default order among committed work: when capacity frees up, the item that has waited longest goes first. Vacanti states it as a gradient and not an absolute:

> The point to all of this is that the further you stray from FIFO queuing, the less predictable you are.
>
> — [[vacanti-actionable-agile-metrics]], L3390

Vacanti does not say a departure is never justified. He adds at once that there are practical reasons to forfeit FIFO, and that "arbitrary business value reasons and fictional Cost of Delay calculations do not fall into this practical category" (L3390). This wiki takes up the value question on [[value-decided-at-replenishment]]. The rule governs the order after commitment; which item enters is [[conditioning-flow]] and [[just-in-time-prioritization]].

## The simulation and its setting

The figures below hold only in this setting (L3276, L3282, L3290).

- A board with three columns: Specifying WIP limit 2, Development WIP limit 2, Test WIP limit 1.
- A backlog of 50 items, each taking exactly 10 days in every column.
- No blocking and no added scope.
- "Expected" cycle time means the 85th percentile.

The pull decision exists because of the narrower column: at the end of day 20, two items finish Development and only one can enter Test (L3286).

| Run | Pull order of Standard items | Expedites | 85th percentile | Spread | Lines |
|---|---|---|---|---|---|
| 1 | Strict FIFO | None | 50 days | 30 to 50 days | L3300, L3356 |
| 2 | Random | None | 60 days | "much more spread out" | L3316 |
| 3 | Strict FIFO | Always exactly one | 65 days | More compact than run 2, wider than run 1 | L3334, L3340 |
| 4 | Random | Always exactly one | 100 days | 40 to 170 days | L3356 |

In runs 3 and 4 the expedite may violate WIP limits in every column and always wins a tie, and a new one is introduced as soon as the last one finishes (L3326, L3344).

Vacanti's reading is that all of this was self-inflicted: "All of the variability in these scenarios was of our own doing." (L3368). Run 2 alone is a 20% rise from replacing FIFO with a coin flip (L3316).

This wiki notes three limits on those figures. Every item in the simulation is the same size, which Vacanti says is neither possible nor suggested in practice, and he says size differences add further variability (L3370). The chapter does not say how many times each run was repeated. A practitioner source is graded here on mechanism, so what this wiki keeps is the direction and the cause, and the percentages do not transfer to a real board. His sentence "introducing an Expedite CoS is worse for predictability than simply pulling items at random" (L3340) is true of the 85th percentile, since he also reports that run 3's histogram is the more compact of the two. This wiki therefore reads run 3 as worse than run 2 on expected time and not on spread.

## The working form: mostly first-in-first-served

Strict FIFO governs finishing as well as starting, which cannot be forced: at a restaurant, the party at the second table need not wait for the first to leave (L3380). First-in-first-served (FIFS) governs the order of starting, as with seating. "A (mostly) FIFS scheme is much more practical in the knowledge work context as well and usually is the best strategy from a predictability perspective." (L3380).

The "mostly" has a stated case. A freed resource that lacks the expertise for the longest-waiting item may reasonably take the second-longest (L3382). Vacanti's caveat is that this is a trade: "even though this may be the best practical decision, it may not be the best predictable decision." (L3388). He leaves the longer-term fix as a question to the reader.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| When each item was committed | Board history, at the [[started-and-finished-points]] |
| Whether the free executor can take the oldest item | The task's text and the project's setup |
| Whether a declared exception applies | [[interrupting-started-work]], [[when-to-use-class-of-service]] |

The table and the following tests are this wiki's. The choice was wrong if following oldest-first leaves the spread of cycle times no tighter than before, or if it repeatedly stalls capacity on an item that cannot progress, in which case that item's block is the thing to look at ([[blocked-work-counts-against-wip]]).

## Observable signs of violation

These signs are this wiki's derivation. Each raises a question ([[smell-is-not-a-finding]]).

- **In history:** the item pulled was not the oldest, and no reason is recorded.
- **In history:** items committed later repeatedly finish before items committed earlier ([[wip-lengthens-cycle-time]]). Size differences also produce this, so like is compared with like first.
- **On the board:** no one can state the order used at a column with a tight limit, which means the pull is effectively random, the policy of runs 2 and 4.

An item passed over this way is [[artificially-aged-work]].

## Cost

Oldest-first ignores what an item is worth once it has been committed, so a more valuable item waits behind an older one. Vacanti accepts that, and places value at the moment of entry instead.

## Which setup this applies under

The chapter treats a continuous flow board. Under a flow setup the rule applies directly to each pull ([[board-rules-by-setup]]). This wiki reads it as applying inside an iteration too, wherever two selected items compete for one slot. The mechanism is a queue and needs no period, but Vacanti does not discuss iterations here.

## Agent executor note

The skill case is about human expertise. This wiki expects it to shrink for an agent, and to return in another form where a run lacks access, or where two tasks touch the same code. The simulation's shape, a narrow column downstream of wider ones, is the shape a board has when several agent runs feed one reviewer, so this wiki expects pull order to matter most at review. On a small board a percentile rests on few items ([[service-level-expectation]]), so the effect will be hard to read from a few people's history. All of this note is this wiki's reasoning and is unmeasured.
