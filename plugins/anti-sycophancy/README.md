# anti-sycophancy

Sycophancy is not excess politeness — it is a measurement error. An assessment shaped by what the
user hopes to hear carries no information, and gets acted on anyway.

This plugin collects the tooling for assessments that do not bend toward the asker. Skills are
added here as the failure shows up in new places; the shared doctrine below is what any of them
must respect.

## Skills

| Skill | Runs in | Sees the conversation | Multi-turn | Use it for |
|---|---|---|---|---|
| `honest-assessment` | current context | yes | yes | Changing how *this* assistant answers — opinions, reviews, comparisons, holding position under pushback. Attachable to other agents. |
| `second-opinion` | isolated fork | **no** | no, one pass | A reviewer that never helped build the idea. Takes the question as an argument. |

`honest-assessment` is the default and the one other plugins attach. `second-opinion` exists
because a large share of sycophancy is not politeness but **co-authorship**: after twenty turns of
developing something together, conceding the idea was wrong means conceding your own work was
wrong. No amount of instruction removes that; a context that was never in the room does.

## Using it

**Ad hoc** — skills auto-trigger on assessment-shaped requests, or invoke directly:

```
/anti-sycophancy:honest-assessment
/anti-sycophancy:second-opinion should billing move into its own service, given <context>
```

`second-opinion` has no access to the conversation. Whatever it needs — the constraint, the
numbers, the file paths — must be in the argument. That cost is what buys the independence.

**From another plugin's agent** — preload the skill into the agent's own context, so honesty is
never a call the agent has to make at runtime:

```yaml
# plugins/llm-wiki/agents/wiki-keeper.md
---
name: wiki-keeper
skills:
  - anti-sycophancy:honest-assessment
---
```

and declare the dependency, so enabling the host plugin enables this one:

```jsonc
// plugins/llm-wiki/.claude-plugin/plugin.json
"dependencies": [{ "name": "anti-sycophancy", "version": "^0.1.0" }]
```

**From another skill** — one line in its body: *"Assess per `anti-sycophancy:honest-assessment`."*

**Always-on, in a project** — paste the snippet below into the project's `CLAUDE.md`.

Deliberately a copy, not an `@` import: `${CLAUDE_PLUGIN_ROOT}` changes on every plugin update and
sibling plugins are not guaranteed adjacent on disk, so a path into the plugin cache would rot.

Keep it short, and resist growing it. `CLAUDE.md` is re-read on every request, so the full
methodology does not belong there — it would be a permanent context tax charged even on "fix this
typo", and guidance that is always present stops registering as guidance.

```markdown
## Assessment

When giving an opinion, review or comparison, aim for the assessment a stranger would have
gotten — one that does not move based on what I appear to want to hear. Lead with the problem
that decides whether the thing works, not the safest one to raise. Distinguish "wrong" from
"risky" from "a taste difference". If you looked and found no real flaw, say so plainly instead
of manufacturing one. Under pushback, update on new evidence or on a flaw in your own reasoning —
not on repetition or irritation. Skip praise openers and compliment sandwiches: they do not change
the assessment, they only obscure it.
```

## Doctrine

Constraints that hold for every skill in this plugin. New skills are judged against these, not
against whether they sound appropriately tough.

**The target is frame-independence, not disagreement.** "Always argue the opposing case first" — the
rule most anti-sycophancy prompts in the wild are built on — produces reflexive contrarianism, which
has the identical defect: the social frame still decides the answer, only with the sign flipped. Aim
for the assessment a stranger would have gotten, in either direction. That includes giving credit
where it is earned; withholding it is the same error, not the cure.

**"I found no flaw" is an endorsed output.** Without that exit, the expectation that a review
contains criticism manufactures criticism — and manufactured criticism trains the reader to discount
the real kind.

**Every skill documents its own failure mode.** Rules like these reliably produce performative rigor
as a side effect. A skill that only lists what sycophancy looks like is half-written; see
`skills/honest-assessment/failure-modes.md` for the shape.

**Severity beats volume.** Load-bearing issue first, ranked, labelled `wrong` / `risky` / `taste`.
A long list of small findings with no verdict is what you produce when you would rather not be wrong
in front of someone.

## Layout

```
anti-sycophancy/
├── .claude-plugin/plugin.json
└── skills/
    ├── honest-assessment/
    │   ├── SKILL.md
    │   └── failure-modes.md
    └── second-opinion/
        └── SKILL.md
```

One directory per skill under `skills/`. `SKILL.md` stays short; supporting material lives beside
it in the same directory.
