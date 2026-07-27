export const meta = {
  name: 'ingest-large-source',
  description: 'Distill a large raw source (a book, or a multi-page web work already gathered into one raw file) into wiki pages via chapter-parallel map-reduce. No single agent reads the whole source, and the parallel distillers never write to the wiki, so they cannot collide on shared pages; one final writer commits everything.',
  phases: [
    { title: 'Resolve', detail: 'find the wiki root and the target raw source (args are an optional hint)' },
    { title: 'Split', detail: 'locate chapter/section line-ranges from the raw source structure map' },
    { title: 'Distill', detail: 'one agent per chunk reads only its range and returns proposed pages (no wiki writes)' },
    { title: 'Merge', detail: 'a single writer dedups the proposals, commits pages, and updates overview/synthesis/log once' },
  ],
}

// --- inputs -----------------------------------------------------------------
// args (wikiRoot, rawSlug) are only a HINT: the runtime can drop workflow args
// (claude-code#63876), so the Resolve phase re-discovers them when missing. That
// makes the workflow robust however it is invoked (by name or by scriptPath).
const asStr = (v) => (typeof v === 'string' ? v.trim() : '')
let A = args
if (typeof A === 'string') { try { A = JSON.parse(A) } catch (e) { A = {} } }
A = A && typeof A === 'object' ? A : {}
let wikiRoot = asStr(A.wikiRoot)
let rawSlug = asStr(A.rawSlug)

const RESOLVE_SCHEMA = {
  type: 'object',
  required: ['wikiRoot', 'rawSlug'],
  properties: { wikiRoot: { type: 'string' }, rawSlug: { type: 'string' } },
}

if (!wikiRoot || !rawSlug) {
  phase('Resolve')
  const res = await agent(
    'Resolve the target for a large-source ingest.\n' +
    '1. Find the WIKI ROOT: a directory containing `SCHEMA.md`. Search the current working directory and its subdirectories (Glob `**/SCHEMA.md`) and pick the shallowest match. Never a home or filesystem root.\n' +
    '2. In `<wikiRoot>/raw/`, find the source NOT yet ingested: its slug does NOT appear in any wiki page\'s `sources:` frontmatter (Grep `wiki/` for the bare slug). Among not-yet-ingested sources, pick the LARGEST by line count. Ignore any whose log.md shows it was rejected as off-charter.\n' +
    (rawSlug ? ('Prefer the slug "' + rawSlug + '" if it exists and is not yet ingested.\n') : '') +
    'Return `wikiRoot` (absolute path) and `rawSlug` (filename stem, no .md).',
    { schema: RESOLVE_SCHEMA, label: 'resolve', phase: 'Resolve' }
  )
  wikiRoot = wikiRoot || asStr(res && res.wikiRoot)
  rawSlug = rawSlug || asStr(res && res.rawSlug)
}
if (!wikiRoot || !rawSlug) {
  log('Could not resolve a wiki root and target raw source — aborting.')
  return { error: 'unresolved', wikiRoot, rawSlug }
}
log('Target: ' + rawSlug + ' in ' + wikiRoot)
const rawPath = wikiRoot + '/raw/' + rawSlug + '.md'
const schemaPath = wikiRoot + '/SCHEMA.md'

// --- phase 1: split ---------------------------------------------------------
const CHUNKS_SCHEMA = {
  type: 'object',
  required: ['chunks'],
  properties: {
    chunks: {
      type: 'array',
      items: {
        type: 'object',
        required: ['title', 'startLine', 'endLine'],
        properties: {
          title: { type: 'string' },
          startLine: { type: 'integer' },
          endLine: { type: 'integer' },
        },
      },
    },
  },
}

