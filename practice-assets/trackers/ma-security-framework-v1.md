# CERG M&A Security Integration Framework v1
## Practice Asset — Not a CERP Corpus Document
## Purpose: Pre-acquisition assessment, 90-day integration, carve-out security, divestiture data sanitization

---

## Engagement Context

M&A security is the highest-stakes work most security teams never practice. The acquiring organization inherits all of the target's security debt on day one. This framework provides the checklist, timeline, and control expectations for each phase.

---

## Phase 1: Pre-Acquisition Assessment (Before Close)

### Minimum Viable Assessment

For acquisitions under 500 employees or under $50M deal value:

| Area | Question | Evidence |
|---|---|---|
| Asset inventory | Does the target have a current inventory of all systems? | CMDB export or equivalent |
| Identity | Is there an IdP with MFA? | IdP policy export, MFA enrollment rate |
| Endpoint protection | Is EDR deployed on all endpoints? | EDR coverage report |
| Vulnerability management | Are systems patched on a defined schedule? | Patch report, vulnerability scan |
| Backup | Are backups running and tested? | Backup report, restore test evidence |
| Incident response | Is there an IR plan? Last tested? | IR plan, exercise records |
| Regulatory scope | Is the target subject to any regulatory framework? | List of applicable frameworks |
| Contracts | Are there vendor contracts that need security review? | Vendor inventory, contract security clauses |

### Full Assessment (Any deal >$50M or >500 employees)

Include all minimum assessment items plus:

| Area | Question | Evidence |
|---|---|---|
| Penetration testing | Has the target had an external pen test in the last 12 months? | Pen test report, remediation evidence |
| Access recertification | Are access reviews conducted quarterly? | Last 2 recertification reports |
| Supply chain | Are top 10 vendors assessed? | Vendor assessment reports |
| Code security | Is SAST/DAST in the CI/CD pipeline? | SAST/DAST scan results |
| Cloud security | Is CSPM deployed? | CSPM compliance score |
| Logging | Are logs sent to a SIEM? | SIEM source inventory |
| Incident history | Any material incidents in the last 24 months? | Incident records, post-mortems |

---

## Phase 2: Day 1–30 — Security Hold

### Immediate Actions (Close Day)

| Priority | Action | Owner |
|---|---|---|
| Critical | Block all unknown inbound network access to target network | Network Engineering |
| Critical | Disable any local admin accounts not explicitly required | Identity Team |
| Critical | Require MFA on all target systems — use acquiring org's IdP | Identity Team |
| High | Deploy EDR agent to target endpoints | Endpoint Engineering |
| High | Add target IP ranges to vulnerability scanner | Vulnerability Management |
| High | Review and restrict target vendor remote access | Vendor Risk |

### First 30 Days

| Week | Action | Owner |
|---|---|---|
| 1 | Asset discovery: identify every system in the target environment | Asset Management |
| 1 | User account inventory: identify every account, disable orphans | Identity Team |
| 2 | Vulnerability baseline: run full scan of target environment | Vulnerability Management |
| 2 | Deploy logging to acquiring org's SIEM | Detection Engineering |
| 3 | Run backup verification on target critical systems | Backup Team |
| 3 | Review target IR plan; merge into acquiring org's plan | IR Team |
| 4 | Complete risk register for target environment | Risk Team |

---

## Phase 3: Day 31–90 — Integration

| Activity | Timeline | Owner |
|---|---|---|
| Migrate target identity to acquiring org's IdP | Day 31–60 | Identity |
| Migrate endpoints to acquiring org's MDM | Day 31–60 | Endpoint |
| Migrate email/colaboration platforms | Day 31–60 | IT |
| Apply DISH baseline to target servers | Day 31–90 | Engineering |
| Implement network segmentation for integrated environment | Day 31–90 | Network |
| Run first access recertification for target users | Day 60 | Identity |
| Run first vulnerability scan with acquiring org's tooling | Day 60 | VM |
| Complete first full evidence collection cycle | Day 90 | Governance |

---

## Phase 4: Carve-Out Security

When divesting a business unit or subsidiary, security controls must be extracted without leaving residual access.

| Action | Owner | Timeline |
|---|---|---|
| Inventory all systems going to the buyer | Asset Management | T-60 days |
| Remove acquiring org's identities from carved-out systems | Identity | T-30 days |
| Disable cross-org federation | Identity | T-30 days |
| Extract and sanitize data going to buyer | Data Governance | T-30 days |
| Run pen test from buyer's perspective | Offensive Security | T-14 days |
| Document remaining shared controls | Governance | T-7 days |
| Verify no residual access 30 days post-close | Identity | T+30 days |

---

## Phase 5: Divestiture Data Sanitization

| Data Type | Sanitization Required | Verification |
|---|---|---|
| Customer data sharing | Remove all cross-entity data sharing agreements | Legal review |
| Shared infrastructure credentials | Rotate all shared credentials | Secrets manager audit |
| Log data containing carved-out entity metrics | Separate or pseudonymize | Log retention policy update |
| Vendor contracts referencing carved-out entity | Update or terminate | Contract review |
