---
title: Closing What No Longer Applies
category: intake
summary: An open item that has stopped needs a stated reason to stay; Kubernetes runs this on timers of 20, 30 and 90 days, which belong to that project, so what transfers is the triggers, the check that the need still stands, and a way to hold something open on purpose.
tags: [decision-rule, intake, triage]
sources: [kubernetes-issue-triage, montgomery-tracker-smells]
created: 2026-11-01
updated: 2026-11-01
---

# Closing What No Longer Applies

The charter's intake topic includes cutting what no longer applies. This rule decides when an open item that has stopped should leave the board. The Kubernetes guide handles it with follow-up triggers, under its stated aim of "Preventing work from lingering endlessly" (L68).

## The triggers, and the setting of their numbers

| Trigger | What happens there | Line |
|---|---|---|
| A question to the reporter goes unanswered for 20 days | Close with a comment | L208 |
| An owner has made no PR in 30 days | A triage engineer asks them "to either create a PR or release ownership" | L263 |
| An owning group shows no movement for 30 days | "gently poke the SIG" | L267 |
| No activity at all for 90 days | A bot marks the issue stale, and it "will eventually be auto-closed" unless someone acts | L271 |

These values are the project's. This wiki reads them as suited to a very large open-source project, with strangers reporting and many people holding issues. The guide gives no reason for them and no measurement. This wiki transfers none of them, and it offers no replacement figure. It keeps the kinds of trigger, which are about what has stopped, and each project reads the length from its own history of Work Item Age ([[flow-metrics]]).

## The rule

For an open item that has stopped, ask what it is waiting for.

1. **It is waiting for an answer from the requester, and the answer has not come:** close it after saying so. It can be reopened by answering.
2. **It has a holder and no output:** ask the holder to produce something or let go. With an agent, there is no one to ask, and the item goes back to be started afresh ([[unfinished-at-period-end]]).
3. **It is waiting for nobody in particular:** check that the need still stands, with the requester. If it does not, close it. If it does, rate it again ([[ordering-by-value-and-urgency]]).
4. **It is being kept on purpose:** it has to say so, as below.

The order of these questions is this wiki's. The guide treats them as separate cases.

## Holding something open on purpose

The guide has two ways of keeping an item that would otherwise go. One is a label for ideas without enough support: "Mostly placeholders for potentially good ideas, so that they don’t get completely forgotten, and can be referenced or deduped every time they come up" (L236). The other stops the bot: "You can block the bot by applying the `/lifecycle frozen` label preemptively" (L271).

This wiki reads those as saying that closing by inactivity needs a declared way out. The two pull against each other, since one keeps what the other removes. The resolution is that a kept item states why it is kept and what would promote it, and an item with no such statement is a candidate for closing. That is what separates a placeholder from an item that was simply forgotten.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| When anything last happened | Board history |
| What the item is waiting for | The task text and its marker ([[waiting-versus-blocked]]) |
| Whether a question to the requester is open | The item's history |
| Whether the need still stands | The requester |
| Whether the code it concerns has changed | The repository |
| How long items normally stay open | Board history ([[flow-metrics]]) |

The closing was wrong if the same need comes back as a new request. Keeping was wrong if an item is later closed unread, after having sat in the count or in the way of a search. The second is harder to see, and it is why a kept item has to state a reason. These tests are this wiki's.

## Why it has to be a rule

Left to judgement, items stay. One participant in [[montgomery-tracker-smells]] described being "reluctant to close issues because they are not urgent and not important" (P15, L459), and another that "delayed tickets lead to a huge backlog of irrelevant tickets" (P06, L459). These are interview notes. What the failure looks like is on [[zombie-issue]] and [[issue-overload]].

## Cost

A closed item can be a real need nobody restated. The risk falls hardest on a requester who was silent for an ordinary reason, so closing says how to reopen. Asking whether a need still stands also spends a person's attention, so it should be batched and not sent one at a time.

## Agent executor note

The triggers read clocks, and a plugin can run them. The guide's human mechanisms do not transfer directly: nudging an owner works on a person who has forgotten. An agent-run task that produced nothing has no one to nudge, so the item needs a fresh start or a decision. Whether the need still stands is a task-only fact, so the plugin proposes and a person decides.
