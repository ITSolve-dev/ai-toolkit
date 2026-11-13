import json, sys
from pathlib import Path
from run import run, VARIANTS
d = Path(sys.argv[1]); out = {}
src = {"ru": ("ru-explain-pool", "Сократи этот текст, сохранив смысл:\n\n"),
       "en": ("en-compare-pk", "Shorten this text, keeping its meaning:\n\n")}
for lang, (qid, ask) in src.items():
    text = json.loads((d / f"{qid}__base.json").read_text(encoding="utf-8"))["result"]
    out[lang] = {"source": text, "source_chars": len(text)}
    for v in VARIANTS:
        r = run(VARIANTS[v]["prefix"] + ask + text, VARIANTS[v]["extra"])
        out[lang][v] = dict(result=r["result"], output_tokens=r["output_tokens"], chars=len(r["result"]))
        print(lang, v, r["output_tokens"], len(r["result"]), flush=True)
(d / "rewrite.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
