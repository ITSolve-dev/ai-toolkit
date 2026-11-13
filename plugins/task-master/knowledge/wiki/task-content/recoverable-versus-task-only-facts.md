---
title: Recoverable Versus Task-Only Facts
category: task-content
summary: A fact the executor cannot recover from the repository must be in the task; a fact it can recover is welcome but does not hold a task back from being ready.
tags: [decision-rule, task-content, agents, readiness, evidence]
sources: [ambig-swe]
created: 2026-11-01
updated: 2026-11-01
---

# Recoverable Versus Task-Only Facts

This test decides whether a fact has to be in a task. It comes from a distinction the Ambig-SWE authors draw between two kinds of information an agent gains by asking:

> In the Interaction setting of the previous experiment, the information gained can be broadly categorized into two types: informational, which relates to the expected behavior or nature of the error, and navigational, which pertains to the locations of the files to modify. The latter can be considered redundant information as it can be recovered from the codebase.
>
> — [[ambig-swe]], L165

## The decision

Ask of each fact: could an executor find this by reading the repository?

- **No, it is task-only.** Expected behaviour, the nature of the error, constraints and choices that live in someone's head. The task must carry it, and a task without it is not ready.
- **Yes, it is recoverable.** File locations and implementation details the code already shows. Include it when known, and do not hold a task back for lack of it.

The two-way split and the commitment are this wiki's extension of the authors' two categories, which they use to analyse results and do not offer as a rule.

## Why

The authors' conclusion supports the line:

> The most effective questions are specific, actionable, and task-level, while vague prompts or implementation details recoverable from the codebase add little value.
>
> — [[ambig-swe]], L273

This wiki reads that as saying what is valuable when asked is what is valuable when written. The transfer from questions to task text is this wiki's.

The numbers need care, because they do not make recoverable facts worthless. In Table 1, resolve rates were higher when navigational details were obtained for five of the six models: Claude Sonnet 3.5 went from 37.94% to 59.52%, and Claude Sonnet 4 from 60.82% to 67.24% (L169-L171). This is why this page says "include it when known". Two things stop that from being a stronger rule:

- The model chose when to ask, so the comparison is not randomised, and the instances on which it asked may differ from the others. This caution is this wiki's. The authors present the split as an impact on performance (L165, L176).
- The effect is not uniform. Qwen 3 Coder did worse with file locations, 52.38% against 55.43% (L170), which the authors explain as re-exploring code to find what it had already been told, and which "wastes interaction turns on redundant navigational information, preventing the model from asking more valuable clarifying questions about task requirements" (L176).

## Inputs, where each is read from, and what would show the choice wrong

| Input | Read from |
|---|---|
| The fact in question | The request or the task |
| Whether the repository holds it | The repository, by reading it |

The classification was wrong if a run failed or was reworked on a fact marked recoverable that the repository did not in fact show. It was too strict if tasks were held back for facts that the executor then found unaided.

## Agent executor note

The evidence here is about agents, on the benchmark described on [[ambig-swe]]: stripped Python issues, a simulated user, and resolve rates set by unit tests. The test also holds for a person, who can read a repository too. What the agent changes is the cost of getting it wrong, because a person would ask about a task-only fact and an agent tends not to ([[agent-silence-is-not-completeness]]).

## Applied to incoming reports

[[incoming-report-content]] applies this test to a defect report, item by item.

## Scope limit

This rule does not ask for step-by-step instructions. Expanding a task that way is outside the charter, and the authors' finding that recoverable implementation details add little points the same way.
