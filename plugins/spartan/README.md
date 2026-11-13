# spartan

Agents answer a yes/no question with paragraphs. The developer reads all of it to find the one line
that mattered, and pays for every token.

`spartan` makes the agent answer with the conclusion first and then only what the reader needs to
act on it. It cuts content, not grammar: no restated question, no preamble, no closing summary, no
alternatives nobody asked for. Sentences stay correct, so it works the same in Russian, English or
any other language.

## Why not caveman

`caveman` saves tokens mostly through grammar: dropping articles and writing in fragments. That
works in English. Russian has no articles, and broken endings or dotted abbreviations ("т.е.",
"кол-во") cost as many tokens as the full words or more. Measured on a sample sentence with a
public tokenizer (tiktoken, used as a stand-in for Claude's), fragments and abbreviations saved 4%
in Russian and 38% in English; cutting content saved about 60% in both.

## Use

```
/spartan            # full, the default
/spartan lite       # conclusion plus a short reason
/spartan ultra      # conclusion only
/spartan off        # or say "normal mode" / "обычный режим"
```

The mode holds for the session. Ask for detail ("explain", "подробнее") and that one answer is
detailed. Warnings before irreversible actions, ambiguous steps and repeated questions get a full
answer automatically. Code, commits, PR text and documentation are written normally.

| Level | What the answer contains |
|---|---|
| lite | The conclusion, then a short reason. |
| full | The conclusion and only what is needed to act. |
| ultra | The conclusion alone. |

**From another plugin's agent** — preload the skill so the agent's reports are short:

```yaml
---
name: my-agent
skills:
  - spartan:spartan
---
```

## Results

See the pull request that introduced the plugin for the evaluation: output tokens and fact recall
per level and language, against no instruction, a one-line "answer concisely", and caveman.
