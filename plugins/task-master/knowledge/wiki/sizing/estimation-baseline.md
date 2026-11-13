---
title: Estimation Baseline
category: sizing
summary: A set of reference stories, agreed in one unit, that gives estimates the same meaning whoever makes them; built from finished work or from a mix of new stories, and then used by analogy.
tags: [method, estimation, relative-estimation, analogy, multi-team]
sources: [cohn-agile-estimating-planning]
created: 2026-11-01
updated: 2026-11-02
---

# Estimation Baseline

An estimation baseline is a small set of stories with agreed sizes in one unit, against which every later estimate is made by analogy. Its purpose is equivalence: a size means the same thing whoever produced it.

Cohn's requirement is that the baseline work "so that an estimate by one team will be similar to that of another team if the other team had estimated the work instead" ([[cohn-agile-estimating-planning]] L4109), and that "Each user story only needs to be estimated by one team, but the estimates should be equivalent regardless of which team estimated the work." (L4109).

## What breaks without it

- **Mixed units cannot be summed.** A remaining total cannot be read if some stories are in ideal days and some in story points (L4107).
- **Same unit, different scale.** Cohn's example is one team estimating a set of stories at 20 points and another estimating the same work at 100 (L4107). Both are internally consistent, and the sum across them means nothing.

The choice between story points and ideal days comes first ([[ideal-days]]), and the baseline then fixes what the chosen unit means. See [[story-points]].

## Two ways to build it

**From past work.** This works only if the estimators have shared a past project. Take finished stories, find two or three that count as one unit, a few that count as two, and so on. "They may identify twenty or so old stories, agreeing upon a new estimate for each, knowing what they now know about the stories." (L4111). The re-estimate uses hindsight on purpose: the baseline records what the work turned out to be, not what it was first guessed to be. This wiki notes that this is not [[re-estimate-when-relative-size-changes]], which raises finished work while open work stays on the old scale; here the set becomes the scale, before estimating starts.

**From new work.** Select an assortment of stories planned for the release and agree estimates on them. "The stories should span a variety of sizes and should be in areas of the situation that most of the estimators can relate to." (L4113).

Either way, the set is then used as the comparison point for separate estimating (L4111). See [[estimation-techniques]] for analogy and [[triangulation]] for comparing against several steps. The figure of about twenty stories is Cohn's for a team-of-teams baseline covering several sizes, not a minimum.

## Sign of violation

These signs are this wiki's.

- A board or plan summing sizes from items estimated in different units.
- Comparable tasks carrying very different sizes depending on who or what estimated them.
- Actual effort per size unit differing systematically across estimators, when compared in history.

Each of these raises a question. The third could also come from a real difference in the work.

## The exception

Cohn allows separate units with no baseline only "when the products being built are truly separate and there is absolutely no opportunity for developers from one team to move onto another" (L4115). He still recommends a baseline there, "as it facilitates communicating about the project" (L4115).

## Trade-off

A baseline costs an agreement step before estimating starts, and with several teams that means representatives or the whole group agreeing. This wiki reads that as worth paying only when more than one estimator contributes to a sum that someone reads. Cohn himself exempts a single team from the multi-team techniques this one belongs to (L4211; the gate is quoted on [[critical-dependency]]).

## Agent executor note

Cohn's mechanism is about several human teams, and the need he names does not arise for one team estimating everything itself. The transfer here is ours: separate agent sessions share no memory of past sizing, so they can behave like separate estimators even inside one small project. On that reading a short reference set of finished tasks, held where every session reads it, does the same job. The hindsight variant suits this setup, since the board's closed tasks supply the material. This has not been tested against a source.
