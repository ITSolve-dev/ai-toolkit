# Organizing Work on a Board — SCHEMA

<!--
This file is the CHARTER and the ROOT MARKER: its presence marks this directory as a wiki
root, and its contents are the lens ingest uses to decide what to keep.

Per Karpathy, the schema is "what makes the LLM a disciplined wiki maintainer rather than a
generic chatbot" — and it is a LIVING document you and the LLM co-evolve as you learn what
works for this domain. The generic structure/conventions/workflows live in the llm-wiki
plugin; this file holds the DOMAIN-SPECIFIC charter and any local overrides. Fill every
section, then keep refining it.
-->

## Purpose

A working reference for organizing software work: how to cut it into tasks, estimate them, order
them, keep a board honest, and read what happened afterwards.

It serves the skills and agents of the plugin that bundles this wiki. They judge from it instead of
reasoning from general knowledge, because a planning judgement without a citation reads exactly
like an invented one, and a wrong one surfaces weeks later, when nobody can say where it came from.

The base doubles as a test of an existing board: a rule stored here carries the sign that reveals
its violation, so the same page advises and audits.

A claim belongs here only if it changes what the plugin outputs when it cuts, sizes, orders, moves,
lays out or explains work for a few people steering an AI agent.

## Scope — the ingestion lens

Ingest judges every candidate fact from a source against this. A claim that only holds at another
team scale is noted as such or dropped. A claim whose mechanism depends on a human executor — pace,
memory, filling gaps from context — is kept only with a note on whether it survives an agent executing
and a person steering.

**In scope (keep):**
- **Decomposition:** what makes a unit of work a unit, signs of a bad cut, and what to do with a task
  that fails. The working tests: once started, the task can be finished without waiting, and its
  result is presented once.
- **Task content:** what a task must carry for an executor that guesses instead of recalling: purpose,
  boundaries, non-goals, acceptance criteria, readiness.
- **Dependencies:** a sequence versus a wait, and how they constrain order.
- **Estimation:** relative estimation and what it converts to; what each step of a scale means and the
  size above which a task is cut; what an estimate does not promise; how it is refined against fact.
- **Prioritization:** what tasks are compared by, what to do with incomparable ones, urgency versus
  importance.
- **Intake triage:** checking and clarifying a request, classifying it, cutting duplicates and what
  no longer applies.
- **Board rules by methodology:** what each methodology claims about moving tasks, limiting concurrent
  work, and commitments over a period. Several methodologies, because the rule for what moves where
  depends on the choice made when a project is set up.
- **Work states:** which states of work are distinguishable and why, and how a board's columns are
  judged against them. The plugin's canonical state set or the criteria for one come from this topic.
- **Iterations:** length, filling, planning a date, a period versus a milestone.
- **Retrospective analysis:** velocity, throughput, time in state and age of open work, and what each
  measures and does not; comparing plan and fact, and explaining the difference.
- **Visualization:** which chart answers which question, and which question it cannot ask.
- **Failures:** typical defects of a board and a process, each with its observable sign and filed
  under the question it breaks.

**Out of scope (drop):**
- Capabilities of particular trackers: they are configuration, and change faster than a page lives.
- Scripts for meetings. The plugin prepares material; it does not run a ceremony. Facilitation decides
  things a board does not show.
- Managing people: motivation, individual load, hiring, skills.
- Tracking spent hours as a practice. Time a task lived is read from board history; logged hours
  need someone to keep them.
- Frameworks for scaling across many teams. They answer how to align dozens of teams; applied to a
  few people they give ritual instead of process.
- Writing the documents that drive development: design docs, requirements, decision records. That is
  `spec-driven-guide`.
- Executing a task, and expanding one into step-by-step instructions.

## Domain extraction schema

From each source, extract these kinds of knowledge:

- **Rules that detect**, each with the sign by which a violation shows up in a task's text, in board
  state, or in board history. Rules about cutting need the first: they apply before a task reaches a
  board.
- **Rules that choose** — what comes first, how big this is — each with its inputs, where each input is
  read from, and what later fact would show the choice wrong.
- **The reasoning under a rule** — what specifically breaks when it is ignored.
- **Discriminating criteria** — what separates two neighbouring cases: one task from two, urgent from
  important, a period from a milestone.
- **Trade-offs** — what a rule costs when followed.
- **Failure modes**, with the observable sign of each.
- **Numbers with their conditions.** A figure without the setting that produced it is not knowledge.

## Grouping principle

Pages live in subdirectories of `wiki/`, named by this domain's own topics, so the folder tree is
self-documenting. New groups are created as topics appear. A page's `category` frontmatter equals its
folder name.

Group by the **question someone organizing work arrives with**, not by source and not by methodology:
how to cut this, what a task must carry, what it costs, what comes first, what to do with what came
in, what state this is, what may move, what fits in a period, what actually happened, how to show it.

A page goes where its rule is applied. A failure goes under the question it breaks, with its kind kept
in `tags`. A methodology's position is a section on the page where it differs, so comparing two
methodologies does not mean opening two trees.

## Languages

- **Wiki language:** English — pages, summaries, and synthesis are written in English, because the
  sources are and a quotation has to stay verbatim.
