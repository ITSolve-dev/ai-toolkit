# ITSolve-dev AI Toolkit

Shared, **tool-agnostic** AI toolkit for the **ITSolve-dev** organization — reusable skills,
agents and plugins meant to be installed and reused across projects.

This repository is a **Claude Code plugin marketplace**: one repo, many plugins under
`plugins/`, each installable independently.

## Plugins

| Plugin | Version | What it does |
|--------|---------|--------------|
| [`llm-wiki`](plugins/llm-wiki) | 0.1.0 | LLM-maintained knowledge wiki (Karpathy pattern): ingest → compile → query → lint, local serve, multi-source adapters (book/html/docx). Ships the `wiki-keeper` expert agent. |
| [`domain-driven-guide`](plugins/domain-driven-guide) | 0.1.0 | Ask DDD questions against a bundled, curated knowledge base — answers with citations via the read-only `guide` agent, plus design skills. Built on `llm-wiki`. |
| [`spec-driven-guide`](plugins/spec-driven-guide) | 0.1.0 | Write design docs, decision records and agent instructions that keep their obligations and shed the mechanism. Bundled base with citations, section-by-section authoring, fan-out review. Built on `llm-wiki`. |

## Install

```
/plugin marketplace add ITSolve-dev/ai-toolkit
/plugin install <plugin>@ai-toolkit
```

A plugin that depends on another pulls it in: installing `domain-driven-guide` enables
`llm-wiki` with it.

## Layout

```
ai-toolkit/
├── .claude-plugin/marketplace.json   # marketplace manifest (lists all plugins)
└── plugins/
    └── <plugin>/                      # a self-contained plugin
```

## Releases

Each plugin is versioned and tagged independently as `<plugin>--v<version>`, which publishes a
GitHub release. Bump the version in both `plugin.json` and the marketplace entry, then:

```
claude plugin tag plugins/<plugin> --push
```

It refuses to tag if those two versions disagree.
