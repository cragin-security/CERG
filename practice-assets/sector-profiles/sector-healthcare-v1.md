# Sector Threat Profile: Healthcare

**Sector:** Healthcare (Hospitals, Health Systems, Pharma, HealthTech)
**Threat intel source:** Real incidents (Change Healthcare 2024, 2025-2026 campaigns)
**Last updated:** 2026-07

---

## Top Attack Scenarios

### Scenario 1: Ransomware via Third-Party Pharmacy/Payment Processor (Change Healthcare Model)

**Attack chain:**
```
Third-party vendor compromise → Lateral movement to core clinical systems →
Ransomware encryption of patient data → Disruption of pharmacy, billing, clinical ops →
National-scale patient care disruption
```

**Real impact:** Change Healthcare attack (Feb 2024) disrupted 100M+ patient records, halted pharmacy operations nationwide, cost $2.3B in recovery. Healthcare is 17% of all ransomware (2026).

**CB-001 controls activated:**
- **SA-2** (Supply Chain Integrity) — Vendor SBOMs, assessment before integration
- **IR-2** (Incident Detection) — Detection of cross-org lateral movement
- **CP-1** (Backup) — Immutable backups for clinical systems
- **SC-1** (Segmentation) — Vendor systems isolated from clinical

**Detection (Sentinel):**
```kusto
// Lateral movement from vendor network to clinical
DeviceNetworkEvents | where RemoteIP !in~ (VendorAllowedRanges)
| where LocalIP in~ (ClinicalSubnets) | project Timestamp, DeviceName, RemoteIP, ProcessName
```

**Tabletop:**
- Inject: "Your pharmacy benefits processor reports a ransomware infection. All claims processing via that vendor has stopped. Patients cannot fill prescriptions."
- Questions: How long before clinical impact? Who notifies patients? What's the backup processing path? Regulatory reporting obligations per HIPAA?

### Scenario 2: Phishing → Credential Theft → EHR Access (CL-STA-1062 Campaign)

**Attack chain:**
```
Targeted phishing to clinical staff → Credential theft → MFA bypass via token harvesting →
Access to EHR system → Patient record exfiltration
```

**Real intel:** CL-STA-1062 APT group targeting SE Asian healthcare (2026). MFA bypass via AITM phishing kits becoming standard in healthcare attacks.

**CB-001 controls:**
- **IA-1** (MFA) — Phishing-resistant MFA (FIDO2) for EHR access
- **AT-2** (Training) — Clinical staff phishing simulations (target <3% click rate)
- **SI-3** (Anti-Phishing) — DMARC enforcement + phishing link detonation
- **PS-3** (Insider Threat) — Unusual EHR query volume after-hours

**Detection:**
```kusto
// Unusual EHR query volume (potential exfiltration)
EhrAuditLog | where TimeGenerated > ago(24h)
| summarize RecordCount = count() by UserPrincipalName, HourOfDay = hourofday(TimeGenerated)
| where HourOfDay < 6 or HourOfDay > 20
| where RecordCount > 100
```

### Scenario 3: Medical Device Network Compromise (DICOM/RADIOLOGY)

**Attack chain:**
```
Internet-exposed DICOM viewer (OHIF) → Exploitation of unpatched medical imaging software →
Lateral movement from imaging network to hospital IT network
```

**Real intel:** CISA advisory June 2026 — OHIF DICOM Viewer, pydicom/pynetdicom libraries both had critical vulns. Medical imaging devices notoriously unpatched.

**CB-001 controls:**
- **RA-2** (Vulnerability Scanning) — Passive scanning for medical devices
- **CM-3** (Drift Detection) — FIM on medical device configurations
- **SC-1** (Segmentation) — Imaging network isolated from EHR/clinical

---

## Testing Procedures

| Scenario | Procedure | Frequency |
|----------|-----------|-----------|
| 1 (Third-party ransomware) | Tabletop: inject vendor compromise, walk through clinical disruption response | Annual |
| 2 (Phishing to EHR exfil) | Simulated phishing + credential harvesting test | Quarterly |
| 3 (Medical device vuln) | Passive vulnerability scan of all IP-connected medical devices | Monthly |

---

## Regulatory Overlay

| Regulation | Critical Controls | Evidence Required |
|------------|------------------|-------------------|
| HIPAA Security Rule | AC-2, AC-3, IA-1, AU-1, AU-2, RA-2, RA-3, SI-1, SI-2 | Risk assessment, access logs, audit controls |
| PCI DSS (if billing) | AC-1 through AC-7, IA-1, RA-2, AU-1 through AU-4 | Quarterly scan, MFA evidence, access reviews |
| HITRUST | All 99 controls (tiered by maturity level) | Full evidence package per control |

---

## Tool Stack Preference

| Category | Primary | Rationale |
|----------|---------|-----------|
| EDR | SentinelOne | Medical device support, passive mode for OT-adjacent |
| SIEM | Microsoft Sentinel | M365/Azure dominance in healthcare; HIPAALog connectors |
| Segmentation | Cloudflare Zero Trust + VLAN | Isolate imaging/IoT without agents |
| Backup | Veeam + immutable storage | Ransomware recovery for clinical systems |
