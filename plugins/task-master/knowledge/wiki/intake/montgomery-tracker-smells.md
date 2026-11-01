---
title: Smells Depend on the Context (Montgomery et al.)
category: intake
summary: An interview study of 26 practitioners on 31 issue-tracker smells and 14 common problems; many smells drew "no" or "it depends", so a smell is a prompt and not a verdict. It gives signs with no thresholds, drawn from perceptions in mostly large companies, and no agent appears in it.
tags: [summary, intake, failures, audit, evidence]
sources: [montgomery-tracker-smells]
created: 2026-11-01
updated: 2026-11-01
---

# Smells Depend on the Context (Montgomery et al.)

This is an interview study, in the authors' version of an article accepted by ACM Transactions on Software Engineering and Methodology (L3, L44; arXiv 2601.04124). The raw file's `authors` field is empty. "Montgomery et al." comes from the paper's citation of its own replication package (L334), and the paper's byline did not survive extraction.

## What was done

| Element | What it was | Lines |
|---|---|---|
| Participants | 26 practitioners from 19 companies: 16 developers, 6 managers, 4 product owners, with 1.5 to 25 years of experience | L93, L264-L297 |
| Company size | 17 large, 7 medium, 2 small, by this wiki's count of the participant table | L264-L291 |
| Tracker size | From 100-1k issues to over a million | L264-L303 |
| Sampling | Through the authors' network, mostly Germany, and "A representative sample was not sought, as we did not aim to generalise our qualitative observations." | L293 |
| Interviews | One hour, semi-structured, not recorded, with two interviewers taking notes; 15 in English and 11 in German, whose notes were translated | L309-L319 |
| Data | 3,660 notes, thematically analysed for problems and closed-coded for smells | L369, L394-L404 |
| Smells | 31 from 11 literature sources, chosen for neither completeness nor representativeness | L239, L243 |
| Coding | Each answer coded yes, no, depends or no answer, with 74% initial agreement (κ = 0.61) and 100% after an alignment session | L404, L493 |

## Thesis

All 31 smells were noted as occurring by at least some participants, and most were noted as problematic by some, but 98 of 290 comments on whether a smell is problematic were "no" or "it depends" (L499-L500). The authors conclude that relevance and severity depend on context (L744), and they name 13 context factors (L558-L571).

## What it does not establish

Every page that files a smell from this study holds these limits.

- **No thresholds.** The smells are worded "too long", "too many" and "for too long" (L148, L160, L169), and the study never says how much. The figures in the authors' suggestions for tools, one week, three months, 100 characters, 30 words, 300 characters (L757, L763, L767), are illustrations marked "for example" and are not findings. This wiki does not use them.
- **Perception, not outcome.** "it remains unclear whether the perceptions of practitioners reflect the objective practice" (L753). No issue data was analysed.
- **No prevalence.** The authors "refrain from claiming generalisability" (L800). A count of participants who mentioned something measures what came up in an hour.
- **"Disagreement" is a merged code.** It joins "no" and "it depends" (L504), and a figure such as 8/9 uses as its base those who answered, not all 26.
- **No few-people setting.** Two of the 26 work at small companies. Team size is a named context factor (L566), so the study itself says this matters.
- **No agent.** Every mechanism in it is about people using a tracker.

Quotations attributed to a participant are the interviewers' notes and not recordings, and some are translated. This wiki quotes them as the paper prints them.

## The 31 smells, and where each is filed

A count is "participants in disagreement / participants who answered", from the text. "None" means the text gives no result, because the coded figure is lost.

| ID | Smell | Count | Filed under |
|---|---|---|---|
| S1.1 | No or short description | 6/17; 11 problematic, 3 refuted (L524, L767) | [[underspecified-task]] |
| S1.2 | Description too long | 6/13 (L522) | [[underspecified-task]] |
| S1.3 | Issues are missing properties | 9/15 (L518) | [[empty-fields]] |
| S1.4 | Issues are assigned to a team | 8/9 (L514) | Not kept: assignment and people, and it is mostly refuted |
| S1.5 | Often switching properties | 4/13 (L528) | [[backward-movement]] |
| S1.6 | Too many issue types | None | [[judging-board-columns]] |
| S1.7 | No link to commit | 4/12 (L526) | Not kept: tracker configuration prevents it |
| S1.8 | Non-assignee resolved issue | 7/10 (L516) | Not kept: assignment and people, and it is mostly refuted |
| S1.9 | Ignored issue or delayed for too long | 4/19; 15 problematic, 1 refuted (L530, L763) | [[zombie-issue]] |
| S1.10 | No comments or too many comments | 9/19 (L520) | Not kept: nothing separates the good case from the bad |
| S1.11 | Toxic discussions | None | Not kept: managing people |
| S1.12 | Properties discussed in comments but not updated | 12 problematic, 0 refuted (L765) | [[fact-stranded-outside-the-task]] |
| S2.1 | Issue without any links | 7/14 (L538) | Not kept: half refuted, and no sign of harm |
| S2.2 | Too many link types | None | Not kept: tracker configuration |
| S2.3 | Multiple links with differing types | None | Not kept: tracker configuration |
| S2.4 | Known link mentioned in comments but not documented | None | [[fact-stranded-outside-the-task]] |
| S2.5 | Mismatch between link types and properties | 4/7 (L536) | [[duplicate-reports]] |
| S2.6 | Mismatch of linked issues' priorities and statuses | 2/10 (L540) | [[what-may-move]] |
| S2.7 | Epic without sub-issues, or the reverse | None | Not kept: tracker hierarchy |
| S2.8 | Circular dependencies | None | [[independent-tasks]] |
| S3.1 | Unplanned work added during sprint | 5/15 (L548) | [[mid-period-change]], [[interrupting-started-work]] |
| S3.2 | Too many complex issues in one sprint | 4/14 (L552) | [[filling-a-period]] |
| S3.3 | Issues are missing an estimate | 2/8 (L554) | [[empty-fields]] |
| S3.4 | Inconsistent or unclear estimate scales | None | [[size-ceiling]] |
| S3.5 | Sprint does not end at the scheduled time | None | [[period-length]] |
| S3.6 | Sprints have different duration | None | [[period-length]] |
| S3.7 | Sprint length differs from recommended length | None | [[period-length]], as not a failure |
| S3.8 | Sprint has to be repeatedly delayed | None | [[period-length]] |
| S3.9 | No acceptance criteria, or too many | 2/7 (L550) | [[testable-acceptance]] |
| S3.10 | Acceptance criteria not checked during testing | None | [[testable-acceptance]] |
| S3.11 | Acceptance criteria changed during sprint | 5/5 (L546) | [[testable-acceptance]] |

