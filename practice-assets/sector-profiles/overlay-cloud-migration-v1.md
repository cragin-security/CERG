# CERG Cloud Migration Security Overlay v1
## Practice Asset — Not a CERP Corpus Document
## Purpose: Security review gates, IAM migration sequencing, and logging continuity during cloud migration

---

## Engagement Context

Cloud migrations create a unique security challenge: for a period of weeks to months, operations run across two environments simultaneously. Controls must operate in both, and the cutover must not create a security gap.

---

## Migration Security Gates

Every migration phase includes a security gate. The gate requires sign-off before the next phase begins.

| Gate | Phase | Security Requirements | Sign-Off |
|---|---|---|---|
| G1 | Planning | Network architecture approved, IAM model designed, logging architecture designed | Engineering Pillar Leader |
| G2 | Foundation | Landing zone deployed, IaC scanning passing, network baseline scanned | Engineering Pillar Leader |
| G3 | Workload Migration | DISH baseline applied to migrated systems, SIEM receiving logs, vulnerability scanner covering new IPs | Risk Pillar Leader |
| G4 | Cutover | MFA verified on migrated systems, backup tested, no critical vulnerabilities open >7 days | CISO |
| G5 | Hypercare | Evidence library updated, risk register reviewed, access recertification completed for migrated scope | Governance Pillar Leader |

---

## IAM Migration Sequencing

| Phase | Identity Actions | Key Risk |
|---|---|---|
| Planning | Document identity topology (on-prem IdP → cloud IdP). Plan sync schedule. Design hybrid identity model. | Incomplete identity topology — missing shadow IT identities |
| Pilot | Migrate 1 business unit. Verify MFA, conditional access, and JIT elevation in cloud IdP. | Pilot users cannot authenticate during migration window |
| Rollout | Migrate remaining users in waves. Maintain sync until all users are migrated. | Desync between on-prem and cloud during migration window |
| Cutover | Disable on-prem IdP for migrated users. Keep break-glass on-prem access. | Fallback required if cloud IdP has outage during first week |
| Steady-state | Remove on-prem IdP dependency. Retain break-glass accounts. | Orphan on-prem accounts not disabled |

### IAM Migration Checklist

- [ ] Cloud IdP configured with MFA before any user migration begins
- [ ] Conditional access policies tested with pilot group
- [ ] Legacy authentication blocked in cloud after all users migrated
- [ ] Service accounts migrated with secrets rotated
- [ ] Break-glass cloud accounts created and stored in vault
- [ ] On-prem AD decommissioned or reduced to read-only after 90 days

---

## Logging Continuity

| Phase | Logging Requirements | Tooling |
|---|---|---|
| Planning | Log source inventory including both on-prem and cloud targets | SIEM source inventory document |
| Migration | Dual logging: both on-prem and cloud systems send to SIEM simultaneously | SIEM with dual collectors |
| Cutover | Confirm all migrated systems are sending logs to the cloud SIEM before disabling on-prem | SIEM query: sources in last 24 hours |
| Post-migration | Decommission on-prem log collectors. Update SIEM source inventory. | Source inventory cleanup |

### Minimum Log Sources for Migrated Systems

| Source | Criticality | Verification |
|---|---|---|
| Cloud resource logs (Azure Diagnostic, AWS CloudTrail, GCP Audit Logs) | Mandatory | SIEM shows logs for all in-scope resources |
| Cloud IdP logs (Entra ID, Okta) | Mandatory | SIEM shows sign-in logs for all migrated users |
| Cloud workload logs (VM, container, serverless) | Mandatory | SIEM shows logs from all migrated compute |
| Network security logs (Cloud firewall, WAF, NSG flow logs) | Mandatory | SIEM shows flow logs for all subnets |
| PaaS/SaaS logs | Recommended | As available per platform |

---

## Security Tool Migration

| Tool Category | Migration Pattern | Risk Window |
|---|---|---|
| EDR | Deploy cloud-native EDR agent before decommissioning on-prem agent | Dual-agent during migration |
| Vulnerability scanner | Add cloud IP ranges to scanner before migration | Orphan VMs without scanning coverage |
| CSPM | Enable CSPM on cloud subscription as first action | Misconfigured cloud resources without detection |
| Backup | Migrate backup to cloud-native tool before cutover | Systems without backup during migration window |
| Patch management | Configure cloud-native patching (Azure Update Manager, AWS Systems Manager) | Unpatched systems during transition |

---

## Migration Risk Register

Common risks to add to the risk register before starting a cloud migration:

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Cloud resource misconfiguration exposed to internet | High | High | CSPM enabled on subscription before any resources deployed |
| User authentication failure during cutover | Medium | High | Pilot group migration first. Keep on-prem IdP active during rollback window. |
| Log gap between on-prem and cloud | Medium | Medium | Dual logging: both environments send to SIEM simultaneously |
| Backup misconfiguration for new cloud resources | Medium | High | Test restore for first migrated workload before full cutover |
| Unpatched migrated workload | High | Medium | Run vulnerability scan on migrated resources within 24 hours of cutover |
| Vendor access not migrated | Low | Medium | Document all vendor remote access paths; migrate with workload |
