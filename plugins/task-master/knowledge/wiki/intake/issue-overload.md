---
title: Issue Overload
category: intake
summary: More open items than anyone can keep in mind, which shows up as duplicates and forgotten work; the sign is new requests that repeat what is already there, and the source gives no count at which it starts.
tags: [failure-mode, intake, evidence]
sources: [montgomery-tracker-smells]
created: 2026-11-01
updated: 2026-11-01
---

# Issue Overload

Issue overload is having more items on a board than the people using it can keep track of. It breaks the question of what to do with what came in, since nobody can tell whether a new request is new. Eight of the 26 interviewed practitioners raised it, and a participant's note reads: "having so many issues can be a problem. We are not sure what to do with all of these issues" (P15, [[montgomery-tracker-smells]] L457).

> The consequences of this smell include a lack of awareness of existing issues, leading to duplicates and overlapping issues, missed links, and issues being forgotten.
>
> — [[montgomery-tracker-smells]], L457

## Sign

- **In board state:** new requests repeat items already open, and the repetition is found late ([[duplicate-reports]]).
- **In board state:** many open items that have not been rated or looked at for a long time ([[zombie-issue]]).
- **In a person's answer:** asked what is on the board, nobody can say.

These signs are this wiki's reading of L457. The paper gives no count, and this wiki does not supply one. The trackers in the study run from a few hundred issues to over a million (L303).

## What this sign does not establish

The study counts closed issues as well as open ones (L457), and its reason is the age of old trackers. It gives no measure of harm, and it reports what eight people raised in an hour. A few people's board is at the far low end of its range, so it may never reach this state from human requests alone.

## Remedy

The authors recommend that "Archiving very old issue data could reduce the overload and stress when searching for relevant issue data." (L718). This wiki keeps the point that an open list should hold what might still be done, and it reads that through [[closing-what-no-longer-applies]]. Which archive feature to use is tracker configuration and out of scope.

## Agent executor note

The mechanism in the study is human attention, and it has two sides here. An agent can read every item on a board, so awareness of what exists is cheap for the plugin. But an agent can also create tasks far faster than a person, so a board may fill with items the people steering have never read. This wiki expects the limit to be what they can review, and no source tests this.
