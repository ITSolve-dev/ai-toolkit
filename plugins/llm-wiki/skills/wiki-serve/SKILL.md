---
name: wiki-serve
description: >-
  Use to preview a wiki in the browser locally — render the compiled wiki/ markdown so the
  user can read the docs and follow [[wikilinks]]. Trigger on "serve the wiki", "open the wiki
  in a browser", "preview the docs".
allowed-tools: Bash(uv run *)
---

# wiki-serve

Serve the compiled `wiki/` markdown with **MkDocs Material**, in two steps.

## 1. Ensure the config exists (once per wiki)

If the wiki has no `mkdocs.yml`, create it from the template with `site_name` filled in: read
`${CLAUDE_PLUGIN_ROOT}/assets/mkdocs.yml.template`, set `site_name` to the wiki's name, and
write the result to `<wiki-root>/mkdocs.yml` (an owned file — the write is auto-approved).

`docs_dir: wiki` already points it at the compiled pages, and the template wires up
`[[wikilinks]]` rendering.

## 2. Serve

Dependencies are fetched on demand by `uv` (nothing installed globally):

```bash
uv run --no-project --with mkdocs-material --with mkdocs-roamlinks-plugin \
  mkdocs serve -f <wiki-root>/mkdocs.yml -a localhost:8000
# -> http://localhost:8000
```

## Notes

- Read-only preview; it never modifies the wiki content.
- `wiki/index.md` is the site's home page and is generated — regenerate it before serving if
  the wiki has changed since the last run.
- `mkdocs.yml` is committed with the wiki (it is config); `mkdocs serve` builds nothing on
  disk, so there is no `site/` artifact to track.
