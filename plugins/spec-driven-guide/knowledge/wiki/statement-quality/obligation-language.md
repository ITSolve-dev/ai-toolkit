---
title: Obligation language
category: statement-quality
summary: Three levels — absolute, defeasible with reasons, and truly optional — each committing the reader to something different, and each defeated by the same failure to choose deliberately.
tags: [concept, obligation-language, requirement]
sources: [web-page-rfc-2119-key-words-for-use-in-rfcs-to-indicate-requirement-levels-rfc-editor]
created: 2026-08-06
updated: 2026-08-06
---

[[rfc-2119-requirement-levels]] fixes three levels of force, with synonyms for each.

**MUST** — also REQUIRED, SHALL — "mean that the definition is an absolute requirement of the
specification" (L49). The negative form, MUST NOT or SHALL NOT, is "an absolute prohibition"
(L51).

**SHOULD** — also RECOMMENDED — is the interesting one, because it is not a weak MUST:

> there may exist valid reasons in particular circumstances to ignore a particular item, but the
> full implications must be understood and carefully weighed before choosing a different course.
>
> — L53

SHOULD does not permit ignoring the item. It permits ignoring it **after understanding what that
costs**. The obligation is transferred from the outcome to the deliberation: a reader who deviates
without weighing has violated the SHOULD as surely as one who violates a MUST.

**MAY** — also OPTIONAL — "mean that an item is truly optional", and the RFC spells out what
optionality implies for everyone else: an implementation omitting the option "MUST be prepared to
interoperate with another implementation which does include the option, though perhaps with reduced
functionality", and vice versa (L64-L74).

That last clause is easy to miss and does real work: **declaring something optional creates
obligations on both sides.** Optionality is not the absence of a requirement; it is a requirement
to tolerate both answers.

## Why the levels are worth the trouble

Without them, force is carried by tone, and tone is read differently by every reader. "The system
should validate input" can mean an absolute requirement, a strong preference, or an aspiration, and
nothing in the sentence distinguishes them. The three levels make the writer choose, and the choice
is then visible to the reader rather than inferred.

For a reader who is an agent rather than a person, this matters more, not less: tone is exactly the
signal a machine reader reconstructs least reliably, and an unmarked "should" invites it to guess
at how binding the statement was meant to be.

## The symptom

**Force asserted by emphasis instead of by level.** Bold text, "it is critical that", "we really
need to" — each signals that the writer felt the weight of a claim and did not state it. The check
is direct: for every statement that constrains what an implementation does, ask which of the three
levels it is. A statement that resists the question has not decided how binding it is, and the
reader will decide instead.

The second symptom is the mirror: **levels applied uniformly**, every statement a MUST. This
carries no more information than none at all, and it runs into
[[imperatives-constrain-outcomes-not-methods]], which restricts when the strong form is legitimate.

Related: [[completion-criteria]], which grades the bound a statement sets rather than the force it
carries — the two vary independently, and a MUST with a vague bound obliges nothing.
