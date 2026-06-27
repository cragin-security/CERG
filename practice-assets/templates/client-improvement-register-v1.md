# Client Improvement Register Template
## Practice Asset — Not a CERP Corpus Document
## Purpose: Bridges handover to new scope; tracks open items with owners and target dates

---

## Template

| # | Item | Type | Owner | Target Date | Status | Notes |
|---|------|------|-------|-------------|--------|-------|
| 1 | | | | | Open / In Progress / Complete / Deferred | |
| 2 | | | | | Open / In Progress / Complete / Deferred | |
| 3 | | | | | Open / In Progress / Complete / Deferred | |

## Item Types

| Type | Definition | Example |
|---|---|---|
| Adoption Gap | A CERG artifact that was deferred during engagement scope | "STD-AC-001 not adopted — session recording not yet implemented" |
| Control Gap | A control that is not implemented or not evidenced | "No file integrity monitoring on CDE systems" |
| Process Gap | A procedure that exists but is not operational | "Architecture review procedure created but no projects have been routed through it" |
| Evidence Gap | An evidence artifact that is stale or missing | "Last access recertification was 8 months ago; 6-month cadence required" |
| Regulatory Gap | A regulatory requirement without documented coverage | "PCI DSS Req 10.4.1.1 — automated log review not configured for all CDE components" |
| Tooling Gap | A capability that requires tooling not yet deployed | "No ASV scanning vendor engaged for quarterly external scans" |
| Training Gap | A role that has not completed required training | "OT operators have not completed annual security awareness training" |
| Deferred Decision | A decision that was explicitly deferred during the engagement | "Regulatory overlay selection pending legal applicability review" |

## Seeding Rules

- Every deferred standard or procedure from the CAT-001 adoption log gets an improvement register entry
- Every scope item marked "out of scope" in the engagement scope document that the client wants to revisit gets an entry
- Every finding from the maturity baseline that was not remediated during the engagement gets an entry
- No entry should be created without a named owner and target date — "TBD" is not an owner

## Review Cadence

| Event | Who | When |
|---|---|---|
| Register seeded | Practice Engagement Lead | At handover |
| First client review | Client Governance | Within 30 days of handover |
| Quarterly review | Client Governance | Quarterly |
| Closure | Client | On evidence of completion |

## Closure Criteria

An item is closed when:
1. The owner confirms the work is complete
2. Evidence of completion is produced (configuration export, policy signed, training records, scan report, etc.)
3. The improvement register is updated with the closure date and evidence reference