- **Communication language:** Russian — the LLM converses in Russian (questions, surfaced takeaways,
  reports).

## Conventions

- Pages, frontmatter, and `[[wikilinks]]` follow the `llm-wiki` plugin's page conventions.
- Link style: `[[slug]]` (Obsidian-style).
- Keep `sources:` as an inline list: lint reads top-level scalars only, and a block list earns a page
  no inbound credit.

### Page kinds

The first entry in `tags` is the page's kind.

| Kind | What it holds |
|---|---|
| `summary` | One per ingested source |
| `concept` | An idea, defined and situated |
| `rule` | A prescription, with its observable sign |
| `method` | A procedure to run against a task, a board, or its history |
| `decision-rule` | A test deciding between two courses |
| `failure-mode` | A defect, with its observable sign |

### Pages this wiki authored itself

Some pages carry `sources: []` and an explicit provenance note. They exist where the charter names
something in scope and no ingested source treats it. They say what would have to be found to ground
them. Their number should go down, not up.

## Workflow customizations

- **Ingest: a rule is kept only if it can be caught or applied.** A rule that detects states the sign
  of its violation; a rule that chooses states its inputs, where each is read from, and what later
  fact would show the choice wrong. A rule that chooses cannot lean on "no basis was stated" as its
  sign, because any rule can meet that; a rule about task content can, since what it detects is the
  omission. "Communicate well" and "stay agile" are commentary, not knowledge for this wiki. Much of what is written about boards fails this
  test, and that is expected. Descriptive pages and source summaries are exempt: they prescribe
  nothing. Lint does not check this; page review does.
- **Ingest: a practitioner source is graded on its mechanisms, not its magnitudes.** Keep a claim that
  names something observable; drop one that only asserts a size of effect.
- **Ingest: where methodologies disagree, the page resolves it per setting.** It states which choice
  holds under which project setup, since the setup is what the plugin knows. Reporting a disagreement
  and leaving it open returns only the easy cases.
- **Ingest: the held-out material below is never read.** A document that reached this base cannot test
  it: the base is the answer key.
- **Writing: any sentence extending a quotation opens with an explicit subject.** "This wiki reads that
  as…", "the transfer here is ours…". A block quote followed by unbroken declarative prose makes the
  extension read as the source's, which is the failure most damaging to a base whose value is that a
  reader can go and check.
- **Compression runs once per release, after the whole base passes lint and review,** because review
  reads for attribution and compressed prose hides it. Pages are written in plain prose until then.
  The commit before it is tagged `task-master-wiki-readable-<version>` and the tag is logged.
- **Compression uses `caveman-compress`, then `tools/verify_compressed.py`.** The tool's own validator
  does not see quotations, wikilinks, negations or numbers; the script does. Frontmatter, headings,
  blockquotes, inline quotations, wikilinks, citations, numbers and negation words must match exactly,
  and each sentence after a blockquote stays unchanged. A page that fails is restored from git and
  compressed by hand.
- **Editing a compressed page starts from the readable page at the last tag:** edit, review, recompress.
  `log.md` and `wiki/index.md` are not compressed.

### Held-out material

Reserved for checking the plugin. Scout and ingest skip these. **No source is ingested until this list
is filled.**

- One private design document with the requests that came out of it, for checking decomposition. It
  stays outside this repository; a person running the check knows which it is.
- The boards used for checking board review, once they exist.

## Notes

Sources were chosen by two scouting passes against this charter, plus three books. The file offered
for Reinertsen's *Principles of Product Development Flow* is a third-party summary, not the book, and
was rejected; see the log. Priority without it rests on the qualitative cost-of-delay source.

The test "once started, it can be finished without waiting" has no source: it comes from the plugin's
design, and pages using it say so. Review of a presented result is not a wait inside the task: the
executor's part has ended.

A section resolving a disagreement per project setup is the wiki's own reading and says so. It does not
count against the rule that self-authored pages should go down: that rule is about claims with no
source, and these sections sit on sourced positions.

<!-- Co-evolution log: record decisions about how THIS wiki is run as they emerge. -->

- 2026-11-01 — Charter written before the first source, from the plugin's design. Two changes against
  that design's topic list: **work states** became a topic of its own, because the canonical state set
  is meant to be derived from this base and no other topic would have carried it; and rules about
  cutting may carry their sign in a task's text, because they apply before a board has anything to show.

- 2026-11-01 — A second opinion on this charter changed four things, before any source. **Rules that
  choose got their own test:** the sign rule fits a rule that detects, but a board cannot show a wrong
  order, and the rule would have emptied prioritization, the judgement `triage` and `schedule` exist
  for. A missing field does not count as a sign, because any rule can meet that. **Relevance moved into
  Purpose:** the sign rule tests checkability, "limit WIP" passes it, and scout's assessors see Purpose
  rather than Scope. **Task content and dependencies became topics:** the design rests on both and the
  list named neither. **`failure-modes` as a group and the `position` kind were dropped,** repeating
  what `spec-driven-guide` learned on 2026-08-24.

  Two predictions to check rather than rules: work states will likely yield criteria for a mapping, not
  a fixed set, since Kanban has teams map their own flow; and intake triage is the likeliest topic to end
  up self-authored.
