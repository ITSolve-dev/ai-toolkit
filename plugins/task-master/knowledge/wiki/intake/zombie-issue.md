---
title: Zombie Issue
category: intake
summary: An open item nobody is acting on; it is the smell practitioners called most problematic, because what could have resolved it decays with time. The sign is an open item with no activity, and the source gives no length of time.
tags: [failure-mode, intake, board-history, evidence]
sources: [montgomery-tracker-smells, kubernetes-issue-triage, zimmermann-good-bug-report]
created: 2026-11-01
updated: 2026-11-02
---

# Zombie Issue

A zombie issue is an open item that nobody is acting on. It breaks the question of what to do with what came in, because the item has neither been done nor been decided against. The interviewed practitioners raised the problem unprompted, and they rated the matching smell above all others:

> The smell “ignored issue or delayed for too long”, declared as problematic by 15 participants (and only refuted by one), is the most problematic smell in our dataset. This smell is problematic because the longer an issue goes unresolved, the harder it is to resolve.
>
> — [[montgomery-tracker-smells]], L763

The authors' reasoning follows: "After enough time has passed, it might be unclear how to even replicate the reported problem, or who to go to for more information. If the issue is a requirement, it might not be relevant to the evolved system years or even just months later." (L763).

## Sign

- **In board history:** an open item with no activity for a long time. The smell's definition is "An issue has been open for a long time, either delayed or completely ignored." (L170).
- **In board history:** a held item with no output. The Kubernetes guide treats this as a trigger ([[closing-what-no-longer-applies]]).
- **In a new request:** someone reports the same thing again, with words like "I raised this issue several times" ([[zimmermann-good-bug-report]] L535, and see [[duplicate-reports]]).

The study does not say how long is long, and this wiki does not supply a figure. Under a flow setup, a started item is compared with the SLE ([[overrun-triggers-a-recut]]). An unstarted item has no such measure, because Work Item Age begins at the start ([[work-item-age]]), so this wiki reads its age from board history against the project's own distribution.

## What this sign does not establish

- That the item is a defect of the process. An unstarted item at the bottom of the order is supposed to wait. Rank 7 to 9 on [[ordering-by-value-and-urgency]] can wait a long time by design.
- That waiting did any harm. The evidence is what practitioners believe. "it remains unclear whether the perceptions of practitioners reflect the objective practice" (L753).
- Anything about a few people. Four of the 19 answers were disagreement (L530), for example where a team reviews issues weekly (L530), and the study's reasons for the problem include "older and larger" trackers (L459).

Apply [[smell-is-not-a-finding]] before reporting it.

## Causes the study names

These are from participants' accounts. The authors say "Specific causes for this problem include when the reporter and assignee are the same person (accountable only to themselves), and low-priority issues (minimal pressure to act)." (L459). They also suggest the number of issues and the lack of anyone answerable for the whole backlog (L763). Both of these survive at a small scale in some form.

## Remedies, and which survive

The authors recommend three workflows (L773). This wiki keeps two, in changed form.

- **Regular review of open issues.** The meeting is out of scope, and what it does can be kept: something looks at every open item on a schedule. That is the follow-up on [[triage-procedure]].
- **Someone curates the backlog.** That is what [[closing-what-no-longer-applies]] does, with the decisions left to a person.
- **Management assigns issues, with no self-assignment.** Dropped, as managing people.

The authors' suggested reminders after one week and three months are illustrations, marked "for example" (L763). They are not findings.

## Agent executor note

The authors' mechanism has three parts, and they do not all transfer. Forgetting how to reproduce and who to ask is human memory, and it depends on the people steering, so it survives for them. The system moving on survives whoever executes: a task written against code that has since changed misleads an agent, which has no memory to correct it. Pressure to act does not transfer at all, since an agent feels none, so a reminder addressed to it does nothing. The check has to come from the plugin. Before a long-open task starts, its text should be read again against the repository.
