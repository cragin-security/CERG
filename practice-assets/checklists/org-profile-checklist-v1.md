# CERG Organization Profile Checklist
## Practice Asset — Not a CERG Corpus Document
## Purpose: Token-by-token validation before running `cerg-render.py`

---

## Instructions

Complete every row before running `cerg-render.py`. Unresolved tokens produce rendering errors; stale defaults produce a corpus that reads like someone else's organization. Both are unacceptable in a client engagement.

The checklist mirrors `CERG-GOV-VAR-001 §4` (Token Catalog). Each token has a validation rule and a common error to avoid.

---

## Section 1: Organization Identity

| # | Token | Client Value | Validation Rule | Common Error |
|---|---|---|---|---|
| 1 | `{{ORG_NAME}}` | | Full name used in prose — not necessarily legal name | Leaving the V1 reference value ("Northwind Energy") — most common mistake |
| 2 | `{{ORG_LEGAL_NAME}}` | | Full legal entity exactly as it appears in contracts | Using a DBA or trade name without legal verification |
| 3 | `{{ORG_SHORT_NAME}}` | | 2–6 character abbreviation; used in dashboards | Making it too long for header space; or including "Inc." |
| 4 | `{{ORG_SECTOR}}` | | Must match one of 8 sector profiles in practice-assets | Generic "technology" when the sector is "healthcare" — changes threat model, metrics, and overlay selection |
| 5 | `{{ORG_CONTENT_REPO}}` | | Valid HTTPS URL to client's CERG repository | Broken link that CI doesn't catch |

---

## Section 2: Program Identity

| # | Token | Client Value | Validation Rule | Common Error |
|---|---|---|---|---|
| 6 | `{{PROGRAM_NAME}}` | | Default "CERG" unless client has renamed their security program | Renaming just because — the original "CERG" has recognition value |
| 7 | `{{PROGRAM_ACRONYM}}` | | Default "CERG" — must match PROGRAM_NAME acronym | Mixing program name and acronym |

---

## Section 3: Scale and Structure

| # | Token | Client Value | Validation Rule | Common Error |
|---|---|---|---|---|
| 8 | `{{TOTAL_EMPLOYEES}}` | | Approximate integer. If between bands, round up | Exact figure that becomes outdated between render and policy sign-off |
| 9 | `{{PROTECTED_POPULATION}}` | | Total identities + devices + access relationships | Using headcount alone (a 500-employee company with 3,000 contractors and 10,000 devices is not 500) |
| 10 | `{{CERG_TEAM_SIZE}}` | | Security team FTE count | Counting open reqs that may not be filled |
| 11 | `{{ENG_STAFF}}` | | Engineering pillar headcount | Including DevOps engineers who are not security-engineer roles |
| 12 | `{{RISK_STAFF}}` | | Risk pillar headcount | Including governance staff in risk count |
| 13 | `{{GOV_STAFF}}` | | Governance pillar headcount | Excluding document control and evidence librarian roles |
| 14 | `{{SCALE_TIER}}` | | `small` / `mid` / `large` — must match team size ranges | `small` for a 100-person team; `large` for a 5-person team (changes how the corpus reads about role consolidation) |

---

## Section 4: Oversight and Standing Teams

| # | Token | Client Value | Validation Rule | Common Error |
|---|---|---|---|---|
| 15 | `{{COG_NAME}}` | | Name of the Cyber Oversight Group or equivalent body | Fictional name with no actual meeting cadence |
| 16 | `{{IR_TEAM_NAME}}` | | Name of standing incident response team | Using a vendor name (MSSP) that changes annually |
| 17 | `{{EXEC_BODY_NAME}}` | | Board or executive body that endorses policy | Name that doesn't match the org chart (audit committee ≠ board of directors) |

---

## Section 5: Regulatory Context

| # | Token | Client Value | Validation Rule | Common Error |
|---|---|---|---|---|
| 18 | `{{REGULATORS}}` | | Comma-separated list of all applicable regulators | Omitting a regulator that applies but the client hasn't prioritized yet (creates silent gap) |
| 19 | `{{PRIMARY_REGULATOR}}` | | The single most consequential regulator | Choosing "None" when the client is a publicly-traded energy company that stores credit cards |

---

## Section 6: Contact and Control

| # | Token | Client Value | Validation Rule | Common Error |
|---|---|---|---|---|
| 20 | `{{SECURITY_CONTACT}}` | | Published email for security matters | Personal email or shared mailbox without an SLA |
| 21 | `{{DOC_CONTROL_CONTACT}}` | | Published email for document control questions | Same as security contact — these should be different roles |
| 22 | `{{ADOPTION_DATE}}` | | Date the client officially adopts CERG | Date of engagement start instead of policy sign-off (engagement start is advisory; sign-off is adoption) |

---

## Validation Gate

Before running `cerg-render.py`:

- [ ] All 22 tokens have client values filled (mandatory)  
- [ ] No token contains the V1 reference value ("Northwind Energy", "14,000", "NERC-CIP")  
- [ ] `{{ORG_SECTOR}}` maps to an existing sector profile in `practice-assets/sector-profiles/`  
- [ ] `{{REGULATORS}}` includes only frameworks the client has confirmed in writing  
- [ ] `{{SCALE_TIER}}` is consistent with `{{CERG_TEAM_SIZE}}`  
- [ ] Client has reviewed and signed off on all token values  
- [ ] Profile file saved as `cerg-org-profile.yml` in root (not a copy in a subdirectory)  

## Post-Render Check

- [ ] Rendered corpus reads as if written for this client (not "Northwind Energy with find-and-replace")  
- [ ] All 22 tokens appear substituted — no bare `{{TOKEN}}` strings remain  
- [ ] Sector-specific examples in the corpus match the client's industry  
- [ ] Scale figures read realistically for the client's team size  
- [ ] Regulatory examples reference the correct operational packages  
