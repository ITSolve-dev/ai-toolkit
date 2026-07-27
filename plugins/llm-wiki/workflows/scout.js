export const meta = {
  name: 'scout',
  description: 'Fan-out source scout for an llm-wiki: read the charter, find coverage gaps, search the web in parallel (one searcher per gap in its own context), judge each candidate against the charter, and return a ranked candidate list for human approval. Never ingests.',
  whenToUse: 'Invoked by the wiki-scout skill. Pass args: { wikiRoot: "<abs path to the wiki root (dir with SCHEMA.md)>", focus?: "<optional topic to scout, else scout the whole charter>" }.',
  phases: [
    { title: 'Resolve', detail: 'find the wiki root if the runtime dropped the args (SCHEMA.md search)' },
    { title: 'Charter', detail: 'one agent reads SCHEMA.md + index + manifest → coverage gaps + already-held sources' },
    { title: 'Search', detail: 'one searcher agent per gap, parallel WebSearch, isolated context' },
    { title: 'Assess', detail: 'fetch each novel candidate, judge fit against Purpose/Scope (the ingest relevance lens)' },
    { title: 'Rank', detail: 'dedup, drop off-charter, rank, assemble the approval list' },
  ],
}

// wiki-scout: Charter → pipeline(Search per gap → URL-dedup vs each other & known sources → Fetch+Assess) → Rank.
// Modeled on the deep-research harness, adapted for sourcing: no adversarial claim voting — a single
// per-candidate fit judgment against the wiki's charter (the same lens wiki-ingest's relevance gate uses).
// Proposes candidates only; ingestion stays a separate, human-approved step (Karpathy: the human curates sources).

const MAX_CANDIDATES = 10   // hard cap on sources fetched+assessed, to bound cost
const PER_GAP_RESULTS = 4   // search results requested per gap before dedup
const MAX_GAPS = 6          // cap on coverage gaps → searcher agents (charter picks the most important)

// ─── Schemas ───
const CHARTER_SCHEMA = {
  type: "object", required: ["purpose", "gaps", "knownSources"],
  properties: {
    purpose: { type: "string" },                 // one line: what this wiki is for (for downstream prompts)
    gaps: { type: "array", minItems: 0, maxItems: 6, items: {
      type: "object", required: ["label", "query"],
      properties: {
        label: { type: "string" },               // short name of the gap
        query: { type: "string" },               // a web search query that would find sources for it
        rationale: { type: "string" },           // why the wiki needs this (missing / thin / one-sided)
      },
    }},
    knownSources: { type: "array", items: { type: "string" } },  // urls/titles already ingested — for dedup
  },
}
const SEARCH_SCHEMA = {
  type: "object", required: ["results"],
  properties: {
    results: { type: "array", maxItems: 8, items: {
      type: "object", required: ["url", "title", "relevance"],
      properties: {
        url: { type: "string" },
        title: { type: "string" },
        snippet: { type: "string" },
        relevance: { enum: ["high", "medium", "low"] },
      },
    }},
  },
}
const ASSESS_SCHEMA = {
  type: "object", required: ["fit", "kind", "why"],
  properties: {
    fit: { enum: ["in", "partial", "off"] },     // in scope / partly / off-charter — the ingest gate lens
    kind: { type: "string" },                    // book | web-page | paper | talk | forum | ...
    fills: { type: "string" },                   // which gap it closes
    why: { type: "string" },                     // one line: authority / why it fits
    caveat: { type: "string" },                  // paywall, dated, low authority, couldn't open — or "none"
    authority: { enum: ["primary", "strong", "ok", "weak"] },
  },
}

// ─── Input ───
// args may arrive as an object, a JSON string of that object, or a bare path string — normalize all three.
// The runtime can also DROP workflow args (claude-code#63876); when wikiRoot is missing we re-discover it
// (like the ingest-large-source workflow), so the workflow is robust however it is invoked.
let input = args
if (typeof input === "string") {
  const t = input.trim()
  if (t.startsWith("{")) { try { input = JSON.parse(t) } catch { input = { wikiRoot: t } } }
  else input = { wikiRoot: t }
}
input = input || {}
const asStr = v => (typeof v === "string" ? v.trim() : "")  // a non-string wikiRoot/focus must not throw
let WIKI_ROOT = asStr(input.wikiRoot)
const FOCUS = asStr(input.focus)
if (!WIKI_ROOT) {
  phase("Resolve")
  const res = await agent(
    "Find the WIKI ROOT for a source scout: the directory that contains `SCHEMA.md`. Search the current " +
    "working directory and its subdirectories (Glob `**/SCHEMA.md`) and pick the shallowest match. " +
    "Never return a home or filesystem root. Return the absolute path as `wikiRoot`.",
    { label: "resolve", phase: "Resolve", schema: { type: "object", required: ["wikiRoot"], properties: { wikiRoot: { type: "string" } } } }
  )
  WIKI_ROOT = asStr(res && res.wikiRoot)
}
if (!WIKI_ROOT) {
  return { error: "No wikiRoot provided, and none could be resolved (no SCHEMA.md found)." }
}
phase("Charter")

