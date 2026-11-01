---
title: Triage Procedure
category: intake
summary: What to do with an item that came in; mark it as not yet looked at, take the oldest first, sort it into a few outcomes with the cheap checks before the costly ones, check the requester's classification, rate what is accepted, and set what follows up. Adapted from a very large project's process.
tags: [method, intake, triage]
sources: [kubernetes-issue-triage, zimmermann-good-bug-report, montgomery-tracker-smells]
created: 2026-11-01
updated: 2026-11-01
---

# Triage Procedure

Triage decides what an incoming item is and what happens to it, before anyone works on it. The Kubernetes guide's definition, for a much larger setting than this wiki's:

> Issue triage is a process by which a SIG intakes and reviews new GitHub issues and requests, and organizes them to be actioned—either by its own members, or by other SIGs. Triaging involves categorizing issues and pull requests based on factors such as priority/urgency, SIG ownership of the issue, and the issue kind (bug, feature, etc.).
>
> — [[kubernetes-issue-triage]], L58

This wiki notes the scale first. That guide describes one of the largest open-source projects, with groups, bots and permissions, and reports no measurement. The procedure below keeps what a triager there has to decide and drops how the project organises people to do it ([[kubernetes-issue-triage]]). The order of steps is this wiki's adaptation, and it departs from the guide in one place, marked below.

## The procedure

1. **Mark arrival.** A new item carries a marker saying it has not been looked at. In the guide, "New issues are automatically assigned a `needs-triage` label" (L152), and `/triage accepted` replaces it. The board must be able to show the difference.
2. **Take the oldest first.** The guide suggests "filtering out the oldest, unlabelled issues and pull requests first" (L168). This is the order of triage and not of work. Work order comes from step 7.
3. **Sort it into an outcome,** from the table below. Do the cheap checks first. The guide starts by looking for "open issues that can be quickly closed" (L172).
4. **Look for a duplicate** by reading the board ([[duplicate-reports]]). The guide does this after reproducing a bug (L194-L197). This wiki moves it earlier, since reading costs little and a reproduction costs a run. A candidate found here is still confirmed by reproduction where the case is unclear.
5. **Check the classification.** A requester's "bug" is a claim. The guide says "Issues that feature the wrong `kind` (for example, support requests labelled as bugs) can be corrected by someone triaging; double-checking is a good approach." (L222). The cost of skipping this is plain in the paper behind [[zimmermann-good-bug-report]]: "Still, misfiled bug reports take away valuable time" (L591).
6. **For a defect, reproduce it** ([[reproduce-before-accepting]]).
7. **Rate what is accepted** ([[ordering-by-value-and-urgency]]). In the guide, "If an issue lacks a `priority` label, this means it has not been reviewed and prioritized yet." (L226). So an absent rating is a state and not a defect until triage has passed ([[empty-fields]]).
8. **Set the follow-up,** so that what stops gets noticed ([[closing-what-no-longer-applies]]).

## Outcomes

| What it turns out to be | Outcome | Page or line |
|---|---|---|
| A question or a request for help | Answer or redirect it. No task | L178 |
| Abandoned, or in the wrong place | Close it, or say why it stays | L184 |
| Missing what is needed | Ask once, and set a follow-up | [[incoming-report-content]], [[clarifying-questions]], L188, L206 |
| A duplicate | Carry what is new and close | [[duplicate-reports]] |
| A defect that reproduces | Accepted, and rated | [[reproduce-before-accepting]] |
| A defect that does not reproduce | Report findings and agree | [[reproduce-before-accepting]] |
| A request for new behaviour | Accepted once it can be cut and checked | [[task-must-justify-itself]], [[testable-acceptance]], [[story-splitting-patterns]] |
| Possibly useful, with nothing yet behind it | Held as a placeholder, outside the order | [[incomparable-tasks]], L236 |

The list of outcomes is this wiki's assembly from the guide's Step Two and its priority table. The guide treats a feature request only as a `kind` and gives it no path of its own.

## How often

The guide allows either form: "Triage can happen asynchronously and continuously, or in regularly scheduled meetings." (L60). One group reports that regularity is what counts: "The api-machinery SIG has found that consistently meeting on a regular, fixed schedule is key to the success of a triaging effort. More frequent, small meetings are better than infrequent, large meetings." (L136). That is one group's report and no measurement. Its meetings are out of scope. The interviews behind [[montgomery-tracker-smells]] point the same way: the most mentioned context factor, at 48 mentions, is workflow design, defined as "Smell is caught early or prevented entirely as part of a standard workflow, such as regular issue review meetings" (L559), and seven participants saw triage meetings as a place to check quality (L609). That too is what people said. This wiki reads the point that survives as small and often, which for a plugin means triaging an item when it arrives and showing the result when the person steering next looks.

## Who decides

The plugin can do the reading, the search, the proposal and the reproduction. Closing is the person's decision, as is the rating, because each rests on facts the repository does not hold. The guide itself requires agreement before closing as not reproducible (L202).

## Sign of violation

- **In board state:** a started task that never left the not-yet-looked-at state, or a board with no such state at all and no other way of telling.
- **In board state:** items waiting for triage that are older than items already triaged.
- **In board history:** a task closed as a duplicate, a question or not reproducible after work on it started. Triage should have caught that before capacity was spent.

These signs are this wiki's.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| What the item says | The request |
| What is already on the board | Open and closed items |
| Whether a defect reproduces | A run against the repository |
| Whether the requester can add anything | The requester |

A triage decision was wrong if a closed item returns as a new request, or if an accepted item is found to be a non-issue after work has started.

## Cost

Triage spends the attention of the people steering before any work happens. A project with few requests, all from the person steering, may need only steps 5 to 7. Nothing here says at what volume the full procedure starts to pay for itself.

## Agent executor note

No source tests an agent as a triager. In the guide, every step is a person with permission to act, and the checks rest on that person's judgement. This wiki expects the reading steps to transfer, since they are classification, and it expects the risk to sit in closing, where a wrong answer loses a real report without anyone noticing. That is why the decision stays with a person.
