---
title: Defect-detection techniques are complementary
category: testing
summary: "Concept: a green suite is taken as proof of a change, but a typical unit or integration test level finds about 30-35% of defects; reading code finds interface defects that tests miss and shows the cause, not just the symptom."
tags: [concept, testing, code-review, inspection, defect-detection]
paradigm: any
sources: [code-complete]
created: 2026-11-06
updated: 2026-11-06
---

No single technique for finding defects catches most of them, and different techniques catch different kinds. McConnell builds this case from published data in chapter 20 of *Code Complete*. This wiki reads it as the reason a passing test suite is not evidence that code is defect-free, and why reading the code stays useful even when the tests pass.

## How much each technique finds

Table 20-2 (p. 463, after Jones 1986 and 1996 and Shull et al. 2002) gives the share of the defects present at that stage that each technique removes, as low / typical / high. Selected typical values:

| Technique | Typical |
|---|---|
| Informal code review | 25% |
| Formal code inspection | 60% |
| Desk-checking code | 40% |
| Modelling or prototyping | 65% |
| Unit testing | 30% |
| Integration testing | 35% |
| Regression testing | 25% |
| System testing | 40% |
| Large beta (over 1000 sites) | 75% |

The book's reading: typical efficiency never goes above 75% and averages about 40%. The two most popular techniques, unit and integration testing, «позволяют найти обычно только около 30–35% дефектов» (p. 463). A testing-heavy approach removes about 85% of defects; the best organisations reach 95% or more by using a wider set of techniques (Jones 2000). Jones also reports that unit, function and system testing combined often find under 60% (p. 464).

## Different techniques find different defects

- In Myers's study (1978, pp. 463-464), experienced programmers looked for 15 known errors using specification-based testing, testing with the source available, or inspection. They found between 1 and 9 errors, averaging 5.1. No single technique was significantly better than another. Any two combined, even the same technique run by two independent groups, nearly doubled the count.
- Reviewers find different defects from each other: only about one in five defects found in inspections was found by two or more people (p. 464).
- Reading code finds more interface defects, while functional testing finds more control-flow defects (Basili, Selby and Hutchens 1986, p. 464).
- Informal testing usually reaches only 50-60% code coverage unless a coverage analyser is used (Beizer, p. 464); see [[code-coverage]].

## Finding a cause versus finding a symptom

The book separates **one-step** techniques from **two-step** ones (pp. 465-466). An inspection finds the symptom and the cause together; a test shows a symptom, and diagnosing the cause is extra work. The figures it cites: code reading found about 80% more defects per hour than testing (Basili and Selby 1987); an inspection cost 3.5 hours per defect against 15-25 for testing at IBM (Kaplan 1995), and 3 hours against 12 for find-and-fix at Microsoft (Moore 1992).

The recommended mix (p. 466): formal inspection of requirements, architecture and the critical parts of the design; modelling or prototyping; code reading or inspection; and execution testing.

## What this changes when working on code

The conclusions in this section are this wiki's own reading of the figures above, not statements made in the book.

- A green test suite does not certify a change; it certifies whatever the tests pin. A review that reads the code still has work to do, especially at interfaces: argument order, units, null or empty handling across a call, and the contract between caller and callee ([[match-arguments-to-parameters]], [[state-the-contract]]). The book's data says these are what reading catches better than tests.
- When a test fails, it gives only a symptom. Rereading the code around it first uses the cheaper one-step route before falling back to the method in [[debugging-procedure]].
- Without a coverage measurement a suite's coverage is unknown, and the cited averages put informal testing near 50-60%; measure it before trusting it ([[code-coverage]]).

## Limits

- These figures are industry averages from the 1970s to the 1990s, measured over whole projects. This wiki reads them as showing which technique dominates at scale, not the yield on one function.
- The figures describe teams and processes. Which techniques a project adopts is a process decision outside this wiki's scope; only the code-level reading above belongs here.
- The book itself warns that comparing cost per defect ignores the number of defects found, when they were found, and other factors (p. 465).
- High-reliability systems (spacecraft, life support) pay more for quality regardless (p. 468).

## Context: the General Principle of Software Quality

The chapter ends on the claim that improving quality lowers development cost, because debugging and rework take about half of a traditional schedule (p. 467). It cites a NASA SEL survey of 50 projects (Card 1987) and IBM data (Jones 2000). In DeMarco and Lister's 1985 study, the programmers who took a middling amount of time made the most errors (p. 468). This is the economic argument for the mix above; as a statement about project process it gets no page of its own here.

## Related

- [[quality-characteristics-trade-offs]]
- [[code-inspection]]
- [[developer-testing]]
- [[debugging-procedure]]

## Source

McConnell, *Code Complete*, 2nd ed., Russian edition, ch. 20, via [[code-complete]]: Table 20-2 and its reading on p. 463; Myers, the reviewer-overlap figure, Basili, Selby and Hutchens, and Beizer on pp. 463-464; Table 20-3 (the extreme programming mix, about 90% typical) on p. 465; cost of finding and fixing, and one-step versus two-step techniques, on pp. 465-466; the General Principle on pp. 467-468. This wiki's own: the section on what this changes when working on code, including the interface checklist and the advice to measure coverage before trusting a suite, and the limits other than the last two.
