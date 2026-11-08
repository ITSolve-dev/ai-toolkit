---
title: The Pragmatic Programmer, 20th Anniversary Edition
category: change
summary: "Source page, no rules of its own: what the book argues and covers, which edition a citation of it means, and how to read its tips, coined terms, exercise answers and general disclaimers before relying on them."
tags: [summary, source, pragmatic-programmer]
sources: [pragmatic-programmer]
created: 2026-11-01
updated: 2026-11-01
---

This is the source page for Thomas and Hunt's *The Pragmatic Programmer* in its 20th anniversary edition, read in the Russian translation published by Dialektika. Rule pages link here from `## Source`. The page states no rule. It describes what the book argues and covers, fixes which edition a citation refers to, and says how the book's own framing bears on what a citation can support.

## Thesis

The book calls itself practical and not theoretical: it concerns applying accumulated experience to make better decisions, and «Это книга о делании» (p. 23). Its position is that no best tool, language or operating system exists, so pragmatism means staying unattached to any one technology and having enough knowledge and experience to decide well in the circumstances at hand (p. 23). Under that stands a habit: «Думайте! О своей работе», meaning a continual critical appraisal of each decision as it is made (p. 25).

For design the book names one value under all its principles: a good design is easier to change than a bad one (p. 58). See [[easier-to-change]]. This wiki reads the rest of the book's code advice as what that value requires in particular cases.

## Authority

The book grew from notes the authors made while working with companies in difficulty in the 1990s (p. 19). They describe themselves as having helped start the agile movement (p. 20). Their authority is that of practitioners and consultants. The book reports experience and rarely measures anything, so this wiki cites a claim from it as the authors' judgement and not as an empirical finding.

## Scope

The book has nine chapters and an appendix of exercise answers. This wiki's map of what each chapter supplied, by page group:

| Chapter | Supplied | Left out |
|---|---|---|
| 1. Pragmatic philosophy | [[software-entropy]], [[good-enough-versus-broken-window]] | Responsibility, career, knowledge portfolio, communication |
| 2. Pragmatic approach | [[easier-to-change]], [[dry]], [[orthogonality]], [[reversibility]], [[tracer-code]], [[tracer-code-vs-prototype]], domain languages | Estimating |
| 3. Basic tools | [[plain-text-for-persistent-data]], [[debugging-procedure]], [[doc-examples-from-tested-code]] | Shells, editors, version control, most of text manipulation, engineering daybooks |
| 4. Pragmatic paranoia | [[design-by-contract]], [[crash-early]], [[assert-the-impossible]], [[finish-what-you-start]], [[small-steps-with-feedback]] | |
| 5. Flexibility or brittleness | [[coupling]], [[event-driven-code]], [[programs-transform-data]], [[inheritance-tax]], [[configuration-behind-a-thin-api]] | |
| 6. Concurrency | [[temporal-coupling]], [[shared-state-is-incorrect-state]], [[actor-model]], [[blackboard]] | |
| 7. While coding | [[prototype-when-code-resists]], [[programming-by-coincidence]], [[estimate-algorithm-order]], [[refactoring]], [[test-is-first-client]], [[property-based-testing]], [[distrust-external-input]], [[name-by-role]] | |
| 8. Before the project | [[find-the-real-constraints]], [[small-steps-with-feedback]] | Requirements, working together |
| 9. Pragmatic projects | [[test-levels]], [[sabotage-your-tests]], [[find-bugs-once]], [[test-early-often-automatically]] | Teams, delivery automation, delighting users, pride in the work |
| Appendix | Worked cases, such as [[assert-the-impossible]] and [[representation-that-fits-by-coincidence]] | |

## Limitations

These are this wiki's own assessment.

- **Rules outnumber their conditions.** The book seldom names a sign in code or a condition under which its advice fails. Most signs, limits and repairs on the rule pages are therefore this wiki's own, and each page says which.
- **Experience stands in for evidence.** A claim such as the ease of managing coupling in transformational code rests on the authors' experience. See [[programs-transform-data]].
- **Answers are not all sound.** The answer to exercise 14 does not close its own invariants, as [[design-by-contract]] shows, and the extracted listing for exercise 19 ignores the table passed to its constructor.
- **Two subjects are thin.** Functional programming is treated as idioms within a general book, and changing code safely gets little beyond one topic on refactoring. The charter names both as gaps to scout.
- **The edition read is a translation.** A quotation matches the Russian text. Terms and numbers can differ from the English original, so a page gives them as this edition states them. The text layer has recognition noise, so a quotation needs checking against the page image.

