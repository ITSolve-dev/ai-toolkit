# ITSolve-dev AI Toolkit

Shared, **tool-agnostic** AI toolkit for the **ITSolve-dev** organization — reusable skills,
agents and plugins meant to be installed and reused across projects.

This repository is a **Claude Code plugin marketplace**: one repo, many plugins under
`plugins/`, each installable independently.

## Plugins

| Plugin | Status | What it does |
|--------|--------|--------------|
| [`llm-wiki`](plugins/llm-wiki) | 🚧 skeleton | LLM-maintained knowledge wiki (Karpathy pattern): ingest → compile → query → lint, local serve, multi-source adapters (book/html/docx). Ships the `wiki-keeper` expert agent. |
| [`domain-driven-guide`](plugins/domain-driven-guide) | 🚧 0.1.0 | Ask DDD questions against a bundled, curated knowledge base — answers with citations via the read-only `guide` agent, plus design skills. Built on `llm-wiki`. |

## Install (once published)

```
/plugin marketplace add ITSolve-dev/ai-toolkit
/plugin install llm-wiki@ai-toolkit
```

## Layout

```
ai-toolkit/
├── .claude-plugin/marketplace.json   # marketplace manifest (lists all plugins)
└── plugins/
    └── llm-wiki/                      # a self-contained plugin
```
