# ITSolve-dev AI Toolkit

Shared, **tool-agnostic** AI toolkit for the **ITSolve-dev** organization — reusable skills,
agents and plugins meant to be installed and reused across projects.

Each plugin under `plugins/` follows the [Agent Plugins](https://agent-plugins.org/) standard
for its manifest and directory layout. Support for hooks, subagents and dependency installation
varies by client.

## Plugins

| Plugin | Version | What it does |
|--------|---------|--------------|
| [`llm-wiki`](plugins/llm-wiki) | 0.1.2 | LLM-maintained knowledge wiki (Karpathy pattern): ingest → compile → query → lint, local serve, multi-source adapters (book/html/docx). Ships the `wiki-keeper` expert agent. |
| [`domain-driven-guide`](plugins/domain-driven-guide) | 0.1.2 | Ask DDD questions against a bundled, curated knowledge base — answers with citations via the read-only `guide` agent, plus design skills. Built on `llm-wiki`. |
| [`spec-driven-guide`](plugins/spec-driven-guide) | 0.1.3 | Write design docs, decision records and agent instructions that keep their obligations and shed the mechanism. Bundled base with citations, section-by-section authoring, fan-out review. Built on `llm-wiki`. |
| [`anti-sycophancy`](plugins/anti-sycophancy) | 0.1.1 | Assessments that don't bend toward the asker. `honest-assessment` shapes answers in the current context and attaches to other plugins' agents; `second-opinion` forks a reviewer into a context that never helped build the idea. |
| [`spartan`](plugins/spartan) | 0.1.0 | Short answers in any language: the conclusion first, then only what the reader needs to act. Cuts content, not grammar, so it works in Russian as well as English. Levels `lite`, `full`, `ultra`. |

## Install

**Claude Code** — run these commands in a session:

```text
/plugin marketplace add ITSolve-dev/ai-toolkit
/plugin install spartan@ai-toolkit
```

**Codex** — run these commands in a terminal:

```sh
codex plugin marketplace add ITSolve-dev/ai-toolkit
codex plugin add spartan@ai-toolkit
```

Replace `spartan` with any plugin name from the table. In other compatible clients, use the
client's standard plugin installation flow.

**OpenCode v2** — install one plugin or the entire toolkit from Git:

```sh
# One plugin (replace spartan with a plugin name from the table)
opencode plugin add 'github:ITSolve-dev/ai-toolkit#main::path:plugins/spartan'

# Entire toolkit
opencode plugin add 'github:ITSolve-dev/ai-toolkit#main'
```

Use `opencode plugin list` to see installed packages and mention `@spartan` in a prompt to
load the skill. The two `ask` skills have distinct IDs: `@domain-driven-guide-ask` and
`@spec-driven-guide-ask`.

OpenCode packages register the existing skills and include their supporting files. They
do not register Claude Code hooks, slash commands or subagents, or install dependencies
declared by another client's marketplace. Workflows depending on those features may not
behave the same way in OpenCode.

## Layout

```text
ai-toolkit/
├── .agents/plugins/marketplace.json  # Codex catalog
├── .claude-plugin/marketplace.json   # Claude Code catalog
└── plugins/<plugin>/
    ├── plugin.json                  # portable manifest
    └── skills/<skill>/SKILL.md      # skill instructions
```

## Releases

Each plugin is versioned independently. Update its version in the portable manifest and the
Claude Code marketplace entry and the plugin's OpenCode `package.json`. After the change
lands, tag the merged commit and push the tag
to publish the GitHub release. For example, for Spartan version 0.1.0:

```sh
git tag -a spartan--v0.1.0 <merge-commit> -m "spartan v0.1.0"
git push origin refs/tags/spartan--v0.1.0
```
