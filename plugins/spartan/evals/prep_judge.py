"""Build blind judge packets: per question, candidates shuffled under letters; key kept apart."""
import json, random, sys
from pathlib import Path

d = Path(sys.argv[1])
qs = json.loads((Path(__file__).parent / "questions.json").read_text(encoding="utf-8"))
facts = json.loads((d / "facts.json").read_text(encoding="utf-8"))
cands = sys.argv[2].split(",") if len(sys.argv) > 2 else ["concise", "caveman", "spartan-lite", "spartan-full", "spartan-ultra"]
rng = random.Random(8)
packets, key = [], {}
for q in qs:
    order = cands[:]; rng.shuffle(order)
    letters = "ABCDE"[:len(order)]
    key[q["id"]] = dict(zip(letters, order))
    answers = {L: json.loads((d / f"{q['id']}__{v}.json").read_text(encoding="utf-8"))["result"]
               for L, v in zip(letters, order)}
    packets.append(dict(id=q["id"], question=q["q"], key_facts=facts[q["id"]], answers=answers))
(d / "judge_packets.json").write_text(json.dumps(packets, ensure_ascii=False, indent=1), encoding="utf-8")
(d / "judge_key.json").write_text(json.dumps(key, indent=1), encoding="utf-8")
print(len(packets))
