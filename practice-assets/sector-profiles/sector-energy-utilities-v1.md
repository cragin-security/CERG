# Sector Threat Profile: Energy & Utilities (OT/ICS)

**Sector:** Electric Utilities, Oil & Gas, Water/Wastewater, Grid Operations
**Threat intel source:** CISA ICS advisories, real incidents (2025-2026)
**Last updated:** 2026-07

---

## Top Attack Scenarios

### Scenario 1: ICS Protocol Exploitation via IT/OT Pivot (CISA-Advised)

**Attack chain:**
```
Phishing email to IT helpdesk → Credential theft → Pivot from IT to OT network →
Exploitation of Schneider/GE/Yokogawa controller → Loss of view → Manual shutdown required
```

**Real intel:** June 25, 2026 — 7 concurrent CISA ICS advisories (Schneider PowerLogic, Yokogawa FAST/TOOLS, Horner Cscape, EVoke EV Charging). Poland energy sector incident (Feb 2026) caused loss of view and control between facilities and distribution operators. Nation-state actors targeting OT at scale.

**CB-001 controls activated:**
- **SC-1** (Network Segmentation) — IT/OT separation per Purdue Model; jump host for OT access
- **IA-1** (MFA) — MFA on all OT jump host access
- **RA-2** (Vulnerability Scanning) — Passive-only scanning for OT; no active probes
- **RA-3** (Remediation) — OT-specific SLA: Critical=30 days with vendor-coordinated patch window

**Detection:**
```kusto
// Unusual OT protocol traffic on IT-monitored interfaces
CommonSecurityLog | where Protocol in~ ("modbus", "dnp3", "iec104", "s7comm")
| where DeviceVendor !in~ ("Schneider", "Siemens", "Rockwell")
| project TimeGenerated, SourceIP, DestinationIP, Protocol
```

**Tabletop:**
- Inject: "You receive a CISA advisory for a critical vulnerability in your distribution management system (Yokogaga FAST/TOOLS). There is no patch. Your grid operator says they cannot take the system offline."
- Questions: How do you assess risk without a patch? What compensating controls apply? Who authorizes continued operation? How do you monitor for exploitation?

### Scenario 2: EV Charging Infrastructure Attack (EV Charging System Exploit)

**Attack chain:**
```
Internet-exposed EV charging management system → Remote code execution (EVoke advisory) →
Grid-side connection manipulation → Load balancing disruption
```

**Real intel:** CISA advisory June 2026 for EVoke Charging Station Management System. EV infrastructure is increasingly targeted as grid-connected assets become more prevalent.

**CB-001 controls:**
- **SC-4** (DoS Protection) — Rate limiting, grid-edge device isolation
- **CM-3** (Drift Detection) — Configuration monitoring on all EV management systems
- **AC-8** (Session Lock) — Short session timeouts on EV management consoles

### Scenario 3: Ransomware Affecting OT Visibility

**Attack chain:**
```
Ransomware on IT domain → Domain controller compromise → OT historian exposed via trusted link →
OT historian encrypted → Grid operators lose visibility → Manual operations required
```

**Real intel:** Colonial Pipeline demonstrated the IT-to-OT ransomware cascade was not isolated. 2026 OT security report shows 50% of OT environments have only partial visibility.

---

## Testing Procedures

| Scenario | Procedure | Frequency |
|----------|-----------|-----------|
| 1 (ICS protocol exploit) | Purple team: simulate IT-to-OT pivot exploiting an unpatched controller | Annual |
| 2 (EV charging) | External scan of EV management interfaces + exploit attempt against test system | Quarterly |
| 3 (OT ransomware) | Tabletop: inject IT ransomware that spreads to OT historian | Annual |

---

## OT Vulnerability SLA Matrix

| Severity | IT SLA | OT SLA | Exception Path |
|----------|--------|--------|----------------|
| Critical | 7 days | 30 days (with vendor coordination) | Engineering + OT lead approval |
| High | 30 days | 90 days | Documented compensating controls |
| Medium | 90 days | 120 days | Risk register entry |

---

## Regulatory Overlay

| Regulation | Critical Controls | Evidence |
|------------|------------------|----------|
| NERC CIP | AC-1-7, IA-1, RA-2, AU-1-4, CM-1-4, CP-1-6, IR-1-3, PE-1-3 | CIP evidence package, 15-month audit cycle |
| ISA/IEC 62443 | Segmentation, secure remote access, patch management | Zone/conduit model evidence |
| DOE C2M2 | Maturity-based controls | Self-assessment scorecard |

---

## Tool Stack Preference

| Category | Primary | Rationale |
|----------|---------|-----------|
| OT Scanning | Nozomi / Claroty (passive) | Active scanning can disrupt OT; passive only |
| Network | Palo Alto OT firewall | Deep packet inspection of ICS protocols |
| SIEM | Splunk | Broad OT log source compatibility |
| Vulnerability | Qualys (OT module) | Agentless, passive OT scanning support |
