---
title: Agent Silence Is Not Completeness
category: task-content
summary: An agent not asking a question does not show the task was complete; readiness is judged from the task and the repository, and telling the agent to ask is not a substitute.
tags: [rule, task-content, agents, readiness, evidence]
sources: [ambig-swe]
created: 2026-11-01
updated: 2026-11-02
---

# Agent Silence Is Not Completeness

An agent that starts a task without asking anything has told you nothing about whether the task was complete. In the Ambig-SWE benchmark, not asking was the default behaviour whatever the input:

> Without explicit prompting, models almost never interact, even for severely underspecified inputs.
>
> — [[ambig-swe]], L202

## The rule

Decide whether a task is ready from its text and the repository, before an agent starts. Do not treat the absence of questions as a pass, and do not treat an instruction to ask as a replacement for the check.

## Sign of violation

- **In board history:** a task that was finished and then reopened or reworked because of a fact that was neither in its text nor recoverable from the repository ([[recoverable-versus-task-only-facts]]), with no question raised before it finished. This sign is this wiki's. The paper measured a benchmark and not a board.
- **In a readiness record:** a task marked ready on the grounds that the agent raised no objection, or a process whose only readiness step is a prompt telling the agent to ask.

## Why

Three findings carry the rule. All come from the detection experiment summarised on [[ambig-swe]], with stripped issues and detection counted in the first three turns only.

**Most models do not calibrate asking to the input; Claude Sonnet is the exception.** The authors report: "Despite the stark difference in the language and detail of summarized issues and fully specified issues, the models, except Claude Sonnet, fail to reliably distinguish them, indicating that LLMs struggle to detect missing information even in obvious cases." (L211). Even the best result in the table, Claude Sonnet 4 under the Strong prompt, missed 18% of the stripped issues (FNR 0.18, L193).

**Encouragement helps some models and harms others.** Claude Sonnet 4 improved on both errors from Neutral to Strong, FPR 0.08 to 0.03 and FNR 0.44 to 0.18, with accuracy 0.74 to 0.89 (L193). Claude Sonnet 3.5 went from Neutral to Moderate with FNR 0.81 to 0.09 and accuracy 0.60 to 0.84, and Claude Haiku 3.5 also improved (L195, L196). The others moved the error or worsened. Claude Sonnet 3.5 went from FPR 0.24 at Moderate to 0.36 at Strong with no gain on misses (FNR 0.09 to 0.10), and accuracy fell from 0.84 to 0.76 (L195). Deepseek-v2 got worse as encouragement rose, from accuracy 0.69 at Neutral to 0.51 at Strong (L197). Llama 3.1 70B asked on nearly everything at Moderate and Strong (FPR 0.95 and 0.93, L198). Qwen 3 Coder did not ask under any of the three prompts (FNR 1.00, L194).

**The authors reach the same conclusion about prompts:**

> Models default to non-interactive behavior unless explicitly prompted, yet prompt engineering alone proves insufficient for reliable underspecificity detection.
>
> — [[ambig-swe]], L213

This wiki reads that as applying to the plugin's own design: an instruction telling an agent to ask is worth having, and it does not make readiness safe to skip. The result depends on the model and on the wording, and neither is under the plugin's control.

## Limit

The study measured a coding agent deciding whether to ask during a run. It did not test a separate review whose only job is to judge a task's completeness, so it does not show that an LLM cannot perform that review. This wiki's rule is therefore about not relying on the executor's silence, and it makes no claim that automated review is impossible. The numbers belong to these six model versions, and the shape is what transfers.

## Cost

The check moves work to before the start, and asking costs something too. The authors say "Unnecessary interaction when sufficient information is already available can introduce inefficiencies and burden users." (L182). So the rule is not to ask more. It is to do the check on the text, and to ask only as [[clarifying-questions]] describes.

## Related

[[underspecified-task]] says why an omission is hard to see. [[conversation-moves-into-the-task]] is the positive form of this rule.
