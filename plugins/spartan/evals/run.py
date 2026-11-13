"""Run each question under each variant with `claude -p` (Sonnet), save answer + usage.

Usage: python run.py <out_dir> [variant ...]
The caveman variant needs CAVEMAN_PLUGIN: a plugin directory holding caveman's SKILL.md.
Runs use --setting-sources project, no tools, and CLAUDE_CODE_DISABLE_CLAUDE_MDS=1, so the
user's own settings, plugins and CLAUDE.md do not leak into the answers.
"""
import json, subprocess, sys, os, tempfile, concurrent.futures as cf
from pathlib import Path

HERE = Path(__file__).parent
SPARTAN = str(HERE.parent)
CAVEMAN = os.environ.get("CAVEMAN_PLUGIN", "")
RUNDIR = Path(tempfile.mkdtemp(prefix="spartan-eval-"))

VARIANTS = {
    "base":         dict(prefix="", extra=[]),
    "concise":      dict(prefix="", extra=["--append-system-prompt", "Answer concisely."]),
    "caveman":      dict(prefix="/caveman full\n\n", extra=["--plugin-dir", CAVEMAN]),
    "spartan-lite": dict(prefix="/spartan lite\n\n", extra=["--plugin-dir", SPARTAN]),
    "spartan-full": dict(prefix="/spartan full\n\n", extra=["--plugin-dir", SPARTAN]),
    "spartan-ultra":dict(prefix="/spartan ultra\n\n", extra=["--plugin-dir", SPARTAN]),
}


def run(prompt, extra, resume=None):
    cmd = ["claude", "-p", "--setting-sources", "project", "--model", "sonnet",
           "--output-format", "json", "--tools", ""] + extra
    if resume:
        cmd += ["--resume", resume]
    p = subprocess.run(cmd, input=prompt, capture_output=True, text=True, encoding="utf-8", cwd=RUNDIR, timeout=600,
                       env={**os.environ, "CLAUDE_CODE_DISABLE_CLAUDE_MDS": "1"})
    d = json.loads(p.stdout)
    u = d["usage"]
    return dict(result=d["result"], session=d["session_id"], output_tokens=u["output_tokens"],
                input_total=u["input_tokens"] + u["cache_creation_input_tokens"] + u["cache_read_input_tokens"],
                cost=d["total_cost_usd"], is_error=d.get("is_error"))


def one(out, q, vname):
    f = out / f"{q['id']}__{vname}.json"
    if f.exists():
        return
    v = VARIANTS[vname]
    r = run(v["prefix"] + q["q"], v["extra"])
    r.update(id=q["id"], lang=q["lang"], type=q["type"], variant=vname, chars=len(r["result"]),
             words=len(r["result"].split()))
    f.write_text(json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f.name, r["output_tokens"], flush=True)


def main():
    out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
    variants = sys.argv[2:] or list(VARIANTS)
    qs = json.loads((HERE / "questions.json").read_text(encoding="utf-8"))
    with cf.ThreadPoolExecutor(6) as ex:
        futs = [ex.submit(one, out, q, v) for q in qs for v in variants]
        for fu in cf.as_completed(futs):
            if fu.exception():
                print("ERR", fu.exception(), flush=True)


if __name__ == "__main__":
    main()
