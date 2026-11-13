---
title: A Smell Is Not a Finding
category: reading-history
summary: A sign on a board prompts a check and does not prove a defect; before reporting one as a failure, check whether the project's workflow prevents it, intends it, or limits it to a stage, a kind of task or a property, and say what the sign does not establish.
tags: [decision-rule, audit, failures, reading-history]
sources: [montgomery-tracker-smells]
created: 2026-11-01
updated: 2026-11-01
---

# A Smell Is Not a Finding

This wiki's charter says the base doubles as a test of an existing board. This rule limits that test. A sign on a board shows that something may be wrong. Whether it is wrong depends on how the project works, which the sign does not show. The word comes from code smells:

> The concept of a “smell” is borrowed from “code smells” in which something is “smelly” if it may lead to a problem, but not necessarily.
>
> — [[montgomery-tracker-smells]], L79

The authors showed 31 smells from the literature to 26 practitioners, and 98 of 290 comments on whether a smell is problematic were "no" or "it depends" (L500). Their summary: "What is considered risky for some was a deliberate, intended procedure for others." (L745). This wiki reads that as applying to its own signs too. Most signs in this base were written by this wiki, and none was tested on a real board.

## The rule

Before a sign goes in a report as a failure:

1. **Is it prevented or caught?** The project's stated workflow or the tracker's configuration may already deal with it.
2. **Is it intended?** Some patterns are how a project works, such as passing a task between author and reviewer ([[backward-movement]]).
3. **Is it limited?** A sign may apply only at one stage, to one kind of task, to one property, or at a certain size.
4. **If it survives,** report it with the page's statement of what it does not establish, and as a question to the people steering.
5. **If a project has declared it intended,** stop reporting it.

## The context factors

The study names 13 and counts their mentions (L558-L571). The first three account for 63 percent (L575).

| Context factor | Mentions | What it means for a sign |
|---|---|---|
| workflow design | 48 | Caught early or prevented by a standard workflow |
| intended outcome | 44 | The sign is what the workflow means to produce |
| ITS configuration | 24 | The tracker prevents it |
| supervisor involvement | 11 | Someone above monitors it |
| team preference | 9 | The team accepts it |
| workflow stage | 8 | A problem only at some stages |
| issue property | 8 | A problem for some properties only |
| team size | 7 | More or less of a problem at some sizes |
| issue complexity | 6 | Depends on how complex the task is |
| issue type | 5 | A problem for some kinds of task only |
| issue dependency | 5 | Depends on how the task relates to others |
| stakeholder role | 5 | A problem for some users only |
| customer priority | 4 | A customer overrides the usual route |

Supervisor involvement and stakeholder role concern a hierarchy that a few people do not have, so the plugin can ignore them. Customer priority is on [[interrupting-started-work]]. That reading is this wiki's.

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The sign | Board state, board history, or the task text |
| The project's stated workflow | Project configuration |
| The task's stage and kind | Board state |
| What the project has declared intended | Project configuration, or an earlier answer from the people steering |

The choice was too cautious if a sign was held back as intended and the failure it warns of then occurred. It was too eager if the people steering repeatedly dismiss a reported sign as intended. No source states these tests, and they are this wiki's.

## How to report one

Two participants commented on the form, in an interview section on tools. P17 said "the information needs to be pre-digested into actions being requested of the developers; they can then decide to do it, or not", and P02 said "but they don’t need the stats, just the lists of smells and where/how to fix it" (L626). P21 wanted to see "the change over time" and not only a static view (L624), and P24 warned that "optimising for green isn’t always good" (L624). This wiki reads these as saying a board report should name the task, the sign and the action, and should leave the decision open. They are remarks from interview notes and not findings.

## Cost

The rule asks for project context that may not exist, and it makes a report slower. A project with nothing declared gets every sign as a question, which spends attention. The cost falls as declared intentions build up.

## Agent executor note

The rule concerns what a sign proves, so it survives. The study has no agent in it, and its contexts are human ones, such as what a team has agreed in a meeting. Where such a context is only in people's heads, an agent cannot read it. So the plugin has to ask, or read a stated workflow. Its own signs could also be wrong in ways nobody has measured, and that is the case for reporting them as questions.
