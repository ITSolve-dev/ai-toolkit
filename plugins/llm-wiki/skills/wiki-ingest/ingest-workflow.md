# Ingest workflow

The full procedure behind [`SKILL.md`](SKILL.md). Ingestion is **context-aware distillation**:
extract the maximum useful signal *for this wiki's charter*, structure it, and weave it into
the existing wiki. Based on Karpathy's llm-wiki flow
([`karpathy-llm-wiki.md`](../../references/karpathy-llm-wiki.md)).

## 0. Orient

- Resolve the wiki root and read `SCHEMA.md`
  ([wiki-resolution](../../references/wiki-resolution.md)). The charter's **Scope** and
  **Domain extraction schema** are your lens for every keep/drop decision.
- Confirm the source is normalized in `raw/<slug>.md` per the
  [adapter contract](../../references/adapter-contract.md). If not, run an adapter first.

## 1. Read the source and the map

- Read `raw/<slug>.md` fully, using its `structure` map (chapters / sections / timestamps)
  to navigate. **A large source — its `structure` map lists many chapters, or it runs to tens of
  thousands of words — is NOT distilled inline: the main agent hands it to the
  `ingest-large-source` workflow (see [`SKILL.md`](SKILL.md)), which fans out per chapter.**
- Read `wiki/index.md` to see what already exists, so you **update rather than duplicate**.

## 2. Gate the source, then distill against the lens

Distillation is coarse-to-fine: first judge whether the source belongs here at all, then mine
what does.

**First, the whole source (the relevance gate).** Before extracting anything, weigh the
source's *subject* against the charter's **Purpose** and **Scope**. Three outcomes:

- **In scope** — proceed to distill.
- **Partly in scope** — ingest only the part that fits; state in your summary what you set
  aside and why. (A DDD wiki taking the domain-modelling half of a general architecture talk
  and dropping its Kubernetes half.)
- **Out of scope** — do **not** ingest. This **ends the workflow for that source**: the
  summary page, page updates, provenance and index steps below do not run. Do only two things —
  append the reject line to `log.md` (`## [YYYY-MM-DD] reject | <source> — <one-line reason vs.
  charter>`) and report the verdict so the human can retune Scope or point you elsewhere. `raw/`
  keeps the faithful extraction; nothing enters the wiki, and the index is untouched.

This gate is about the source's subject, not individual facts — the per-claim keep/drop below
still runs on whatever passes.

**Then, per claim (distill).**

- Keep only what the charter's Scope marks in-scope; drop the rest.
- Extract the kinds of knowledge the Domain extraction schema names (e.g. frameworks,
  decision rules, trade-offs, definitions) — not a generic summary of the document.
- Note everything the source meaningfully touches; those become page edits, each in the group
  that fits it (groups are the wiki's own — see [page conventions](../../references/page-conventions.md)).
- **Capture substance.** For each thing you keep, take its reasoning and its concrete
  specifics with it — numbers, mechanisms, worked examples, trade-offs, limits — plus the
  verbatim quotes worth preserving. Distillation makes the material shorter and denser, not
  vaguer.

**Reader discussion, where the source has it.** A source may carry comments or a forum thread
(the adapter script does not fetch these — check the live page and read it if it has one worth
reading; see [read-html](../read-html)). The knowledge there is real — corrections,
counter-examples, field experience — so mine it like any content, but under a **stricter bar**:
a commenter is not the author. Keep a claim from discussion only when it is corroborated,
soundly reasoned, or clearly from someone who knows; drop opinion, guesses, and the unverifiable.
When you keep one, attribute it to the discussion (not the author) in the citation, so the page
records who actually said it.

## 3. Surface takeaways

Direction reaches you in one of three ways; take whichever applies.

- **Inline / foreground:** say what you found and invite the user to steer emphasis before you
  write (Karpathy's preferred human-in-the-loop). If they don't steer, proceed on your own
  charter-based judgment and flag the calls you made.
- **In the task you were given:** explicit steering in the prompt that dispatched you is
  first-class direction — weigh it alongside `SCHEMA.md`.
- **From the charter alone:** follow the emphasis encoded in `SCHEMA.md`, and collect takeaways
  for your return summary.

## 4. Write the source summary page

- Create `wiki/<group>/<slug>.md` summarizing this source: what it is, its thesis, the points
  relevant to this wiki, and how to read it — what it is authoritative on and where it is weak
  or dated. Place it in the group it most informs. Frontmatter per
  [page conventions](../../references/page-conventions.md); `category` equals the folder name.

## 5. Update the pages the source touches across the wiki

- For everything the source touches, create or edit its page. **Choose each page's group by the
  grouping principle in `SCHEMA.md`** — groups are named by the domain's own topics (a
  reader-navigable tree), not generic page-type words like `concepts/`. If a page belongs to a
  topic no existing group covers, create a new group (subdirectory), and — since the tree is
  self-documenting — just keep `SCHEMA.md`'s stated principle current. Integrate new
  information with what's already there; when the source disagrees with an existing page, note
  the disagreement with attribution rather than silently overwriting.
- A rich source may cascade into many pages (Karpathy cites 10-15); do that cross-reference
  bookkeeping thoroughly when it does. Let the source's signal against the charter set the
  count.

## 6. Cross-link and cite

- Link liberally with `[[slug]]` in page bodies; every new page needs at least one inbound
  link (or lint flags it as an orphan).
- Cite claims back to the source: the source slug in `sources:`, and a pinned location where
  practical (e.g. a line range `L120-L138` in the raw file, or a chapter).

## 7. File a new connection (when warranted)

- If ingesting surfaces a comparison or connection worth keeping, write it as an ordinary page
  of whatever kind fits, in the group that fits it. (This is the same mechanism `wiki-query`
  uses to file answers back — connections are as valuable as the documents.)

## 8. Revisit the top-level pages

- Update `wiki/overview.md` if a new group appeared or the wiki's shape changed.
- Ask whether this source strengthens or challenges the thesis in `wiki/synthesis.md`, and
  revise it where it does — that is what keeps the synthesis reflecting everything read.

## 9. Provenance — nothing to do by hand

- `.manifest.json` (source `sha256` + `origin`, for provenance — tracing and dedup) is **derived**
  from the `raw/` frontmatter the adapter already wrote, by
  [`build_manifest.py`](../wiki-lint/scripts/build_manifest.py) — regenerated by the Stop hook
  each turn, like the index. Do not hand-edit it. Just make sure the source is in `raw/` with
  its provenance frontmatter (it is, if an adapter produced it); the manifest follows.

## 10. Regenerate the index

- Run [`build_index.py`](../wiki-lint/scripts/build_index.py) so `wiki/index.md` reflects the
  new/updated pages. Never hand-edit the index.

## 11. Log

- Append one line to `log.md` at the wiki root:
  `## [YYYY-MM-DD] ingest | <source title — sections covered>`.
- Ingesting several sources: run this whole flow per source and **log each as you finish it**,
  not in one batch at the end — so an interrupted run still records what it completed.

## Guardrails

- Treat `raw/` as immutable — the faithful record of what the source said. Never hand-edit it; if
  the extraction is defective, re-run the adapter. If it still can't produce a clean file, don't
  patch `raw/` — note the defect as an extraction caveat on the source's page and transcribe the
  affected passage there (per [page conventions](../../references/page-conventions.md)), so
  provenance stays honest.
- Keep pages atomic; prefer merging into an existing page over creating a near-duplicate.
- Images: read the extracted text first, then view locally-downloaded images separately.
