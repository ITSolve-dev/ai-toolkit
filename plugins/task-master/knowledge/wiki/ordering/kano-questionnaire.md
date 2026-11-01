---
title: Kano Questionnaire
category: ordering
summary: To place a feature on the Kano model, ask users how they would feel if it were present and if it were absent, cross-reference the two answers into one category, and read the distribution across some 20-30 users; two peaks in one row mean two populations, not a tie.
tags: [method, ordering, prioritization, value, kano]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-01
---

# Kano Questionnaire

This procedure replaces a guess about a feature's [[kano-model]] category with an answer from users. The source ranks the two ways plainly:

> The easiest way to make use of a Kano model on an agile project is to think about each theme and make an educated guess about the type of each. A much better way, however, is to speak with customers or users in order to truly determine the type of each theme.
>
> — [[cohn-agile-estimating-planning]], L2423

## Procedure

1. **Write two forms of one question per feature.** The functional form asks how the user would feel if the feature were present, the dysfunctional form how they would feel if it were absent: "If you can graph a swimmer’s times in an event over the past season, how do you feel?" and its "cannot" twin (L2447-L2449).
2. **Offer the same five answers to both:** I like it that way; I expect it to be that way; I am neutral; I can live with it that way; I dislike it that way (L2427-L2435).
3. **Cross-reference each user's pair** in the table below, so that "a prospective user’s responses can be reduced to a single meaning" (L2479).
4. **Aggregate across users** into a percentage distribution per feature, and read the category from it (L2490).
5. **Where a row has two high values, split the respondents** before reading it (L2502-L2506).

## The cross-reference table

Rows are the answer to the functional question, columns the answer to the dysfunctional one. M is must-have, L linear, E exciter, I indifferent, R reverse, Q questionable.

| Functional / Dysfunctional | Like | Expect | Neutral | Live with | Dislike |
|---|---|---|---|---|---|
| Like | Q | E | E | E | L |
| Expect | R | I | I | I | M |
| Neutral | R | I | I | I | M |
| Live with | R | I | I | I | M |
| Dislike | R | R | R | R | Q |

This table is rebuilt from the extracted text of Figure 11.3 (L2488), not from an image. One cell can be checked against the prose: expect plus dislike gives must-have (L2479-L2483).

The source defines Q by example, where a user likes having a feature and also likes not having it: "it is possible for a user to give inconsistent responses" (L2477). I and R appear only as labels. This wiki reads I as a user who does not care either way and R as a user who prefers the feature absent, and the source says nothing on what to do with either. A large I share is, on this wiki's reading, a reason to ask whether the feature should be built at all.

## Worked distribution

Table 11.1 (L2494-L2498), percentages of respondents:

| Theme | E | L | M | I | R | Q | Category |
|---|---|---|---|---|---|---|---|
| Graph event times | 18.4 | 43.8 | 22.8 | 12.8 | 1.7 | 0.5 | Linear |
| Can upload photos | 8.3 | 30.9 | 54.3 | 4.2 | 1.4 | 0.9 | Must-have |
| Post autobiographical profile | 39.1 | 14.8 | 36.6 | 8.2 | 0.2 | 1.1 | Exciter / Must-have |

The category is read "From observation of this table" (L2490), and no cut-off is given. The figures are the book's illustration and not a measurement.

## How many users

The figure is that "you may need to survey as few as 20–30 users to accurately prioritize requirements" (L2423), cited to Griffin and Hauser (1993). The chapter does not give the setting that produced it, so this wiki holds it as an order of magnitude only. Splitting by sub-population divides the same respondents, so the number that suffices for one homogeneous group does not obviously suffice for each of several. That caution is ours.

## Failure modes

- **Two peaks read as one category.** The sign is a row with two high values, as with the profile at 39.1 and 36.6. The source's reading: "This indicates that different types of customers and users have different expectations." (L2502). This wiki adds that taking the top value would file the profile as an exciter while over a third of respondents treat it as mandatory. The remedy is to analyse by a factor that differentiates respondents, such as company size, job role or industry segment (L2506).
- **Asking only about presence.** This wiki's reading is that almost any feature is liked when offered, so the dysfunctional form is what separates a must-have from an exciter. The source's own wording is that "We need a way for looking at both answers simultaneously" (L2477). The sign is a questionnaire, or a value rating, with no question about absence. See [[relative-penalty]].
- **A guess recorded as a measurement.** The source accepts the educated guess as the easy way. The sign, on this wiki's reading, is a category on a task with no note of where it came from; the origin should be stated.

## Defects in the source's text

The chapter's example was renamed incompletely, and a reader checking citations will meet the leftovers. The prose says "reviews on the website are a threshold feature" (L2483), then "reviews are a one-dimenstional (linear) feature and that shipping options are a mandatory (threshold) feature" (L2490), and later refers to "detailed photos" (L2502). No such rows exist in the table. This wiki reads them as Graph event times, Can upload photos and Post autobiographical profile, by position and by the Category column. Table 11.2 also disagrees with this table about photos: see [[relative-weighting]].

## Cost

The source calls this "surprisingly easy because it can be done with a written questionnaire" (L2423). This wiki reads that as a claim about effort, assuming users can be reached. It costs a pair of questions per feature for each respondent. It yields a category only: nothing in it sees cost, so it cannot rank within a category. [[kano-or-relative-weighting]] says when to pay for it.

## Agent executor note

The plugin can draft the question pairs and tabulate answers. It cannot supply the answers. An agent answering in the users' place produces the educated guess and not the survey, and should be labelled as a guess. For a few people steering an agent the method holds only where a population of users exists to ask, which the charter's scale does not guarantee.
