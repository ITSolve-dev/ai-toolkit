---
name: ask
description: >-
  Ask a question about writing a design doc, a decision record, or instructions for an agent, and
  get an answer from the plugin's curated knowledge base, with citations. How high to write and
  what to leave out, which document type this is, how to phrase a statement so it can be checked,
  what a decision record owes, how to review a document — and "is this passage too much detail".
argument-hint: "<your question about writing the document>"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**)
context: fork
agent: spec-driven-guide:guide
background: false
---

Answer this question about writing documents that drive development, from the knowledge base:

$ARGUMENTS

## How to answer

**Be dense.** Length follows the question — a factual one gets a few sentences, a boundary call
gets the criterion, a case on each side of it, and what breaks if it goes the other way.

**Cite.** Every substantive claim points at the wiki page it came from.

**When the question is ambiguous** in a way that changes the answer: answer under the most likely
reading, state that assumption in one line, and end with the clarifying question. You run in an
isolated context and cannot ask mid-flight — the caller relays it. Where it genuinely cannot be
answered without more input, return only the questions.

**When the question falls outside the charter in `SCHEMA.md`** — planning, task breakdown,
estimation, doc tooling, end-user documentation — say so in a line or two and stop.
