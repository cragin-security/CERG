# CERG GRC Rollout Guide

## Wiring ServiceNow GRC (or Vanta) into Your CERG Program

| | |
|---|---|
| **Document ID** | CERG-OPN-TOOLS-002 |
| **Version** | 1.0.0 |
| **Status** | Draft |
| **Classification** | Public |
| **Owner** | Consulting Practice Lead |
| **Parent Policy** | CERG-POL-001 |
| **Review Cycle** | Quarterly |
| **Frameworks** | CERG 100-Core · NIST 800-53r5 · CIS Controls v8 |
| **Regulations** | CMMC L2 · SOX ITGC · PCI DSS v4 |
| **Environments** | IT · Cloud · SaaS |

---

## Purpose

This guide provides copy-paste instructions for deploying a GRC platform as the CERG anchor. It covers two paths:

1. **Enterprise / MSP path:** ServiceNow GRC with CERG control import, evidence automation, and audit reporting
2. **SMB path:** Vanta with CERG control mapping for compliance-only use cases

Both paths assume you've read the [Opinionated Tool Matrix](opinionated-tool-matrix-v1.md) and chosen your stack.

---

## Path 1: ServiceNow GRC (Enterprise / MSP)

### 1.1 Prerequisites

- ServiceNow instance with GRC: Advanced plugin (com.snc.governance_advanced)
- Admin or snc_grc_admin role
- Access to import sets and transform maps
- CERG 100-Core Control Baseline (see [CERG-GOV-CB-002](../../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md))

### 1.2 Control Import

ServiceNow GRC uses the **Policy and Compliance** module. Controls live in the `sn_compliance_control` table.

#### Step 1: Load the CERG Control Framework

Navigate to **Policy and Compliance > Administration > Control Objectives** and create a new framework:

```
Name: CERG 100-Core
Version: 1.0
Description: CERG 100-Core Control Baseline — practice-hardened fork
Source: cragin-security/CERG
```

#### Step 2: Import Controls via REST API

Use the ServiceNow Table API to bulk-import controls from the CERG machine-readable manifest:

```bash
# Authenticate to ServiceNow
export SN_INSTANCE="your-instance"
export SN_USER="admin"
export SN_PASS="your-password"

# Import controls from machine-readable manifest
curl -s -u "$SN_USER:$SN_PASS"   -H "Content-Type: application/json"   "https://$SN_INSTANCE.service-now.com/api/now/table/sn_compliance_control"   -X POST -d @cerg-controls.json
```

The expected JSON format for each control:

```json
{
  "number": "AC-001",
  "name": "Account Lifecycle Management",
  "description": "Every account has an approved request, named owner, defined access level, and documented JML record.",
  "category": "Access Control",
  "framework": "CERG 100-Core",
  "frequency": "Continuous",
  "evidence_type": "JML log, quarterly recert report",
  "owning_pillar": "Engineering",
  "system_applicability": "Hardware, Software, Network, Cloud, Data, Process"
}
```

### 1.3 Evidence Automation

ServiceNow GRC integrates with the evidence layer through **Indicator Templates**. Each control gets an indicator that defines what evidence looks like.

#### Configuration Steps

1. Navigate to **Policy and Compliance > Administration > Indicator Templates**
2. For each control in the CERG baseline, create an indicator template:
   - **Name:** `CERG-{Control ID}-{Evidence Type}`
   - **Type:** Manual (MSP collects and uploads) or Automated (API integration)
   - **Frequency:** Per control spec (Continuous, Quarterly, Annual)
   - **Required attachments:** Named evidence artifact from control spec

#### Automated Evidence Examples

| Integration | Control IDs Covered | Evidence |
|-------------|-------------------|----------|
| SentinelOne → ServiceNow | AC-003, SI-003, SI-004 | Agent deployment report, detection coverage |
| Wiz → ServiceNow | CA-007, CM-008, CM-009 | CSPM findings, configuration drift |
| Okta → ServiceNow | AC-002, AC-006, IA-002 | MFA enrollment, access recertification |
| Tenable → ServiceNow | RA-005, CM-010, SI-002 | Vulnerability scan results, remediation status |
| Veeam → ServiceNow | CP-009, CP-010 | Backup success/failure, immutability status |

### 1.4 Audit Reporting

#### Quarterly Compliance Dashboard

Create a dashboard in **Performance Analytics** with these widgets:

