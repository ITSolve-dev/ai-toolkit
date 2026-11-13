"""5-turn dialogue per variant (does brevity hold?) + per-turn context cost of each skill."""
import json, sys
from pathlib import Path
from run import run, VARIANTS

TURNS_RU = [
    "Чем отличается git merge от git rebase?",
    "А что безопаснее для общей ветки?",
    "Как посмотреть, какие коммиты есть в feature, но нет в main?",
    "Почему `git pull` иногда создаёт merge-коммит?",
    "Как это отключить глобально?",
]
TURNS_EN = [
    "What's the difference between a process and a thread?",
    "Which one should I use for CPU-bound work in Python?",
    "How do I share data between processes then?",
    "Is multiprocessing.Queue safe to use from several producers?",
    "What happens to the queue if a producer crashes mid-put?",
]

out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
res = {}
for lang, turns in (("ru", TURNS_RU), ("en", TURNS_EN)):
    for vname in ("base", "caveman", "spartan-full"):
        v = VARIANTS[vname]
        sess, rows = None, []
        for i, t in enumerate(turns):
            r = run((v["prefix"] if i == 0 else "") + t, v["extra"], resume=sess)
            sess = r["session"]
            rows.append(dict(turn=i + 1, q=t, answer=r["result"], output_tokens=r["output_tokens"], cost=r["cost"]))
            print(lang, vname, i + 1, r["output_tokens"], flush=True)
        res[f"{lang}/{vname}"] = rows

# context cost: invoked skill body (input tokens with skill minus without), same trivial prompt
probe = "Reply with the single word OK."
cost = {}
for vname in ("base", "caveman", "spartan-full"):
    v = VARIANTS[vname]
    cost[vname] = run(v["prefix"] + probe, v["extra"])["input_total"]
# always-on description cost: plugin loaded, not invoked
cost["spartan-loaded-not-invoked"] = run(probe, VARIANTS["spartan-full"]["extra"])["input_total"]
cost["caveman-loaded-not-invoked"] = run(probe, VARIANTS["caveman"]["extra"])["input_total"]
res["context_cost_input_tokens"] = cost
(out / "drift.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps(cost))
