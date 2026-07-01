# CERG Practice Backlog & Improvement Process v1
| | |
|---|---|
| **Document ID** | CERG-PA-BACK-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | CERG Practice Lead |

**Purpose:** Formalize how the practice captures, prioritises, and implements improvements to CERG.
**Format:** This file is the practice backlog. Entries move through: Backlog → Triaged → In Progress → Shipped.

---

## 1. Improvement Process

```text
DISCOVERY ──> TRIAGE ──> IMPLEMENT ──> SHIP ──> CLOSE
  (anyone)   (2 hours)   (per item)    (push)   (notify)
```

**Sources of improvements:**
- Client debriefs (see `trackers/debrief-protocol-v1.md`)
- Consultant observations during delivery
- Threat intel (new attack patterns that reveal control gaps)
- Regulatory changes (new frameworks, updated requirements)
- Tool stack changes (new tools that warrant opinion updates)
- Upstream CERG changes (content drift from `m0dernz/CERG`)

**Triage criteria:**
| Score | Criteria | Action |
|-------|----------|--------|
| P0 | Critical gap actively exploited in client environments | Fix within 24 hours |
| P1 | Client-facing blocker (missing control, broken guidance) | Fix within current sprint |
| P2 | Quality improvement (better commands, deeper MSP guidance) | Next sprint |
| P3 | Nice to have (additional sector profiles, enhanced automation) | Backlog, no deadline |
| P4 | Upstream contribution candidate | File against m0dernz/CERG |

---

## 2. Active Backlog

### Recently Shipped

| ID | Item | Source | Shipped |
|----|------|--------|---------|
| B-001 | CB-001 TOC anchors fixed: added 6 missing family section headers (6.3-6.8) | B-001 | 2026-06-30 |
| B-002 | SI-7 duplicate removed | B-002 | 2026-06-30 |
| B-007 | 20 standalone Sigma rule files created from detection framework | B-007 | 2026-06-30 |

### P0 — Critical (None currently)

*No items at this priority.*

### P1 — High Priority

| ID | Item | Source | Filed | Assigned | Status |
|----|------|--------|-------|----------|--------|
| B-001 | CB-001 TOC anchors broken (6 anchor_missing warnings) | Validation output | 2026-06-30 | — | **SHIPPED** |
| B-002 | CB-001 has duplicate SI-7 (Information Input Validation + Security Function Verification) | Section numbering | 2026-06-30 | — | **SHIPPED** |

### P2 — Medium Priority (Next Sprint)

| ID | Item | Source | Filed | Notes |
|----|------|--------|-------|-------|
| B-003 | CB-001 controls without `— Tier: Core` suffix (~10 controls lost it during replacement) | Audit | 2026-07 | Cosmetic only — no functional impact |
| B-004 | Add Vanta GRC reference to CB-001 compensating controls section | Tool alignment | 2026-07 | Small update to §7 |
| B-005 | Check upstream CERG for changes (drift since fork) | Process | 2026-06-30 | Merged 6 upstream commits |

### P3 — Backlog

| ID | Item | Priority | Notes |
|----|------|----------|-------|
| B-006 | Add FedRAMP overlay to CB-001 (FedRAMP controls + AC-3 baseline mappings) | P3 | Useful for gov/DIB clients |
| B-007 | Build detection framework rules as Sigma files (not just KQL) | P3 | Platform independence |
| B-008 | Add GDPR-specific control overlay to CB-001 | P3 | EU client readiness |
| B-009 | Build Terraform/IaC examples for cloud controls | P3 | Developer audience |
| B-010 | Crosswalk CB-001 to AWS Security Hub CIS benchmarks | P3 | AWS-native client support |
| B-011 | Create client-facing CERG adoption dashboard (Power BI / Looker) | P3 | Differentiator |
| B-012 | Build POA&M auto-population script from GRC tool output | P3 | Efficiency |
| B-013 | Record CERG training walkthrough video (client onboarding) | P3 | Scale delivery |

