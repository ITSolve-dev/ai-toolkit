---
name: wiki-scout
description: >-
  Use to find candidate sources on the internet for an llm-wiki, driven by its SCHEMA.md
  charter rather than a blind search. Fans out parallel searcher agents (a bundled workflow) —
  one per coverage gap, each searching in its own context — and returns a ranked, deduplicated
  candidate list for the human to approve. It never ingests. Trigger on "find sources for the
  wiki", "what should I add to the wiki", "scout for material on X", "suggest sources",
  "gather sources".
allowed-tools: Read, Grep, Glob, Workflow
---

# wiki-scout

Curating sources is the human's call in Karpathy's pattern — the LLM does the grunt work of
maintenance. This skill assists that curation: it **proposes candidates for approval; it never
ingests.** After `wiki-init` the agent holds the charter, so it can propose sharper material than
a cold search.

Gathering sources floods a single context — every fetched page competes with the reasoning.
So scouting runs as a **fan-out workflow**: one searcher agent per coverage gap, each searching
and fetching in its **own** context and returning only a compact result. The bulky page content
never reaches the caller; only the ranked candidate list does.

## Run

1. **Resolve the wiki root** — the nearest ancestor directory containing `SCHEMA.md`
   ([wiki-resolution](../../references/wiki-resolution.md)). Never scout from a home/drive root.
2. **Invoke the bundled workflow** by name, passing the wiki root (and an optional focus topic):

   ```
   Workflow({
     name: "llm-wiki:scout",
     args: { wikiRoot: "<abs path to the wiki root>", focus: "<optional topic, else omit>" }
   })
   ```

   (A bundled workflow, registered by name once the plugin is loaded. Pass the wiki root; the
   workflow re-discovers it on its own if the runtime drops the args.)

   The workflow reads the charter and index, names the coverage gaps, dispatches one searcher
   per gap in parallel, judges each candidate's fit against Purpose/Scope (the same lens the
   ingest relevance gate uses), dedups against sources already in the wiki, and returns a ranked
   candidate list.
3. **Present the candidates for approval** (format below). The human picks.
4. **On approval only:** ingest each accepted source the same way as any new source — normalize
   it with its `read-*` adapter, then `wiki-ingest`. A **large** source (a book, or a multi-page
   work gathered into one big raw file) is handed to the `ingest-large-source` workflow by the
   main agent, not delegated to `wiki-keeper` — a keeper subagent cannot launch a workflow.
   Rejected candidates are dropped; scouting itself ingested nothing.

## Candidate list format

Show the returned `candidates`, best-first, one scannable line each — the human decides go/no-go
per line, not by reading prose:

```
- <title> — <url>
  kind: <book|web-page|paper|talk|…>   fit: <in|partial>   fills: <gap>
  why: <one line on authority / fit>    caveat: <paywall|dated|weak|none>
```

Also surface the count the workflow **dropped as off-charter**, so the human sees the gate worked
and can widen Scope if it was too strict.

## Guardrails

- **Propose, never ingest.** The workflow has no write tools; ingestion is a separate,
  human-approved step.
- **Charter-driven, not volume-driven.** A short list that closes real gaps beats a long list
  that pads coverage. If a gap has no good source, say so rather than proposing a weak one.
- **Sourcing stays the human's call.** Surface each candidate's trade-offs (authority, recency,
  bias) and let the human choose the wiki's reading list.
