---
title: Process Policies from Little's Law
category: moving-work
summary: Little's Law's assumptions can be written as explicit policies on starting, finishing, unblocking and pull order, so that flow data becomes trustworthy.
tags: [rule, policy, predictability, wip, pull, board-rules]
sources: [vacanti-actionable-agile-metrics]
created: 2026-11-02
updated: 2026-11-02
---

# Process Policies from Little's Law

The assumptions of [[littles-law]] can be stated as explicit policies for how a board runs. Vacanti's argument is that predictability is designed through such policies and not computed from a formula: "The design of your process is really just the sum of all the policies you have in place" ([[vacanti-actionable-agile-metrics]] L1024). A process that conforms, or mostly conforms, gives data the team can start to trust, and only then is it probabilistically predictable (L1088-L1094).

## The policies

Vacanti offers four, as examples and not a complete list (L1018). The pairing with assumptions is this wiki's reading, because the source derives them from the assumptions as a set; the numbers refer to [[littles-law-assumptions]].

| Policy (L1018) | Assumption served | Sign of violation in board history |
|---|---|---|
| "We will only start new work at about the same rate that we finish old work." | 1, arrivals equal departures | Starts exceed finishes across a window |
| Finish what is started and minimize discarded items, which needs "some notion of late-binding “commitment”" | 2, everything started exits | Items abandoned part-way, especially late in the flow |
| Unblock blocked work as quickly as possible | 3 and 4, stable WIP and age | Blocked items whose age keeps rising |
| "We will closely monitor our policies around the order in which we pull items through our system so that some work items do not sit and age unnecessarily." | 4, age not rising | Old items passed over while newer ones finish |

The chapter's conclusion puts the same matters as questions to ask of a running process: why work flows in faster than it flows out, why items age through blockages or poor pull policies, and why work is abandoned part-way "(and how you account for that abandonment)" (L1112). The audit of a running process's policies against these is on [[littles-law-assumptions]], and the pull-order policy is on [[fifo-pull-order]].

## What breaks when they are ignored

Vacanti says every violation reduces predictability, and that the data may hide this for a while (L1006-L1012). Interventions then stop producing the results expected of them: the payoff of conformance is that actions "will result in outcomes more closely aligned with our expectations" (L1106).

## The loop

Vacanti quotes Frank Vega: "your policies shape your data and your data shape your policies" (L1026). In Vacanti's account, policies influence the data collected, and that data then points at where the policies are deficient (L1026).

## Trade-offs and limits

- **Following them has a cost.** Vacanti says that lowering WIP "feels uncomfortable" (L906) and that taking control of these policies "will mean saying no to customer requests to start new work immediately" (L234). Requests wait outside the process while the team finishes.
- **Violations will happen.** Some are "unavoidable or even necessary"; the aim is not to "compound those uncontrollable events" with ones that could have been prevented (L1014).
- **Unmeasured abandonment.** This wiki reads the parenthetical about accounting for abandonment (L1112) as a warning: if discarded items simply vanish from the data, assumption 2 appears to hold when it does not.

## Which setup this applies under

The resolution is this wiki's. The first policy is a rate, and [[wip-control]] is a bound on a count; a project under a bound that holds meets the rate as a consequence, since nothing starts until something finishes. So under a flow setup the first policy is checked through the bound. Under an iteration setup with no WIP control there is no bound to rely on, so the policy is read directly from starts against finishes inside the period.

## Agent executor note

This wiki's reading, not the source's: starting is close to free for an agent, so the first policy is easier to violate, not harder. Several items can begin at once while finishes stay gated by the person who reviews them. On that reading, the rate to match is the rate at which results get accepted, not the rate at which the agent produces them. This transfer is untested. It would be shown wrong if a board's finishes kept pace with its starts at much higher concurrency.
