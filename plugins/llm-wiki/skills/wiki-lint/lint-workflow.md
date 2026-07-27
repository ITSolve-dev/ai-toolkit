# Lint workflow

The full procedure behind [`SKILL.md`](SKILL.md). A two-tier health check with a clear
authority boundary: the machine auto-fixes only what is certain; the LLM reports judgment
calls. Based on Karpathy's lint operation
([`karpathy-llm-wiki.md`](../../references/karpathy-llm-wiki.md)).

## 0. Orient

- Resolve the wiki root ([wiki-resolution](../../references/wiki-resolution.md)) and read
  `SCHEMA.md`.

## Tier 1 — mechanical (deterministic)

Run the scripts; these decisions are certain, so they may be applied directly:

- [`build_index.py`](scripts/build_index.py) — regenerate `wiki/index.md` from frontmatter
  (fixes any index drift).
- [`lint_mechanical.py`](scripts/lint_mechanical.py) — report:
  - pages missing required frontmatter fields, or with an invalid `category`;
  - broken `[[links]]` (target page does not exist);
  - orphan pages (no inbound `[[link]]`).

Fix the mechanical findings: repair or remove broken links, add the missing inbound link (or
delete a truly orphaned page), complete missing frontmatter. Re-run to confirm clean.

This tier also runs automatically via the [Stop hook](../../hooks/hooks.json) — so most
mechanical drift is already caught between sessions.

## Tier 2 — semantic (LLM judgment, report-only)

These need reading and reasoning; **report them, do not silently rewrite**:

- **Contradictions** — two pages asserting incompatible claims. Surface both with attribution.
- **Stale claims** — a page whose original source has changed (re-run its adapter and compare the
  fresh `sha256` against the one in `.manifest.json`) or whose `updated` date is old relative to
  newer, conflicting information. Flag for re-ingest.
- **Coverage gaps** — concepts referenced across many pages that have no page of their own
  (frequently-mentioned-but-undefined), or areas the `SCHEMA.md` scope says should exist but
  don't.
- **Weak cross-linking** — pages that should reference each other but don't.
- **New questions & sources (generative)** — the gist's lint also looks forward: name questions
  worth investigating next, and sources worth adding. Where a coverage gap could be filled from
  the web, hand it to `wiki-scout` (charter-driven fan-out → approvable candidates). Lint
  proposes; it does not fetch, and sourcing stays the human's call.

Present Tier 2 findings as a list for the user (or the wiki-keeper's return summary) to act
on — typically by scheduling a re-ingest, a merge/split, or a scout for the gaps found.

## Log

Append one line to `log.md` at the wiki root:
`## [YYYY-MM-DD] lint | <N> issues found, <M> auto-fixed, <K> flagged`.
