# Tier 1: Foundations — Scope Guardrails
## Practice Asset — Not a CERG Corpus Document
## Purpose: Explicit "do not do" list that protects Foundations engagements from scope creep

---

## Why Guardrails Exist

Tier 1 engagements are for organizations with 1–15 security FTEs, no operating model, and minimal existing security program. The value is acceleration to a running MVC spine, not coverage of every control family.

Without guardrails, every client meeting becomes a request for a standard they do not need yet, a tool evaluation they are not ready for, or a regulatory package they have not selected. Guardrails let the practitioner say "That's Tier 2 work — here is the entry criteria."

---

## Out-of-Scope: Absolute (Never Included, Regardless of Client Request)

| Item | Rationale | What to Say |
|---|---|---|
| Tool procurement, configuration, or vendor selection | CERG is process-neutral; tools are the client's operational decision. A Foundations client cannot evaluate tools until they know what controls they need. | "Let's get your risk register running first. Tool evaluation happens in Operating Model phase — here is the criteria that will tell you what to buy." |
| Penetration testing or adversarial validation | Requires controls to be implemented and stable before testing has signal value. | "Pen testing pre-controls finds the obvious stuff you already know about. We sequence it after Architecture Review activation in Tier 2." |
| Custom standard or procedure creation beyond the MVC 8 | The MVC is 8 documents. Every new document adds maintenance burden that a 1–15 person team cannot sustain. | "Defer that standard to the standards layer. We adopt the MVC spine first, prove the cadence works, then add standards one at a time." |
| Regulatory operational package implementation (PCI, CUI, SOX, etc.) | A Foundations client with regulatory obligations enters as Tier 3, not Tier 1. If they are Tier 1, they have no active regulatory package. | "Your regulatory packages are Tier 3 scope. We will select the right package in the standards gap analysis. Here is what to expect when we activate it." |
| Metrics dashboard or reporting platform deployment | CERG Metric definitions live in MTR-001. Deploying a BI tool or SIEM dashboard is an operational decision outside CERG scope. | "Metric definitions are in the CERG corpus. We will help you identify which metrics matter for your first board report. The platform is yours to implement." |

---

## Out-of-Scope: Conditional (Included Only if Client Manifests the Readiness Criteria)

| Item | Condition for Inclusion | Default |
|---|---|---|
| Architecture review procedure activation | Client has 2+ projects in flight that need security intake AND the client names an Engineering lead to own the procedure | Deferred to post-Day-30 advisory window |
| Exposure management cycle activation | Client has an existing vulnerability scanner or asset inventory tool with data that can be loaded within 2 hours of practitioner time | Deferred to Day-30 review gate |
| Access management standard adoption | Client has an existing IdP or IAM tool that is operational (not in procurement) | Deferred to Tier 2 scope |
| Role consolidation map refinement beyond first pass | Initial mapping (Day 1–5) produces a workable assignment; refinement requests mean the client needs dedicated pillar leads | Included once, at Day 5. Refinement is Tier 2. |
| Second risk register review cycle | First review cycle completed and documented. Client demonstrates that at least one risk was updated, one risk was closed, and one risk was added between cycles | Included once after Day 30 if first review was completed |

---

## Scope Creep Red Flags (Escalate to Practice Principal)

| Client Behavior | Response |
|---|---|
| Requests penetration testing before risk register exists | Explain sequence; offer Tier 2 upgrade assessment |
| Asks for tool recommendations ("which SIEM should we buy?") | Refer to CERG tool-agnostic design principle; offer tool-evaluation workshop as separate SOW |
| Wants to add regulatory packages mid-engagement | Stop. Re-assess tier assignment. If regulatory scope is new, the engagement may need to re-scope as Tier 3. |
| Refuses to name an Executive Sponsor for policy sign-off | Engagement cannot proceed past Day 5. Escalate to Practice Principal. Policy sign-off is the spine; without it, no adoption has occurred. |
| Treats the risk register as a compliance artifact rather than an operating tool | Reframe during first review. If the register is not updated between cycles, the program is not running — the cadence is not the overhead; it is the program. |

---

## Engagement Closure Criteria (What "Done" Looks Like for Tier 1)

Before handover, verify:

- [ ] Cybersecurity Policy signed by CISO and endorsed by Executive Sponsor
- [ ] `cerg-org-profile.yml` completed and validated against org profile checklist
- [ ] Rendered CERG corpus in client repository — no bare `{{TOKEN}}` strings remain
- [ ] CAT-001 updated with adopted/deferred artifact statuses
- [ ] Role consolidation map documented: named person → canonical roles
- [ ] Risk register has 10+ entries with scoring rationale
- [ ] One risk register review cycle completed and minutes recorded
- [ ] Maturity baseline recorded per MAT-001
- [ ] Improvement register seeded with at least deferred-decision entries
- [ ] Handover memo signed by client
