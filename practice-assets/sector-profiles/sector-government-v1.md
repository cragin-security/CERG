# Sector Threat Profile: Government & Defense (CMMC)

**Sector:** Federal/State/Local Government, Defense Contractors (DIB), National Security
**Threat intel source:** CMMC enforcement, CISA advisories, nation-state campaigns (2025-2026)
**Last updated:** 2026-07

---

## Top Attack Scenarios

### Scenario 1: CUI Exfiltration via Supply Chain (CMMC Scope)

**Attack chain:**
```
Third-party subcontractor compromise → Access to prime contractor's CUI repository →
Bulk CUI exfiltration over 6 months → Undetected until GAO audit
```

**Real intel:** GAO report (June 2026) highlights CMMC rollout risks as nation-state attacks target defense contractors. CMMC has moved from planning to enforcement — contractors are losing contracts for non-compliance. 2025 saw multiple DIB contractors compromised via subcontractor attack paths.

**CB-001 controls activated:**
- **SR-1** (Vendor Risk Assessment) — Tier all subcontractors handling CUI
- **SA-2** (Supply Chain) — SBOMs for all software in CUI-scoped systems
- **CM-4** (Inventory) — Complete CUI-scoped system inventory
- **PL-2** (System Security Plan) — Current SSP for every CUI system

**Detection:**
```kusto
// Bulk file access outside business hours
FileAuditLog | where SensitivityLabel == "CUI"
| summarize FileCount = count(), TotalSizeMB = sum(FileSize)/1e6 by UserPrincipalName, bin(TimeGenerated, 1h)
| where FileCount > 100 or TotalSizeMB > 500
```

**Tabletop:**
- Inject: "Your DCMA CMMC assessment is scheduled in 6 weeks. During a pre-assessment walkthrough, you discover that a subcontractor with access to CUI has no current SSP and no evidence of annual security training."
- Questions: What's your immediate action? Do you need to file a CUI incident report? Can you pass the assessment?

### Scenario 2: Nation-State Targeting of Gov Email (CL-STA-1062 / Russian Campaigns)

**Attack chain:**
```
Spear phishing to procurement/scheduling staff → Credential harvesting → Mailbox access →
Read sensitive correspondence → Establish persistent mailbox monitoring
```

**Real intel:** CL-STA-1062 (June 2026) targets SE Asian government systems. Russian Turla STOCKSTAY backdoor (2026) targets Ukraine government systems. Five Eyes warns of AI-accelerated government targeting.

---

## Testing Procedures

| Scenario | Procedure | Cadence |
|----------|-----------|---------|
| 1 (CUI exfil) | Quarterly CUI access review + bulk download alert test | Quarterly |
| 2 (Gov spearphish) | Government-specific phishing simulation + incident response walkthrough | Monthly |
| CMMC gap assessment | Annual SPRS score review + full mock assessment | Annual |

---

## CMMC Readiness: Fastest Path

| Level | Requirements | CERG Controls | Timeline |
|-------|-------------|---------------|----------|
| L1 (Basic) | 17 practices | CB-001 AC-1, AC-2, IA-1, AU-1 | 2 weeks |
| L2 (Intermediate) | 110 practices + assessment | 50 CB-001 controls | 3-6 months |
| L3 (Advanced) | L2 + additional | 75+ CB-001 controls + internal assessor | 6-12 months |
| L4+ | L3 + external assessment | All 99 controls + CMMC CSP | 12-18 months |

---

## Tool Stack Preference (FedRAMP Authorized)

| Category | Primary | FedRAMP Status |
|----------|---------|----------------|
| SIEM | Splunk Gov / Sentinel (GCC High) | FedRAMP High |
| EDR | CrowdStrike (IL5) / SentinelOne (FedRAMP) | FedRAMP Moderate |
| GRC | ServiceNow GRC (FedRAMP) | FedRAMP Moderate |
| Cloud | AWS GovCloud / Azure Government | FedRAMP High |
| Identity | Entra ID (GCC High) | FedRAMP High |
