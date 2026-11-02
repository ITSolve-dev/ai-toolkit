---
title: Reproduce Before Accepting
category: intake
summary: A reported defect is accepted once someone has seen it happen; if it cannot be reproduced the findings go back to the reporter and it closes by agreement or after a stated follow-up goes unanswered, and a successful reproduction yields the check the task will be judged by.
tags: [decision-rule, intake, triage, bug-reports]
sources: [kubernetes-issue-triage, zimmermann-good-bug-report]
created: 2026-11-01
updated: 2026-11-02
---

# Reproduce Before Accepting

A report of a defect is a claim. This rule decides what happens to the claim before anyone fixes anything. The Kubernetes guide opens its section on bugs with it: "First, validate if the problem is a bug by trying to reproduce it." ([[kubernetes-issue-triage]] L192).

> If you can’t reproduce it:
>
> - Contact the issue reporter with your findings .
> - Close the issue if both the parties agree that it could not be reproduced.
>
> — [[kubernetes-issue-triage]], L199-L202

This wiki keeps the source's stray space before the full stop. The guide's next branch covers needing more from the reporter (L204-L206), and a timer covers silence: "In all cases, if you do not get a response within 20 days, close the issue with an appropriate comment." (L208). That value belongs to Kubernetes ([[closing-what-no-longer-applies]]).

## The rule

| Reproduction | Next step |
|---|---|
| It reproduces | Accept it, keep the reproduction as a failing case, and rate it |
| It does not reproduce | Send the findings to the reporter. Close by agreement, or after a stated follow-up goes unanswered: the guide closes on silence after 20 days "In all cases" (L208; [[closing-what-no-longer-applies]] rule 1) |
| It cannot be tried, or more is needed | Ask the reporter for what is missing, and set a follow-up |

Keeping the failing case is this wiki's addition, and the guide stops at validating. A failing case is the check that [[testable-acceptance]] asks for, so a successful reproduction has already written the task's acceptance.

## Why

A report can look complete and still be wrong. The survey behind [[zimmermann-good-bug-report]] found "errors in steps to reproduce" among the most severe problems (L313), and a footnote gives an example of wrong details at volume: "In ECLIPSE, 205 bug reports were submitted for “Windows” but later reassigned to “Linux.”" (L181). This wiki reads these as saying that reading a report cannot catch its errors, and only trying can.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| How to reach the failure | The report ([[incoming-report-content]]) |
| Whether the failure occurs | A run against the repository, in the stated environment |
| What the reporter says of the findings | The reporter |

The source does not state what would show this wrong, so these tests are this wiki's.

- **Closed wrongly:** the same failure is reported again after closing as not reproducible.
- **Accepted wrongly:** the failure seen at triage turns out to be a different one, so the fix passes its check and the reporter's problem remains.
- **Reproduced in the wrong place:** a failure that depends on an environment the executor does not have was called not reproducible. Read this from the environment named in the report.

## Cost

A reproduction takes a run and possibly a set-up, and it can be spent on a report that a person would have dismissed at a glance. The cheap checks therefore come first ([[triage-procedure]]). A failure that needs an environment nobody has cannot pass this rule, and it stays open as a question until it can be tried.

## Scale note

The guide is written for strangers reporting into a very large project, where the reporter may not be reachable and a triager cannot always run the case. With a few people, the reporter is usually reachable, so the agreement in the second branch is quick and the timer rarely fires.

## Agent executor note

This rule suits an agent, because reproducing is something it can do at the cost of a run, and the paper's developers' complaints about set-up (L429, L431) are about human patience. The second branch needs care. A person failing to reproduce has usually tried the case properly, while an agent may fail for reasons of its own, such as a wrong environment or a misread step. So an agent's failure to reproduce is weak evidence, and closing still takes a person. This caution is this wiki's, and no source tests it.
