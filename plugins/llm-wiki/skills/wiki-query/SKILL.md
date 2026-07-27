---
name: wiki-query
description: >-
  Use to answer a question against an llm-wiki built with this plugin. Locates relevant pages,
  synthesizes an answer WITH citations to those pages, and — when the answer is a valuable new
  synthesis — files it back as a page so it is reused, not re-derived. Lightweight and
  read-mostly: run inline; you do not need to dispatch the wiki-keeper agent for it. Trigger
  when a question should be answered from the wiki rather than from general knowledge.
allowed-tools: Read, Grep, Write, Edit, Bash(uv run *)
---

# wiki-query

Answer from the wiki, with citations. A valuable query result becomes a permanent page instead
of disappearing into chat history.

## The flow

Full procedure: [`query-workflow.md`](query-workflow.md). In short:

1. **Locate** relevant pages — read `index.md` first (the catalog), then search page bodies.
2. **Read** the located pages.
3. **Synthesize** an answer **with citations** to the pages (and, through them, their
   sources). Where the wiki doesn't cover something, say so and suggest a source to ingest; if
   you do draw on outside knowledge, mark it plainly as coming from outside the wiki.
4. **File back** — if the answer is a genuinely new synthesis (a comparison, analysis, or
   discovered connection), write it as an ordinary page in the group that fits it, regenerate
   the index, and log it. Next time it is retrieved, not re-derived.

## Calibrate the answer to the question — decide on the fly

Two judgments belong to you, made per query from the nature of the question, not by habit or by asking:

- **Answer size follows the question.** A simple, factual question deserves a couple of sentences and a
  citation or two — don't inflate it with structure it doesn't need. A hard, analytical question (a
  comparison, a trade-off, a "why", a design call) deserves a full worked treatment: the reasoning, the
  concrete specifics, the failure modes, the cross-links. Read the question and match it.
- **File-back is your own call — act, don't ask.** When a result is a genuinely new synthesis that will
  be asked again, write the page; when it is trivial or already covered, don't (extend the existing page
  rather than make a near-duplicate). Deciding this and doing the mechanical page work is exactly what
  the human delegates, so decide and do it rather than asking permission.

## Retrieval tiers

Use the lightest tier that answers the question:

1. **`index.md`** — the catalog; always read this first to find candidate pages.
2. **ripgrep** — full-text search across `wiki/` (via the Grep tool). The default
   workhorse; no dependencies.
3. **A configured search tool** *(opt-in)* — semantic/hybrid search or graph traversal, for
   when keyword search stops being enough. Use whatever the wiki's `.mcp.json` provides.

## Citations

Every claim in the answer must point to the wiki page it came from (and that page carries its
own source citation). This is what makes answers verifiable — see
[page conventions](../../references/page-conventions.md).
