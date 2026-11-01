# task-master

Board management and planning as an expert the working agent calls. It hands the plugin a problem
and its context; the plugin works in its own context, grounded in a curated knowledge base, and
returns a result. What to do with that result stays the caller's decision.

Status: in development, not released. Design: [`docs/specs/2026-08-24-task-master-design.md`](../../docs/specs/2026-08-24-task-master-design.md).

## Layout

```
task-master/
└── knowledge/
```

`knowledge/` is a wiki root in its own right — it holds `SCHEMA.md`, so the `llm-wiki` skills
operate on it directly.
