# Sector Threat Profile: SaaS & Technology

**Sector:** SaaS Platforms, Cloud Infrastructure, Developer Tools, Tech Startups
**Threat intel source:** Miasma supply chain, Shai Hulud cloud exfil, CVEs (2026)
**Last updated:** 2026-07

---

## Top Attack Scenarios

### Scenario 1: CI/CD Pipeline Compromise (Miasma / Shai Hulud Model)

**Attack chain:**
```
Compromised npm/GitHub Actions package → CI/CD pipeline injection → Production build infected →
Customer data exfiltration via trojaned SaaS application
```

**Real intel:** Miasma malware (June 2026) compromised npm packages and GitHub Actions runners. Shai Hulud (June 2026) used CI/CD credentials to exfiltrate from Redshift to attacker storage. 76% of SaaS breaches originate from credential theft.

**CB-001 controls activated:**
- **SA-2** (Supply Chain) — CI/CD pipeline scanning, dependency pinning, SBOM generation
- **AC-3** (Access Enforcement) — CI/CD credentials scoped per-environment, rotated every 90 days
- **AU-2** (Log Review) — Pipeline execution audit logging
- **IR-2** (Detection) — Unusual CI/CD deploy patterns (time, frequency, target)

**Detection:**
```kusto
// Unusual CI/CD deployment pattern
CICDAudit | where TimeGenerated > ago(7d)
| summarize DeployCount = count() by Repo, Environment, HourOfDay
| where DeployCount > 20 or HourOfDay < 6 or HourOfDay > 22
```

### Scenario 2: SaaS Tenant Compromise via OAuth Consent Phishing

**Attack chain:**
```
Fake "Zoom connector" app → OAuth consent prompt → User grants email/calendar access →
Attacker reads all email and calendars → Lateral phishing to contacts
```

**Real intel:** OAuth consent attacks against SaaS platforms increased 300% in 2025-2026. Attackers register apps that look like legitimate integrations.

**CB-001:**
- **AC-11** (External System Use) — Block user consent for third-party apps
- **IA-1** (MFA) — Admin consent required for all app grants
- **AU-1** (Logging) — Audit all OAuth consent grants

---

## SOC 2 Readiness Path

| Trust Principle | Key CERG Controls | Evidence Required |
|----------------|-------------------|-------------------|
| Security | AC-1 through AC-7, IA-1, RA-2, SI-1, CM-1 | Access reviews, MFA, AV, config baseline |
| Availability | CP-1, CP-2, CP-4, SC-4 | Backups, DR plan test, uptime metrics |
| Confidentiality | AC-2, AC-4, AC-13, SC-3 | Encryption, access controls, sharing policy |
| Processing Integrity | CM-2, CM-3, PRC-CHG-001 | Change management evidence |

---

## Tool Stack

| Category | Primary | Why |
|----------|---------|-----|
| SIEM | Sentinel | Native SaaS log integration |
| CSPM | Wiz | Agentless, API-native, developer-focused |
| CI/CD Security | GitHub Advanced Security + Trivy | Pipeline-native |
| GRC (SMB) | Vanta | Automated SOC 2 evidence, API-native |
