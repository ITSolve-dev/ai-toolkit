---
title: What an Incoming Report Must Carry
category: intake
summary: A defect report is fit to become a task when it says how to reach the failure, what happened and what should have happened; those are what the repository cannot show, and most other fields are recoverable, hard for a reporter to supply, or rarely used.
tags: [rule, intake, task-content, bug-reports, agents, evidence]
sources: [zimmermann-good-bug-report, ambig-swe, montgomery-tracker-smells]
created: 2026-11-01
updated: 2026-11-01
---

# What an Incoming Report Must Carry

An incoming defect report has to tell the executor what only the reporter knows. This page applies [[recoverable-versus-task-only-facts]] to one kind of request, using the survey behind [[zimmermann-good-bug-report]]. It covers defect reports only. A request for new behaviour is covered by [[task-must-justify-itself]] and [[testable-acceptance]], and the study does not speak to it.

The authors summarise their developers' view:

> For the importance of items, steps to reproduce stand out clearly. Next in line are stack traces and test cases, both of which help to narrow down the search space for defects.
>
> — [[zimmermann-good-bug-report]], L265

This wiki does not copy that ranking directly, because it measures what experienced people found helpful in other people's open-source software, and a person who knows a system can supply things an agent cannot.

## The rule

A report is fit to become a task when it states:

1. how to reach the failure, as steps or as a failing case,
2. what happened, and
3. what should have happened.

Everything else is included when known and does not hold a report back, except an environment the failure depends on.

## Item by item

The study's column is from the paper's prose, since its tables are lost ([[zimmermann-good-bug-report]]). The right-hand column is this wiki's classification.

| Item | What the study says | This wiki's treatment |
|---|---|---|
| Steps to reproduce, or a failing case | Stands out for importance (L265) | Required. It is task-only unless the repository's tests already show the failure |
| Observed behaviour | Rated important, "albeit weakly" as a stand-in for steps (L265) | Required. The repository cannot show what the reporter saw |
| Expected behaviour | Among items of "relatively low importance" (L267) | Required, against the study; see below |
| Environment | Developers favoured a description of "the environment (or the context) when the error occurred" (L619), while a Mozilla developer found OS fields rarely needed (L271) | Required only if the failure depends on it |
| Stack trace, log output | Next in line, but "often hidden in log files and difficult to find" (L291) | Welcome. Recoverable if the executor can run the software |
| Test case | Helpful, and "test cases being the most difficult item" for reporters (L277) | Not asked of a reporter. Produced at reproduction ([[reproduce-before-accepting]]) |
| Component | "often it is impossible for them to locate the component in which a bug occurs" (L277), and of marginal importance to both sides (L291) | Not asked. Recoverable |
| Product, version, OS, hardware, severity | Relatively low importance (L263, L267), though version was high for Apache developers (L1109) | Not required, unless a project's history says otherwise |

The authors warn against reading low as useless: "Items with low importance in our survey are not totally irrelevant because they still might be needed to understand, reproduce, or triage bugs." (L273).

## Where this wiki departs from the study

Expected behaviour scored low with the study's developers. This wiki still requires it, for two reasons. The authors' own category of what agents gain from asking is "informational, which relates to the expected behavior or nature of the error" ([[ambig-swe]] L165), which this wiki treats as task-only. And an experienced developer who knows a system can usually tell what it should have done, while an agent reading a report guesses. That second reason is this wiki's reading, and neither source tests it. The transfer would be shown wrong if agents given observed behaviour alone resolved reports as well as agents also given the expected behaviour.

## Sign of violation

Task-content rules may use the omission as the sign, and this one does.

- **In the report:** nothing says how to reach the failure. The authors' extreme cases are "“Sem Web”", "“wqqwqw”", and just "“GUI” with comment “The page is too clumsy”" (L81).
- **In the report:** it says what happened and gives no statement of what should have.
- **At reproduction:** the steps given do not lead to the failure. This is a report that looks complete and is not, and it can only be caught by trying.
- **In the report:** it asks for help and reports no failure, such as the misfiled Eclipse report #175222 (L591-L597). That is a matter for [[triage-procedure]].

## Absent or wrong

The paper contains a quotable line that overstates its own finding. One developer's comment says "The biggest causes of delay are not wrong information, but absent information." (L315). That sentence is a survey comment and not the authors' conclusion. Their result is that "The most severe problems were errors in steps to reproduce and incomplete information." (L313), and their conclusion adds "wrong observed behavior" (L903). This wiki keeps the authors' version, so both absence and error count, and error is the harder of the two because it does not show in the text.

## Why asking harder is not enough

The study's central result is that reporters mostly know what is wanted. The relation between what developers find important and what reporters provide is about zero, at -0.035 (L299), while the relation between what developers find important and what reporters expect to be relevant is 0.839 (L305). The authors conclude that "ignorance of reporters is not a reason for the aforementioned information mismatch" (L305), and they point to difficulty (L277). They do suggest telling reporters what matters, for items like screenshots, and they add "At the same time, one should provide better tools to collect important information" (L307).

This wiki reads that as a limit on what a template can do: a form reminds people of what they already know. So the plugin should ask a reporter only for what is cheap for the reporter and impossible for the executor, which is the three items above, and it should leave the rest to the run, on the condition that the executor can run the software. That division is this wiki's and is unmeasured.

## Numbers and their conditions

All figures are from surveys of experienced Apache, Eclipse and Mozilla participants: 130 consistent developer responses and 215 consistent reporter responses (L247, L255). The authors say they "do not contend" the results transfer to closed-source projects (L863).

## Cost

Each required item can lose a report that a person would not finish writing. The paper's comments on complicated reporting concern tools and are not kept here. The interviews behind [[montgomery-tracker-smells]] name the same cost in tracker terms, "the amount of information that must be entered while creating an issue report, particularly when the required information is not known at the issue creation time" (L427). A few people can usually be asked in person, so this cost is smaller than in the study's setting, and it is the reason the list stops at three.

## Agent executor note

The three required items survive, and they matter more, because a developer can fill a gap by asking the reporter or by knowing the system, and an agent tends to proceed ([[agent-silence-is-not-completeness]]). Claims resting on a human reporter survive when the reporter is a person. When the reporter is an agent that hit a failure during a run, the difficulty argument falls away: it holds its own logs and steps, and it should supply all of them. The developers' setup complaints (L429, L431) describe human patience. An agent bears setup differently, and no source here says how.
