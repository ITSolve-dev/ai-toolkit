---
name: writing-discipline
description: >-
  Use when writing or editing any document that drives development — a design doc, a decision
  record, instructions for an agent, a section of any of them. The discipline that decides what
  a passage may state, how high to pitch it, and how to phrase it so it can be checked.
---

# Writing discipline

Genre-neutral. The genre skills add what a design doc or a decision record owes on top of this.

Each rule below carries the symptom that reveals its violation **in the text**, and a page in the
bundled base holding the reasoning. Read the page when a case is borderline; the symptom is enough
for the clear ones. Base root: `${CLAUDE_PLUGIN_ROOT}/knowledge` — open pages there, not from a copy
of this plugin that happens to sit in the project you are working in.

## 1. State the commitment, not the means

Two tests, both applied to the same passage:

- **Replaceability** — could the named thing be swapped for another without changing what the
  document promises? Then it is mechanism. Name the promise instead.
- **Lifespan** — does it change faster than the document that names it? Then naming it makes the
  document wrong rather than detailed.

The discriminator is not concreteness. Operation names, parameters, types, schemas and API
contracts are commitments and stay; storage formats, internal decomposition, library choices,
file paths and framework-specific implementations are mechanism and go.

**Exception, with three conditions all required.** A fragment stays when it encodes the decision
more exactly than prose can (state machine, reducer, schema, type shape), prose genuinely cannot
match its precision, and it is trimmed to the lines a reader would have to change in order to
change the decision. A fragment that runs — imports, setup, error paths — has failed the third.

*Symptom:* a passage you can rewrite with a different tool, library or file name while every
promise in the document still holds.
→ `wiki/obligation-and-mechanism/state-the-commitment-not-the-means.md`,
`wiki/obligation-and-mechanism/when-a-snippet-beats-prose.md`

## 2. Do not restate what the environment already says

A document copying a config file, a directory layout or a `--help` output is a cache of a lookup,
and it goes stale against its original. Write what cannot be found by looking: the unwritten
convention, the reason behind a choice, the trap no artifact confesses.

*Symptom:* a fact a reader could obtain by opening one file in the repository.
→ `wiki/reviewing/pruning-a-document.md`

## 3. Declare the level, then hold it

Fix who the document is for and at what grain before writing. Every statement then sits at that
grain. A document about a system commits more coarsely than one about a component, and the line in
rule 1 moves with it.

*Symptom:* two adjacent statements whose readers are different — one addressed to someone choosing
between approaches, the next to someone typing.
→ `wiki/altitude/defining-a-level.md`, `wiki/altitude/mixed-levels-of-abstraction.md`

## 4. Cut mechanism; never cut obligation

Every rule above says remove. The floor stops them: a document may drop anything not required to
establish what it commits to, and may not drop what is. Minimal is not short.

Where a document is long and **every line in it is live and unique**, the repair is relocation —
push what only some readers need behind a reference to it, split paths so each carries its own
share. Deleting live material there removes obligations while feeling like discipline.

*Symptom of the floor breached:* the document reads as principled and a reader with a decision to
make cannot make it. Every sentence looks defensible; what is wrong is absent.
→ `wiki/writing-for-agents/minimal-is-not-short.md`, `wiki/writing-for-agents/sprawl.md`

## 5. Make every statement checkable

- **Force is earned.** Reserve the strong form for what breaks interoperation or causes harm. Every
  statement a MUST carries no more information than none of them being.
- **Bounds are clear and demanding.** "Every X accounted for" obliges; "produce a list of X" is met
  by a file existing. Ask what the cheapest thing is that satisfies each criterion as written.
- **Prefer the positive.** State the target behaviour rather than the banned one; a prohibition
  earns its place only where no positive form exists, and then states the target beside it.
- **One word beats a restated triad.** Where the same three-word phrase appears at several sites in
  one sense, replace it with a word that names the state — ideally an observable one.

*Symptom:* a claim no reader could disagree with — "robust", "clean", "as needed", "where
appropriate".
→ `wiki/statement-quality/obligation-language.md`,
`wiki/statement-quality/imperatives-constrain-outcomes-not-methods.md`,
`wiki/statement-quality/completion-criteria.md`, `wiki/statement-quality/leading-words.md`,
`wiki/statement-quality/imprecise-terminology.md`

## 6. Every claim carries its because

An assertion without its reasoning cannot be applied to a case its author did not foresee, and
cannot be argued with. This is the sentence that makes a document outlive the discussion behind it.

*Symptom:* a decision stated with no reason, or with "for consistency" as the reason.
→ `wiki/decision-records/every-argument-carries-a-because.md`

## 7. Structure: two anchors, then importance

No template. The document takes the shape its content needs, within two fixed anchors:

- **The problem statement opens it** — context and what is wrong, before any solution.
- **Open questions close it.**

Between them, order sections by descending importance to the reader, not by the order the work will
be done in. Processing order is a description of one execution and does not survive the execution
changing.

*Symptom:* a section order that mirrors a sequence of steps.
→ `wiki/structure/processing-order-is-not-a-structure.md`

## Language and project conventions

Write in the language the project uses. Where `.claude/spec-driven-guide.md` exists in the working
project, it sets the language and any local conventions, and it wins over the defaults here.
