# spec-driven-guide

Write design docs, decision records and agent instructions that keep their obligations and shed
the mechanism — so a document survives the implementation changing underneath it, and can move
between projects.

Grounded in a curated knowledge base bundled with the plugin. Every answer cites the page it came
from.

## Use it

```
/spec-driven-guide:init                    # once per repository
/spec-driven-guide:ask is a JSON schema too much detail for a design doc?
/spec-driven-guide:prepare-brief           # raw intent → something writable
/spec-driven-guide:write-design-doc
/spec-driven-guide:write-decision-record
/spec-driven-guide:review-doc docs/specs/notifications.md
```

## The rule the plugin is built on

**State the commitment, not the means.** Two tests decide any passage:

- **Replaceability** — could the named thing be swapped without changing what the document
  promises? Then it is mechanism.
- **Lifespan** — does it change faster than the document naming it? Then naming it makes the
  document wrong rather than detailed.

The discriminator is not concreteness. Operation names, parameters, types, schemas and API
contracts are commitments and stay. Storage formats, library choices, file paths and
framework-specific implementations are mechanism and go.

And the floor under all of it: **minimal is not short.** A document may drop anything not required
to establish what it commits to, and may not drop what is.

## Skills

| Skill                  | For                                                            |
| ---------------------- | -------------------------------------------------------------- |
| `ask`                  | Any question about writing one of these documents — read-only  |
| `init`                 | Project conventions: language, paths, house rules              |
| `writing-discipline`   | The genre-neutral base every writing skill applies             |
| `prepare-brief`        | A ticket or a conversation → a brief a document can come from  |
| `write-design-doc`     | Section by section, each approved before the next              |
| `write-decision-record`| One decision, gated on whether it earns a record               |
| `review-doc`           | Fan-out review, findings ranked by how far the damage travels  |

## Agents

Every agent is read-only — `Read, Grep, Glob`. The tool list is the boundary, not the prompt.

| Agent          | Input → output                              |
| -------------- | ------------------------------------------- |
| `guide`        | a question → an answer with citations       |
| `doc-reviewer` | one review dimension → structured findings  |
| `reader`       | a document and a task → every guess it forced |

`reader` is the one that earns the fan-out. It ignores the rules and simply tries to use the
document, which is the only way to find what the document never said — no textual check can detect
an absence.

## What it does not do

Planning, task decomposition, estimation. This plugin is the theory half: what a document must
state and at what level. Turning an approved document into work is a different practice and
belongs to a different plugin.

## Requires `llm-wiki`

The bundled base is an [llm-wiki](../llm-wiki) — a declared dependency, enabled with this plugin.
It powers answering (`wiki-query`) and maintaining the base (`wiki-ingest`, `wiki-lint`,
`wiki-serve`, `wiki-keeper`).

## The base

58 pages in eight groups, distilled from eleven open sources — Parnas on information hiding, Design
Docs at Google, Oxide's RFD process, Nygard and MADR on decision records, the C4 model, RFC 2119,
Anthropic on context engineering, and two practitioner documents on writing for agent readers.

Grouped by **the question a writer arrives with**, not by source: how high to write and how to stay
there, what to keep and what to drop, which document this is, how to phrase something checkably,
how to record a decision, how to write for a machine reader, how to review, and what goes wrong.

Every rule page carries the **symptom** that reveals its violation in a text. A prescription that
cannot be checked against a piece of writing is commentary, and the charter drops it.

`SCHEMA.md` holds the charter and an honest account of what is still missing.

## Layout

```
spec-driven-guide/
├── agents/
├── skills/
└── knowledge/       # a wiki root — holds SCHEMA.md
```

`knowledge/raw/` is gitignored (copyright); `knowledge/wiki/` is committed.
