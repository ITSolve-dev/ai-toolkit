---
name: wiki-init
description: >-
  Use to bootstrap a new llm-wiki for a domain — the quick-start step. Scaffolds the
  directory layout (SCHEMA.md, raw/, wiki/) from the plugin's templates, then interviews the
  user about the domain and fills in the SCHEMA.md charter so ingestion has a lens to work
  with.
  Trigger on "start a new wiki", "set up an llm-wiki here", "initialize a knowledge base".
allowed-tools: Bash(uv *)
---

# wiki-init

Bootstrap a new wiki. Not part of Karpathy's gist (which is abstract about setup) but the
practical quick-start every implementation adds. After this runs, `wiki-ingest`,
`wiki-query` and `wiki-lint` have a wiki to operate on.

## Precondition — uv must be available

The scaffold script, the plugin's per-turn hooks, and the `read-*` adapters all run through
[`uv`](https://docs.astral.sh/uv/). Before scaffolding, check it is present:

```bash
uv --version
```

If it is missing, tell the user uv is required and **ask whether to install it** — it is a single
standalone binary that needs no `pip` and no preexisting Python (uv provisions its own). On their
consent, run the official installer for their OS:

- **Windows:** `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
- **macOS / Linux:** `curl -LsSf https://astral.sh/uv/install.sh | sh`

If the user declines, stop: without uv the wiki can't be scaffolded and the hooks and adapters
stay inert. Don't install it silently.

## Steps

1. **Pick the target directory.** Default to the current project, and say where you are
   creating it; ask only if the location is genuinely ambiguous.
   **Never** initialize at a home or drive root (see
   [`wiki-resolution.md`](../../references/wiki-resolution.md)) — refuse and ask for a
   subdirectory instead.
2. **Refuse to clobber.** If a `SCHEMA.md` already exists there, stop — the directory is
   already a wiki root.
3. **Scaffold** by running the bundled script, which stamps the templates from
   [`assets/`](../../assets) and creates the layout in
   [`directory-layout.md`](../../references/directory-layout.md):

   ```bash
   uv run --no-project "${CLAUDE_PLUGIN_ROOT}/skills/wiki-init/scripts/init_wiki.py" <target-dir>
   ```

   It stamps the layout and prints what it created, leaving any existing file untouched.
   Page groups are not scaffolded — they emerge as the keeper ingests.
4. **Interview the user, then fill the charter.** `SCHEMA.md` is what makes the wiki
   disciplined for its domain, and every later ingest and query keys off it — so gather it
   from the user rather than guessing. **If the request already named the domain** (e.g. "set up
   a DDD wiki"), treat that as a seed: pre-fill every section it already answers and ask only
   about what it leaves open. Otherwise ask roughly in this order and write each answer into
   its section:

   1. **Domain & purpose** — what is this wiki about, and what work or decisions will it
      support? → *Purpose*
   2. **Audience** — who or what reads it: you, a team, a downstream agent? → *Purpose*
   3. **The lens** — what kinds of claims and artifacts are in scope, and what should be
      deliberately dropped as noise? Push for concrete examples of both. → *Scope*
   4. **Extraction targets** — what should each source yield: definitions, decision rules,
      trade-offs, failure modes, data? → *Domain extraction schema*
   5. **Key sources** — which authoritative sources will you feed it first? → *Notes*
   6. **Grouping instinct** — how would you split this domain into topics? This is what keeps
      group names domain-specific from day one. → *Grouping principle*
   7. **Workflow preferences** — any per-wiki rules (always write a source summary, lint
      cadence)? Skip if none. → *Workflow customizations*
   8. **Languages** — which language should the wiki's pages be written in (recommend English —
      widest sources, cleanest cross-links), and which language should I converse in (defaults to
      the language they're using)? → *Languages*

   Run it as a short conversation, not a form — follow up where an answer stays vague, and
   don't leave placeholders behind. If you are running delegated with nobody to ask, infer
   conservatively from the sources at hand and flag which sections need confirmation.
5. **Log it.** Append `## [YYYY-MM-DD] schema | initialized wiki` to `log.md` at the wiki root.

## Notes

- The wiki lives in the user's project, not in the plugin — resolution finds it by the
  `SCHEMA.md` marker.
- Heavy ongoing work (ingest, lint) belongs to [`wiki-keeper`](../../agents/wiki-keeper.md);
  init is a one-shot, lightweight setup.
