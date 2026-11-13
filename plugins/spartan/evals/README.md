# spartan evaluation

Measures how much shorter answers get and how much meaning survives. 12 developer questions, six
in Russian and six in English. Types: yes/no, fact, explanation, debugging, steps, comparison,
dangerous operation.

## Method

1. `run.py <dir>` answers every question in `questions.json` under six variants, with Sonnet via
   `claude -p`: no instruction (`base`), a one-line system prompt "Answer concisely." (`concise`),
   `/caveman full`, and `/spartan lite|full|ultra`. Runs are isolated from the user's settings,
   plugins and `CLAUDE.md`. Output tokens come from the CLI's `usage`, so they are Claude's own
   counts.
2. `drift.py <dir>` runs two 5-turn dialogues (RU and EN) under `base`, `caveman` and
   `spartan-full`, to see whether brevity holds. It also measures how many input tokens the
   invoked skill adds.
3. A separate agent lists the key facts of each `base` answer (`facts.json`). Each list has 4–6
   facts, generous on purpose: it includes caveats a developer would want.
4. `prep_judge.py <dir>` shuffles the candidate answers under letters. Blind judge agents mark each
   key fact present, missing or distorted, count wrong claims, and say whether the answer can be
   acted on without a follow-up question.
5. `aggregate.py <dir> [earlier dirs]` prints the table.
6. `rewrite.py <dir>` asks each variant to shorten an existing long answer.

## Results (Sonnet, 2026-11-13)

Output tokens summed over the 6 questions per language, compared with `base`. "Facts kept" is the
share of key facts present.

| variant | RU tokens | EN tokens | facts kept | distorted | wrong claims | usable without follow-up |
|---|---|---|---|---|---|---|
| base | 5031 | 3331 | — | — | — | — |
| concise | −39% | −35% | 89% | 0 | 1 | 12/12 |
| caveman full | −41% | −41% | 92% | 0 | 1 | 12/12 |
| spartan lite | −65% | −74% | 83% | 0 | 0 | 12/12 |
| **spartan full** | **−72%** | **−74%** | 80% | 0 | 0 | 12/12 |
| spartan ultra | −77% | −85% | 64% | 0 | 0 | 12/12 |

**Five-turn dialogues, total output tokens.** Brevity holds through turn 5; no turn drifts back to
the base length.

| | base | caveman | spartan full |
|---|---|---|---|
| RU | 2891 | 1346 (−53%) | 561 (−81%) |
| EN | 4649 | 2769 (−40%) | 1209 (−74%) |

**Context cost.**
- Invoked, the spartan skill adds about 1.6k input tokens to the conversation; caveman adds about
  2.7k.
- When not invoked, only the description (about 100 tokens, estimated from its length) sits in the skill listing.
- After the first turn the body is read from the prompt cache.

**Shortening an existing text** ("shorten this, keeping its meaning"):
- Every variant cut 18–33% of the characters, and the no-instruction baseline did about as well.
- The skill's gain comes from what the agent chooses to say, not from rewriting.
- caveman was weakest on the Russian text (−18%).

## Reading the numbers

- Small sample: 12 questions and one run each. Treat differences of a few points as noise.
- The key-fact lists are generous. Most facts `spartan full` drops are secondary: an extra
  alternative, a second caveat. A blind judge found no distorted fact, no wrong claim, and every
  answer usable.
- A one-line "Answer concisely" already gets about 37%; caveman adds little on top of it.
  `spartan` roughly doubles the saving.
