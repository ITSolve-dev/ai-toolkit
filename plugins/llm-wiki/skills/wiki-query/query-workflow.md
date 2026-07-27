# Query workflow

The full procedure behind [`SKILL.md`](SKILL.md). Answer a question from the wiki, with
citations, and file valuable answers back for reuse. Based on Karpathy's query operation
([`karpathy-llm-wiki.md`](../../references/karpathy-llm-wiki.md)).

## 0. Orient

- Resolve the wiki root ([wiki-resolution](../../references/wiki-resolution.md)). If the
  current location is not in a wiki, say so.

## 1. Locate relevant pages

Use the lightest retrieval tier that works:

1. Read `wiki/index.md` — the category catalog — to find candidate pages by title/summary.
2. Search page bodies with **ripgrep** (the Grep tool) for terms and `[[slug]]` links.
3. *(opt-in)* If configured, use **qmd** for semantic/hybrid search, or **graphify** to
   traverse relationships. Not required — index + ripgrep is the default.

Follow `[[wikilinks]]` from the pages you find to reach connected pages.

## 2. Read

- Read the located pages in full before answering. Prefer the wiki's own pages over
  re-reading `raw/` (that's what the pages are for), but drop to `raw/` to verify a specific
  cited claim when needed.

## 3. Synthesize with citations

- Compose the answer from what the pages say. **Cite each claim** back to the page it came
  from (and those pages cite their sources — so the chain is answer → page → source).
- **Don't silently fill gaps from general knowledge.** The answer's substance comes from the
  wiki, cited. Where the wiki doesn't cover the question, say so plainly and suggest a source to
  ingest. If outside knowledge is genuinely needed, label it explicitly as coming from outside
  the wiki — never let it pass as a cited wiki claim.
- If pages disagree, surface the disagreement with attribution rather than picking silently.

## 4. File back valuable answers ("crystallize")

If the answer is a genuinely new synthesis — a comparison, an analysis, a discovered
connection — that isn't already a page:

- Write it as `wiki/<group>/<slug>.md` in the group that fits it, frontmatter per
  [page conventions](../../references/page-conventions.md), citing the pages it draws on.
- Cross-link it with `[[slug]]` to the pages it relates.
- Regenerate the index with [`build_index.py`](../wiki-lint/scripts/build_index.py).
- Append `## [YYYY-MM-DD] query | filed back: [[<slug>]]` to `log.md` at the wiki root.

Don't file back trivial lookups — only answers whose reasoning is worth keeping. Next time the
question comes up, retrieval (step 1) finds that page and the answer is reused.

## Note

Query is read-mostly and lightweight — run it inline in whatever context asked the question
(main session or a domain-expert agent). It does not need the `wiki-keeper` agent.
