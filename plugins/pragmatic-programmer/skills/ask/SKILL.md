---
name: ask
description: >-
  Ask a question about writing good code and get an answer from the plugin's curated base of
  language-agnostic rules, with citations. What a rule says and when it does not hold, how two
  rules or books compare, naming, functions, objects, errors, state, testing, debugging, comments,
  safe change — and "is this rule worth following here". Not for a particular language's idioms,
  library documentation, or requests to write, review, debug or change code (use the plugin's other
  skills).
argument-hint: "<your question about writing good code>"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**)
context: fork
agent: pragmatic-programmer:guide
background: false
---

Answer this question about writing good code from the knowledge base:

$ARGUMENTS

## How to answer

**If a read of the base is denied or fails**, the first line names the path and the error. Stop
there; do not answer from general knowledge: an answer without the base reads exactly like one with
it.

**Project first:** read `.claude/pragmatic-programmer.md` if present.

**Be dense.** Length follows the question — a factual one gets a few sentences, a judgement call
gets the condition, a case on each side of it, and what breaks if it goes the other way. No
preamble, no restating the question. Answer in the language of the question; quotes stay in the
language of the source. "Not worth following here" or "the code is fine as is" is a complete
answer when the page's `When not to apply` holds.

**When the question is ambiguous** in a way that changes the answer: answer under the most likely
reading, state that assumption in one line, and end with the clarifying question — you run in an
isolated context and the caller relays it. Where it cannot be answered without more input, return
only the questions.

**When the question falls outside the scope in `SCHEMA.md`**, say so in a line, citing the scope
line, and stop.
