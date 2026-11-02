---
title: One Estimate per Task, Not One per Role
category: sizing
summary: A task carries one aggregate estimate, reached by judging the whole and not by adding role or phase parts; per-role estimates multiply planning bookkeeping and are justified only where parallel versions must match and people cannot substitute.
tags: [rule, estimation, ideal-days, planning-cost, failure-mode, task-content]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# One Estimate per Task, Not One per Role

A task carries one aggregate estimate, not a separate estimate for each role or person who will touch it. Cohn states this for [[ideal-days]]: "assign one aggregate estimate to each user story" ([[cohn-agile-estimating-planning]] L1143). If the parts are known, "it is better to sum those and say the story as a whole will take nine ideal days" rather than record four programmer days, two tester days and three product owner days (L1157).

## The sign

- A task's text or estimate field splits the number by role or person, or by coloured markers and stickers as in Cohn's example (L1143).
- Velocity or remaining work is kept separately per role.

A sign raises a question: check whether the exception below applies before calling it a defect. This rule settles what is recorded; how the number is reached is a separate failure, on *Summed Role Estimates* (below).

## What breaks when it is ignored

Cohn puts the cost in planning. Per-role estimates "vastly increases the amount of work necessary to plan a release", because the plan must then take each role into account, and "we’d have to track velocity and remaining work for each role as well" (L1145). This wiki reads the mechanism as bookkeeping that multiplies: one number per task becomes one number per role per task, and each role needs its own [[velocity]] for the plan to mean anything.

Cohn also objects that the split shifts thinking away from a shared team mentality (L1145). That is a claim about managing people and is out of scope here.

## The exception

Cohn allows one: "While this is rarely worth the additional effort it may sometimes be necessary." (L1147). His case had two conditions together:

- Parallel versions must match: "it is absolutely critical that each version be released with exactly the same functionality" (L1147).
- People cannot substitute: "the individuals on this team do not currently have the skills to switch between Mac, Windows, and handheld development" (L1147).

Even then the team "may want to" estimate per role, and "should, however, be aware of the extra administrative burden this will require" (L1147).

## Trade-off

This wiki notes that following the rule hides any imbalance inside one number. A task that needs a scarce role looks the same as one that does not, so a bottleneck on that role will not appear in the estimates and has to be seen elsewhere.

## Agent executor note

This wiki reads the bookkeeping argument as surviving unchanged, and the team-mentality argument as irrelevant. The transfer here is ours: a split between agent execution and a person's review would be a role split by this rule. It also comes close to the exception's second condition, because a person's review cannot be substituted by the agent. The source does not address this setting, so the default stays one number, and a split needs the same justification Cohn asks for.

## Summed Role Estimates

A summed estimate is reached by each specialty sizing its own part and adding the results, in place of one judgement of the whole task. Cohn ties the habit to ideal days: "Estimating ideal days, on the other hand, often involves specialty groups estimating how long “their part” of a story will take and then summing these sub-estimates." ([[cohn-agile-estimating-planning]] L1558). His example has programmers at three ideal days, the database engineer at one and the tester at two, which gives an estimate of six (L1558).

### Why it matters

The contrast is in what the estimate forces people to talk about. "Because a story point estimate needs to be a single number that represents all of the work for the whole team, estimating story points initiates high-level discussions about everything that will be involved." (L1558). Cohn claims a lasting effect: the way the earliest discussion goes has "an ongoing impact on how the story is developed" (L1560). He later sets the two framings side by side, “my part will take three ideal days and your part will take two ideal days so the total is five ideal days” against “overall this story seems about the same size as that one so let’s call it five story points also.” (L1636).

A related mechanism feeds the same habit: in ideal days "it is easier to think about the individual tasks necessary to develop a story" (L1596), which also lengthens estimating.

### Relation to one estimate per task

The rule at the top of this page can read as approving this section's defect, since Chapter 5 says of known role figures that "it is better to sum those" (L1157). This wiki reads the two chapters as answering different questions. Chapter 5 settles what is recorded: one number, not one per role. Chapter 8 settles how that number is reached: by judging the whole and not by adding parts. A sum recorded as one number passes the first and not the second. Adding up pieces also remains a named way of estimating, with its own limit, on [[estimation-techniques]] and [[over-disaggregation]], so a sum raises the question and does not settle it.

### Observable signs

These signs are this wiki's derivation. Each raises a question to check.

- A task's text or comments show an estimate as a sum by role or phase.
- Several partial estimates sit on one task with no judgement of the whole.
- Sub-tasks are estimated and the parent carries only their total.

### Scope of the claim

Cohn's argument is mainly about making a human team behave cross-functionally, and how people identify with their department is outside this wiki. Kept here is only the effect on the estimate: a whole-task number compels someone to consider the whole task.

### With an agent executing

The literal form needs several specialists, so with one executor it mostly disappears. This wiki reads the risk as surviving in a phase-shaped version, for instance implementing plus testing plus review added up, and that sum can leave out what falls between the parts. Whether a whole-task number gives better estimates than a phase sum when an agent is the executor is not established by this source.

The unit that discourages the habit is [[story-points]]; the choice is on [[ideal-days]]. Comparing a task to an earlier one, as in the second framing above, is the alternative to adding up its parts.
