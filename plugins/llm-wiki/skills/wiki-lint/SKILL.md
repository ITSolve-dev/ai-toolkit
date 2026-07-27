---
name: wiki-lint
description: >-
  Use to health-check an llm-wiki — find contradictions, stale claims, orphan pages, broken
  links, and coverage gaps. Two tiers: deterministic mechanical checks (a script, also run
  automatically by the plugin's Stop hook) and deep semantic checks (LLM judgment, on demand).
  Trigger on "lint the wiki", "check the wiki's health", "find problems in the wiki", or run
  periodically after a batch of ingests.
allowed-tools: Bash(uv run *)
---

# wiki-lint

Karpathy's lint: a periodic health check for what rots as a wiki grows — contradictions
between pages, claims gone stale, orphan pages, concepts mentioned but lacking a page, missing
cross-references, and coverage gaps. Two tiers with a clear authority boundary.

## Two tiers

1. **Mechanical (deterministic).** What a machine can decide for certain — missing/invalid
   frontmatter, broken `[[links]]`, orphan pages, and index regeneration. Run the scripts:

   ```bash
   uv run --no-project "${CLAUDE_PLUGIN_ROOT}/skills/wiki-lint/scripts/build_index.py" <wiki-root>
   uv run --no-project "${CLAUDE_PLUGIN_ROOT}/skills/wiki-lint/scripts/lint_mechanical.py" <wiki-root>
   ```

   This tier also runs **automatically** via the plugin's [Stop hook](../../hooks/hooks.json)
   at the end of each turn, so mechanical drift is caught without asking.

2. **Semantic (LLM judgment, report-only).** What needs reading and reasoning —
   contradictions between pages, claims gone stale (the source behind a page changed — re-run its
   adapter and compare the fresh hash against the one in `.manifest.json`), coverage gaps, and
   concepts mentioned often but lacking a page. Report
   these for the user to resolve; don't silently "fix" a judgment call.

   Lint is also **generative**, per the gist: surface **new questions worth investigating** and
   **new sources worth looking for**. Where a coverage gap could be filled from the web, name it
   — and hand it to `wiki-scout` (its charter-driven fan-out is exactly this, turned into
   approvable source candidates). Sourcing stays the human's call; lint proposes, it does not
   fetch.

Full procedure: [`lint-workflow.md`](lint-workflow.md).

## After linting

Append a line to `log.md` at the wiki root:
`## [YYYY-MM-DD] lint | <N> issues found, <M> auto-fixed, <K> flagged`.
