---
title: Project Buffer Sizing
category: periods
summary: Sizing a schedule buffer as the square root of the sum of squared 50-to-90 spreads, so that riskier items weigh more; or, failing two estimates, half the sum of 50% estimates, which ignores where the risk is.
tags: [method, planning-a-date, buffer, estimation, numbers]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Project Buffer Sizing

The size of a [[schedule-buffer]] comes from how far each item's 90% estimate sits above its 50% estimate. The spread is the measure of risk: "the numbers very clearly point out the degree of schedule risk associated with each item" ([[cohn-agile-estimating-planning]] L3962). Two stories both starting at 3 are not the same if one tops out at 5 and the other at 10.

## Square root of the sum of the squares

Buffer = √( (w₁−a₁)² + (w₂−a₂)² + … + (wₙ−aₙ)² ), where w is the 90% estimate and a the 50% estimate (L3966, L3968). In Cohn's words, "The schedule buffer is the square root of the sum of these squares" (L3968). The technique goes back to Reinertsen (1997), Newbold (1998) and Leach (2000) (L3970).

Table 17.2 (L3978-L3986):

| Story | 50% | 90% | (90%−50%)² |
|---|---|---|---|
| Authentication | 1 | 3 | 4 |
| Practice schedule | 3 | 5 | 4 |
| League pool locations | 5 | 8 | 9 |
| National records | 2 | 5 | 9 |
| Personal records | 5 | 13 | 64 |
| Meet results | 1 | 1 | 0 |
| **Total** | **17** | **35** | **90** |

The source gives √90 as 9.4 and rounds it to 9, so the plan is 17 + 9 = 26 (L3968, L3974). This wiki notes that √90 is closer to 9.5, which leaves the rounding unchanged. The widest item dominates and a certain item adds nothing (L3990). The printed text calls the widest item "the first story"; the table shows it is the personal-records row.

## The simpler calculation

With only one estimate per item, "Estimate each story at the 50% level and then set the buffer at half the size of the sum of the 50% estimates" (L4000). Its price is "the serious flaw of not being influenced by the actual uncertainty around the specific user stories in the project" (L4002): two 5-point stories add 2.5 each even if one could reach 100 and the other 10. Cohn prefers the formula, since asking for two estimates is easy (L4004). This wiki notes that the simple rule always yields a buffer of one third of total duration, whatever the risk.

The simple rule is only valid if the estimates really are 50% ones (L4051).

## Guidelines and their conditions

Both come from Leach (2000), via Cohn, as advice with no data given (L4008):

- The formula is most reliable from ten items up. Below that, "you probably shouldn’t be planning with a buffer anyway" (L4010).
- "The project buffer should represent at least 20% of the total project duration" (L4012).

This wiki notes that both of Cohn's worked examples break the first guideline, at six stories and five airport steps. They illustrate the arithmetic only. The second guideline binds on large plans: the formula grows with the square root of the item count, so with identical items whose spread equals their 50% estimate it reaches exactly 20% at 16 items and falls below after that.

## What the formula assumes

The sections below are this wiki's reading.

- **Independence.** The reduction relies on items not going wrong together, which is Cohn's "very little chance that everything will go wrong" (L3935). If many items share one cause, such as one unproven integration or one review gate, the spreads add rather than pool. Table 17.2 would then need up to 18 (35 − 17), not 9. The sign is several wide items whose risk names the same thing. Cohn himself says earlier in the book that software durations are often not independent and that "variations in completion time will not balance out" (L610), which the formula in this chapter does not revisit. This wiki resolves the two by the items: the formula applies to items of unlike kinds, and for a set of similar items ([[similar-tasks-overrun-together]]) the plan treats their spreads as one risk and adds them.
- **The two-sigma label.** Cohn says the 50-90 gap "is about two standard deviations" (L3964). On a normal curve it is about 1.28. The result is unaffected: whatever multiple is used, it cancels, because the same multiple converts the spread into σ and the total σ back into a buffer. The label is loose; the formula stands.
- **Median versus average.** Table 17.2 calls the 50% figure the "average case". On a right-skewed [[completion-time-distribution]] the median sits below the mean, so a sum of 50% figures slightly understates the likely total. The claimed 90% level is an approximation; L4055 says "90–95%" of the same thing.

## A printed discrepancy

Figure 17.4 shows a 53-minute buffer on 70 minutes of 50% estimates and a total of 1:58 (L3948), and the text repeats 1:58 as "nearly an hour shorter" than 2:50 (L3952). The formula on Figure 17.3's spreads gives √2750 ≈ 52.4, which supports 53, but 70 + 53 is 2:03, or 47 minutes shorter. This wiki takes 2:03 as the consistent figure.
