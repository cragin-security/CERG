# Sector Profile: Government / Federal (Non-DoD)
## Practice Asset — Not a CERP Corpus Document

---

## Default Tier
Tier 3 (Compliance-to-Operations). Federal agencies and state governments have FISMA, FedRAMP, or state-specific compliance obligations.

## Default Overlays
CUI (if handling CUI). NIST 800-53 as baseline (not an overlay — it is the default for federal).
Privacy (if handling PII).

## Regulatory Routing

| Trigger | Package |
|---|---|
| Federal agency subject to FISMA | NIST 800-53 is the baseline; CERG CB-001 covers this directly |
| FedRAMP-authorized or pursuing authorization | Practice FedRAMP overlay adapter |
| Handles CUI | `CERG-PLN-CUI-001` |
| State government with PII | `CERG-PLN-PRIV-001` + state-specific laws (CA, NY, TX, etc.) |
| International government (non-US) | Practice-specific engagement; no standard overlay applies |

## Key Adaptation Guidance

| Token | Guidance |
|---|---|
| `{{ORG_SECTOR}}` | "Government / Federal" — differentiate: US Federal agency ≠ State government ≠ international government |
| `{{REGULATORS}}` | Federal agencies report to OMB; state to state legislature; no single regulator |
| `{{SCALE_TIER}}` | Government organizations often have large IT/Security teams by headcount but lower security maturity due to civil service constraints and procurement timelines |
| `{{EXEC_BODY_NAME}}` | Federal: "CIOC" or "Information Security Council"; State: "IT Governance Board" or "CIO Steering Committee" |

## Metric Priorities

| Metric | CERG Reference | Why It Matters for Gov |
|---|---|---|
| FISMA compliance rating (low/moderate/high) | CA-2, PM-14 | OMB reports FISMA metrics annually to Congress |
| Plan of Action and Milestones (POA&M) closure rate | MTR-001 RM-001 | OMB tracks POA&M aging as a key FISMA metric |
| Incident reporting to US-CERT | PRC-IR-002 | Statutory requirement; FISMA requires reporting within timeframes |
| Authority to Operate (ATO) currency | CA-2 | Expired ATOs for federal systems are a compliance violation |

## Key CERG Artifacts to Emphasize

| Artifact | Why |
|---|---|
| CB-001 (NIST 800-53 baseline) | Federal default — no overlay needed; the baseline IS the requirement |
| STD-CUI-001 | CUI handling for any federal data that is not classified |
| PRC-AUD-001 | Audit management for OIG, GAO, or state auditor reviews |
| PRC-VM-001 | FISMA vulnerability scanning requirements; CDM integration |
| PRC-IR-002 | US-CERT incident reporting; federal-specific notification requirements |

## Common Engagement Mistakes

- Treating federal security as unique (NIST 800-53 is the same framework CERG is built on; the adaptation is in reporting, not controls)
- Assuming government procurement cycles don't affect engagement scope (evidence collection happens quarterly; tool procurement takes 12-18 months; plan accordingly)
- Not accounting for CDM (Continuous Diagnostics and Mitigation) program requirements — federal clients have CDM sensors and dashboards that produce mandatory evidence
- Confusing ATO (Authority to Operate) with an audit — ATO is the official authorization; it requires a risk acceptance decision at the Authorizing Official level, not just control compliance