### P4 — Upstream Contribution Candidates

| ID | Item | Description |
|----|------|-------------|
| B-101 | Threat Intel Validation sections (already in our fork) | Upstream doesn't have real-threat-intel validation per control |
| B-102 | MSP-specific guidance (our `For the MSP:` sections) | Upstream is engineer-only |
| B-103 | Tool opinion mappings (✅/◐/❌) | Upstream is tool-agnostic |
| B-104 | Compensating control paths per control | Upstream doesn't address this |

---

## 3. Sprint Cadence

| Activity | Cadence | Participants | Duration |
|----------|---------|-------------|----------|
| Backlog review | Weekly (Monday) | Practice lead, delivery leads | 30 min |
| Sprint planning | Bi-weekly | Practice lead + consultant(s) | 1 hour |
| Implementation | As available | Assigned consultant | Variable |
| Retrospective | Monthly | All consultants | 30 min |
| Practice standup | Daily (async) | All consultants | Slack thread |

---

## 4. Implementation Workflow

### Ticketing

- Each backlog item gets a GitHub Issue in `cragin-sec/CERG`
- Issue template: `Purpose / Impact / Effort estimate / Controls affected / Files to change`
- Label with priority (P0-P4) and domain (controls, automation, docs, tooling)

### Branching

```bash
# For P0-P1 fixes (fast path)
git checkout main
# Fix → commit → push (single file, direct to main)

# For P2+ improvements (cross-cutting)
git checkout -b feature/descriptive-name
# Work → commit → push → PR → merge
```

### Verification

Before closing any backlog item:
1. `python3 tools/cerg-validate.py` — zero errors required
2. `python3 tools/regenerate-machine-readable.py` — if metadata changed
3. `python3 tools/regenerate-llm-index.py` — if docs added/removed
4. If new automation: `python3 {script}` — confirm output
5. Update the backlog in this file — move to SHIPPED

---

## 5. Shipping Criteria

A backlog item is **done** when:

- [ ] Code/doc change committed and pushed
- [ ] Validation passes (0 errors)
- [ ] Machine-readable artifacts regenerated (if applicable)
- [ ] Backlog entry moved to SHIPPED with date and commit hash
- [ ] (Optional) Team notified via practice channel

---

## 6. Shipped Items

| ID | Item | Shipped | Commit | Notes |
|----|------|---------|--------|-------|
| — | Initial CB-001 100 controls | 2026-06-27 | 29c4558 | Expanded from 40 to 100 |
| — | Threat intel validation | 2026-06-27 | 4ec2ed5 | 6 controls validated against feed |
| — | Control deepening (AC-1 through AC-7) | 2026-06-27 | 8cb9d49 | LAPS, PIM, ZTNA, MAM |
| — | Remaining control deepening | 2026-06-27 | 81e5510 | 45 controls across all families |
| — | Corpus consolidation | 2026-06-27 | 8c34b7c | IMP-merged, AI/RM merged, shelfware removed |
| — | Tool matrix v1 + GRC rollout plan | 2026-06-27 | 8c34b7c | Full stack opinions |
| — | SN GRC accelerator + playbook + automation + detection mapping | 2026-06-27 | 60ee605 | 9 files, 1349 lines |
| — | Sector profiles updated with threat intel | 2026-06-27 | Current | Healthcare, financial, energy, gov, SaaS |
| — | MSP runbook pack v1 | 2026-06-27 | Current | Multi-tenant playbook |

---

## 7. File Map

| File | Purpose |
|------|---------|
| This file (`backlog-v1.md`) | Formal backlog, shipping criteria, shipped items |
| `trackers/engagement-status-schema-v1.md` | Per-engagement status tracking |
| `templates/client-improvement-register-v1.md` | Client-specific improvement register (shared with client) |
| `trackers/debrief-protocol-v1.md` | Engagement debrief for practice improvement |

---

## Document Control

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | 2026-07 | CERG Practice | Initial backlog and improvement process |