phase('Split')
const split = await agent(
  'Split a large raw source into chapter-sized chunks by LINE RANGE, without reading the whole file (it is very large).\n' +
  '1. Read just the frontmatter of `' + rawPath + '` — its `structure:` list names the source\'s chapters/sections in order.\n' +
  '2. For each real chapter/section, find its heading line number in the BODY with Grep (search the heading text; return line numbers). Do NOT Read the whole body. If the structure list skips a chapter number (e.g. 5 then 7), Grep for the missing one too.\n' +
  '3. Return `chunks`: one entry per chapter with `title`, `startLine` (its heading line) and `endLine` (the line just before the next chapter heading; the last ends at end-of-file).\n' +
  'Fold trivial front/back matter (title page, copyright, table of contents, praise, "about the author", bibliography, index) into a neighbour or drop it. If any single chapter spans more than ~1500 lines, split it into 2-3 contiguous ranges titled "<title> (part N)". Aim for chunks of roughly 300-1500 lines each.',
  { schema: CHUNKS_SCHEMA, label: 'split:' + rawSlug, phase: 'Split' }
)
const chunks = (split && Array.isArray(split.chunks)) ? split.chunks.filter((c) => c && typeof c.startLine === 'number') : []
if (!chunks.length) {
  log('Split produced no chunks — aborting.')
  return { error: 'no-chunks', rawSlug }
}
log(chunks.length + ' chunk(s) to distill in parallel')

// --- phase 2: distill (map) -------------------------------------------------
const PAGES_SCHEMA = {
  type: 'object',
  required: ['verdict', 'pages'],
  properties: {
    verdict: { type: 'string', enum: ['in', 'partial', 'reject'] },
    note: { type: 'string' },
    pages: {
      type: 'array',
      items: {
        type: 'object',
        required: ['slug', 'group', 'title', 'body'],
        properties: {
          slug: { type: 'string' },
          group: { type: 'string' },
          title: { type: 'string' },
          kind: { type: 'string' },
          summary: { type: 'string' },
          tags: { type: 'array', items: { type: 'string' } },
          body: { type: 'string' },
        },
      },
    },
  },
}

phase('Distill')
const proposals = await parallel(
  chunks.map((c, i) => () =>
    agent(
      'Distill ONE chunk of a large source into PROPOSED wiki pages. Do NOT write any files — return the pages as data only; a later merge step commits them.\n' +
      'Charter: read `' + schemaPath + '` (Purpose / Scope / Domain extraction schema / Grouping principle / Languages). It is your lens. Write pages in the wiki\'s declared language.\n' +
      'Content: read ONLY lines ' + c.startLine + '-' + c.endLine + ' of `' + rawPath + '` with Read offset/limit — do NOT read the rest of the file. This chunk is: "' + (c.title || ('chunk ' + i)) + '".\n' +
      'Gate against Scope: set verdict "in", "partial", or "reject" (reject -> empty pages).\n' +
      'For the in-scope substance, return `pages` — atomic proposed pages: slug (lowercase-kebab, the natural name of the one thing the page is about, unique), group (the domain-topic folder a reader would look in), kind, summary, tags, and body = full markdown (encyclopedic lead, the reasoning + concrete specifics + trade-offs + failure modes, [[wikilinks]] to related slugs, and short verbatim quotes cited like `(raw L' + c.startLine + '..)`).\n' +
      'One page = one thing. Prefer a few substantial pages over many stubs. It is fine and expected that different chunks propose the same slug (e.g. "aggregate") — the merge step will fuse them.',
      { schema: PAGES_SCHEMA, label: 'distill:' + (c.title ? c.title.slice(0, 40) : i), phase: 'Distill' }
    ).then((r) => ({ chunk: c.title, verdict: (r && r.verdict) || 'reject', pages: (r && r.pages) || [] }))
  )
)
const kept = proposals.filter(Boolean).filter((p) => p.verdict !== 'reject')
const allPages = kept.flatMap((p) => p.pages.map((pg) => ({ ...pg, fromChunk: p.chunk })))
log(allPages.length + ' proposed page(s) from ' + kept.length + '/' + chunks.length + ' in-scope chunk(s)')
if (!allPages.length) {
  log('No in-scope pages proposed — recording the source as an off-charter rejection.')
  await agent(
    'The large source `' + rawSlug + '` was distilled against the charter at `' + schemaPath + '` and NO chunk was in scope — it is off-charter. Create NO wiki pages. Record the rejection: append ONE line to `' + wikiRoot + '/log.md`: `## [date] reject | ' + rawSlug + ' -- off-charter (large-source workflow), no pages created`. Do not touch index.md or .manifest.json.',
    { agentType: 'llm-wiki:wiki-keeper', label: 'reject-log', phase: 'Merge' }
  )
  return { chunks: chunks.length, proposedPages: 0, rejected: true }
}

