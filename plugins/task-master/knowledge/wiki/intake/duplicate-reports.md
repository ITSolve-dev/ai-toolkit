---
title: Duplicate Reports
category: intake
summary: A duplicate is closed against its original, and whatever it knows that the original does not is carried across first; the study behind this finds duplicates add information, and the test of a duplicate is one defect and not one symptom.
tags: [rule, intake, duplicates, bug-reports, evidence]
sources: [zimmermann-good-bug-report, kubernetes-issue-triage, montgomery-tracker-smells]
created: 2026-11-01
updated: 2026-11-01
---

# Duplicate Reports

A duplicate is a report of something already on the board. The usual treatment is to close it and move on, and the study behind [[zimmermann-good-bug-report]] argues against the second half of that:

> Our findings show that duplicates are likely to provide different perspectives and additional pointers to the origin of bugs, and thus can help developers to correct bugs. For example, having more stack traces reveals more active methods during a crash, which helps to narrow down the suspects.
>
> — [[zimmermann-good-bug-report]], L509

The authors contrast this with common practice, where duplicates "are simply closed and all information that they provided is discarded." (L479). Their recommendation is "Encourage users to submit additional details, ideally to an already existing bug report. Provide tool support for merging bugs." (L523). The tool half is out of scope, and the merge is kept.

## The rule

1. Whoever triages looks for duplicates. The reporter does not have to.
2. Test by defect and not by symptom, as below.
3. Before closing, carry into the original whatever the duplicate knows that the original does not.
4. Close the duplicate with a reference to the original.

Step 4 is the Kubernetes guide's practice: "Search for duplicates to see if the issue has been reported already. If a duplicate is found, let the issue reporter know, reference the original issue, and close the duplicate." ([[kubernetes-issue-triage]] L197). That guide says nothing about carrying information across, so the two sources do not conflict. Step 3 adds to it.

Step 1 comes from an argument the paper reports from Page: "Triagers are more skilled in detecting duplicates than users and they also know the system better." and "triagers can often decide within minutes" (L465). The authors also note that "Most reporters are aware that they should check first" (L411). The paper's survey shows developers treat duplicates as a small harm: they "do not suffer too much from bug duplicates" (L317), although the authors note that earlier research disagreed.

## The discriminating test

Two reports are duplicates if they concern one defect, and the same change would close both. Similar wording is not the test, and neither is similar behaviour. The paper names the harder direction, in which reports look different and are the same: "Sometimes, it is not obvious that two failures (error in the program execution) belong to the same defect (error in the program code)." (L533). The wording of the test is this wiki's.

## Kinds of duplicate, and what each needs

The authors list reasons in Section 5.2. This wiki keeps those that change what is done, and drops two that describe reporters and tool search.

| Kind | How it looks | What it needs | Source |
|---|---|---|---|
| Accidental resubmission | Same title, description, product and component, same user, less than 10 minutes apart | Close. Nothing to carry | L537-L539 |
| Several failures, one defect | Different symptoms that a single change closes | Carry each failure, since each is a case the fix must pass | L533 |
| Same defect, another reporter | A further report, often with more or other detail | Carry what is new | L499-L505 |
| Intentional resubmission | "I raised this issue several times, but it is still a problem." | Carry what is new, and look at the original: it has stalled | L535 |

In the last case, the authors say users resubmit "often out of frustration that it has not been fixed so far" (L535). This wiki reads that as evidence about the original rather than about the new report. The authors do not draw that step.

## Sign of violation

- **In board state:** an item closed as a duplicate whose text holds a fact, such as a failing case or an environment, that the original lacks.
- **In board history:** a fix closed the original, and the failure in a closed duplicate still occurs. That one was never a duplicate.
- **In board state:** two open tasks, both finished by one change. They were duplicates and nobody saw it.
- **In board state:** an item closed as a duplicate with no reference to the original. This one is a listed smell: "an issue is closed as “duplicate” but no duplicate link is added." ([[montgomery-tracker-smells]] L194). Four of the 7 participants who answered disagreed or said it depends (L536), and P19's reason was "they don’t use properties much". So it shows a missing record and does not show harm.

Apart from the listed smell, these signs are this wiki's.

Duplicates are also a symptom of something else. Participants traced them to search, "Difficulties in locating relevant existing issues lead to a less connected ITS, as well as duplicate issues." ([[montgomery-tracker-smells]] L454), and to overload ([[issue-overload]]). This wiki keeps the effect and leaves search features out as tool capability.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The new report | The request |
| Candidates for the original | Open and closed items on the board |
| Whether one change would close both | The repository, and reproduction ([[reproduce-before-accepting]]) |
| What the original lacks | Comparing the two texts |

The choice to close was wrong if the closed failure outlives the fix. The choice to keep two items was wrong if one change closes both. A search was too narrow if a duplicate is found only after work was done twice.

## Numbers and their conditions

These figures are from Eclipse and Mozilla only. They are averages of items added per master report, counting unique values, and the increase was significant at p < 0.001 by a one-sided paired t-test (L495). Table 4 is lost, so only the figures the prose repeats are available.

| Item | Added per master report | Project | Line |
|---|---|---|---|
| Operating systems | 0.631 | Eclipse | L497 |
| Operating systems | 1.102 | Mozilla | L497 |
| Patches | 0.113-0.146, a relative increase below 10 percent | Both | L503 |
| Screenshots | 0.143-0.187, roughly 100 percent | Both | L503 |
| Stack traces | 0.918, about 180 percent | Eclipse | L505 |
| New exceptions | 0.118 | Eclipse | L505 |
| Stack traces with new code locations | 0.281 | Eclipse | L505 |

The accidental count is 521 confirmed duplicates in Eclipse, by the definition in the table above (L539). One Eclipse bug was reported by 33 users over almost 900 days (L531). These counts describe large open-source projects with many strangers reporting, and a project of a few people will not see them.

What the figures show is that items exist, not that they helped. The authors' wording is careful: duplicates "could add" (L497) and "are likely to provide" (L509). No fix was timed against them.

## Cost

Reading a duplicate and carrying facts across takes longer than closing it. The study's developers report little harm from duplicates, so a project could reasonably close the accidental kind at once and spend the effort only on the others.

## Agent executor note

The information mechanism does not depend on who executes: a further failing case is useful to an agent. Two other mechanisms in the paper are about people. The discouraging of reporters, who become "reluctant to provide additional information" (L451, and the argument at L463), matters less when the reporters are a few known people. And the developers' ease with duplicates, which the authors explain as "Possibly developers can easily recognize duplicates" (L327), does not carry over: an agent handed a duplicate may simply do the work again, and nobody here has tested that. So the check belongs before a task starts, with the plugin and not with the executor.
