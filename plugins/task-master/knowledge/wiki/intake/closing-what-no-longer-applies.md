---
title: Closing What No Longer Applies
category: intake
summary: An open item that has stopped needs a stated reason to stay. Kubernetes runs this on timers of 20, 30 and 90 days that belong to that project; what transfers is the triggers (unanswered requester, holder with no output, waiting for nobody), the check that the need still stands, a declared way to hold something open, and lengths read from the project's own history: Work Item Age for started items, time since last activity against time-to-start for unstarted ones, or a review interval the person steering sets. Its failures are the zombie issue, which practitioners rated the most problematic smell, and issue overload, which shows as duplicates.
tags: [decision-rule, intake, triage, failure-mode, board-history, evidence]
sources: [kubernetes-issue-triage, montgomery-tracker-smells, zimmermann-good-bug-report]
created: 2026-11-01
updated: 2026-11-02
---

# Closing What No Longer Applies

The charter's intake topic includes cutting what no longer applies. This rule decides when an open item that has stopped should leave the board. The Kubernetes guide handles it with follow-up triggers; "Preventing work from lingering endlessly" is among the benefits that SIGs who triage regularly report (L64-L68), which the guide gives as their self-report.

## The triggers, and the setting of their numbers

| Trigger | What happens there | Line |
|---|---|---|
| A question to the reporter goes unanswered for 20 days | Close with a comment | L208 |
| An owner has made no PR in 30 days | A triage engineer asks them "to either create a PR or release ownership" | L263 |
| An owning group shows no movement for 30 days | "gently poke the SIG" | L267 |
| No activity at all for 90 days | A bot marks the issue stale, and it "will eventually be auto-closed" unless someone acts | L271 |

These values are the project's. This wiki reads them as suited to a very large open-source project, with strangers reporting and many people holding issues. The guide gives no reason for them and no measurement. This wiki transfers none of them, and it offers no replacement figure. It keeps the kinds of trigger, which are about what has stopped, and each project reads the length from its own history. A started item is compared with its Work Item Age ([[work-item-age]]). An unstarted item has no Work Item Age, since age begins at the start, so this wiki's input for it is the time since its last activity, compared with how long items that were eventually started had waited before they started. On a young board with too little history for that comparison, the person steering sets a review interval, and the plugin uses it until the history exists. Both inputs are this wiki's; the sources give no length.

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
| How long items normally stay open | Board history: Work Item Age for started items, time to first start for unstarted ones ([[flow-metrics]]), or a review interval set by the person steering |

The closing was wrong if the same need comes back as a new request. Keeping was wrong if an item is later closed unread, after having sat in the count or in the way of a search. The second is harder to see, and it is why a kept item has to state a reason. These tests are this wiki's.

## Why it has to be a rule

Left to judgement, items stay. One participant in [[montgomery-tracker-smells]] described being "reluctant to close issues because they are not urgent and not important" (P15, L459), and another that "delayed tickets lead to a huge backlog of irrelevant tickets" (P06, L459). These are interview notes. What the failure looks like is on *Zombie Issue* (below) and *Issue Overload* (below).

## Cost

A closed item can be a real need nobody restated. The risk falls hardest on a requester who was silent for an ordinary reason, so closing says how to reopen. Asking whether a need still stands also spends a person's attention, so it should be batched and not sent one at a time.

## Agent executor note

The triggers read clocks, and a plugin can run them. The guide's human mechanisms do not transfer directly: nudging an owner works on a person who has forgotten. An agent-run task that produced nothing has no one to nudge, so the item needs a fresh start or a decision. Whether the need still stands is a task-only fact, so the plugin proposes and a person decides.

## Zombie Issue

A zombie issue is an open item that nobody is acting on. It breaks the question of what to do with what came in, because the item has neither been done nor been decided against. The interviewed practitioners raised the problem unprompted, and they rated the matching smell above all others:

> The smell “ignored issue or delayed for too long”, declared as problematic by 15 participants (and only refuted by one), is the most problematic smell in our dataset. This smell is problematic because the longer an issue goes unresolved, the harder it is to resolve.
>
> — [[montgomery-tracker-smells]], L763

The authors' reasoning follows: "After enough time has passed, it might be unclear how to even replicate the reported problem, or who to go to for more information. If the issue is a requirement, it might not be relevant to the evolved system years or even just months later." (L763).

### Sign

