## ENDPOINT AND MOBILE SECURITY STANDARD
### Endpoint Protection · EDR · Device Posture · Mobile Device Management · BYOD

---

| | |
|---|---|
| **Document ID** | CERG-STD-EP-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader (Endpoint) |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Supporting Standards** | [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) · [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) · [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) · [`CERG-STD-NET-001`](CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md) · [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) · [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) |
| **Review Cycle** | Annual / On material change to the endpoint or mobility estate |
| **Frameworks** | [NIST 800-53r5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) (CM, SI, AC families) · [NIST 800-124](https://csrc.nist.gov/pubs/sp/800/124/r2/final) (mobile device security) · [CIS Controls v8](https://www.cisecurity.org/controls) (Controls 1, 4, 10) · [NIST CSF 2.0](https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final) (PROTECT) |
| **Regulations** | CMMC L2 / 800-171r3 (3.1.x, 3.4.x, 3.14.x) · NERC-CIP (Transient Cyber Assets) · SOX ITGC |
| **Environments** | All CERG-managed endpoints and mobile devices: owned, corporate, and BYOD with access to in-scope resources |

---

## Table of Contents

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Principles](#2-principles)
3. [Endpoint Classes](#3-endpoint-classes)
4. [Baseline Endpoint Protection](#4-baseline-endpoint-protection)
5. [Endpoint Detection and Response](#5-endpoint-detection-and-response)
6. [Device Posture](#6-device-posture)
7. [Mobile Device Management](#7-mobile-device-management)
8. [Bring Your Own Device](#8-bring-your-own-device)
9. [Transient and Removable Devices](#9-transient-and-removable-devices)
10. [Roles and Responsibilities](#10-roles-and-responsibilities)
11. [Regulatory and Framework Alignment Summary](#11-regulatory-and-framework-alignment-summary)
12. [Document Control](#12-document-control)

---

## 1. Purpose and Scope

The endpoint is where the user meets the estate, and where most intrusions begin. A phishing click, a malicious document, a compromised laptop: the endpoint is the first system an attacker touches and the device from which they reach everything else. The Secure Configuration Baseline Standard hardens endpoints; the Access Management Standard governs who signs in. Neither owns the endpoint as a security surface in its own right. This standard does.

This standard establishes the requirements for endpoint and mobile device security across CERG-managed environments: baseline endpoint protection, endpoint detection and response, the device posture signal other standards depend on, mobile device management, and the terms under which a personally owned device may access in-scope resources.

It applies to every endpoint and mobile device that accesses in-scope resources: owned workstations and laptops, corporate mobile devices, and personally owned devices used under the bring-your-own-device terms in Section 8.

> **The Endpoint Posture Signal Is Used Everywhere**
>
> This standard does more than protect laptops. It produces the device posture signal that the Network Security Standard consumes for zero-trust access decisions, that the Access Management Standard consumes for conditional access, and that remote access depends on. An endpoint estate with no reliable posture signal forces every other standard to fall back to trusting the network or the password alone. Endpoint security is a supplier to the rest of the program, not just a protector of devices.

---

## 2. Principles

1. **Every endpoint is managed or it has no access.** A device that accesses in-scope resources is enrolled in management and meets this standard, or it does not get access. There is no unmanaged-but-trusted category.
2. **The endpoint is inventoried.** Every endpoint is an asset in the inventory governed by [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md). An endpoint not in the inventory is an unmanaged asset and is contained.
3. **Posture is checked, not assumed.** A device's compliance with this standard is verified continuously and at the point of access, not assumed because the device was compliant once.
4. **Protect, detect, and respond on the device.** Endpoints carry preventive controls and a detection-and-response capability. Prevention fails; the endpoint must also be a place where compromise is seen and contained.
5. **BYOD is a deliberate, bounded decision.** Personal devices may access in-scope resources only under explicit terms that bound what they reach and what the organization controls. BYOD is never the absence of a rule.
6. **Loss of a device is not loss of the data.** Endpoint data is encrypted and remotely recoverable or erasable, so a lost or stolen device is an inconvenience, not a breach.

---

## 3. Endpoint Classes

| **Class** | **What It Covers** | **Management Model** |
|---|---|---|
| **Workstation** | Owned desktops and laptops used for daily work. | Fully managed; full baseline. |
| **Corporate mobile** | Organization-owned phones and tablets. | Fully managed via mobile device management (Section 7). |
| **BYOD** | Personally owned devices accessing in-scope resources. | Bounded management of organization data only (Section 8). |
| **Privileged-access endpoint** | Endpoints used for administrative access to infrastructure. | Fully managed; hardened beyond baseline; see Section 4.5. |
| **Transient and removable** | Devices that connect briefly: contractor laptops, removable media, maintenance devices. | Controlled per Section 9. |

OT field devices and OT engineering workstations are governed by [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md), not this standard. Where an OT engineering workstation is also a transient cyber asset, Section 9 and the OT standard are read together.

---

## 4. Baseline Endpoint Protection

Every managed endpoint carries the following at minimum.

1. **Secure configuration baseline.** The endpoint is configured to the applicable baseline in [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md), and configuration drift is detected and corrected.
2. **Disk encryption.** Endpoint storage is encrypted at rest per [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md). Encryption is enforced by management, not left to the user.
3. **Patching.** The operating system and installed software are patched against the SLAs in [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md). The endpoint reports its patch state to management.
4. **Malware protection.** The endpoint runs current malware protection.
5. **Host firewall.** A host-based firewall is enabled and configured to default-deny inbound, consistent with [`CERG-STD-NET-001`](CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md).
6. **Application control.** Tier-appropriate control over what software may execute. Privileged-access endpoints (Section 4.5) and endpoints handling regulated data enforce allowlisting; standard workstations enforce at minimum a block on known-bad and unsigned execution.
7. **Screen lock and authentication.** The endpoint enforces an automatic screen lock and authenticates the user per [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md).
8. **Local administrative rights are restricted.** Users do not hold standing local administrator rights on their workstations. Where elevation is needed it is granted just in time and recorded.

### 4.1 Privileged-Access Endpoints

An endpoint used to administer infrastructure is a high-value target and is hardened beyond the baseline: application allowlisting is mandatory, the device is dedicated to administrative use and not used for email or general browsing, and it is segmented per [`CERG-STD-NET-001`](CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md). Administering the estate from a general-purpose daily-use laptop is prohibited.

> **Standing Local Admin Rights Are a Self-Inflicted Wound**
>
> When every user is a local administrator of their own machine, every phishing click runs with administrative privilege, every piece of malware installs cleanly, and the endpoint's own controls can be disabled by the very user the controls protect. Removing standing local admin rights is one of the highest-value, lowest-cost endpoint controls in existence. CERG mandates it, and grants elevation just in time when a genuine need arises.

---

## 5. Endpoint Detection and Response

1. **Every managed endpoint runs EDR.** An endpoint detection and response capability runs on every workstation, corporate mobile device where supported, and privileged-access endpoint.
2. **EDR telemetry reaches the detection platform.** EDR telemetry is delivered to the platform governed by [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md), so endpoint events are visible alongside the rest of the estate.
3. **EDR supports containment.** The capability allows a compromised endpoint to be isolated from the network quickly, so a foothold can be contained without physically retrieving the device.
4. **EDR tampering is itself an alert.** An attempt to disable, uninstall, or evade EDR is a detection signal and is alerted on.
5. **CERG feeds, the IR team responds.** Consistent with [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) §3.4, CERG operates the EDR capability and feeds its telemetry and detections to the standing Incident Response team. CERG does not run incident response from this standard.

---

## 6. Device Posture

Device posture is the set of facts about an endpoint that other standards use to make access decisions. This standard owns producing it.

1. **Posture is defined.** A device is in posture when it is enrolled in management, on a supported and patched operating system, encrypted, running current EDR and malware protection, and not flagged with an unresolved high-severity finding.
2. **Posture is evaluated continuously and at access.** Posture is checked continuously by management and again at the point a device requests access to a resource.
3. **Out-of-posture devices lose access.** A device that falls out of posture loses access to in-scope resources until it is brought back into posture. The loss of access is automatic, not a manual follow-up.
4. **Posture is the signal other standards consume.** The posture verdict is the input that [`CERG-STD-NET-001`](CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md) uses for zero-trust decisions and that [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) uses for conditional access. This standard is the authoritative producer of that signal.

---

## 7. Mobile Device Management

1. **Corporate mobile devices are enrolled in mobile device management.** Organization-owned phones and tablets are managed: configuration is enforced, security policy is pushed, and compliance is reported.
2. **Mobile baseline.** A managed mobile device enforces device encryption, a passcode or biometric unlock, automatic lock, current operating system, and a block on installing applications from untrusted sources.
3. **Organization data is containerized.** Organization email, files, and applications on a mobile device are held in a managed container separable from anything personal on the device.
4. **Remote lock and wipe.** A managed mobile device can be remotely locked and can have organization data remotely wiped. A lost corporate device is wiped.
5. **Jailbroken and rooted devices are blocked.** A device whose operating system integrity has been compromised does not access in-scope resources.

---

## 8. Bring Your Own Device

BYOD is permitted only under the explicit terms in this section. An organization adopting CERG may decline BYOD entirely; if it permits BYOD, these terms apply.

1. **BYOD access is enrolled and bounded.** A personal device accessing in-scope resources is enrolled in management scoped to organization data only. The organization manages its container; it does not manage the user's personal device.
2. **The managed container is the boundary.** Organization email, files, and applications live in a managed, encrypted container. Organization data does not leave the container onto the personal device.
3. **Posture still applies.** A BYOD device meets the device posture definition in Section 6 for the managed container. An out-of-posture personal device loses access exactly as a corporate device does.
4. **Selective wipe, not full wipe.** The organization can wipe the managed container, removing organization data without touching the user's personal content. Offboarding a user or losing the device triggers a container wipe.
5. **What BYOD may not reach.** Personal devices do not reach privileged administrative interfaces, OT systems, or, unless an explicit risk acceptance is recorded, regulated data scopes such as CUI. Administrative and regulated access is from managed, organization-owned endpoints.
6. **The terms are agreed in writing.** A user using BYOD acknowledges the terms: the managed container, the organization's right to wipe it, and the posture requirements. BYOD without recorded user agreement is not permitted.

> **BYOD Is a Trade, and the Trade Is Written Down**
>
> Bring-your-own-device trades convenience for a controlled reduction in assurance. That trade is acceptable when it is bounded and explicit, and dangerous when it is silent. The failure mode is the personal phone quietly syncing the entire mailbox with no container, no posture check, and no way to wipe it when the employee leaves. CERG permits BYOD only as a written, bounded arrangement: a managed container, a posture requirement, a selective-wipe right, and a clear list of what personal devices may never reach.

---

## 9. Transient and Removable Devices

1. **Transient devices are controlled before they connect.** A device that connects briefly to the estate, a contractor laptop, a maintenance device, is checked for posture before connection or is restricted to an isolated network segment per [`CERG-STD-NET-001`](CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md).
2. **Removable media is controlled.** Use of removable storage is restricted by default. Where permitted, removable media is encrypted and scanned. Endpoints handling regulated data block removable storage unless an exception is recorded.
3. **Transient cyber assets in OT scope.** A transient device connecting to OT, including for maintenance, is a transient cyber asset and is governed by [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) and NERC-CIP requirements. Section 9 and the OT standard are read together for those devices.

---

## 10. Roles and Responsibilities

Roles below are the canonical role names from [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) §6.1.

| **Role** | **Endpoint and Mobile Responsibility** |
|---|---|
| **Endpoint Engineer** | Owns this standard. Owns endpoint and mobile baselines, the management and EDR platforms, and the device posture signal. |
| **Engineering Pillar Leader** | Accountable for endpoint security across the pillar; approves BYOD terms and privileged-access endpoint design. |
| **Identity Engineer** | Consumes the posture signal for conditional access; owns just-in-time elevation of local administrative rights. |
| **Detection Engineer** | Owns endpoint detection content; consumes EDR telemetry. |
| **OT Security Engineer** | Owns transient cyber asset control where devices connect to OT. |
| **Exposure Management Lead** | Tracks endpoint patch state and endpoint vulnerability findings against SLAs. |
| **Vendor Risk Analyst** | Coordinates transient contractor-device access with [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md). |
| **Governance Pillar Leader** | Tracks endpoint-management coverage metrics and BYOD exceptions; cross-references this standard with the control baseline. |
| **Policy & Standards Manager** | Maintains this document, its version, and its review cycle. |

---

## 11. Regulatory and Framework Alignment Summary

| **Regulation / Framework** | **Reference** | **Where in This Standard** |
|---|---|---|
| NIST 800-53r5 | CM-7, SI-3, SI-4, AC-6, AC-19, MP-7 | Sections 4, 5, 8, 9 |
| NIST 800-124 | Mobile device security and management | Sections 7, 8 |
| CIS Controls v8 | Control 1 (assets), Control 4 (secure configuration), Control 10 (malware defenses) | Sections 3, 4, 5 |
| NIST CSF 2.0 | PROTECT (PR.PS, PR.AA), DETECT (DE.CM) | Sections 4, 5, 6 |
| NIST 800-171r3 / CMMC L2 | 3.1.x (access), 3.4.x (configuration), 3.14.x (system integrity), 3.8.x (media) | Sections 4, 8, 9 |
| NERC-CIP | CIP-010 Transient Cyber Assets and Removable Media | Section 9 |
| SOX ITGC | Endpoint access and configuration control | Sections 4, 6 |

---

## 12. Document Control

| Field | Value |
|---|---|
| **Document ID** | CERG-STD-EP-001 |
| **Version** | 1.0 |
| **Status** | Approved |
| **Effective Date** | 2026-05-21 |
| **Classification** | Public |
| **Owner** | Engineering Pillar Leader (Endpoint) |
| **Approved By** | CISO |
| **Parent Policy** | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) - Cybersecurity Policy |
| **Review Cycle** | Annual; and on material change to the endpoint or mobility estate |
| **Next Scheduled Review** | 2027-05-21 |
| **Frameworks** | NIST 800-53r5 (CM, SI, AC); NIST 800-124; CIS Controls v8 (1, 4, 10); NIST CSF 2.0 (PROTECT) |
| **Regulations** | CMMC L2 / 800-171r3; NERC-CIP (Transient Cyber Assets); SOX ITGC |
| **Environments** | All CERG-managed endpoints and mobile devices |

### Revision History

| **Version** | **Date** | **Author** | **Change Summary** |
|---|---|---|---|
| 1.0 | 2026-05-21 | Cyber Engineering | Initial release. Establishes endpoint classes, baseline endpoint protection including removal of standing local administrator rights, endpoint detection and response, the device posture signal consumed by the network and access standards, mobile device management, bounded bring-your-own-device terms, and control of transient and removable devices. |

### Review Triggers

- Material change to the endpoint estate, mobility model, or BYOD policy
- Revision of NIST 800-124 or relevant NIST 800-53 controls
- A significant endpoint-originated security incident
- Internal audit or regulatory finding affecting endpoint security
- Direction from the CISO

Cyber Engineering owns this document. The Engineering Pillar Leader (Endpoint) is responsible for initiating reviews, managing the revision cycle, and obtaining Governance Pillar Leader approval, with CISO endorsement, for all changes.

### Related Documents

| **Document** | **ID** | **Relationship** |
|---|---|---|
| Cybersecurity Policy | [`CERG-POL-001`](../governance/CERG-POL-001_Cybersecurity_Policy.md) | Parent policy |
| Secure Configuration Baseline Standard (DISH) | [`CERG-STD-CFG-001`](CERG-STD-CFG-001_Secure_Configuration_Baseline_Standard_DISH.md) | Endpoint configuration baselines |
| Access Management Standard | [`CERG-STD-AC-001`](CERG-STD-AC-001_Access_Management_Standard.md) | Conditional access consuming device posture; just-in-time elevation |
| Asset Management and Inventory Standard | [`CERG-STD-AM-001`](CERG-STD-AM-001_Asset_Management_and_Inventory_Standard.md) | Endpoints as inventoried assets |
| Network Security and Segmentation Standard | [`CERG-STD-NET-001`](CERG-STD-NET-001_Network_Security_and_Segmentation_Standard.md) | Zero-trust decisions consuming device posture; transient-device segmentation |
| Cryptography and Key Management Standard | [`CERG-STD-CR-001`](CERG-STD-CR-001_Cryptography_and_Key_Management_Standard.md) | Endpoint disk encryption |
| Logging, Monitoring, and Detection Standard | [`CERG-STD-LM-001`](CERG-STD-LM-001_Logging_Monitoring_and_Detection_Standard.md) | EDR telemetry and endpoint detection content |
| Grid Control Systems Security Standard | [`CERG-STD-OT-001`](CERG-STD-OT-001_Grid_Control_Systems_Security_Standard.md) | OT devices and transient cyber assets |
| Exposure Management Procedure | [`CERG-PRC-VM-001`](../procedures/CERG-PRC-VM-001_Exposure_Management_Procedure.md) | Endpoint patching SLAs |
| Third-Party and Supply Chain Risk Procedure | [`CERG-PRC-TPRM-001`](../procedures/CERG-PRC-TPRM-001_Third_Party_and_Supply_Chain_Risk_Procedure.md) | Contractor transient devices |
| Operating Model | [`CERG-GOV-OM-001`](../governance/CERG-GOV-OM-001_CERG_Operating_Model.md) | CERG feeds EDR telemetry; the IR team responds |
| Document Catalog and Naming Convention | [`CERG-GOV-CAT-001`](../governance/CERG-GOV-CAT-001_Document_Catalog_and_Naming_Convention.md) | Registers this artifact and the `EP` domain |
