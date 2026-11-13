"""Aggregate lengths, cost and (if present) judge verdicts into a markdown table."""
import json, sys, statistics as st
from pathlib import Path

d = Path(sys.argv[1])
rows = [json.loads(f.read_text(encoding="utf-8")) for f in d.glob("*__*.json")]
variants = ["base", "concise", "caveman", "spartan-lite", "spartan-full", "spartan-ultra"]
by = {}
for r in rows:
    by.setdefault((r["variant"], r["lang"]), []).append(r)
    by.setdefault((r["variant"], "all"), []).append(r)

verdict = {}
def load(dd, only=None):
    vf = dd / "judge_verdicts.json"
    if not vf.exists():
        return
    key = json.loads((dd / "judge_key.json").read_text(encoding="utf-8"))
    for item in json.loads(vf.read_text(encoding="utf-8")):
        for L, v in item["answers"].items():
            var = key[item["id"]][L]
            if only is None or var in only:
                verdict[(item["id"], var)] = v
# earlier iterations supply verdicts for variants not re-run here
for extra in sys.argv[2:]:
    load(Path(extra), only={"concise", "caveman"})
load(d)

base_tok = {r["id"]: r["output_tokens"] for r in rows if r["variant"] == "base"}
print("| variant | lang | output tokens (sum) | vs base | median chars | cost $ | facts kept | distorted | wrong adds | usable |")
print("|---|---|---|---|---|---|---|---|---|---|")
for lang in ("ru", "en", "all"):
    bsum = sum(r["output_tokens"] for r in by[("base", lang)])
    for v in variants:
        rs = by.get((v, lang), [])
        if not rs:
            continue
        tok = sum(r["output_tokens"] for r in rs)
        cost = sum(r["cost"] for r in rs)
        kept = tot = dist = wrong = usable = n = 0
        for r in rs:
            j = verdict.get((r["id"], v))
            if j:
                n += 1
                tot += len(j["facts"]); kept += sum(x == "present" for x in j["facts"])
                dist += sum(x == "distorted" for x in j["facts"])
                wrong += j["wrong_additions"]; usable += bool(j["usable_without_follow_up"])
        facts = f"{kept}/{tot} ({100*kept/tot:.0f}%)" if tot else "-"
        print(f"| {v} | {lang} | {tok} | {100*(tok-bsum)/bsum:+.0f}% | {st.median(r['chars'] for r in rs):.0f} | {cost:.2f} | {facts} | {dist if n else '-'} | {wrong if n else '-'} | {f'{usable}/{n}' if n else '-'} |")
