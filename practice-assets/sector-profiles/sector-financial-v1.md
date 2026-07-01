# Sector Threat Profile: Financial Services

**Sector:** Banking, Insurance, FinTech, Payments, Wealth Management
**Threat intel source:** Real incidents (2025-2026 campaigns)
**Last updated:** 2026-07

---

## Top Attack Scenarios

### Scenario 1: AI-Enabled Wire Fraud / Payment Redirection

**Attack chain:**
```
Deepfake CEO voice → Call to treasury department → Urgent wire transfer authorization →
Funds sent to attacker-controlled account → $25M+ loss before detection
```

**Real intel:** Financial app attacks up 38% in 2026. AI-generated deepfake voice and video used in wire fraud campaigns. 76% increase in finance-sector incidents Q1 2026 vs Q1 2025.

**CB-001 controls activated:**
- **AC-4** (Least Privilege) — Payment approval requires two-person authorization
- **IA-1** (MFA) — Out-of-band verification for high-value transactions
- **AT-2** (Training) — Treasury staff deepfake awareness training
- **AU-9** (Non-Repudiation) — Session recording for payment systems

**Detection (Sentinel):**
```kusto
// Unusual payment activity: amount > threshold OR time outside business hours
PaymentLogs | where Amount > 100000 or hourofday(Timestamp) < 6 or hourofday(Timestamp) > 20
| where ApprovalMethod != "out_of_band_verified"
| project Timestamp, Requestor, Amount, Beneficiary, ApprovalMethod
```

**Tabletop:**
- Inject: "Your CEO calls the treasury manager and authorizes an urgent $15M wire to a new vendor for an acquisition. The voice sounds exactly like the CEO."
- Questions: What verification step catches this? Who has authority to override? What's the recovery process for fraudulently transferred funds?

### Scenario 2: Mobile Banking Credential Harvesting (MFA Bypass)

**Attack chain:**
```
SMS phishing → Fake banking app login page → Real-time credential harvesting →
Token interception → Account takeover → Funds transfer
```

**Real intel:** Phishing and ransomware attacks targeting banks increased 520% from 2020 baseline. Mobile banking trojans now include AITM (adversary-in-the-middle) functionality to bypass MFA.

**CB-001 controls:**
- **IA-1** (MFA) — FIDO2 passkeys over SMS/OTP
- **AT-1** (Training) — Customer phishing awareness
- **SI-3** (Anti-Phishing) — DMARC enforcement + brand impersonation detection
- **AC-7** (Mobile) — MAM policies for banking apps

**Detection:**
```kusto
// Impossible travel on banking app logins
SigninLogs | where AppId == "BankingApp" | summarize Locations = make_set(LocationDetails) by UserPrincipalName, bin(TimeGenerated, 1h) | where array_length(Locations) > 1
```

### Scenario 3: Cloud Bank Infrastructure Compromise

**Attack chain:**
```
CI/CD pipeline compromise → Access to payment processing server → Modified transaction routing →
Funds redirected to attacker accounts over 72 hours
```

**Real intel:** Shai Hulud operation (June 2026): CI/CD credentials used to access Redshift databases and exfiltrate financial data to attacker-controlled storage.

---

## Testing Procedures

| Scenario | Procedure | Frequency |
|----------|-----------|-----------|
| 1 (Wire fraud) | Tabletop: inject deepfake CEO call, walk through verification | Quarterly |
| 2 (Mobile harvesting) | Simulated phishing + MFA bypass test on test accounts | Monthly |
| 3 (Cloud infra) | CI/CD compromise simulation + lateral movement detection | Annual |

---

## Regulatory Overlay

| Regulation | Critical Controls | Evidence |
|------------|------------------|----------|
| SOX ITGC (404) | AC-1/2/3/4, AU-1/2/3, CM-1/2 | Access reviews, audit logs, change management |
| PCI DSS | AC-1-7, IA-1, RA-2, AU-1-4, SI-1-3 | QSA evidence package, ASV scan |
| NYDFS 500 | All controls (banking specific) | Annual certification, incident reporting |
| FFIEC CAT | Risk-based controls | Maturity assessment |

---

## Tool Stack Preference

| Category | Primary | Rationale |
|----------|---------|-----------|
| SIEM | Splunk + Sentinel | Regulated banks need Splunk breadth; cloud native needs Sentinel |
| EDR | SentinelOne | Autonomous rollback for ransomware |
| IAM | Okta + Entra PIM | Multi-IdP for acquisitions/heterogeneous |
| PAM | CyberArk | Session recording for SOX-relevant admin actions |
| GRC | ServiceNow (enterprise) / OneTrust (mid) | SOX audit management, evidence collection |