// ─── Phase 0: Charter — read the wiki, derive gaps and known sources ───
const charter = await agent(
  "## Wiki charter reader\n\n" +
  "Wiki root: `" + WIKI_ROOT + "`\n" +
  (FOCUS ? "Scout focus (narrow to this): **" + FOCUS + "**\n" : "") +
  "\n## Task\n" +
  "1. Read `" + WIKI_ROOT + "/SCHEMA.md` — its **Purpose**, **Scope**, **Domain extraction schema**, and grouping principle.\n" +
  "2. Read `" + WIKI_ROOT + "/wiki/index.md` and the source-summary pages it lists to see what is already covered.\n" +
  "3. Read `" + WIKI_ROOT + "/.manifest.json` if it exists — each entry's `origin` is a source already ingested (its URL or path).\n" +
  "4. Name the **coverage gaps**: sub-topics the charter wants but the wiki lacks or is thin/one-sided on. " +
  (FOCUS ? "Stay within the focus topic. " : "Range across the charter. ") +
  "Return only the **" + MAX_GAPS + " most important** gaps (fewer, or none, if the wiki is well-covered) — each spins up a searcher, so prioritize, don't enumerate exhaustively. " +
  "For each gap give a short label, a concrete web-search query that would find good sources for it, and a one-line rationale.\n" +
  "5. Return `knownSources`: every `origin` value from `.manifest.json` (the actual URLs/paths already ingested), so the search can skip re-proposing them. Empty list if there is no manifest.\n\n" +
  "Do not search the web here — only read the wiki and reason about what it needs. Structured output only.",
  { label: "charter", phase: "Charter", schema: CHARTER_SCHEMA }
)
if (!charter) return { error: "Charter agent returned no result — could not read the wiki at " + WIKI_ROOT }
log(charter.gaps.length + " gaps identified; " + charter.knownSources.length + " known sources to skip")

