# domain-driven-guide

Ask Domain-Driven Design questions and get answers **from a curated knowledge base**, with
citations — not from a model's memory.

## Use it

```
/domain-driven-guide:ask what is an anticorruption layer, and when do I need one
/domain-driven-guide:ask is my Order class a correct aggregate root?
```

## Skills

| Skill                              | For                                                         |
| ---------------------------------- | ----------------------------------------------------------- |
| `ask`                              | Any DDD question — the read-only entry point                |
| `discover-bounded-contexts`        | Where to split a system; subdomains; the context map        |
| `design-aggregates`                | Consistency boundaries, roots, invariants, references by id |
| `model-entities-and-value-objects` | Entity or value object, identity, immutability, validation  |
| `review-domain-model`              | Auditing existing code against DDD                          |

## Agents

Every agent is read-only — `Read, Grep, Glob`. The tool list is the boundary, not the prompt.

| Agent             | Input → output                                       |
| ----------------- | ---------------------------------------------------- |
| `guide`           | a question → an answer with citations                |
| `domain-modeler`  | a design task → a decision, its rationale, a diagram |
| `model-inspector` | one review dimension → structured findings           |

The design skills dispatch these, so the codebase reading happens in their contexts and only
the result reaches yours. `review-domain-model` fans out one inspector per dimension in
parallel.

**If an agent cannot reach the base, it stops and says so** rather than answering from general
knowledge. An ungrounded answer reads exactly like a grounded one, so the refusal is the point.
Outside Windows the first read of the base may ask for permission once — the base lives in the
plugin directory, which is outside your project.

## Requires `llm-wiki`

The bundled base is an [llm-wiki](../llm-wiki), so the `llm-wiki` plugin is a declared
dependency and gets enabled with this one. It powers both halves: answering, via `wiki-query`,
and maintaining the base, via `wiki-ingest`, `wiki-lint`, `wiki-serve` and `wiki-keeper`.

## Layout

```
domain-driven-guide/
├── agents/
├── skills/
└── knowledge/
```

`knowledge/` is a wiki root in its own right — it holds `SCHEMA.md`, so the `llm-wiki` skills
operate on it directly.
