---
title: Issue Triage Guidelines (Kubernetes)
category: intake
summary: The Kubernetes contributor guide to triaging incoming issues; a five-step process for one of the largest open-source projects, unsigned and unmeasured, of which the outcomes, the order of checks and the follow-up triggers survive at a few people and the groups, labels, bots and meetings do not.
tags: [summary, intake, triage, open-source]
sources: [kubernetes-issue-triage]
created: 2026-11-01
updated: 2026-11-02
---

# Issue Triage Guidelines (Kubernetes)

This is a page from the Kubernetes contributor documentation at kubernetes.dev. The raw file's `authors` and `published` fields are empty, so the page is cited as the project's and it has no date. It is the base's only source that describes triage as a procedure, and the charter predicted that this topic would otherwise be self-authored.

## Grade and scale

The page is a project's process document. It states what contributors there should do, and it reports no measurement. Its benefits are hearsay by its own wording: "SIGs who triage regularly say it offers a number of benefits" (L64).

Scale matters more here than for any other source in this wiki. The project divides components among Special Interest Groups, runs a bot for labels, has contributors without permission to close issues, and has someone in a "triage engineer" role (L172, L263). Its issues come from strangers. Even so the page limits itself: "These guidelines only apply to the Kubernetes repository." (L54). So nothing here is claimed for a small project, and each page built on it says what was kept and why. The charter's test is applied below.

## Thesis

Issues are reviewed as they arrive and sorted into a few outcomes: closed as not work, sent back for information, or accepted with a priority and an owner. Anything accepted is then followed up on a timer, so that nothing lingers.

## What survives at a few people steering an agent

| Kept | Why it survives | Page |
|---|---|---|
| The set of outcomes for an incoming item | They describe the item and not the project's size | [[triage-procedure]] |
| A marker for "not yet looked at" (L152) | The board has to show it at any size | [[triage-procedure]] |
| A requester's classification is a claim to check (L222) | Requesters mistake a question for a bug at any size | [[triage-procedure]] |
| Reproduce first, and close by agreement or after 20 days without a response (L192-L208) | It is about evidence | [[reproduce-before-accepting]] |
| Reference the original and close the duplicate (L197) | It is about the record | [[duplicate-reports]] |
| Triggers for items that have stopped (L208, L263-L271) | The triggers survive and their values do not | [[closing-what-no-longer-applies]] |
| A held placeholder for ideas with no support yet (L236) | It answers what to do with what cannot be rated | [[incomparable-tasks]] |
| Priority definitions (L230-L236) | As a contrast to two ratings | [[urgent-versus-important]] |
| The top level that stops other work (L232) | A second voice on the same point | [[interrupting-started-work]] |
| One holder for a task (L257) | The collision is real with several agents | [[what-may-move]] |

## What this wiki dropped, and why

- **SIG ownership** (L238-L251). It answers which of dozens of groups owns an issue, which is multi-team scaling. A few people have no such question.
- **Triage Party, GitHub project boards, DevStats, the Prow bot and its commands, label names as such** (L84-L118, L152, L240-L255). These are tracker capabilities and tools.
- **Meeting practice** (L122-L146). This covers api-machinery's agenda, consensus, and who attends. One sentence about regularity is kept on [[triage-procedure]], as that group's report.
- **Help wanted and good first issue** (L210-L218). These recruit contributors.
- **Load balancing and asking people before assigning** (L138), **company diversity** (L141), **skill-building and community benefits** (L71-L74). These are managing people.
- **The benefit list** (L66-L72) as evidence. It is self-report.
- **Support channels and the template reply** (L275-L294). They are specific to this community. The idea that a question is redirected is kept.

## Extraction caveat

- The priority table's Examples column shows `[ **XXXX**]` for three of five rows (L233-L235). These look like placeholders in the published page, and this wiki reads no examples into them.
- The examples for `priority/critical-urgent` lost their separators and read "user-visible bugs in core features broken builds tests and critical security issues" (L232). A page quoting them transcribes this as a list and says so.
- The list of support channels at L277 and the sentence's continuation at L290 are empty.

## Inconsistencies in the source

- The heading at L261 says no PR "Within the Current Release Cycle", while the text under it says "within 30 days" (L263). This wiki uses the text and notes the difference.
- L271 says a stale issue "will eventually be auto-closed" and gives no period, so the page offers no total time to closure.

## How to read it

Read it as the shape of a procedure from a very large project. Its steps are what a triager has to decide, and they translate. Its people, permissions, numbers of days and labels do not. A figure such as 20 or 90 days records what suited that project, and a few people should not adopt it without reading their own history ([[closing-what-no-longer-applies]]).
