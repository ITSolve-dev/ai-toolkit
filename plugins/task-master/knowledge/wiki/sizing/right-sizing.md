---
title: Right-Sizing
category: sizing
summary: Before pulling an item, ask one yes/no question; can it finish within the SLE? Yes means pull it; no means split it, reduce its fidelity, or spike it. This replaces item-level points on a project that has an SLE.
tags: [decision-rule, estimation, decomposition, cycle-time, pull]
sources: [vacanti-actionable-agile-metrics, kanban-playbook-right-sizing, flow-metrics-scrum-teams]
created: 2026-11-02
updated: 2026-11-02
---

# Right-Sizing

**Right-sizing** is a yes/no check made just before an item is pulled: can it finish within the chosen [[service-level-expectation]]? It exists because deferring commitment raises the duty to make sure that a committed item has the best chance of flowing through ([[vacanti-actionable-agile-metrics]] L3106). See [[just-in-time-commitment]].

> the SLA will act as the litmus test for whether an item is of the right size to flow through the system.
>
> — [[vacanti-actionable-agile-metrics]], L3108

The Kanban Playbook asks the same question ([[kanban-playbook-right-sizing]] L30), and [[size-ceiling]] places it among the other ceilings. It does not mean making items equal: [[right-sizing-not-same-sizing]].

## The test

With an SLE of fourteen days at 85%, the team asks whether it believes this item can be finished in fourteen days or less (L3108).

> The length of this conversation should be measured in seconds. Seriously, seconds.
>
> — [[vacanti-actionable-agile-metrics]], L3108

Neither exact duration nor comparison is sought. Five days, nine days and 8.247 days are all the same answer (L3108), and "We also do not care what this particular relative complexity is compared to the other items." (L3108)

- **Yes:** the conversation ends and the item is pulled (L3108).
- **No:** the team considers how to "break it up, or change the fidelity, or spike it to get more information" (L3114). See [[story-splitting-patterns]] and [[spike-as-last-resort]].

## The same test at selection

[[flow-metrics-scrum-teams]] runs the check on each item chosen for a period, after a forecast has said how many fit ([[filling-a-period]]), because that forecast counts right-sized items only (L1022). Line references in this section are to that source. Its question keeps the bar low: "based on what we know about this PBI right now–which is not much–do we think we have an 85% chance of getting it done in 7 days or less?" (L1044). It gives two ways out of a no, "(a) pull the PBI in as is and take that risk, or (b) choose not to work on that PBI in this Sprint" (L1044). Vacanti's signed note adds a third for the item next in order, an effort at refinement, meaning to "break the PBI up into several other PBIs–not tasks!–or change the acceptance criteria" (L1046).

This wiki resolves those by what each costs, and the resolution is ours. An item next in order is cut first, since skipping it changes the order for a reason of size ([[order-by-value-not-convenience]]). Taking it as it stands stays open to whoever steers, and the plugin records that the check said no, so that a later overrun reads as an accepted risk. Leaving it out is for an item that cannot be cut now.

## Smallest bit of value

The book quotes Prateek Singh's guidance to one of his teams, which asks two things: "is this the smallest bit of value and can it get done in 11 days or less?" (L1216). This wiki reads the first half as adding to the SLE question, since an item inside the SLE can still hold separable value. It reads that half as the text check on [[compound-task-text-signs]] and not as a push to minimize, which Cohn warns against ([[size-ceiling]]), because each piece still has to deliver something ([[vertical-slice]]). The 11 days belong to that team: "Each team will figure out their right-size stories from their own data." (L1216).

## Inputs and what would show the choice wrong

- **The SLE:** from [[choosing-a-service-level-expectation]], read from board history.
- **The judgement:** the executor's belief about this item, read from the item's text.

The later fact is not stated by the source. This wiki takes it to be an item that passed the check and then aged past the SLE. Such an item is what [[percentile-intervention-triggers]] catches in flight, and a pattern of them says the check is being answered carelessly or the item text does not carry what the check needs.

## It is still estimation

Vacanti concedes this.

> I never said that all estimation goes away. All I said was that the amount and frequency with which you do estimation will change.
>
> — [[vacanti-actionable-agile-metrics]], L3116

The saving he claims is the removal of "“pointless” debates of whether a story is two points or three points" (L3116). He also says this "does not mean you do a lot of upfront estimation and planning" (L3108). What it costs is detail: the check yields no number for planning a date, and its one output is the SLE's range.

The Kanban Playbook says the opposite: "Right-sizing is not estimation." ([[kanban-playbook-right-sizing]] L30). This wiki sides with Vacanti, as [[size-ceiling]] already does: the check is estimation of a smaller, cheaper kind.

## Sign of the failure it prevents

This sign is the wiki's phrasing: a pulled item whose text describes more than the SLE can hold, seen either before the pull as a task too big to answer yes for, or afterwards as an item aged beyond the 85th percentile line. See [[hidden-wip-in-large-items]].

## Per setting

This section resolves a disagreement between methodologies and is the wiki's own reading.

- **Project with an SLE:** a stable process and enough finished items (about 11 to 30, see [[choosing-a-service-level-expectation]]). Right-sizing replaces point estimates at the item level.
- **Project without one:** a new project or a recently changed process. There is no SLE to test against, so this check is unavailable and relative estimation stays the sizing tool until the data exists.
- **Project planning dates or filling periods:** a yes/no gives no sum to plan with. The SLE's forecast applies to one item, so filling a period needs something else, whether velocity or throughput. The count from [[throughput-monte-carlo]] and this check then work as a pair: one says how many, and the other says which items may count.

## Agent executor note

This note is the wiki's own. The check rests on a person's sense of how long work takes, which does not transfer to an agent directly, and the source does not address this. The fit is plausible, as the person steering can still ask the question, but cycle time with an agent executor is likely dominated by waiting for review and not by work, so "can it finish in N days" may need reading as "can it be presented once and accepted within N days".

The check and the charter's first working test are separate. Review of a presented result is no wait inside the task, yet review time counts against the SLE if the finished point sits after acceptance ([[started-and-finished-points]]). This wiki therefore reads a yes here as saying nothing about whether the task can be finished without waiting, and that test is applied on its own ([[unit-of-work]]).