- **In board history:** an open item with no activity for a long time. The smell's definition is "An issue has been open for a long time, either delayed or completely ignored." (L170).
- **In board history:** a held item with no output. The Kubernetes guide treats this as a trigger (the triggers table at the top of this page).
- **In a new request:** someone reports the same thing again, with words like "I raised this issue several times" ([[zimmermann-good-bug-report]] L535, and see [[duplicate-reports]]).

The study does not say how long is long, and this wiki does not supply a figure. Under a flow setup, a started item is compared with the SLE ([[overrun-triggers-a-recut]]). An unstarted item has no such measure, because Work Item Age begins at the start ([[work-item-age]]); its input is set out in the rule at the top of this page, time since last activity against how long started items had waited, or a review interval the person steering sets.

### What this sign does not establish

- That the item is a defect of the process. An unstarted item at the bottom of the order is supposed to wait. Rank 7 to 9 on [[ordering-by-value-and-urgency]] can wait a long time by design.
- That waiting did any harm. The evidence is what practitioners believe. "it remains unclear whether the perceptions of practitioners reflect the objective practice" (L753).
- Anything about a few people. Four of the 19 answers were disagreement (L530), for example where a team reviews issues weekly (L530), and the study's reasons for the problem include "older and larger" trackers (L459).

Apply [[smell-is-not-a-finding]] before reporting it.

### Causes the study names

These are from participants' accounts. The authors say "Specific causes for this problem include when the reporter and assignee are the same person (accountable only to themselves), and low-priority issues (minimal pressure to act)." (L459). They also suggest the number of issues and the lack of anyone answerable for the whole backlog (L763). This wiki reads both as surviving at a small scale in some form.

### Remedies, and which survive

The authors recommend three workflows (L773). This wiki keeps two, in changed form.

- **Regular review of open issues.** The meeting is out of scope, and what it does can be kept: something looks at every open item on a schedule. That is the follow-up on [[triage-procedure]].
- **Someone curates the backlog.** That is what the rule at the top of this page does, with the decisions left to a person.
- **Management assigns issues, with no self-assignment.** Dropped, as managing people.

The authors' suggested reminders after one week and three months are illustrations, marked "for example" (L763). They are not findings.

### Agent executor note

This wiki reads the sources as follows, and the transfer is its own. The authors' mechanism of harm (L763) has two parts. Forgetting how to reproduce and who to ask is human memory, and it depends on the people steering, so it survives for them. The system moving on survives whoever executes: a task written against code that has since changed misleads an agent, which has no memory to correct it. The causes participants gave (L459) are a separate matter, and one of them, low priority meaning "minimal pressure to act", does not transfer to the executor: an agent feels no pressure, so a reminder addressed to it does nothing. This wiki therefore puts the check in the plugin: before a long-open task starts, its text is read again against the repository.

## Issue Overload

Issue overload is having more items on a board than the people using it can keep track of. It breaks the question of what to do with what came in, since nobody can tell whether a new request is new. Eight of the 26 interviewed practitioners raised it, and a participant's note reads: "having so many issues can be a problem. We are not sure what to do with all of these issues" (P15, [[montgomery-tracker-smells]] L457).

> The consequences of this smell include a lack of awareness of existing issues, leading to duplicates and overlapping issues, missed links, and issues being forgotten.
>
> — [[montgomery-tracker-smells]], L457

### Sign

- **In board state:** new requests repeat items already open, and the repetition is found late ([[duplicate-reports]]).
- **In board state:** many open items that have not been rated or looked at for a long time (*Zombie Issue* (above)).
- **In a person's answer:** asked what is on the board, nobody can say.

These signs are this wiki's reading of L457. The paper gives no count, and this wiki does not supply one. The trackers in the study run from a few hundred issues to over a million (L303).

### What this sign does not establish

The study counts closed issues as well as open ones (L457), and its reason is the age of old trackers. It gives no measure of harm, and it reports what eight people raised in an hour. A few people's board is at the far low end of its range, so it may never reach this state from human requests alone.

### Remedy

The authors recommend that "Archiving very old issue data could reduce the overload and stress when searching for relevant issue data." (L718). This wiki keeps the point that an open list should hold what might still be done, and it reads that through the rule at the top of this page. Which archive feature to use is tracker configuration and out of scope.

### Agent executor note

The mechanism in the study is human attention, and it has two sides here. An agent can read every item on a board, so awareness of what exists is cheap for the plugin. But an agent can also create tasks far faster than a person, so a board may fill with items the people steering have never read. This wiki expects the limit to be what they can review, and no source tests this.