1. **Control Compliance by Family** — bar chart showing % implemented per NIST family
2. **Evidence Currency** — pie chart: Current / Expiring (30d) / Lapsed
3. **Risk Register Heatmap** — inherent vs residual risk for accepted findings
4. **Open POA&M Items** — count and aging of planned controls
5. **Inheritance Status** — controls marked Inherited with current attestation vs expired

### 1.5 MSP Multi-Tenancy

ServiceNow supports MSP multi-tenancy via **Domain Separation**. Each client gets a domain with isolated controls, evidence, and audit data.

```bash
# Create a new client domain
curl -s -u "$SN_USER:$SN_PASS"   -H "Content-Type: application/json"   "https://$SN_INSTANCE.service-now.com/api/now/table/sys_domain"   -X POST -d '{
    "name": "ClientName_Domain",
    "parent": "global",
    "description": "CERG client: ClientName"
  }'
```

Each domain inherits the CERG 100-Core framework definition from global but maintains its own control statuses, evidence, and audit artifacts.

---

## Path 2: Vanta (SMB)

### 2.1 Prerequisites

- Vanta account with admin access
- Client's cloud and identity providers connected (AWS, Azure, GCP, M365, Okta, etc.)
- CERG control mapping spreadsheet

### 2.2 Control Mapping

Vanta doesn't support custom frameworks natively, but you can map CERG controls to Vanta's built-in framework tests.

#### Approach: CERG-to-SOC2 Mapping

Vanta's strongest automation is SOC 2. Map CERG controls to SOC 2 Trust Services Criteria to get automated evidence collection:

| CERG Control Family | SOC 2 TSC | Vanta Automation |
|---------------------|-----------|------------------|
| Access Control (AC) | Security — Logical Access | Automated via IdP integration |
| Audit & Accountability (AU) | Security — Monitoring | Cloud log ingestion |
| Configuration Management (CM) | Security — Change Management | Cloud CSPM |
| Identification & Authentication (IA) | Security — Logical Access | MFA enforcement via IdP |
| System Integrity (SI) | Security — System Operations | Agent-based monitoring |
| Risk Assessment (RA) | Security — Risk Assessment | Manual with Vanta risk register |

For controls without SOC 2 equivalents (OT, CUI, BES overlays), use Vanta's manual tests with documented collection procedures.

### 2.3 Evidence Collection

Vanta's agent automatically collects evidence from:
- Cloud providers (AWS, Azure, GCP) — configuration, IAM, logging
- Identity providers (Okta, Entra ID, Google Workspace) — MFA, access, accounts
- Endpoint management (Jamf, Intune, Kandji) — device posture
- HRIS (BambooHR, Rippling, Gusto) — personnel controls
- Code repositories (GitHub, GitLab) — SDLC controls

For evidence Vanta can't auto-collect (OT systems, physical controls, custom applications), document the collection procedure in the [MSP Runbook](../msp-runbook-v1.md).

### 2.4 MSP Multi-Client with Vanta

Vanta's partner program supports multi-client management:

1. **Vanta Partner Portal** — centralized view of all client instances
2. **Template frameworks** — push your CERG mapping template to new clients
3. **Automated evidence collection** — per-client agent deployment
4. **Quarterly review cadence** — Vanta prompts for recertification

Limitations: Vanta's partner reporting is not as robust as ServiceNow's domain separation. No cross-client risk aggregation. Each client is a separate instance.

---

## Path Decision Guide

| Factor | ServiceNow GRC | Vanta |
|--------|---------------|-------|
| **Client size** | 50+ employees | Under 50 employees |
| **Budget** | $50k-150k/yr | $10k-30k/yr |
| **Compliance scope** | CMMC L2, SOX, PCI, NERC-CIP | SOC 2, ISO 27001, HIPAA |
| **Custom controls** | Full support | Mapped to built-in frameworks |
| **Multi-tenancy** | Domain separation | Partner portal |
| **Evidence automation** | API integrations + manual | Agent-based + cloud connectors |
| **Operational integration** | Incident, Change, CMDB linked | Compliance-only |
| **Engineering effort** | Moderate (import + configure) | Low (connect + map) |
| **CERG alignment** | Full — CERG-native controls | Partial — mapped via SOC 2 |

---

## Document Control

### Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-03 | cragin-security | Initial release |

### Related Documents

- [Opinionated Tool Matrix](opinionated-tool-matrix-v1.md)
- [MSP Runbook](../msp-runbook-v1.md)
- [CERG 100-Core Control Baseline](../../governance/CERG-GOV-CB-002_100-Core_Control_Baseline.md)
