---
title: Blending Distinct Models in One Bounded Context
category: anti-patterns
summary: The failure of packing linguistically unrelated concepts (e.g. security/permissions) into one domain model — "two models in one", an application silo, a slide toward a Big Ball of Mud — plus the Segregated Core refactoring that recovers a clean Core Domain.
tags: [anti-pattern, failure-mode, blending-models, bounded-context, ubiquitous-language, segregated-core, big-ball-of-mud, case-study]
sources: [book-implementing-ddd-vaughn-vernon]
created: 2026-07-26
updated: 2026-07-26
---

A classic strategic-design failure — and, per Vernon, "one of the basic problems encountered by those
new to DDD" (raw L1814) — is fusing concepts from different [[ubiquitous-language]]s into a single
model. SaaSOvation "blended their core concepts with generic ones, causing the creation of two models
in one" (raw L1782). The concrete case: security and permissions (`User`, `Permission`) baked into a
*Collaboration Context*.

## The symptom

Domain behaviour reaches for the wrong linguistic concepts — querying a **Repository** for a `User`
and checking `Permission` in the middle of core business logic:

```java
public class Forum extends Entity {
    public Discussion startDiscussion(String aUsername, String aSubject) {
        if (this.isClosed()) { throw new IllegalStateException("Forum is closed."); }
        User user = userRepository.userFor(this.tenantId(), aUsername);
        if (!user.hasPermissionTo(Permission.Forum.StartDiscussion)) {
            throw new IllegalStateException("User may not start forum discussion.");
        }
        String authorUser = user.username();
        String authorName = user.person().name().asFormattedName();
        ...
    }
}
```

"This was really bad design. Developers should not have been able to reference User here, let alone
query a Repository for one. Even Permission should have been out of reach." (raw L2185) The distortion
also *hid* a concept the model needed — an `Author` [[value-object]] gathering the three related
attributes — because "Security was on their minds rather than collaboration." (raw L2185)

## Why it is harmful

- **Ripple on change.** "If something changed about the way users and/or permissions worked, a lot or
  all of the model would suffer from the ripple." (raw L1796)
- **Application silo.** Building users/permissions into each system creates "a silo effect in every
  application" — users of one system can't be associated with users of another (raw L2291–L2303). The
  remedy is a centralized identity/access system.
- **Obscured Core Domain and a slide to mud.** Left unchecked it fosters "an undisciplined mindset that
  would allow more tangle to eventually creep in" (raw L1804), heading toward a [[big-ball-of-mud]].

## Root cause — and what does NOT fix it

The cause is missing strategic design: the team's "focus was on the details of [[entity]]s and
[[value-object]]s, which obscured their vision of the bigger picture" (raw L1782). Critically,
modularization alone is insufficient: "While modularization is an essential DDD modeling tool, it
doesn't fix linguistic misalignment." (raw L1802) Moving `User`/`Permission` into a tidy **Module**
would leave the *language* still wrong.

## Remedies (interim → ultimate)

1. **Responsibility Layers [Evans] — rejected.** Pushing security into a lower layer keeps it *in* the
   model, appropriate only for genuinely Core large-scale models. Here the concepts were
   "misappropriated… ones that didn't belong in the [[core-domain|Core Domain]]" (raw L2199).
2. **Segregated Core [Evans] — the chosen interim step.** Exhaustively find all security/permissions
   concerns, refactor them into separate **Modules** in the same model, then require
   [[application-service]] clients to check security *before* calling into the Core. The pattern
   applies "when you have a large Bounded Context that is critical to the system, but where the
   essential part of the model is being obscured by a great deal of supporting capability" (raw L2201).
   The check moves up to the service, which passes a clean `Author` into the domain:

   ```java
   public class ForumApplicationService {
       @Transactional
       public Discussion startDiscussion(String aTenantId, String aUsername,
               String aForumId, String aSubject) {
           Forum forum = this.forum(new Tenant(aTenantId), new ForumId(aForumId));
           Author author = this.collaboratorService.authorFrom(tenant, anAuthorId);
           Discussion newDiscussion = forum.startDiscussion(
                   this.forumNavigationService(), author, aSubject);
           this.discussionRepository.add(newDiscussion);
           return newDiscussion;
       }
   }
   ```

   The `Forum` is now "focused… strictly on collaboration" — taking an `Author`, and publishing a
   `DiscussionStarted` [[domain-event]] (raw L2247–L2281).
3. **Ultimate: a separate Bounded Context.** Identity and access management eventually "occupy a
   context boundary of its own" — the *Identity and Access Context* (product IdOvation), a **Generic
   [[subdomain]]** to the consuming contexts, integrated via standard DDD techniques (raw L2307–L2309).

## The generalizable lesson

The same mistake would recur by melding the collaboration and agile-PM models into one; ProjectOvation
avoided it precisely because the team had learned from the collaboration mess (raw L2333–L2335). The
test is linguistic: every concept in a context must have a linguistic association to that context's
[[ubiquitous-language]]. See also [[bounded-context-sizing]] for the sizing failures that produce
muddled contexts.

## Related

- [[bounded-context]] — the linguistic boundary this violates.
- [[ubiquitous-language]] — the test: every concept must belong to the context's Language.
- [[core-domain]], [[subdomain]] — what gets obscured, and where the misfit concepts belong.
- [[big-ball-of-mud]] — where an unchecked blend leads.
- [[bounded-context-sizing]] — the related sizing failures.
- [[anemic-domain-model]], [[application-service]] — the service-side of the Segregated Core fix.
- [[book-implementing-ddd-vaughn-vernon]] — source summary.