## The 14 problems, and where each is filed

These came up before participants saw the smell list (L417). Counts are participants who mentioned the problem.

| Problem | Count | Line | Filed under |
|---|---|---|---|
| Missing Issue Information | 18 | L438 | [[underspecified-task]], [[fact-stranded-outside-the-task]] |
| Lack of a Fitting Workflow | 17 | L423 | [[judging-board-columns]] |
| Lack of Workflow Support | 15 | L425 | Not kept: tracker automation |
| Workflow Bloat | 14 | L427 | [[judging-board-columns]], [[incoming-report-content]] |
| Divergent Tracking Needs | 11 | L467 | Not kept: many teams on one tracker |
| Ineffective Search | 10 | L448 | Tool not kept; its effect is on [[duplicate-reports]] |
| Information Islands | 10 | L470 | [[fact-stranded-outside-the-task]] |
| Lack of Mindset & Discipline | 9 | L479 | Not kept: managing people |
| Scoping Issues is Hard | 9 | L487 | [[started-and-finished-points]] |
| Issue Overload | 8 | L457 | [[issue-overload]] |
| Zombie Issues | 8 | L459 | [[zombie-issue]] |
| Lack of Comprehensive Overview | 8 | L461 | Not kept: a tracker feature, and this wiki has no visualization pages yet |
| Lack of Workflow Enforcement | 6 | L429 | [[empty-fields]] |
| Unclear Workflow | 5 | L431 | [[started-and-finished-points]], [[judging-board-columns]] |

## What this wiki took from it

The governing point, that a smell is reported as a question until its context is checked, is on [[smell-is-not-a-finding]]. The tables above give the rest.

## What this wiki dropped, and why

- **All of RQ3** (L582-L628), apart from two remarks on the form of a report kept on [[smell-is-not-a-finding]]. It is tool design, feedback on four prototype screens.
- **Recommendations to tool vendors and on training** (L734-L740, L757, L777). Tool capabilities and managing people.
- **Management assigning issues and forbidding self-assignment** (L773). Managing people. The other two workflows there, regular review and a curated backlog, are kept on [[zombie-issue]].
- **Role differences** between managers and developers (L425, L440, L461, L739). Individual and organisational.
- **Related work** (L630-L694). This wiki does not cite the authors' secondary reports of other studies as findings.

## Extraction caveat

- The names of the context factors are missing from the text wherever they appear inline, as in "the context factor of , whereby" (L514). The table at L558-L571 keeps them. Which factor a passage means has to be inferred from its definition, so this wiki quotes around these gaps and gives factor names only from the table.
- The figure with the coded responses per smell (L494) is lost. So 13 of the 31 smells have no result in the text, and the "None" entries above are a gap in the extraction and not a finding.
- The smell table at L112-L143 lost its names. They follow at L145-L236 in the same order, and this wiki pairs them by order. "Same as S1.12, but specific to links." (L191) and the IDs used in the text agree with that pairing.
- The source's own slips are kept in quotation, such as "acceptable criteria" for "acceptance criteria" (L230).

## An inconsistency in the source

The conclusion lists "missing commits in issue reports" among what is generally considered problematic (L804). The discussion's three most problematic smells do not include it (L761-L767), and S1.7 is reported as prevented by automation (L526). This wiki follows the discussion.

## How to read it

Read it as a catalogue of what to look at and a warning about what looking proves. It is independent of the Kanban school behind [[judging-board-columns]], which is worth something on its own. Its strongest finding is negative: a sign that seems plainly bad is often an intended part of how someone works.
