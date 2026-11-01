---
title: Conditioning Flow
category: ordering
summary: Among items near the top of the order, pull the one most likely to finish within the promised range, using current context such as an overloaded state, a soon-absent resource, or uncertainty that calls for a spike first; it can override strict priority order.
tags: [decision-rule, prioritization, pull-system, predictability, spike, bottleneck, vacanti]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Conditioning Flow

Conditioning flow is choosing which item to pull next by its chance of succeeding, not only by its priority. Vacanti derives it from what commitment demands: "Everything in its power" means first choosing an achievable range and probability, and also doing what can be done to choose items with the best chance of meeting it ([[vacanti-actionable-agile-metrics]] L2316).

> This idea of selecting items for success is a concept that I like to refer to as “Conditioning Flow”.
>
> — [[vacanti-actionable-agile-metrics]], L2316

The chapter's takeaway restates it as "being smart about what items to pull in next based on contextual information that we currently have" (L2370).

It decides between two courses at one moment: pull the next item in priority order, or pull a lower-ranked item or a preparatory one instead. It operates inside the free slots that [[just-in-time-prioritization]] has defined, before the [[just-in-time-commitment]] is made, because the item "has not been pulled in yet" (L2318).

## The three cases

| Context | Read from | Choice in the source |
|---|---|---|
| A state downstream is overloaded, and the top item needs much of it while the second needs little | Board state for the overload; the task's content for the effort profile | Pull the second priority (L2318) |
| The top item needs a specific resource that is about to be away for weeks | Availability known to the person steering | Do not pull it: it would be worked for two days and then blocked (L2320-L2326) |
| The team disagrees on whether the top item is the right size | The disagreement itself, as a sign of uncertainty | Create a spike and pull that first (L2328) |

The first case carries a qualifier that should stay attached to it:

> All other things being equal, we should probably pull the second priority in preference to the first priority.
>
> — [[vacanti-actionable-agile-metrics]], L2318

This wiki reads that as a tie-break near the top of the order, not a licence to reorder the whole list: the second item has to be close enough in priority for "all other things" to be roughly equal.

A spike is "a work item—user story—that is used to drive out risk and uncertainty in another work item" (L2328). This wiki's cut-side view is on [[spike-as-last-resort]]. Sizing itself is deferred to the source's Chapter 12 ([[right-sizing]]).

## What would show the choice wrong

This wiki's transfer: the pulled item blocks or exceeds its communicated range for the reason conditioning should have seen, or the item skipped turns out to have been the one that mattered and was delayed past when its value lapsed. Conditioning is also wrong if a skipped item stays skipped while the same bottleneck persists.

## Trade-offs

The source names no cost, and this wiki reads two. Priority is overridden, so importance is traded for predictability on that pull, and the trade should be stated when it is made. Repeated, it starves heavy items: a state that stays overloaded keeps deferring whatever needs it, so a skipped item that recurs is a sign to address the overload rather than to keep conditioning around it, and such an item is on its way to being [[artificially-aged-work]].

This wiki separates the override from the failure on [[order-by-value-not-convenience]]: conditioning names a fact about the current state of flow and moves an item near the top, while that failure orders the whole plan for the builders' ease.

## Agent note

The three cases rest on human executors to different degrees. An overloaded downstream state survives when the bottleneck is a person reviewing what an agent produced. The expert on vacation survives as a person, credential or environment an item requires and that will not be there; an agent itself does not go away. A size disagreement among people has no direct analogue for one agent, so this wiki reads the trigger as stated uncertainty in the task, which still favours a spike first. Pulling only what can be carried through then matches the plugin's working test that a task once started can be finished without waiting, which comes from the plugin's design and not from this source.
