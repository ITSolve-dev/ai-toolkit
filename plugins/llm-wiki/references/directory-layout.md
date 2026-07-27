# Directory layout

The concrete shape of one wiki. `SCHEMA.md` at the root is both the charter and the marker
that resolution keys on (see [wiki-resolution.md](wiki-resolution.md)).

```
<wiki-root>/
├── SCHEMA.md          # charter + ingestion lens + root marker (human-directed, co-evolved)
├── log.md             # append-only operation log
├── .gitignore         # ignores the generated index + manifest (from assets/gitignore.template)
├── .manifest.json     # GENERATED from raw/ frontmatter — per-source sha + origin (provenance + dedup)
├── raw/               # immutable, normalized sources (one file per source)
│   └── <source_kind>-<slug>.md   # produced by a read-* adapter, per the adapter contract
└── wiki/
    ├── index.md       # GENERATED catalog by group — never hand-edited, gitignored
    ├── overview.md    # entry point: what this wiki covers and how it is organized
    ├── synthesis.md   # the evolving thesis — what it all means (optional)
    └── <group>/       # one subdirectory per page group — groups are NOT predefined; they
        └── <slug>.md  #   emerge as the keeper ingests. frontmatter `category` == folder name
```

## Rules

- **`raw/` is immutable.** Adapters write it; ingest reads it. Never edit a raw file to
  "fix" content — re-run the adapter. Its files are the factual source of truth.
- **Pages are grouped into subdirectories, one per group.** A page lives at
  `wiki/<group>/<slug>.md`; its `category` frontmatter equals the folder name. **The set of
  groups is not predefined** — any subdirectory of `wiki/` is a group, discovered at runtime.
  The keeper creates whatever groups the domain needs as the wiki grows, keeping `SCHEMA.md`'s
  grouping principle current (see [page-conventions.md](page-conventions.md)).
- **The slug is the identity.** It is unique across all groups, so `[[wikilinks]]` resolve by
  slug regardless of which group a page lives in.
- **`index.md` is derived, not authored.** Regenerated from page frontmatter by
  [`build_index.py`](../skills/wiki-lint/scripts/build_index.py), which discovers the groups
  from the filesystem. Gitignored so it can't drift.
- **`log.md` is append-only and lives at the wiki root.** One line per operation,
  `## [YYYY-MM-DD] <op> | <description>`. It records what the keeper did — operational
  bookkeeping rather than curated knowledge — so it sits beside the charter. `index.md` stays
  inside `wiki/`, where it serves as the catalog and the site's home page.
- **`.manifest.json` is derived, not authored.** Regenerated from `raw/` frontmatter by
  [`build_manifest.py`](../skills/wiki-lint/scripts/build_manifest.py) (Stop hook, like the
  index), keyed by raw slug. It records each source's content hash and origin, so any page can
  be traced to its source, `wiki-scout` can dedup candidates against sources already held, and
  lint can check a source for change by re-running its adapter and comparing the fresh hash to
  the recorded one. Gitignored so it can't drift from `raw/`.
- **`SCHEMA.md` is the only per-wiki config.** It also states this wiki's grouping principle —
  not an enumerated group list; the folder tree and generated index are that.
- **Synthesized query answers are first-class pages.** When `wiki-query` files a valuable
  answer back (a comparison, analysis, or discovered connection), it becomes an ordinary page
  in whichever group fits — indexed, linked, and lint-checked like any other. That is how a
  query result stops disappearing into chat history and gets reused.

## What lives where (summary)

| Concern | Location |
|---------|----------|
| Charter / scope / extraction schema / grouping principle | `SCHEMA.md` |
| Raw normalized sources | `raw/<source_kind>-<slug>.md` |
| Curated knowledge | `wiki/<group>/<slug>.md` |
| Entry point / evolving thesis | `wiki/overview.md` / `wiki/synthesis.md` |
| Catalog (generated) | `wiki/index.md` |
| History | `log.md` (wiki root) |
| Source bookkeeping (generated) | `.manifest.json` |
