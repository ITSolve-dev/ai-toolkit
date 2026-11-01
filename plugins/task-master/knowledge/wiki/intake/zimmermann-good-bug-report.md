---
title: What Makes a Good Bug Report? (Zimmermann et al.)
category: intake
summary: A 2010 IEEE TSE survey of developers and reporters on Apache, Eclipse and Mozilla, with a mining study of duplicates; it measures what experienced open-source people say helps, finds that reporters know what is needed and rarely supply it, and shows duplicates carry extra information.
tags: [summary, intake, bug-reports, evidence]
sources: [zimmermann-good-bug-report]
created: 2026-11-01
updated: 2026-11-01
---

# What Makes a Good Bug Report? (Zimmermann et al.)

This is a journal paper by Zimmermann, Premraj, Bettenburg, Just, Schröter and Weiss (IEEE Transactions on Software Engineering, vol. 36, no. 5, 2010; L65, L71). The raw file's `title` reads "untitled" and its `authors` field is empty, so these details come from the paper's own text. It is the only source in this wiki that surveys what people need from an incoming report, and the second source after [[ambig-swe]] to report a measurement.

## What was done

| Element | What it was | Lines |
|---|---|---|
| Developer survey | 872 invited, 156 responses, 26 discarded as inconsistent, 130 used | L101-L103, L219, L247 |
| Reporter survey | 1,354 invited, 310 responses, 95 discarded as inconsistent, 215 used | L107, L219, L255 |
| Who was invited | Experienced people only: developers assigned to at least 50 bug reports, reporters who submitted at least 25 and were assigned none | L155 |
| Questions | A fixed list of 16 items and 21 problems, each asked twice: what was used, and which three mattered most | L165-L175 |
| Quality ratings | 1,244 developer votes on 289 of 300 sampled reports, on a five-point scale | L105, L571, L723 |
| Comments | 175 comments, split into 237 statements and sorted by open card sort | L333-L335 |
| Duplicates | Reports from Eclipse and Mozilla, compared with and without their duplicates by counting unique items, using a one-sided paired t-test | L475, L495 |
| Mining | 50,000 reports from each project, 150,000 in all | L813 |

"Importance" in the paper is a conditional likelihood: how often an item was named among the three most helpful, given that the respondent had used it (L211). So an item few people use can still score high.

## Findings, with their conditions

**Reporters know, and do not supply.** Three Spearman correlations across the survey responses (L297-L305):

| Compared | Spearman | Line |
|---|---|---|
| What developers use against what reporters provide | 0.321 | L297 |
| What developers find most important against what reporters provide | -0.035 | L299 |
| What developers find most important against what reporters expect is relevant | 0.839 | L305 |

The authors' reading: "In other words, ignorance of reporters is not a reason for the aforementioned information mismatch." (L305). They point to difficulty, since test cases are the item reporters find hardest (L277), and to tools: "To a large extent, lacking tool support causes this mismatch." (L903).

**Which items matter.** The ranking comes through in prose only, because Tables 2 and 3 are lost ([[incoming-report-content]]).

**Which problems matter.** "Among the problems experienced by developers, incomplete information was, by far, most commonly encountered." (L311), and "The most severe problems were errors in steps to reproduce and incomplete information." (L313).

**Developers agree on quality.** Only 23 of 289 reports (8 percent) had a standard deviation of ratings above 1.5 (L611). This rests on small numbers of votes per report and voluntary raters.

**Duplicates add information.** The figures and their conditions are on [[duplicate-reports]].

**Quality and lifetime are separate.** Spearman correlations between ratings and lifetime were between 0.002 and 0.068 (L871). See [[flow-metrics]].

## Limits

The authors state these:

- Only experienced developers and reporters were asked (L851).
- Participation was voluntary, so results may lean toward people "who care about the quality of bug reports" (L853).
- The lists of items were not exhaustive (L861).
- The transfer is bounded: "We are confident that our findings also apply to smaller open-source projects. However, we do not contend that they are transferable to closed-software projects (which have no patches and rarely stack traces)." (L863).

This wiki adds these:

- It concerns bug reports. Feature requests are outside the study, and the authors note that such reports in the rated sample may reflect "an artifact of our sampling" (L619).
- It reports what people say helped and not what made fixes succeed, apart from the mined associations in Section 8, which are correlations.
- The respondents are people reading reports for other people's software. No agent is involved, and the paper is from 2010.
- A few people steering an agent are not a large open-source project. The reporter is often known and reachable, which is a difference from the strangers this study mostly describes.

## What this wiki took from it

- What a report must carry, and what it need not: [[incoming-report-content]].
- How to treat duplicates, and why not to discard them: [[duplicate-reports]].
- Why time to resolve does not read report quality: [[flow-metrics]].

## What this wiki dropped, and why

- **CUEZILLA** (L647-L807), its features, models and accuracies of 43 to 50 percent. This is tool design, and the authors call it "an early prototype" (L795).
- **Readability scores and itemization as quality features** (L699, L777). They were found by modelling ratings, they rest on a human reader, and they say nothing about what a report contains.
- **Rewards, reputation and motivation of reporters** (L367-L391, L811). These are incentives and people. That includes the comments on well-known reporters getting more attention (L373-L375), and the appendix's finding on experience and reputation, which the authors limit to Eclipse (L1013).
- **Tool recommendations** (L365, L403-L433): interfaces by user level, capture and replay, search features, translation volunteers. These are tracker capabilities.
- **The mined associations as advice** (L837-L841), such as stack traces going with faster fixes. They are correlations, offered as motivation for reporters. The authors themselves cite another study finding that reports with attachments are fixed later (L843).
- **Replication appendix and per-project tables** (L917-L1163), apart from the note that importance differed by project.

## Extraction caveat

- Tables 1 to 10 and all figures are missing from the raw file. Item-level percentages, the importance scores, and the counts behind Table 4 are therefore unavailable, and this wiki states only what the prose states.
- The overall response rate of 23.2 percent (L157) cannot be recomputed. 466 of 2,226 is 20.9 percent, and the difference presumably comes from bounces listed in the lost Table 1. This wiki does not rely on the figure.
- The extraction is noisy in places. L81 opens with "BUGallow reports". Minus signs come through as a replacement character, so this wiki reads the correlation at L299 as -0.035, relying on the text around it, which calls it "a huge gap" (L303), and on the footnote's scale at L301.

## How to read it

Trust the direction: incomplete reports hurt, reporters mostly know what is wanted, and duplicates are worth reading before they are closed. Do not carry the ranking of items across without thought, because it describes experienced humans fixing other people's open-source software, and at least one of its findings, on expected behaviour, does not transfer to an agent ([[incoming-report-content]]).
