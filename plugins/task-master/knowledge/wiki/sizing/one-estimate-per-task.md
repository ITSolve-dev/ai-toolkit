---
title: One Estimate per Task, Not One per Role
category: sizing
summary: Give each task a single aggregate estimate. Per-role estimates force velocity and remaining work to be tracked per role, which is rarely worth it unless roles truly cannot substitute for one another.
tags: [rule, estimation, ideal-days, planning-cost]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# One Estimate per Task, Not One per Role

A task carries one aggregate estimate, not a separate estimate for each role or person who will touch it. Cohn states this for [[ideal-days]]: "assign one aggregate estimate to each user story" ([[cohn-agile-estimating-planning]] L1143). If the parts are known, "it is better to sum those and say the story as a whole will take nine ideal days" rather than record four programmer days, two tester days and three product owner days (L1157).

## The sign

- A task's text or estimate field splits the number by role or person, or by coloured markers and stickers as in Cohn's example (L1143).
- Velocity or remaining work is kept separately per role.

A sign raises a question: check whether the exception below applies before calling it a defect. This rule settles what is recorded; how the number is reached is a separate failure, on [[summed-role-estimates]].

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
