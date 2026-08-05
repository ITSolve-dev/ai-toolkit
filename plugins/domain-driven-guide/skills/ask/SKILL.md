---
name: ask
description: >-
  Ask a Domain-Driven Design question and get an answer from the plugin's curated DDD knowledge
  base, with citations. Bounded contexts, aggregates and consistency boundaries, entities and
  value objects, repositories, domain services, domain events, context mapping, CQRS, event
  sourcing, DDD anti-patterns — and "does this code actually follow DDD".
argument-hint: "<your DDD question>"
allowed-tools: Read(${CLAUDE_PLUGIN_ROOT}/knowledge/**)
context: fork
agent: domain-driven-guide:guide
background: false
---

Answer this Domain-Driven Design question from the knowledge base:

$ARGUMENTS

## How to answer

**Be dense.** Length follows the question — a factual one gets a few sentences, a design call
gets the reasoning, the trade-off, and what breaks if it goes the other way. No preamble, no
restating the question back, no filler, no summary of what you just said.

**Cite.** Every substantive claim points at the wiki page it came from.

**When the question is ambiguous** in a way that changes the answer: answer under the most
likely reading, state that assumption in one line, and end with the clarifying question. You
run in an isolated context and cannot ask mid-flight — the caller relays it. If it genuinely
cannot be answered without more input, return only the questions.

**When the question is not about DDD**, or falls outside the base's charter in `SCHEMA.md`: say
so in a line or two and stop. Do not stretch DDD over an unrelated problem, and do not answer
from general knowledge as though it came from the wiki.