## Key takeaways

This wiki's selection of what the book gives a reader of code:

- A design is judged by the cost of the next change, and duplication of knowledge and coupling are the two main ways that cost grows. See [[dry]] and [[orthogonality]].
- A program should fail at the point where it is wrong: [[design-by-contract]], [[crash-early]] and [[assert-the-impossible]].
- Thinking of a program as data moving through stages removes much of what objects and shared state otherwise have to coordinate: [[programs-transform-data]] and [[shared-state-is-incorrect-state]].
- Code that works for a reason nobody can state will stop working for a reason nobody can find: [[programming-by-coincidence]].
- A suite earns trust only if its tests are seen to fail and every escaped defect adds one: [[sabotage-your-tests]] and [[find-bugs-once]].
- Decay starts locally and spreads, so a small visible defect is worth fixing or boarding up: [[software-entropy]] and [[broken-windows]].

## Which edition a citation means

The book opens with a foreword by Saron Yitbarek (pp. 16-18), the authors' introduction to the second edition (pp. 19-22) and material from the first edition's preface (pp. 23-27).

The authors say that about a third of the topics are new and that the others were reworked: «совершенно новыми, а остальные были частично или полностью переписаны» (p. 19). They removed dated references, naming CORBA, CASE and indexed loops (p. 19), and the foreword adds loop invariants and build machines (p. 16). The appendix of primary sources was dropped because it could not be kept current (p. 20). The concurrency topics were reorganised and rewritten. New material covers the agile movement, functional programming idioms, and privacy and security (p. 20).

The authors' reasoning is that technology changed and people did not, so the general principles still hold (p. 19).

This wiki reads that as a warning about recollection: a rule remembered from the first edition is not evidence of what this edition says, so a page cites only what was read here.

## How the book's statements are meant

**Topics and tips.** The book is a collection of short, self-contained topics that can be read in any order, tied together by cross-references (p. 20). Its numbered tips are meant to stand alone and be used daily (p. 20). This wiki takes from this that a tip may be cited alone as a statement of a rule, but the tip sentence does not make a page: the charter still requires a sign and a limit, and whatever the surrounding topic does not supply is marked as this wiki's own.

**Exercises and answers.** Exercises have relatively simple solutions, and challenges admit many. The answers sit in an appendix to show the authors' line of reasoning, although «лишь немногие из них имеют единственное правильное решение» (p. 20). This wiki therefore cites an answer as one way the authors reasoned, and not as the correct form of the code.

**Coined terms.** The authors deliberately pass over some serviceable terms and invent their own. Standard terms, they say, are tied to one domain or one stage of development, while one of the book's main principles is that «большая часть рекомендуемых нами методик оказывается универсальной» (p. 21). Their example is modularity, which they apply to source code, design, documentation and team organisation (p. 21). This wiki reads two consequences from that. A page uses such a term in the book's sense and defines it, because the ordinary sense of the word may mislead. And since this wiki's scope is code, a page records the code reading only and leaves out the transfer to documents and teams.

## What the authors say about the limits of their advice

The authors deny that a best tool, language or operating system exists. There are only «лишь такие системы, которые более пригодны в конкретных обстоятельствах» (p. 23). They describe the pragmatic programmer as fitting the approach to the current circumstances and reweighing the factors as the work proceeds (p. 24). They do not claim to answer all or even most of a programmer's questions, nor that their ideas apply in every possible case (p. 24).

This wiki reads these statements as licence for a `## When not to apply` section on every page drawn from the book. They cannot fill that section, though: they name no condition, so none of them can be cited as the limit of a particular rule.

The claim of universality on p. 21 and the disclaimer on p. 24 could look opposed. This wiki's reading, which the book does not state, is that they concern different things: the first says that a technique crosses kinds of artefact, and the second says that it does not cover every situation.

## Code examples

Most of the book's code is taken from compilable source files that the authors publish for download (p. 22). Pages here do not reproduce those listings. Their `## Before and after` pairs are this wiki's own pseudocode, as the charter requires.

## What was left out

The rest of the opening pages is out of scope, because it has no sign in code: the foreword's account of becoming a programmer, the traits of a pragmatic programmer, the tips on caring for the craft and thinking about one's work, individual craft in large teams, and kaizen as personal improvement (pp. 16-18, 24-27).

The same holds across the book for career, team, process and estimation advice, tool use, and delivery operations, as the `## Scope` table lists. The charter excludes them, and they are not judged here.