// --- phase 3: merge (reduce), in SERIAL batches -----------------------------
// One writer at a time (no races on shared files), but split across batches so a large book's
// proposals are never truncated by a single prompt. Each batch sees the pages earlier batches
// wrote and merges into them; the final batch finalizes overview/synthesis/log.
const BATCH_CAP = 100000
const batches = []
{
  let cur = []
  let len = 0
  for (const pg of allPages) {
    const s = JSON.stringify(pg)
    if (len + s.length > BATCH_CAP && cur.length) { batches.push(cur); cur = []; len = 0 }
    cur.push(pg)
    len += s.length
  }
  if (cur.length) batches.push(cur)
}
log('merging ' + allPages.length + ' proposals in ' + batches.length + ' serial batch(es)')

phase('Merge')
const reports = []
for (let b = 0; b < batches.length; b++) {
  const last = b === batches.length - 1
  const rep = await agent(
    'You are the sole WRITER (batch ' + (b + 1) + ' of ' + batches.length + ') merging a large-source ingest into the llm-wiki at `' + wikiRoot + '`. Batches run one at a time, so you never race another writer.\n' +
    'Orient: read `' + schemaPath + '` (conventions, grouping principle, Languages) and `' + wikiRoot + '/wiki/index.md` — earlier batches and prior ingests may already have pages you must MERGE into, never overwrite.\n' +
    'Several proposals here may share a slug, or a slug may already exist in the wiki — fuse them into one coherent page. Write `' + wikiRoot + '/wiki/<group>/<slug>.md` with correct frontmatter (title; category = its group/folder; one-sentence summary; tags including the page kind; sources: the union of any sources already on the page and [' + rawSlug + '] (never drop provenance from earlier ingests); created and updated dates) and a coherent body with [[wikilinks]]. Keep pages atomic and cross-linked.\n' +
    (last
      ? 'This is the FINAL batch: after writing its pages, update `' + wikiRoot + '/wiki/overview.md` and `' + wikiRoot + '/wiki/synthesis.md` to reflect the whole source, and append ONE line to `' + wikiRoot + '/log.md`: `## [date] ingest | ' + rawSlug + ' -- large-source workflow, ' + allPages.length + ' proposals`. Ensure a source-summary page exists at `' + wikiRoot + '/wiki/<group>/' + rawSlug + '.md` — the source itself described (thesis, authority, scope, limitations, key takeaways) with sources: [' + rawSlug + ']; create it if earlier batches did not. Finally, regenerate the two DERIVED artifacts so a completed ingest leaves a consistent wiki even when the Stop hook that normally does this is not loaded: rebuild `index.md` and `.manifest.json` by running the wiki-lint `build_index` and `build_manifest` scripts against the wiki root.'
      : 'More batches follow: write/merge only this batch\'s pages. Do NOT finalize overview.md / synthesis.md / log.md yet — the final batch does that.') + '\n' +
    'PROPOSED PAGES (JSON array):\n' + JSON.stringify(batches[b]),
    { agentType: 'llm-wiki:wiki-keeper', label: 'merge ' + (b + 1) + '/' + batches.length, phase: 'Merge' }
  )
  reports.push(rep)
}
return { wikiRoot, rawSlug, chunks: chunks.length, proposedPages: allPages.length, batches: batches.length, merge: reports }
