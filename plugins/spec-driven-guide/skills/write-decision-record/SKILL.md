---
name: write-decision-record
description: >-
  Record one architectural decision so it outlives the discussion that produced it — context, the
  choice, why, what it costs, and what was rejected. Use when someone says "let's write an ADR",
  "document this decision", "why did we pick X", or when a call has just been made in conversation
  that a future reader would find surprising without the reasoning. Also use to supersede a record
  whose decision has since been reversed.
---

# Write a decision record

A decision record fixes one point of an argument and outlives the document that made it. A design
doc decays with the system; the record of why a choice was made does not.

Apply [`writing-discipline`](../writing-discipline/SKILL.md) throughout.

## Step 1 — the entry gate

Three conditions, all required:

1. **Hard to reverse** — the cost of changing your mind later is meaningful.
2. **Surprising without context** — a future reader will look at the result and wonder why on earth
   it was done this way.
3. **The result of a real trade-off** — there were genuine alternatives and one was picked for
   specific reasons.

Where one fails, say so and write nothing. An easily reversed decision will simply be reversed; an
unsurprising one prompts no question; one with no alternative records nothing beyond "we did the
obvious thing". The gate is not bureaucracy — a log nobody can search is the failure mode of this
genre, and every record that clears no bar makes the ones that matter harder to find.

## Step 2 — write it

The record owes five things. Whether each gets its own heading is a presentation choice; whether
each is discharged is not.

| Owed | The test |
|---|---|
| Context | The forces in play, stated neutrally — someone who disagreed with the decision would still accept this paragraph |
| The decision | Stated in active voice, as something done: "we will…" |
| Because | The reasoning, not a restatement of the decision |
| Consequences | Including the ones nobody wanted and accepted anyway |
| Alternatives | What was rejected, and why each was rejected |

**Consequences are where records are weakest.** A record listing only benefits is an advertisement,
and the next reader — who inherits the costs — learns nothing they could act on. Where a decision
genuinely costs nothing beyond itself, say that in the same sentence as the reasoning; do not leave
the reader guessing whether the cost was omitted or absent.

A record can be one paragraph. The value is in recording *that* a decision was made and *why* — a
format cheap enough to always use beats a thorough one used sometimes.

## Step 3 — status and reversal

Where the project revisits decisions, mark status: proposed, accepted, deprecated, or superseded by
a later record.

**A reversed decision is superseded, never edited.** Editing destroys the thing the log exists for
— the record of what was believed, and why, at the time. Write a new record, state that it
supersedes the old one, and mark the old one superseded with a pointer forward. The old record
keeps its original text, wrong or not.

## Done when

- All three gate conditions hold, or nothing was written and the user was told why.
- Context is neutral enough that someone who disagreed with the decision would accept it.
- The reasoning is reasoning, not the decision restated.
- Consequences include at least one cost, or state explicitly that there is none.
- Each rejected alternative carries the reason it was rejected.
- Nothing in an existing record was edited to reflect a change of mind.
