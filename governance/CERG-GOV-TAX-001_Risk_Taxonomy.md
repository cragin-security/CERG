
## 22 Control Areas Mapped to Security Risks: All Pillars · All Severity Levels

> **How to read this document:** Each control area is mapped to the specific risk it prevents and how it differs from similar-looking controls. Where controls address overlapping threat categories, the nuance column explains the distinct failure mode each one guards against.

---
| | |
|---|---|
| **Document ID** | CERG-GOV-TAX-001 |
| **Version** | 1.21 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Risk Pillar Leader |
| **Parent Policy** | [`CERG-POL-001`](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on framework or organizational change |
| **Frameworks** | NIST CSF 2.0 (IDENTIFY); ISO/IEC 27001 A.5, A.8; NIST SP 800-53r5 RA-3, RA-5, RA-7 |
| **Regulations** | Cross-cutting |
| **Environments** | All in-scope: IT, OT, Cloud |

---

## Theme 1 - Visibility: knowing what you own and what's happening

### 1.1 Know what you own: maintain an authoritative asset inventory

**Pillar:** Engineering | **Severity:** Critical

**Risk prevented:** Shadow IT and unmanaged attack surface. Assets you don't know exist can't be patched, monitored, or protected. Attackers routinely compromise forgotten systems, decommissioned servers, unregistered OT devices, contractor-managed endpoints, because they appear on no one's radar.

**Nuance vs. similar controls:** The OT dimension is distinct from IT: an unregistered BES Cyber System isn't just an unpatched box, it's a potential NERC-CIP CIP-002 violation that could affect grid reliability and trigger enforcement. The risk isn't just exploitation; it's an invisible compliance gap and an unreported reliability asset.

---

### 1.2 Monitor threats continuously: detect what vulnerability scans miss

**Pillar:** Risk | **Severity:** Critical

**Risk prevented:** Undetected intrusion and dwell time. Vulnerability scans find known weaknesses at a point in time. Continuous monitoring catches active adversary behavior, lateral movement, credential misuse, anomalous data flows, that scans never see. The longer dwell time, the greater the blast radius.

**Nuance vs. similar controls:** In OT environments, a missed intrusion isn't just a data breach, it's potential manipulation of physical processes. A compromised SCADA workstation detected at 30 days dwell looks entirely different from one detected at 6 months. The monitoring gap directly determines whether an incident stays contained or becomes an operational emergency.

---

### 1.3 Assess your own security posture: periodic internal evaluation

**Pillar:** Risk | **Severity:** High

**Risk prevented:** Unknown control failures and compliance drift. Controls degrade. Configurations change. People leave. Periodic self-assessment catches the gap between what the policy says and what is actually happening in the environment, before a regulator or adversary does.

**Nuance vs. similar controls:** Where continuous monitoring catches active threats, self-assessment catches structural drift, a firewall rule opened for a project that was never closed, an access review that stopped happening when the person who ran it departed. The risk here is systemic erosion, not a single event.

---

## Theme 2 - Identity: controlling who gets in and what they can do

### 2.1 Control who can access what: enforce least privilege

**Pillar:** Engineering | **Severity:** Critical

**Risk prevented:** Over-privileged accounts as a force multiplier for attackers. When a compromised account has access to everything, attackers move laterally without needing to escalate. Least privilege limits the blast radius, an attacker operating within one account's permissions can only reach what that account can reach.

**Nuance vs. similar controls:** Least privilege is architectural risk reduction, not detective. It doesn't stop the initial compromise, it limits what an attacker can do afterward. The absence of least privilege transforms every phishing success into a potential enterprise-wide breach. In OT environments, over-privileged accounts can reach control systems that have no detective controls to catch misuse.

---

### 2.2 Authenticate users and systems: verify identity before granting access

**Pillar:** Engineering | **Severity:** Critical

**Risk prevented:** Credential-based attacks and identity fraud. Weak or absent authentication is the entry point for most breaches, password spray, credential stuffing, phishing for MFA bypass, default credentials on OT devices. Authentication failure means the attacker is inside and appears legitimate.

**Nuance vs. similar controls:** Authentication and least privilege are often confused. Authentication is the gate, does this person or system prove who they are? Least privilege is what happens after the gate. A strong authentication control with excessive permissions still produces a high-impact breach. A well-scoped account with weak authentication is still easily compromised. Both must be present.

---

### 2.3 Manage accounts throughout their lifecycle: provisioning through termination

**Pillar:** Engineering | **Severity:** High

**Risk prevented:** Orphaned credentials and insider threat via ghost accounts. Accounts not deprovisioned on departure become permanent backdoors, accessible to the former employee, to anyone who later obtains those credentials, or to attackers who enumerate inactive accounts. Provisioning failures (over-granting at hire) compound over time as roles change.

**Nuance vs. similar controls:** Lifecycle management addresses a temporal risk that point-in-time authentication and access controls miss entirely. An account that was appropriate at hire may become a critical violation 18 months later after a role change. The specific failure mode is stale privilege accumulation, a risk that grows invisibly over time rather than from a single event.

---

### 2.4 Control and log privileged/remote access: know who did what, when

**Pillar:** Engineering | **Severity:** High

**Risk prevented:** Undetectable abuse of elevated permissions and remote sessions. Privileged access, local admin, domain admin, root, OT engineer credentials, is the primary target for attackers post-compromise. Without logging and session controls, privileged misuse (insider or external) is invisible and unattributable.

**Nuance vs. similar controls:** This control addresses accountability and forensics, not prevention. Least privilege reduces what privileged accounts can reach; logging makes their actions visible afterward. The risk is not just breach, it's breach without attribution, which makes incident response impossible and regulatory reporting inaccurate. CIP-005 R2 treats unlogged remote access to BES systems as a reportable violation regardless of whether misuse occurred.

---

## Theme 3 - Hardening: reducing the attack surface of systems themselves

### 3.1 Harden systems: remove what isn't needed, lock down what is

**Pillar:** Engineering | **Severity:** High

**Risk prevented:** Unnecessary services and default configurations as entry points. Default credentials, open ports serving unused protocols, and unneeded services are free entry points for attackers. System hardening eliminates the attack surface that was never needed in the first place.

**Nuance vs. similar controls:** Hardening is permanent risk reduction through design, distinct from patching (which addresses known vulnerabilities in needed software). An unneeded service running an unpatched protocol is doubly exposed, it wouldn't be exploitable at all if the service were disabled. In OT environments, CIP-007 R1 makes unnecessary ports and services a compliance finding independent of whether any vulnerability exists in them.

---

### 3.2 Segment networks: limit lateral movement and blast radius

**Pillar:** Engineering | **Severity:** Critical

**Risk prevented:** Unconstrained lateral movement enabling enterprise-wide compromise. Flat networks allow an attacker who compromises one endpoint to reach everything. Segmentation is the primary architectural control that limits an intrusion to the segment where it began.

**Nuance vs. similar controls:** Segmentation and hardening both reduce attack surface, but at different layers. Hardening reduces what an attacker can exploit on a single system. Segmentation limits where an attacker can go after they've exploited it. For OT environments, the consequence is not just data loss, a flat IT/OT network means a ransomware event that begins in enterprise IT can reach operational control systems. CIP-005 ESP requirements exist because this failure mode affects grid reliability, not just data confidentiality.

---

### 3.3 Manage configuration changes: track drift, prevent unauthorized changes

**Pillar:** Engineering | **Severity:** High

**Risk prevented:** Configuration drift creating exploitable vulnerabilities and undetected tampering. Systems drift from their secure baselines over time, through patches, updates, human error, and deliberate tampering. Unauthorized configuration changes are a primary persistence technique for advanced attackers.

**Nuance vs. similar controls:** Configuration management addresses a risk that hardening alone cannot, an initially hardened system that drifts back to an insecure state. The distinct risk here is change without authorization: an attacker who modifies a firewall rule or disables a logging agent has bypassed your controls without exploiting a CVE. [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) treats unauthorized changes to financial systems as a control failure independent of any security event.

---

### 3.4 Protect data in transit and at rest: encryption as a baseline control

**Pillar:** Engineering | **Severity:** High

**Risk prevented:** Data interception, exfiltration, and regulatory exposure for unprotected sensitive data. Unencrypted data in transit is readable by anyone on the network path. Unencrypted data at rest is readable by anyone with storage access. For CUI and BCSI, unencrypted data is a compliance violation independent of whether it was accessed.

**Nuance vs. similar controls:** Encryption is a last-resort control, it assumes the perimeter has already failed and the data has been accessed. Its value is that even with access, the data is useless without the key. The OT-specific nuance: CIP-011 applies to BES Cyber System Information, not to operational data flows, protecting the documentation and configuration of grid systems, not the operational telemetry itself.

---

## Theme 4 - Exposure management: finding and fixing weaknesses before attackers do

### 4.1 Identify and remediate known vulnerabilities on a defined schedule

**Pillar:** Risk | **Severity:** Critical

**Risk prevented:** Known, exploitable vulnerabilities providing attackers a reliable entry point. The majority of successful breaches exploit known vulnerabilities for which patches exist. An unpatched CVE with a public exploit is a guaranteed entry point given sufficient attacker persistence.

**Nuance vs. similar controls:** Exposure management in OT is categorically different from IT. A CVSS 9.x vulnerability in an enterprise server gets patched within 35 days. The same severity finding in a BES relay management workstation may require vendor testing before any patch can be applied, introducing a compliance tension between CIP-007-6 patch timelines and operational safety requirements. The risk calculus shifts: patching too fast can introduce reliability risk; patching too slow creates security and compliance exposure.

---

### 4.2 Conduct adversarial testing: find what scanners miss

**Pillar:** Risk | **Severity:** High

**Risk prevented:** Logic vulnerabilities, misconfigurations, and chained attack paths that automated scanning cannot find. Automated vulnerability scans find known CVEs. Penetration testing finds the things that have no CVE, overly permissive trust relationships, weak segmentation that passes a scan but fails under an active attack, authentication bypasses that require human ingenuity to construct.

**Nuance vs. similar controls:** This is distinct from exposure management in both what it finds and what it validates. Exposure management confirms known weaknesses. Adversarial testing confirms that your controls actually work under adversarial conditions, that your network segmentation stops a real attacker, not just a scan. Segmentation testing validates that sensitive environments are actually isolated, not just documented.

---

## Theme 5 - Third-party and supply chain risk: extending controls beyond the perimeter

### 5.1 Manage vendor and third-party risk: extend controls beyond the perimeter

**Pillar:** Risk | **Severity:** High

**Risk prevented:** Trusted third-party access as a vector for breach and data exposure. Third parties with legitimate access to your environment are a primary attack vector, through their compromised credentials, their compromised infrastructure, or malicious code in their products. The SolarWinds supply chain attack demonstrated that even trusted, certified vendors can be weaponized.

**Nuance vs. similar controls:** Vendor risk has two distinct threat models that require different controls. Access-based risk (the vendor has credentials or a connection into your environment) is addressed through access controls and remote access logging. Software supply chain risk (the vendor's product contains malicious or vulnerable code) is addressed through CIP-013 supply chain risk management controls and software integrity verification. These require different assessment frameworks, a vendor questionnaire doesn't catch a compromised software build pipeline.

---

## Theme 6 - Governance: the operating framework that makes everything else consistent

### 6.1 Write and maintain policies: define what good looks like

**Pillar:** Governance | **Severity:** High

**Risk prevented:** Inconsistent security decisions and unenforceable standards without written policy. Without documented policy, security decisions are made ad hoc, varying by person, by team, and by pressure. You cannot hold anyone accountable to a standard that was never written down, and regulators will cite the absence of policy as a standalone finding.

**Nuance vs. similar controls:** Policy risk is distinct from technical control risk. A technically hardened system with no supporting policy has no mechanism for ensuring that hardening is maintained, that exceptions are managed, or that new systems are hardened to the same standard. Policy failure doesn't cause a breach directly, it causes the conditions under which breaches happen systematically rather than occasionally.

---

### 6.2 Train and background-check personnel with access to sensitive systems

**Pillar:** Governance | **Severity:** High

**Risk prevented:** Insider threat enablement and human error as the leading breach vector. Untrained personnel make security decisions without understanding consequences, clicking phishing links, misconfiguring systems, sharing credentials. Unvetted personnel with privileged access represent an unquantified insider threat. CIP-004 treats unvetted access to BES Cyber Systems as a reportable violation.

**Nuance vs. similar controls:** Training and background checks address different threat profiles within the personnel risk category. Training reduces unintentional insider risk, the well-meaning employee who makes a dangerous mistake. Background checks address intentional insider risk, the person who should not have been granted access in the first place. Both are required; neither substitutes for the other.

---

### 6.3 Manage risk formally: document, accept, or treat identified risks

**Pillar:** Governance | **Severity:** High

**Risk prevented:** Untracked risk accumulation and accountability gaps when controls fail. Risks that are not formally documented tend to be informally ignored. When an accepted risk materializes into an incident, the absence of a documented risk decision means no one is accountable, no compensating controls were required, and there is no audit trail to demonstrate that the risk was understood.

**Nuance vs. similar controls:** Risk management is not the same as exposure management. Exposure management tracks technical findings in systems. Risk management tracks organizational decisions, the choice to accept a finding, the compensating controls committed to in exchange for that acceptance, and the timeline for eventual remediation. The regulatory exposure for unmanaged risk is the absence of documented decisions, not the existence of vulnerabilities.

---

### 6.4 Collect, protect, and retain audit evidence: prove controls are working

**Pillar:** Governance | **Severity:** High

**Risk prevented:** Inability to demonstrate control effectiveness, triggering regulatory findings and enforcement. A control that cannot be evidenced is treated as a control that does not exist by regulators and auditors. Evidence loss or gaps, whether from poor retention practices or from failure to collect in the first place, can convert a security success into a compliance failure.

**Nuance vs. similar controls:** Evidence risk is bureaucratic, not technical. You can have a fully functioning security program that fails an audit because no one collected the records proving it functioned. The distinct failure mode: a pre-audit scramble to reconstruct evidence often produces incomplete or inconsistent records that create more questions than they answer. NERC-CIP evidence retention is explicitly tiered by standard and requirement, loss of required evidence is itself a potential violation.

---

### 6.5 Define and enforce a compliance calendar: no surprises at audit time

**Pillar:** Governance | **Severity:** Medium

**Risk prevented:** Missed regulatory deadlines and last-minute compliance failures under time pressure. Compliance obligations have hard deadlines, annual NERC-CIP evidence reviews, C3PAO assessment cycles, [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC audit milestones. Organizations that don't track these systematically miss them, producing findings that would have been preventable with basic operational discipline.

**Nuance vs. similar controls:** The calendar is a meta-control, it doesn't prevent any specific attack, but its absence causes compliance failures across every framework simultaneously. A missed [SOX](https://www.govinfo.gov/app/details/PLAW-107publ204) ITGC audit milestone is a different risk than a missed annual NERC-CIP vulnerability assessment: one creates financial-control audit exposure, the other can produce an enforcement notice. The calendar ensures the right activity reaches the right people with sufficient lead time to actually happen.

---

### 6.6 Plan and practice incident response: know what to do before it happens

**Pillar:** Governance | **Severity:** Critical

**Risk prevented:** Chaotic, slow, or incorrect response that amplifies breach impact. Untested incident response plans fail under the stress of an actual incident, people don't know their roles, communications break down, regulatory notification timelines are missed. The incident itself may be unavoidable; poor response execution is not.

**Nuance vs. similar controls:** IR planning and IR execution are different risks. An untested plan is a documented assumption, it may be entirely wrong about how an incident actually unfolds. CIP-008 makes the gap concrete: a utility that experiences a reportable cybersecurity incident without a tested, compliant IR plan faces both the incident impact and an enforcement action for the plan failure. The NERC regulatory notification clock starts running whether or not the utility is ready.

---

### 6.7 Manage recovery: restore operations and capture lessons learned

**Pillar:** Governance | **Severity:** Critical

**Risk prevented:** Extended outages and repeated incidents from failure to restore and learn. Recovery capability determines how long an organization remains impaired after a significant event. For BES environments, extended recovery directly translates to grid reliability risk. Absent lessons learned, the same vulnerability or process failure recurs.

**Nuance vs. similar controls:** Recovery risk is often treated as identical to IR risk, but they address different phases. IR is about containing and investigating; recovery is about restoring operations safely. CIP-009 is notably prescriptive about testing cadence specifically because restoration of a BES Cyber System that fails introduces its own reliability risk. The lesson-learned function is what converts a security incident into a permanent improvement, its absence means incidents are events rather than inputs.

---

### 6.8 Protect physical access to critical systems: cyber starts at the door

**Pillar:** Governance | **Severity:** High

**Risk prevented:** Physical bypass of all logical controls. An attacker with physical access to a system can bypass authentication, install hardware implants, exfiltrate data directly, and destroy equipment, all without triggering a single network-based alert. Physical security is the control that all cyber controls depend on.

**Nuance vs. similar controls:** CIP-006 is unique in treating physical access to BES Cyber Systems as a distinct compliance requirement, not because physical threats are new, but because the consequence of physical compromise to a substation or control center is a reliability event, not just a data breach.

---

## Quick Reference: Severity Summary

|Severity|Control Areas|
|---|---|
|**Critical**|Asset inventory · Threat monitoring · Least privilege · Authentication · Network segmentation · Exposure management · IR planning · Recovery|
|**High**|Self-assessment · Account lifecycle · Privileged access logging · System hardening · Config change management · Encryption · Adversarial testing · Vendor risk · Policy & standards · Personnel training · Risk management · Audit evidence · Physical security|
|**Medium**|Compliance calendar|

---

## Quick Reference: Pillar Summary

|Pillar|Control Areas Owned|
|---|---|
|**Engineering**|Asset inventory · Least privilege · Authentication · Account lifecycle · Privileged access logging · System hardening · Network segmentation · Config change management · Encryption|
|**Risk**|Threat monitoring · Self-assessment · Exposure management · Adversarial testing · Vendor risk|
|**Governance**|IR planning · Recovery · Physical security · Policy & standards · Personnel training · Risk management · Audit evidence · Compliance calendar|

---

---

## Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-GOV-TAX-001 |
| **Version** | 1.21 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Risk Pillar Leader |
| **Parent Policy** | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on framework or organizational change |
| **Next Scheduled Review** | 2027-05-01 |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-05-01 | Cyber Risk | Initial release. Risk taxonomy with categories, definitions, and control mappings. |
| 1.21 | 2026-05-22 | Cyber Risk | Updated category definitions and regulatory mappings. |

### Review Triggers

- New regulatory framework affecting risk categories
- Material change to organizational scope or structure
- Direction from the CISO

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [CERG-POL-001](CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Risk Register and Exception Process | [CERG-PRC-RM-001](../procedures/CERG-PRC-RM-001_Risk_Register_and_Exception_Process.md) | Uses taxonomy for risk categorization |
| Document Catalog | [CERG-GOV-CAT-001](CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Master document inventory |
