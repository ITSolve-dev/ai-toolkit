# spartan

Agents answer a yes/no question with paragraphs. The developer reads all of it to find the one line
that mattered, and pays for every token.

`spartan` makes the agent answer with the conclusion first and then only what the reader needs to
act on it. It cuts content, not grammar: no restated question, no preamble, no closing summary, no
alternatives nobody asked for. Sentences stay correct, so it works the same in Russian, English or
any other language.

## Use

Ask your agent to use Spartan, for example “Use Spartan lite for this session.” Clients that support slash commands can also use the following forms.

```
/spartan            # full, the default
/spartan lite       # conclusion plus a short reason
/spartan ultra      # conclusion with its conditions
/spartan off        # or say "normal mode" / "обычный режим"
```

The mode holds for the session. Ask for detail ("explain", "подробнее") and that one answer is
detailed. Warnings before irreversible actions, ambiguous steps and repeated questions get a full
answer automatically. Code, commits, PR text and documentation are written normally.

| Level | What the answer contains |
|---|---|
| lite | What `full` has, plus the reason and caveats that change what you do. |
| full | The conclusion and only what is needed to act. |
| ultra | The conclusion with its conditions. |

To use Spartan in another agent's reports, ask that agent to use the Spartan skill.
