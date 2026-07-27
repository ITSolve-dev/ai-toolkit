---
name: read-docx
description: >-
  Adapter: convert a Word .docx file into a normalized raw/ source file for an llm-wiki.
  Preserves headings and tables. Faithful extraction only — no relevance filtering (that is
  wiki-ingest's job). Uses Pandoc (default, best fidelity) or Mammoth (--mammoth, pure-Python
  fallback). Trigger when a .docx is a source to add to the wiki.
allowed-tools: Bash(uv run *)
---

# read-docx

An adapter. Turns one `.docx` into `raw/<slug>.md` per the
[adapter contract](../../references/adapter-contract.md).

## Backends

- **Pandoc** (default) — best headings/tables fidelity. External binary (install separately:
  `winget install JohnMacFarlane.Pandoc` / `brew install pandoc` / `apt install pandoc`).
- **Mammoth** (`--mammoth`) — pure-Python fallback (no binary), weaker markdown.

## Run

```bash
# Pandoc (requires the pandoc binary on PATH)
uv run --no-project "${CLAUDE_PLUGIN_ROOT}/skills/read-docx/scripts/extract.py" \
  <source.docx> --raw-dir <wiki-root>/raw [--slug NAME]

# Mammoth fallback (installs on demand)
uv run --no-project --with mammoth \
  "${CLAUDE_PLUGIN_ROOT}/skills/read-docx/scripts/extract.py" \
  <source.docx> --raw-dir <wiki-root>/raw --mammoth
```

## Notes

- Pandoc extracts embedded images to `<raw-dir>/<slug>-media/` and rewrites references.
- Faithful extraction only: the adapter does not decide what matters for the wiki.