// ─── Dedup state — URL keys, seeded with sources already in the wiki ───
const URL_HOST_PATTERN = /^[a-z][a-z0-9+.-]*:\/\/(?:[^/?#\\]*@)?(?:www\.)?([^/:?#@\\]+)(?::\d+)?([^?#]*)(?:\?([^#]*))?/i
const TRACKING = new Set(["fbclid", "gclid", "gclsrc", "dclid", "yclid", "ref", "ref_src", "mc_cid", "mc_eid", "igshid", "_ga"])
const isTracking = key => key.startsWith("utm_") || key.startsWith("_hs") || TRACKING.has(key.toLowerCase())
const normURL = u => {
  const m = String(u).match(URL_HOST_PATTERN)
  if (!m) return String(u).trim().toLowerCase()
  const base = (m[1] + m[2].replace(/\/$/, "")).toLowerCase()
  // Keep the query — it distinguishes ?v=A from ?v=B, ?id=A from ?id=B (talks, books, threads) —
  // but drop tracking params so utm noise never splits one source into several. Query keeps its
  // case (IDs are case-sensitive); host+path stay lowercased.
  const query = (m[3] || "").split("&").filter(kv => kv && !isTracking(kv.split("=")[0])).sort().join("&")
  return query ? base + "?" + query : base
}
// Web-controlled host/title reach the terminal via progress labels — strip control/bidi/zero-width
// and quote-lookalike chars so a result can't forge a trusted-looking host or smuggle escape sequences.
const LABEL_CAP = 40
const LABEL_STRIP = /[\x00-\x1f\x7f-\x9f​-‏‪-‮⁦-⁩﻿"“-‟″‶❝❞〝〞＂]/g
const STRICT_HOST = /^[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)*$/
const stripLabelChars = s => String(s).replace(LABEL_STRIP, "")
const quotedLabel = s => {
  const cps = Array.from(stripLabelChars(s))
  return '"' + cps.slice(0, LABEL_CAP).join("").trim() + (cps.length > LABEL_CAP ? "…" : "") + '"'
}
const safeHostLabel = url => {
  const host = (String(url).match(URL_HOST_PATTERN)?.[1] ?? "").toLowerCase()
  const clean = stripLabelChars(host)
  const bare = clean === host && host !== "" && Array.from(host).length <= LABEL_CAP && STRICT_HOST.test(host)
  return clean === "" ? "src" : bare ? host : quotedLabel(host)
}
// Gap labels are web-derived (the charter agent reads ingested pages) and reach the terminal as
// progress labels — strip the same dangerous chars before displaying them.
const safeText = s => {
  const cps = Array.from(stripLabelChars(s))
  return cps.slice(0, LABEL_CAP).join("") + (cps.length > LABEL_CAP ? "…" : "")
}

const seen = new Map()
for (const s of charter.knownSources) seen.set(normURL(s), "known")
const relRank = { high: 0, medium: 1, low: 2 }
let slots = MAX_CANDIDATES
// Reserve a fair share per gap so whichever searchers resolve first can't take every slot and
// starve later gaps (ordering is just agent latency). Unused reserved slots simply go unfilled.
const perGapCap = Math.max(1, Math.floor(MAX_CANDIDATES / Math.max(1, charter.gaps.length)))
const budgetDropped = []

const SEARCH_PROMPT = gap =>
  "## Source searcher: " + gap.label + "\n\n" +
  "Wiki purpose: " + charter.purpose + "\n" +
  "Gap to fill: **" + gap.label + "** — " + (gap.rationale || "") + "\n" +
  "Search query: `" + gap.query + "`\n\n" +
  "## Task\nUse WebSearch (the query above or a refinement). Return the " + PER_GAP_RESULTS + " best SOURCES for this gap — " +
  "prefer primary/authoritative material (the canonical book, standard reference, practitioner with standing) over SEO restatements. " +
  "Rank by relevance to the wiki's purpose, not just the query. Skip content farms.\n\nStructured output only."

const ASSESS_PROMPT = (source, gapLabel) =>
  "## Candidate assessor\n\n" +
  "Wiki purpose: " + charter.purpose + "\n" +
  "Candidate found for gap: **" + gapLabel + "**\n" +
  "**URL:** " + source.url + "\n**Title:** " + source.title + "\n\n" +
  "## Task\n1. WebFetch the page enough to confirm it is real, substantive, and on-topic — not a stub, listicle, or paywalled teaser.\n" +
  "2. Judge FIT against the wiki's Purpose/Scope, exactly as an ingest relevance gate would: `in` (belongs), " +
  "`partial` (only part is on-charter — say which in `why`), or `off` (drop it).\n" +
  "3. Classify `kind` (book/web-page/paper/talk/forum/…) and `authority` (primary/strong/ok/weak).\n" +
  "4. `fills`: the gap it closes. `why`: one line on authority/fit. `caveat`: paywall/dated/weak/couldn't-open, or \"none\".\n\n" +
  "If the fetch fails, return fit:\"off\" only if clearly irrelevant; otherwise fit:\"partial\" — and STILL fill every required field: kind:\"web-page\", why:\"couldn't fully open\", plus caveat:\"couldn't fully open\".\nStructured output only."

// ─── Pipeline: search per gap → dedup → fetch+assess (no barrier) ───
const assessed = await pipeline(
  charter.gaps,

  gap => agent(SEARCH_PROMPT(gap), { label: "search:" + safeText(gap.label), phase: "Search", schema: SEARCH_SCHEMA })
    .then(r => (r ? { gap: gap.label, results: r.results } : null)),

  searchResult => {
    if (!searchResult) return []
    const sorted = [...searchResult.results].sort((a, b) => relRank[a.relevance] - relRank[b.relevance])
    let takenThisGap = 0
    const novel = sorted.filter(r => {
      const key = normURL(r.url)
      if (seen.has(key)) return false                          // already in wiki, or picked by another gap
      if (takenThisGap >= perGapCap || slots <= 0) {           // this gap's fair share, or the global budget, is spent
        budgetDropped.push(r.url)
        return false
      }
      seen.set(key, searchResult.gap)
      slots--
      takenThisGap++
      return true
    })
    const filtered = searchResult.results.length - novel.length
    if (filtered) log(safeText(searchResult.gap) + ": " + novel.length + " kept, " + filtered + " skipped (known/dup/over-budget)")
    return parallel(novel.map(source => () =>
      agent(ASSESS_PROMPT(source, searchResult.gap), {
        label: "assess:" + safeHostLabel(source.url), phase: "Assess", schema: ASSESS_SCHEMA,
      }).then(a => (a ? { ...a, url: source.url, title: source.title, gap: searchResult.gap } : null))
        .catch(() => ({ fit: "partial", kind: "web-page", why: "assessment errored", caveat: "couldn't open", url: source.url, title: source.title, gap: searchResult.gap }))
    ))
  }
)

// ─── Rank & assemble the approval list ───
phase("Rank")
const all = assessed.flat().filter(Boolean)
const kept = all.filter(c => c.fit !== "off")
const dropped = all.filter(c => c.fit === "off")

const fitRank = { in: 0, partial: 1 }
const authRank = { primary: 0, strong: 1, ok: 2, weak: 3 }
kept.sort((a, b) =>
  (fitRank[a.fit] - fitRank[b.fit]) ||
  (authRank[a.authority] ?? 2) - (authRank[b.authority] ?? 2)
)

log("Assessed " + all.length + " candidates → " + kept.length + " on-charter (" + dropped.length + " dropped as off-topic)")

return {
  wikiRoot: WIKI_ROOT,
  focus: FOCUS || null,
  purpose: charter.purpose,
  gaps: charter.gaps.map(g => g.label),
  candidates: kept.map(c => ({
    title: c.title, url: c.url, kind: c.kind, fit: c.fit,
    fills: c.fills || c.gap, why: c.why, authority: c.authority || null, caveat: c.caveat || "none",
  })),
  droppedOffCharter: dropped.map(c => ({ title: c.title, url: c.url, why: c.why })),
  stats: {
    gaps: charter.gaps.length,
    knownSourcesSeeded: charter.knownSources.length,
    assessed: all.length,
    onCharter: kept.length,
    droppedOffCharter: dropped.length,
    budgetDropped: budgetDropped.length,   // candidates found but not assessed (per-gap cap / global budget)
  },
}
